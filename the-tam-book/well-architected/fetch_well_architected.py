#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取六家云厂商 Well-Architected 框架官方文档全文，落盘为 Markdown。

用法：
    python3 fetch_well_architected.py            # 全量抓取
    python3 fetch_well_architected.py --limit 2  # 每家只抓 2 页，用于验证解析

输出：
    ./aws/*.md  ./azure/**/*.md  ./google/*.md
    ./aliyun/*.md  ./tencent/*.md  ./huawei/*.md
每个文件头部写来源 URL、抓取时点、标题；文末回链原页面。
抓取完成后重写 ./README.md 索引（份数、字数、源、时点）。

设计纪律：
1. 只抓官方文档站，不放宽证书、不绕过登录；
2. 单线程 + 间隔，避免给对方站点压力；
3. 页面为空或解析失败时写“抓取失败”存根并保留链接，不静默丢弃；
4. 可重复执行，重复运行会覆盖同名文件并刷新时点。
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import date
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

BASE = os.path.dirname(os.path.abspath(__file__))
VENDORS = [
    ("AWS", "aws", "https://docs.aws.amazon.com/wellarchitected/latest/framework/"),
    ("Azure", "azure", "https://learn.microsoft.com/en-us/azure/well-architected/"),
    ("Google Cloud", "google", "https://docs.cloud.google.com/architecture/framework"),
    ("阿里云", "aliyun", "https://help.aliyun.com/zh/well-architected/"),
    ("腾讯云", "tencent", "https://cloud.tencent.com/document/product/1264"),
    ("华为云", "huawei", "https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/"),
]
CAPTURED = os.environ.get("WA_CAPTURED") or date.today().isoformat()
FAIL_LOG = os.path.join(BASE, ".fetch_failures.tsv")   # 失败清单落盘，--summary 重写 README 时不丢
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
DELAY = 0.1
STATS = []          # (vendor, files, chars, source)
FAILED = []         # (vendor, url, reason)
SKIPPED = [0]        # 目录页/纯截图页：不单独成文，也不算失败
WRITTEN = [0]


# ---------------------------------------------------------------- http
def get(url, retry=2, timeout=30):
    for i in range(retry + 1):
        try:
            r = requests.get(url, headers=HEADERS, timeout=timeout)
            if r.status_code == 200:
                r.encoding = r.apparent_encoding or r.encoding
                return r
            if r.status_code in (403, 404, 410):
                return r
        except Exception as exc:                                    # noqa: BLE001
            if i == retry:
                FAILED.append(("http", url, f"{type(exc).__name__}: {exc}"))
        time.sleep(0.6 * (i + 1))
    return None


# ---------------------------------------------------------------- html -> md
SKIP = {"script", "style", "nav", "footer", "header", "aside", "form", "noscript", "svg"}


def inline(node):
    """把行内标签压成 markdown 片段。"""
    parts = []
    for child in node.children:
        name = getattr(child, "name", None)
        if name is None:
            parts.append(str(child))
        elif name == "a":
            txt = child.get_text(" ", strip=True)
            href = child.get("href", "")
            parts.append(f"[{txt}]({href})" if txt and href else txt)
        elif name in ("code", "tt"):
            txt = child.get_text(" ", strip=True)
            parts.append(f"`{txt}`" if txt else "")
        elif name in ("strong", "b"):
            txt = child.get_text(" ", strip=True)
            parts.append(f"**{txt}**" if txt else "")
        elif name in ("em", "i"):
            txt = child.get_text(" ", strip=True)
            parts.append(f"*{txt}*" if txt else "")
        elif name == "br":
            parts.append(" ")
        elif name == "img":
            src = child.get("src", "")
            if src.startswith("//"):
                src = "https:" + src
            if src:
                parts.append(f"![{child.get('alt', '')}]({src})")
        elif name in SKIP:
            continue
        else:
            parts.append(inline(child))
    txt = "".join(parts)
    txt = re.sub(r"[ \t\u00a0]+", " ", txt)
    return txt.strip()


def to_md(root):
    out = []

    def walk(node):
        name = node.name
        if name in SKIP:
            return
        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            txt = node.get_text(" ", strip=True)
            if txt:
                out.append("\n" + "#" * int(name[1]) + " " + txt + "\n")
            return
        if name == "p":
            txt = inline(node)
            if txt:
                out.append(txt + "\n")
            return
        if name in ("ul", "ol"):
            for idx, li in enumerate(node.find_all("li", recursive=False), 1):
                txt = inline(li)
                if not txt:
                    continue
                if name == "ol":
                    out.append(f"{idx}. {txt}")
                else:
                    out.append(f"- {txt}")
            out.append("")
            return
        if name == "pre":
            code = node.get_text("\n", strip=False).rstrip()
            if code:
                out.append("```\n" + code + "\n```\n")
            return
        if name == "table":
            rows = [[td for td in tr.find_all(["th", "td"])] for tr in node.find_all("tr")]
            rows = [r for r in rows if r]
            if not rows:
                return
            width = max(len(r) for r in rows)
            if width <= 1:
                # 单列表格（AWS 用它包“问题框”）：拆回正文，避免生成一列表
                for r in rows:
                    for td in r:
                        walk(td)
                return
            text_rows = []
            for r in rows:
                cells = [re.sub(r"\s+", " ", inline(td)).replace("|", "\\|") for td in r]
                text_rows.append(cells + [""] * (width - len(cells)))
            out.append("| " + " | ".join(text_rows[0]) + " |")
            out.append("|" + " --- |" * width)
            for r in text_rows[1:]:
                out.append("| " + " | ".join(r) + " |")
            out.append("")
            return
        if name == "blockquote":
            txt = inline(node)
            if txt:
                out.append("> " + txt + "\n")
            return
        if name == "img":
            src = node.get("src", "")
            if src.startswith("//"):
                src = "https:" + src
            if src:
                out.append(f"![{node.get('alt', '')}]({src})\n")
            return
        for child in node.children:
            if getattr(child, "name", None):
                walk(child)

    walk(root)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def pick_container(soup, selectors):
    """按选择器优先级取正文容器；返回 (element, selector)。"""
    for sel in selectors:
        el = soup.select_one(sel)
        if el and len(el.get_text(" ", strip=True)) >= 200:
            return el, sel
    # 兜底：正文最长的 main/article/div
    best, best_len = None, 0
    for el in soup.find_all(["main", "article", "div"]):
        ln = len(el.get_text(" ", strip=True))
        if 200 < ln < 200000 and ln > best_len:
            best, best_len = el, ln
    return best, "fallback"


NOISE = [
    r"^Access to this page requires authorization.*$",
    r"^Stay organized with collections.*$",
    r"^[-*\s]*\[?(x\.com|Facebook|LinkedIn|Twitter|Weibo|微博|复制链接|分享)\]?\(javascript:.*$",
    r"^[-*\s]*\[(x\.com|Facebook|LinkedIn|Twitter|Weibo|微博|复制链接)\]\(.*$",
    r"^链接复制成功！?$",
    r"^\[?(上一篇|下一篇)[:：].*$",
    r"^#{0,4}\s*您对此文档页面的整体评价.*$",
    r"^如您有其它疑问.*$",
    r"^\s*\[?\s*(返回顶部|回到顶部)\s*\]?.*$",
    r"^-?\s*\[?(Home|Documentation|Cloud Architecture Center)\]?\(https?://(docs\.cloud\.google\.com|cloud\.google\.com).*$",
]


def clean_title(title):
    """去掉站点拼进标题的前后缀（Google 的收藏提示、腾讯的栏目名与产品前缀等）。"""
    t = re.sub(r"\s*Stay organized with collections.*$", "", title or "").strip()
    t = re.sub(r"-文档中心-腾讯云$", "", t)
    t = re.sub(r"-(操作指南|购买指南|API 文档|开发指南|最佳实践)$", "", t)
    t = re.sub(r"^智能顾问[\s　]*[-—]?\s*", "", t)
    t = t.lstrip("-— 　").strip()
    return re.sub(r"\s{2,}", " ", t).strip()


def text_len(md):
    """正文字数：去掉图片链接、注释与空白后再数，避免纯图页面或目录页被当成有正文。"""
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md or "")
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    return len(re.sub(r"\s+", "", t))


def clean_md(md, title):
    """去掉重复标题与站点噪声。"""
    lines = [ln for ln in md.splitlines() if not any(re.match(p, ln.strip()) for p in NOISE)]
    body = "\n".join(lines).strip()
    # 去掉与本文件 H1 重复的标题行（只保留文档头部那一个 H1）
    if title:
        key = re.sub(r"\s+", "", title)[:30]
        kept, dropped = [], False
        for ln in body.splitlines():
            if ln.startswith("# ") and re.sub(r"\s+", "", ln[2:])[:30] == key:
                if not dropped:
                    dropped = True
                    continue
            kept.append(ln)
        body = "\n".join(kept).strip()
    return body


def write_doc(vendor, rel_path, url, title, body, extra=""):
    time.sleep(DELAY)
    WRITTEN[0] += 1
    if WRITTEN[0] % 50 == 0:
        print(f"   ...已写 {WRITTEN[0]} 个文件（{vendor}/{rel_path}）", flush=True)
    path = os.path.join(BASE, vendor, rel_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    head = [
        f"<!-- source: {url} -->",
        f"<!-- captured: {CAPTURED} -->",
        f"<!-- vendor: {vendor} -->",
    ]
    if extra:
        head.append(f"<!-- {extra} -->")
    doc = "\n".join(head) + "\n\n" + f"# {title}\n\n" + body.strip() + \
          f"\n\n---\n\n> 原页面：{url}（抓取时点 {CAPTURED}；正文为自动抓取，排版已规整，语义未改写）\n"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(doc)
    return path, len(body)


def slug(name):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", name).strip("-").lower()
    return s or "index"


# ---------------------------------------------------------------- vendors
def aws(limit):
    toc = "https://docs.aws.amazon.com/wellarchitected/latest/framework/toc-contents.json"
    base = "https://docs.aws.amazon.com/wellarchitected/latest/framework/"
    r = get(toc)
    if not r or r.status_code != 200:
        FAILED.append(("aws", toc, "toc 不可用"))
        return
    pages = []

    def walk(node):
        if isinstance(node, dict):
            if node.get("href"):
                pages.append((node.get("title", ""), node["href"]))
            for key in ("contents", "children"):
                for child in node.get(key, []) or []:
                    walk(child)
        elif isinstance(node, list):
            for child in node:
                walk(child)

    walk(r.json().get("contents", []))
    pages = [(t, h) for t, h in pages if h.endswith(".html")]
    n = 0
    for title, href in pages[:limit] if limit else pages:
        url = base + href
        page = get(url)
        if not page or page.status_code != 200:
            FAILED.append(("aws", url, "抓取失败"))
            continue
        soup = BeautifulSoup(page.text, "html.parser")
        h1 = soup.find("h1")
        title = h1.get_text(" ", strip=True) if h1 else title
        el, _ = pick_container(soup, ["div#main-column", "div.awsdocs-content"])
        body = clean_md(to_md(el) if el else "", title)
        if len(body) < 100:
            FAILED.append(("aws", url, "正文为空"))
            continue
        write_doc("aws", href.replace(".html", ".md"), url, title, body)
        n += 1
    STATS.append(("AWS", n, "https://docs.aws.amazon.com/wellarchitected/latest/framework/"))


def toc_pages(slug):
    """读 doc set 的 toc-contents.json，返回去重后的 [(title, href)]；不可用返回 None。"""
    base = "https://docs.aws.amazon.com/wellarchitected/latest/"
    r = get(base + slug + "/toc-contents.json")
    if not r or r.status_code != 200:
        FAILED.append(("aws", base + slug, "toc 不可用"))
        return None
    pages, seen = [], set()

    def walk(node):
        if isinstance(node, dict):
            href = str(node.get("href", ""))
            if href.endswith(".html") and href not in seen:
                seen.add(href)
                pages.append((node.get("title", ""), href))
            for key in ("contents", "children"):
                for child in node.get(key) or []:
                    walk(child)
        elif isinstance(node, list):
            for child in node:
                walk(child)

    try:
        walk(r.json().get("contents", []))
    except ValueError:
        FAILED.append(("aws", base + slug, "toc 非 JSON"))
        return None
    return pages


def fetch_docset(slug, limit=None, pages=None):
    """抓一个 AWS doc set 的全部页面，返回成功页数；失败逐条记入 FAILED。

    正文容器优先 `div#main-column`，回退 `div.awsdocs-content`。
    """
    base = "https://docs.aws.amazon.com/wellarchitected/latest/"
    if pages is None:
        pages = toc_pages(slug)
        if pages is None:
            return 0
    n = 0
    for title, href in pages:
        if limit and n >= limit:
            break
        url = base + slug + "/" + href
        page = get(url)
        if not page or page.status_code != 200:
            FAILED.append(("aws", url, "抓取失败"))
            continue
        soup = BeautifulSoup(page.text, "html.parser")
        h1 = soup.find("h1")
        heading = h1.get_text(" ", strip=True) if h1 else title
        el, _ = pick_container(soup, ["div#main-column", "div.awsdocs-content"])
        body = clean_md(to_md(el) if el else "", heading)
        if len(body) < 100:
            FAILED.append(("aws", url, "正文为空"))
            continue
        write_doc("aws", slug + "/" + href.replace(".html", ".md"), url, heading, body)
        n += 1
    return n


def aws_ext(limit):
    """AWS 扩展层：支柱详解、DevOps/治理指南、ORR、用户指南是独立 doc set。

    从已落盘文件的链接里反复发现新 doc set，直到不再出现新的 slug（最多 3 轮），
    避免漏掉正文互引的延伸页面。Lens 不在正文里互引，另由 aws_lens 按索引页补齐。
    """
    base = "https://docs.aws.amazon.com/wellarchitected/latest/"
    done = {"framework"}
    n = 0
    for _ in range(3):
        slugs = set()
        for root, _, names in os.walk(os.path.join(BASE, "aws")):
            for name in names:
                if not name.endswith(".md"):
                    continue
                with open(os.path.join(root, name), encoding="utf-8", errors="ignore") as fh:
                    slugs.update(re.findall(r"wellarchitected/latest/([a-z0-9-]+)/", fh.read()))
        todo = sorted(slugs - done)
        if not todo:
            break
        for slug in todo:
            done.add(slug)
            n += fetch_docset(slug, limit)
    STATS.append(("AWS（扩展层）", n, base))


def aws_lens(limit):
    """Lens 补齐层：以 docs 产品索引页的 `*-lens` 清单为准，按 toc 页数逐个校验补缺。

    aws_ext 只能发现正文里被引用的 doc set，而营销卡片上的新 Lens（agentic-ai、
    digital-sovereignty、maori-data 等）不进正文互引；索引页
    https://docs.aws.amazon.com/wellarchitected/index.html 是 docs 站的 guide 总表，
    30 份 Lens 全部在列。已落盘目录按「toc 页数不少于目录内文件数」判完整，
    因此中途中断后重跑能续补，不会因目录存在而误跳。
    """
    base = "https://docs.aws.amazon.com/wellarchitected/latest/"
    r = get("https://docs.aws.amazon.com/wellarchitected/index.html")
    if not r or r.status_code != 200:
        FAILED.append(("aws", "index.html", "索引页不可用"))
        return
    slugs = sorted(set(re.findall(r"wellarchitected/latest/([a-z0-9-]+-lens)/", r.text)))
    root = os.path.join(BASE, "aws")
    n = 0
    for slug in slugs:
        pages = toc_pages(slug)
        if pages is None:
            continue
        folder = os.path.join(root, slug)
        have = 0
        for _, _, files in os.walk(folder):
            have += sum(1 for f in files if f.endswith(".md"))
        if have >= len(pages):
            print(f"   {slug}: 已完整（{have}/{len(pages)}）", flush=True)
            continue
        got = fetch_docset(slug, limit, pages)
        print(f"   {slug}: 补 {got} 页（原 {have}/{len(pages)}）", flush=True)
        n += got
    STATS.append(("AWS（Lens 补齐）", n, base))


def azure(limit):
    toc = "https://learn.microsoft.com/en-us/azure/well-architected/toc.json"
    base = "https://learn.microsoft.com/en-us/azure/well-architected/"
    r = get(toc)
    if not r or r.status_code != 200:
        FAILED.append(("azure", toc, "toc 不可用"))
        return
    pages = []

    def walk(node):
        if isinstance(node, dict):
            if node.get("href"):
                pages.append((node.get("toc_title", ""), node["href"]))
            for key in ("items", "children"):
                for child in node.get(key, []) or []:
                    walk(child)
        elif isinstance(node, list):
            for child in node:
                walk(child)

    walk(r.json().get("items", []))
    seen, uniq = set(), []
    for t, h in pages:
        h = h.strip("/")
        if not h or h in (".", "..") or h in seen or h.startswith("http"):
            continue
        seen.add(h)
        uniq.append((t, h))
    n = 0
    for title, href in uniq[:limit] if limit else uniq:
        url = base + href
        page = get(url)
        if not page or page.status_code != 200:
            FAILED.append(("azure", url, "抓取失败"))
            continue
        soup = BeautifulSoup(page.text, "html.parser")
        h1 = soup.find("h1")
        title = h1.get_text(" ", strip=True) if h1 else title
        el, _ = pick_container(soup, ["main#main", "div.reading-width"])
        body = clean_md(to_md(el) if el else "", title)
        if len(body) < 100:
            FAILED.append(("azure", url, "正文为空"))
            continue
        write_doc("azure", href + ".md", url, title, body)
        n += 1
    STATS.append(("Azure", n, "https://learn.microsoft.com/en-us/azure/well-architected/"))


def google(limit):
    seeds = ["https://docs.cloud.google.com/architecture/framework",
             "https://docs.cloud.google.com/architecture/framework/reliability"]
    links, seen_pages, queue = set(), set(), list(seeds)
    for seed in seeds:
        r = get(seed)
        if not r or r.status_code != 200:
            continue
        links.update(re.findall(r'href="(/architecture/framework[^"#?]*)"', r.text))
    links = sorted(links)
    n = 0
    for path in links[:limit] if limit else links:
        url = "https://docs.cloud.google.com" + path
        if url in seen_pages or path.endswith("/printable"):
            continue
        seen_pages.add(url)
        page = get(url)
        if not page or page.status_code != 200:
            FAILED.append(("google", url, "抓取失败"))
            continue
        soup = BeautifulSoup(page.text, "html.parser")
        h1 = soup.find("h1")
        title = clean_title(h1.get_text(" ", strip=True)) if h1 else path.strip("/").split("/")[-1]
        el, _ = pick_container(soup, ["article.devsite-article", "div.devsite-article-body"])
        body = clean_md(to_md(el) if el else "", title)
        if len(body) < 100:
            FAILED.append(("google", url, "正文为空"))
            continue
        rel = path.replace("/architecture/framework", "").strip("/") or "index"
        write_doc("google", rel + ".md", url, title, body)
        n += 1
    STATS.append(("Google Cloud", n, "https://docs.cloud.google.com/architecture/framework"))


# 腾讯云「卓越架构」的方法论正文不在产品文档里，而在官方开发者社区的产品白皮书中；
# 产品文档 1264 只覆盖智能顾问的功能与操作，两者合并才算全量。
TENCENT_ARTICLES = [
    ("2446243", "腾讯云顾问产品白皮书：三层模型与六大支柱原文"),
    ("2677400", "腾讯云顾问应用白皮书：卓越指数与客户案例"),
    ("2677389", "腾讯云顾问可视化治理平台白皮书"),
]


def tencent(limit):
    index = "https://cloud.tencent.com/document/product/1264"
    r = get(index)
    if not r or r.status_code != 200:
        FAILED.append(("tencent", index, "目录页不可用"))
        return
    ids = sorted(set(re.findall(r"/document/product/1264/(\d+)", r.text)))
    n = 0
    for doc_id in ids[:limit] if limit else ids:
        url = f"https://cloud.tencent.com/document/product/1264/{doc_id}"
        page = get(url)
        if not page or page.status_code != 200:
            FAILED.append(("tencent", url, "抓取失败"))
            continue
        soup = BeautifulSoup(page.text, "html.parser")
        raw_title = soup.title.get_text(strip=True) if soup.title else doc_id
        title = clean_title(raw_title.split("_")[0]) or doc_id
        h1 = soup.find("h1")
        if h1 and h1.get_text(strip=True):
            title = clean_title(h1.get_text(" ", strip=True)) or title
        el = soup.select_one("div.doc-article-content") or soup.select_one("div.J-markdown-box")
        body = clean_md(to_md(el) if el else "", title)
        if text_len(body) < 200:
            # 目录页与纯截图页不单独成文，也不计失败
            SKIPPED[0] += 1
            continue
        write_doc("tencent", f"1264-{doc_id}.md", url, title, body)
        n += 1
    for aid, note in TENCENT_ARTICLES[:limit] if limit else TENCENT_ARTICLES:
        url = f"https://cloud.tencent.com/developer/article/{aid}"
        page = get(url)
        if not page or page.status_code != 200:
            FAILED.append(("tencent", url, "抓取失败"))
            continue
        soup = BeautifulSoup(page.text, "html.parser")
        h1 = soup.find("h1")
        el = soup.select_one("div.rno-markdown")
        title = clean_title(h1.get_text(" ", strip=True)) if h1 else aid
        body = clean_md(to_md(el) if el else "", title)
        if len(body) < 200:
            FAILED.append(("tencent", url, "正文缺失（需登录或付费）"))
            continue
        write_doc("tencent", f"article-{aid}.md", url, title, body, extra=f"community: {note}")
        n += 1
    STATS.append(("腾讯云", n, "https://cloud.tencent.com/document/product/1264"))


def huawei(limit, cap=420):
    prefix = "https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/"
    menu = "https://support.huaweicloud.com/intl/zh-cn/architecture/v3_support_leftmenu_fragment.html"
    frag = get(menu)
    pages = []
    if frag and frag.status_code == 200:
        pages = sorted(set(re.findall(r"usermanual-architecture/(architecture_\d+_\d+\.html)", frag.text)))
    if not pages:
        pages = ["architecture_01_0001.html"]
    n = 0
    for name in pages[:limit] if limit else pages:
        url = prefix + name
        page = get(url)
        if not page or page.status_code != 200:
            FAILED.append(("huawei", url, "抓取失败"))
            continue
        soup = BeautifulSoup(page.text, "html.parser")
        h1 = soup.find("h1")
        title = clean_title(h1.get_text(" ", strip=True)) if h1 else url.rsplit("/", 1)[-1]
        el, _ = pick_container(soup, ["div#support-content", "div#content", "div.help-page"])
        body = clean_md(to_md(el) if el else "", title)
        if len(body) < 100:
            FAILED.append(("huawei", url, "正文为空"))
            continue
        write_doc("huawei", name.replace(".html", ".md"), url, title, body)
        n += 1
    STATS.append(("华为云", n, prefix))


ALI_TREE = ("https://help.aliyun.com/help/json/menupath.json"
            "?alias=%2Fwell-architected%2F&website=cn&language=zh&channel=")
ALI_DOC = ("https://help.aliyun.com/help/json/document_detail.json"
           "?alias={alias}&pageNum=1&pageSize=20&website=cn&language=zh&channel=")


def aliyun(limit):
    """阿里云：走官方 JSON 接口取「卓越架构」全集。

    新版 /zh/ 与旧版 document_detail/ 都有大量页面是客户端渲染，HTML 里只剩加载占位；
    同一份内容在 menupath.json（全量目录树）与 document_detail.json（正文 HTML）里可直接取到。
    """
    r = get(ALI_TREE)
    if not r or r.status_code != 200:
        FAILED.append(("aliyun", ALI_TREE, "目录树不可用"))
        return
    try:
        tree = r.json().get("data") or {}
    except ValueError:
        FAILED.append(("aliyun", ALI_TREE, "目录树非 JSON"))
        return
    nodes = []

    def walk(node, trail):
        slug = (node.get("alias") or "").rstrip("/").rsplit("/", 1)[-1]
        trail = trail + [slug] if slug else trail
        if node.get("validDocument") and node.get("alias"):
            nodes.append((node.get("title", ""), node["alias"], node.get("url", ""), trail))
        for child in node.get("children") or []:
            walk(child, trail)

    walk(tree, [])
    n = 0
    for title, alias, path, trail in nodes[:limit] if limit else nodes:
        resp = get(ALI_DOC.format(alias=quote(alias, safe="")))
        if not resp or resp.status_code != 200:
            FAILED.append(("aliyun", "https://help.aliyun.com" + (path or alias), "接口取数失败"))
            continue
        try:
            data = resp.json().get("data") or {}
        except ValueError:
            FAILED.append(("aliyun", "https://help.aliyun.com" + (path or alias), "接口返回非 JSON"))
            continue
        html = data.get("content") or ""
        title = clean_title(data.get("docTitle") or title)
        url = "https://help.aliyun.com" + (data.get("url") or path or alias)
        body = clean_md(to_md(BeautifulSoup(html, "html.parser")), title) if html else ""
        if len(body) < 80:
            FAILED.append(("aliyun", url, "正文过短"))
            continue
        write_doc("aliyun", "/".join(trail) + ".md", url, title, body,
                  extra=f"node-id: {data.get('nodeId', '')}")
        n += 1
    STATS.append(("阿里云", n, "https://help.aliyun.com/zh/well-architected/"))


# ---------------------------------------------------------------- index
DOC_RE = re.compile(r"\A((?:<!--[^\n]*-->\n)+)\n# ([^\n]+)\n\n(.*)\n\n---\n\n(> 原页面：[^\n]+)\n?\Z", re.S)


def clean_existing():
    """离线清洗：对已落盘文件重跑一遍噪声过滤，不联网、不重抓。

    用途：调完 NOISE 规则后批量回填，或某厂商本次抓取失败、旧文件还带着页脚噪声时。
    """
    changed = 0
    for _, folder, _ in VENDORS:
        for root, _, names in os.walk(os.path.join(BASE, folder)):
            for name in names:
                if not name.endswith(".md"):
                    continue
                path = os.path.join(root, name)
                with open(path, encoding="utf-8") as fh:
                    txt = fh.read()
                m = DOC_RE.match(txt)
                if not m:
                    continue
                head, title, body, footer = m.groups()
                new_body = clean_md(body, title.strip())
                if new_body != body:
                    with open(path, "w", encoding="utf-8") as fh:
                        fh.write(f"{head}\n# {title}\n\n{new_body}\n\n---\n\n{footer}\n")
                    changed += 1
    print(f"离线清洗完成：{changed} 个文件有改动", flush=True)


def write_readme():
    if not FAILED and os.path.exists(FAIL_LOG):
        with open(FAIL_LOG, encoding="utf-8") as fh:
            for line in fh:
                parts = line.rstrip("\n").split("\t")
                if len(parts) == 3:
                    FAILED.append((parts[0], parts[1], parts[2]))
    lines = [
        "<!-- 本文件由 fetch_well_architected.py 生成，请勿手工编辑正文结构 -->",
        "# Well-Architected 官方文档本地归档",
        "",
        "六家云厂商 Well-Architected 框架官方文档的离线副本。"
        "腾讯云另含官方开发者社区的三份卓越架构白皮书（`tencent/article-*.md`）。"
        "用途：附录 Z 的事实核对底稿、断网写作与季度复核对照。**引用以原页面为准**，"
        "本目录只保证「当时页面写了什么」。",
        "",
        "## 目录结构",
        "",
        "`aws/` 根下是框架正文，`aws/<doc-set>/` 是延伸文档集（支柱详解、DevOps 与治理指引、"
        "运营就绪评审、用户指南）与 30 份 Lens（行业与技术两类）；`aliyun/` 按官方目录树分层，"
        "其余厂商平铺。",
        "",
        "## 归档范围",
        "",
        "| 厂商 | 文件数 | 抓取源 | 说明 |",
        "| --- | --- | --- | --- |",
    ]
    notes = {
        "AWS": "框架指南全量（六支柱设计原则与逐条最佳实践）＋延伸文档集与 30 份 Lens",
        "Azure": "Well-Architected 目录全量（支柱、设计原则、工作负载、评审）",
        "Google Cloud": "architecture/framework 全量（支柱、Perspective、部署原型）",
        "腾讯云": "产品 1264（智能顾问·卓越架构）全量 + 官方社区三份卓越架构白皮书",
        "华为云": "usermanual-architecture 卓越架构技术框架全量（按左侧导航全量抓取）",
        "阿里云": "卓越架构文档集全量（官方 menupath/document_detail 接口树，含 AI 卓越架构）",
    }
    total, chars, stamps = 0, 0, set()
    for vendor, folder, src in VENDORS:
        files = 0
        for root, _, names in os.walk(os.path.join(BASE, folder)):
            for name in names:
                if not name.endswith(".md"):
                    continue
                with open(os.path.join(root, name), encoding="utf-8") as fh:
                    text = fh.read()
                files += 1
                chars += len(text)
                m = re.search(r"captured:\s*(\d{4}-\d{2}-\d{2})", text)
                if m:
                    stamps.add(m.group(1))
        total += files
        lines.append(f"| {vendor} | {files} | <{src}> | {notes.get(vendor, '')} |")
    window = "、".join(sorted(stamps)) if stamps else CAPTURED
    lines += [
        "",
        f"合计 **{total} 个文件**、约 **{chars // 1000} 千字符**，抓取日 {window}。",
        "",
        "抓取分两批：首轮全量落盘后，后续只补新出现在官方索引里的 doc set（当前为 AWS 23 份 Lens）；"
        "批内跨零点统一标注批次日，故文件头的 `captured` 只有批次日、没有具体时刻。",
        "",
        "## 文件约定",
        "",
        "每个文件头部三行注释记录 `source`（原始 URL）、`captured`（抓取日期）、`vendor`；"
        "文末回链原页面。正文为 HTML 自动转 Markdown，标题层级、列表、表格、代码块已规整，**语义未改写**。",
        "",
        "## 复跑与维护（对接附录 Z.9.2）",
        "",
        "```bash",
        "python3 fetch_well_architected.py            # 全量重抓，覆盖同名文件并刷新 captured",
        "python3 fetch_well_architected.py --limit 2  # 抽样验证解析是否失效",
        "```",
        "",
        "季度复核时先看本文件底部的失败清单：解析规则失效（页面改版）会表现为某厂商份数骤降或正文变短，"
        "此时修选择器而不是删条目。",
        "",
    ]
    if SKIPPED[0]:
        lines += [f"另有 **{SKIPPED[0]} 个目录页/纯截图页**未单独成文（导航页或仅有截图，不计失败）。", ""]
    if FAILED:
        lines += ["## 本次未取到的页面", "", "| 厂商 | URL | 原因 |", "| --- | --- | --- |"]
        for vendor, url, reason in FAILED[:200]:
            lines.append(f"| {vendor} | <{url}> | {reason} |")
        if len(FAILED) > 200:
            lines.append(f"| … | 其余 {len(FAILED) - 200} 条省略 | — |")
        lines.append("")
    with open(os.path.join(BASE, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    if FAILED:
        with open(FAIL_LOG, "w", encoding="utf-8") as fh:
            for vendor, url, reason in FAILED:
                fh.write(f"{vendor}\t{url}\t{reason}\n")
    elif os.path.exists(FAIL_LOG):
        os.remove(FAIL_LOG)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="每家抓取页数上限，0 为全量")
    ap.add_argument("--only", default="", help="只抓某一组：aws/aws-ext/aws-lens/azure/google/tencent/huawei/aliyun")
    ap.add_argument("--summary", action="store_true", help="不抓取，只按磁盘现有文件重写 README 索引")
    ap.add_argument("--clean", action="store_true", help="不抓取，只对已落盘文件重跑噪声过滤")
    args = ap.parse_args()
    if args.clean:
        clean_existing()
        return 0
    if args.summary:
        write_readme()
        print("索引已按磁盘现状重写", flush=True)
        return 0
    limit = args.limit or None
    jobs = [("aws", aws), ("azure", azure), ("google", google),
            ("tencent", tencent), ("huawei", huawei), ("aliyun", aliyun),
            ("aws-ext", aws_ext), ("aws-lens", aws_lens)]
    for name, fn in jobs:
        if args.only and args.only != name:
            continue
        print(f"== {name} ==", flush=True)
        fn(limit)
        print(f"   -> {STATS[-1][1]} 个文件，累计失败 {len(FAILED)}", flush=True)
    write_readme()
    print(f"完成：{sum(n for _, n, _ in STATS)} 文件，失败 {len(FAILED)} 条", flush=True)


if __name__ == "__main__":
    sys.exit(main())
