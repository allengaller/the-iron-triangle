<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0041.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES05-03 不同流量模型业务的网络共享带宽隔离

不同流量模型业务共享网络带宽时，可能会导致流量抢占，相互影响，一个业务流量突然可能会导致其他业务不可用。

- **风险等级** 高
- **关键策略** 相同流量模型的业务，可共享网络带宽，带宽需要满足所有共享业务的需求 不同流量模型的业务，为了避免相互干扰，建议使用各自独立的共享带宽实例 不同特性的业务，建议使用各自独立的域名隔离。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0041.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
