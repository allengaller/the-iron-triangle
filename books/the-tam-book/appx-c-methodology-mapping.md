<!-- Diátaxis: Reference -->
# 附录 C　方法论与标准映射

> 性质说明：本附录是**阅读与迁移工具**，不是标准拟定稿。它回答一个问题：“我已经懂 ITIL 4 / IT4IT / SRE / FinOps / 等保 2.0 / Well-Architected 里的某些概念。它们对应本书的哪一章、哪份附录？”框架全称：ITIL 4（信息技术基础架构库，Information Technology Infrastructure Library）。SRE（站点可靠性工程，Site Reliability Engineering）与 FinOps（云成本优化）。映射按框架分节。左列是框架原概念，右列是本书落点。本书不重复定义框架概念细节。原始文献见[附录 D](appx-d-further-reading.md)。本书只给对应关系与岗位化增量。

---

## C.0 引言：本书与通用框架的关系

通用框架管“组织该怎么运转”。本书管“TAM 在运转里干什么、怎么干好”。两者是骨架与血肉的关系：

- 框架给流程与概念，本书给**岗位动作、时限锚点与红线**。ITIL 说要有事件管理。本书说 TAM 在故障 P1 的黄金 30 分钟里做哪几件事（[附录 K](appx-k-incident-emergency-drill-standard.md)）；
- 框架是厂商中立的，本书的判断校准到**金融级场景**。SRE 的错误预算（error budget）在金融客户那里要叠加监管口径才可用；
- 框架之间互有重叠，本书的章节是**唯一事实源**。映射表里多个框架概念指向同一章。这说明本书做了合并与取舍。以本书为准。

### 多框架同落点速查

多个框架概念汇聚到同一落点时，按本书口径使用：

| 本书落点 | 汇聚的框架概念 |
| --- | --- |
| 事件与复盘（第 25 章、附录 R） | ITIL Incident/Problem、IT4IT Detect to Correct、SRE Postmortem |
| 变更治理（第 11、16 章、附录 T） | ITIL Change Enablement、IT4IT Requirement to Deploy |
| 度量口径（第 34 章） | ITIL Service Level Management、SRE SLI/SLO、FinOps 用量可见性 |
| 容量与成本（第 5、21、27 章） | SRE 容量规划、FinOps 成本优化 |
| 架构评审（第 5 章、模板 03） | Well-Architected 支柱与问询、SRE 容量规划 |
| 平台与取数（附录 H） | IT4IT 工具链、等保安全管理中心 |
| 连续性（第 23、24 章） | ITIL Service Continuity、等保安全区域边界 |

## C.1 ITIL 4

| ITIL 4 概念 | 本书落点 | 本书的增量 |
| --- | --- | --- |
| Incident Management | 第 18、25 章，附录 K、U | P1–P4 分级、分钟级响应时钟、监管上报口径 |
| Problem Management | 附录 R、模板 07/16 | 三级复盘与六条强制触发；复发即升级 |
| Change Enablement | 第 11、16 章，附录 T | CH1–CH4 分级、冻结窗口纪律、双人复核 |
| Service Level Management | 第 11 章 11.3，第 34 章，模板 01 | SLA/OLA/XLA 三层契约、口径前置三问 |
| Service Continuity | 第 23、24 章 | 重保五阶段、容灾演练组织 |
| Continual Improvement | 第 34 章，附录 G/R | 改进项“验证有效才算闭环”、指标防异化 |
| Service Catalog / CMDB | 第 11 章 11.5，附录 H | 四张台账、系统取数纪律 |
| Monitoring & Event Management | 第 30 章，附录 I | 告警降噪红线、低频高危永不静默 |
| Service Request Management | 附录 U | 工单四分类与首响时限 |
| Knowledge Management | 第 28 章、附录 Y | 知识库保鲜纪律、故障模式库训练 |
| 指导原则（聚焦价值等） | 第 3、21 章 | 价值实现报告（VBR）作为价值证据链 |

## C.2 IT4IT

| IT4IT 价值流 | 本书落点 | 说明 |
| --- | --- | --- |
| Strategy to Portfolio | 第 11 章服务计划、附录 B 流程 P1 | 单客户粒度而非组织粒度 |
| Requirement to Deploy | 第 16、19 章，模板 04 | 需求五要素、上线闸门 |
| Request to Fulfill | 附录 U 工单管理 | TK-F/Q/R/C 四分类 |
| Detect to Correct | 第 25、30 章，附录 K/R | 事件→复盘→风险册闭环链 |

IT4IT 的工具链视角对应本书[附录 H](appx-h-tool-platform-acceptance-standard.md) 的平台验收要求。数据在工具间流动。“取数只认系统”纪律见[第 34 章](ch34-measurement-system.md)。

## C.3 SRE

