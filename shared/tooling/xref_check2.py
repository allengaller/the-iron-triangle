#!/usr/bin/env python3
"""节号级交叉引用校验：附录 X.Y 引用、章内 X.Y 节引用。"""
import os, re, glob

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 仓库根
ROOT = os.path.join(REPO, "books", "the-tam-book")                                  # 书稿目录
MS = ROOT                                                                           # 书稿已扁平到书根
BOOK_MD = re.compile(r"(?:ch\d|appx-|tpl-\d|00-|99-|DIATAXIS-MAP)")

_appx_all = {}
for f in glob.glob(os.path.join(MS, "appx-*.md")):
    _appx_all.setdefault(re.match(r"appx-([a-z]+)-", os.path.basename(f)).group(1).upper(), []).append(f)
# 落地件（*-howto.md）不承载 X.y 条文节号；节号索引一律取主件
appx = {L: (sorted([f for f in fs if not f.endswith("-howto.md")]) or sorted(fs))[0]
        for L, fs in _appx_all.items()}

def section_set(path, letter):
    secs = set()
    try:
        text = open(path, encoding="utf-8").read()
    except Exception:
        return secs
    for m in re.finditer(rf"(?m)^#+\s*{letter}\.(\d+(?:\.\d+)?)", text):
        secs.add(m.group(1))
    return secs

appx_secs = {L: section_set(f, L) for L, f in appx.items()}

# 章节内节号索引。改号后每章一个文件，节号形如 13.5，无 plus 变体。
ch_files = {}
for f in glob.glob(os.path.join(MS, "ch*.md")):
    n = int(re.match(r"ch(\d+)-", os.path.basename(f)).group(1))
    ch_files.setdefault(n, []).append(f)

ch_secs = {}
for n, fs in ch_files.items():
    secs = set()
    for f in fs:
        text = open(f, encoding="utf-8").read()
        secs |= set(re.findall(rf"(?m)^#+\s*{n}\.(\d+(?:\.\d+)?)", text))
    ch_secs[n] = secs

issues = []
files = sorted(f for f in glob.glob(os.path.join(MS, "*.md"))
               if BOOK_MD.match(os.path.basename(f)))

for path in files:
    base = os.path.basename(path)
    own_letter = None
    m = re.match(r"appx-([a-z]+)-", base)
    if m:
        own_letter = m.group(1).upper()
    lines = open(path, encoding="utf-8").read().splitlines()
    for i, line in enumerate(lines, 1):
        # 附录 X.Y 显式引用
        for mm in re.finditer(r"附录\s*([A-Z]{1,2})\.(\d+(?:\.\d+)?)", line):
            L, s = mm.group(1), mm.group(2)
            if L in appx_secs:
                ok = s in appx_secs[L] or s.split(".")[0] in appx_secs[L]
                if not ok:
                    issues.append((base, i, mm.group(0), f"附录 {L} 无节 {s}"))
        # 本附录内部 X.Y 引用（非标题行）
        if own_letter and not line.startswith("#"):
            for mm in re.finditer(rf"(?<![A-Za-z0-9]){own_letter}\.(\d+\.\d+)", line):
                s = mm.group(1)
                if s not in appx_secs[own_letter] and s.split(".")[0] not in appx_secs[own_letter]:
                    issues.append((base, i, mm.group(0), f"本附录无节 {s}"))
        # 章内节引用（形如 13.5 节）。旧 N+.M 形态已随改号清零：若残留 N+.M 节
        # 引用，下面的普通规则不会匹配它，故单独拦截报错。
        for mm in re.finditer(r"(?<![\d.])(\d{1,2})\+\.(\d{1,2})\s*节", line):
            issues.append((base, i, mm.group(0), "旧 N+.M 节号形态残留（应已改号）"))
        for mm in re.finditer(r"(?<![\d.+])(\d{1,2})\.(\d{1,2})\s*节", line):
            n, s = int(mm.group(1)), mm.group(2)
            if n in ch_secs and s not in ch_secs[n]:
                issues.append((base, i, mm.group(0), f"ch{n:02d} 无 {n}.{s} 节"))

print(f"节号级问题 {len(issues)} 条\n")
seen = set()
for base, ln, ref, msg in issues:
    key = (base, ref)
    if key in seen:
        continue
    seen.add(key)
    print(f"{base}:{ln} {ref} — {msg}")
