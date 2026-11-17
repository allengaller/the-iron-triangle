#!/usr/bin/env python3
"""内容质量门禁：把"可读性"从主观评价变成可复跑的指标。

设计原则（对应 REVIEW 2026-11-10 第五节"可审计性驱逐了可读性"）：

1. 只收可计算的指标。凡不能脚本化的要求，不写进本门禁，避免再造"写得好但没人执行"的规范。
2. 每个指标都是代理指标（proxy），必须标注它测不到什么。见 QUALITY-GATE.md。
3. 阈值由基线分布决定，不由主观设定。用 --calibrate 输出分布后再回填 THRESHOLDS。
4. 分级：block（结构硬伤，必须修）/ warn（内容薄弱，记入整改台账）。

用法：
    python3 scripts/content_gate.py --calibrate        # 输出指标分布，用于定阈值
    python3 scripts/content_gate.py --report           # 生成 Markdown 门禁报告
    python3 scripts/content_gate.py --json out.json    # 输出机器可读结果
    python3 scripts/content_gate.py --strict           # 有 block 项时退出码 1
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MS = ROOT / "manuscript"

CJK = re.compile(r"[\u4e00-\u9fff]")

# 论证连接词：用于测"主张—依据"结构的存在密度，不测论证是否成立。
ARGUMENT_MARKERS = re.compile(
    r"因为|由于|所以|因此|意味着|原因|依据|证据|例如|比如|反例|否则|"
    r"前提|除非|边界|不成立|失效|代价|权衡|后果|导致|源于|说明"
)

# 失效类词：用于测"边界意识"，即作者是否承认自己的主张会失效。
FAILURE_MARKERS = re.compile(
    r"反例|不成立|失效|例外|前提是|除非|边界|代价|局限|不适用|误判|误区|常见错误"
)

# 具象标记：数字、年月、金额、比例、时效单位。表格与代码不计入，避免虚高。
CONCRETE = re.compile(
    r"\d+(?:[.,]\d+)?\s*(?:%|％|天|小时|分钟|个月|年|万元|亿元|人|次|倍|台|份|页|QPS|TPS|IOPS)"
    r"|\d{4}\s*[-年]\s*\d{1,2}"
    r"|20\d{2}\s*年"
)

# 草案徽标：标题带（拟定稿）的文件，首屏必须有状态徽标。
# 为什么需要：本书自订了十七份草案，标题里带“标准”二字。读者第一眼看到“标准”，
# 容易读成“官方标准”。徽标是标题的免责声明，删除即误导。
DRAFT_MARK = "（拟定稿）"
BADGE_KEY = "**文件状态**"
BADGE_FACTS = ("无机构背书", "无外部评审", "无企业试点", "可反驳")

# 骨架检查：把 SKILL Phase 2 的 scaffold 变成可验证项。
#
# 只认“结构可供性”，不认“标题措辞”。标题叫不叫“操作步骤”不重要，
# 有没有可执行步骤才重要。早期版本只匹配标题关键词，把一份带 12 个
# 勾选项的贡献指南判成“无验收标准”——这类假阳性会让门禁被合理无视。
SCAFFOLD = {
    # 每项 = (名称, 判定方式, 规格, 级别)
    #   keyword  正则在标题或正文命中即可
    #   checkbox 文档中 "- [ ]" 勾选项不少于规格值
    #
    # 只收“项目明文约定过、且不靠措辞就能核”的结构件：
    #   学习效果清单（AGENTS.md）、验收勾选项（How-to 定义）、表格（Reference 定义）。
    # 刻意不收“是否讲了机制/有没有误区”类判定：这类只能靠关键词，而关键词
    # 可以被动词套利——把“机制”两个字塞进标题就过。讲得好不好交给密度指标
    # 与人工通读，不交给门禁。
    "Explanation": [
        ("学习效果清单", "keyword", r"学习效果清单", "block"),
    ],
    "How-to": [
        ("操作步骤", "keyword", r"步骤|操作|做法|执行|提交|准备|流程", "block"),
        ("验收可供性", "checkbox", 3, "block"),
    ],
    "Reference": [],  # 特殊规则：至少一张表（block）+ 两个文件链接（warn）
    "Tutorial": [
        ("分步操作", "keyword", r"步骤|操作|第[一二三四五六七八九十]步", "block"),
        ("成果验证", "keyword", r"验证|验收|检查|确认", "block"),
    ],
}

# 达标线（warn）：按 Diátaxis 类型分档。
#
# 为什么必须分档：Explanation 以论证为主、清单为辅；How-to 以指令为主、
# 清单是合法形态；Reference 以表格为主。用一套阈值量四种体裁，等于用
# 错误的尺子，会重复"形式标准驱逐内容"的旧错（REVIEW 2026-11-10 第五节）。
#
# 为什么只设 warn、不设 block：block 的语义是"这份稿子还不能算完成"，
# 只能由体裁矛盾与结构破损触发（见 judge）。内容厚度是连续量，用硬阈值
# 一刀切会逼作者去凑指标——那正是本书犯过的病。
#
# 每项为 (阈值, 方向)。阈值取自 2026-11-10 对 80 个文件的 --calibrate 分布，
# 落在 p60–p80 之间：过线即优于多数同体裁文件，不过线进整改台账。
WARN = {
    "Explanation": {
        "argument_density": (0.28, ">="),   # 13 篇，中位 0.32
        "para_len": (45, ">="),             # 中位 51.5
        "list_ratio": (0.35, "<="),         # 中位 0.14
        "concrete_per_k": (1.0, ">="),      # 中位 0.35（全书最大缺口：有论断无事实）
        "failure_markers": (6, ">="),       # 中位 23
        "recap_ratio": (0.07, "<="),        # 中位 0.05
    },
    "How-to": {
        "para_len": (28, ">="),             # 36 篇，中位 28.4
        "list_ratio": (0.80, "<="),         # 中位 0.77
        "concrete_per_k": (3.0, ">="),      # 中位 3.69
        "failure_markers": (3, ">="),       # 中位 6
        "table_density": (32, "<="),        # 中位 20.9
    },
    "Reference": {
        "para_len": (35, ">="),             # 28 篇，中位 49.3
        "list_ratio": (0.65, "<="),         # 中位 0.46
        "concrete_per_k": (2.5, ">="),      # 中位 6.71
        "table_density": (30, "<="),        # 中位 15.5，表格是主体
    },
    "Tutorial": {
        "para_len": (25, ">="),             # 2 篇，中位 25.9
        "concrete_per_k": (3.0, ">="),      # 中位 7.1
        "failure_markers": (5, ">="),       # 中位 14.5
    },
}

# 与体裁无关的通用达标线。
COMMON = {
    "ngram_dup": (0.12, "<="),               # 中位 0.07，高值 = 同构模板痕迹
}

# block 级体裁判定：Explanation 若清单化率过高且几乎不含因果句，
# 说明它在用清单冒充解释——这是体裁矛盾，不是内容薄。
GENRE_CONFLICT = {
    "Explanation": (0.60, 0.10),   # (list_ratio 上限, argument_density 下限)
}

# 回顾注水线：要点回顾占全文比重超过该值，说明正文没说完、靠复述凑篇幅。
RECAP_BLOCK = 0.15

# 外链型附录豁免内部链接要求（它们以外部文献/法规/官网为主）。
EXEMPT_SCAFFOLD = {
    "manuscript/appx-d-further-reading.md",
    "manuscript/appx-f-cloud-vendor-notices-2026.md",
    "manuscript/appx-w-financial-ops-standards.md",
}

# 法规/标准汇编类豁免 n-gram 重复：条文名称与术语必然高频复现。
EXEMPT_NGRAM = {
    "manuscript/appx-w-financial-ops-standards.md",
}

# 指标中文名，用于报告。
LABELS = {
    "argument_density": "论证密度",
    "failure_markers": "失效边界词",
    "concrete_per_k": "具象密度",
    "list_ratio": "清单化率",
    "para_len": "段落均长",
    "ngram_dup": "n-gram 重复",
    "recap_ratio": "回顾占比",
    "table_density": "表格密度",
}

# 每条问题对应的整改方向。门禁只负责指出“哪里薄”，不负责说“怎么补”；
# 但不给方向的门禁会被当成噪音，所以给最小提示，不展开成八股。
FIX_HINT = {
    "H1": "合并为单一 H1",
    "表格": "重排为列数一致的表格",
    "骨架": "补体裁必需的结构件，或改标注为正确体裁",
    "体裁矛盾": "减清单、补因果段：把断言改写成“因为…所以…”的论证",
    "回顾注水": "压缩要点回顾，把省下的篇幅还给正文",
    "论证密度": "补机制解释：每节至少回答一次“为什么会这样”",
    "具象密度": "补带来源的真实数字与时限；确实无量化对象则注明原因",
    "段落均长": "把碎片句并为完整论证段，或反过来拆分超长段",
    "失效边界词": "补失效条件：什么情况下这条主张不成立",
    "清单化率": "把清单条目展开成论证段",
    "n-gram 重复": "同构段改写：合并重复句式，换论证角度",
    "表格密度": "表格过多，改为正文论证，只留真正需要对照的表",
    "回顾占比": "压缩要点回顾",
}


def zh_len(text: str) -> int:
    return len(CJK.findall(text))


def split_blocks(text: str):
    """把文档切成 (kind, content) 块。kind ∈ heading/table/list/para/code/fence。"""
    in_fence = False
    blocks: list[tuple[str, str]] = []
    buf: list[str] = []

    def flush():
        if buf:
            blocks.append(("para", "\n".join(buf).strip()))
            buf.clear()

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.lstrip().startswith("```"):
            flush()
            in_fence = not in_fence
            blocks.append(("fence", line))
            continue
        if in_fence:
            continue
        if not line.strip():
            flush()
            continue
        if line.startswith("#"):
            flush()
            blocks.append(("heading", line.lstrip("#").strip()))
        elif line.startswith("|"):
            flush()
            blocks.append(("table", line))
        elif re.match(r"^\s*(?:[-*+] |\d+\. )", line):
            flush()
            blocks.append(("list", line.strip()))
        elif line.startswith(">"):
            flush()
            blocks.append(("para", line.lstrip("> ").strip()))
        else:
            buf.append(line)
    flush()
    return blocks


def strip_recap(text: str):
    """切出要点回顾段，返回 (正文, 回顾)。兼容 `## 本章要点回顾` 与 `**本章要点回顾**`。"""
    m = re.search(r"^(?:#+\s*|\*\*\s*)本[章附][录]?要点回顾", text, re.M)
    if not m:
        return text, ""
    return text[:m.start()], text[m.start():]


def ngram_dup(text: str, n: int = 4) -> float:
    chars = "".join(CJK.findall(text))
    if len(chars) < n * 2:
        return 0.0
    grams = [chars[i:i + n] for i in range(len(chars) - n + 1)]
    return 1 - len(set(grams)) / len(grams)


def doc_type(text: str) -> str:
    m = re.search(r"<!--\s*Diátaxis:\s*(Explanation|How-to|Reference|Tutorial)\s*-->", text)
    return m.group(1) if m else "UNKNOWN"


def check_scaffold(dtype: str, blocks, text: str = "") -> list[tuple[str, str]]:
    """按 Diátaxis 类型检查结构可供性。返回 [(级别, 缺失项)]。未知类型不判。"""
    if dtype not in SCAFFOLD:
        return []
    rules = SCAFFOLD[dtype]
    headings = "\n".join(c for k, c in blocks if k == "heading")
    body = "\n".join(c for k, c in blocks if k in ("para", "list"))
    joined = headings + "\n" + body
    missing = []
    for name, kind, spec, level in rules:
        if kind == "keyword":
            if not re.search(spec, joined, re.I):
                missing.append((level, name))
        elif kind == "checkbox":
            n = len(re.findall(r"^\s*[-*+]\s*\[[ xX]\]", text, re.M))
            if n < spec:
                missing.append((level, f"{name}（勾选项 {n} < {spec}）"))
    if dtype == "Reference":
        if not any(k == "table" for k, _ in blocks):
            missing.append(("block", "分类结构（表格）"))
        if len(re.findall(r"\]\([^)]+\.md\)", text)) < 2:
            missing.append(("warn", "交叉引用（至少 2 个文件链接）"))
    return missing


def metrics_of(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    body, recap = strip_recap(text)
    blocks = split_blocks(body)

    paras = [c for k, c in blocks if k == "para" and zh_len(c) > 0]
    lists = [c for k, c in blocks if k == "list"]
    tables = [c for k, c in blocks if k == "table"]
    body_zh = zh_len(body)
    recap_zh = zh_len(recap)

    # 论证密度按“散文段 + 清单条目”合并统计。只数段落会系统性低估清单体
    # 章节的论证量，把“用列表排版讲道理”误判成“没有讲道理”。
    arg_units = paras + [c for c in lists if zh_len(c) >= 10]
    para_lens = [zh_len(p) for p in paras]
    arg_hits = sum(1 for p in arg_units if ARGUMENT_MARKERS.search(p))
    # 具象标记按全文算（含表格）：表格中的时限、阈值、比例是真实证据。
    # 只剔代码围栏与行内序号，避免把"1. 2. 3."当具象。
    body_no_code = re.sub(r"```[\s\S]*?```", "", body)
    concrete = len(CONCRETE.findall(body_no_code))

    content_lines = len([c for k, c in blocks if k in ("para", "list")] )
    # 段落可能跨行，用块数近似行数会失真；改用原始行统计
    raw_lines = [l for l in body.splitlines() if l.strip() and not l.startswith(("|", "#", "|"))]
    list_lines = [l for l in raw_lines if re.match(r"^\s*(?:[-*+] |\d+\. )", l)]
    denom = max(len([l for l in raw_lines if not l.lstrip().startswith("```")]), 1)

    dtype = doc_type(text)
    return {
        "file": path.relative_to(ROOT).as_posix(),
        "type": dtype,
        "zh": zh_len(text),
        "argument_density": round(arg_hits / len(arg_units), 3) if arg_units else 0.0,
        "failure_markers": len(FAILURE_MARKERS.findall(body)),
        "concrete_per_k": round(concrete / max(body_zh, 1) * 1000, 2),        "list_ratio": round(len(list_lines) / denom, 3),
        "para_len": round(statistics.mean(para_lens), 1) if para_lens else 0.0,
        "ngram_dup": round(ngram_dup(body), 3),
        "recap_ratio": round(recap_zh / max(zh_len(text), 1), 3),
        "table_density": round(len(tables) / max(body_zh, 1) * 1000, 2),
        "images": text.count("!["),
        "scaffold_missing": check_scaffold(dtype, blocks, text),
        "exempt": path.relative_to(ROOT).as_posix() in EXEMPT_SCAFFOLD,
        "exempt_ngram": path.relative_to(ROOT).as_posix() in EXEMPT_NGRAM,
        "has_h1": sum(1 for l in text.splitlines() if l.startswith("# ")) == 1,
        "table_malformed": malformed_tables(text),
    }


def draft_badge_issues(files: list[Path]) -> list[dict]:
    """标题与徽标必须成对：有拟定稿必有徽标，有徽标必有拟定稿。

    徽标四句缺一也算 block。理由是四句分别对应四种被追问的方式：
    谁背书、谁评过、哪里试过、能不能反驳。删掉一句，免责就不完整。
    """
    out = []
    for p in files:
        lines = p.read_text(encoding="utf-8").splitlines()
        # H1 在第 1 行或第 2 行（首行可能是 Diátaxis 注释）。
        idx = 0 if lines and lines[0].startswith("# ") else 1
        title = lines[idx] if len(lines) > idx else ""
        is_draft = DRAFT_MARK in title
        badge_line = next((x for x in lines[:14] if BADGE_KEY in x), "")

        # 更根本的一条：自订标准件即使忘写（拟定稿），也要拦。
        # 判据看标题结尾：以“标准”或“标准（…版）”收尾的是自订件。
        # 附录 C“方法论与标准映射”、附录 W“…要求汇编”不是自订件。
        body = title.replace(DRAFT_MARK, "").split("　", 1)[-1].strip()
        looks_standard = bool(re.search(r"标准(（[^）]*）)?$", body))

        if looks_standard and not is_draft:
            out.append({"level": "block", "file": p.name, "type": "——", "zh": 0,
                        "issues": [("block", "草案标题缺标注",
                                    "标题以“标准”收尾但无（拟定稿）")]})
            continue
        if is_draft and not badge_line:
            out.append({"level": "block", "file": p.name, "type": "——", "zh": 0,
                        "issues": [("block", "草案徽标缺失",
                                    "标题带（拟定稿）但首屏无状态徽标")]})
            continue
        if badge_line and not is_draft:
            out.append({"level": "block", "file": p.name, "type": "——", "zh": 0,
                        "issues": [("block", "草案徽标多余",
                                    "有状态徽标但标题无（拟定稿）")]})
            continue
        if badge_line:
            missing = [f for f in BADGE_FACTS if f not in badge_line]
            if missing:
                out.append({"level": "block", "file": p.name, "type": "——", "zh": 0,
                            "issues": [("block", "草案徽标不完整",
                                        "缺：" + "、".join(missing))]})
    return out


def malformed_tables(text: str) -> int:
    """表格管道列数不一致的行数。"""
    bad, block, in_fence = 0, [], False
    for line in text.splitlines() + [""]:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("|") and line.endswith("|"):
            block.append(line)
        else:
            if len(block) >= 2 and re.match(r"^\|(?:\s*:?-+:?\s*\|)+$", block[1]):
                expected = block[0].count("|")
                bad += sum(1 for b in block if b.count("|") != expected)
            block = []
    return bad


def judge(m: dict) -> list[tuple[str, str, str]]:
    """返回 [(级别, 指标, 说明)]。

    分级原则是本门禁最重要的一条设计：\n
      block = 体裁矛盾或结构破损。文件因此不能算完成品，当期必修。
      warn  = 内容厚度不足。系统性差距，进整改台账，不阻断发布。

    block 只收“能不能用”，不收“写得好不好”。可读性没法被一条阈值定义，
    用量化阈值去卡“写得好不好”，正是本门禁要修的那个病。
    """
    out = []
    if not m["has_h1"]:
        out.append(("block", "H1", "不唯一"))
    if m["table_malformed"]:
        out.append(("block", "表格", f"{m['table_malformed']} 行管道列数不一致"))

    # 骨架缺失：逐项按声明好的级别入册。缺结构件属结构破损（block），
    # 缺理想节属厚度不足（warn）。
    if not m["exempt"]:
        for level, name in m["scaffold_missing"]:
            out.append((level, "骨架", f"缺：{name}"))

    if m["type"] in GENRE_CONFLICT:
        list_max, arg_min = GENRE_CONFLICT[m["type"]]
        if m["list_ratio"] > list_max and m["argument_density"] < arg_min:
            out.append(("block", "体裁矛盾",
                        f"清单化率 {m['list_ratio']} > {list_max} 且论证密度 "
                        f"{m['argument_density']} < {arg_min}"))
        if m["recap_ratio"] > RECAP_BLOCK:
            out.append(("block", "回顾注水", f"{m['recap_ratio']} > {RECAP_BLOCK}"))

    if m["type"] not in WARN:
        return out  # 导读等非章节文件只做结构检查

    rules = dict(WARN[m["type"]])
    for k, v in COMMON.items():
        rules.setdefault(k, v)

    for key, (limit, direction) in rules.items():
        if key not in m:
            continue
        if key == "ngram_dup" and m["exempt_ngram"]:
            continue
        v = m[key]
        label = LABELS.get(key, key)
        if direction == ">=":
            if v < limit:
                out.append(("warn", label, f"{v} < {limit}"))
        else:
            if v > limit:
                out.append(("warn", label, f"{v} > {limit}"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibrate", action="store_true", help="输出指标分布，用于回填阈值")
    ap.add_argument("--report", action="store_true", help="生成 Markdown 报告")
    ap.add_argument("--json", metavar="PATH", help="写出 JSON 结果")
    ap.add_argument("--strict", action="store_true", help="存在 block 项时退出码 1")
    ap.add_argument("--only", metavar="PREFIX", help="只检查文件名前缀匹配的文件")
    args = ap.parse_args()

    files = sorted(p for p in MS.glob("*.md") if not p.name.startswith("00-outline")
                   and not p.name.startswith("DIATAXIS"))
    if args.only:
        files = [p for p in files if p.name.startswith(args.only)]

    rows = [metrics_of(p) for p in files]

    if args.calibrate:
        keys = ["argument_density", "failure_markers", "concrete_per_k", "list_ratio",
                "para_len", "ngram_dup", "recap_ratio", "table_density"]
        print(f"样本 {len(rows)} 个文件\n")
        print(f"{'指标':<18}{'min':>8}{'p25':>8}{'中位':>8}{'p75':>8}{'max':>8}")
        for k in keys:
            vals = sorted(r[k] for r in rows if isinstance(r.get(k), (int, float)))
            if not vals:
                continue
            q = statistics.quantiles(vals, n=4)
            print(f"{k:<18}{vals[0]:>8.2f}{q[0]:>8.2f}{q[1]:>8.2f}{q[2]:>8.2f}{vals[-1]:>8.2f}")
        print("\n按类型的中位值：")
        for dtype in WARN:
            sub = [r for r in rows if r["type"] == dtype]
            if not sub:
                continue
            print(f"  {dtype}（{len(sub)} 篇）")
            for k in WARN[dtype]:
                vals = sorted(r[k] for r in sub)
                print(f"    {k:<18} 中位 {statistics.median(vals):>7.2f}  min {vals[0]:>6.2f}  max {vals[-1]:>7.2f}")
        print("\n骨架缺失统计：")
        for r in rows:
            if r["scaffold_missing"]:
                items = "、".join(f"[{lv}]{n}" for lv, n in r["scaffold_missing"])
                print(f"  {r['file']:<52} {r['type']:<12} {items}")
        return 0

    for r in rows:
        r["issues"] = judge(r)

    # 草案徽标是文件级一致性检查，不进内容厚度统计，单独并入。
    for bad in draft_badge_issues(files):
        for r in rows:
            if r["file"] == bad["file"]:
                r["issues"].extend(bad["issues"])
                break

    blocked = [r for r in rows if any(i[0] == "block" for i in r["issues"])]
    warned = [r for r in rows if not any(i[0] == "block" for i in r["issues"])
              and any(i[0] == "warn" for i in r["issues"])]
    clean = [r for r in rows if not r["issues"]]

    if args.json:
        Path(args.json).write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.report:
        lines = ["# 内容质量门禁报告", "",
                 "> 生成方式：`python3 scripts/content_gate.py --report`（可复跑，勿手改）",
                 "> 口径与盲区见 `QUALITY-GATE.md`；本节报告只举证，不代替人工通读。", "",
                 f"样本 {len(rows)} 个文件｜block {len(blocked)}｜warn {len(warned)}｜通过 {len(clean)}", "",
                 "## 一、block：体裁矛盾与结构破损（当期必修）", ""]
        if not blocked:
            lines.append("无。")
        else:
            lines += ["| 文件 | 类型 | 中文字 | 问题 | 整改方向 |", "|---|---|---|---|---|"]
            for r in blocked:
                for lv, name, detail in r["issues"]:
                    if lv != "block":
                        continue
                    lines.append(f"| {r['file']} | {r['type']} | {r['zh']} | "
                                 f"{name} {detail} | {FIX_HINT.get(name, '')} |")

        lines += ["", "## 二、warn：内容厚度（进整改台账，不阻断发布）", ""]
        if not warned:
            lines.append("无。")
        else:
            lines += ["| 文件 | 类型 | 中文字 | 差距 | 整改方向 |", "|---|---|---|---|---|"]
            for r in warned:
                items = "<br>".join(f"{n} {d}" for lv, n, d in r["issues"] if lv == "warn")
                hints = "；".join(dict.fromkeys(FIX_HINT.get(n, "") for lv, n, _ in r["issues"] if lv == "warn"))
                lines.append(f"| {r['file']} | {r['type']} | {r['zh']} | {items} | {hints} |")

        lines += ["", "## 三、达标线（可调，但调阈须重跑 --calibrate 并记入 HANDOFF）", ""]
        for dtype, rules in WARN.items():
            lines += [f"### {dtype}", "", "| 指标 | 达标线 | 方向 |", "|---|---|---|"]
            for k, (v, d) in rules.items():
                lines.append(f"| {LABELS.get(k, k)} | {v} | {d} |")
            lines.append("")
        lines += ["### 通用", "", "| 指标 | 达标线 | 方向 |", "|---|---|---|",
                  *[f"| {LABELS.get(k, k)} | {v} | {d} |" for k, (v, d) in COMMON.items()], ""]

        out = ROOT / "content-gate-report.md"
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"报告已写入 content-gate-report.md（block {len(blocked)} / warn {len(warned)} / 通过 {len(clean)}）")
    else:
        print(f"样本 {len(rows)}｜block {len(blocked)}｜warn {len(warned)}｜通过 {len(clean)}")
        for r in rows:
            if r["issues"]:
                print(f"  {'[B]' if any(i[0]=='block' for i in r['issues']) else '[W]'} "
                      f"{r['file']:<52} " + "；".join(f"{i[1]} {i[2]}" for i in r["issues"]))

    if args.strict and blocked:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
