#!/usr/bin/env python3
"""build_web.py — 把三书 Markdown 构建成丛书静态阅读站（site/）。

站是一套丛书，不是一本书：首页是丛书总览，每本书有自己的目录、封面与
身份，进入任一本后可连续阅读，跨书引用直接跳书内页，不落 GitHub。

设计：
- 三书结构同构：章节/附录/模板同处书根，靠文件名前缀区分；
- 阅读顺序取自各书目录（TAM/SA 为 00-outline.md，BTE 为 plan-outline.md），
  目录没列到的文件按编号归入对应部分，不静默丢弃；
- pandoc (gfm) 渲染正文，Python 做链接 .md→.html 改写、表格包裹、
  配图转 figure、标题锚点编号、搜索索引与页面组装；
- 链接键空间为「书键:书内路径」，跨书链接 ../the-sa-book/x.md 解析为 sa:x.md；
  仓库内其他文件压平渲染到 site/ext/；
- 产物 shared/dist/site/，不入库。

用法：
    python3 shared/tooling/build_web.py            构建
    python3 shared/tooling/build_web.py --serve    构建后起本地预览（默认 8765）
    python3 shared/tooling/build_web.py --check    只构建并校验站内链接
"""
from __future__ import annotations

import html as html_mod
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]           # 仓库根（脚本在 shared/tooling/）
WEB = REPO / "shared" / "tooling"                    # 构建资源与脚本同处
SITE = REPO / "shared" / "dist" / "site"              # 构建产物统一到共用 shared/dist/
GH_BLOB = "https://github.com/allengaller/the-iron-triangle/blob/main"

ZH = re.compile(r"[一-鿿]")
DIATAXIS = re.compile(r"Diátaxis:\s*([A-Za-z-]+)")
H1_RE = re.compile(r"^#\s+(.+)$", re.M)
MD_HREF = re.compile(r'href="([^"]+\.md)(#[^"]*)?"')
MD_LINK = re.compile(r"\]\(([^)\s]+\.md)(#[^)]*)?\)")
FILE_RE = re.compile(
    r"(?:ch\d+|appx-|tpl-|00-|99-|front-|back-|plan-|map-|DIATAXIS|README|CHANGELOG)[\w.-]*\.md")
CH_NUM = re.compile(r"第\s*(\d+)\+?\s*章")
CH_RANGE = re.compile(r"第\s*(\d+)\s*[–—\-~至到]\s*(\d+)\s*章")
APPX_LET = re.compile(r"附录\s*([A-Z]{1,2})(?![\w])")
TPL_NUM = re.compile(r"模板\s*(\d+)")
# 只有这几种 ## 是结构性的「篇」；其余是目录的元信息小节
PART_HEAD = re.compile(r"^(前置页|书末|附录|模板|正文|第[一二三四五六七八九十]+部分)")

# 书的身份写在这里，不写进正文：角色定位来自三书承诺链，稳定不变；
# 卷面文案与缺件由构建实测，不手写。
BOOKS: list["Book"] = []


@dataclass
class Book:
    key: str          # 站内路径前缀
    dir: str          # books/ 下目录名
    outline: str      # 目录唯一事实源
    seal: str         # 顶栏方形徽记
    en: str
    zh: str
    role: str         # 承诺链角色：设计/证明/兑现
    scope: str
    order: list[tuple[str, str]] = field(default_factory=list)   # [(rel, part)]
    parts: list[str] = field(default_factory=list)
    missing: list[tuple[str, str]] = field(default_factory=list)
    info: dict[str, dict] = field(default_factory=dict)
    stats: dict[str, int] = field(default_factory=dict)

    @property
    def root(self) -> Path:
        return REPO / "books" / self.dir


def make_books() -> list[Book]:
    return [
        Book(key="tam", dir="the-tam-book", outline="00-outline.md", seal="TAM",
             en="The TAM Book of AI Era", zh="AI 时代的 TAM 白皮书",
             role="兑现承诺", scope="交付、服务治理、风险兜底、续约扩容"),
        Book(key="sa", dir="the-sa-book", outline="00-outline.md", seal="SA",
             en="The SA Book of AI Era", zh="AI 时代的售前架构师白皮书",
             role="证明承诺", scope="需求洞察、方案工程、竞争、投标、承诺边界"),
        Book(key="bte", dir="the-bte-book", outline="plan-outline.md", seal="BTE",
             en="The BTE Book of AI Era", zh="AI 时代的技术销售白皮书",
             role="设计承诺", scope="商机判断、决策链、价值证明、商业结构、谈判签约"),
    ]


# ---------------------------------------------------------------- 通用

def zh_count(text: str) -> int:
    return len(ZH.findall(text))


