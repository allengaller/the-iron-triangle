# 内容质量门禁报告

> 生成方式：`python3 shared/tooling/content_gate.py --report`（可复跑，勿手改）
> 口径与盲区见 `QUALITY-GATE.md`；本节报告只举证，不代替人工通读。

样本 71 个文件｜block 0｜warn 39｜通过 32

## 一、block：体裁矛盾与结构破损（当期必修）

无。

## 二、warn：内容厚度（进整改台账，不阻断发布）

| 文件 | 类型 | 中文字 | 差距 | 整改方向 |
|---|---|---|---|---|
| appx-a-glossary.md | Reference | 3309 | 骨架 缺：交叉引用（至少 2 个文件链接）<br>表格密度 39.58 > 30 | 补体裁必需的结构件，或改标注为正确体裁；表格过多，改为正文论证，只留真正需要对照的表 |
| appx-aa-tam-reporting-standard.md | Reference | 8547 | 骨架 缺：交叉引用（至少 2 个文件链接） | 补体裁必需的结构件，或改标注为正确体裁 |
| appx-ab-subtam-domain-collaboration.md | Reference | 7135 | 骨架 缺：交叉引用（至少 2 个文件链接）<br>具象密度 2.02 < 2.5 | 补体裁必需的结构件，或改标注为正确体裁；补带来源的真实数字与时限；确实无量化对象则注明原因 |
| appx-ac-sre-cre-engineering-depth.md | How-to | 2281 | 具象密度 1.39 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| appx-ad-career-lifecycle-guide.md | How-to | 4244 | 失效边界词 2 < 3 | 补失效条件：什么情况下这条主张不成立 |
| appx-b-tam-process-system.md | Reference | 5739 | 清单化率 0.765 > 0.65 | 把清单条目展开成论证段 |
| appx-c-methodology-mapping.md | Reference | 1764 | 具象密度 2.48 < 2.5<br>表格密度 38.41 > 30 | 补带来源的真实数字与时限；确实无量化对象则注明原因；表格过多，改为正文论证，只留真正需要对照的表 |
| appx-d-further-reading.md | Reference | 1361 | 表格密度 36.72 > 30 | 表格过多，改为正文论证，只留真正需要对照的表 |
| appx-e-contribution-guide.md | How-to | 2214 | 具象密度 0.0 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| appx-g-tam-work-evaluation-standard.md | Reference | 4331 | 骨架 缺：交叉引用（至少 2 个文件链接） | 补体裁必需的结构件，或改标注为正确体裁 |
| appx-h-tool-platform-acceptance-standard.md | Reference | 2546 | 骨架 缺：交叉引用（至少 2 个文件链接） | 补体裁必需的结构件，或改标注为正确体裁 |
| appx-l-project-onboarding-standard.md | Reference | 3949 | n-gram 重复 0.127 > 0.12 | 同构段改写：合并重复句式，换论证角度 |
| appx-r-problem-retrospective-standard.md | Reference | 4928 | 骨架 缺：交叉引用（至少 2 个文件链接）<br>清单化率 0.689 > 0.65 | 补体裁必需的结构件，或改标注为正确体裁；把清单条目展开成论证段 |
| appx-t-online-change-standard.md | Reference | 5936 | n-gram 重复 0.129 > 0.12 | 同构段改写：合并重复句式，换论证角度 |
| appx-u-ticket-management-standard.md | Reference | 4421 | 骨架 缺：交叉引用（至少 2 个文件链接） | 补体裁必需的结构件，或改标注为正确体裁 |
| appx-v-tam-bte-sa-triangle.md | Reference | 4932 | 清单化率 0.683 > 0.65 | 把清单条目展开成论证段 |
| appx-y-training-tutorial.md | Tutorial | 6152 | 段落均长 24.0 < 25<br>n-gram 重复 0.169 > 0.12 | 把碎片句并为完整论证段，或反过来拆分超长段；同构段改写：合并重复句式，换论证角度 |
| appx-z-well-architected-framework.md | Reference | 11912 | 骨架 缺：交叉引用（至少 2 个文件链接）<br>段落均长 31.4 < 35 | 补体裁必需的结构件，或改标注为正确体裁；把碎片句并为完整论证段，或反过来拆分超长段 |
| ch01-tam-origin-evolution.md | Explanation | 6174 | 具象密度 0.34 < 1.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch04-ai-era-tam-redefined.md | Explanation | 6424 | 具象密度 0.16 < 1.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch07-business-insight.md | Explanation | 5861 | 具象密度 0.18 < 1.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch10-relationship-management-practical.md | How-to | 4168 | 具象密度 2.74 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch11-service-governance.md | Explanation | 5296 | 段落均长 42.4 < 45<br>具象密度 0.2 < 1.0 | 把碎片句并为完整论证段，或反过来拆分超长段；补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch12-service-governance-practical.md | How-to | 3868 | 具象密度 1.34 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch14-risk-compliance-practical.md | How-to | 5050 | 具象密度 0.41 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch15-project-change.md | Explanation | 4032 | 回顾占比 0.071 > 0.07 | 压缩要点回顾 |
| ch16-project-change-practical.md | How-to | 5542 | 具象密度 0.19 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch17-customer-lifecycle.md | How-to | 4757 | 失效边界词 2 < 3 | 补失效条件：什么情况下这条主张不成立 |
| ch19-internal-collaboration.md | How-to | 4865 | 具象密度 0.21 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch22-financial-industry.md | Explanation | 4354 | 具象密度 0.72 < 1.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch23-financial-availability.md | How-to | 3766 | 具象密度 1.68 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch24-major-assurance.md | How-to | 5598 | 具象密度 2.61 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch27-ai-workload-assurance.md | How-to | 5561 | 具象密度 0.38 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch28-ai-for-tam.md | How-to | 3553 | 具象密度 0.59 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch29-tam-copilot-tutorial.md | Tutorial | 4871 | 具象密度 1.85 < 3.0<br>n-gram 重复 0.139 > 0.12 | 补带来源的真实数字与时限；确实无量化对象则注明原因；同构段改写：合并重复句式，换论证角度 |
| ch30-service-model-evolution.md | Explanation | 4630 | 论证密度 0.237 < 0.28<br>段落均长 43.8 < 45 | 补机制解释：每节至少回答一次“为什么会这样”；把碎片句并为完整论证段，或反过来拆分超长段 |
| ch32-ai-risk-governance-howto.md | How-to | 3827 | 清单化率 0.897 > 0.8<br>具象密度 0.28 < 3.0 | 把清单条目展开成论证段；补带来源的真实数字与时限；确实无量化对象则注明原因 |
| ch37-career-team-building.md | Explanation | 3493 | 清单化率 0.45 > 0.35 | 把清单条目展开成论证段 |
| ch38-career-team-building-howto.md | How-to | 2132 | 段落均长 23.2 < 28 | 把碎片句并为完整论证段，或反过来拆分超长段 |

