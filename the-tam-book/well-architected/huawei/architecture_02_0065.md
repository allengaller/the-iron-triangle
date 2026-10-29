<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0065.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES09-02 客户端需要根据综合评估是否要重试

当客户端请求超时或收到错误响应时，客户端需要决定是否重试；重试有助于客户端在请求失败时，通过重复消息来获得预期的结果，避免业务失败，但也会消耗更多的服务器时间来获取所需的成功响应。

- **风险等级** 高
- **关键策略** 请求超时，可能是链路闪断或其他临时性故障导致消息丢失，可以进行重试。 根据错误响应码进行有针对性的重试；对于临时性故障，如错误码指示为系统繁忙时，可等待一段时间后重试，否则无需重试。 请求SDK中内置了消息重试时，客户端无需重复重试。 多层业务栈一般只在源端重试，避免逐层重试。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0065.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
