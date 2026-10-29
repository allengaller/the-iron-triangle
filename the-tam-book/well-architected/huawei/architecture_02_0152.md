<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0152.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 可靠性功能

#### 数据持久性

OBS通过存储介质的慢盘/坏道检测、AZ内设备和数据冗余、AZ之间数据容灾、跨区域复制等技术方案，提供针对介质、服务器、机柜、数据中心和区域的多级可靠性保障。其数据持久性高达99.9999999999%（12个9），可用性高达99.995%，远高于传统架构。

详见“[OBS的持久性和可用性如何?](https://support.huaweicloud.com/intl/zh-cn/obs_faq/obs_faq_0058.html)”。

#### 数据备份和恢复

OBS支持多版本控制，可以在一个桶中保留多个版本的对象，以便方便地检索和还原各个版本，在意外操作或应用程序故障时快速恢复数据。

#### 跨AZ容灾

在创建桶时，数据冗余存储策略可选择多AZ存储，数据将冗余存储至多个AZ中，可靠性更高。

#### 跨Region容灾

OBS支持跨区域复制，能够为用户提供跨区域数据容灾的能力，满足用户数据复制到异地进行备份的需求。

#### 监控告警

配合CES服务，支持对OBS桶的请求、流量、时延和错误响应等进行监控和告警。

详见“[监控对象存储服务](https://support.huaweicloud.com/intl/zh-cn/usermanual-obs/obs_03_0009.html)”。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0152.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
