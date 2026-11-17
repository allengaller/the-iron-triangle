# 《The TAM Book of AI Era》整体缺陷与薄弱点评估

> 评估时点：2026-11-10
> 评估对象：`the-tam-book/manuscript/`（82 个 Markdown 文件，28.2 万中文字）、`the-tam-book/templates/`（23 份）、仓库根 README、导读、目录、DIATAXIS-MAP
> 评估方法：全量通读 + 量化体检（字数分布、引用网络、AI 密度、图表密度、元数据一致性）+ 横向对照（SA 书、BTE 书）
> 性质：第三方视角的内部评审记录，不修改任何正文

---

## 零、评估方法与口径

本评估不依赖印象，所有结论均可由**可复跑的命令**或**可核对的文件位置**支撑。复核命令见附录 C。

四类证据源：

1. **体量分布**：逐文件统计中文字数（正则 `[\u4e00-\u9fff]`），得全书字数谱与断崖位置；
2. **引用网络**：以文件名与标题字符串做入链统计，识别"存在但不被需要"的文件；
3. **内容密度**：AI 相关段落占比、图片数量、表格行数、清单类型分布、要点回顾覆盖；
4. **横向对照**：三书体量与完成度口径、跨书重叠审计的覆盖范围。

---

## 一、总体判断

**这是一部"体系完备、条目齐备，但体裁已经跑偏"的稿子。**

它有超过多数同类书的骨架完整度（79 个文件、23 个模板、120 条术语、0 断链、0 混合类型），但真正属于"一本书"的内容大约只有 15 万字；另外 12 万字是一个组织的**内部管理制度汇编**，被装进了附录。同时，副标题承诺的主线（AI 时代）在体量上只占 15.6%。

问题不在"写得少"，而在**四组结构失衡**：附录与正文失衡、读者与内容失衡、承诺与交付失衡、形式审计与内容价值失衡。

---

## 二、结构性缺陷（P0，决定这本书能不能成立）

### 1. 附录反客为主：43 个附录 > 36 个正文文件

| 指标 | 数值 |
|---|---|
| 正文 | 36 文件 / 154,734 字 / 均值 4,298 |
| 附录 | 43 文件 / 118,900 字 / 均值 2,765 |
| 附录占全书字数 | **42%** |
| 标"拟定稿"的文件 | **19 个** |
| 附录 / 正文文件数 | **43 : 36** |

更严重的是这 43 个附录里有 **15 对"标准 + 落地"文件**（附录 B/B+、I/I+、J/J+、K/K+、L/L+、M/M+、N/N+、O/O+、R/R+、S/S+、T/T+、U/U+、V/V+、Y/Y+）。14 个"落地件"的字数：

| 落地件 | 字数 |
|---|---|
| appx-j-enablement-training-howto | 1,360 |
| appx-k-incident-emergency-howto | 1,379 |
| appx-o-tam-onsite-promotion-howto | 1,390 |
| appx-n-tam-onsite-certification-howto | 1,393 |
| appx-u-ticket-management-howto | 1,449 |
| appx-m-product-introduction-howto | 1,478 |
| appx-i-on-duty-standard-howto | 1,494 |
| appx-l-project-onboarding-howto | 1,512 |
| appx-s-overtime-compoff-howto | 1,564 |
| appx-t-online-change-howto | 1,565 |
| appx-r-problem-retrospective-howto | 1,587 |
| appx-b-tam-process-system-howto | 1,670 |
| appx-v-tam-bte-sa-triangle-howto | 1,744 |
| appx-y-training-howto（唯一例外） | 2,972 |

13 个落在 1,360–1,744 字这个极窄区间，结构完全同构：**前置条件 → 五个操作 → 验收标准 → 故障排查 → 检查清单 → 要点回顾**。

这是批量模板的产物，不是内容需要。证据在引用网络里：**这 14 个文件在全书只有 3 个入链**（主件、自己的主件、一处顺带提及）。它们是"为了配套完整"而存在的，读者不会真的去读。

### 2. 体裁漂移：从"岗位方法书"变成"服务管理体系文件集"

附录 I–U 的实际内容是：值班排班、培训分级、驻场认证、晋升评审、加班调休折算、工单抽检、变更签批。

这些是**服务总监与 HR 的制度设计素材**，不是 TAM 个人能用的方法。而导读把"在职 TAM"列为第一读者。第一读者拿到的正文只有 15 万字，其中还有 8 个是"实战章"的重复叙事。

一句话：**它更像一套 ISO 体系文件，而不是一本 TAM 会在地铁上读的书。**

### 3. 内涵六维只完成 4/6，标尺闭环断裂

`00-outline.md` 第二部分明确写"每维两章：主章 Explanation + 实战章 How-to"。实际：

