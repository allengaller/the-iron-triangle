<!-- Diátaxis: Reference -->
# 第 26 章　度量体系

> 前面二十五章反复引用“口径见第 26 章”。服务等级协议（Service Level Agreement，SLA）的达成口径指向这里。平均修复时间（Mean Time To Repair，MTTR）的口径也是。净推荐值（Net Promoter Score，NPS）、客户健康分、SLA 赔偿（SLA Credit）同样在本章定义。本章是全书度量口径的唯一事实源。[附录 G](appx-g-tam-work-evaluation-standard.md) 的考核口径指向本章。[附录 P](appx-p-tam-service-quality-standard-public-cloud.md)/[附录 Q](appx-q-tam-service-quality-standard-dedicated-cloud.md) 的服务质量打分同样如此。[附录 I](appx-i-on-duty-standard.md)/[附录 K](appx-k-incident-emergency-drill-standard.md) 的响应与应急时限也一样。任何地方只引用、不重新定义。度量实施动作见[第 26+ 章](ch26-measurement-system-howto.md)。度量篇先讲度量，再讲[第 27 章](ch27-maturity-model.md)成熟度与[第 28 章](ch28-career-team-building.md)职业发展。没有口径一致的度量，后两章全是空中楼阁。

## 26.1 度量的目的与元规则

度量只有三个合法目的。**做决策**：资源往哪投、风险在哪。**建信任**：给客户和组织一个可核对的事实底座。**促改进**：找到下一个要修的东西。不能落到这三个目的上的指标，是工作量证明工具。它存在的理由通常是“总要考核点什么”。

三条元规则先于一切指标设计：

1. **口径先于数值**：指标落地前写清三件事。怎么算、从哪取数、谁仲裁争议，三件都要写明。分子分母要写明。取数以系统记录为准。争议仲裁机制是[第 8 章](ch08-service-governance.md) SLA 口径管理的泛化；
2. **取数只认系统**：手工填报的指标必然失真。这是统计学问题，不是道德问题。平台证据能力要求见[附录 H](appx-h-tool-platform-acceptance-standard.md)；
3. **每个指标配一个反异化条款**：指标一经考核就会异化（Goodhart 定律）。定义指标时就写明刷分手法与防线。通用机制见 26.8。

## 26.2 指标体系总览

按度量对象分四族，各自回答一个问题：

| 族 | 回答的问题 | 核心指标 | 主要消费方 |
| --- | --- | --- | --- |
| 客户健康族 | 这个客户整体好不好 | 客户健康分（Customer Health Score）（26.3）、用量健康度（[第 15 章](ch15-commercial-synergy.md)） | TAM 自管、服务经理 |
| 服务质量族 | 服务交付达不达标 | [附录 P](appx-p-tam-service-quality-standard-public-cloud.md)/[附录 Q](appx-q-tam-service-quality-standard-dedicated-cloud.md) 五/六维度各项指标（本章供口径） | 服务经理、客户（QBR 公开） |
| 事件效率族 | 出事应对快不快、稳不稳 | MTTR、平均故障间隔（Mean Time Between Failures，MTBF）、响应达标率、复发率（26.5） | 全体，监管场景客户 |
| 感知与价值族 | 客户感觉好不好、值不值 | 客户满意度（Customer Satisfaction Score，CSAT）/费力度（Customer Effort Score，CES）（26.6）、价值实现度量（26.7） | 管理层、续约场景 |

四族的关系有先后。健康族是**领先指标**（预测未来）。质量族与效率族是**同步指标**（正在发生）。感知与价值族是**滞后指标**（结果确认）。只看滞后指标的管理是后视镜开车。

## 26.3 客户健康分口径

客户健康分（[模板 10](../templates/10-customer-health-scorecard.md)）是 TAM 最重要的自管指标。它也是[第 11 章](ch11-customer-lifecycle.md)生命周期运营和[第 15 章](ch15-commercial-synergy.md)续约预测的输入。

**构成（建议权重，按业务校准）**：

