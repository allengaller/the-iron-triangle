# The TAM Book of AI Era｜AI 时代的 TAM 白皮书

> 开源技术图书 · 总体目录（v0.2 初稿）
>
> 定位：以 Technical Account Manager（TAM）岗位最佳实践为根本，以 AI 时代带来的变化为主线课题，
> 最终让读者（和作者自己）能够在企业级、金融级顶级大项目中落地这套实践。
> 最佳实践覆盖内涵（核心能力模型）与外延（生命周期、协同生态、商业化、行业纵深）全部维度。

---

## 前置页

- **前言**：为什么有这本书、主张什么、不主张什么、可信度来自哪、怎么读。已完成：`manuscript/00-preface.md`。
- **版权与版本页**：版本与状态、版权与许可、如何引用、声明与边界（含九份“标准”的公开草案性质）、成书方式、关于作者、致谢。已完成：`manuscript/00-front-matter.md`。
- **导读**：三类读者地图（在职 TAM／想转型的工程师／服务交付管理者）、两种读法（顺序读与场景索引读）、配套材料地图、开源协作方式。已完成：`manuscript/00-reading-guide.md`。
- **索引**：章节、模板、附录三层编号索引，由 `scripts/gen_metadata.py --index` 生成，不手改。已完成：`manuscript/99-index.md`。
- **版本记录**：修订历史与版本号规则。已完成：`CHANGELOG.md`（仓库根）。

---

## 第一部分　定位篇：TAM 是谁

> 回答"这个岗位到底是什么、为什么存在、AI 时代还存不存在"。

- **第 1 章　TAM 的起源与演进 [Explanation]**
  从产品支持到战略伙伴：Cisco / AWS / Microsoft / Google / Salesforce 的 TAM 体系对比；中国市场 TAM 的本土化变迁。样章已完成：`manuscript/ch01-tam-origin-evolution.md`（含 2026-10-25 联网核验的更名潮与来源时点标注）。样章已完成：`manuscript/ch01-tam-origin-evolution.md`。
- **第 2 章　岗位边界与协作图谱 [Reference]**
  TAM vs. 售前 SA、交付 PM、CSM、客服/支持工程师、SRE/运维、升级经理：一张 RACI 图说清边界与接缝。样章已完成：`manuscript/ch02-role-boundary-map.md`。
- **第 3 章　TAM 的三维价值主张 [Explanation]**
  对客户（技术成功与风险兜底）、对公司（续约与增购的技术引擎）、对生态（产品反馈回路）。样章已完成：`manuscript/ch03-value-proposition.md`。
- **第 4 章　AI 时代的 TAM 再定义 [Explanation]**
  从"技术客户经理"到"客户技术成功的操盘手"：AI 改变了什么、没改变什么；本书核心论点。样章已完成：`manuscript/ch04-ai-era-tam-redefined.md`。

## 第二部分　内涵篇：TAM 核心能力模型

> 内涵六维：技术纵深、业务洞察、关系经营、服务治理、风险合规、项目变革。每维两章：主章（Explanation）讲能力定义、机制与误区；实战章（How-to）给操作步骤、验收与排查，章号紧随主章。配套训练见附录 Y。

- **第 5 章　技术纵深 [Explanation]**
  架构评审、性能与容量规划、可用性设计评审、技术雷达与版本生命周期管理。样章已完成：`manuscript/ch05-technical-depth.md`。
- **第 6 章　技术纵深实战 [How-to]**
  架构评审、性能与容量规划、可用性设计评审、版本生命周期管理的操作步骤与验收标准。已完成：`manuscript/ch06-technical-depth-practical.md`。
- **第 7 章　业务洞察 [Explanation]**
  读懂客户业务目标（以金融为例：核心系统、渠道、风控、监管报送）；把技术指标翻译成业务价值。样章已完成：`manuscript/ch07-business-insight.md`。
- **第 8 章　业务洞察实战 [How-to]**
  画业务地图、建业务日历、做价值翻译、验目标挂靠。已完成：`manuscript/ch08-business-insight-practical.md`。
