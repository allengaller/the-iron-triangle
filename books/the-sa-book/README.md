# The SA Book of AI Era｜AI 时代的售前架构师白皮书

售前解决方案架构师（SA）的岗位方法书。核心命题：**把图画对，把单做实，把承诺守住。** 与姊妹书《The TAM Book of AI Era》拼完铁三角两翼。SA 管签单前，TAM 管签单后。前者是需求—方案—竞争—承诺，后者是服务—信任—续约。两书共用一套事实源体系，三角分工与共用事实源表见公用卷[《承诺链》](../../shared/00-commitment-chain.md)。

当前状态：**全书成稿**（33 个正文文件 + 五件模板；2026-11-17 通过与 TAM 书的句级重叠审计，重复率 0.5%）。待外部试读，见 [00-overlap-audit-2026-11-17.md](../../shared/review/the-sa-book/00-overlap-audit-2026-11-17.md)。

## 内容结构

七部分 33 文件（书根 `ch*.md`，一章一文件）：

| 部分 | 内容 | 章节 |
| --- | --- | --- |
| 一定位篇 | SA 是谁 | 第 1–4 章 |
| 二 内涵篇 | SA 六维能力 | 第 5–10 章 + 5+–8+ |
| 三 流程篇 | 售前生命周期七步 | 第 11–17 章 |
| 四 金融级实战篇 | 行业特殊性与案例 | 第 18–20 章 |
| 五 AI 变革篇 | 卖 AI、用 AI、边界与不可替代 | 第 21–24 章 + 22+ |
| 六 度量与成长篇 | 度量、成熟度、职业与团队 | 第 25–27 章 + 27+ |

工具箱（书根 `tpl-*.md`）：SA-01 方案建议书、SA-02 POC 计划书、SA-03 TCO 模型、SA-04 竞争对比矩阵、SA-05 讲标检查表；另共用 TAM 书模板 19（承诺清单与移交三件套）。

书稿与模板平铺在书根（`ch*.md`、`appx-*.md`、`tpl-*.md`），另设 `DIATAXIS-MAP.md` 分型总览：本册暂不单独出构建物，不设产线；工具链与构建产物统一在仓库根 `shared/tooling/` 与 `shared/dist/`。写作与质量治理文档（AGENTS／QUALITY-GATE／HANDOFF／DESIGN／PRODUCT）三书共用：AGENTS 在仓库根，其余在 `shared/governance/`。

## 事实源与引用纪律

- 一处定义，两书引用。铁三角机制（TAM 附录 V）、指标口径（TAM 第 34 章）。需求五要素（TAM 附录 C）、脱敏规定（TAM 附录 E）；职业周期与倦怠分层处置（TAM 附录 AD）；
- 本册唯一事实源：SA 成熟度映射表（第 26 章）、承诺工程（第 9 章）；
- Diátaxis 分型维护：Explanation 12 / Reference 3 / How-to 17 / Tutorial 1。类型总览见 `DIATAXIS-MAP.md`。

## 时效性与发布闸门

本册时效性内容一律引用 TAM 书相应章节，不自行定义监管与厂商口径。发布闸门见[公用卷《声明与脱敏》](../../shared/00-disclaimer-and-anonymization.md)：发布前核对所引 TAM 章节的数据时点，未刷新须注明「数据时点未刷新，以官方最新发布为准」。案例脱敏按 TAM 附录 E 口径。

## 许可

随仓库根目录 [LICENSE](../../LICENSE)（CC BY-NC-SA 4.0）。条款与商业授权说明见公用卷[《版权与许可》](../../shared/00-copyright-and-license.md)。提交贡献即视为同意按该许可发布。
