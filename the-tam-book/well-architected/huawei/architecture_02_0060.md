<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0060.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES08-02 依赖松耦合

系统内组件之间直接访问时，会产生紧耦合关系一个组件的状态变化会对其他组件产生直接影响，从而会导致所有组件的可用性均下降。而采用松耦合架构时，各个组件之间的依赖关系非常弱，它们可以独立地进行修改和扩展，而不影响其他组件；系统更加灵活，易于维护和升级，并且稳定性和可靠性也更强。

- **风险等级** 中
- **关键策略** 组件之间通过消息队列、消息缓存、负载均衡器等交互（即松耦合关系），可一定程度上屏蔽组件的状态变化，防止对其他组件造成影响
- **相关云服务和工具** 弹性负载均衡服务 ELB 分布式缓存服务 DCS 分布式消息服务Kafka版 分布式消息服务RabbitMQ版 分布式消息服务RocketMQ版 事件网格 EG

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0060.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