- **第 9 章　关系经营 [Explanation]**
  关键人地图（决策链/影响链/防线）、信任账户模型、高层对话（CIO/CTO/总工）、冲突与期望值管理。样章已完成：`manuscript/ch09-relationship-management.md`。
- **第 10 章　关系经营实战 [How-to]**
  画关键人地图、管信任账户、做高层对话、处理冲突与期望值、带边界地拒绝。已完成：`manuscript/ch10-relationship-management-practical.md`。
- **第 11 章　服务治理 [Explanation]**
  服务计划（Service Plan）、SLA/OLA/XLA、变更与发布治理、配置与资产可视、例会体系、服务质量度量（附录 P/Q 五/六维度框架与模板 15 记分卡）。样章已完成：`manuscript/ch11-service-governance.md`。
- **第 12 章　服务治理实战 [How-to]**
  定服务计划、管 SLA/OLA/XLA、治变更、建资产台账、跑例会、度量服务质量。已完成：`manuscript/ch12-service-governance-practical.md`。
- **第 13 章　风险与合规 [Explanation]**
  风险与合规能力的定义、形成机制、分级标尺（L1–L5）与常见误区；与技术纵深、项目变革两维的接缝。待完成：`manuscript/ch13-risk-compliance.md`。
- **第 14 章　风险与合规实战 [How-to]**
  风险登记册、主动式风险扫描、审计与监管配合、数据安全边界。已完成：`manuscript/ch14-risk-compliance-practical.md`。
- **第 15 章　项目与变革管理 [Explanation]**
  项目与变革能力的定义、形成机制、分级标尺（L1–L5）与常见误区；闸门治理与技术仲裁的"为什么"。待完成：`manuscript/ch15-project-change.md`。
- **第 16 章　项目与变革管理实战 [How-to]**
  大型项目节奏感：里程碑、上线闸门（Go/No-Go）、跨厂商集成的技术仲裁、客户侧变革推动。已完成：`manuscript/ch16-project-change-practical.md`。

## 第三部分　外延篇：工作全景与生态协同

> 外延四维：客户全生命周期、升级与危机、内部协同、伙伴生态与商业化。

- **第 17 章　客户全生命周期运营 [How-to]**
  Onboarding（90 天计划）→ 采纳深化 → 稳态运营 → 续约/扩容；每个阶段的交付物与节奏表。样章已完成：`manuscript/ch17-customer-lifecycle.md`。
- **第 18 章　升级与危机管理 [How-to]**
  Escalation 机制设计、作战室（War Room）运作、重大故障中的客户沟通脚本、事后信任重建。样章已完成：`manuscript/ch18-escalation-crisis.md`。
- **第 19 章　内部协同接口 [How-to]**
  与研发/产品的需求通道、与支持团队的工单质量、与销售/续费团队的信号共享；内部 RACI 与灰度地带处理。样章已完成：`manuscript/ch19-internal-collaboration.md`。
- **第 20 章　伙伴与供应链生态 [How-to]**
  生态角色与位置识别、接口规范、联合治理、接缝争议处理；总集、分包与平级三种位置的 TAM 打法。样章已完成：`manuscript/ch20-partner-ecosystem.md`。
- **第 21 章　商业化协同 [How-to]**
  续约预测的技术信号、用量健康度、增购机会识别、QBR/EBR 的设计与交付、价值实现报告（VBR）。样章已完成：`manuscript/ch21-commercial-synergy.md`。

## 第四部分　金融级实战篇：顶级大项目落地

> 目标篇：把前三篇的能力在金融级场景中合成可执行打法。所有案例脱敏虚构化处理。

- **第 22 章　金融行业的特殊性 [Explanation]**
  监管体系速览（金融监管总局/人行/证监会、等保 2.0、数据分级分类、信创要求）；金融客户决策链与采购特点。样章已完成：`manuscript/ch22-financial-industry.md`。
