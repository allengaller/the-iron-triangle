# 内容质量门禁报告

> 生成方式：`python3 scripts/content_gate.py --report`（可复跑，勿手改）
> 口径与盲区见 `QUALITY-GATE.md`；本节报告只举证，不代替人工通读。

样本 71 个文件｜block 0｜warn 47｜通过 24

## 一、block：体裁矛盾与结构破损（当期必修）

无。

## 二、warn：内容厚度（进整改台账，不阻断发布）

| 文件 | 类型 | 中文字 | 差距 | 整改方向 |
|---|---|---|---|---|
| manuscript/appx-a-glossary.md | Reference | 3309 | 骨架 缺：交叉引用（至少 2 个文件链接）<br>表格密度 39.58 > 30 | 补体裁必需的结构件，或改标注为正确体裁；表格过多，改为正文论证，只留真正需要对照的表 |
| manuscript/appx-aa-tam-reporting-standard.md | Reference | 8547 | 骨架 缺：交叉引用（至少 2 个文件链接） | 补体裁必需的结构件，或改标注为正确体裁 |
| manuscript/appx-ab-subtam-domain-collaboration.md | Reference | 7099 | 骨架 缺：交叉引用（至少 2 个文件链接）<br>具象密度 2.03 < 2.5 | 补体裁必需的结构件，或改标注为正确体裁；补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/appx-ac-sre-cre-engineering-depth.md | How-to | 2023 | 清单化率 0.817 > 0.8<br>具象密度 1.58 < 3.0 | 把清单条目展开成论证段；补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/appx-ad-career-lifecycle-guide.md | How-to | 3944 | 失效边界词 1 < 3 | 补失效条件：什么情况下这条主张不成立 |
| manuscript/appx-b-tam-process-system.md | Reference | 5282 | 段落均长 32.3 < 35<br>清单化率 0.785 > 0.65 | 把碎片句并为完整论证段，或反过来拆分超长段；把清单条目展开成论证段 |
| manuscript/appx-c-methodology-mapping.md | Reference | 1764 | 具象密度 2.48 < 2.5<br>表格密度 38.41 > 30 | 补带来源的真实数字与时限；确实无量化对象则注明原因；表格过多，改为正文论证，只留真正需要对照的表 |
| manuscript/appx-d-further-reading.md | Reference | 1361 | 表格密度 36.72 > 30 | 表格过多，改为正文论证，只留真正需要对照的表 |
| manuscript/appx-e-contribution-guide.md | How-to | 1956 | 具象密度 0.0 < 3.0<br>失效边界词 1 < 3 | 补带来源的真实数字与时限；确实无量化对象则注明原因；补失效条件：什么情况下这条主张不成立 |
| manuscript/appx-g-tam-work-evaluation-standard.md | Reference | 3892 | 骨架 缺：交叉引用（至少 2 个文件链接） | 补体裁必需的结构件，或改标注为正确体裁 |
| manuscript/appx-h-tool-platform-acceptance-standard.md | Reference | 2546 | 骨架 缺：交叉引用（至少 2 个文件链接） | 补体裁必需的结构件，或改标注为正确体裁 |
| manuscript/appx-l-project-onboarding-standard.md | Reference | 3700 | n-gram 重复 0.132 > 0.12 | 同构段改写：合并重复句式，换论证角度 |
| manuscript/appx-r-problem-retrospective-standard.md | Reference | 4669 | 骨架 缺：交叉引用（至少 2 个文件链接）<br>清单化率 0.706 > 0.65 | 补体裁必需的结构件，或改标注为正确体裁；把清单条目展开成论证段 |
| manuscript/appx-t-online-change-standard.md | Reference | 5679 | n-gram 重复 0.133 > 0.12 | 同构段改写：合并重复句式，换论证角度 |
| manuscript/appx-u-ticket-management-standard.md | Reference | 4166 | 骨架 缺：交叉引用（至少 2 个文件链接） | 补体裁必需的结构件，或改标注为正确体裁 |
| manuscript/appx-v-tam-bte-sa-triangle.md | Reference | 4636 | 清单化率 0.707 > 0.65 | 把清单条目展开成论证段 |
| manuscript/appx-y-training-tutorial.md | Tutorial | 5902 | 段落均长 24.0 < 25<br>n-gram 重复 0.169 > 0.12 | 把碎片句并为完整论证段，或反过来拆分超长段；同构段改写：合并重复句式，换论证角度 |
| manuscript/appx-z-well-architected-framework.md | Reference | 11912 | 骨架 缺：交叉引用（至少 2 个文件链接）<br>段落均长 31.4 < 35 | 补体裁必需的结构件，或改标注为正确体裁；把碎片句并为完整论证段，或反过来拆分超长段 |
| manuscript/ch01-tam-origin-evolution.md | Explanation | 5978 | 具象密度 0.35 < 1.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch02-role-boundary-map.md | Reference | 6106 | 具象密度 0.0 < 2.5 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch03-value-proposition.md | Explanation | 6711 | 具象密度 0.0 < 1.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch04-ai-era-tam-redefined.md | Explanation | 6424 | 具象密度 0.16 < 1.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch05-technical-depth.md | Explanation | 6066 | 具象密度 0.0 < 1.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch07-business-insight.md | Explanation | 5861 | 具象密度 0.18 < 1.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch09-relationship-management.md | Explanation | 5510 | 具象密度 0.0 < 1.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch10-relationship-management-practical.md | How-to | 3862 | 具象密度 2.97 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch11-service-governance.md | Explanation | 5296 | 段落均长 42.4 < 45<br>具象密度 0.2 < 1.0 | 把碎片句并为完整论证段，或反过来拆分超长段；补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch12-service-governance-practical.md | How-to | 3744 | 具象密度 1.39 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch13-risk-compliance.md | Explanation | 3071 | 具象密度 0.72 < 1.0<br>回顾占比 0.097 > 0.07 | 补带来源的真实数字与时限；确实无量化对象则注明原因；压缩要点回顾 |
| manuscript/ch14-risk-compliance-practical.md | How-to | 5050 | 具象密度 0.41 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch15-project-change.md | Explanation | 2838 | 具象密度 0.0 < 1.0<br>回顾占比 0.1 > 0.07 | 补带来源的真实数字与时限；确实无量化对象则注明原因；压缩要点回顾 |
| manuscript/ch16-project-change-practical.md | How-to | 5183 | 具象密度 0.21 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch17-customer-lifecycle.md | How-to | 4396 | 失效边界词 1 < 3 | 补失效条件：什么情况下这条主张不成立 |
| manuscript/ch19-internal-collaboration.md | How-to | 4542 | 具象密度 0.23 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch20-partner-ecosystem.md | How-to | 3727 | 具象密度 0.0 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch22-financial-industry.md | Explanation | 4354 | 具象密度 0.72 < 1.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch23-financial-availability.md | How-to | 3766 | 具象密度 1.68 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch24-major-assurance.md | How-to | 5560 | 具象密度 2.63 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch25-financial-incident.md | How-to | 3835 | 清单化率 0.808 > 0.8<br>具象密度 2.74 < 3.0 | 把清单条目展开成论证段；补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch27-ai-workload-assurance.md | How-to | 5561 | 具象密度 0.38 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch28-ai-for-tam.md | How-to | 3553 | 具象密度 0.59 < 3.0 | 补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch29-tam-copilot-tutorial.md | Tutorial | 4825 | 具象密度 1.87 < 3.0<br>n-gram 重复 0.136 > 0.12 | 补带来源的真实数字与时限；确实无量化对象则注明原因；同构段改写：合并重复句式，换论证角度 |
| manuscript/ch30-service-model-evolution.md | Explanation | 4604 | 论证密度 0.227 < 0.28<br>段落均长 44.1 < 45 | 补机制解释：每节至少回答一次“为什么会这样”；把碎片句并为完整论证段，或反过来拆分超长段 |
| manuscript/ch32-ai-risk-governance-howto.md | How-to | 3790 | 清单化率 0.907 > 0.8<br>具象密度 0.28 < 3.0 | 把清单条目展开成论证段；补带来源的真实数字与时限；确实无量化对象则注明原因 |
| manuscript/ch35-measurement-system-howto.md | How-to | 2306 | 段落均长 24.4 < 28 | 把碎片句并为完整论证段，或反过来拆分超长段 |
| manuscript/ch37-career-team-building.md | Explanation | 3493 | 清单化率 0.45 > 0.35 | 把清单条目展开成论证段 |
| manuscript/ch38-career-team-building-howto.md | How-to | 2132 | 段落均长 23.2 < 28 | 把碎片句并为完整论证段，或反过来拆分超长段 |

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