def short_title(t: str) -> str:
    return re.sub(r"^(第\s*\d+\+?\s*章[\s　]+|附录\s*[A-Z]{1,2}[\s　]+|模板\s*\d+[\s　]+)", "", t.strip()).strip()


def split_prefix(t: str) -> tuple[str, str]:
    """返回 (编号, 去前缀标题)。编号用于排序与部分归属。"""
    pats = (
        (r"第\s*(\d+)\+?\s*章[\s　]+(.+)$", "ch"),
        (r"附录\s*([A-Z]{1,2})[\s　]+(.+)$", "appx"),
        (r"模板\s*(\d+)[\s　]+(.+)$", "tpl"),
    )
    for pat, _kind in pats:
        m = re.match(pat, t.strip())
        if m:
            return m.group(1), m.group(2)
    return "", t.strip()


def split_kind(t: str) -> tuple[str, str, str]:
    """返回 (kind, 编号, 标题)：kind ∈ ch/appx/tpl/''。"""
    pats = (
        (r"第\s*(\d+)\+?\s*章[\s　]+(.+)$", "ch"),
        (r"附录\s*([A-Z]{1,2})[\s　]+(.+)$", "appx"),
        (r"模板\s*(\d+)[\s　]+(.+)$", "tpl"),
    )
    for pat, kind in pats:
        m = re.match(pat, t.strip())
        if m:
            return kind, m.group(1), m.group(2)
    return "", "", t.strip()


def clean_part(p: str) -> str:
    """「第一部分　定位篇：TAM 是谁」→「定位篇：TAM 是谁」，侧栏分组头不重复编号。"""
    return re.sub(r"^第[一二三四五六七八九十]+部分[\s　]+", "", p.strip()) or p.strip()


def book_path(book: Book, rel: str) -> str:
    return f"{book.key}/{Path(rel).with_suffix('.html').as_posix()}"


def ext_out(rel_repo: str) -> str:
    """站外文件在 site/ext/ 下的输出名。同名文件用路径前缀消歧。"""
    p = Path(rel_repo)
    stem = p.stem
    if stem.upper() in {"README", "CHANGELOG", "LICENSE"}:
        stem = rel_repo[: -len(".md")].replace("/", "-")
    return f"ext/{stem}.html"


# ---------------------------------------------------------------- 目录

