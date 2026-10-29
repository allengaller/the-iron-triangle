<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0089.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 概述

当系统流量超过一定阈值后，导致系统处于过载状态时，可能会导致部分请求失败，失败触发业务重试，会进一步增加系统的负荷，形成恶性循环，导致业务成功率远远低于系统的设计容量，甚至整体不可用。因此应用应该设计过载保护机制，使得在过载状态下依然可以保证一定比例设计容量的处理能力。

通过过载保护，可以缓解客户流量突增、泛洪攻击或重试风暴所造成的大量容量峰值情况，让工作负载能够继续正常处理支持的请求量，避免出现资源耗尽而导致所有请求都不能处理的情况。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0089.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