- **第 23 章　金融级可用性架构护航 [How-to]**
  两地三中心与单元化、容灾演练组织、变更冻结窗口、灰度与回退纪律、容量与峰值水位。样章已完成：`manuscript/ch23-financial-availability.md`。
- **第 24 章　重大保障（重保）方法论 [How-to]**
  核心系统上线、年终决算、大促/行情峰值：重保立项 → 体检 → 预案 → 值守 → 复盘五阶段全流程，附完整 Checklist。样章已完成：`manuscript/ch24-major-assurance.md`。
- **第 25 章　金融级事件管理 [How-to]**
  分钟级响应机制、监管事件上报口径、RCA 的金融级标准、故障定级与问责边界。样章已完成：`manuscript/ch25-financial-incident.md`。
- **第 26 章　标杆案例解剖（虚构化案例集） [Explanation]**
  国有大行核心下移、券商极速交易系统、保险核心替换、支付清算峰值保障：每个案例按"背景 → 冲突 → TAM 动作 → 结果 → 复盘"展开。样章已完成：`manuscript/ch26-case-studies.md`（H 银行/D 证券/L 保险/P 支付四案例，五段结构即附录 E 案例征集的体例样板）。

## 第五部分　AI 变革篇：AI 时代的新课题（主线）

> 三条线：AI 作为客户的工作负载（要为它护航）、AI 作为 TAM 的生产力（要用它武装自己）、AI 对服务模式和岗位本身的冲击。

- **第 27 章　护航 AI 工作负载 [How-to]**
  LLM/GenAI/Agent 项目的交付特点：GPU 容量与排队、推理成本与 FinOps、模型评估与上线闸门、RAG/微调架构评审要点。样章已完成：`manuscript/ch27-ai-workload-assurance.md`。
- **第 28 章　AI for TAM：用 AI 武装自己 [How-to]**
  数据／人审／判断三边界；个人知识库 RAG、工单智能摘要与聚类、会议纪要与行动项自动化、AI 辅助 RCA、提示词与工作流资产化。样章已完成：`manuscript/ch28-ai-for-tam.md`。
- **第 29 章　TAM Copilot 搭建教程 [Tutorial]**
  沙箱准备、知识库组织、知识问答、工单摘要、纪要结构化、周报草稿、提示词版本库、月度抽检与真实数据上线检查。样章已完成：`manuscript/ch29-tam-copilot-tutorial.md`。
- **第 30 章　服务模式的跃迁 [Explanation]**
  被动响应 → 主动预防 → 预测性服务 → 自愈系统：成熟度阶梯、AIOps 接入、告警降噪与异常检测的落地边界。样章已完成：`manuscript/ch30-service-model-evolution.md`。
- **第 31 章　AI 时代的新风险与解析 [Explanation]**
  三类概率性偏差（幻觉、漂移、偏见）的成因机制、金融 AI 监管坐标、数据与提示词边界、AI 决策的可解释性与问责链。样章已完成：`manuscript/ch31-ai-risk-governance.md`（监管内容时点 2026-10-23，含时点声明与发布闸门）。
- **第 32 章　AI 风险治理动作 [How-to]**
  AI 应用台账、高风险识别判定、上线闸门证据、漂移监测、数据流与提示词边界评审、人工复核检查、AI 事件复盘、供应商治理与风险登记册接入。样章已完成：`manuscript/ch32-ai-risk-governance-howto.md`。
- **第 33 章　TAM 的不可替代性 [Explanation]**
  AI 吃掉什么（信息搬运、初稿、例行巡检、浅层咨询）、留下什么（信任、判断、政治敏感度、责任承担）、放大什么（人效与差距）；新能力清单、职业生涯含义与六个常见误区。样章已完成：`manuscript/ch33-tam-irreplaceability.md`。

## 第六部分　度量与成长篇

- **第 34 章　度量体系 [Reference]**
  客户健康分口径、NPS/CSAT/CES、SLA 达成与 SLA Credit、MTTR/MTBF、价值实现度量；指标异化与防异化机制、口径变更纪律。样章已完成：`manuscript/ch34-measurement-system.md`（全书指标口径唯一事实源，附录 G/I/K/P/Q 只引用不重定义）。