def parse_outline(book: Book) -> None:
    """按 outline 定顺序，未列出的文件按前缀归位；缺件登记不静默。

    outline 的 ## 只认真正的篇名（前置页/第 N 部分/附录/书末）。其他 ## 是
    「命名与别名」「配套文档」这类元信息小节，不能当篇，否则侧栏会出现
    只有一两行的碎组。这些小节里列到的文件名交给前缀规则归位。
    """
    text = (book.root / book.outline).read_text(encoding="utf-8")
    seen: set[str] = set()
    part = "前置页"
    meta_section = False
    book.parts = [part]
    numpart: dict[tuple[str, str], str] = {}

    def add(rel: str) -> None:
        """记一笔已见；元信息小节里列到的文件不进 order，留给 place() 按前缀归位。"""
        if rel in seen:
            return
        seen.add(rel)
        if not meta_section:
            book.order.append((rel, part))

    for line in text.splitlines():
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            raw = m.group(1).strip()
            # 先拿原始标题判篇（「第X部分」要在剥前缀前认），再存剥过的篇名
            meta_section = not PART_HEAD.match(raw)
            if not meta_section:
                part = clean_part(raw)
                if part not in book.parts:
                    book.parts.append(part)
            continue
        # 文件名有两种写法：Markdown 链接，或行内代码里的裸文件名。
        # 带 / 的是跨书或仓库路径，交给链接解析，不算本书目录条目。
        for mm in re.finditer(r"\]\(([^)\s#]+\.md)(?:#[^)]*)?\)", line):
            href = mm.group(1)
            if "/" in href or href.startswith(("http", "#")):
                continue
            if (book.root / href).is_file():
                add(href)
            elif (href, part) not in book.missing:
                book.missing.append((href, part))
        for token in re.findall(r"`([\w.-]+\.md)`", line):
            if (book.root / token).is_file():
                add(token)
        # 编号→部分：先剥掉链接目标，避免把跨书引用的「附录 V」记成本书。
        # 元信息小节（「对标 TAM 第 5 章」之类）不参与，否则会把本书前几章拉进前置页。
        if not meta_section:
            plain = re.sub(r"\]\([^)]*\)", "]", line)
            for mm in CH_RANGE.finditer(plain):
                for n in range(int(mm.group(1)), int(mm.group(2)) + 1):
                    numpart.setdefault(("ch", str(n)), part)
            for mm in CH_NUM.finditer(plain):
                numpart.setdefault(("ch", mm.group(1)), part)
            for mm in APPX_LET.finditer(plain):
                numpart.setdefault(("appx", mm.group(1)), part)
            for mm in TPL_NUM.finditer(plain):
                numpart.setdefault(("tpl", str(int(mm.group(1)))), part)

    # 目录页本身是「总目录」，排在书首：封面与各章的「总目录」入口必须能打开
    if (book.root / book.outline).is_file() and book.outline not in seen:
        book.order.insert(0, (book.outline, "前置页"))
        seen.add(book.outline)

    def place(rel: str) -> str:
        """未在篇内列出的文件：先按编号找篇，再按文件名前缀找，最后进书末。"""
        h1m = H1_RE.search((book.root / rel).read_text(encoding="utf-8"))
        kind, no, _ = split_kind(h1m.group(1).strip() if h1m else rel)
        fm = re.match(r"(ch|appx|tpl)-(\w+)", rel)
        if not kind and fm:
            # SA 模板 H1 写作「SA-01 方案建议书」，编号只在文件名里
            kind, no = fm.group(1), fm.group(2)
            no = str(int(no)) if kind == "tpl" and no.isdigit() else no.upper()
        if kind:
            # 附录与模板全归各自篇，不按编号散落：正文章节里偶尔提到「附录 E」，
            # 那是交叉引用，不是它所在的位置。
            if kind == "appx" and "附录" in book.parts:
                return "附录"
            if kind == "tpl":
                hit = next((p for p in book.parts if "模板" in p or "工具箱" in p), None)
                if hit:
                    return hit
            hit = numpart.get((kind, no))
            if hit:
                return hit
            if kind == "tpl":
                return "模板与清单"
            if kind == "appx":
                return "附录" if "附录" in book.parts else "书末"
            if kind == "ch" and no.isdigit():
                # 实战章常与主章同号（ch05-technical-depth / ch05-practical），目录只列主章；
                # 按章号就近隶到已在目录里的章所在篇，避免掉进书末。
                near = [(abs(int(re.match(r"ch(\d+)", r).group(1)) - int(no)), p)
                        for r, p in book.order if re.match(r"ch\d+", r)]
                if near:
                    return min(near)[1]
        if rel.startswith(("front-", "00-", "plan-")) or rel in ("README.md", "CHANGELOG.md"):
            return "前置页"
        return "书末"

    # 本书全部 md：outline 没列到的按前缀归位，归不进去的收进「书末」
    listed = set(seen)
    already = {rel for rel, _ in book.order}
    rest_by_part: dict[str, list[str]] = {}
    for f in sorted(book.root.glob("*.md")):
        rel = f.name
        if rel in already:
            continue
        rest_by_part.setdefault(place(rel), []).append(rel)
    for p in rest_by_part:
        if p not in book.parts:
            book.parts.append(p)

    merged: list[tuple[str, str]] = []
    for p in book.parts:
        # 同一篇的目录条目与补录条目合在一起，不拆成两个同名分组
        merged.extend((rel, part) for rel, part in book.order if part == p)
        merged.extend((rel, p) for rel in rest_by_part.get(p, []))
    got = {rel for rel, _ in merged}
    merged.extend((rel, part) for rel, part in book.order if rel not in got)
    book.order = merged

    unknown = [rel for rel, _ in book.order if rel not in listed]
    book.stats["unlisted"] = len(unknown)
    book.stats["unlisted_files"] = unknown


def missing_parts(book: Book) -> list[str]:
    """前置件与索引的缺件清单。不靠目录，直接看磁盘：目录没写不等于文件不在。"""
    have = {f.name for f in book.root.glob("*.md")}
    checks = (
        ("卷首页（前言或版本声明）", ("00-preface.md", "front-preface.md",
                                    "00-front-matter.md", "front-matter.md")),
        ("阅读导读", ("00-reading-guide.md", "front-reading-guide.md")),
        ("索引页", ("99-index.md",)),
        ("术语表", ("appx-a-glossary.md",)),
    )
    out = [label for label, names in checks if not any(n in have for n in names)]
    if not any(n.startswith("appx-") for n in have):
        out.append("附录体系")
    return out


def build_info(book: Book) -> None:
    for rel, part in book.order:
        text = (book.root / rel).read_text(encoding="utf-8")
        h1m = H1_RE.search(text)
        h1 = h1m.group(1).strip() if h1m else rel
        g = DIATAXIS.search(text[:600])
        no, clean = split_prefix(h1)
        book.info[rel] = {
            "out": book_path(book, rel), "part": part, "h1": h1, "clean": clean, "no": no,
            "genre": g.group(1) if g else "", "short": short_title(h1),
            "zh": zh_count(text), "text": text,
        }
        if rel == book.outline:
            # 目录页的 H1 是书名，直接拿来当标题会与封面重复；侧栏与页头统一显示「总目录」
            book.info[rel].update({"no": "", "clean": "总目录", "short": "总目录",
                                   "genre": "Reference"})
    book.stats.update({
        "pages": len(book.order),
        "chapters": sum(1 for f in book.root.glob("ch*.md")),
        "appendices": sum(1 for f in book.root.glob("appx-*.md")),
        "templates": sum(1 for f in book.root.glob("tpl-*.md")),
        "words": sum(d["zh"] for d in book.info.values()),
    })


