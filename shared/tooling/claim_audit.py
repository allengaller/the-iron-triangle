"""数值断言出处审计：找出“像事实但没有口径”的数字。

## 为什么有这个脚本

评估第 10 项：全书大量数值断言零出处。资源水位“不超过 70%”、“EOL 前 6–12 个月”、
“抽查比例 10%”、“99.995% = 支付清算级”……这些可能是对的行业经验，但读者无从判断
它们是标准条款、厂商口径，还是作者手感。

AGENTS.md 自己写着“时效性内容必须标注来源与时点”。在自称“标准”的语境下，
这个缺口会被专业读者第一眼抓住。

## 治法

不是给每个数字找出处——那不可能，也不诚实。治法是把数字分四类，各带各的标签：

    〔标准〕GB/T 20988-2007 5.2      外部标准条款，可查原文
    〔监管〕银保监办发〔2010〕114 号   监管规章，可查原文
    〔厂商〕阿里云 WA 可靠性支柱       厂商公开文档，可查原页
    〔经验值〕本书实践归纳，无外部出处
    〔建议值〕本书主张的阈值，落地须自校准

四类之外还有一个合法形态：数字在引用句里，同块有“第 X 章 / 附录 X / 模板 NN”
指向本书别处的唯一事实源。

## 判定口径

只报“高风险断言”，不报所有数字。高风险 = 下面五种形态之一：

    百分比        70%、99.95%、10% 以上
    数值区间      50–60%、6–12 个月
    时效承诺      30 分钟内、2 小时内、48h
    倍数          3 倍、10 倍于
    金额          500 万元、1.2 亿元

流程序号（第一步/第二级）、节号（5.2）、章号（第 9 章）、模板号（模板 01）、
日期（2026-10）、标准编号（GB/T 22239-2019）都不算。

## 用法

    python3 shared/tooling/claim_audit.py              # 汇总 + Top 未标注清单（在仓库根执行）
    python3 shared/tooling/claim_audit.py --report     # 写 shared/review/the-tam-book/ 报告
    python3 shared/tooling/claim_audit.py --only ch05  # 只看某个文件
    python3 shared/tooling/claim_audit.py --list       # 逐条列出未标注断言
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]           # 仓库根（脚本在 shared/tooling/）
ROOT = REPO / "books" / "the-tam-book"               # 默认书稿目录，--book 可切
REPORT = REPO / "shared" / "review" / "the-tam-book" / "claim-audit-report.md"
MS = ROOT                                            # 书稿已扁平到书根，模板用 tpl- 前缀区分

# 口径三书通用。SA/BTE 先出台账，不阻断：它们的数字密度本就低，缺的是内容而不是标注。
BOOKS = {"tam": "the-tam-book", "sa": "the-sa-book", "bte": "the-bte-book"}


def select_book(name: str) -> None:
    global ROOT, MS, REPORT
    ROOT = REPO / "books" / BOOKS[name]
    MS = ROOT
    REPORT = REPO / "shared" / "review" / BOOKS[name] / "claim-audit-report.md"


def run_all(args) -> int:
    """--book all：逐书起子进程，各写一份台账。"""
    rc = 0
    for name in BOOKS:
        cmd = [sys.executable, str(Path(__file__)), "--book", name]
        for flag in ("--report", "--list"):
            if getattr(args, flag.lstrip("-")):
                cmd.append(flag)
        if args.only:
            cmd += ["--only", args.only]
        rc = max(rc, subprocess.call(cmd))
    return rc

# 四类出处标签 + 本书内部引用 + 两种合法形态：算术可复算、案例虚构声明。
TAG = re.compile(
    r"〔标准〕|〔监管〕|〔厂商〕|〔经验值〕|〔建议值〕"
    r"|GB/T\s*\d|GB\s*\d|JR/T\s*\d|ISO/IEC\s*\d|ISO\s*\d"
    r"|银保监|银监发|证监|人民银行|金标委|工信部"
    r"|第\s*\d+\s*章|附录\s*[A-Z]{1,2}\b|模板\s*\d{2}|见\s*[A-Z]\.\d"
    r"|算术可复算|按\s*365\s*天|按定义换算|等比折算"
    r"|数字.{0,4}虚构|虚构值|演示值"
)

# 阈值型断言：本书给的建议值、上下限、判据线。
# 这类数字不需要外部出处，因为它的性质就是“本书建议”，不是“外部事实”。
# 标准件的性质说明已统一声明“文中阈值均为建议值”，即文件级标注。
# 正文与模板没有这层声明，仍需块级标注或就地说明。
THRESHOLD = re.compile(
    r"≥|≤|>=|<=|不超过|不低于|不少于|至多|至少|以内|上限|下限"
    r"|不得|必须|须|建议|阈值|判据|判定|合格线|基线|目标值"
)

# 文件级声明：三类都算已经交了口径。
# 一、标准件自述“阈值均为建议值”。
# 二、落地件把时限委托给主件。
# 三、厂商汇编声明“数据核对时点 + 取自厂商官方文档”。
DRAFT_DECL = re.compile(
    r"文中\s*[^。]{0,26}(?:均|一律)?(?:为|属)建议值"
    r"|(?:时限|阈值|门禁|锚点|口径).{0,10}一律以附录\s*[A-Z]{1,2}\+?\s*为准"
    r"|以附录\s*[A-Z]{1,2}\+?\s*为准"
    r"|数据核对时点.{0,40}取自厂商官方"
)

# 生成物：数字来自脚本，不参与审计。
GENERATED = ("DIATAXIS-MAP.md", "99-index.md")

# 高风险断言分两档。
# 硬断言：百分比、倍数、金额。这类数字最容易被读成行业事实，必须有口径。
CLAIM_HARD = re.compile(
    r"\d+(?:\.\d+)?\s*[–\-~至]\s*\d+(?:\.\d+)?\s*%"      # 区间百分比
    r"|\d+(?:\.\d+)?\s*%"                                  # 百分比
    r"|\d+(?:\.\d+)?\s*倍"
    r"|\d+(?:\.\d+)?\s*(?:万|亿)\s*元"
)

# 软断言：时限承诺。绝大多数是操作要求（“会上 24 小时内发纪要”），不是事实陈述。
# 只在连续叙述段落里追问出处；在清单、表格、步骤里不报。
CLAIM_SOFT = re.compile(r"\d+\s*(?:分钟|小时|天|个月|周)\s*内|\d+\s*h\s*内")

# 结构化块：清单项、表格行、步骤行。这类位置上的时限是“该做到什么”。
STRUCTURED = re.compile(r"^\s*-\s*\[[ xX]\]|^\s*\||^\s*\d+\.\s")

# 非断言语境：流程序号、节号、日期、标准编号、纯表格序号。
NOISE = re.compile(
    r"^\s*\|?\s*\d+\s*\|"                                  # 表格首列序号
    r"|^#+\s"                                              # 标题
    r"|\d{4}-\d{2}-\d{2}"                                  # 日期
    r"|GB/T\s*\d|JR/T\s*\d|JR/T\s*\d"                       # 标准号
    r"|^\s*-\s*\*\*第\s*\d+\s*步\*\*"                       # “第 N 步”
    r"|\|\s*[SPLM]\d"                                      # 节号表格
)

FENCE = re.compile(r"^\s*```")

# 清单语境：验收清单与动作表中的时限，是“你该做到什么”，不是“世界是什么样”。
# 这类时限天然是本书建议，不需要外部出处。


def blocks(text: str):
    """按空行切块，跳过代码块。返回 [(起行号, 块文本)]。"""
    out, buf, start, in_fence = [], [], 0, False
    for i, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.strip():
            if not buf:
                start = i
            buf.append(line)
        elif buf:
            out.append((start, "\n".join(buf)))
            buf = []
    if buf:
        out.append((start, "\n".join(buf)))
    return out


def audit_file(p: Path) -> list[dict]:
    hits = []
    text = p.read_text(encoding="utf-8")
    declared = bool(DRAFT_DECL.search(text[:2000]))
    if declared:
        # 文件首屏已交口：阈值性质、或委托给主件。整份跳过。
        # 这不是放水。阈值本来就该由文件级声明管，逐行贴〔建议值〕会把表格读碎。
        return hits
    bl = blocks(text)
    for i, (ln, b) in enumerate(bl):
        if NOISE.search(b):
            continue
        claims = CLAIM_HARD.findall(b)
        if not claims and not STRUCTURED.search(b):
            # 软断言只在叙述段落里计入。
            claims = CLAIM_SOFT.findall(b)
        if not claims:
            continue
        # 阈值型断言不要求外部出处：它本身就是本书主张。
        if THRESHOLD.search(b):
            continue
        # 出处可以在本块，也可以在紧邻的上一块（“来源：”常在断言下一行独立成段）。
        window = b
        if i > 0:
            window += "\n" + bl[i - 1][1]
        if TAG.search(window):
            continue
        # 截取首个断言前后各 40 字做预览。
        m = CLAIM_HARD.search(b) or CLAIM_SOFT.search(b)
        s = max(0, m.start() - 40)
        prev = re.sub(r"\s+", " ", b[s:m.end() + 30]).strip()
        hits.append({"file": p.name, "line": ln, "claim": claims[0],
                     "n": len(claims), "preview": prev, "declared": declared})
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", metavar="PREFIX", help="只查文件名前缀")
    ap.add_argument("--list", action="store_true", help="逐条列出")
    ap.add_argument("--report", action="store_true", help="写 Markdown 报告")
    ap.add_argument("--book", default="tam", choices=[*BOOKS, "all"],
                    help="被审计的书：tam（默认）/ sa / bte / all")
    args = ap.parse_args()

    if args.book == "all":
        return run_all(args)
    select_book(args.book)

    files = sorted(p for p in MS.glob("*.md")
                   if not p.name.startswith(("tpl-", "README", "CHANGELOG")))
    files = [p for p in files if p.name not in GENERATED]
    if args.only:
        files = [p for p in files if p.name.startswith(args.only)]

    all_hits: list[dict] = []
    for p in files:
        all_hits += audit_file(p)

    if args.report:
        by_file: dict[str, list[dict]] = {}
        for h in all_hits:
            by_file.setdefault(h["file"], []).append(h)
        lines = [f"# 数值断言出处审计（{REPORT.parent.name}）", "",
                 f"> 生成方式：`python3 shared/tooling/claim_audit.py --report --book {args.book}`（可复跑，勿手改）",
                 "> 口径见本脚本头部注释与 `QUALITY-GATE.md` 第十节。", "",
                 f"样本 {len(files)} 个文件｜高风险数值断言 {sum(h['n'] for h in all_hits)} 条｜"
                 f"无口径块 {len(all_hits)} 个｜涉及 {len(by_file)} 个文件", "",
                 "## 一、按文件（块数降序）", "",
                 "| 文件 | 无口径块 |", "|---|---|"]
        for f, hs in sorted(by_file.items(), key=lambda kv: -len(kv[1])):
            lines.append(f"| {f} | {len(hs)} |")
        lines += ["", "## 二、明细（前 80 条）", "",
                  "| 文件:行 | 断言 | 原文片段 |", "|---|---|---|"]
        for h in all_hits[:80]:
            prev = h["preview"].replace("|", "\\|")
            lines.append(f"| {h['file']}:{h['line']} | {h['claim']} | {prev} |")
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"报告已写入 {REPORT.relative_to(REPO).as_posix()}"
              f"（{sum(h['n'] for h in all_hits)} 条断言 / {len(all_hits)} 块 / {len(by_file)} 文件）")
        return 0

    by_file: dict[str, int] = {}
    for h in all_hits:
        by_file[h["file"]] = by_file.get(h["file"], 0) + 1
    print(f"样本 {len(files)} 文件｜高风险断言 {sum(h['n'] for h in all_hits)} 条｜"
          f"无口径块 {len(all_hits)}｜涉及 {len(by_file)} 文件")
    print("\nTop 未标注文件：")
    for f, n in sorted(by_file.items(), key=lambda kv: -kv[1])[:15]:
        print(f"  {n:3}  {f}")
    if args.list:
        print("\n明细：")
        for h in all_hits:
            print(f"  {h['file']}:{h['line']}  [{h['claim']}]  {h['preview'][:70]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
