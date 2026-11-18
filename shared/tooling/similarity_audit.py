#!/usr/bin/env python3
"""跨文件同构审计：检测批量生产的痕迹。

为什么需要这个脚本：单文件内的 n-gram 重复只能发现"自己抄自己"。本书真正
的问题在文件之间——13 个"落地件"骨架相同、篇幅相近、动作序列一样。这类
同构在单文件指标里完全隐形，却正是"可审计性驱逐可读性"最直接的产物：
一份模板套十三遍，每份都合格，合起来是同一份。

两种口径，回答两个不同问题：

1. 文本重合（containment）：A 的 12 字片段有多大比例出现在 B 中。
   用包含率而非 Jaccard，因为长短文件对比时 Jaccard 会系统性偏低。
   它回答"这两份是不是同一篇文章的变体"。

2. 骨架同构（skeleton）：二级标题归一化后的 Jaccard 相似度。
   它回答"这两份是不是同一套模板套出来的"。文本可以改写，骨架很难改。

用法：
    python3 shared/tooling/similarity_audit.py              # 全部文件对，按重合排序
    python3 shared/tooling/similarity_audit.py --min 0.3    # 只看高重合对
    python3 shared/tooling/similarity_audit.py --report     # 写 Markdown 报告
    python3 shared/tooling/similarity_audit.py --only appx  # 只看附录
"""
from __future__ import annotations

import argparse
import itertools
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]           # 仓库根（脚本在 shared/tooling/）
ROOT = REPO / "books" / "the-tam-book"               # 默认书稿目录，--book 可切
REPORT = REPO / "shared" / "review" / "the-tam-book" / "similarity-audit.md"
MS = ROOT                                            # 书稿已扁平到书根，模板用 tpl- 前缀区分

# 同构审计三书通用。跨书同构目前只比单书内部：跨书对比需先解决命名与体裁对齐。
BOOKS = {"tam": "the-tam-book", "sa": "the-sa-book", "bte": "the-bte-book"}


def select_book(name: str) -> None:
    global ROOT, MS, REPORT
    ROOT = REPO / "books" / BOOKS[name]
    MS = ROOT
    REPORT = REPO / "shared" / "review" / BOOKS[name] / "similarity-audit.md"


def run_all(args) -> int:
    """--book all：逐书起子进程，各写一份台账。"""
    rc = 0
    for name in BOOKS:
        cmd = [sys.executable, str(Path(__file__)), "--book", name]
        if args.report:
            cmd.append("--report")
        if args.min:
            cmd += ["--min", str(args.min)]
        if args.only:
            cmd += ["--only", args.only]
        rc = max(rc, subprocess.call(cmd))
    return rc
CJK = re.compile(r"[\u4e00-\u9fff]")

SHINGLE = 12          # 片段长度，与 BTE 书重叠审计口径一致
TEXT_MIN = 0.12       # 文本重合警戒线（整文件对比天然偏低，0.12 已属可疑）
SKELETON_EXACT = 0.999  # 骨架完全相同
REPLICA_TEXT = 0.10   # 同构簇内文本重合中位数超过此值 → 判为复刻


def cluster(pairs: list[tuple[float, str, str]]) -> list[list[str]]:
    """把骨架完全相同的文件并成簇（并查集）。"""
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for _, a, b in pairs:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    groups: dict[str, list[str]] = {}
    for x in parent:
        groups.setdefault(find(x), []).append(x)
    return [sorted(g) for g in groups.values() if len(g) > 1]


def load(path: Path) -> tuple[str, set[str], set[str]]:
    text = path.read_text(encoding="utf-8")
    chars = "".join(CJK.findall(text))
    shingles = {chars[i:i + SHINGLE] for i in range(max(len(chars) - SHINGLE + 1, 0))}
    # 骨架：只取二级标题，去掉编号与序号词，留下结构语义
    heads = set()
    for line in text.splitlines():
        if line.startswith("## "):
            h = re.sub(r"^##\s*", "", line)
            h = re.sub(r"^[0-9A-Za-z+.]+\s*", "", h)
            h = re.sub(r"[：:].*$", "", h)
            heads.add(h.strip())
    return text, shingles, heads