# ---------------------------------------------------------------- 渲染

def pandoc(md_text: str) -> str:
    return subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none"],
        input=md_text, capture_output=True, text=True, check=True,
    ).stdout


def wrap_tables(fragment: str) -> str:
    fragment = fragment.replace("<table>", '<div class="tw" tabindex="0"><table>')
    fragment = fragment.replace("</table>", "</table></div>")
    def fig(m: re.Match) -> str:
        attrs = m.group(1)
        am = re.search(r'alt="([^"]*)"', attrs)
        alt = html_mod.escape(am.group(1)) if am else ""
        cap = f"<figcaption>{alt}</figcaption>" if alt else ""
        return f"<figure><img {attrs}/>{cap}</figure>"
    fragment = re.sub(r"<p>\s*<img\s+([^>]+?)\s*/?>\s*</p>", fig, fragment)
    fragment = re.sub(r'<a href="(https?://[^"]+)"', r'<a target="_blank" rel="noopener" href="\1"', fragment)
    return fragment


def assign_ids(fragment: str) -> tuple[str, list[tuple[str, str, str]]]:
    """给 h2/h3 分配稳定锚点 id，按小节切分返回 (html, [(id, 标题, 正文)])。"""
    parts = re.split(r"(<h[23][^>]*>.*?</h[23]>)", fragment, flags=re.S)
    out: list[str] = []
    sections: list[tuple[str, str, str]] = []
    cur_id, cur_h, buf = "", "", ""
    n = 0
    for p in parts:
        m = re.match(r"<h([23])[^>]*>(.*?)</h\1>", p, flags=re.S)
        if m:
            if cur_h or buf.strip():
                sections.append((cur_id, cur_h, buf))
            n += 1
            cur_id, cur_h, buf = f"s{n}", re.sub(r"<[^>]+>", "", m.group(2)).strip(), ""
            out.append(f'<h{m.group(1)} id="{cur_id}">{m.group(2)}</h{m.group(1)}>')
        else:
            buf += p
            out.append(p)
    if cur_h or buf.strip():
        sections.append((cur_id, cur_h, buf))
    return "".join(out), sections


# ---------------------------------------------------------------- 链接

def to_key(abs_t: Path, books: list[Book]) -> str:
    """绝对路径 → 链接键：tam:ch01-x.md / sa:ch09-x.md / @ext:shared/00-citation.md。"""
    try:
        rel = os.path.relpath(abs_t, REPO).replace(os.sep, "/")
    except ValueError:
        return ""
    if rel.startswith(".."):
        return ""
    if rel.startswith("books/"):
        parts = rel.split("/")
        if len(parts) >= 3:
            for b in books:
                if parts[1] == b.dir:
                    return f"{b.key}:" + "/".join(parts[2:])
        return ""
    return "@ext:" + rel


def out_of(key: str, books: list[Book]) -> str:
    if key.startswith("@ext:"):
        return ext_out(key[len("@ext:"):])
    bkey, _, rel = key.partition(":")
    return f"{bkey}/{Path(rel).with_suffix('.html').as_posix()}"


def collect_targets(books: list[Book]) -> dict[str, str]:
    """规划全部 .md 链接目标的站内渲染位。键 → 相对 site/ 的 html 路径。"""
    targets: dict[str, str] = {}
    for b in books:
        for rel, _ in b.order:
            targets[f"{b.key}:{rel}"] = book_path(b, rel)
    if "tam:README.md" in targets:
        pass

    def scan(src: Path) -> None:
        text = src.read_text(encoding="utf-8")
        for href in MD_LINK.findall(text):
            abs_t = Path(os.path.normpath(os.path.join(src.parent, href[0])))
            if not abs_t.is_file():
                continue
            key = to_key(abs_t.resolve(), books)
            if key and (not key.startswith("@ext:")
                       or abs_t.parent in (REPO, REPO / "shared")):
                targets.setdefault(key, out_of(key, books))

    for b in books:
        for rel, _ in b.order:
            scan(b.root / rel)
    # 书稿公用卷（shared/00-*.md）是三书的读者入口，只把 top-level 的 00-*.md 成页。
    # 子目录（governance/、review/、standards/）是证据与产线，不进阅读站，
    # 它们的链接由 rewrite_links 兜底指向 GitHub。
    for f in sorted((REPO / "shared").glob("00-*.md")):
        scan(f)
    # 丛书首页与页脚引用的仓库文档：不论书稿是否引到，都固定成页
    for rel in ("README.md", "CONTRIBUTING.md", "shared/00-reading-status.md",
                "shared/00-citation.md", "shared/00-copyright-and-license.md",
                "shared/00-commitment-chain.md", "shared/00-disclaimer-and-anonymization.md"):
        if (REPO / rel).is_file():
            targets.setdefault("@ext:" + rel, ext_out(rel))
    return targets


