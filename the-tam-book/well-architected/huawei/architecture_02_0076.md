<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0076.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES11-02 压力负载测试

通过施加超出系统容量的业务压力，验证云服务的过载保护、业务隔离和优雅降级等能力。为全面验证系统整体的容量规划和业务依赖，云服务应用通常采用全链路压测进行测试。

- **风险等级** 高
- **关键策略** 模拟大量接口消息进行压力测试。 模拟各种业务场景进行压力测试。 持续自动测试。 性能发生偏差时自动告警，以便及时定位和处理。
- **相关云服务和工具** 性能测试 CodeArts PerfTest：针对HTTP/HTTPS/TCP/UDP/HLS/RTMP/ WEBSOCKET/HTTP-FLV等协议构建的云应用提供性能测试的服务，其支持快速模拟大规模并发用户的业务高峰场景，通过自定义报文内容、时序、多事务组合等复杂场景，帮助用户测试验证业务高峰下的服务表现。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0076.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
