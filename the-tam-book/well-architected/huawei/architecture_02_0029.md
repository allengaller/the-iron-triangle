<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0029.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES03-03 对接容灾仲裁，支持自动切换

针对有状态的主备类型业务，在跨AZ部署并支持自动切换时，需要对接容灾仲裁，以避免出现双主或双备，从而在AZ间链路中断的情况下，业务能自动切换到一个AZ提供服务而不受影响；对于集群类业务不涉及。

- **风险等级** 高

- **关键策略** 面向有状态主备类型业务提供容灾仲裁，站点间链路中断不双主，不破坏数据完整性。 应用内所有相关组件对接一致性仲裁，在链路中断的情况下所有组件均能切换到同一个站点，实现端到端的业务可用性

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0029.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
