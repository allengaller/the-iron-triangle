#!/usr/bin/env python3
"""全仓相对链接校验。

遍历仓库内所有 .md/.html，解析 Markdown 链接与 HTML href/src 中的本地相对路径，
逐条检查目标是否存在。跳过外链、锚点、绝对路径与构建产物；
扫描前先剥掉围栏代码块与行内代码，避免把正文里的链接格式示例当成真链接。

用法（仓库根执行）：
    python3 shared/tooling/link_check.py   # 退出码 0 = 无断链

已知非断链（脚本已列入 SKIP_FILES，不报）：
- shared/tooling/{collection,book-cover,template}.html：构建模板，链接在 shared/dist/.../site/ 下才成立；
  template.html 的 {{ROOT}} 等为运行时占位符。
- books/*/CHANGELOG.md 与 shared/governance/HANDOFF.md：历史记录，路径按当时结构书写，不作活引用校验。
- shared/review/repo/bte-book-feasibility-2026-11-02.md：带日期的可研快照，其中章节编号已被后续重排，按归档规则不回改。
"""
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", "dist", ".impeccable", ".tmp", "__pycache__", "well-architected", "node_modules"}
SKIP_FILES = {
    # 构建模板：其中的相对链接以 shared/dist/site/ 为基准，源码位置必断
    "shared/tooling/cover.html",
    "shared/tooling/collection.html",
    "shared/tooling/book-cover.html",
    "shared/tooling/template.html",
    # 历史记录：路径按当时结构书写
    "books/the-tam-book/CHANGELOG.md",
    "books/the-sa-book/CHANGELOG.md",
    "books/the-bte-book/CHANGELOG.md",
    "shared/governance/HANDOFF.md",
    # 带日期的可研快照：章节编号已重排，按归档规则不回改
    "shared/review/repo/bte-book-feasibility-2026-11-02.md",
}
MD = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HTML = re.compile(r'(?:href|src)="([^"]+)"')
FENCE = re.compile(r"```.*?```", re.S)
INLINE = re.compile(r"`[^`\n]*`")


def strip_code(text):
    return INLINE.sub("", FENCE.sub("", text))


def iter_files():
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith((".md", ".html")):
                p = Path(root) / f
                if p.relative_to(REPO).as_posix() in SKIP_FILES:
                    continue
                yield p


def targets(text, path):
    pat = HTML if path.suffix == ".html" else MD
    for m in pat.finditer(text):
        href = m.group(1).strip()
        if not href or href.startswith(("#", "http://", "https://", "mailto:", "data:", "javascript:")):
            continue
        if href.startswith("/"):
            continue
        href = unquote(href.split("#")[0].split("?")[0])
        if not href:
            continue
        yield href


def main():
    bad = []
    total = 0
    for p in iter_files():
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        for href in targets(strip_code(text), p):
            total += 1
            dest = (p.parent / href).resolve()
            if not dest.exists():
                bad.append((p.relative_to(REPO), href, dest.relative_to(REPO) if str(dest).startswith(str(REPO)) else dest))
    print(f"扫描 {total} 条本地链接，断链 {len(bad)} 条")
    for src, href, dest in bad:
        print(f"  {src}  ->  {href}   (解析为 {dest})")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