| 维度 | Explanation 主章 | How-to 实战章 | L1–L5 分级 |
|---|---|---|---|
| 技术纵深 | ch05 | ch05-practical | 有 |
| 业务洞察 | ch06 | ch06-practical | 有 |
| 关系经营 | ch07 | ch07-practical | 有 |
| 服务治理 | ch08 | ch08-practical | 有 |
| 风险合规 | **缺** | ch09（单章 9.1–9.9 全为操作） | **0 处** |
| 项目变革 | **缺** | ch10（单章 10.1–10.9 全为操作） | **0 处** |

而 `ch27-maturity-model.md` 规定"M3 要求六维无短板、单项最低 3 分"。**第 9、10 维没有分级标尺，无法打分。** 这是全书度量体系里唯一一处逻辑硬断裂。

附带问题：`ch28-career-team-building.md` 是 Explanation 章，但全书 12 个 Explanation 章里**只有它没有"学习效果清单"**，违反 `AGENTS.md` 自己规定的清单分类约定。

### 4. 后四章断崖式变薄，而最薄的两章自称"事实源"

| 区段 | 章均字数 |
|---|---|
| ch01–ch04 | 6,300 |
| ch05–ch15 | 4,700 |
| ch16–ch24 | 4,300 |
| **ch25–ch28** | **2,400** |

- `ch26-measurement-system.md`：**2,416 字**，自称"全书度量口径唯一事实源"
- `ch27-maturity-model.md`：**2,102 字**，自称"全书唯一映射事实源"
- `ch28-career-team-building.md`：**1,973 字**，是全书最短的正文文件

这是"事实源悖论"：作者用"唯一事实源 + 只引用不重定义"的架构纪律解决了重复问题，代价是**把认知切碎**。读者要搞懂"一个 TAM 怎么被评估"，得跨 ch26 + ch27 + 附录 G + N + O + J + 模板 12/13 共 8 个文件。而这 8 个文件里，最薄的就是那两个"事实源"。

ch26 具体缺什么（抽查）：

- 健康分只给"建议权重"，未给绿/黄/红阈值数字与计算方法；
- SLA 达成率的预警线未定义（只写"月报化与预警线动作见第 26+ 章"）；
- 口径变更无影响评估机制；
- 全部 9 节，无一个反例或误用案例。

### 5. 编号体系不可出版

`ch05-practical / ch06-practical / ch07-practical / ch08-practical / ch22-tam-copilot-tutorial / ch24-ai-risk-governance-howto / ch26-measurement-system-howto / ch28-career-team-building-howto`，在目录中被表述为 **第 5+、6+、7+、8+、22+、24+、26+、28+ 章**；附录同理为 **B+、I+、J+、K+…V+、Y+**。

用加号当章号，且阅读顺序是"第 22 章 → 第 22+ 章 → 第 23 章"。这套编号能跑通脚本校验，但**没有出版社能照此排版**，读者也会迷路。

---

## 三、内容质量缺陷

### 6. AI 主线被稀释到 15.6%

全书 3,466 个有效段落（中文字符 > 15）中，含 AI / 大模型 / LLM / 模型 / 智能体 / Agent / GPU / 推理 / 幻觉 / 提示词等词的仅 **540 段，占 15.6%**。

更刺眼的是核心制度附录的 AI 提及次数：

| 文件 | AI 提及 |
|---|---|
| 附录 K 故障应急与演练标准 | **0** |
| 附录 L 项目导入标准 | **0** |
| 附录 O 驻场晋升标准 | **0** |
| 附录 Q 专有云服务质量标准 | **0** |
| 附录 S 加班调休标准 | **0** |
| 附录 T 线上变更标准 | **0** |
| 附录 I 值班标准 | 1 |
| 附录 R 复盘标准 | 1 |

副标题是"AI 时代的 TAM 白皮书"。一本 AI 时代的书，连"值班""变更""晋升""复盘"都不提 AI 怎么改变它们，这个承诺是空的。第五部分 5 章（约 2 万字，占 7%）扛不动 28 万字的书名。

### 7. 零图。28 万字，0 张图，4,531 行表格

`grep "!\["` 全书结果 = **0**。

RACI、三链六要素、五域共管面、故障分钟级时序、成熟度阶梯、度量四族因果、闸门流程、铁三角接缝——这些**本质上是图形知识**，全部被压成表格。

`00-outline.md` 第 27 行承诺"一张 RACI 图说清边界"，交付的是表格。这不是排版问题，是**理解成本问题**：表格能查，图才能懂。

### 8. 案例章是全书可信度的命门，却是最薄的一章之一

`ch20-case-studies.md` 4,631 字装 4 个五段式案例（背景 → 冲突 → TAM 动作 → 结果 → 复盘），**每个约 1,100 字**。H 银行 / D 证券 / L 保险 / P 支付全部虚构，无一个真实公开案例、无一个可外部核验的数据锚点。

案例写作本身质量不差（"约 70% 耗时差来自联调环境数据分布失真"这类细节很有说服力），但一本讲"金融级顶级大项目落地"的书，**没有任何一个真实项目能证明这套打法被用过**。读者凭什么信？

