#!/usr/bin/env python3
"""merge_landing.py — 一次性合并：14 个落地件（appx-*-howto.md）并入各自主件。

历史脚本：2026-11-17 已完成，仅留档；下文路径按当时的 manuscript/、templates/
子目录结构编写，2026-11-18 扁平化后不再直接运行。

规则（2026-11-17 裁定，见 AGENTS.md「体裁合并裁定」）：
- 主件末尾新增 `## X.(max+1) 执行落地` 节，位置在最后一个编号节之后、
  尾随的非编号节（版本与共建 / 要点回顾）之前；无尾随节则追加到文件末尾。
- 落地件正文降级一级标题（## → ###、### → ####），节号 X+.k → X.(max+1).k。
- 落地件的 Diátaxis 头、H1、导语引言、尾部「要点回顾」不并入。
- 主件首屏「落地执行见附录 X+」改指本文件新节。
- 全仓引用改写：链接 [附录 X+](howto) → [附录 X](主件)；裸 X+.k → X.(max+1).k。

用法：python3 tooling/merge_landing.py [--dry-run]（仅历史参考）
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]           # 仓库根（历史脚本，路径按当时结构）
ROOT = REPO / "books" / "the-tam-book"
MS = ROOT / "manuscript"

# 字母 -> (主件文件名, 落地件文件名, 主件最大节号)
PAIRS: dict[str, tuple[str, str, int]] = {
    "B": ("appx-b-tam-process-system.md", "appx-b-tam-process-system-howto.md", 4),
    "I": ("appx-i-on-duty-standard.md", "appx-i-on-duty-standard-howto.md", 10),
    "J": ("appx-j-enablement-training-standard.md", "appx-j-enablement-training-howto.md", 9),
    "K": ("appx-k-incident-emergency-drill-standard.md", "appx-k-incident-emergency-howto.md", 10),
    "L": ("appx-l-project-onboarding-standard.md", "appx-l-project-onboarding-howto.md", 9),
    "M": ("appx-m-product-introduction-standard.md", "appx-m-product-introduction-howto.md", 10),
    "N": ("appx-n-tam-onsite-certification.md", "appx-n-tam-onsite-certification-howto.md", 6),
    "O": ("appx-o-tam-onsite-promotion-standard.md", "appx-o-tam-onsite-promotion-howto.md", 10),
    "R": ("appx-r-problem-retrospective-standard.md", "appx-r-problem-retrospective-howto.md", 10),
    "S": ("appx-s-overtime-compoff-standard.md", "appx-s-overtime-compoff-howto.md", 11),
    "T": ("appx-t-online-change-standard.md", "appx-t-online-change-howto.md", 10),
    "U": ("appx-u-ticket-management-standard.md", "appx-u-ticket-management-howto.md", 12),
    "V": ("appx-v-tam-bte-sa-triangle.md", "appx-v-tam-bte-sa-triangle-howto.md", 9),
    "Y": ("appx-y-training-tutorial.md", "appx-y-training-howto.md", 8),
}


def extract_body(howto_text: str, letter: str) -> str:
    """取落地件正文：首个 ## 标题起到尾部要点回顾之前的段落。"""
    lines = howto_text.splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("## "))
    body = lines[start:]
    # 切掉尾部：...内容 + --- + **本附录/本章要点回顾** + 列表
    for i in range(len(body) - 1, -1, -1):
        if "要点回顾" in body[i]:
            cut = i
            if cut > 0 and body[cut - 1].strip() == "---":
                cut -= 1
            while cut > 0 and body[cut - 1].strip() == "":
                cut -= 1
            body = body[:cut]
            break
    text = "\n".join(body).strip("\n")
    # 标题降级（先深后浅，避免二次降级）
    text = re.sub(r"(?m)^### ", "#### ", text)
    text = re.sub(r"(?m)^## ", "### ", text)
    # 节号 X+.k -> X.(max+1).k
    new_sec = PAIRS[letter][2] + 1
    text = re.sub(rf"\b{letter}\+\.(\d+)", rf"{letter}.{new_sec}.\1", text)
    return text


