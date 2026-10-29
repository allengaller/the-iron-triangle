<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0153.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 常见故障模式

#### OBS桶流量过载

- 检测：通过CES监控请求数、请求成功率、上传/下载带宽等流量指标。

- 恢复： 应用层调整批量业务，避免业务高峰期进行备份等业务； 应用层进行重试，以应对暂时性故障，如网络拥塞；应用故障重试处理可参考“[故障重试](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0062.html)”。 应用层进行过载保护，保障优先业务的运行。

#### OBS对象上传/下载失败

- 检测：对象上传/下载失败。

- 恢复： 应用层进行重试，以应对暂时性故障，如网络拥塞；应用故障重试处理可参考“[故障重试](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0062.html)”。 当OBS桶由于过载导致网络限制时，可参考“OBS桶流量过载”的处理。

#### OBS桶内数据被误删

- 检测：NA

- 恢复：针对OBS桶启用多版本控制，在数据被删除时使用历史版本快速恢复。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0153.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