| 维度 | 权重 | 数据来源 |
| --- | --- | --- |
| 技术健康 | 30% | 监控告警趋势、未闭环风险数、版本合规状态 |
| 服务消费 | 25% | 用量趋势、功能采纳度、工单量趋势（异常低也是信号） |
| 服务交互 | 20% | 例会出席率、行动项闭环率、升级频次 |
| 关系信号 | 15% | 关键人覆盖度（[模板 11](../templates/11-key-person-map-canvas.md)）、高层互动频次、NPS 最近值 |
| 商业价值 | 10% | 续约窗口距离、扩容信号（只作参考，不考核金额，见[附录 G](appx-g-tam-work-evaluation-standard.md)） |

**口径约束**：

- 分数必须**可解释**：每个维度能下钻到原始证据。“系统算的 72 分”不可接受；
- 阈值分绿/黄/红三档。每档触发预定义动作。动作清单见[第 26+ 章](ch26-measurement-system-howto.md)；
- 防异化：健康分不得作为唯一续约预测依据。它测技术关系温度，测不到采购流程与预算周期（[第 15 章](ch15-commercial-synergy.md)）。

## 26.4 SLA 达成与 SLA Credit 口径

**口径定义**（[附录 P](appx-p-tam-service-quality-standard-public-cloud.md) 的 P5.5-1 与[附录 Q](appx-q-tam-service-quality-standard-dedicated-cloud.md) 的 Q5.2-1 引用本节）：

- **统计周期**：自然月。按服务、按客户分别计算，不做全平台混算。混算会淹没单客户违约；
- **可用性口径**：可用性 =（周期总分钟 − 不可用分钟）/ 周期总分钟。不可用分钟从故障确认起算，到服务恢复验证止。起算点不取客户报障时刻。**计划内维护是否剔除必须写进合同**。不写明就是争议地雷；
- **响应类 SLA**：以系统时间戳为准。计时从工单创建到首次有效响应。有效响应须包含实质性处置动作。自动回复不算；
- **SLA Credit**：违约确认后协助客户申领，时限建议 ≤ 5 个工作日（[附录 P](appx-p-tam-service-quality-standard-public-cloud.md) 的 P5.5-2）。Credit 是止损，不是补偿。TAM 的责任是不让客户自己发现违约。监测覆盖 100% 是服务质量项。

达成率月报化与预警线动作见[第 26+ 章](ch26-measurement-system-howto.md)。

## 26.5 事件效率指标口径

**口径定义**（[附录 I](appx-i-on-duty-standard.md)、[附录 K](appx-k-incident-emergency-drill-standard.md)、附录 P/Q 引用本节）：

| 指标 | 口径 | 注意 |
| --- | --- | --- |
| 平均确认时长（Mean Time To Acknowledge，MTTA） | 事件触发 → 值班人确认介入 | 附录 I 响应达标率的分子 |
| 平均修复时间（MTTR） | 确认介入 → **业务恢复**（非工单关闭） | 工单关闭晚于恢复，用关闭时间会虚高 |
| 平均故障间隔（MTBF） | 相邻两次同级故障的业务恢复点间隔 | 分级别算，P3/P4 混入会稀释信号 |
| 复发率 | 90 天内同根因事件再发生占比 | [附录 R](appx-r-problem-retrospective-standard.md) 的闭环质量锚点。目标 0 |

**防异化条款**：

- MTTR 分级分客户看趋势，不做绝对值横比。金融核心系统与测试环境没有可比性；
- 防“降级定级”：把 P1 记成 P2 让数字好看。防线是[第 19 章](ch19-financial-incident.md)定级标准与[附录 R](appx-r-problem-retrospective-standard.md)复盘核查；
- MTBF 长期走高要审计告警阈值。阈值调钝会造成假稳定（[附录 I](appx-i-on-duty-standard.md) 告警质量审计）。

指标使用与审计动作见[第 26+ 章](ch26-measurement-system-howto.md)。

## 26.6 感知度量口径

| 指标 | 问法 | 适用场景 | 频率 |
| --- | --- | --- | --- |
| CSAT（客户满意度） | “本次服务你满意吗”（5 分制） | 单次交互：工单、重保、评审后 | 事件后即时 |
| CES（费力度） | “办成这件事你费了多少劲” | 流程体检：客户觉得哪累 | 季度抽样 |
| NPS（净推荐值） | “你愿意把我们推荐给同行吗”（0–10） | 关系温度与续约先行指标 | 半年/年度 |