def rewrite_links(fragment: str, src_dir: Path, site_of: dict[str, str],
                  out_dir: str, books: list[Book]) -> tuple[str, list[str]]:
    """把片段中的 .md 链接改写为站内 .html。src_dir = 源文件所在目录（绝对路径）。"""
    unresolved: list[str] = []

    def link(m: re.Match) -> str:
        href, frag = m.group(1), m.group(2) or ""
        abs_t = Path(os.path.normpath(os.path.join(src_dir, href)))
        target = abs_t.resolve() if abs_t.exists() else abs_t
        key = to_key(target, books)
        if key and key in site_of:
            return f'href="{os.path.relpath(site_of[key], out_dir or ".")}{frag}"'
        if key and key.startswith("@ext:") and key in site_of:
            return f'href="{os.path.relpath(site_of[key], out_dir or ".")}{frag}"'
        # 仓库内存在的文件但未单独成页：直接用 GitHub 绝对链接，避免站内 .md 断链
        if abs_t.is_file():
            try:
                rel = os.path.relpath(abs_t, REPO).replace(os.sep, "/")
            except ValueError:
                rel = ""
            if rel and not rel.startswith(".."):
                return f'href="{GH_BLOB}/{rel}{frag}"'
        unresolved.append(f"{href}（相对 {src_dir.name}）")
        return m.group(0)

    fragment = MD_HREF.sub(link, fragment)
    # LICENSE 是仓库根的非 md 文件，指向它的链接统一落到站根副本
    def lic(m: re.Match) -> str:
        href = m.group(1)
        abs_t = os.path.normpath(os.path.join(src_dir, href))
        if abs_t != str(REPO / "LICENSE"):
            return m.group(0)
        return f'href="{os.path.relpath(SITE / "LICENSE", SITE / out_dir if out_dir else SITE)}"'
    fragment = re.sub(r'href="([^"]*LICENSE)"', lic, fragment)
    # 目录与二进制资源（shared/figures/、shared/review/…）不进站，指向 GitHub 对应页
    def other(m: re.Match) -> str:
        href = m.group(1)
        if href.startswith(("http", "mailto:", "data:", "#", "javascript:")):
            return m.group(0)
        base, _, frag = href.partition("#")
        if not base or base.lower().endswith(".md"):
            return m.group(0)
        abs_t = Path(os.path.normpath(os.path.join(src_dir, base)))
        try:
            rel = os.path.relpath(abs_t, REPO).replace(os.sep, "/")
        except ValueError:
            return m.group(0)
        if rel.startswith("..") or not abs_t.exists():
            return m.group(0)
        kind = "tree" if abs_t.is_dir() else "blob"
        tail = f"#{frag}" if frag else ""
        return f'href="https://github.com/allengaller/the-iron-triangle/{kind}/main/{rel}{tail}"'
    fragment = re.sub(r'href="([^"]+)"', other, fragment)
    # 图源在 shared/figures/，站点内平铺为 figures/，剥掉越出站点根的前缀
    fragment = re.sub(r'src="(?:\.\./)+shared/figures/', 'src="{{ROOT}}figures/', fragment)
    return fragment, unresolved


# ---------------------------------------------------------------- 页面

def build_sidebar(book: Book, root: str, cur: str) -> str:
    out = ['<div class="search-wrap"><input id="search-input" type="search" '
           'placeholder="搜索三书…（按 /）" autocomplete="off"></div>']
    cur_part = None
    for rel, part in book.order:
        if part != cur_part:
            if cur_part is not None:
                out.append("</ul>")
            out.append(f'<div class="part-head">{html_mod.escape(part)}</div>')
            out.append('<ul class="toc">')
            cur_part = part
        d = book.info[rel]
        active = ' class="active"' if rel == cur else ""
        out.append(
            f'<a href="{root}{d["out"]}" data-file="{rel}"{active}>'
            f'<span class="no">{html_mod.escape(d["no"])}</span>'
            f'<span class="tt">{html_mod.escape(d["short"])}</span></a>'
        )
    if cur_part is not None:
        out.append("</ul>")
    return "\n".join(out)


