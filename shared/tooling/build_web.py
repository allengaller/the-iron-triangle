#!/usr/bin/env python3
"""build_web.py — 把全书 Markdown 构建成静态阅读站（site/）。

设计：
- 书稿已扁平到书根，章节/附录/模板同处一层，靠文件名前缀区分；
- TOC 与阅读顺序取自 00-outline.md（目录唯一事实源）；
- pandoc (gfm) 渲染正文，Python 做链接 .md→.html 重写、表格包裹、
  配图转 figure、标题锚点编号、搜索索引与页面组装；
- 站内链接键 = 相对 the-tam-book/ 的路径；站外仓库文件（CHANGELOG、
  shared/standards/README 等）统一压平渲染到 site/ext/。

用法：python3 shared/tooling/build_web.py   （在仓库根执行；产物 shared/dist/site/，不入库）
"""
from __future__ import annotations

import html as html_mod
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]           # 仓库根（脚本在 shared/tooling/）
BOOK = REPO / "books" / "the-tam-book"               # 书稿目录（书根只剩 md）
SITE = REPO / "shared" / "dist" / "site"               # 构建产物统一到共用 shared/dist/
WEB = REPO / "shared" / "tooling"                    # 构建资源与脚本同处
GH_BLOB = "https://github.com/allengaller/the-iron-triangle/blob/main"

ZH = re.compile(r"[一-鿿]")
DIATAXIS = re.compile(r"Diátaxis:\s*([A-Za-z-]+)")
H1_RE = re.compile(r"^#\s+(.+)$", re.M)
OUTLINE_PART = re.compile(r"^##\s+(.+)$", re.M)
OUTLINE_PATH = re.compile(r"(?:ch\d+|appx-|tpl-\d+|00-|99-|DIATAXIS)[\w.-]*\.md")
MD_HREF = re.compile(r'href="([^"]+\.md)(#[^"]*)?"')          # HTML 片段中的链接
MD_LINK = re.compile(r"\]\(([^)\s]+\.md)(#[^)]*)?\)")          # Markdown 源文中的链接（收集用）


def zh_count(text: str) -> int:
    return len(ZH.findall(text))


def short_title(t: str) -> str:
    return re.sub(r"^(第\s*\d+\s*章[\s　]+|附录\s*[A-Z]{1,2}[\s　]+|模板\s*\d+[\s　]+)", "", t.strip()).strip()


def split_prefix(t: str) -> tuple[str, str]:
    """返回 (章号/附录字母/模板号, 去前缀标题)。"""
    for pat in (r"第\s*(\d+)\s*章[\s　]+(.+)$", r"附录\s*([A-Z]{1,2})[\s　]+(.+)$", r"模板\s*(\d+)[\s　]+(.+)$"):
        m = re.match(pat, t.strip())
        if m:
            return m.group(1), m.group(2)
    return "", t.strip()


# ---------------------------------------------------------------- TOC

def parse_outline() -> list[tuple[str, str]]:
    """[(md 相对路径, 部分标题)]，按 00-outline.md 的阅读顺序。"""
    text = (BOOK / "00-outline.md").read_text(encoding="utf-8")
    order: list[tuple[str, str]] = []
    seen: set[str] = set()
    part = "前置页"
    for line in text.splitlines():
        m = OUTLINE_PART.match(line)
        if m:
            part = m.group(1).strip()
            continue
        for p in OUTLINE_PATH.findall(line):
            if p not in seen:
                seen.add(p)
                order.append((p, part))
    for f in sorted(BOOK.glob("*.md")):
        if not OUTLINE_PATH.fullmatch(f.name):
            continue
        rel = f.name
        if rel not in seen:
            seen.add(rel)
            order.append((rel, "导航与索引"))
    if "00-outline.md" not in seen:
        order.insert(0, ("00-outline.md", "导航与索引"))
    return order


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


def ext_out(rel_repo: str) -> str:
    """站外文件在 site/ext/ 下的输出名。README、CHANGELOG 同名，用路径前缀消歧。"""
    stem = Path(rel_repo).stem
    if stem.upper() in {"README", "CHANGELOG"}:
        stem = rel_repo[: -len(".md")].replace("/", "-")
    return f"ext/{stem}.html"


