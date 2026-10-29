<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0018.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES01-02 应用组件多位置部署

应用组件需要部署在多个数据中心，以避免单个数据中心故障而导致业务中断。

- **风险等级** 高

- **关键策略** 可根据不同需求，将应用的数据和资源部署在多个位置： 应用多AZ部署：应用应尽可能部署在多个可用区，避免由于单个可用区故障而导致所有业务中断。 应用多Region部署：对于可用性要求高的应用系统，需要考虑多Region部署，避免由于单个Region故障而导致所有业务中断。 在多AZ部署能满足需求的情况下，应优先使用多AZ部署。大多数工作负载的可用性目标都可通过在单个Region内多 AZ 部署来实现，只有工作负载具有极高的可用性要求或者其他业务目标时，才考虑多Region架构。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0018.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