def book_switch(current: Book, books: list[Book], root: str, in_book: bool,
                skip_current: bool = False) -> str:
    """三书切换：书内顶栏与书封面共用。封面只列另外两本，顶栏列全三本并标当前。"""
    items = []
    for b in books:
        if skip_current and b.key == current.key:
            continue
        cls = ' class="switch-item current"' if b.key == current.key else ' class="switch-item"'
        items.append(
            f'<a{cls} href="{root}{b.key}/index.html" title="{html_mod.escape(b.en)}">'
            f'<span class="sw-seal">{html_mod.escape(b.seal)}</span>'
            f'<span class="sw-txt"><b>{html_mod.escape(b.zh.split("，")[0])}</b>'
            f'<small>{html_mod.escape(b.role)}</small></span></a>'
        )
    return "".join(items)


def render_page(template: str, mapping: dict[str, str]) -> str:
    page = template
    for k, v in mapping.items():
        page = page.replace("{{" + k + "}}", v)
    return page


def read_status() -> dict[str, str]:
    """从状态页解析三书状态，不手写。"""
    out = {"tam": "初稿", "sa": "初稿", "bte": "初稿"}
    p = REPO / "shared" / "00-reading-status.md"
    if p.is_file():
        for line in p.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\|\s*(TAM|SA|BTE)\s*\|\s*([^|]+?)\s*\|", line)
            if m:
                out[m.group(1).lower()] = m.group(2).strip()
    return out


def render_cover(book: Book, tpl: str, status: str, root: str) -> str:
    """书封面：数字全部实测，不手写。"""
    first = next((rel for rel, _ in book.order
                  if book.info[rel]["part"] == "前置页" and rel.startswith("00-p")), None)
    guide = "00-reading-guide.md" if (book.root / "00-reading-guide.md").is_file() else None
    outline = book.outline if (book.root / book.outline).is_file() else None
    ch1 = next((r for r in (r for r, _ in book.order) if r.startswith("ch01")), None)

    def href(rel: str | None) -> str:
        # 封面就在该书目录下，章节链接与封面同层，直接给文件名
        return f'href="{Path(rel).with_suffix(".html").as_posix()}"' if rel else 'style="display:none"'

    cta = []
    if first:
        cta.append(f'<a class="primary" {href(first)}>从书的立场读起 · 前言</a>')
    if guide:
        cta.append(f'<a {href(guide)}>选一条阅读路径 · 导读</a>')
    if ch1:
        cta.append(f'<a {href(ch1)}>直接读第 1 章</a>')
    if outline:
        cta.append(f'<a {href(outline)}>总目录</a>')

    s = book.stats
    facts = [
        f'<span><b>{s["chapters"]}</b>章正文</span>',
        f'<span><b>{s["appendices"]}</b>附录</span>',
        f'<span><b>{s["templates"]}</b>件模板</span>',
        f'<span><b>{s["pages"]}</b>个页面</span>',
        f'<span><b>{s["words"] / 10000:.1f}</b>万字</span>',
        f'<span><b>{html_mod.escape(status)}</b></span>',
    ]
    return render_page(tpl, {
        "ROOT": root,
        "BOOK_EN": html_mod.escape(book.en),
        "BOOK_ZH": html_mod.escape(book.zh),
        "BOOK_SEAL": html_mod.escape(book.seal),
        "BOOK_ROLE": html_mod.escape(book.role),
        "BOOK_SCOPE": html_mod.escape(book.scope),
        "BOOK_STATUS": html_mod.escape(status),
        "FACTS": "\n      ".join(facts),
        "CTA": "\n      ".join(cta),
        "SWITCH": book_switch(book, BOOKS, root, False, skip_current=True),
    })


def render_collection(tpl: str, books: list[Book], status: dict[str, str]) -> str:
    cards = []
    for b in books:
        s = b.stats
        cards.append(f"""<a class="bk-card" href="{b.key}/index.html">
  <div class="bk-head"><span class="bk-seal">{html_mod.escape(b.seal)}</span>
    <span class="bk-role">{html_mod.escape(b.role)}</span></div>
  <h2>{html_mod.escape(b.zh)}</h2>
  <div class="bk-en">{html_mod.escape(b.en)}</div>
  <p>{html_mod.escape(b.scope)}</p>
  <div class="bk-stats"><b>{s["chapters"]}</b> 章 · <b>{s["appendices"]}</b> 附录 · <b>{s["templates"]}</b> 模板 · <b>{s["words"] / 10000:.1f}</b> 万字</div>
  <div class="bk-foot"><span class="bk-state">{html_mod.escape(status[b.key])}</span><span class="bk-go">进入阅读 →</span></div>
</a>""")
    total_pages = sum(b.stats["pages"] for b in books)
    total_words = sum(b.stats["words"] for b in books)
    return render_page(tpl, {
        "CARDS": "\n".join(cards),
        "TOTAL_PAGES": str(total_pages),
        "TOTAL_WORDS": f"{total_words / 10000:.1f}",
    })