## 三、达标线（可调，但调阈须重跑 --calibrate 并记入 HANDOFF）

### Explanation

| 指标 | 达标线 | 方向 |
|---|---|---|
| 论证密度 | 0.28 | >= |
| 段落均长 | 45 | >= |
| 清单化率 | 0.35 | <= |
| 具象密度 | 1.0 | >= |
| 失效边界词 | 6 | >= |
| 回顾占比 | 0.07 | <= |

### How-to

| 指标 | 达标线 | 方向 |
|---|---|---|
| 段落均长 | 28 | >= |
| 清单化率 | 0.8 | <= |
| 具象密度 | 3.0 | >= |
| 失效边界词 | 3 | >= |
| 表格密度 | 32 | <= |

### Reference

| 指标 | 达标线 | 方向 |
|---|---|---|
| 段落均长 | 35 | >= |
| 清单化率 | 0.65 | <= |
| 具象密度 | 2.5 | >= |
| 表格密度 | 30 | <= |

### Tutorial

| 指标 | 达标线 | 方向 |
|---|---|---|
| 段落均长 | 25 | >= |
| 具象密度 | 3.0 | >= |
| 失效边界词 | 5 | >= |

### 通用

| 指标 | 达标线 | 方向 |
|---|---|---|
| n-gram 重复 | 0.12 | <= |

