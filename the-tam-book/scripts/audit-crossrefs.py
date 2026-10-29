#!/usr/bin/env python3
"""全书交叉引用回核：扫描 manuscript/ 与 templates/ 中的 第N章 / 附录X / 模板NN 引用，校验目标存在性。"""
import re, os, glob

# 定位仓库根目录（脚本在 scripts/ 下，取上一级）
_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not os.path.isdir(os.path.join(_root, "manuscript")):
    _root = os.getcwd()
os.chdir(_root)

# 目标清单
chapters = {int(re.match(r"ch(\d+)-", f).group(1)) for f in os.listdir("manuscript") if re.match(r"ch\d+-", f)}
templates = {int(re.match(r"(\d+)-", f).group(1)) for f in os.listdir("templates") if re.match(r"\d+-", f)}
appx = {re.match(r"appx-([a-z]+)-", f).group(1).upper() for f in os.listdir("manuscript") if re.match(r"appx-[a-z]+-", f)}

files = sorted(glob.glob("manuscript/*.md") + glob.glob("templates/*.md") + ["HANDOFF.md"])

pat_ch = re.compile(r"第\s*(\d{1,2})\s*章")
pat_tp = re.compile(r"模板\s*(\d{1,2})")
pat_ax = re.compile(r"附录\s*([A-Z]{1,2})\b")

issues, refs_missing_target = [], []
for fp in files:
    if fp.endswith("00-outline.md"):
        continue  # 目录是计划清单，允许前向引用
    text = open(fp, encoding="utf-8").read()
    for m in pat_ch.finditer(text):
        n = int(m.group(1))
        if n not in chapters:
            refs_missing_target.append((fp, f"第{n}章", "章节文件不存在"))
    for m in pat_tp.finditer(text):
        n = int(m.group(1))
        if n not in templates:
            refs_missing_target.append((fp, f"模板{n}", "模板文件不存在"))
    for m in pat_ax.finditer(text):
        L = m.group(1)
        if L not in appx:
            refs_missing_target.append((fp, f"附录{L}", "附录文件不存在"))

print("== 缺失目标的引用（按文件） ==")
from collections import defaultdict
agg = defaultdict(list)
for fp, ref, why in refs_missing_target:
    agg[(ref, why)].append(fp)
for (ref, why), fps in sorted(agg.items()):
    print(f"{ref} ({why}) <- {len(fps)} 处: {', '.join(sorted(set(fps)))}")

# 反向：存在但目录未登记的章节/附录文件
outline = open("manuscript/00-outline.md", encoding="utf-8").read()
print("\n== 文件存在但目录正文未提及文件名 ==")
for f in sorted(os.listdir("manuscript")):
    if f == "00-outline.md":
        continue
    if f not in outline:
        print("manuscript/" + f)

# 章节号语义抽查：附录字母与主题的对应是否与 HANDOFF 锁定一致
print("\n== 现有附录字母 ==", "".join(sorted(appx)))
print("== 现有章节 ==", sorted(chapters))
print("== 现有模板 ==", sorted(templates))