### 9. 格言体：结论密度高，论证密度低

典型段落（`ch28` 28.5）：

> 绩效体系是附录 G 的三层评估。本章只补三条团队级原则。
> 1. 不背金额……
> 2. 团队健康进主管绩效……
> 3. 指标配对防异化……

每条 1–2 句，全是判决，没有反例、没有失败故事、没有"什么情况下这条不成立"。

结构上也一致：**76 / 82 个文件以"要点回顾"收尾**。这是内训 PPT 的结构，不是书的结构。书的结尾应该把问题交还给读者，不是再复述一遍要点。

### 10. 大量数值断言零出处

- 资源水位"不超过 70%"、"金融核心 50–60%"（ch05-practical）
- "EOL 前 6–12 个月启动评估"（ch05-practical）
- "抽查比例 10%"（appx-i+、appx-u）
- "99.95% = 重要业务系统"、"99.995% = 支付清算级"（ch05-practical）
- "内部转岗成功率高于外招"（ch28）

这些可能是对的行业经验，但**全书没有一处标注"这是经验值 / 这是某厂商口径 / 这是某标准条款"**。而 `AGENTS.md` 自己写着"数据、行情、监管条文等时效性内容必须标注来源与时点"。在自称"行业标准"的语境下，这个缺口会被专业读者第一眼抓住。

---

## 四、定位与可信度风险

### 11. "行业标准"自封 19 处

附录 G 的性质声明写得诚实（"不是任何官方机构发布的标准"），这点值得肯定。但**标题仍叫《TAM 工作评估行业标准》**，且没有任何外部机构评审、企业试点、专家背书。

一本开源书自封"行业标准"，实际效果是把主张降格为"作者个人意见"——读者会想：谁认？

### 12. 没有前置页

全书没有：序 / 前言 / 作者与背景介绍 / 致谢 / 索引 / 版本记录（`grep -i "front\|preface\|序\|ack\|index\|about\|changelog"` 在 manuscript 下为空）。

读者翻开不知道"凭什么信这个人"、"这本书的边界在哪"、"它和 ITIL、和厂商 TAM 手册的区别"。在一本要立"标准"的书里这是致命的——**权威感来自作者的可信度叙事，不是来自条文数量**。

### 13. 元数据全面漂移，门面第一印象即失分

`README.md` 与正文实际：

| README 说 | 实际 |
|---|---|
| 附录 30 个文件（A–W、Y、Z、AA–AC） | **43 个**，且漏 **AD** |
| 66 个正文文件 | **79**（DIATAXIS-MAP 口径）/ 82（磁盘） |
| Explanation 13 / How-to 23 / Reference 16 / Tutorial 2 / **混合 12** | 13 / 36 / 28 / 2 / **混合 0** |
| templates 22 份 | **23 份** |
| manuscript 65 个文件 | **82 个** |

`00-reading-guide.md` 第 48 行同样写"**22 个**可直接复制的模板"，且附录清单同样漏 AD。

一本把"唯一事实源"作为核心纪律的书，自己的门面数据落后两轮拆分战役。这不是笔误，是**没有"发布前一致性门禁"**。

---

## 五、根因分析：可审计性驱逐了可读性

`HANDOFF.md` 里记录的质量门是：**长句 0、被动语态 0、链接全通、表格列数一致、节号可校验**。

这些都是能被脚本验证的形式指标。而"这一章是否真的教会了读者一件事"、"这个判断在什么情况下会错"、"读者照做会不会翻车"——**没有任何一个环节校验这些**。

于是内容向"可分块、可登记、可校验"的形态单向收敛：表格、条文、五步法、要点回顾。这套流程能生产出**完美的一致性**，也能生产出 **13 个只有 1,500 字左右的同构附录**。

批量生产的痕迹已经漏出来了：

| 位置 | 问题 |
|---|---|
| `appx-i-on-duty-standard-howto.md` 第 4 行 | "五个动作：模式落地、排班执行、交接执行**。**日志与度量执行、红线处置。"（顿号误作句号） |
| 同文件第 66 行 | "客户敏感事项**。。**"（双句号） |
| `ch28-career-team-building.md` | Explanation 章缺"学习效果清单" |
| `ch18-major-assurance.md` | 存在"。。"双句号 |

四处都是"没人从头到尾通读过"的证据。

**这是本书最根本的病灶**：不是某一章写得不好，而是生产流程把"可被脚本审计"当成了质量本身。结果是全书呈现出高度同构、内容稀薄、论证缺失的统一形态——每一节都合格，整本书不透气。

---

## 六、公平地说：它做对了什么

评估需要基准，否则上面全是苛责：

