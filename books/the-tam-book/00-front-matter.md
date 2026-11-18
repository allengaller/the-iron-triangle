# 版本与声明

> 这一页回答三个问题。这本书现在是什么状态？怎么长出来的？边界在哪里？

## 版本

| 项 | 内容 |
| --- | --- |
| 书名 | The TAM Book of AI Era｜AI 时代的 TAM 白皮书 |
| 版本 | v0.3（全书成稿，待试读） |
| 更新 | 2026-11-17 |
| 规模 | 正文 <!-- META:chapter_count -->38<!-- /META:chapter_count --> 个文件、附录 <!-- META:appendix_count -->29<!-- /META:appendix_count --> 个、模板 <!-- META:templates_count -->23<!-- /META:templates_count --> 份 |
| 状态 | 内容完整，未经外部评审与企业试点 |
| 许可 | CC BY-NC-SA 4.0 |

版本号含义与引用格式三书统一，见公用卷[《如何引用》](../../shared/00-citation.md)。详细修订历史见 [CHANGELOG](CHANGELOG.md)。

## 卷首公用页

三书共用的卷首内容在 [`shared/`](../../shared/README.md)，本页不重复：

| 内容 | 位置 |
| --- | --- |
| 版权与许可 | [00-copyright-and-license.md](../../shared/00-copyright-and-license.md) |
| 承诺链与三书定位 | [00-commitment-chain.md](../../shared/00-commitment-chain.md) |
| 声明与脱敏 | [00-disclaimer-and-anonymization.md](../../shared/00-disclaimer-and-anonymization.md) |
| 如何引用 | [00-citation.md](../../shared/00-citation.md) |
| 完成状态口径 | [00-reading-status.md](../../shared/00-reading-status.md) |

TAM 特有的两条补充：附录 F 每年封存一版，附录 D 与附录 W 按年复核；各时效性内容的当前时点见 [README](README.md) 的「时效性声明」。

## 关于“标准”二字

附录共 <!-- META:draft_count -->17<!-- /META:draft_count --> 份文件标题带“（拟定稿）”，其中十六份标题含“标准”。它们是本书发起的公开草案，不是任何官方机构发布的标准。性质与使用边界见公用卷[《声明与脱敏》](../../shared/00-disclaimer-and-anonymization.md)。附录 G 开头的性质声明是本条的原始出处，术语层面的约定见[附录 A](appx-a-glossary.md) A.5。

## 成书方式

本书的写作过程是公开的。

判断、结构、取舍由作者决定。起草、核查、审计脚本由 AI 辅助完成。每段 AI 辅助生成的内容，都要过三道检查。证据有无来源。句子合不合本书规约。结论有没有边界。

三道检查不靠自觉，靠脚本。五项检查全部可复跑。交叉引用、术语一致性、句式规范、内容厚度、跨文件同构。脚本留在 `shared/tooling/`，读者可以自己跑一遍，看这本书够不够格。

写作与协作约定见 [AGENTS.md](../../AGENTS.md)。踩过的坑、做过的关键决策、推翻过的方案，见 [HANDOFF.md](../../shared/governance/HANDOFF.md)。这两份文件随书公开。读者可以看到这本书怎么长出来。也包括它长歪又改回来的地方。

## 关于作者

本书由 Allen Galler 发起并主笔。

本书不列作者履历。原因不是回避。一份未经核实的头衔列表，对读者的判断没有帮助。反而容易变成另一种营销。

可以核实的部分都在书里。每条建议、每个判据、每份模板，读者都可以拿去用。用了有用，比任何头衔都硬。用了不对，欢迎提 Issue 指出。这本书希望得到的检验，是使用，不是掌声。

参与共建的方式见[附录 E](appx-e-contribution-guide.md)。

## 致谢

本书的外部标尺库来自公开资料。云厂商的 WA 框架文档。监管机构发布的规章。国家标准与行业标准的公开文本。这些资料的维护者，让独立写作成为可能。

感谢 SA 书与 BTE 书的写作过程。三本书共用铁三角、承诺清单与指标口径这三套事实源。没有前两本，就没有这本的三角视角。

感谢所有提交勘误、案例与模板的贡献者。名单随版本记录累积，见 [CHANGELOG](CHANGELOG.md)。

## 版本记录

| 版本 | 日期 | 主要变化 |
| --- | --- | --- |
| v0.3 | 2026-11-17 | 顺序重编号 1–38；落地件合并（附录 43→29）；ch13/ch15 新增；ch34/ch36 扩容；AI 密度 18.3%；17 张配图；跨书章号同步 |
| v0.2 | 2026-11-10 | 补前置页（前言、版权页、索引）；元数据改为脚本生成；内容门禁上线 |
| v0.1 | 2026-10-23 | 目录定稿，全书初稿分批次落盘 |

完整记录见 [CHANGELOG](CHANGELOG.md)。本表只列里程碑版本。