- **第 35 章　度量实施动作 [How-to]**
  统一口径落地、取数与平台证据、健康分运营、SLA 达成管理、事件效率使用、感知调研执行、价值度量与 VBR 沉淀、防异化审计与指标退休。样章已完成：`manuscript/ch35-measurement-system-howto.md`。
- **第 36 章　TAM 成熟度模型 [Reference]**
  个人五级（执行者 → 可靠接口人 → 顾问 → 战略伙伴 → 行业影响力）与团队五级；各级证据口径、跃迁标志与误判；使用纪律与晋级路径。样章已完成：`manuscript/ch36-maturity-model.md`（36.3 标尺映射表为全书唯一映射事实源：附录 G/N/O/J 与模板 12 统一锚定 M1–M5）。
- **第 37 章　TAM 的职业发展 [Explanation]**
  岗位三特征与设计含义、技能矩阵（内容维度×高度）、招聘画像、90 天培养框架、绩效设计原则、出口生态设计与常见误区。样章已完成：`manuscript/ch37-career-team-building.md`（附录 G/J/N/O/S 的上游：职业框架与团队设计原则）。
- **第 38 章　团队建设动作 [How-to]**
  技能矩阵搭建、招聘执行、新人 90 天培养运行、团队结构配置、绩效与激励落地、出口经营与方法论沉淀。样章已完成：`manuscript/ch38-career-team-building-howto.md`。

## 第七部分　开源工具箱（模板与清单库）

> 所有模板以可复制的 Markdown/Excel 形式收录于 `templates/` 目录，随书共建。

1. 服务计划（Service Plan）模板。已完成：`templates/01-service-plan.md`（配套第 11 章、附录 B 流程 P1；附录 I/Q/T/M/L 的入计划条款均有承载节）。
2. Onboarding 90 天清单。已完成：`templates/02-onboarding-90d-checklist.md`（配套附录 L/M）。
3. 架构评审 Checklist（含 AI 工作负载专项）。已完成：`templates/03-architecture-review-checklist.md`（配套第 5 章、附录 G/L/M）。
4. 上线闸门（Go/No-Go）清单。已完成：`templates/04-go-nogo-gate-checklist.md`（配套第 16 章、附录 K/M）。
5. 重保 Checklist 与值守手册。已完成：`templates/05-major-assurance-checklist.md`（配套第 24 章、附录 B 流程 P5）。
6. 重大事件沟通脚本与升级矩阵。已完成：`templates/06-major-incident-communication-matrix.md`（配套第 18 章、附录 K）。
7. RCA 模板（金融级）。已完成：`templates/07-rca-template.md`（配套附录 K/R、第 25 章；初步 48h / 正式 5 个工作日，防线四问必答，改进项汇模板 16/09）。
8. QBR/EBR 模板。已完成：`templates/08-qbr-ebr-template.md`（配套第 21 章、附录 B 流程 P8）。
9. 风险登记册模板。已完成：`templates/09-risk-register.md`（配套第 14 章；3×3 分级、月度过册、三扫描线汇入、关闭验证与附录 R 联动）。
10. 客户健康度评分卡。已完成：`templates/10-customer-health-scorecard.md`（配套第 34 章 34.3，与模板 15 组成起跑两件套）。
11. 关键人地图画布。已完成：`templates/11-key-person-map-canvas.md`（配套第 10 章 10.1 节，模板 10 健康分 R1 取数来源；三链六要素、三层覆盖核查、防线专项、两周变动日志）。
12. TAM 个人能力自检表。已完成：`templates/12-tam-self-assessment.md`（配套附录 G、第二部分各章自检清单）。
13. TAM 工作评估计分卡。已完成：`templates/13-tam-evaluation-scorecard.md`（配套附录 G）。
14. TAM 驻场晋升申请与证据核验表。已完成：`templates/14-onsite-promotion-review-checklist.md`（配套附录 O）。
15. TAM 服务质量记分卡（公共云 / 专有云双版本）。已完成：`templates/15-tam-service-quality-scorecard.md`（配套附录 P/Q）。
16. 问题复盘报告与改进项台账。已完成：`templates/16-problem-retrospective-template.md`（配套附录 R）。
17. TAM 加班认定与调休台账。已完成：`templates/17-overtime-compoff-ledger.md`（配套附录 S）。
18. 变更申请与实施记录单（变更台账）。已完成：`templates/18-change-request-record.md`（配套附录 T）。
19. 承诺清单与移交三件套（铁三角协同台账）。已完成：`templates/19-commitment-handover-kit.md`（配套附录 V）。
20. 主 TAM 报告四件套（日/周/季/年）。已完成：`templates/20-lead-tam-reporting-set.md`（配套附录 AA 的 RP1–RP4；第 28/34/37 章）。
21. 团队成员报告四件套（日/周/季/年）。已完成：`templates/21-team-member-reporting-set.md`（配套附录 AA 的 RP5–RP8；附录 G/O、模板 12）。
22. 子 TAM 域分工与共管面矩阵。已完成：`templates/22-subtam-domain-collaboration-matrix.md`（配套附录 AB 的五域、十面共管面、四字段工单与交接包）。
23. 个人年度职业体检表。已完成：`templates/23-career-annual-checkup.md`（配套附录 AD：CL 阶段判定、四账户盘点、五红灯自查与处置计划；与模板 12 互补——能力 vs 职业资本）。