**口径约束**：

- 三指标互补不可互替：CSAT 管单次、CES 管流程、NPS 管关系。NPS 高而 CSAT 走低，说明关系存量在兜底、服务增量在恶化；
- 样本量口径：单客户 NPS 样本 < 5 时只看不考核。小样本波动是噪声；
- 防异化：禁止求高分话术与挑客户投放问卷（[附录 G](appx-g-tam-work-evaluation-standard.md) 红线 R3）。

低分回访与复盘触发规则见[第 26+ 章](ch26-measurement-system-howto.md)。

## 26.7 价值实现度量口径

续约时客户买的不是 SLA 绿条，是“这东西给我带来了什么”。价值实现度量分三类。结果沉淀为价值实现报告（Value Realization Report，VBR）。

1. **风险规避类**：重保零事故、演练拦住的隐患数。通告触达避免的停服也算。证据锚点见[附录 P](appx-p-tam-service-quality-standard-public-cloud.md) 的 D3。换算要有测算依据；
2. **效率与成本类**：包含三项。用量优化节省金额（[第 15 章](ch15-commercial-synergy.md)云成本优化）。MTTR 改善折算的业务时间。自动化替代的人日；
3. **业务结果类**：客户业务指标中可归因的部分。例如峰值承载、上线周期缩短。归因要谨慎。**写“贡献”不写“功劳”**。夸大归因，客户识破一次，价值报告信用清零。

价值度量进 QBR/EBR。季度业务回顾（Quarterly Business Review，QBR）与高管业务回顾（Executive Business Review，EBR）共用[模板 08](../templates/08-qbr-ebr-template.md)。一年至少沉淀一份 VBR。它是[附录 G](appx-g-tam-work-evaluation-standard.md) L3.7（价值证明交付）的考核证据。

## 26.8 指标异化与防异化

Goodhart 定律的标准剧本：指标变目标 → 行为变形 → 数据失真 → 决策失效。四个通用机制：

1. **配对制衡**：任何效率指标配一个质量指标。MTTR 配复发率，响应速度配一次解决率。单押一边必然变形；
2. **抽查审计**：季度按比例抽查原始记录，与上报值核对。造假适用[附录 G](appx-g-tam-work-evaluation-standard.md) 红线 R2/R3；
3. **趋势优于绝对值**：考核锚点用“逐季改善或优于基线”。[附录 P](appx-p-tam-service-quality-standard-public-cloud.md)/[附录 Q](appx-q-tam-service-quality-standard-dedicated-cloud.md) 已采用此锚点。绝对值横比逼出数字游戏；
4. **指标退休**：达标四季又无决策价值的指标降级为监测项。指标只增不减，三年后团队在为报表打工。

## 26.9 口径变更与引用纪律

- **唯一事实源**：本章定义口径，别处只引用不重定义。附录与模板中的同名指标，口径必须与本章一致；
- **变更留版本**：口径调整须记录生效日期与变更原因。历史数据按旧口径可比，不追溯重算；
- **变更通知**：口径变更同步附录 G/I/K/P/Q 与模板 10/15 的引用方。实施动作见[第 26+ 章](ch26-measurement-system-howto.md)。

---

**本章要点回顾**

1. 度量三目的：决策、信任、改进。元规则有三：口径先于数值、取数只认系统、每指标配防异化。
2. 四族有先后：健康领先，质量和效率同步，感知与价值滞后。只看滞后指标是后视镜开车。
3. 关键口径：SLA 按月分客户，不可用从确认到恢复验证。MTTR 止于业务恢复，不是工单关闭。MTBF 分级计算。健康分可下钻解释。
4. 感知三件套分工：CSAT 管单次、CES 管流程、NPS 管关系。小样本不考核，低分必回访。
5. 价值度量三类：风险规避、效率成本、业务结果。归因写贡献不写功劳。
6. 防异化四机制：配对制衡、抽查审计、趋势锚点、指标退休。实施动作见第 26+ 章。
