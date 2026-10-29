<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0066.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES09-03 重试需要避免造成流量压力

对于链路闪断等原因导致的临时性故障，客户端进行一定的重试，可取得较好的效果；对于流量过载等原因导致的故障，重试可能会导致情况进一步恶化，因此需要避免这种影响。

- **风险等级** 高
- **关键策略** 客户端进行重试处理时，建议： 增加指数回退和抖动方法，以避免对服务端造成流量压力；采用指数回退重试时，每次重试之间的间隔会逐渐延长，并在两次重试之间引入抖动，以随机调整重试间隔，避免同时出现造成重试峰值。 限制最大重试次数或用时，避免由于消息积压而导致流量过载。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0066.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
