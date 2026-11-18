<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0061.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES08-03 减少被依赖项故障的影响

被依赖项自身的可用性需要增强，以减少对依赖它的组件的影响。

- **风险等级** 中
- **关键策略** 对于被依赖项本身，为减少由于服务故障或运行缓慢对依赖它的组件的影响，需要考虑使用以下技术和原则： 减少被依赖项本身的外部依赖。 优化性能，减少消息响应时延和负载。 使用优先队列，优先处理高优先级用户的请求，以便在流量过载时不影响应用系统的核心功能。 流量过载时支持功能逐步降级。 被依赖项本身的功能受损时，提供缺省处理，以便应用系统仍可继续正常运行；由于缺省处理可能与实际配置有差异，此时需要告警以便通知系统管理员解决问题。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0061.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
