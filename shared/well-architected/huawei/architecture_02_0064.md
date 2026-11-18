<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0064.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES09-01 API及命令调用需要设计为可重试

在进行重试处理时，API及命令调用会重复发送，服务方会多次重复执行，需要保证重复执行多次的结果不变。

- **风险等级** 高
- **关键策略** 应用系统在设计时，应使操作具有幂等性，也就是允许一个操作连续执行两次或多次时，应该与单次调用产生的结果相同，从而保证重试安全；若不支持操作的幂等性，会导致客户端难以重试或重试的处理更复杂。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0064.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
