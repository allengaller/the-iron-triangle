#!/usr/bin/env python3
"""crossbook_remap.py — 姊妹书（SA/BTE）中指向 TAM 书的旧章号/旧文件名改写。

历史脚本：2026-11-03 已完成，仅留档；正则按当时的 the-tam-book/manuscript/
路径编写，2026-11-18 扁平化后不再直接运行。

只改两类 TAM 语境引用，SA/BTE 自有章号一律不动：
1. 带 `the-tam-book/manuscript/chXX-slug` 目标的 markdown 链接（链接文字的章号
   按目标文件的新章号同步）与裸路径。
2. 文字式 TAM 引用：`TAM 第 N 章`、`TAM 书第 N+ 章`、`《The TAM Book》第 N 章`
   （含枚举 `TAM 第 21、24 章`）。

用法：python3 crossbook_remap.py --dry-run | --apply
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # 仓库根（shared/tooling/ 上两级）

# 旧 slug -> 新 slug（与 the-tam-book/scripts/renumber_remap.py SLUG 一致）
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
# 旧章号 -> 新章号（文字引用；1–5 恒等）
CH = {
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 7, 7: 9, 8: 11, 9: 14, 10: 16,
    11: 17, 12: 18, 13: 19, 14: 20, 15: 21, 16: 22, 17: 23, 18: 24,
    19: 25, 20: 26, 21: 27, 22: 28, 23: 30, 24: 31, 25: 33, 26: 34,
    27: 36, 28: 37,
}
PLUS = {5: 6, 6: 8, 7: 10, 8: 12, 22: 29, 24: 32, 26: 35, 28: 38}

# 1) 带 TAM 目标的链接：同步链接文字章号与目标 slug
LINK = re.compile(
    r"\[([^\]]*?第\s*(\d{1,2})(\+?)\s*章[^\]]*)\]"
    r"\(([^)]*the-tam-book/manuscript/)(ch\d{2}-[a-z0-9-]+)(\.md)\)"
)
# 2) 裸 TAM 路径（含反引号）
PATH = re.compile(r"(the-tam-book/manuscript/)(ch\d{2}-[a-z0-9-]+)(\.md)")
# 3) 文字式 TAM 引用（单号 / 枚举，可带 +、可带“书”）。必须在 LINK 之前跑：
#    LINK 会把标签改成新号，新号与旧号区间重叠（如 25），再跑文字规则会双重映射。
TXT_ENUM = re.compile(
    r"(TAM\s*书?\s*第\s*|《The TAM Book》第\s*)(\d{1,2})(\+?)\s*、\s*(\d{1,2})(\+?)(\s*章)"
)
TXT_SINGLE = re.compile(
    r"(TAM\s*书?\s*第\s*|《The TAM Book》第\s*)(\d{1,2})(\+?)(\s*章)"
)
# 4) 节号式引用：该书 26.8 / 《The TAM Book》26.8（首分量是旧章号）
TXT_SEC = re.compile(
    r"(该书\s*|《The TAM Book》)(\d{1,2})\.(\d{1,2})"
)


def map_slug(old: str) -> str:
    return SLUG.get(old, old)


WARN: list[str] = []


def map_num(n: int, plus: str) -> str:
    if plus:
        if n not in PLUS:
            WARN.append(f"{n}+ 不在 PLUS 映射，原样保留")
            return f"{n}+"
        return str(PLUS[n])
    if n not in CH:
        # 已是新号（LINK 规则先跑时会产出新号）或超出旧号范围：原样保留
        return str(n)
    return str(CH[n])


def rewrite(text: str) -> str:
    def link_sub(m: re.Match) -> str:
        label, num, plus, prefix, slug, ext = m.groups()
        new_slug = map_slug(slug)
        new_num = int(new_slug[2:4])  # 从新文件名取章号
        label2 = re.sub(
            rf"(第\s*){num}(\+?)(\s*章)",
            lambda x: f"{x.group(1)}{new_num}{x.group(3)}",
            label,
            count=1,
        )
        return f"[{label2}]({prefix}{new_slug}{ext})"

    def path_sub(m: re.Match) -> str:
        prefix, slug, ext = m.groups()
        return f"{prefix}{map_slug(slug)}{ext}"

    def enum_sub(m: re.Match) -> str:
        pre, n1, p1, n2, p2, tail = m.groups()
        return f"{pre}{map_num(int(n1), p1)}、{map_num(int(n2), p2)}{tail}"

    def single_sub(m: re.Match) -> str:
        pre, n, p, tail = m.groups()
        return f"{pre}{map_num(int(n), p)}{tail}"

    def sec_sub(m: re.Match) -> str:
        pre, n, rest = m.groups()
        return f"{pre}{map_num(int(n), '')}.{rest}"

    # 顺序关键：文字规则先（旧号语境），链接规则后（标签可能已是新号，须幂等）
    text = TXT_ENUM.sub(enum_sub, text)
    text = TXT_SINGLE.sub(single_sub, text)
    text = TXT_SEC.sub(sec_sub, text)
    text = LINK.sub(link_sub, text)
    text = PATH.sub(path_sub, text)
    return text


def targets() -> list[Path]:
    files: list[Path] = []
    for book in ("the-sa-book", "the-bte-book"):
        base = ROOT / book
        files += sorted(base.rglob("*.md"))
    # 排除构建产物与 dated 记录
    return [
        p for p in files
        if "dist/" not in p.as_posix()
        and p.name not in ("00-overlap-audit-2026-11-03.md",)
        and "bte-book-feasibility" not in p.name
    ]


def main() -> int:
    apply = "--apply" in sys.argv
    changed = 0
    for p in targets():
        old = p.read_text(encoding="utf-8")
        new = rewrite(old)
        if new == old:
            continue
        changed += 1
        if apply:
            p.write_text(new, encoding="utf-8")
            print(f"rewritten {p.relative_to(ROOT)}")
        else:
            import difflib
            sys.stdout.writelines(
                difflib.unified_diff(
                    old.splitlines(keepends=True),
                    new.splitlines(keepends=True),
                    fromfile=p.name, tofile=p.name,
                )
            )
    print(f"{'已改写' if apply else '将改写'} {changed} 个文件")
    for w in sorted(set(WARN)):
        print(f"警告：{w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
