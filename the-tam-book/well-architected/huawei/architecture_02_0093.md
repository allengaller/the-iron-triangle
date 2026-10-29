<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0093.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES13-04 支持主动扩容

当由于计划性活动而导致资源需求增加时，需要支持主动扩容，避免由于资源不足而导致业务受影响。

- **风险等级** 高
- **关键策略** 当发现应用系统业务需要更多资源时，可主动扩展资源以满足需求，而避免影响可用性。典型场景如产品促销前预测会有突发大流量，则可手工进行扩容处理。 华为云服务实例支持主动横向或纵向扩容功能；如对于ECS实例可以通过创建多个ECS实例实现横向扩容，也可升级ECS规格实现纵向扩容；对于RDS实例可升级RDS实例规格实现纵向扩容。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0093.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
