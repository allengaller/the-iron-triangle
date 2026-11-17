"""给自订标准件补标题与状态徽标。幂等。"""
import pathlib

MS = pathlib.Path("/Users/allengaller/Documents/GitHub/allengaller/the-tam-book/the-tam-book/manuscript")

BADGE = "> **文件状态**：本书公开草案 v0.1。无机构背书。无外部评审。无企业试点。条文可引用、可反驳、可替换。"
MARK = "**文件状态**"

# 16 份自订标准件。C 是映射表、W 是外部标准汇编，不算自订。
TARGETS = [
    "appx-g-tam-work-evaluation-standard.md",
    "appx-h-tool-platform-acceptance-standard.md",
    "appx-i-on-duty-standard.md",
    "appx-j-enablement-training-standard.md",
    "appx-k-incident-emergency-drill-standard.md",
    "appx-l-project-onboarding-standard.md",
    "appx-m-product-introduction-standard.md",
    "appx-n-tam-onsite-certification.md",
    "appx-o-tam-onsite-promotion-standard.md",
    "appx-p-tam-service-quality-standard-public-cloud.md",
    "appx-q-tam-service-quality-standard-dedicated-cloud.md",
    "appx-r-problem-retrospective-standard.md",
    "appx-s-overtime-compoff-standard.md",
    "appx-t-online-change-standard.md",
    "appx-u-ticket-management-standard.md",
    "appx-aa-tam-reporting-standard.md",
]

# 标题带副题的，把副题拆到正文首行，标题只留主名。
# value = (新 H1 行, 覆盖范围句)
TITLE_FIX = {
    "appx-m-product-introduction-standard.md": (
        "# 附录 M　TAM 产品导入标准（拟定稿）",
        "> 覆盖范围：产品能力导入与技术转移。",
    ),
    "appx-aa-tam-reporting-standard.md": (
        "# 附录 AA　TAM 报告体系标准（拟定稿）",
        "> 覆盖范围：主 TAM 与团队成员的四级报告模板，以及 AI 时代的报告实践。",
    ),
}


def main() -> None:
    changed = []
    for name in TARGETS:
        p = MS / name
        lines = p.read_text(encoding="utf-8").splitlines()
        orig = list(lines)

        # 1) 标题补（拟定稿）
        if "（拟定稿）" not in lines[1]:
            lines[1] = lines[1].rstrip() + "（拟定稿）"

        # 2) 拆副题
        if name in TITLE_FIX:
            new_h1, scope = TITLE_FIX[name]
            lines[1] = new_h1
            if not any(x.startswith("> 覆盖范围：") for x in lines):
                for i in range(2, len(lines)):
                    if lines[i].strip():
                        lines.insert(i, "")
                        lines.insert(i + 1, scope)
                        break

        # 3) 徽标插到第一个非空 blockquote 之前
        if not any(MARK in x for x in lines):
            for i in range(2, len(lines)):
                if lines[i].startswith(">"):
                    lines.insert(i, BADGE)
                    lines.insert(i + 1, ">")
                    break

        if lines != orig:
            p.write_text("\n".join(lines) + "\n", encoding="utf-8")
            changed.append(name)

    print(f"改动 {len(changed)} 份：")
    for c in changed:
        print("  " + c)


if __name__ == "__main__":
    main()
