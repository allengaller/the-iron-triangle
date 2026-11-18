#!/usr/bin/env python3
"""renumber_remap.py — 一次性章号重写（旧 N / N+ 体系 → 新 1–38 顺序编号）。

历史脚本：2026-11-03 已完成，仅留档；路径按当时的 manuscript/、templates/
子目录结构编写，2026-11-18 扁平化后不再直接运行。

设计约束：
- 单遍 re.sub + 回调映射。旧号被复用（旧 6→新 7，新 6=旧 5+），链式替换必串号。
- 同一位置多规则竞争时，长者/具体者优先（枚举 > 范围 > 连号 > 带+ > 单号）。
- 只处理引用形态（第 N 章 / N+.M / N.M 节 / 见 N.M / 文件名 / 章文件标题行），
  绝不碰数值数据（12.31、8.8 小时、99.9%）与模板内部节号（### 2.1，仅章文件启用标题规则）。

用法：
  python3 tooling/renumber_remap.py --dry-run     # 输出 unified diff（仅历史参考）
  python3 tooling/renumber_remap.py               # 就地改写
"""
import argparse
import difflib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]           # 仓库根（历史脚本，路径按当时结构）
ROOT = REPO / "books" / "the-tam-book"
MS = ROOT / "manuscript"
TP = ROOT / "templates"

# 旧章号 -> 新章号（1–5 恒等）
CH = {
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5,
    6: 7, 7: 9, 8: 11, 9: 14, 10: 16,
    11: 17, 12: 18, 13: 19, 14: 20, 15: 21,
    16: 22, 17: 23, 18: 24, 19: 25, 20: 26,
    21: 27, 22: 28, 23: 30, 24: 31, 25: 33,
    26: 34, 27: 36, 28: 37,
}
# 旧 N+ 实战章 -> 新号
PLUS = {5: 6, 6: 8, 7: 10, 8: 12, 22: 29, 24: 32, 26: 35, 28: 38}

# 旧文件名（去 .md） -> 新文件名（去 .md）
SLUG = {
    "ch05-practical": "ch06-technical-depth-practical",
    "ch06-business-insight": "ch07-business-insight",
    "ch06-practical": "ch08-business-insight-practical",
    "ch07-relationship-management": "ch09-relationship-management",
    "ch07-practical": "ch10-relationship-management-practical",
    "ch08-service-governance": "ch11-service-governance",
    "ch08-practical": "ch12-service-governance-practical",
    "ch09-risk-compliance": "ch14-risk-compliance-practical",
    "ch10-project-change": "ch16-project-change-practical",
    "ch11-customer-lifecycle": "ch17-customer-lifecycle",
    "ch12-escalation-crisis": "ch18-escalation-crisis",
    "ch13-internal-collaboration": "ch19-internal-collaboration",
    "ch14-partner-ecosystem": "ch20-partner-ecosystem",
    "ch15-commercial-synergy": "ch21-commercial-synergy",
    "ch16-financial-industry": "ch22-financial-industry",
    "ch17-financial-availability": "ch23-financial-availability",
    "ch18-major-assurance": "ch24-major-assurance",
    "ch19-financial-incident": "ch25-financial-incident",
    "ch20-case-studies": "ch26-case-studies",
    "ch21-ai-workload-assurance": "ch27-ai-workload-assurance",
    "ch22-ai-for-tam": "ch28-ai-for-tam",
    "ch22-tam-copilot-tutorial": "ch29-tam-copilot-tutorial",
    "ch23-service-model-evolution": "ch30-service-model-evolution",
    "ch24-ai-risk-governance": "ch31-ai-risk-governance",
    "ch24-ai-risk-governance-howto": "ch32-ai-risk-governance-howto",
    "ch25-tam-irreplaceability": "ch33-tam-irreplaceability",
    "ch26-measurement-system": "ch34-measurement-system",
    "ch26-measurement-system-howto": "ch35-measurement-system-howto",
    "ch27-maturity-model": "ch36-maturity-model",
    "ch28-career-team-building": "ch37-career-team-building",
    "ch28-career-team-building-howto": "ch38-career-team-building-howto",
}