| 项 | 表现 |
|---|---|
| 术语纪律 | 120 条术语表，只收"本书有特定含义"的词，明确排除 API/GPU/DNS 等通用词，这是专业做法 |
| 事实源架构 | "唯一事实源 + 只引用不重定义"解决了多作者重复定义的顽疾 |
| 脱敏规范 | 案例全虚构但明确声明，比"半真半假"诚实 |
| 附录 G 性质声明 | 主动说明"不是官方标准"，有分寸 |
| 时点标注机制 | 监管与厂商通告标数据时点，且设发布闸门 |
| 工具化 | xref 脚本、DIATAXIS-MAP、HANDOFF 登记，工程化程度远超一般书稿 |
| 单章质量 | ch01–ch04 的论证密度、ch26 的口径纪律、ch27 的映射表设计，均属上乘 |

问题不是它不专业，而是**专业的方向偏了**——它把"体系完备"当成了目标，而书的目标是"读者改变"。

---

## 七、建议的行动优先级

### P0（不做则这本书不成立）

1. **体裁二选一**。建议：正文 = 书（28 章 + 少量附录）；把 15 对制度件整体下沉为独立的《TAM 服务管理规范》配套文档，不进附录。附录从 43 降到 10–12。
2. **补齐 ch09 / ch10 的 Explanation 主章 + L1–L5 分级**，闭合六维标尺。否则 ch27 的"六维无短板"是空话。
3. **ch26 / ch27 扩到与"事实源"地位相称**（各 5,000 字以上，补阈值、算法、边界、反例）。
4. **重写 ch20**：至少 2 个有公开事实锚点的真实案例（可脱敏，但架构/时间/量级要能对上公开信息），每案例 3,000 字。

### P1（决定读者体验）

5. 14 个"落地件"合并回主件（改为"条文 + 执行"单文件），或整体移出。改造后附录控制在 12 个以内。
6. 补 **20 张图**：RACI、三链、五域共管面、故障时序、成熟度阶梯、四族因果、闸门流程、铁三角接缝、六维雷达、健康分下钻。
7. AI 主线加固：每个制度件加"AI 时代的增量"一节；或诚实声明"本书 70% 内容与 AI 无关，AI 部分集中在第五部分"。
8. 去掉"+"号编号，改 Part / Chapter 规范体系。

### P2（打磨）

9. README / 导读 / outline 元数据用脚本一次性生成，纳入发布门禁。
10. 关键判断补"反例 / 失败案例 / 不适用边界"——把格言体改成论证体。
11. 补前置页：序、作者与方法说明、索引、版本记录。

---

## 附录 A：量化体检原始数据

### A.1 正文 36 文件字数（升序）

| 文件 | 中文字 |
|---|---|
| ch28-career-team-building.md | 1,973 |
| ch27-maturity-model.md | 2,102 |
| ch28-career-team-building-howto.md | 2,132 |
| ch26-measurement-system-howto.md | 2,306 |
| ch26-measurement-system.md | 2,416 |
| ch05-practical.md | 2,526 |
| ch25-tam-irreplaceability.md | 3,003 |
| ch06-practical.md | 3,119 |
| ch22-ai-for-tam.md | 3,553 |
| ch15-commercial-synergy.md | 3,693 |
| ch14-partner-ecosystem.md | 3,727 |
| ch08-practical.md | 3,744 |
| ch17-financial-availability.md | 3,766 |
| ch24-ai-risk-governance-howto.md | 3,790 |
| ch19-financial-incident.md | 3,835 |
| ch07-practical.md | 3,856 |
| ch24-ai-risk-governance.md | 3,886 |
| ch16-financial-industry.md | 4,354 |
| ch11-customer-lifecycle.md | 4,396 |
| ch13-internal-collaboration.md | 4,542 |
| ch23-service-model-evolution.md | 4,604 |
| ch20-case-studies.md | 4,631 |
| ch12-escalation-crisis.md | 4,672 |
| ch22-tam-copilot-tutorial.md | 4,821 |
| ch09-risk-compliance.md | 5,048 |
| ch10-project-change.md | 5,181 |
| ch08-service-governance.md | 5,296 |
| ch07-relationship-management.md | 5,510 |
| ch18-major-assurance.md | 5,545 |
| ch21-ai-workload-assurance.md | 5,561 |
| ch06-business-insight.md | 5,861 |
| ch01-tam-origin-evolution.md | 5,978 |
| ch05-technical-depth.md | 6,066 |
| ch02-role-boundary-map.md | 6,106 |
| ch04-ai-era-tam-redefined.md | 6,424 |
| ch03-value-proposition.md | 6,711 |

合计 154,734 字，均值 4,298。

### A.2 附录 43 文件字数（升序）