def collect_targets(order: list[tuple[str, str]]) -> dict[str, str]:
    """规划全部 .md 链接目标的站内渲染位。

    键空间统一为「相对 the-tam-book/ 的路径」；站外仓库文件用 "@ext:" 前缀。
    值为相对 site/ 的 html 路径。
    """
    targets: dict[str, str] = {rel: Path(rel).with_suffix(".html").as_posix() for rel, _ in order}

    def scan(src: Path) -> None:
        text = src.read_text(encoding="utf-8")
        for href, _ in MD_LINK.findall(text):
            if not href.endswith(".md"):
                continue
            abs_t = os.path.normpath(os.path.join(src.parent, href))
            if not os.path.isfile(abs_t):
                continue
            try:
                rel_repo = os.path.relpath(abs_t, REPO).replace(os.sep, "/")
            except ValueError:
                continue
            if rel_repo.startswith("the-tam-book/") or not rel_repo.startswith(".."):
                inner = os.path.relpath(abs_t, BOOK).replace(os.sep, "/")
                if not inner.startswith("..") and inner.endswith(".md"):
                    targets.setdefault(inner, Path(inner).with_suffix(".html").as_posix())
                elif not rel_repo.startswith(".."):
                    targets.setdefault("@ext:" + rel_repo, ext_out(rel_repo))

    for rel, _ in order:
        scan(BOOK / rel)
    # 书稿公用卷（shared/00-*.md）是三书的读者入口，其一级链接一并成页；不递归，
    # 二级页面未成页的链接由 rewrite_links 兜底指向 GitHub。
    for f in sorted((REPO / "shared").glob("00-*.md")):
        scan(f)
    return targets


def rewrite_links(fragment: str, base_abs: Path, site_of: dict[str, str], out_dir: str) -> tuple[str, list[str]]:
    """把片段中的 .md 链接改写为站内 .html。base_abs = 源文件所在目录（绝对路径）。"""
    unresolved: list[str] = []

    def link(m: re.Match) -> str:
        href, frag = m.group(1), m.group(2) or ""
        abs_t = os.path.normpath(os.path.join(base_abs, href))
        # 站内（the-tam-book/ 内）
        try:
            inner = os.path.relpath(abs_t, BOOK).replace(os.sep, "/")
        except ValueError:
            inner = ""
        key = inner if not inner.startswith("..") else ""
        if not key or key not in site_of:
            try:
                rel_repo = os.path.relpath(abs_t, REPO).replace(os.sep, "/")
            except ValueError:
                rel_repo = ""
            if rel_repo and not rel_repo.startswith(".."):
                key2 = "@ext:" + rel_repo
                if key2 in site_of:
                    return f'href="{os.path.relpath(site_of[key2], out_dir or ".")}{frag}"'
                if os.path.isfile(abs_t):
                    # 仓库内未成页的文件（二级 README、标准全文等）兜底到 GitHub
                    return f'href="{GH_BLOB}/{rel_repo}{frag}"'
            unresolved.append(f"{href}（相对 {base_abs.name}）")
            return m.group(0)
        return f'href="{os.path.relpath(site_of[key], out_dir or ".")}{frag}"'

    fragment = MD_HREF.sub(link, fragment)
    # LICENSE 是仓库根的非 md 文件，指向它的链接统一落到站根副本
    def lic(m: re.Match) -> str:
        href = m.group(1)
        abs_t = os.path.normpath(os.path.join(base_abs, href))
        if abs_t != str(REPO / "LICENSE"):
            return m.group(0)
        return f'href="{os.path.relpath(SITE / "LICENSE", SITE / out_dir if out_dir else SITE)}"'
    fragment = re.sub(r'href="([^"]*LICENSE)"', lic, fragment)
    # 图源在 shared/figures/，站点内平铺为 figures/，剥掉越出站点根的前缀
    fragment = fragment.replace('src="../../shared/figures/', 'src="figures/')
    return fragment, unresolved