| SRE 概念 | 本书落点 | 本书的增量 |
| --- | --- | --- |
| SLI/SLO/Error Budget | 第 34 章，第 11 章 11.3 | 金融场景叠加监管口径；SLO 违约的客户沟通动作（模板 06） |
| Toil（琐事）削减 | 第 28、33 章 | AI 杠杆替代信息搬运与例行巡检 |
| Blameless Postmortem | 附录 R，模板 07 | 对事不对人三纪律；金融级“问责到流程不只到人”（第 25 章） |
| 监控与告警（四大黄金信号） | 第 30 章 | 告警降噪红线、AIOps 接入三前提 |
| 容量规划 | 第 5 章 | 水位管理与业务日历基线 |
| On-Call 与应急演练（Wheel of Misfortune） | 附录 K、I | 三级演练与合格判定、不透题红线；值班纪律 |

立场差异：SRE 的语境是“我运营我自己的系统”。TAM 的语境是“我帮客户运营他买的服务”。所有权、权限、责任边界完全不同。映射前先过[第 2 章](ch02-role-boundary-map.md)的岗位边界。

## C.4 FinOps

| FinOps 概念 | 本书落点 | 说明 |
| --- | --- | --- |
| Inform / Optimize / Operate 三阶段 | 第 21、34 章 | 用量三判读（趋势/结构/水位）先行 |
| 用量可见性与分摊 | 第 21 章用量健康度、第 34 章 | 数据源同附录 H 取数纪律 |
| 成本优化 | 第 21 章 | “先优化成本再谈扩容”纪律 |
| 云账单异常 | 第 14 章风险扫描、附录 P D3 | 账单突变作为主动服务信号 |
| AI/推理成本治理 | 第 27 章 | GPU 容量与排队、推理成本专项 |

## C.5 等保 2.0（GB/T 22239）

| 等保 2.0 要求域 | 本书落点 | 说明 |
| --- | --- | --- |
| 安全计算环境（身份鉴别、审计） | 附录 Q 合规与审计支持维度、第 14 章数据安全 | 专有云六维中的 D6 |
| 安全区域边界与通信网络 | 第 23 章架构护航 | 容灾与单元化设计评审 |
| 安全管理中心 | 第 30 章 AIOps、附录 H | 监控平台验收项 |
| 管理体系（制度/人员/建设/运维） | 附录 B 九项运营规范、附录 I/S | 值班、疲劳管理与自检纪律 |
| 数据分级分类（配套 GB/T 43697 等） | 第 14、22 章 | 数据安全三铁律、金融行业特殊性 |

监管侧的事件上报时限与口径不来自等保本身。它们来自各行业监管规定。本书在[第 22 章](ch22-financial-industry.md)、[第 25 章](ch25-financial-incident.md)按金融行业给出。其他行业读者须替换成本行业监管口径。[附录 F](appx-f-cloud-vendor-notices-2026.md) 收录年度云厂商通告，不含监管条文。

## C.6 Well-Architected（WA）

六厂商支柱对照、问询库与 Lens 全量索引见[附录 Z](appx-z-well-architected-framework.md)。本节只给框架概念到本书的落点：

| Well-Architected 概念 | 本书落点 | 说明 |
| --- | --- | --- |
| 支柱与设计原则（六厂商对照） | 第 5 章，附录 Z Z.2 | 岗位化增量：支柱落到评审动作与证据 |
| 架构评审问询（Review Questions） | 第 6 章 6.1，模板 03 | 8 域 40 问的评审动作库；AI 工作负载专项 |
| Lens／Perspective（行业与场景视角） | 第 27、31 章，附录 Z Z.3.2 | AI 族 Lens 驱动 AI 专项评审 |
| 能力域对齐（Capability Mapping） | 附录 Z Z.4 | 六厂商能力域对齐矩阵 |
| 卓越运营支柱（Operational Excellence） | 第 30 章，附录 I/K | 服务模式跃迁与值班、应急纪律 |

## C.7 版本与共建

| 版本 | 日期 | 状态 | 说明 |
| --- | --- | --- | --- |
| v0.1 | 2026-10 | 初版 | 覆盖目录承诺的五个框架，随本书章节滚动回核 |
| v0.2 | 2026-11 | 修订 | 补多框架汇聚速查与三张映射表增量行 |
| v0.3 | 2026-11 | 修订 | 增补 C.6 Well-Architected 映射（第六种方法论），版本节顺延为 C.7 |

映射表随章节完成度滚动修订，修订流程见[附录 E](appx-e-contribution-guide.md)。重点征集方向有两类。其他框架的映射（COBIT、TOGAF、ISO 20000/22301）。非金融行业监管口径的映射分支。Well-Architected 六厂商对照见[附录 Z](appx-z-well-architected-framework.md)，本附录 C.6 已给映射行。

---

**本章要点回顾**

- 本附录是迁移工具。从读者已懂的框架概念，索引到本书章节与附录；
- 框架给组织骨架，本书给岗位血肉。动作、时限、红线以本书为唯一事实源；
- 多框架同落点时按汇聚速查表使用，合并与取舍以本书为准；
- SRE 概念映射前先过岗位边界（[第 2 章](ch02-role-boundary-map.md)）。“运营自己的系统”与“帮客户运营”是两个语境；
- 金融级读者注意。SLO、复盘、上报等概念须叠加监管口径后使用。口径见[第 22 章](ch22-financial-industry.md)、[第 25 章](ch25-financial-incident.md)。