| 文件 | 中文字 |
|---|---|
| appx-j-enablement-training-howto.md | 1,360 |
| appx-d-further-reading.md | 1,361 |
| appx-k-incident-emergency-howto.md | 1,379 |
| appx-o-tam-onsite-promotion-howto.md | 1,390 |
| appx-n-tam-onsite-certification-howto.md | 1,393 |
| appx-u-ticket-management-howto.md | 1,449 |
| appx-m-product-introduction-howto.md | 1,478 |
| appx-i-on-duty-standard-howto.md | 1,494 |
| appx-l-project-onboarding-howto.md | 1,512 |
| appx-n-tam-onsite-certification.md | 1,548 |
| appx-s-overtime-compoff-howto.md | 1,564 |
| appx-t-online-change-howto.md | 1,565 |
| appx-r-problem-retrospective-howto.md | 1,587 |
| appx-b-tam-process-system-howto.md | 1,670 |
| appx-v-tam-bte-sa-triangle-howto.md | 1,744 |
| appx-c-methodology-mapping.md | 1,764 |
| appx-j-enablement-training-standard.md | 1,881 |
| appx-f-cloud-vendor-notices-2026.md | 1,908 |
| appx-i-on-duty-standard.md | 1,955 |
| appx-e-contribution-guide.md | 1,956 |
| appx-ac-sre-cre-engineering-depth.md | 2,023 |
| appx-l-project-onboarding-standard.md | 2,037 |
| appx-k-incident-emergency-drill-standard.md | 2,261 |
| appx-s-overtime-compoff-standard.md | 2,420 |
| appx-h-tool-platform-acceptance-standard.md | 2,513 |
| appx-p-tam-service-quality-standard-public-cloud.md | 2,532 |
| appx-u-ticket-management-standard.md | 2,792 |
| appx-a-glossary.md | 2,802 |
| appx-m-product-introduction-standard.md | 2,886 |
| appx-y-training-howto.md | 2,972 |
| appx-y-training-tutorial.md | 3,041 |
| appx-v-tam-bte-sa-triangle.md | 3,050 |
| appx-q-tam-service-quality-standard-dedicated-cloud.md | 3,092 |
| appx-r-problem-retrospective-standard.md | 3,165 |
| appx-o-tam-onsite-promotion-standard.md | 3,254 |
| appx-w-financial-ops-standards.md | 3,309 |
| appx-b-tam-process-system.md | 3,757 |
| appx-t-online-change-standard.md | 3,831 |
| appx-g-tam-work-evaluation-standard.md | 3,864 |
| appx-ad-career-lifecycle-guide.md | 3,941 |
| appx-ab-subtam-domain-collaboration.md | 7,055 |
| appx-aa-tam-reporting-standard.md | 8,503 |
| appx-z-well-architected-framework.md | 11,842 |

合计 118,900 字，均值 2,765。

### A.3 全书形态统计

| 指标 | 数值 |
|---|---|
| 文件总数（manuscript） | 82 |
| 中文字总数 | 282,249 |
| 图片数 | **0** |
| 表格行总数（`^\|`） | 4,531 |
| 代码块标记数（`^```） | 30 |
| 以"要点回顾"收尾的文件 | **76 / 82** |
| 标"拟定稿"的文件 | 19 |
| 术语表条目 | 120 |
| 模板数 | 23 |
| 模板引用次数为 1 的 | 模板 13、17、23 |
| 模板引用次数为 2 的 | 模板 14 |

### A.4 引用网络（入链次数，节选）

| 入链 | 文件 |
|---|---|
| 32 | appx-r-problem-retrospective-standard |
| 23 | appx-g-tam-work-evaluation-standard、ch09-risk-compliance |
| 22 | ch26-measurement-system |
| 21 | ch05-technical-depth |
| 17 | ch08-service-governance |
| 16 | ch06-business-insight、ch07-relationship-management、ch10-project-change |
| 15 | ch22-ai-for-tam |
| 14 | ch12-escalation-crisis、ch19-financial-incident、appx-k-incident-emergency-drill-standard |
| 13 | ch02-role-boundary-map、ch16-financial-industry、ch18-major-assurance、appx-j-enablement-training-standard、appx-t-online-change-standard |
| **3** | **全部 14 个 howto 落地件**（appx-i+ / j+ / k+ / l+ / m+ / n+ / o+ / r+ / s+ / t+ / u+ / v+ / b+ / y+） |
| 3 | appx-w-financial-ops-standards、appx-c-methodology-mapping、appx-d-further-reading |
| 4 | ch25-tam-irreplaceability、ch05-practical、appx-z-well-architected-framework |

结论：入链最少的一档不是"冷门专题"，而是"落地件"这一类——它们的存在不构成任何章节的必要输入。

### A.5 AI 段落密度

| 指标 | 数值 |
|---|---|
| 有效段落（中文字 > 15） | 3,466 |
| 含 AI 相关词的段落 | 540 |
| 占比 | **15.6%** |

判定词：AI / 大模型 / LLM / 模型 / 智能体 / Agent / GPU / 推理 / 幻觉 / 提示词。

### A.6 三书体量与完成度口径

