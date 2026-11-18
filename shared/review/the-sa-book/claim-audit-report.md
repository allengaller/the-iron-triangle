# 数值断言出处审计（the-sa-book）

> 生成方式：`python3 shared/tooling/claim_audit.py --report --book sa`（可复跑，勿手改）
> 口径见本脚本头部注释与 `QUALITY-GATE.md` 第十节。

样本 34 个文件｜高风险数值断言 4 条｜无口径块 3 个｜涉及 3 个文件

## 一、按文件（块数降序）

| 文件 | 无口径块 |
|---|---|
| ch05-practical.md | 1 |
| ch05-technical-breadth.md | 1 |
| ch19-financial-solution-design.md | 1 |

## 二、明细（前 80 条）

| 文件:行 | 断言 | 原文片段 |
|---|---|---|
| ch05-practical.md:58 | 2 分钟内 | 2 分钟内出量级。偏差一个数量级内可接受。量级错了才是事故。 |
| ch05-technical-breadth.md:66 | 20% | 售前阶段精算是伪专业。量级错了才致命。差 20% 没人在意。 |
| ch19-financial-solution-design.md:37 | 99.99% | - 档位拍脑袋。99.99% 与 99.9% 的成本差一倍。 - 形态超配。管理类系统配 |
