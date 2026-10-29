<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0035.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES04-03 容灾恢复过程自动化

由于容灾恢复场景涉及容灾站点的业务恢复、数据库的主备切换、业务到容灾站点的流量切换等，恢复过程比较复杂，因此需要提供容灾管理功能，实现容灾状态及RPO监控，以及灾难场景下的一键式自动切换，减少人工干预。

- **风险等级** 高

- **关键策略** 实时监控容灾状态，了解容灾运行状态。 支持应用级数据校验，比较AZ间数据同步差异，监控RPO指标。 灾难场景下的一键式自动切换，减少人工干预，满足RPO/RTO指标。 支持容灾恢复流程编排、容灾演练等功能。
- **相关云服务和工具** 多活高可用服务 MAS

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0035.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
