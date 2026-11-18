# shared/ — 公用层

三书共用的东西都在这里，分两类：**书稿公用篇**（`00-*.md`，读者会读到的卷首内容）与**资产**（治理、标准、工具、配图、构建产物等子目录）。`books/` 只放三本书的书稿，各书书根只有 md。2026-11-18 起 `books/shared/` 并入本目录，公用层只此一处。

## 书稿公用篇

| 文件 | 内容 |
| --- | --- |
| `00-copyright-and-license.md` | 版权与许可：CC BY-NC-SA 4.0、三个条件、贡献即同意 |
| `00-commitment-chain.md` | 承诺链：三角分工、三书定位、共用事实源表 |
| `00-disclaimer-and-anonymization.md` | 声明与脱敏：案例虚构、非专业意见、时效标注、发布闸门、草案性质 |
| `00-citation.md` | 如何引用：引用格式、版本号含义、节号写法 |
| `00-reading-status.md` | 完成状态口径：四级状态的判定与三书当前位置 |

三书正文引用本卷写 `../../shared/00-xxx.md`。TAM 阅读站由 `tooling/build_web.py` 渲染到 `dist/site/ext/`，BTE 由 `tooling/build.sh` 拼进 HTML／EPUB／PDF。各书落点：版权与许可、声明与脱敏、如何引用挂在前置页或 README；承诺链挂在 README 与前置页；完成状态口径挂在根 README。

维护规则两条：只放三书口径完全一致的内容，某书要加自己的说法写进该书正文；改本卷一篇等于三书同时改，改完跑 TAM 六命令与 `tooling/link_check.py`（均在仓库根执行）。

## 资产

```
shared/
├── 00-copyright-and-license.md  ┐
├── 00-commitment-chain.md       │ 书稿公用篇（读者内容，见上表）
├── 00-disclaimer-and-anonymization.md
├── 00-citation.md               │
├── 00-reading-status.md         ┘
├── governance/                  治理文档（三书共用）
│   ├── QUALITY-GATE.md          内容门禁的规范与指标口径
│   ├── HANDOFF.md               全仓交接与踩坑记录
│   ├── DESIGN.md                阅读站设计契约
│   └── PRODUCT.md               阅读站产品规格
├── standards/                   共享事实源：标准与法规全文库（索引见 standards/README.md）
│   ├── data/                    GB/T、JR/T、法律与监管文件全文
│   └── scripts/                 采集与元数据生成脚本
├── tooling/                     门禁与构建：内容门禁、同构审计、元数据、交叉引用、站点构建、BTE 打包、封面、全仓链接校验（说明见 tooling/README.md）
├── figures/                     配图（SVG，书稿以相对路径引用）
├── well-architected/            六厂商 WA 公开文档归档（TAM 附录 Z 证据源）
├── dist/                        构建产物（出库，共用）：site/ 阅读站、bte-book 三件套与发布包
├── review/                      评审、审计与发布归档（repo/ + 三书子目录）
└── gtm/index.html               落地页（自包含）
```

## 不在本目录的公用件

两样东西必须在仓库根，是工具约定，不是疏漏：

- `AGENTS.md`：Agent 约定文件，入口必须在仓库根才会被自动读取。它是公用层的总纲，治理文档的具体条款都在它之外。
- `.qoder/skills/allen-writes/`：Qoder 项目级写作技能，只认仓库根路径。

根目录的 `README.md` 与 `LICENSE` 是仓库门面与授权文本，同样留在根。

## 引用约定

- 书稿引用公用资产用相对路径，从书目录出发：`../../shared/standards/README.md`。
- 评审台账由脚本写入 `shared/review/the-tam-book/`，不手工编辑。
- 归档规则见 [`review/README.md`](review/README.md)。
