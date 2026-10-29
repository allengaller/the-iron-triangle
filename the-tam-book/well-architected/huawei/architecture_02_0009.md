<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0009.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 数据持久度

数据持久度是指数据不丢失的概率，即存储在预计周期内不出现数据丢失的概率，可以用于度量一个存储系统的可靠性。其只表示数据是否丢失的概率，不体现数据丢失多少；数据持久度的预计周期，一般按一年进行预计。

影响存储数据持久度的主要因子有：冗余数、磁盘失效率与数据修复时间。其中每多一个冗余，数据持久度通常可增加2~3个9；云上常用的对象存储，一般采用3副本冗余，通常可提供11~12个9的数据持久度。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0009.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