## 附录

- **附录 A**　术语表（中英对照）：全书术语唯一事实源，分八组（岗位组织/服务流程/等级度量/生命周期商业化/风险合规金融级/人员组织/AI 时代/编号前缀速查），A.8 消解 P 前缀四义。已完成：`manuscript/appx-a-glossary.md`（v0.1，随书滚动补充；2026-10-25 经并发覆盖后以此版为准，详见 HANDOFF 撞车记录）。
- **附录 B**　TAM 体系流程与规范：十二项核心流程速查（P1–P12）与九项运营规范汇编（含驻场组内自检任务标准）、流程成熟度分级。样章已完成：`manuscript/appx-b-tam-process-system.md`（Reference：流程地图与规范条文）。
- **附录 C**　方法论与标准映射：ITIL 4 / IT4IT / SRE / FinOps / 等保 2.0 / Well-Architected 六种方法论与本书章节的对应（WA 映射见 C.6，六厂商全量对照见附录 Z）。已完成：`manuscript/appx-c-methodology-mapping.md`（迁移索引工具，非标准拟定稿；SRE 映射前须过第 2 章岗位边界）。
- **附录 D**　延伸阅读与参考资料：真实可获取文献按五组对应章节 + 内部资料索引 + 维护规则（监管类年度复核）。已完成：`manuscript/appx-d-further-reading.md`。
- **附录 E**　开源贡献指南：如何提交勘误、案例与模板。已完成：`manuscript/appx-e-contribution-guide.md`（三类贡献流程、维护纪律唯一事实源对照表、拒绝清单）。
- **附录 F**　2026 年主要云厂商通告汇编：退市/下线/生命周期通告速查（AWS/Azure/Google Cloud/阿里云/腾讯云/华为云），数据时点 2026-10-23。样章已完成：`manuscript/appx-f-cloud-vendor-notices-2026.md`。
- **附录 G**　TAM 工作评估标准（拟定稿）：三层指标（L1 能力/L2 过程/L3 结果）、S–D 五级、四条否决红线。已完成：`manuscript/appx-g-tam-work-evaluation-standard.md`。
- **附录 H**　TAM 工具与平台验收标准（拟定稿）：六类平台【必须】/【建议】验收项、三阶段验收流程、否决条款。已完成：`manuscript/appx-h-tool-platform-acceptance-standard.md`。
- **附录 I**　TAM 值班标准（拟定稿）：三档值班模式（M1/M2/M3）、排班与疲劳管理、P1–P4 响应与升级时限、行为红线与度量。已完成：`manuscript/appx-i-on-duty-standard.md`。
- **附录 J**　TAM 赋能与实操培训标准（拟定稿）：T1/T2/T3 三级培训体系、实操占比 ≥ 50%、三段式认证、认证与客户分配挂钩。已完成：`manuscript/appx-j-enablement-training-standard.md`。
- **附录 K**　TAM 故障应急与演练标准（拟定稿）：P1 黄金 30 分钟动作序列、作战室接口、三级演练与合格判定、事后闭环与红线。已完成：`manuscript/appx-k-incident-emergency-drill-standard.md`。
- **附录 L**　TAM 项目导入标准（拟定稿）：导入四阶段闸门（S1–S4）、各阶段交付物、七项量化验收锚点、二手项目与金融级专项要求。已完成：`manuscript/appx-l-project-onboarding-standard.md`。
- **附录 M**　TAM 产品导入标准（拟定稿）：产品能力导入五阶段（PL1–PL5）与技术转移（分层转移、认证为准、独立运营准入验收、AI 产品专项）。已完成：`manuscript/appx-m-product-introduction-standard.md`。
- **附录 N**　TAM 驻场能力认证标准：C1–C3 三级认证（维度权重、五种考核方式、合格线与一票否决项、认证与年审流程）。样章已完成：`manuscript/appx-n-tam-onsite-certification.md`。
- **附录 O**　TAM 驻场能力晋升标准（拟定稿）：C3 后专家/现场管理双通道、四块晋升证据（经验/能力/客户/组织贡献）、评审流程与 6 个月观察期、破格与降级机制。已完成：`manuscript/appx-o-tam-onsite-promotion-standard.md`。
- **附录 P**　TAM 服务质量标准·公共云版（拟定稿）：五维度质量框架（响应与事件/主动服务/变更与通告/服务节奏/结果与感知）、SLA 监测与 Credit 协助、厂商通告触达义务、四条质量红线。已完成：`manuscript/appx-p-tam-service-quality-standard-public-cloud.md`。
- **附录 Q**　TAM 服务质量标准·专有云版（拟定稿）：六维度质量框架（含平台运行质量、合规与审计支持两个专有云特有维度）、责任共担边界、版本合规率与冻结窗口纪律、驻场衔接。已完成：`manuscript/appx-q-tam-service-quality-standard-dedicated-cloud.md`。
- **附录 R**　TAM 问题复盘标准（拟定稿）：三级复盘与六条强制触发、四阶段流程（RT1–RT4）、技术/管理/客情三类复盘要点、闭环度量与红线。已完成：`manuscript/appx-r-problem-retrospective-standard.md`。
- **附录 S**　TAM 加班与调休管理标准（拟定稿）：OT1/OT2/OT3 三分类认定、审批与 36 小时管控上限、调休分级折算与刚性兑现、疲劳红线与度量。已完成：`manuscript/appx-s-overtime-compoff-standard.md`。
- **附录 T**　TAM 线上变更标准（拟定稿）：CH1–CH4 变更分级与五条通用原则，分公共云版（通告触达、影响分析、确认/延期、值守回访）与专有云版（三板斧评审、分级签批、双人复核、窗口与冻结纪律、监管留痕）两个执行版本。已完成：`manuscript/appx-t-online-change-standard.md`。
- **附录 U**　TAM 工单管理标准（拟定稿）：四分类 TK-F/Q/R/C 与 P1–P4 分级复用、时限与静默规则、记录七要素、关闭与重开规则、≥10% 抽检四维评分、四条红线。已完成：`manuscript/appx-u-ticket-management-standard.md`。
- **附录 V**　TAM-BTE-SA 铁三角协同最佳实践：三角角色分工与全周期 RACI、四个接缝打法（承诺管理 / 方案评审可运营性一票 / 移交三件套 + 伴随期 / 信号回流三类分道）、例行协同机制、共背+分背联合度量、四条红线、AI 时代的三角变化。已完成：`manuscript/appx-v-tam-bte-sa-triangle.md`。
- **附录 W**　中国金融行业运维相关标准与监管要求汇编：法律与行政法规、GB/GB/T 国标（等保 2.0、运维服务、数据中心、容灾）、JR/T 金融行业标准（JR/T 0265、JR/T 0361-2026 智能运维等）、三监管条线规章（银监发〔2009〕19 号/银监办发〔2010〕114 号/证监会信息技术管理办法等）四层汇编；含"国七条"辨伪（查无此文件，最接近者为 GB/T 20988 灾难恢复七级）。数据时点 2026-10-25，年度复核。已完成：`manuscript/appx-w-financial-ops-standards.md`。
- **附录 Y**　六维能力训练教程：技术纵深、业务洞察、关系经营、服务治理、风险与合规、项目与变革六维逐维训练，Y.1–Y.7 训练流程（目标、前置、走法、预期结果、常见错误），末节为六维联合评审综合演练与完成判定。已完成：`manuscript/appx-y-training-tutorial.md`（Tutorial）。
- **附录 Z**　Well-Architected 架构框架全量汇编：AWS／Azure／Google Cloud／阿里云／腾讯云／华为云六家的支柱与设计原则逐条对照（含能力域对齐矩阵）、Lens／Perspective／Workload 全量索引、8 域 40 问评审动作库、10 个公开案例与参考架构；记录 Google 官网"六支柱／五支柱"口径不一、AWS Lens 30 份、阿里云 AI Lens 等时点事实。附与第 5 章、模板 03、附录 C/W 的分工与维护规则。数据时点 2026-10-25，季度复核。已完成：`manuscript/appx-z-well-architected-framework.md`；官方原文归档于 `well-architected/`（六厂商 5741 份，含 AWS 30 份 Lens 全量，见 Z.9.2）。
- **附录 AA**　TAM 报告体系标准（拟定稿）：主 TAM 与团队成员的双轨四级报告（RP1–RP4 / RP5–RP8）、八个决策槽与必填结构、双轨衔接的反二传手三规则、四判据与五种病、AI 时代的方法与呈现（一数三面、异常优先、请求区块、活页 diff、结构化抬头）、30/60/90 落地路径与四条红线。已完成：`manuscript/appx-aa-tam-reporting-standard.md`（配套模板 20/21；字母取双字母 AA，X/Y/Z 均已占用）。
- **附录 AB**　标杆项目 TAM 团队分域分工与协作最佳实践（拟定稿）：机房／IaaS／PaaS／SaaS／AI-Infra 五域责任地图、十个共管面与面主机制、三档编制与“1 + N”值班、四字段域间工单、跨域变更三问、故障三权分立（事实／判断／流程）、域手册五件套、五个协作指标与四条红线。已完成：`manuscript/appx-ab-subtam-domain-collaboration.md`（配套模板 22；字母取双字母 AB，与“A/B 测试”不是同一记号）。
- **附录 AC**　SRE/CRE 工程纵深（How-to）：错误预算政策（SLI/SLO、烧率告警、耗尽冻结）、On-Call 体系（主备双岗、认证上岗、书面交接）、Toil 治理（五特征、台账、削减路径）、不透题演练与流程级复盘；SLO 与 SLA 别混、金融级增量（监管窗口策略、预算非免责牌）。已完成：`manuscript/appx-ac-sre-cre-engineering-depth.md`（口径同源第 34 章与附录 C.3/I/K/R/S；适用岗位别名映射见导读）。
- **附录 AD**　TAM 职场全生命周期生存与发展指南：CL1–CL6 六阶段打法（入行/生存/成长/瓶颈/跃迁/长青，按证据判定不按年龄）、职业资本四账户年度体检、四大生存主题（向上管理/办公室政治工程化解法/倦怠与健康管理/裁员与跳槽纪律）、五条职业红线。已完成：`manuscript/appx-ad-career-lifecycle-guide.md`（How-to；与第 33/36/37 章分工：讲个人全周期的生存动作与发展动作；BTE/SA 角色同样适用，见 AD.0）。
