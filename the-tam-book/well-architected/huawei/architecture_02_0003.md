<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0003.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 概念表

| 概念 | 解释 |
| --- | --- |
| 韧性 (Resilience) | 系统从故障中保持在已知运行状态（甚至降级）的能力。在遭遇故障后快速恢复核心功能和数据，且在业务需要的时间窗内恢复到有效运行状态。 |
| 可靠性 (Reliability) | 产品在规定的条件下和规定的时间内完成规定功能的能力。它的概率度量称为可靠度。 |
| 可用性 (Availability) | 产品在任意随机时刻需要和开始执行任务时，处于可工作或可使用状态的程度。它的概率度量称为可用度 |
| 云服务指标 SLI | Service level Indicator，面向服务的指标，如：请求响应成功率 |
| 云服务目标 SLO | Service Level Object，面向服务的目标，如：一定时间范围内的请求响应成功率大于XX%，或正常运行时间的百分比 |
| 云服务协议等级 SLA | Service Level Agreement，面向用户的协议等级，涉及不满足时的补偿 |
| 数据恢复点目标 RPO | Recovery Point Objective，主要指的是业务系统所能容忍的数据丢失量 |
| 恢复时间目标 RTO | Recovery Time Objective，主要指的是所能容忍的业务停止服务的最长时间，也就是从灾难发生到业务系统恢复服务功能所需要的最短时间周期。 |

业界对韧性没有统一的定义。狭义韧性，指的是自动或快速从故障中恢复运行的能力；而广义韧性，除了从故障中恢复运行的能力外，还包括故障容忍能力。

故障容忍（[fault tolerance](https://en.wikipedia.org/wiki/Fault_tolerance)，简称“容错”），是使系统在其某些组件中出现一个或多个故障时能够继续提供服务的能力，从客户的角度来看，该服务仍能完全正常运行，或可能降级运行。

而可靠性同样分为狭义可靠性与广义可靠性。狭义可靠性工程的目标是提高系统无故障运行的能力，即提高可靠性。而广义可靠性工程的目标除了提高可靠性外，还包括提高从故障中恢复运行能力，即维修性（maintainability），同时还包括其他围绕故障展开的各种能力，如可用性（availability）、保障性（supportability）等。

因此，从广义韧性与广义可靠性的定义来看，并没有显著区别。只是可靠性和韧性的侧重点不同。可靠性工程的目标是尽可能减少系统中的故障，保证系统无故障运行。而韧性工程，接受故障总会发生的现实，关注的是如何降低故障带来的损失以及如何从故障中恢复。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0003.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
