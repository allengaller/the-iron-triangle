<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0126.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 常见故障模式

#### ECS的CPU /内存/磁盘容量/磁盘IOPS使用率过高

- 检测：通过CES监控CPU/内存/磁盘容量/磁盘IOPS使用率。
- 恢复： 根据业务情况，手工变更规格以扩展资源或增加ECS实例进行负荷分担。 对于无状态业务，启动AS弹性伸缩，自动扩展资源。 应用层进行过载保护，保障优先业务的运行。

#### 连接后端ECS失败

- 检测：网络连接失败。
- 恢复： 至少部署2个后端ECS。对于无状态业务，配置ELB弹性负载均衡保障业务可靠性；对于有状态业务，由应用层实现多实例高可用。 应用层进行重试，以应对暂时性故障，如ECS正在进行故障恢复时。应用故障重试处理可参考“[故障重试](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0062.html)”。 当ECS由于过载导致网络限制时，可参考“ECS的CPU /内存/磁盘容量/磁盘IOPS使用率过高”的处理。

#### ECS实例不可用或运行异常

- 检测：配置ELB弹性负载均衡器的后端服务器健康检查，以便定期检查后端服务器的运行状态。健康检查应检查关键功能是否能正确响应。
- 恢复：针对每个应用层，配置多个ECS实例，通过ELB弹性负载均衡器进行健康检查，当检测到某个ECS实例不可用时，ELB弹性负载均衡器停止向该实例发送业务请求。

#### ECS实例或挂载的磁盘或数据被意外删除

- 检测：NA
- 恢复：对于无状态业务，使用模板快速发放新实例；对于有状态业务，使用CBR云备份服务对ECS进行定期备份，在数据被删除时使用备份数据快速恢复。

#### ECS实例使用本地盘时本地盘故障

- 检测：应用层检测本地盘运行状态。
- 恢复：应用层采用RAID实现ECS内硬盘高可用，并实现跨ECS的数据复制与高可用，以便在本地盘故障时业务可快速恢复。建议非必须使用本地盘场景，尽可能使用EVS云硬盘，以提升硬盘的可靠性。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0126.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
