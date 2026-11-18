<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0069.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES10-01 应用控制平面与数据平面隔离

通常应用的数据平面处理业务，比较重要，可用性要求比较高，而控制平面不直接处理业务，因此其故障时不应该影响业务系统。

- **风险等级** 高
- **关键策略** 应用控制平面与数据平面隔离，避免控制系统故障影响业务。 数据平面所在业务系统的故障恢复可不依赖控制平面，避免由于控制平面故障而导致业务系统无法恢复。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0069.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
