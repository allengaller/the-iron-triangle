# review/ — 评审、审计与发布归档

本目录在公用资产层（`shared/review/`）。带日期的评估、审计、台账，以及发布清单与发布说明统一放这里。正文与代码不在此目录。

**归档规则**：

- 文件名带日期（`*-YYYY-MM-DD.md`）表示时点快照，**不随正文改动而回改**；结论过期就新开一份。
- 少数不带日期的（`content-gate-report.md`、`similarity-audit.md`、`TODO-DIATAXIS.md`）是**可复跑的台账**，由脚本覆盖重写，不手工编辑。
- 新增报告先判断归属：跨书或仓库级进 `repo/` 或本层，单书进对应子目录。
- 截图类快照不入库：TAM 阅读站设计评审的 19 张截图与 `report.json` 在 `books/the-tam-book/.impeccable/review/`（本地，已 gitignore），重跑设计评审会重新生成。

## 仓库级

| 文件 | 日期 | 内容 |
| --- | --- | --- |
| [repo/repo-open-source-book-assessment-2026-11-18.md](repo/repo-open-source-book-assessment-2026-11-18.md) | 2026-11-18 | 仓库级十维评估：按开源技术图书最高标准评工程、治理、出版、法务与可复现性 |
| [sa-bte-depth-breadth-2026-11-18.md](sa-bte-depth-breadth-2026-11-18.md) | 2026-11-18 | SA／BTE 两书深度与广度评估，与 TAM 门禁同口径 |
| [repo/bte-book-feasibility-2026-11-02.md](repo/bte-book-feasibility-2026-11-02.md) | 2026-11-02 | BTE 书立项可行性评估，Phase 0 决策依据 |
| [repo/standards-verification-report-2026-10-25.md](repo/standards-verification-report-2026-10-25.md) | 2026-10-25 | 标准法规库逐份校验报告与问题清单 |

## the-tam-book

| 文件 | 日期 | 内容 |
| --- | --- | --- |
| [the-tam-book/the-tam-book-overall-assessment-2026-11-10.md](the-tam-book/the-tam-book-overall-assessment-2026-11-10.md) | 2026-11-10 | 全书缺陷与薄弱点评估（第三方视角通读） |
| [the-tam-book/the-tam-book-status-2026-11-17.md](the-tam-book/the-tam-book-status-2026-11-17.md) | 2026-11-17 | 状态复评：门禁六命令、字数与图表密度、同构审计现场复跑 |
| [the-tam-book/consistency-review-2026-10-25.md](the-tam-book/consistency-review-2026-10-25.md) | 2026-10-25 | 统稿一致性第一刀（构件、断链、目录、时点） |
| [the-tam-book/content-gate-report.md](the-tam-book/content-gate-report.md) | 台账 | `python3 shared/tooling/content_gate.py --report` 输出：block／warn 清单 |
| [the-tam-book/similarity-audit.md](the-tam-book/similarity-audit.md) | 台账 | `python3 shared/tooling/similarity_audit.py --report` 输出：骨架同构簇与文本重合对 |
| [the-tam-book/TODO-DIATAXIS.md](the-tam-book/TODO-DIATAXIS.md) | 台账 | Diátaxis 整改项登记与核销状态 |

## the-sa-book

| 文件 | 日期 | 内容 |
| --- | --- | --- |
| [the-sa-book/00-overlap-audit-2026-11-17.md](the-sa-book/00-overlap-audit-2026-11-17.md) | 2026-11-17 | 与 TAM 书句级重叠审计（0.5%） |

## the-bte-book

| 文件 | 日期 | 内容 |
| --- | --- | --- |
| [the-bte-book/00-phase0-review.md](the-bte-book/00-phase0-review.md) | 2026-11-03 | Phase 0 评审：读者问卷、重叠审计、模板测试、决策记录 |
| [the-bte-book/00-overlap-audit-2026-11-03.md](the-bte-book/00-overlap-audit-2026-11-03.md) | 2026-11-03 | 与 SA 书重叠审计（最高 4.9%，第 2 章除外） |
| [the-bte-book/00-reader-test-kit.md](the-bte-book/00-reader-test-kit.md) | 工具 | 试读邀请话术、问卷、评分表、汇总模板 |
| [the-bte-book/00-template-test-kit.md](the-bte-book/00-template-test-kit.md) | 工具 | 模板实测：BTE-01 任务、观察表、访谈与评分 |
| [the-bte-book/00-release-checklist.md](the-bte-book/00-release-checklist.md) | 清单 | v1.0 发布检查表 |
| [the-bte-book/release-readme.md](the-bte-book/release-readme.md) | 发布 | v1.0 发布包说明：格式、安装、引用与校验 |
| [the-bte-book/release-v1.0.md](the-bte-book/release-v1.0.md) | 发布 | v1.0 发布说明：内容、格式、已知限制与反馈 |

## 复跑方式

```bash
# 在仓库根执行
python3 shared/tooling/content_gate.py --report
python3 shared/tooling/similarity_audit.py --report
```

两份台账会直接覆盖本目录下的同名文件。其余带日期的报告只增不改。