def containment(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / min(len(a), len(b))


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--min", type=float, default=0.0, help="只显示文本重合不低于该值的文件对")
    ap.add_argument("--report", action="store_true", help="写入 Markdown 报告")
    ap.add_argument("--only", metavar="PREFIX", help="只比较文件名以该前缀开头的文件")
    ap.add_argument("--book", default="tam", choices=[*BOOKS, "all"],
                    help="被审计的书：tam（默认）/ sa / bte / all")
    args = ap.parse_args()

    if args.book == "all":
        return run_all(args)
    select_book(args.book)

    files = sorted(p for p in MS.glob("*.md")
                   if not p.name.startswith(("00-outline", "DIATAXIS", "tpl-", "README", "CHANGELOG")))
    if args.only:
        files = [p for p in files if p.name.startswith(args.only)]

    docs = {p.name: load(p) for p in files}
    pairs = []
    exact = []
    for a, b in itertools.combinations(docs, 2):
        ta, sa, ha = docs[a]
        tb, sb, hb = docs[b]
        c = containment(sa, sb)
        j = jaccard(ha, hb)
        if j >= SKELETON_EXACT:
            exact.append((c, a, b))
        elif c >= args.min:
            pairs.append((c, j, a, b))

    pairs.sort(reverse=True)
    clusters = cluster([(c, a, b) for c, a, b in exact])

    def zh(name: str) -> int:
        return len(CJK.findall(docs[name][0]))

    if args.report:
        lines = [f"# 跨文件同构审计（{REPORT.parent.name}）", "",
                 "> `python3 shared/tooling/similarity_audit.py --report`（可复跑，勿手改）",
                 "> 口径见 `QUALITY-GATE.md`。", "",
                 f"样本 {len(docs)} 个文件｜比较 {len(docs) * (len(docs) - 1) // 2} 对"
                 f"｜骨架完全相同 {len(exact)} 对｜同构簇 {len(clusters)} 个", "",
                 "## 一、同构簇：骨架完全相同", "",
                 "骨架相同不等于缺陷。本书内涵篇本就统一“定义→分级→训练→自检”四段，"
                 "那是设计选择。真正要判的是两件事：文字是不是抄的（文本重合），"
                 "以及是不是同一个模板批量填出来的（成员数 + 字数跨度）。", ""]
        if not clusters:
            lines.append("无。")
        else:
            lines += ["| 文件数 | 字数区间 | 文本重合中位 | 判定 | 成员 |", "|---|---|---|---|---|"]
            for g in sorted(clusters, key=len, reverse=True):
                vals = [c for c, a, b in exact if a in g and b in g]
                med = sorted(vals)[len(vals) // 2] if vals else 0.0
                zs = [zh(x) for x in g]
                span_ratio = (max(zs) - min(zs)) / max(zs) if max(zs) else 0.0
                if med >= REPLICA_TEXT:
                    verdict = "复刻"
                elif len(g) >= 5 and span_ratio <= 0.25:
                    verdict = "批量填充"
                else:
                    verdict = "统一体例"
                span = f"{min(zs)}–{max(zs)}" if min(zs) != max(zs) else str(zs[0])
                members = "、".join(x.replace("appx-", "").replace(".md", "") for x in g)
                lines.append(f"| {len(g)} | {span}（跨度 {span_ratio:.0%}） | {med:.2f} | {verdict} | {members} |")

        lines += ["", f"## 二、文本重合 ≥ {TEXT_MIN} 的文件对（非同构簇）", "",
                  "这一栏抓的是“换个标题重发”的情形：骨架不同，但文字大量重合。", ""]
        hot = [(c, 1.0, a, b) for c, a, b in exact if c >= TEXT_MIN] + [p for p in pairs if p[0] >= TEXT_MIN]
        hot.sort(reverse=True)
        if not hot:
            lines.append("无。")
        else:
            lines += ["| 文本重合 | 骨架同构 | A | B |", "|---|---|---|---|"]
            for c, j, a, b in hot:
                lines.append(f"| {c:.2f} | {j:.2f} | {a} | {b} |")

        lines += ["", "## 三、口径与盲区", "",
                  f"- 文本重合：{SHINGLE} 字片段的包含率（A 的片段有多少出现在 B 中）。"
                  "用包含率而非 Jaccard，因为长短文件对比时 Jaccard 系统性偏低。",
                  "- 骨架同构：二级标题去掉编号与冒号后取 Jaccard。文本可以改写，骨架很难改。",
                  "- 测不到同义改写：换词复述、调换小节顺序、重写标题都会拉低分数。",
                  "- 不判断质量：两份同构文件可能都很好，也可能都很差，需人工看。",
                  "- 不同体裁不该同构。若两个不同 Diátaxis 类型的文件骨架相同，优先怀疑标注有误。", ""]
        out = REPORT
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"报告已写入 {out.relative_to(REPO)}（同构簇 {len(clusters)} 个 / 文本重合超线 {len(hot)} 对）")
        return 0

    print(f"样本 {len(docs)}｜比较 {len(docs) * (len(docs) - 1) // 2} 对"
          f"｜骨架完全相同 {len(exact)} 对｜同构簇 {len(clusters)} 个")
    print("同构簇：")
    for g in sorted(clusters, key=len, reverse=True):
        print(f"  {len(g):>2} 个: " + "、".join(x.replace("appx-", "").replace(".md", "") for x in g))
    print("\n文本重合最高的 20 对：")
    allp = sorted([(c, 1.0, a, b) for c, a, b in exact] + pairs, reverse=True)
    for c, j, a, b in allp[:20]:
        print(f"{c:>6.2f}{j:>6.2f}  {a} / {b}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
