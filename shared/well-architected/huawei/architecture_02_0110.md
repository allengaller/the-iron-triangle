<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0110.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 概述

本章节以典型Web应用为例，介绍不同可用性目标要求下部署的典型架构示例。针对每种场景，从以下几个维度进行设计，来达成可用性目标。

| 类别 | 应用可用性影响 |
| --- | --- |
| 冗余 | 应用内组件的高可用能力，在应用内部分节点故障时业务自动恢复能力 |
| 备份 | 应用数据被破坏的情况下的恢复能力 |
| 容灾 | 在Region/AZ/IDC或其他云站点发生灾难的情况下的恢复能力 |
| 监控告警 | 应用系统故障后的检测和告警能力 |
| 弹性扩缩容 | 应用容量不足时的自动恢复能力 |
| 变更防差错 | 变更对应用业务中断的影响 |
| 应急恢复处理 | 应用在故障情况下的应急恢复能力 |

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0110.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