| 书 | 文件数 | 中文字 | 项目自称 |
|---|---|---|---|
| the-tam-book | 82 | 282,249 | v0.1 草案 |
| the-sa-book | 34 | 35,501 | **全书成稿** |
| the-bte-book | 44 | 64,900 | 初稿完成 |

跨书重叠审计（`the-bte-book/00-overlap-audit-2026-11-03.md`）只覆盖 **BTE vs SA** 与 **BTE vs TAM**，**没有做 TAM vs SA 的审计**；且审计方法为 12 字以上、字符相似度 ≥ 0.85 的句级比对，明确声明"不识别同义改写"。

同时，SA 书以 3.5 万字 / 34 文件被称为"全书成稿"，TAM 书以 28 万字 / 82 文件仍称"v0.1 草案"——**"成稿"的定义在项目内不一致**，三书同发会让读者对完成度产生误判。

---

## 附录 B：证据索引

每条结论对应的可核对位置。

| 结论 | 证据位置 |
|---|---|
| 附录占全书 42% | 附录 A.1 / A.2 字数表 |
| 14 个落地件同构 | `appx-i-on-duty-standard-howto.md` 与 `appx-j-enablement-training-howto.md` 等骨架逐一对照 |
| 落地件只有 3 入链 | 附录 A.4 |
| ch09/ch10 无分级 | `grep -c 'L1\.\|L1–L5' ch09-risk-compliance.md ch10-project-change.md`，结果均为 0 |
| ch28 缺学习效果清单 | `grep -c '学习效果清单' ch28-career-team-building.md` = 0，其余 12 个 Explanation 章均为 1 |
| ch26 只 2,416 字 | 附录 A.1 |
| ch27 只 2,102 字 | 附录 A.1 |
| 后四章均值 2,400 | 附录 A.1 分组统计 |
| AI 占 15.6% | 附录 A.5 |
| 附录 K/L/O/Q/S/T AI 提及为 0 | 逐文件 `grep -o "AI\|大模型\|智能体\|模型" \| wc -l` |
| 0 张图 | `grep -o "!\[" manuscript/*.md \| wc -l` = 0 |
| 4,531 行表格 | `grep -c "^\|" manuscript/*.md` 求和 |
| 76 文件以要点回顾收尾 | `grep -l "要点回顾" manuscript/*.md \| wc -l` = 76 |
| README 附录数 30 | `README.md` 第 32 行 |
| README 66 文件 / 混合 12 | `README.md` 第 34 行 |
| README 模板 22 | `README.md` 第 53 行 |
| 导读模板 22 | `00-reading-guide.md` 第 48 行 |
| 导读附录清单漏 AD | `00-reading-guide.md` 第 49 行 |
| 标点瑕疵 | `appx-i-on-duty-standard-howto.md` 第 4、66 行；`ch18-major-assurance.md` 存在"。。" |
| 15 对标准+落地 | 文件清单：B/B+、I/I+、J/J+、K/K+、L/L+、M/M+、N/N+、O/O+、R/R+、S/S+、T/T+、U/U+、V/V+、Y/Y+（14 对，B 对为流程体系） |
| 跨书审计未覆盖 TAM vs SA | `the-bte-book/00-overlap-audit-2026-11-03.md` 第 3、6 行审计范围 |

---

## 附录 C：复核命令

在 `the-tam-book/manuscript/` 下执行。

```bash
# 字数分布（中文）
python3 - <<'PY'
import re,glob
for f in sorted(glob.glob('*.md')):
    t=open(f,encoding='utf-8').read()
    print(len(re.findall(r'[\u4e00-\u9fff]',t)), f)
PY

# 图表密度
grep -o "!\[" *.md | wc -l
grep -c "^|" *.md | awk -F: '{s+=$2} END {print s}'

# 清单类型分布
grep -l "学习效果清单" *.md
grep -l "执行检查清单" *.md

# 分级缺失
for f in ch05-technical-depth.md ch06-business-insight.md ch07-relationship-management.md \
         ch08-service-governance.md ch09-risk-compliance.md ch10-project-change.md; do
  echo "$f $(grep -c 'L1\.\|L1–L5' $f)"
done

# AI 段落占比
python3 - <<'PY'
import re,glob
tot=ai=0
for f in glob.glob('*.md'):
    if f in ('00-outline.md','DIATAXIS-MAP.md'): continue
    for p in open(f,encoding='utf-8').read().split('\n\n'):
        if len(re.findall(r'[\u4e00-\u9fff]',p))>15:
            tot+=1
            if re.search(r'AI|大模型|LLM|模型|智能体|Agent|GPU|推理|幻觉|提示词',p): ai+=1
print(tot, ai, f"{ai/tot:.1%}")
PY

# 交叉引用体检
cd .. && python3 xref_check.py && python3 xref_check2.py
```

---

## 附录 D：本评估未覆盖的范围

诚实标注边界，避免读者误当全量结论：

