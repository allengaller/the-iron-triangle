#!/usr/bin/env python3
"""元数据单一事实源：从磁盘算，不手写。

## 为什么有这个脚本

本书的文件数、类型分布、字数曾被手写在四个地方：根 README、导读、GTM 落地页、
DIATAXIS-MAP。文件一增删，四处各漂各的。读者第一眼看到的门面数字，全都不对。

治法不是再手改一遍——手改的数字会再腐坏。治法是把这些数字变成"从磁盘算出来的"，
并用标记区锁进文档：

    <!-- META:diataxis -->...由脚本填写...<!-- /META:diataxis -->

标记区之外，文档可以随便写。标记区之内，只有脚本能改。

## 用法

    python3 shared/tooling/gen_metadata.py            # 打印全部事实（在仓库根执行）
    python3 shared/tooling/gen_metadata.py --write    # 回填所有标记区
    python3 shared/tooling/gen_metadata.py --check    # 校验，漂移即退出码 1（门禁用）
    python3 shared/tooling/gen_metadata.py --index    # 重建 99-index.md

## 口径

- 中文字数：`[\\u4e00-\\u9fff]` 匹配数，含标点外的全部汉字。
- 分型文件：首行 400 字符内带 `<!-- Diátaxis: X -->` 的文件。
- 附录：文件名以 `appx-` 开头者为附录（2026-11-17 起落地件已并入主件，无独立落地件）。
- 标准库：`shared/standards/` 为唯一主库（2026-11-17 双库合并、2026-11-18 入公用层）。
- 前置页：文件名以 `00-` 或 `99-` 开头者，不计入章节与分型统计。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]           # 仓库根（脚本在 shared/tooling/）
ROOT = REPO / "books" / "the-tam-book"               # 书稿目录（书根只剩 md）
MS = ROOT                                            # 书稿已扁平到书根，模板用 tpl- 前缀区分
TEMPLATES = ROOT
# 书稿文件：章节、附录、前置页、索引、类型总览。模板（tpl-）与仓库文档（README/CHANGELOG）不算。
BOOK_MD = re.compile(r"(?:ch\d|appx-|00-|99-|DIATAXIS-MAP)")
STD_ROOT = REPO / "shared" / "standards" / "data"         # 2026-11-18 公用层：全文在 shared/standards/data/

CJK = re.compile(r"[\u4e00-\u9fff]")
DIATAXIS = re.compile(r"<!--\s*Diátaxis:\s*(Explanation|How-to|Reference|Tutorial)\b")

# 附录字母排序：单字母在前，双字母在后。
LETTER_ORDER: dict[str, int] = {}
for _i, _ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    LETTER_ORDER[_ch] = _i
for _i, _a in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    for _j, _b in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        LETTER_ORDER[_a + _b] = 100 + _i * 26 + _j


def zh_len(text: str) -> int:
    return len(CJK.findall(text))


def _is_draft(p: Path) -> bool:
    """标题行带“（拟定稿）”的算自订标准件。"""
    lines = p.read_text(encoding="utf-8").splitlines()
    return len(lines) > 1 and "（拟定稿）" in lines[1]


def compress(names: list[str], sep: str = "") -> str:
    """把有序记号压成区间串：B,I,J,K,L,M,N,O,R,S,T,U,V,Y -> B、I–O、R–V、Y。"""
    if not names:
        return ""
    idx = [LETTER_ORDER.get(n, 9999) for n in names]
    order = sorted(range(len(names)), key=lambda k: idx[k])
    groups: list[list[str]] = []
    for k in order:
        if groups and idx[k] == LETTER_ORDER.get(groups[-1][-1], -99) + 1:
            groups[-1].append(names[k])
        else:
            groups.append([names[k]])
    out = []
    for g in groups:
        if len(g) >= 3:
            out.append(f"{g[0]}{sep}–{g[-1]}{sep}")
        else:
            out.extend(f"{x}{sep}" for x in g)
    return "、".join(out)


def parse_badge(name: str) -> str:
    """appx-ad-career-lifecycle-guide.md -> 'AD'。"""
    body = name[len("appx-"):-len(".md")]
    return body.split("-")[0].upper()


def scan() -> dict:
    md = sorted(p for p in MS.glob("*.md") if BOOK_MD.match(p.name))
    body = [p for p in md if p.name.startswith("ch")]
    appx = [p for p in md if p.name.startswith("appx-")]
    # 前置页与导航件：既不是章，也不是附录。目录、导读、类型总览、索引都算。
    front = [p for p in md if p not in body and p not in appx]

    types: dict[str, int] = {"Explanation": 0, "How-to": 0, "Reference": 0, "Tutorial": 0}
    for p in md:
        head = p.read_text(encoding="utf-8")[:400]
        m = DIATAXIS.search(head)
        if m:
            types[m.group(1)] += 1

    main = sorted((parse_badge(p.name) for p in appx),
                  key=lambda x: LETTER_ORDER.get(x, 9999))

    # 草案件：标题带“（拟定稿）”的附录。附录 C 是映射表、W 是外部标准汇编，标题不含拟定稿。
    drafts = [p for p in appx if _is_draft(p)]

    total_zh = sum(zh_len(p.read_text(encoding="utf-8")) for p in md)

    def count_md(d: Path, deep: bool = False) -> int:
        if not d.exists():
            return 0
        it = d.rglob("*.md") if deep else d.glob("*.md")
        return len([p for p in it if p.name.upper() != "README.MD"])

    wa = count_md(REPO / "shared" / "well-architected", deep=True)

    typed = sum(types.values())
    return {
        "zh_total": total_zh,
        "draft_count": len(drafts),
        "files_manuscript": len(md),
        "files_chapter": len(body),
        "files_appendix": len(appx),
        "files_front": len(front),
        "appendix_main": len(main),
        "appendix_main_list": compress(main, ""),
        "diataxis_typed": typed,
        "type_explanation": types["Explanation"],
        "type_howto": types["How-to"],
        "type_reference": types["Reference"],
        "type_tutorial": types["Tutorial"],
        "type_mixed": 0,
        "templates": len(list(TEMPLATES.glob("tpl-*.md"))),
        "standards_root": count_md(STD_ROOT),
        "wa_pages": wa,
    }


def pct(n: int, total: int) -> str:
    return f"{round(n * 100 / total) if total else 0}%"


def render(key: str, f: dict) -> str:
    """标记区内容。全部单行，避免破坏所在段落。"""
    table = {
        "type_explanation": str(f["type_explanation"]),
        "type_howto": str(f["type_howto"]),
        "type_reference": str(f["type_reference"]),
        "type_tutorial": str(f["type_tutorial"]),
        "type_explanation_pct": pct(f["type_explanation"], f["diataxis_typed"]),
        "type_howto_pct": pct(f["type_howto"], f["diataxis_typed"]),
        "type_reference_pct": pct(f["type_reference"], f["diataxis_typed"]),
        "type_tutorial_pct": pct(f["type_tutorial"], f["diataxis_typed"]),
        "diataxis_typed": str(f["diataxis_typed"]),
        "diataxis": (
            f"Explanation {f['type_explanation']}、How-to {f['type_howto']}、"
            f"Reference {f['type_reference']}、Tutorial {f['type_tutorial']}、"
            f"混合 {f['type_mixed']}，合计 {f['diataxis_typed']} 个分型文件"
        ),
        "diataxis_dot": (
            f"Explanation {f['type_explanation']} · How-to {f['type_howto']} · "
            f"Reference {f['type_reference']} · Tutorial {f['type_tutorial']} · "
            f"混合 {f['type_mixed']}"
        ),
        "appendix": (
            f"{f['files_appendix']} 个（{f['appendix_main_list']}）"
        ),
        "appendix_count": str(f["files_appendix"]),
        "draft_count": str(f["draft_count"]),
        "manuscript_count": str(f["files_manuscript"]),
        "chapter_count": str(f["files_chapter"]),
        "front_count": str(f["files_front"]),
        "templates_count": str(f["templates"]),
        "standards_root_count": str(f["standards_root"]),
        "zh_total": f"{f['zh_total']:,}",
        "wa_pages": f"{f['wa_pages']:,}",
    }
    if key not in table:
        raise KeyError(f"未知 META 键：{key}")
    return table[key]


BLOCK = re.compile(r"<!--\s*META:([a-z_]+)\s*-->(.*?)<!--\s*/META:\1\s*-->", re.S)


def rewrite(text: str, f: dict) -> tuple[str, list[str]]:
    """返回 (新文本, 变更说明)。"""
    notes: list[str] = []
    for m in BLOCK.finditer(text):
        key, old = m.group(1), m.group(2)
        new = render(key, f)
        if old != new:
            notes.append(f"{key}: {old.strip()!r} -> {new!r}")
    return BLOCK.sub(lambda m: f"<!-- META:{m.group(1)} -->{render(m.group(1), f)}"
                            f"<!-- /META:{m.group(1)} -->", text), notes


TARGETS = [
    ROOT / "README.md",                          # 2026-11-18 书级 README 建立，META span 随 TAM 内容下移
    ROOT / "00-reading-guide.md",
    ROOT / "00-front-matter.md",                 # 版权页 3 处 span，曾漏登导致 静默陈旧
    ROOT / "DIATAXIS-MAP.md",
    REPO / "shared" / "gtm" / "index.html",      # gtm 七批已迁入 shared/gtm
]


# ---------------------------------------------------------------- 索引生成

CHAPTER_H1 = re.compile(r"^#\s*第\s*(\d+)\s*章[\s　]*(.+?)\s*$")
APPX_H1 = re.compile(r"^#\s*附录\s*([A-Z]+)\+?[\s　]*(.+?)\s*$")
TPL_H1 = re.compile(r"^#\s*模板\s*(\d+)[\s　]*(.+?)\s*$")


def first_sentence(text: str, limit: int = 58) -> str:
    """取用途首句。跳过“对应…”行，剥掉“用途/用法：”前缀。"""
    body = ""
    for line in text.splitlines():
        if not line.startswith(">"):
            continue
        body = line.lstrip("> ").strip()
        if not body or body.startswith("对应"):
            continue
        break
    else:
        return ""
    body = re.sub(r"^(用途|用法|使用说明)[：:]\s*", "", body)
    cut = re.split(r"[。；]", body, maxsplit=1)[0].strip()
    if len(cut) > limit:
        cut = cut[:limit].rstrip("，、") + "…"
    return cut


def build_index(f: dict) -> str:
    chapters, appendices = [], []
    for p in sorted(MS.glob("*.md")):
        if not BOOK_MD.match(p.name):
            continue
        text = p.read_text(encoding="utf-8")
        first = text.splitlines()[0] if text else ""
        h1 = next((l for l in text.splitlines() if l.startswith("# ")), "")
        m = DIATAXIS.search(text[:400])
        dtype = m.group(1) if m else ""
        mc = CHAPTER_H1.match(h1)
        ma = APPX_H1.match(h1)
        if mc:
            chapters.append((int(mc.group(1)), mc.group(2), dtype, p.name, first))
        elif ma:
            letter = ma.group(1)
            # 部分附录 H1 带“：说明”后缀，索引只留主标题。
            title = re.split(r"[：:]", ma.group(2), maxsplit=1)[0].strip()
            appendices.append((LETTER_ORDER.get(letter, 9999), title, dtype, p.name))

    chapters.sort(key=lambda x: x[0])
    appendices.sort(key=lambda x: x[0])

    out = [
        "# 索引",
        "",
        "> 本索引按**编号**检索。按**主题**检索用导读的场景表。按**类型**检索用"
        "[DIATAXIS-MAP](DIATAXIS-MAP.md)。按**流程编号**检索用[附录 B](appx-b-tam-process-system.md)。",
        ">",
        "> 三张表由 `shared/tooling/gen_metadata.py --index` 从磁盘生成。新增或改名文件后重跑，"
        "不要手改本文件。校验命令见 [AGENTS.md](../../AGENTS.md) 内容门禁一节。",
        "",
        "---",
        "",
        "## 一、章节索引",
        "",
        f"正文 {f['files_chapter']} 个文件，按章号排列。内涵篇每维两章：主章讲判断，"
        "紧随的实战章给动作。",
        "",
        "| 章 | 标题 | 类型 | 文件 |",
        "| --- | --- | --- | --- |",
    ]
    for num, title, dtype, fname, _ in chapters:
        out.append(f"| {num} | {title} | {dtype} | [`{fname}`]({fname}) |")

    out += [
        "",
        "---",
        "",
        "## 二、模板索引",
        "",
        f"`tpl-*.md` 共 {f['templates']} 份可复制件，按编号排列。每条给用途首句，"
        "完整字段见模板文件本身。",
        "",
        "| 编号 | 名称 | 用途 | 文件 |",
        "| --- | --- | --- | --- |",
    ]
    for p in sorted(TEMPLATES.glob("tpl-*.md")):
        text = p.read_text(encoding="utf-8")
        h1 = next((l for l in text.splitlines() if l.startswith("# ")), "")
        mt = TPL_H1.match(h1)
        num = mt.group(1) if mt else p.stem.split("-")[1]
        name = mt.group(2) if mt else p.stem
        out.append(f"| {num} | {name} | {first_sentence(text)} | "
                   f"[`{p.name}`]({p.name}) |")

    out += [
        "",
        "---",
        "",
        "## 三、附录索引",
        "",
        f"{f['files_appendix']} 个附录，按字母排列，条文与执行动作用同一节号。",
        "",
        "| 字母 | 标题 | 类型 | 文件 |",
        "| --- | --- | --- | --- |",
    ]
    for _, title, dtype, fname in appendices:
        out.append(f"| {parse_badge(fname)} | {title} | {dtype} | [`{fname}`]({fname}) |")

    out += [
        "",
        "---",
        "",
        "## 四、四个事实源",
        "",
        "本书有四类内容只在一处定义，别处引用。改之前先确认改的是不是事实源：",
        "",
        "| 查什么 | 去哪 | 说明 |",
        "| --- | --- | --- |",
        "| 术语与缩写 | [附录 A](appx-a-glossary.md) | 八组术语表，A.8 是编号前缀速查 |",
        "| 流程与规范编号 | [附录 B](appx-b-tam-process-system.md) | P1–P12 流程，九项运营规范 |",
        "| 指标口径 | [第 34 章](ch34-measurement-system.md) | 定义、算法、阈值只在这里改 |",
        "| 章节与阅读路径 | [目录](00-outline.md) | 结构唯一事实源 |",
        "",
        "P 前缀有四种语义（流程 P1–P12、故障级 P1–P4、评估原则 P1–P5、附录 P 节号）。"
        "首现须带语境限定词，歧义消解表在附录 A.8。",
        "",
    ]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="元数据单一事实源")
    ap.add_argument("--write", action="store_true", help="回填所有 META 标记区")
    ap.add_argument("--check", action="store_true", help="只校验，漂移退出码 1")
    ap.add_argument("--index", action="store_true", help="重建 99-index.md")
    args = ap.parse_args()

    f = scan()

    if args.index:
        target = MS / "99-index.md"
        target.write_text(build_index(f), encoding="utf-8")
        print(f"已重建 {target.relative_to(ROOT)}")
        return 0

    if not (args.write or args.check):
        for k in sorted(f):
            print(f"{k:26} {f[k]}")
        return 0

    drifted, missing = [], []
    for t in TARGETS:
        if not t.exists():
            continue
        text = t.read_text(encoding="utf-8")
        new, notes = rewrite(text, f)
        if not BLOCK.search(text):
            missing.append(str(t.relative_to(REPO)))
        if notes:
            drifted.append((t, notes))
            if args.write:
                t.write_text(new, encoding="utf-8")

    for t, notes in drifted:
        rel = t.relative_to(REPO)
        for n in notes:
            print(f"{'已回填' if args.write else '漂移'} {rel}: {n}")
        if not args.write:
            print()

    if missing:
        print("未找到 META 标记区：" + "、".join(missing))
    if not drifted and not args.write:
        print("元数据一致，无漂移。")

    if args.check and drifted:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