def merge_one(letter: str) -> str:
    main_name, howto_name, max_sec = PAIRS[letter]
    main_path, howto_path = MS / main_name, MS / howto_name
    main = main_path.read_text(encoding="utf-8")
    howto = howto_path.read_text(encoding="utf-8")
    body = extract_body(howto, letter)
    new_sec = max_sec + 1

    section = (
        f"## {letter}.{new_sec} 执行落地\n\n"
        f"> 本节把本附录条文转成可照做的动作：前置条件、操作步骤、验收与检查清单。"
        f"条文定义见上文各节，不重复；时限与锚点以本附录条文为准。\n\n"
        f"{body}\n"
    )

    # 插入点：最后一个编号节之后的首个非编号 ## 节之前；无则追加文件末尾
    lines = main.splitlines()
    last_num = max(
        (i for i, l in enumerate(lines) if re.match(rf"## {letter}\.\d+ ", l)),
        default=-1,
    )
    insert_at = len(lines)
    for i in range(last_num + 1, len(lines)):
        if lines[i].startswith("## "):
            insert_at = i
            break
    # 跳过插入点前的空行，保持单空行分隔
    while insert_at > 0 and lines[insert_at - 1].strip() == "":
        insert_at -= 1
    new_lines = lines[:insert_at] + [""] + section.rstrip("\n").splitlines() + lines[insert_at:]
    main = "\n".join(new_lines).rstrip("\n") + "\n"

    # 主件首屏指针句
    main = re.sub(
        rf"落地执行(动作)?见\[附录 {letter}\+\]\({re.escape(howto_name)}\)",
        f"落地执行动作见本附录 {letter}.{new_sec} 节",
        main,
    )
    # 主件内对落地件节号的直引（如 appx-y 的 Y+.1）
    main = re.sub(
        rf"\[附录 {letter}\+\]\({re.escape(howto_name)}\)\s*{letter}\+\.(\d+)",
        rf"{letter}.{new_sec}.\1",
        main,
    )
    # 主件内其余对落地件的链接（兜底）
    main = re.sub(
        rf"\[附录 {letter}\+\]\({re.escape(howto_name)}\)",
        f"[附录 {letter}]({main_name})",
        main,
    )
    main_path.write_text(main, encoding="utf-8")
    return f"{letter}: +{letter}.{new_sec} 执行落地（正文 {len(body)} 字符）"


def rewrite_refs() -> int:
    """全仓（manuscript + templates + AGENTS/QUALITY-GATE）改写残留落地件引用。"""
    files = list(MS.glob("*.md")) + list((ROOT / "templates").glob("*.md")) + [
        REPO / "AGENTS.md",
        REPO / "QUALITY-GATE.md",
    ]
    changed = 0
    for p in files:
        if p.name.endswith("-howto.md") and p.name.startswith("appx-"):
            continue  # 待删除，不改
        t = p.read_text(encoding="utf-8")
        orig = t
        for letter, (main_name, howto_name, max_sec) in PAIRS.items():
            new_sec = max_sec + 1
            # 跨文件链接
            t = t.replace(f"[附录 {letter}+]({howto_name})", f"[附录 {letter}]({main_name})")
            # 反引号路径
            t = t.replace(howto_name, main_name)
            # 裸节号 X+.k（含 X+.k 节 形态）
            t = re.sub(rf"\b{letter}\+\.(\d+)", rf"{letter}.{new_sec}.\1", t)
            # 裸「附录 X+」文字
            t = t.replace(f"附录 {letter}+", f"附录 {letter}")
            # 成对简写 Y/Y+、B/B+ 等
            t = re.sub(rf"\b{letter}/{letter}\+", letter, t)
        if t != orig:
            p.write_text(t, encoding="utf-8")
            changed += 1
    return changed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.dry_run:
        for letter in PAIRS:
            main_name, howto_name, max_sec = PAIRS[letter]
            body = extract_body((MS / howto_name).read_text(encoding="utf-8"), letter)
            print(f"{letter}: 新节 {letter}.{max_sec + 1}，并入正文 {len(body)} 字符")
        return 0

    for letter in PAIRS:
        print(merge_one(letter))
    n = rewrite_refs()
    print(f"\n引用改写：{n} 个文件")
    print(f"待删除落地件：{len(PAIRS)} 个（git rm 由执行者完成）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
