<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0030.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES03-04 支持容灾管理

提供容灾管理功能，实现容灾状态及RPO监控，及异常场景下的业务切换。

- **风险等级** 高
- **关键策略** 实时监控容灾状态，了解容灾运行状态。 支持应用级数据校验，比较AZ间数据同步差异，监控RPO指标。 典型确定性故障场景下自动容灾或切换，无需人工接入，业务不受影响，满足RPO/RTO指标。 典型亚健康故障场景，支持业务降级或主动切换，业务不持续受损。
- **相关云服务和工具** 多活高可用服务 MAS

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0030.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
