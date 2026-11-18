# 数值断言出处审计（the-bte-book）

> 生成方式：`python3 shared/tooling/claim_audit.py --report --book bte`（可复跑，勿手改）
> 口径见本脚本头部注释与 `QUALITY-GATE.md` 第十节。

样本 49 个文件｜高风险数值断言 20 条｜无口径块 14 个｜涉及 10 个文件

## 一、按文件（块数降序）

| 文件 | 无口径块 |
|---|---|
| ch07-value-engineering.md | 3 |
| ch09-commercial-architecture.md | 3 |
| ch03-value-proposition.md | 1 |
| ch05-opportunity-judgment.md | 1 |
| ch05-practical.md | 1 |
| ch07-practical.md | 1 |
| ch10-negotiation-relationship.md | 1 |
| ch13-value-case.md | 1 |
| ch23-bte-copilot-tutorial.md | 1 |
| ch26-bte-measurement.md | 1 |

## 二、明细（前 80 条）

| 文件:行 | 断言 | 原文片段 |
|---|---|---|
| ch03-value-proposition.md:98 | 12% | 口，不是只卖了软件 \| \| 结果 \| 变化带来什么业务后果 \| 季度放款量提升 12% \| \| 意义 \| 对客户意味着什么 \| 同样人力覆盖更多网 |
| ch05-opportunity-judgment.md:101 | 48 小时内 | 六种信号出现，48 小时内复核： |
| ch05-practical.md:148 | 100% | 证方式 \| \| --- \| --- \| --- \| \| 清单完整 \| 活跃商机 100% 在册 \| 抽查 CRM 与清单 \| \| 门槛证据 \| 五道 |
| ch07-practical.md:153 | 20% | 个指标写取数方式、频率、责任人； 3. 上线后按月或按季取数； 4. 偏差超过 20% 写归因； 5. 季度复盘，更新 VBR 素材。 |
| ch07-value-engineering.md:24 | 12% | 期从 5 天降到 2 天 \| \| 价值 \| 经济或风险后果 \| 季度放款量提升 12%，人力不变 \| |
| ch07-value-engineering.md:73 | 30% | 20 人，人均成本 15 万/年 \| \| 估算 \| 基于事实的推算 \| 可替代 30%，年省 540 万 \| \| 判断 \| 专家意见 \| 我认为替 |
| ch07-value-engineering.md:116 | 30% | 偏差要归因，不要掩盖。承诺 30% 替代率，实际 15%，就写 15%。写清原因，客户才会继续 |
| ch09-commercial-architecture.md:12 | 1000 万元 | 举例。某客户三年合同，TCV 都是 1000 万元。三种结构： |
| ch09-commercial-architecture.md:64 | 3000 万元 | 举例。某银行 AI 客服项目，BTE 测算三年可减少人工坐席成本 3000 万元。这个数字要拆开。四个变量是：现有坐席数、人均成本、可替代比 |
| ch09-commercial-architecture.md:85 | 60% | 一笔账：如果流量减半，公司毛利转负；如果流量翻倍，客户预算超支。最终结构是保底 60% 加超量阶梯价，加年度调价条款。客户接受，因为保底对应其最低 |
| ch10-negotiation-relationship.md:57 | 10% | 举例。客户要降价 10%。BTE 不直接让，换三个条件。合同从一年改三年，预付从 3 |
| ch13-value-case.md:131 | 20% | 个指标写取数方式、频率、责任人； 3. 上线后按月或按季取数； 4. 偏差超过 20% 写归因； 5. 验证结果进入 VBR 素材。 |
| ch23-bte-copilot-tutorial.md:78 | 30 分钟内 | **预期结果**：30 分钟内出一页可用简报。 |
| ch26-bte-measurement.md:76 | 10% | 利率，管道覆盖配转化率，预测准确率配增长率。 2. **抽查审计**：每季度抽 10% 商机，核对评分、承诺、成本。 3. **趋势锚点**：看连 |