# ---------------------------------------------------------------- 主流程

def main(argv: list[str]) -> int:
    global BOOKS
    BOOKS = make_books()
    serve = "--serve" in argv

    tpl_page = (WEB / "template.html").read_text(encoding="utf-8")
    tpl_cover = (WEB / "book-cover.html").read_text(encoding="utf-8")
    tpl_coll = (WEB / "collection.html").read_text(encoding="utf-8")
    status = read_status()

    for b in BOOKS:
        parse_outline(b)
        build_info(b)
    site_of = collect_targets(BOOKS)

    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "assets").mkdir(parents=True)
    for name in ("reader.css", "reader.js"):
        shutil.copy(WEB / name, SITE / "assets" / name)

    # 非 md 资源：shared/figures 平铺为 figures/；LICENSE 镜像到站根
    src_fig = REPO / "shared" / "figures"
    for f in src_fig.rglob("*"):
        if f.is_file():
            dst = SITE / "figures" / f.relative_to(src_fig)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(f, dst)
    if (REPO / "LICENSE").is_file():
        shutil.copy(REPO / "LICENSE", SITE / "LICENSE")

    unresolved: list[str] = []
    index: list[dict] = []

    for book in BOOKS:
        (SITE / book.key).mkdir(parents=True, exist_ok=True)
        root = "../"

        # 书封面
        (SITE / book.key / "index.html").write_text(
            render_cover(book, tpl_cover, status[book.key], root), encoding="utf-8")

        flat = [rel for rel, _ in book.order]
        for idx, (rel, part) in enumerate(book.order):
            d = book.info[rel]
            body = re.sub(r"(?m)^#\s+.+$", "", d["text"], count=1)
            frag = wrap_tables(pandoc(body))
            frag, unres = rewrite_links(frag, book.root, site_of, book.key, BOOKS)
            frag = frag.replace("{{ROOT}}", root)
            frag, sections = assign_ids(frag)
            unresolved += unres

            bignum = f'<div class="bignum">{html_mod.escape(d["no"])}</div>' if d["no"] else ""
            genre = (f'<span class="chip {html_mod.escape(d["genre"])}">'
                     f'{html_mod.escape(d["genre"])}</span>') if d["genre"] else ""
            crumb = (f'<a href="{root}{book.key}/index.html">{html_mod.escape(book.seal)}</a>'
                     f'<span class="sep">/</span>{html_mod.escape(part)}'
                     f'<span class="sep">/</span><span class="now">{html_mod.escape(d["short"])}</span>')

            prev_rel = flat[idx - 1] if idx > 0 else None
            next_rel = flat[idx + 1] if idx < len(flat) - 1 else None
            page = render_page(tpl_page, {
                "ROOT": root, "TITLE": html_mod.escape(d["h1"]), "BRAND_HREF": f"{root}{book.key}/index.html",
                "BOOK_EN": html_mod.escape(book.en), "BOOK_ZH": html_mod.escape(book.zh),
                "BOOK_SEAL": html_mod.escape(book.seal), "BOOK_KEY": book.key,
                "BOOK_STATUS": html_mod.escape(status[book.key]),
                "CRUMB": crumb, "KICKER": html_mod.escape(part), "GENRE": genre,
                "BIGNUM": bignum, "H1": html_mod.escape(d["clean"]),
                "META": html_mod.escape(f'{rel} · {d["zh"]:,} 字'),
                "CONTENT": frag, "FILE": rel,
                "SIDEBAR": build_sidebar(book, root, rel),
                "SWITCH": book_switch(book, BOOKS, root, True),
                "PREV_CLS": "" if prev_rel else "disabled",
                "NEXT_CLS": "" if next_rel else "disabled",
                "PREV_HREF": (f'{root}{book.info[prev_rel]["out"]}' if prev_rel else "#"),
                "NEXT_HREF": (f'{root}{book.info[next_rel]["out"]}' if next_rel else "#"),
                "PREV_TITLE": html_mod.escape(book.info[prev_rel]["short"] if prev_rel else "——"),
                "NEXT_TITLE": html_mod.escape(book.info[next_rel]["short"] if next_rel else "——"),
            })
            out = SITE / d["out"]
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(page, encoding="utf-8")

            for sid, heading, sec in sections:
                txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", sec)).strip()
                if not txt and not heading:
                    continue
                index.append({
                    "b": book.key, "f": d["out"], "t": d["clean"], "h": heading,
                    "i": sid, "x": (heading + " " + txt).strip()[:2000],
                })

    # 扩展页：仓库其他文件（@ext:）
    extras = sorted(k for k in site_of if k.startswith("@ext:"))
    for key in extras:
        src = REPO / key[len("@ext:"):]
        if not src.is_file():
            continue
        out_rel = site_of[key]
        text = src.read_text(encoding="utf-8")
        h1m = H1_RE.search(text)
        h1 = h1m.group(1).strip() if h1m else src.name
        body = re.sub(r"(?m)^#\s+.+$", "", text, count=1)
        frag = wrap_tables(pandoc(body))
        frag, unres = rewrite_links(frag, src.parent, site_of, os.path.dirname(out_rel), BOOKS)
        frag = frag.replace("{{ROOT}}", "../" * out_rel.count("/"))
        frag, _ = assign_ids(frag)
        unresolved += unres
        root = "../" * out_rel.count("/")
        page = render_page(tpl_page, {
            "ROOT": root, "TITLE": html_mod.escape(h1), "BRAND_HREF": f"{root}index.html",
            "BOOK_EN": "the-iron-triangle", "BOOK_ZH": "铁角指北 · 仓库文档",
            "BOOK_SEAL": "仓", "BOOK_KEY": "ext", "BOOK_STATUS": "仓库文档",
            "CRUMB": f'<a href="{root}index.html">丛书总览</a><span class="sep">/</span>'
                     f'<span class="now">{html_mod.escape(h1)}</span>',
            "KICKER": "仓库文档", "GENRE": "", "BIGNUM": "",
            "H1": html_mod.escape(h1),
            "META": html_mod.escape(key[len("@ext:"):]),
            "CONTENT": frag, "FILE": key, "SIDEBAR": "",
            "SWITCH": book_switch(BOOKS[0], BOOKS, root, False),
            "PREV_CLS": "disabled", "NEXT_CLS": "disabled",
            "PREV_HREF": "#", "NEXT_HREF": "#",
            "PREV_TITLE": "——", "NEXT_TITLE": "——",
        })
        out = SITE / out_rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")

    # 丛书首页
    (SITE / "index.html").write_text(render_collection(tpl_coll, BOOKS, status), encoding="utf-8")

    # 搜索索引（三书合一，带书键）
    idx_path = SITE / "search-index.json"
    idx_path.write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    # ---- 构建报告 ----
    print("── 三书页面 ──")
    for b in BOOKS:
        s = b.stats
        print(f"  {b.seal:4} 页 {s['pages']:3}｜章 {s['chapters']:2}｜附录 {s['appendices']:2}"
              f"｜模板 {s['templates']:2}｜{s['words'] / 10000:5.1f} 万字｜状态 {status[b.key]}")
        if b.missing:
            print(f"       目录列出但缺文件：{len(b.missing)} 条 → "
                  + "、".join(f"{r}" for r, _ in b.missing[:6]))
        if s["unlisted"]:
            print(f"       目录未列、按文件名编号归位：{s['unlisted']} 个")
        gaps = missing_parts(b)
        print("       缺件：" + ("、".join(gaps) if gaps else "无"))
    print(f"── 合计页面 {sum(b.stats['pages'] for b in BOOKS)} + 扩展 {len(extras)}"
          f"｜搜索索引 {len(index)} 条（{idx_path.stat().st_size / 1e6:.2f} MB）")

    # ---- 站内断链自检 ----
    bad = check_links()
    if bad:
        print(f"⚠ 站内断链 {len(bad)} 条：")
        for b in bad[:20]:
            print("   ", b)
    else:
        print("✓ 站内链接 0 断链")
    if unresolved:
        print(f"⚠ 未解析 .md 链接 {len(unresolved)} 条：")
        for u in sorted(set(unresolved))[:20]:
            print("   ", u)
    else:
        print("✓ 全部 .md 链接已解析")

    print(f"→ 产物 {SITE}")
    if serve:
        port = 8765
        print(f"→ 本地预览 http://127.0.0.1:{port}/")
        return subprocess.call([sys.executable, "-m", "http.server", str(port), "-d", str(SITE)])
    return 1 if bad else 0


def check_links() -> list[str]:
    """扫描产物 HTML 的内部链接与静态资源，返回断链清单。"""
    bad: list[str] = []
    for html in SITE.rglob("*.html"):
        text = html.read_text(encoding="utf-8", errors="ignore")
        for attr in re.findall(r'(?:href|src)="([^"]+)"', text):
            if attr.startswith(("http", "mailto:", "data:", "#", "javascript:")):
                continue
            target = attr.split("#")[0]
            if not target:
                continue
            p = (html.parent / target).resolve()
            if not p.exists():
                bad.append(f"{html.relative_to(SITE)} → {attr}")
    return bad


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