# 不处理的文件：仅索引（由 --index 重建）。outline 与 DIATAXIS-MAP 由本脚本改号，
# 结构性增删（新章条目、落地件条目删除）随后手工完成。
SKIP = {"99-index.md"}

# 范围端点映射特例：旧 26–28 章（度量篇主章）新号为 34–38（含 35/38 实战章），
# 纯端点映射得 34–37 会漏 38。
RANGE_OVERRIDE = {(26, 28): (34, 38)}

WARN = []


def ch(n: int) -> str:
    if n not in CH:
        WARN.append(f"章号 {n} 不在映射表")
        return str(n)
    return str(CH[n])


def plus(n: int) -> str:
    if n not in PLUS:
        WARN.append(f"实战章号 {n}+ 不在映射表")
        return f"{n}+"
    return str(PLUS[n])


# 单遍组合规则：顺序 = 同位置竞争时的优先级
PATTERN = re.compile(
    r"""
      (?P<slug>ch\d{2}-[a-z0-9-]+)                             # 1 文件名 slug（含/不含 .md）
    | 第\s*(?P<e1>\d{1,2})(?P<ep1>\+)?(?P<esep>\s*[、/]\s*)(?P<e2>\d{1,2})(?P<ep2>\+)?(?:(?P<esep2>\s*[、/]\s*)(?P<e3>\d{1,2})(?P<ep3>\+)?)?\s*章   # 2 枚举（、或 / 分隔，元素可带 +）
    | 第\s*(?P<r1>\d{1,2})\s*[–—-]\s*(?P<r2>\d{1,2})\s*章      # 3 范围
    | 第\s*(?P<c1>\d{1,2})\s*章\s+(?P<c2>\d{1,2})(?P<crest>\.\d+(?:\.\d+)*)  # 4 连号 第N章 N.M
    | 第\s*(?P<p1>\d{1,2})\+\s*章                              # 5 第 N+ 章
    | 第\s*(?P<s1>\d{1,2})\s*章                                # 6 第 N 章
    | (?<![\d.])\b(?P<bp1>\d{1,2})\+\s*章                      # 6b 裸 N+ 章（如"22+ 章"）
    | (?<![\w-])ch(?P<b1>\d{2})(?P<bplus>\+)?(?![\w-])         # 7 裸 chNN（±+）
    | (?<![\d.])(?P<ps1>\d{1,2})\+(?P<psrest>\.\d+(?:\.\d+)*)  # 8 N+.M 节号
    | (?<![\d.])(?P<sec1>\d{1,2})\.(?P<sec2>\d{1,2}(?:\.\d+)*)(?=\s*节)  # 9 N.M 节
    | 见\s*(?P<k1>\d{1,2})\.(?P<k2>\d{1,2})(?![\d.%])         # 10 见 N.M
    | （(?P<pr1>\d{1,2})\.(?P<prest>\d{1,2}(?:\.\d+)*)         # 11 （N.M 括号内联节号
    """,
    re.VERBOSE,
)

# 标题行规则（仅章文件）：## 6.1 -> ## 7.1
HEADING = re.compile(r"^(?P<hash>#{1,6}[ \t]+)(?P<n>\d{1,2})(?P<rest>\.)", re.M)


