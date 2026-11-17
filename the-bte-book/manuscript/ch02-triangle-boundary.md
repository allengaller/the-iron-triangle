<!-- Diátaxis: Reference -->
# 第 2 章　铁三角边界与决策权

> 本章是铁三角的 BTE 视角索引。本章不重写三角机制。完整定义见[《The TAM Book》附录 V](../../the-tam-book/manuscript/appx-v-tam-bte-sa-triangle.md)；SA 侧动作见[《The SA Book》第 2 章](../../the-sa-book/manuscript/ch02-triangle-boundary.md)。本章回答三件事：BTE 管什么，决策权怎么分，接缝处 BTE 做什么。

## 2.1 三角色一句话

| 角色 | 一句话 | 对什么负责 | 不对什么负责 |
| --- | --- | --- | --- |
| BTE（技术销售，Business Technology Executive） | 把门打开 | 商机选择、客户关系商务面、价值证明、商业结构、赢单质量、承诺的商务合理性 | 方案技术正确性、交付兑现 |
| SA（解决方案架构师，Solution Architect） | 把图画对 | 架构正确性、技术选型、概念验证（Proof of Concept，POC）技术结论、方案可交付 | 商务条款、运行期值守 |
| TAM（技术客户经理，Technical Account Manager） | 让画变成日常 | 交付后的技术成功、承诺的运营期兑现、风险兜底 | 报价折扣、合同条款 |

原句记住分工：**BTE 把门打开，SA 把图画对，TAM 让画变成日常。**

按承诺链再说一遍：**BTE 设计承诺，SA 证明承诺，TAM 兑现承诺。**

两句话不冲突。第一句讲动作，第二句讲责任。

## 2.2 角色属性表

| 属性 | BTE | SA | TAM |
| --- | --- | --- | --- |
| 活跃阶段 | 全周期，核心在商机期与续约期 | 签单前为主 | 签单后为主 |
| 主产出 | 商机、价值案例、商业结构 | 方案、承诺 | 服务、信任 |
| 判断场景 | 值不值得跟、怎么赢得好 | 这么买对不对、能不能交付 | 这么跑稳不稳 |
| 首要接口 | 客户决策人与采购 | 客户技术与业务 | 客户运维与管理 |
| 交接对象 | SA（方案期）、TAM（交付期） | 交付与 TAM | 续约回 BTE |
| 主要考核 | 赢单质量（Win Quality）、承诺偏差、毛利 | 方案一次通过率、POC 转化率 | 健康分、服务水平协议（SLA）、续约技术信号 |

## 2.3 决策权矩阵

RACI（执行、负责、咨询、知会）说谁参与，决策权说谁拍板。两件事不能混。

同一活动可以三人参与，但只有一个决策人。下表列 BTE 必须拍板的十项决策。

| 关键决策 | BTE | SA | TAM | 判断依据 |
| --- | --- | --- | --- | --- |
| 跟不跟这个商机 | A/R | C | C | [BTE-01 机会评分卡](../templates/bte-01-opportunity-scorecard.md) |
| 客户决策链与切入点 | A/R | C | C | 决策链地图 |
| 价值假设与业务案例 | A/R | C | C | 价值证据链 |
| 方案架构与技术路线 | C | A/R | C | 架构评审记录 |
| POC 业务成功标准 | A | R | C | 证明计划 |
| POC 技术结论 | C | A/R | C | 测试记录 |
| 报价与合同结构 | A/R | C | C | 商业结构方案 |
| 承诺的商务合理性 | A/R | C | C | 承诺清单（Commitment List） |
| 交付移交 | R | C | A | 三件套 |
| 续约与增购 | A/R | C | R | 信号单 |

R 执行，A 负责，C 咨询，I 知会。

三条规则：

1. **一个决策只有一个 A**。两个 A 等于没人负责。
2. **不越位**。BTE 不替 SA 定架构，SA 不替 BTE 定价，TAM 不替 BTE 谈合同。
3. **灰度先接住再划界**。客户面前不暴露内部分工。回到内部再按本表归属。

## 2.4 RACI 示例（BTE 侧）

| 场景 | R | A | C | I |
| --- | --- | --- | --- | --- |
| 商机立项 | BTE | BTE | SA、TAM | 交付 |
| 客户高层拜访 | BTE | BTE | SA、TAM | 市场 |
| 价值案例编制 | BTE | BTE | SA、财务 | 交付 |
| 方案评审 | SA | SA | BTE、TAM | 交付 |
| POC 执行 | SA | SA | BTE、TAM | 交付 |
| 报价与谈判 | BTE | BTE | SA、法务 | TAM |
| 签单交接 | BTE | TAM | SA、交付 | 财务 |
| 续约与增购 | BTE | BTE | TAM、SA | 交付 |

这张表只列常见场景。完整全周期 RACI 见[附录 V](../../the-tam-book/manuscript/appx-v-tam-bte-sa-triangle.md)。