1. **语义级重复**：未做句级相似度全量比对（仅抽样）。跨章"同义改写"的重复可能被低估。
2. **事实准确性**：未逐条核验监管条文、云厂商通告、GB/T 与 JR/T 条款（作者已有 `standards-verification-report-2026-10-25.md` 与之对应）。
3. **可读性实测**：未做真实读者试读（BTE 书有 `00-reader-test-kit.md`，TAM 书没有）。
4. **模板可用性**：23 份模板仅抽查模板 10，未逐个试填。
5. **代码与脚本**：仅运行 `xref_check.py` / `xref_check2.py`，未审计其分类逻辑（已知其将 79 个文件报为"章 28、附录 29、模板 23"，与 DIATAXIS-MAP 的 79 口径存在统计差）。

---

*本评估为内部评审记录，结论可直接引用，但不作为对外发布材料。*

---

## 附录 E：整改状态（2026-11-10 当日）

本附录记录"第五节根因"的整改落地情况，供后续核对。改后数据与改前不可直接比较——门禁口径同期调整过，见 `the-tam-book/QUALITY-GATE.md` 第十节改阈记录。

### E.1 已落地（机制层）

| 项 | 产物 | 说明 |
|---|---|---|
| 内容门禁 | `the-tam-book/scripts/content_gate.py`（491 行） | 按 Diátaxis 四体裁分档，测八项内容指标；`--strict` 拦发布、`--report` 出台账、`--calibrate` 定阈 |
| 门禁规范 | `the-tam-book/QUALITY-GATE.md`（128 行） | 指标逐条附盲区、block/warn 分界理由、三条 Goodhart 禁令、附录准入三问 |
| 同构审计 | `the-tam-book/scripts/similarity_audit.py`（186 行） | 跨文件文本重合 + 骨架同构，用并查集并簇，按两轴判定复刻/批量填充/统一体例 |
| 流程接入 | `AGENTS.md` 新增"内容门禁"节 | 交付前四条命令；三条纪律写入仓库规约 |
| 决策留痕 | `HANDOFF.md` 关键决策 + 两条交付记录 | 含两次判定校准的失败教训 |

关键设计取舍：**block 只收体裁矛盾与结构破损，内容厚度一律 warn**。首版曾把"具象密度为 0"判为 block，导致 5 个章节被拦——其中 ch02 岗位边界图合法地没有量化对象，硬拦会逼作者编数。同理，"机制因果""误区反例"的关键词骨架判定被整体删除：ch25 用"判据/连带效应/一笔账"讲因果却被误判，说明关键词骨架可被套利。

### E.2 已落地（内容层）

**ch28《TAM 的职业发展》**（唯一 block 项）：1,973 → 3,468 字（+76%）。补三处因果链（三特征为何构成链而非并列、为何先看最低分、考核什么就得到什么）、四处失效边界（内部转岗何时反成劣势、90 天期限可例外标准不可例外、出口设计失效条件、长板补位的前提）、一处面试验证法；新增 28.8 学习效果清单六条，补齐 12/13 章的约定缺口；要点回顾由 6 条压到 4 条。长句 0、被动 0、断链 0。

### E.3 新证据（本轮新增，此前未测）

跨文件同构审计（80 文件 3,160 对）：

- **骨架完全相同 84 对，同构簇 5 个。**
- 最重一簇 = **13 个落地件，骨架完全一致，字数 1,360–1,744（跨度 22%），簇内文本重合中位 0.04**。不是抄袭，是同一模板套十三遍。
- 附录 P/Q（公共云/专有云服务质量标准）文本重合 0.18，全书最高。两份本应"共用框架、差异在责任边界"，实际共用过多。
- ch09/ch12/ch13 骨架相同但文本重合 0.00，判为"统一体例"——内涵篇四段式设计使然，不是缺陷。这条区分很重要：**体例统一 ≠ 批量生产**。

### E.4 未落地（需 Allen 裁定或另立任务）

1. **13 个落地件是否合并**（附录 43 → 10–12 的前置问题）。属结构性删改，本轮不动正文。
2. **P/Q 是否抽共用部分到前言**。同上。
3. **warn 62 项的逐条修补**。台账已生成于 `the-tam-book/content-gate-report.md`，建议按"改它值不值"排序，不按数量。其中 ch02/ch03/ch05/ch07/ch14 五章具象密度为 0——不是误报，是通篇无一个带单位数据，需补真实锚点（不可编）。
4. **零图**（28 万字 0 图）。本轮未涉及。
5. **ch09/ch10 缺 Explanation 主章与 L1–L5 分级**。本轮未涉及。

### E.5 本附录对附录 D 的修正

附录 D 第 1 条"未做句级相似度全量比对"现已部分完成：跨文件 12 字片段包含率已全量比对（3,160 对）。仍未覆盖的是**同义改写**——换词复述会拉低分数，测不出。

---

## 附录 F：第 12、13 项整改状态（2026-11-10 当日）

