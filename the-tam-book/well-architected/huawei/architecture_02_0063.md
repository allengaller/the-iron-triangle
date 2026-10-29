<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0063.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 概述

当应用系统部署在云中，虽然云具有一定的高可用和故障自动恢复能力，但对外仍会导致短时间的故障，需要应用系统能针对这种短时间故障进行适配处理，主要是采用重试机制。

云中故障需要重试的典型场景有：

1. 实例主备切换时可能会导致连接中断，如DCS、RDS实例由于某些原因主备切换时，会导致连接中断，需要客户端重试。
2. 实例由于故障重启可能会导致通信中断，如ECS所在物理服务器由于硬件原因故障时，ECS重启或在其他物理服务器中自动恢复，恢复过程中与ECS的通信会中断，需要重试。
3. 实例由于过载导致无法及时响应，需要重试。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0063.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
