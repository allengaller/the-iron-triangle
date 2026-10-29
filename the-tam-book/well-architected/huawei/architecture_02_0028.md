<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0028.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES03-02 跨AZ数据同步

针对有状态业务，需要进行跨AZ的数据同步，以便在一个AZ故障的情况下，数据不丢失；对于无状态业务不涉及。

- **风险等级** 高

- **关键策略** 当应用组件对应的云服务实例支持跨AZ高可用实例时，可采用云服务实例自身的跨AZ数据同步；如RDS数据库、DCS实例、OBS桶等。 当应用组件对应的云服务实例不支持跨AZ高可用实例，但提供了同步服务进行跨AZ数据同步时，可利用该服务进行跨AZ数据同步；如存在有状态数据的ECS实例不支持跨AZ高可用，但可通过SDRS服务进行跨AZ数据同步。 当应用组件对应的云服务实例不支持跨AZ高可用实例，且不支持跨AZ数据同步或不使用跨AZ数据同步服务时，则需要由应用层进行数据复制；如存在有状态数据的BMS实例。
- **相关云服务和工具** 存储容灾服务 SDRS 弹性云服务器 ECS 云数据库 RDS 分布式缓存服务 DCS 对象存储服务 OBS

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0028.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
