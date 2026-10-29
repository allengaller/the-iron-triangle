<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0141.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 常见故障模式

#### DCS的CPU /内存/带宽/连接数使用率过高

- 检测：通过CES监控CPU /内存/带宽/连接数使用率。

- 恢复： 根据业务情况，手工变更规格以扩展资源。 应用层进行过载保护，保障优先业务的运行，如将部分性能要求不高的业务切回到原始数据源。

#### 连接后端DCS失败

- 检测：连接失败。

- 恢复： 应用层进行重试，以应对暂时性故障，如DCS实例正在进行主备切换时；应用故障重试处理可参考“[故障重试](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0062.html)”。 当DCS实例由于过载导致网络限制时，可参考“DCS的CPU /内存/带宽/数据库连接数使用率过高”的处理。 对于非暂行性故障，应用层需要能回退到原始数据源进行处理，避免由于缓存故障而导致业务无法运行。

#### 读写DCS概率性失败

- 检测：读写失败。针对低概率超时错误，是Redis使用的正常现象。Redis使用受到网络传输、客户端设置超时时间等因素影响，可能出现单个请求超时问题。

- 恢复： 应用层进行重试，以应对暂时性故障，如DCS实例正在进行主备切换时；应用故障重试处理可参考“[故障重试](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0062.html)”。 当DCS实例由于过载导致网络限制时，可参考“DCS的CPU /内存/带宽/数据库连接数使用率过高”的处理。 对于非暂行性故障，应用层需要能回退到原始数据源进行处理，避免由于缓存故障而导致业务无法运行。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0141.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