第 12 项（没有前置页）与第 13 项（元数据漂移）同根：书的门面没有做。门面缺两样东西，一样是"这本书是什么"的叙事，一样是"这本书有多少内容"的数字。前者没有，读者不知凭什么信；后者不准，读者第一眼就发现不专业。

### F.1 第 12 项：补前置页五件

| 文件 | 作用 | 规模 |
|---|---|---|
| `manuscript/00-preface.md` | 前言：为什么有、主张什么、不主张什么、可信度来自哪、怎么读 | 1,421 字 |
| `manuscript/00-front-matter.md` | 版本、许可、如何引用、声明与边界、成书方式、关于作者、致谢 | 1,200 字 |
| `manuscript/99-index.md` | 章节／模板／附录三层编号索引 | 1,895 字，102 条 |
| `CHANGELOG.md` | 版本记录，v0.1 至 v0.2 五个版本 | 794 字 |
| `00-outline.md` 前置页节 + 导读入口 | 把上面四件接进目录与阅读路径 | — |

三个处理决定值得记录。

**其一，"凭什么信这个人"改成"凭什么信这本书"。** 评估原文说"权威感来自作者的可信度叙事"。本轮没有编造作者履历，而是把可信度重建在可复核上：建议可执行（落成清单与模板）、事实可追溯（来源与时点）、修订可复跑（脚本留库）、边界写明（每个模型的失效条件）。版权页明写"本书不列作者履历"及其理由。

**其二，"行业标准"自封问题（第 11 项）一并处理。** 版权页新增一节，把附录 G/H/I/J/K/L/M/N/O 九份文件定性为公开草案，明写"不是任何官方机构发布的标准，没有外部评审与企业试点"。这不解决命名问题，但解决了误导问题——读者拿到条文前就知道它是什么。

**其三，成书方式透明化。** 版权页写明判断与结构由作者定，起草与核查由 AI 辅助，三道检查（事实来源、句法规约、结论边界）由脚本执行。这比藏着更可信，也把"AI 写的书"这个质疑转成了可验证项。

### F.2 第 13 项：从"改对一次"改成"不会再错"

手改一遍数字只能追上今天。本轮改成三层机制：

1. **能算的不写。** `scripts/gen_metadata.py` 从磁盘算文件数、类型分布、字数、模板数、两份标准库份数、WA 归档页数、附录主件与落地件的字母区间。
2. **算出来的锁住。** 文档里的数字包进 `<!-- META:key -->` 标记区，标记区归脚本所有。共 30 处，分布在 README（8）、类型总览（14）、版权页（3）、导读（1）、GTM 落地页（4）。
3. **不一致就拦。** `--check` 漂移退出码 1，进 AGENTS.md 交付前五条命令。

索引同时变成生成物。`99-index.md` 由 `--index` 重建，禁止手改。这样"索引"与"数字"共用一套事实源，不会互相漂。

漂移实测修正，逐条可核：

| 位置 | 原值 | 实值 |
|---|---|---|
| README 附录数 | 30 个（漏 AD，漏 14 个落地件） | 43 个（主件 29 + 落地件 14） |
| README 类型分布 | 13/23/16/2/12，合计 66 | 13/36/28/2/0，合计 79 |
| README 正文文件 | 65 | 85（含前置页与索引） |
| README 模板 | 22 | 23 |
| README 标准主库 | 49 | 50 |
| 导读模板 | 22 | 23 |
| GTM 类型分布 | 13/23/16/2/12 | 13/36/28/2/0 |

**一个现场证据。** 本轮新建 `99-index.md` 后立刻跑 `--check`，README 的 82 就报成 83；再建前言与版权页，又报成 85。两次都是脚本抓到的，不是人眼发现的。这证明机制有效：手写追不上文件增删，脚本能。

### F.3 验证

```
元数据：30 处标记｜漂移 0｜--check 退出码 0
索引：章 36 / 模板 23 / 附录 43 = 102 条，链接全通
内容门禁：样本 83｜block 0｜warn 62｜通过 21｜--strict 退出码 0
同构审计：比较 3,403 对｜骨架完全相同 84 对｜同构簇 5 个（前置页未形成新簇）
交叉引用：xref_check 3 条（全为 HANDOFF:122 跨书历史存量）｜xref_check2 0 条
句式：新增四件长句 0、被动 0、断链 0
```

### F.4 未落地

1. **作者履历**。需要作者本人提供可公开的内容。本轮以"不列履历"的显式声明替代，不编造。
2. **页码索引**。Markdown 书没有页码，改做"章节／模板／附录"编号索引与四类事实源索引。概念索引未做，理由是附录 A 已是术语唯一事实源，再做一份必然漂。
3. **前置页与姊妹书的一致性**。BTE 书有 `00-front-matter.md`，TAM 书现在也有，但两书体例不同（BTE 合并在一个文件，TAM 拆成五个）。若三书要对齐出版体例，需另立任务。
