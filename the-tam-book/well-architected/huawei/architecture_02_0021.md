<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0021.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 概述

对于应用系统中的重要数据，需要提供备份功能，以便在病毒入侵、人为误删除、软硬件故障等场景，能够快速将数据恢复到备份点。

由于容灾通常对数据采用实时复制且没有多备份点，在主数据被误删或误改的情况下，错误数据会同步到备端，从而无法达到数据备份的效果，因此通常不能使用容灾来代替备份。

备份恢复时的RPO指标（即数据丢失量），与最近一个备份时间点相关；不同类型的数据，允许丢失数据量可以不同，即RPO不同；为了保证数据备份的RPO目标，需要采用定期自动备份，而不要依赖人工进行手工备份。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0021.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
