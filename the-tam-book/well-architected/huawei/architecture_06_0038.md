<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_06_0038.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# OPS06-06 实施分布式跟踪

Trace是一系列因果相关的分布式事件的表示，这些事件编码了流经分布式系统的端到端请求流。

- **风险等级** 高
- **关键策略** 当系统出现问题时，需要能够追踪系统中每个组件的行为和交互情况。通过在系统中实现分布式跟踪，可以快速定位问题并进行有效的故障排除。
- **设计建议** 链路跟踪可以通过在系统中添加跟踪标识符来实现。当请求进入系统时，标识符将被添加到请求中，并在整个系统中传递。每个组件都可以将标识符添加到它们的日志中，以便在出现问题时进行故障排除。分布式跟踪可以使用开源工具Jaeger、Zipkin、skywalking或CAT等,华为云APM提供了调用链观测能力。 可参考[定位请求异常原因](https://support.huaweicloud.com/intl/zh-cn/bestpractice-apm2/apm_08_0002.html)

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_06_0038.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