def sub_callback(m: re.Match) -> str:
    g = m.groupdict()
    if g["slug"] is not None:
        return SLUG.get(g["slug"], g["slug"])
    if g["e1"] is not None:
        n1 = plus(int(g["e1"])) if g["ep1"] else ch(int(g["e1"]))
        n2 = plus(int(g["e2"])) if g["ep2"] else ch(int(g["e2"]))
        if g["e3"]:
            n3 = plus(int(g["e3"])) if g["ep3"] else ch(int(g["e3"]))
            return f"第 {n1}{g['esep']}{n2}{g['esep2']}{n3} 章"
        return f"第 {n1}{g['esep']}{n2} 章"
    if g["r1"] is not None:
        a, b = int(g["r1"]), int(g["r2"])
        a, b = RANGE_OVERRIDE.get((a, b), (int(ch(a)), int(ch(b))))
        return f"第 {a}–{b} 章"
    if g["c1"] is not None:
        return f"第 {ch(int(g['c1']))} 章 {ch(int(g['c2']))}{g['crest']}"
    if g["p1"] is not None:
        return f"第 {plus(int(g['p1']))} 章"
    if g["s1"] is not None:
        return f"第 {ch(int(g['s1']))} 章"
    if g["bp1"] is not None:
        return f"第 {plus(int(g['bp1']))} 章"
    if g["b1"] is not None:
        # 裸 chNN(±+)：映射到新号；新体系无 "+" 号，后缀一律不保留
        base = plus(int(g["b1"])) if g["bplus"] else ch(int(g["b1"]))
        return f"ch{int(base):02d}"
    if g["ps1"] is not None:
        return plus(int(g["ps1"])) + g["psrest"]
    if g["sec1"] is not None:
        return ch(int(g["sec1"])) + "." + g["sec2"]
    if g["k1"] is not None:
        return "见 " + ch(int(g["k1"])) + "." + g["k2"]
    if g["pr1"] is not None:
        n = int(g["pr1"])
        # 仅映射真实章号；99.99%、0.99 等百分数与模板内部节号原样保留
        if n not in CH or CH[n] == n:
            return m.group(0)
        return "（" + ch(n) + "." + g["prest"]
    return m.group(0)


def heading_callback(m: re.Match, own_old: int, own_new: int) -> str:
    """只映射本文件自己的旧章号。不做全局兜底——通用规则随后会处理其余引用。"""
    n = int(m.group("n"))
    if n == own_old:
        return f"{m.group('hash')}{own_new}{m.group('rest')}"
    return m.group(0)


def process(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    # HANDOFF 是历史日志：只修文件路径引用（保持可点），章号等叙述一字不动。
    if path.name == "HANDOFF.md":
        return re.sub(
            r"ch\d{2}-[a-z0-9-]+",
            lambda m: SLUG.get(m.group(0), m.group(0)),
            text,
        )
    out = text
    # 标题行先于通用规则：改名章文件的 ## N.x -> ## M.x。
    # 顺序关键：若通用规则先把 5+.1 改成 6.1，标题规则会把 6 误当旧号再改成 7。
    if path.name.startswith("ch"):
        own_new = int(re.match(r"ch(\d+)-", path.name).group(1))
        own_old = next(
            (int(re.match(r"ch(\d+)-", k).group(1)) for k, v in SLUG.items() if v + ".md" == path.name),
            own_new,
        )
        if own_old != own_new:
            out = HEADING.sub(lambda m: heading_callback(m, own_old, own_new), out)
    return PATTERN.sub(sub_callback, out)


def targets() -> list[Path]:
    files = [p for p in sorted(MS.glob("*.md")) if p.name not in SKIP]
    files += sorted(TP.glob("*.md"))
    repo = ROOT.parents[1]
    gov = repo / "shared" / "governance"
    files += [p for p in (repo / "AGENTS.md", gov / "QUALITY-GATE.md", gov / "HANDOFF.md") if p.exists()]
    todo = repo / "shared" / "review" / "the-tam-book" / "TODO-DIATAXIS.md"
    if todo.exists():
        files.append(todo)
    return files


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    changed = 0
    for p in targets():
        old = p.read_text(encoding="utf-8")
        new = process(p)
        if old == new:
            continue
        changed += 1
        if args.dry_run:
            diff = difflib.unified_diff(
                old.splitlines(keepends=True),
                new.splitlines(keepends=True),
                fromfile=p.name,
                tofile=p.name,
            )
            sys.stdout.writelines(diff)
        else:
            p.write_text(new, encoding="utf-8")
            print(f"rewritten {p.relative_to(ROOT)}")

    mode = "dry-run，将改写" if args.dry_run else "已改写"
    print(f"\n{mode} {changed} 个文件")
    if WARN:
        print("警告：")
        for w in sorted(set(WARN)):
            print(f"  {w}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
