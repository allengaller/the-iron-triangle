#!/usr/bin/env python3
"""全书交叉引用体检：校验五类引用的目标是否存在。"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
MS = os.path.join(ROOT, "manuscript")
TP = os.path.join(ROOT, "templates")

files = sorted(glob.glob(os.path.join(MS, "*.md")) + glob.glob(os.path.join(TP, "*.md")) + [os.path.join(ROOT, "HANDOFF.md")])

# 现有资产清单
ch_files = {}
for f in glob.glob(os.path.join(MS, "ch*.md")):
    ch_files[int(re.match(r"ch(\d+)-", os.path.basename(f)).group(1))] = f
_appx_all = {}
for f in glob.glob(os.path.join(MS, "appx-*.md")):
    _appx_all.setdefault(re.match(r"appx-([a-z]+)-", os.path.basename(f)).group(1).upper(), []).append(f)
# 落地件（*-howto.md）不承载 X.y 条文；取主件做附录存在性与节号索引
appx_letters = {L: (sorted([f for f in fs if not f.endswith("-howto.md")]) or sorted(fs))[0]
                for L, fs in _appx_all.items()}
tpl_nums = {int(re.match(r"(\d+)-", os.path.basename(f)).group(1)): f
            for f in glob.glob(os.path.join(TP, "*.md"))}

# 附录 B 的 B.x 节号、各附录的节号索引
def section_index(path, letter):
    secs = set()
    try:
        text = open(path, encoding="utf-8").read()
    except Exception:
        return secs
    for m in re.finditer(rf"{letter}\.(\d+(?:\.\d+)?)", text):
        secs.add(m.group(1))
    return secs

appx_b_secs = section_index(appx_letters.get("B", ""), "B") if "B" in appx_letters else set()

issues = []

def report(src, line_no, kind, ref, msg):
    issues.append((os.path.relpath(src, ROOT), line_no, kind, ref, msg))

for path in files:
    rel = os.path.relpath(path, ROOT)
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except Exception:
        continue
    for i, line in enumerate(lines, 1):
        is_handoff = os.path.basename(path) == "HANDOFF.md"
        # 1. 文件路径引用 manuscript/xxx.md templates/xxx.md（含 HANDOFF；跳过 <占位符>）
        for m in re.finditer(r"`((?:manuscript|templates)/[^`]+\.md)`", line):
            if "<" in m.group(1):
                continue
            if not os.path.exists(os.path.join(ROOT, m.group(1))):
                report(path, i, "路径", m.group(1), "目标文件不存在")
        # 1b. 配图：![](target) 目标文件须存在，alt 须非空（配图约定见 AGENTS.md）
        for m in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", line):
            alt, target = m.group(1).strip(), m.group(2).strip()
            if not alt:
                report(path, i, "配图", target, "alt 文本为空")
            if target.startswith(("http://", "https://")):
                continue
            if not os.path.exists(os.path.join(os.path.dirname(path), target)):
                report(path, i, "配图", target, "图片文件不存在")
        if is_handoff:
            # HANDOFF 是历史日志：章节/附录/模板/节号字样为记录性文字，不作活引用校验
            continue
        # 2. 第 X 章
        for m in re.finditer(r"第\s*(\d{1,2})\s*章", line):
            n = int(m.group(1))
            if not (1 <= n <= 38):
                report(path, i, "章节", m.group(0), f"章号 {n} 超出 1–38")
            elif n not in ch_files:
                report(path, i, "章节", m.group(0), f"ch{n:02d} 文件不存在")
        # 3. 附录 X（字母；X 为预留字母，见 HANDOFF 待裁定）
        for m in re.finditer(r"附录\s*([A-Z])\b", line):
            L = m.group(1)
            if L == "X":
                continue
            if L not in appx_letters:
                report(path, i, "附录", m.group(0), f"附录 {L} 无对应文件")
        # 4. 模板 NN
        for m in re.finditer(r"模板\s*(\d{2})", line):
            n = int(m.group(1))
            if n not in tpl_nums:
                report(path, i, "模板", m.group(0), f"模板 {n:02d} 文件不存在")
        # 5. B.x 引用（仅查引用的节号是否存在于 appx-b；左边界排除 AB.x 等双字母节号）
        if "B" in appx_letters and os.path.basename(path) != os.path.basename(appx_letters["B"]):
            for m in re.finditer(r"(?<!附录 )(?<![A-Za-z0-9])B\.(\d+\.\d+)", line):
                if m.group(1) not in appx_b_secs:
                    report(path, i, "B节号", m.group(0), f"附录 B 中无 B.{m.group(1)}")

print(f"扫描文件 {len(files)} 个；章 {len(ch_files)}、附录 {len(appx_letters)}、模板 {len(tpl_nums)}")
print(f"发现问题 {len(issues)} 条\n")
for src, ln, kind, ref, msg in issues:
    print(f"{src}:{ln} [{kind}] {ref} — {msg}")