# ---------------------------------------------------------------- 组装

def build_sidebar(order, info, root, cur) -> str:
    out = ['<div class="search-wrap"><input id="search-input" type="search" '
           'placeholder="搜索全书…（按 /）" autocomplete="off"></div>']
    cur_part = None
    for rel, part in order:
        if part != cur_part:
            if cur_part is not None:
                out.append("</ul>")
            out.append(f'<div class="part-head">{html_mod.escape(part)}</div>')
            out.append('<ul class="toc">')
            cur_part = part
        d = info[rel]
        active = ' class="active"' if rel == cur else ""
        out.append(
            f'<a href="{root}{d["out"]}" data-file="{rel}"{active}>'
            f'<span class="no">{html_mod.escape(d["no"])}</span>'
            f'<span class="tt">{html_mod.escape(d["short"])}</span></a>'
        )
    if cur_part is not None:
        out.append("</ul>")
    return "\n".join(out)


def render_page(template: str, mapping: dict[str, str]) -> str:
    page = template
    for k, v in mapping.items():
        page = page.replace("{{" + k + "}}", v)
    return page


def main() -> int:
    template = (WEB / "template.html").read_text(encoding="utf-8")
    order = parse_outline()
    site_of = collect_targets(order)

    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "assets").mkdir(parents=True)
    shutil.copy(WEB / "reader.css", SITE / "assets" / "reader.css")
    shutil.copy(WEB / "reader.js", SITE / "assets" / "reader.js")
    shutil.copy(WEB / "cover.html", SITE / "index.html")

    # 非 md 资源：shared/figures/ 在站内平铺为 figures/
    src_fig = REPO / "shared" / "figures"
    for f in src_fig.rglob("*"):
        if f.is_file():
            dst = SITE / "figures" / f.relative_to(src_fig)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(f, dst)
    # 被引用的非 md 文件：LICENSE 在仓库根（书根只剩 md），镜像到站根供链接解析
    for f in (REPO / "LICENSE", BOOK / "README.md"):
        if f.is_file():
            shutil.copy(f, SITE / f.name)

    # 页面元信息
    info: dict[str, dict] = {}
    for rel, part in order:
        text = (BOOK / rel).read_text(encoding="utf-8")
        h1m = H1_RE.search(text)
        h1 = h1m.group(1).strip() if h1m else rel
        g = DIATAXIS.search(text[:500])
        no, clean = split_prefix(h1)
        info[rel] = {
            "out": site_of[rel], "part": part, "h1": h1, "clean": clean, "no": no,
            "genre": g.group(1) if g else "", "short": short_title(h1),
            "zh": zh_count(text), "text": text,
        }

    # 渲染正文（去首行 H1，页面自带章首块）
    fragments: dict[str, tuple[str, list]] = {}
    unresolved: list[str] = []
    for rel, _ in order:
        body = re.sub(r"(?m)^#\s+.+$", "", info[rel]["text"], count=1)
        frag = wrap_tables(pandoc(body))
        frag, unres = rewrite_links(frag, BOOK / os.path.dirname(rel), site_of, os.path.dirname(site_of[rel]))
        frag, sections = assign_ids(frag)
        fragments[rel] = (frag, sections)
        unresolved += unres

    # 扩展页：站外仓库文件（@ext:）+ 书内被引用但不在目录的文件（CHANGELOG/AGENTS/HANDOFF…）
    order_set = {rel for rel, _ in order}
    extras = sorted(k for k in site_of if k.startswith("@ext:") or k not in order_set)
    for key in extras:
        src = (REPO / key[len("@ext:"):]) if key.startswith("@ext:") else (BOOK / key)
        if not src.is_file():
            continue
        out_rel = site_of[key]
        text = src.read_text(encoding="utf-8")
        h1m = H1_RE.search(text)
        h1 = h1m.group(1).strip() if h1m else src.name
        body = re.sub(r"(?m)^#\s+.+$", "", text, count=1)
        frag = wrap_tables(pandoc(body))
        frag, unres = rewrite_links(frag, src.parent, site_of, os.path.dirname(out_rel))
        frag, _ = assign_ids(frag)
        unresolved += unres
        root = os.path.relpath(SITE, (SITE / out_rel).parent)
        root = "" if root == "." else root + "/"
        page = render_page(template, {
            "ROOT": root, "TITLE": html_mod.escape(h1), "CRUMB": html_mod.escape(h1),
            "KICKER": "仓库文档", "GENRE": "", "BIGNUM": "",
            "H1": html_mod.escape(h1),
            "META": html_mod.escape(key[len("@ext:"):] if key.startswith("@ext:") else key),
            "CONTENT": frag, "FILE": key, "SIDEBAR": "",
            "PREV_CLS": "disabled", "NEXT_CLS": "disabled",
            "PREV_HREF": "#", "NEXT_HREF": "#",
            "PREV_TITLE": "——", "NEXT_TITLE": "——",
        })
        out = SITE / out_rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")

    # 主站页面
    flat = [rel for rel, _ in order]
    for idx, (rel, part) in enumerate(order):
        d = info[rel]
        frag, _ = fragments[rel]
        out_dir = os.path.dirname(d["out"])
        root = os.path.relpath(SITE, SITE / out_dir) if out_dir else ""
        root = "" if root == "." else root + "/"
        bignum = f'<div class="bignum">{html_mod.escape(d["no"])}</div>' if d["no"] else ""
        genre = (f'<span class="chip {html_mod.escape(d["genre"])}">'
                 f'{html_mod.escape(d["genre"])}</span>') if d["genre"] else ""
        crumb = (f'{html_mod.escape(part)}<span class="sep">/</span>'
                 f'<span class="now">{html_mod.escape(d["short"])}</span>')

        prev_rel = flat[idx - 1] if idx > 0 else None
        next_rel = flat[idx + 1] if idx < len(flat) - 1 else None
        page = render_page(template, {
            "ROOT": root, "TITLE": html_mod.escape(d["h1"]), "CRUMB": crumb,
            "KICKER": html_mod.escape(part), "GENRE": genre, "BIGNUM": bignum,
            "H1": html_mod.escape(d["clean"]),
            "META": html_mod.escape(f'{rel} · {d["zh"]:,} 字'),
            "CONTENT": frag, "FILE": rel,
            "SIDEBAR": build_sidebar(order, info, root, rel),
            "PREV_CLS": "" if prev_rel else "disabled",
            "NEXT_CLS": "" if next_rel else "disabled",
            "PREV_HREF": (os.path.relpath(site_of[prev_rel], out_dir) if prev_rel else "#"),
            "NEXT_HREF": (os.path.relpath(site_of[next_rel], out_dir) if next_rel else "#"),
            "PREV_TITLE": html_mod.escape(info[prev_rel]["short"] if prev_rel else "——"),
            "NEXT_TITLE": html_mod.escape(info[next_rel]["short"] if next_rel else "——"),
        })
        out = SITE / d["out"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")

    # 搜索索引（按小节切分）
    index = []
    for rel, _ in order:
        d = info[rel]
        for sid, heading, body in fragments[rel][1]:
            txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", body)).strip()
            if not txt and not heading:
                continue
            index.append({
                "f": d["out"], "t": d["clean"], "h": heading,
                "i": sid, "x": (heading + " " + txt).strip()[:2000],
            })
    idx_path = SITE / "search-index.json"
    idx_path.write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    print(f"✓ 页面 {len(order)} + 扩展 {len(extras)}，搜索索引 {len(index)} 条（{idx_path.stat().st_size / 1e6:.2f} MB）")
    if unresolved:
        print(f"⚠ 未解析 .md 链接 {len(unresolved)} 条：")
        for u in sorted(set(unresolved))[:20]:
            print("   ", u)
    else:
        print("✓ 全部 .md 链接已解析")
    print(f"→ 打开 {SITE / 'index.html'}（推荐 python3 -m http.server -d {SITE}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
