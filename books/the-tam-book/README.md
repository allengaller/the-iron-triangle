# The TAM Book of AI Era｜AI 时代的 TAM 白皮书

AI 时代技术客户经理（Technical Account Manager，TAM）的开源方法书。以岗位最佳实践为根本，以 AI 时代的变化为主线。目标是让读者在企业级、金融级大项目中落地这套实践。

它不是厂商产品手册（方法论厂商中立）。不是 ITIL 等框架的复读机（映射见附录 C，骨架来自实战）。不是职场成功学（每条建议都落成清单、模板或可观察行为）。

## 读者对象

**适用岗位**：TAM（技术客户经理）／CRE（客户可靠性工程师）。技术客户成功、驻场架构师同样适用。同一岗位不同花名，叫法对照见[导读](00-reading-guide.md)。

- **在职 TAM**：先用第 34、36 章的度量与成熟度模型定位短板，再按维度回读；
- **想转型的工程师**：按第 1–4 章 → 第 5–16 章 → 第 37 章的顺序读；
- **服务交付管理者**：定位篇 → 外延篇 → 度量成长篇 → 附录体系；
- **伙伴与生态协作方**：第 20 章与附录 V。

完整阅读路径见[导读](00-reading-guide.md)。

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

全书按 Diátaxis 框架分型维护：<!-- META:diataxis -->Explanation 15、How-to 22、Reference 28、Tutorial 2、混合 0，合计 67 个分型文件<!-- /META:diataxis -->。类型总览见 [DIATAXIS-MAP](DIATAXIS-MAP.md)。

## 快速开始

1. 先读[前言](00-preface.md)，弄清这本书主张什么、不主张什么；
2. 读[导读](00-reading-guide.md)，选你的阅读路径；
3. 目录是唯一事实源：[00-outline.md](00-outline.md)。按编号检索用[索引](99-index.md)；
4. 三个常用事实源：术语表（附录 A）、指标口径（[第 34 章](ch34-measurement-system.md)）、流程编号 P1–P12（附录 B）；
5. 可复制的模板以 `tpl-*.md` 平铺在书根，编号索引见[索引](99-index.md)，与正文锚点一一对应。

## 本目录结构

```
the-tam-book/
├── *.md                书稿平铺：00-* 前置页、ch* 章节、appx-* 附录、99-index 索引、DIATAXIS-MAP（<!-- META:manuscript_count -->73<!-- /META:manuscript_count --> 个文件）
├── tpl-*.md            可复用模板（<!-- META:templates_count -->23<!-- /META:templates_count --> 份）
└── CHANGELOG.md        版本记录
```

书根只有 md，不放任何文件夹。非 md 资产统一在仓库根的 `shared/`：配图在 [`shared/figures/`](../../shared/figures/)，WA 归档在 [`shared/well-architected/`](../../shared/well-architected/)（<!-- META:wa_pages -->5,741<!-- /META:wa_pages --> 份，附录 Z 的证据源），工具在 [`shared/tooling/`](../../shared/tooling/README.md)，阅读站产物在 `shared/dist/site/`（出库，由 `shared/tooling/build_web.py` 生成）。

治理文档（QUALITY-GATE／HANDOFF／DESIGN／PRODUCT）与写作技能（`.qoder/skills/`）都是三书共用的：治理文档在 `shared/governance/`，技能在仓库根。评审与审计报告统一归档在 [`shared/review/the-tam-book/`](../../shared/review/the-tam-book/)。共享事实源（标准法规全文库）在 [`shared/standards/`](../../shared/standards/README.md)（<!-- META:standards_root_count -->51<!-- /META:standards_root_count --> 份全文）。

## 贡献

三类贡献：勘误、案例、模板。统一流程先 Issue 后 PR。脱敏是硬门槛。时效性数据须附来源与时点。详见[开源贡献指南](appx-e-contribution-guide.md)。

## 时效性声明

监管条文、云厂商通告等时效性内容均标注数据时点。第 31 章监管节为 2026-11-01（已联网复核）。附录 F 为 2026-11-02（全量复核）。附录 D/W 为 2026-10-25。**发布闸门**：每次正式发布前须刷新时点。未刷新须注明“数据时点未刷新，以官方最新发布为准”。

## 姊妹书

铁三角的另外两角：

- [The SA Book of AI Era](../the-sa-book/README.md)——售前解决方案架构师的方法书，管签单前（需求、方案、竞争、承诺）；
- [The BTE Book of AI Era](../the-bte-book/README.md)——技术销售的方法书，管商机与商业结构（设计承诺）。

三书共用一套事实源体系：一处定义，三书引用。三角分工与共用事实源表见公用卷[《承诺链》](../../shared/00-commitment-chain.md)，跨书引用纪律见本册附录 V。

## 许可

三书共用一套许可：**CC BY-NC-SA 4.0**（署名—非商业性使用—相同方式共享 4.0 国际许可协议）。全文见仓库根 [LICENSE](../../LICENSE)，条款与商业授权说明见公用卷[《版权与许可》](../../shared/00-copyright-and-license.md)。提交贡献即视为同意按该许可发布。
