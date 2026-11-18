<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0144.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 常见故障模式

#### CPU /内存/磁盘/带宽使用率过高

- 检测：通过CES监控CPU /内存/磁盘/带宽使用率。

- 恢复： 当CPU/内存使用高时，可根据业务情况，手工修改代理规格或增加代理数量以扩展资源。 当磁盘使用率高时，可根据业务情况，修改实例存储空间支持更大存储空间。 当带宽使用率高时，可根据业务情况，变更规格以支持更大带宽。 应用层进行过载保护，保障优先业务的运行。

#### 生产消息失败

- 检测：生产消息失败

- 恢复： 应用层进行重试，以应对暂时性故障；应用故障重试处理可参考“[故障重试](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0062.html)”。 当多次重试后仍无法写入成功，可将数据写入本地缓存，待服务可用后再写入实例。 当实例由于过载导致网络限制时，可参考“CPU /内存/带宽使用率过高”的处理。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0144.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