## 2.5 四个接缝与 BTE 侧动作

接缝机制的定义在[附录 V](../../the-tam-book/manuscript/appx-v-tam-bte-sa-triangle.md)。下表只列 BTE 侧动作。

| 接缝 | BTE 动作 | 不合格表现 | 锚点 |
| --- | --- | --- | --- |
| 承诺管理 | 48 小时内登记；口头承诺也登记；组织 TAM 一票关注；签约时随合同留痕 | 先承诺后补；口头承诺不入账 | 附录 V.5.1、[模板 19](../../the-tam-book/templates/19-commitment-handover-kit.md) |
| 方案评审 | 提供客户约束与商业约束；不绕过可运营性评审；带条件通过进风险清单 | 为赢单压配置；绕过评审 | 附录 V.5.2、[SA 第 7 章](../../the-sa-book/manuscript/ch07-solution-engineering.md) |
| 移交仪式 | 发起移交会；移交三件套齐备；30 天伴随期；商务关系不断 | 一封邮件三个附件；移交即失联 | 附录 V.5.3、[模板 19](../../the-tam-book/templates/19-commitment-handover-kit.md) |
| 信号回流 | 接收 TAM 信号；5 个工作日内书面化；决定商务动作；跟踪闭环；不压信号 | 口头听说；压信号；只收不复 | 附录 V.5.4、[TAM 第 21 章](../../the-tam-book/manuscript/ch21-commercial-synergy.md) |

### 2.5.1 承诺管理

BTE 是承诺的第一道闸门。客户听到的每句“可以”，都要有依据、代价、载体与接单人。

四问见[SA 第 9 章](../../the-sa-book/manuscript/ch09-commitment-engineering.md)。SA 管技术可达性，BTE 管商务合理性，TAM 管可运营性。

移交三件套指方案基线、承诺清单与风险清单。三件齐备，TAM 才签收。

### 2.5.2 方案评审

BTE 在评审中的角色不是技术裁判，是商业约束的提供者。

BTE 要带来三个输入。客户预算与采购节奏，决策链的否决点，承诺的商务边界。没有这三个输入，方案可能技术上正确，商业上不可行。可运营性（Operability）评审由 TAM 行使一票关注，BTE 不得绕过。

### 2.5.3 移交仪式

移交不是切割，是接力棒的并排跑段。

BTE 发起移交，TAM 签收，SA 澄清基线。三件套不齐不移交。移交后 30 天，BTE 保持每周一次三方同步。

### 2.5.4 信号回流

TAM 是三角的传感器。BTE 是信号的商务处置人。

信号给事实与证据，不给“我感觉”。BTE 收到信号后，5 个工作日内书面化处置意见。续约风险、增购机会、方案反哺三类分道，见[附录 V.5.4](../../the-tam-book/manuscript/appx-v-tam-bte-sa-triangle.md)。

## 2.6 BTE 与相邻岗位

| 岗位 | 主责 | 与 BTE 的接缝 | 判断句 |
| --- | --- | --- | --- |
| AE（客户经理，Account Executive） | 合同、回款、客户关系 | 合并或配对 | 分设时，BTE 管技术可信，AE 管合同 |
| SA | 方案与技术正确性 | 方案期 | BTE 定商业方向，SA 定技术路线 |
| TAM | 交付与运营 | 交付期 | BTE 设计承诺，TAM 兑现承诺 |
| 售前支持/产品专家 | Demo、标书、产品答疑 | 按需调用 | 专家给证据，BTE 做决策 |
| CSM（客户成功经理，Customer Success Manager） | 采用、续费运营 | 续约期 | BTE 管商机，CSM 管采用 |

一个判断句：**这个动作是否改变一个商业决策？** 不改变，归 SA、售前支持或 CSM。

## 2.7 引用与冲突裁定

- 机制口径冲突时，以[《The TAM Book》附录 V](../../the-tam-book/manuscript/appx-v-tam-bte-sa-triangle.md)为准；
- 指标口径冲突时，以[《The TAM Book》第 34 章](../../the-tam-book/manuscript/ch34-measurement-system.md)为准；
- 售前流程细节冲突时，以[《The SA Book》第 11–17 章](../../the-sa-book/manuscript/ch11-lead-qualification.md)为准；
- 本书只写 BTE 的决策、证据与交接；
- 本书各章的接缝动作均锚定本章编号。

---

**本章要点回顾**

1. 三角色一句话：BTE 把门打开，SA 把图画对，TAM 让画变成日常。
2. 按承诺链说：BTE 设计承诺，SA 证明承诺，TAM 兑现承诺。
3. 决策权矩阵比 RACI 更关键：同一活动三人可参与，但只有一个拍板人。
4. 四个接缝各有 BTE 侧动作：承诺台账、评审输入、移交发起、信号处置。
5. 判断归属只问一句：这个动作是否改变一个商业决策。