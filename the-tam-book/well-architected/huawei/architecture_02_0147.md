<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0147.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 常见故障模式

#### RDS的CPU /内存/磁盘容量/磁盘IOPS/数据库连接数使用率过高

- 检测：通过CES监控CPU /内存/磁盘容量/磁盘IOPS/数据库连接数使用率。

- 恢复： 根据业务情况，手工变更规格以扩展资源。 开启存储空间自动扩容，以便在磁盘容量不足时自动扩容。 应用层进行过载保护，保障优先业务的运行。

#### 连接后端RDS失败

- 检测：连接失败。

- 恢复： 应用层进行重试，以应对暂时性故障，如RDS实例正在进行主备切换时；应用故障重试处理可参考“[故障重试](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0062.html)”。 当RDS实例由于过载导致网络限制时，可参考“RDS的CPU /内存/磁盘容量/磁盘IOPS/数据库连接数使用率过高”的处理。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0147.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
