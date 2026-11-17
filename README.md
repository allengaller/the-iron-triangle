# the-tam-book

**The TAM Book of AI Era｜AI 时代的 TAM 白皮书**

AI 时代技术客户经理（Technical Account Manager，TAM）的开源方法书。以岗位最佳实践为根本。以 AI 时代的变化为主线。目标是让读者在企业级、金融级大项目中落地这套实践。

它不是厂商产品手册（方法论厂商中立）。不是 ITIL 等框架的复读机（映射见附录 C，骨架来自实战）。不是职场成功学（每条建议都落成清单、模板或可观察行为）。

## 读者对象

**适用岗位**：TAM（技术客户经理）／CRE（客户可靠性工程师）。技术客户成功、驻场架构师同样适用。同一岗位不同花名，叫法对照见[导读](the-tam-book/manuscript/00-reading-guide.md)。

- **在职 TAM**：先用第 34、36 章的度量与成熟度模型定位短板，再按维度回读；
- **想转型的工程师**：按第 1–4 章 → 第 5–16 章 → 第 37 章的顺序读；
- **服务交付管理者**：定位篇 → 外延篇 → 度量成长篇 → 附录体系；
- **伙伴与生态协作方**：第 20 章与附录 V。

完整阅读路径见[导读](the-tam-book/manuscript/00-reading-guide.md)。

## 内容结构

| 部分 | 内容 | 章节 |
| --- | --- | --- |
| 一 定位篇 | TAM 是谁 | 第 1–4 章 |
| 二 内涵篇 | 六维能力模型（每维两章：主章 + 实战章） | 第 5–16 章 |
| 三 外延篇 | 工作全景与生态协同 | 第 17–21 章 |
| 四 金融级实战篇 | 行业特殊性与高压场景 | 第 22–26 章 |
| 五 AI 变革篇 | 护航 AI、武装自己、风险治理 | 第 27–33 章 |
| 六 度量与成长篇 | 度量、成熟度、职业发展 | 第 34–38 章 |
| 七 开源工具箱 | 模板与清单库 | 模板 01–<!-- META:templates_count -->23<!-- /META:templates_count --> |

附录 <!-- META:appendix -->29 个（A–W、Y、Z、AA–AD）<!-- /META:appendix -->。内容覆盖术语表、流程与规范、方法论映射、延伸阅读、贡献指南。云厂商通告、评估与验收标准、值班培训演练也在其中。项目与产品导入、服务质量、复盘、变更、工单一并收录。铁三角、金融标准汇编、训练教程也在。WA 框架对照、报告标准、子 TAM 协同、SRE/CRE 工程纵深等同样收录。

全书按 Diátaxis 框架分型维护：<!-- META:diataxis -->Explanation 15、How-to 22、Reference 28、Tutorial 2、混合 0，合计 67 个分型文件<!-- /META:diataxis -->。类型总览见[DIATAXIS-MAP](the-tam-book/manuscript/DIATAXIS-MAP.md)。

## 快速开始

1. 先读[前言](the-tam-book/manuscript/00-preface.md)，弄清这本书主张什么、不主张什么；
2. 读[导读](the-tam-book/manuscript/00-reading-guide.md)，选你的阅读路径；
3. 目录是唯一事实源：[00-outline.md](the-tam-book/manuscript/00-outline.md)。按编号检索用[索引](the-tam-book/manuscript/99-index.md)；
4. 三个常用事实源：术语表（附录 A）、指标口径（[第 34 章](the-tam-book/manuscript/ch34-measurement-system.md)）、流程编号 P1–P12（附录 B）；
5. 可复制的模板在 [templates/](the-tam-book/templates/)，与正文锚点一一对应。

## 仓库结构

```
gtm/                        Go-to-Market 落地页（自包含 HTML）
standards/                  标准与法规主库（<!-- META:standards_root_count -->50<!-- /META:standards_root_count --> 份 + 索引 + 采集脚本）
standards-verification-report-2026-10-25.md   标准库校验报告
the-sa-book/                SA 书（姊妹项目，全书成稿）
the-bte-book/               BTE 书（姊妹项目，初稿完成）
the-tam-book/
├── manuscript/             章节、附录与前置页（<!-- META:manuscript_count -->73<!-- /META:manuscript_count --> 个文件）
├── templates/              <!-- META:templates_count -->23<!-- /META:templates_count --> 份可复用模板
├── standards/              标准与法规全文镜像库（<!-- META:standards_mirror_count -->48<!-- /META:standards_mirror_count --> 份 + 索引）
├── well-architected/       六厂商 WA 公开文档归档（<!-- META:wa_pages -->5,741<!-- /META:wa_pages --> 份）
├── scripts/                内容门禁、同构审计、元数据生成等工具
├── AGENTS.md               写作与协作约定
├── QUALITY-GATE.md         内容门禁的规范与指标口径
├── CHANGELOG.md            版本记录
└── HANDOFF.md              协作交接与并发登记
```

## 贡献

三类贡献：勘误、案例、模板。统一流程先 Issue 后 PR。脱敏是硬门槛。时效性数据须附来源与时点。详见[开源贡献指南](the-tam-book/manuscript/appx-e-contribution-guide.md)。

## 时效性声明

监管条文、云厂商通告等时效性内容均标注数据时点。第 31 章监管节为 2026-11-01（已联网复核）。附录 F 为 2026-11-02（全量复核）。附录 D/W 为 2026-10-25。**发布闸门**：每次正式发布前须刷新时点。未刷新须注明“数据时点未刷新，以官方最新发布为准”。

## 姊妹项目

《The SA Book of AI Era｜AI 时代的售前架构师白皮书》全书成稿——售前解决方案架构师的岗位方法书。与本书拼完铁三角两翼（SA 管签单前，TAM 管签单后），共用一套事实源体系。七部分 33 文件 + 模板五件齐备，见 [the-sa-book/](the-sa-book/)。

《The BTE Book of AI Era｜AI 时代的技术销售白皮书》全书初稿完成——技术销售的岗位方法书，补完铁三角第三角（BTE 管商机与商业结构）。七部分 36 个正文文件 + 7 个附录 + 模板十件齐备，另附阅读指南、重叠审计与发布清单；决策门待试读。见 [the-bte-book/](the-bte-book/)。

## 许可

内容采用 **CC BY-NC-SA 4.0**（署名-非商业性使用-相同方式共享 4.0 国际许可协议）。全文见根目录 [LICENSE](LICENSE)。提交贡献即视为同意按该许可发布。
