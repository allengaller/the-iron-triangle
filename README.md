# the-iron-triangle｜铁角指北

> 仓库原名 `the-tam-book`，2026-11-18 更名为 `the-iron-triangle`（铁角指北）——AI 时代铁三角（TAM／SA／BTE）三书开源仓库；GitHub 会自动重定向旧地址。

AI 时代企业级项目里，签单成败由三个角色共同决定。三本书各写一角，合起来是一条承诺链：**BTE 设计承诺，SA 证明承诺，TAM 兑现承诺。**

| 角色 | 管什么 | 书 | 状态（2026-11-18） |
| --- | --- | --- | --- |
| **BTE** 技术销售 | 商机判断、决策链、价值证明、商业结构、谈判签约 | [The BTE Book](books/the-bte-book/README.md) | **初稿**（构建完成，决策门待试读） |
| **SA** 售前架构师 | 需求洞察、方案工程、竞争、POC、投标、承诺边界 | [The SA Book](books/the-sa-book/README.md) | **初稿**（33 文件 + 模板五件；门禁 block 0，厚度 warn 32/33） |
| **TAM** 技术客户经理 | 交付、服务治理、风险兜底、续约扩容 | [The TAM Book](books/the-tam-book/README.md) | **成稿** v0.3（六命令门禁全绿，待试读） |

**完成状态口径**（三书统一）：**草稿**（结构未齐）→ **初稿**（文件齐备，形式门禁通过）→ **成稿**（内容完成，内部质化审计通过，待外部试读）→ **定稿**（试读通过、发布检查表全过、时点刷新，v1.0 可引用）。判定条件与三书当前位置见公用篇[《完成状态口径》](shared/00-reading-status.md)。

## 仓库结构

```
the-iron-triangle/
├── books/                          三本书；书根只有 md，不放任何文件夹
│   ├── the-tam-book/
│   │   ├── *.md                    书稿平铺：00-* 前置页、ch* 章节、appx-* 附录、tpl-* 模板、99-index 索引
│   │   └── CHANGELOG.md            版本记录
│   ├── the-sa-book/
│   │   └── *.md                    书稿平铺（暂不单独出构建物）
│   └── the-bte-book/
│       └── *.md                    书稿平铺（前置页、章节、附录、模板）
├── shared/                         公用层：书稿公用篇 + 资产，书稿之外的一切
│   ├── 00-*.md                     书稿公用篇：版权、承诺链、声明与脱敏、引用格式、状态口径（说明见其 README）
│   ├── governance/                 治理文档：QUALITY-GATE / HANDOFF / DESIGN / PRODUCT
│   ├── standards/                  共享事实源：标准与法规全文库（索引见其 README）
│   ├── tooling/                    门禁、同构审计、元数据、交叉引用、站点构建、BTE 打包、封面、全仓链接校验（脚本与构建资源同处）
│   ├── figures/                    配图（SVG，书稿以相对路径引用）
│   ├── well-architected/           六厂商 WA 文档归档（TAM 附录 Z 证据源）
│   ├── dist/                       构建产物（出库，三书共用）：site/ 阅读站、bte-book 三件套与发布包
│   ├── review/                     评审、审计与发布归档（repo/ + 三书子目录）
│   └── gtm/index.html              落地页（自包含）
├── AGENTS.md                       仓库级约定：写作规则、术语、门禁口径（必须在根）
├── .qoder/skills/allen-writes/     写作技能：Diátaxis 定型、去 AI 味、质量验收
├── LICENSE                         CC BY-NC-SA 4.0
└── .tmp/                           本地草稿区（出库），按月份归档
```

公用层只有 `shared/` 一处：`00-*.md` 是**书稿公用篇**（卷首声明类内容，三书正文引用），子目录是**资产**（治理文档、标准库、工具、配图、构建产物、评审、落地页）。卷说明与目录见 [shared/README.md](shared/README.md)。

`AGENTS.md` 与 `.qoder/` 留在仓库根是工具约定：前者必须根级才能被 Agent 自动读取，后者只认根级路径。

## 从哪读起

| 你想做的事 | 入口 |
| --- | --- |
| 了解 TAM 岗位怎么做 | [TAM 书导读](books/the-tam-book/00-reading-guide.md) |
| 了解售前 SA 怎么打单 | [SA 书目录](books/the-sa-book/00-outline.md) |
| 了解技术销售怎么设计承诺 | [BTE 书导读](books/the-bte-book/front-reading-guide.md) |
| 看三角怎么咬合 | [TAM 附录 V](books/the-tam-book/appx-v-tam-bte-sa-triangle.md) · [SA 第 2 章](books/the-sa-book/ch02-triangle-boundary.md) · [BTE 第 2 章](books/the-bte-book/ch02-triangle-boundary.md) |
| 看三书怎么分工 | [公用篇《承诺链》](shared/00-commitment-chain.md) |
| 直接拿模板用 | [TAM](books/the-tam-book/tpl-01-service-plan.md) · [SA](books/the-sa-book/tpl-01-proposal-skeleton.md) · [BTE](books/the-bte-book/tpl-01-opportunity-scorecard.md) |
| 查监管原文 | [shared/standards/](shared/standards/README.md) |

## 三书共用的纪律

前三条已收进书稿公用卷，本页只挂指针：

1. **一处定义，三书引用。** 共用事实源表见[《承诺链》](shared/00-commitment-chain.md)。
2. **脱敏是硬门槛。** 案例一律虚构化，锚事件结构不锚客户身份。口径见[《声明与脱敏》](shared/00-disclaimer-and-anonymization.md)。
3. **时效性内容标注来源与时点。** 发布闸门同见该页。

仓库侧另两条：

4. **能算的数字不手写。** 文件数、类型分布、模板数由 `shared/tooling/gen_metadata.py` 从磁盘计算，锁在 `<!-- META:key -->` 标记区里，`--check` 不一致即拦。
5. **写作先加载技能。** 动笔前加载仓库根 `.qoder/skills/allen-writes/SKILL.md`：先定 Diátaxis 类型，再按体裁写，去 AI 味，最后过验收清单。

## 质量门禁

门禁规范见 [shared/governance/QUALITY-GATE.md](shared/governance/QUALITY-GATE.md)（指标口径、盲区、Goodhart 禁令，三书通用）；门禁脚本在 `shared/tooling/`，六条命令在仓库根执行：

```bash
python3 shared/tooling/content_gate.py --strict     # 体裁与结构破损
python3 shared/tooling/content_gate.py --report     # 内容厚度台账 → shared/review/the-tam-book/
python3 shared/tooling/claim_audit.py               # 数值断言出处
python3 shared/tooling/similarity_audit.py --report # 跨文件同构 → shared/review/the-tam-book/
python3 shared/tooling/gen_metadata.py --check      # 元数据漂移
python3 shared/tooling/xref_check.py && python3 shared/tooling/xref_check2.py  # 交叉引用
```

跨书与仓库级路径另有一道全仓校验，在仓库根执行：

```bash
python3 shared/tooling/link_check.py
# 已知非断链：shared/tooling/{cover,template}.html 构建模板、shared/review/ 带日期快照中的旧章节 slug
```

## 贡献

三类贡献：勘误、案例、模板。统一流程先 Issue 后 PR。详见 [TAM 附录 E 贡献指南](books/the-tam-book/appx-e-contribution-guide.md)。

## 许可

内容采用 **CC BY-NC-SA 4.0**（署名-非商业性使用-相同方式共享 4.0 国际许可协议）。全文见 [LICENSE](LICENSE)。提交贡献即视为同意按该许可发布。
