<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0128.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 可靠性功能

#### 数据备份和恢复

使用CBR云备份服务可对BMS的所有云硬盘（系统盘和数据盘）进行备份，支持基于多云硬盘一致性快照技术的备份服务，并支持利用备份数据恢复裸金属服务器数据，最大限度保障用户数据的安全性和正确性，确保业务安全。

详见“[备份裸金属服务器](https://support.huaweicloud.com/intl/zh-cn/usermanual-bms/bms_01_0042.html)”。

#### 集群HA

配合共享云硬盘，可以构建AZ内集群或HA关键应用。一块共享云硬盘最多可同时挂载至16台BMS。并需要搭建共享文件系统或类似的集群管理系统，例如Windows MSCS集群、Veritas VCS集群和CFS集群等。

详见“[共享云硬盘及使用方法](https://support.huaweicloud.com/intl/zh-cn/productdesc-evs/zh-cn_topic_0032860759.html)”。

#### 负载均衡

配合弹性负载均衡ELB服务，可以实现多BMS实例的负载均衡。

#### 健康检查

通过弹性负载均衡ELB服务，可对BMS实例进行健康检查。

详见“[修改健康检查配置](https://support.huaweicloud.com/intl/zh-cn/usermanual-elb/elb_ug_hc_0005.html)”。

#### 跨AZ容灾

配合ELB服务，可以实现跨AZ的故障切换。

#### 监控告警

配合CES服务，支持对BMS的CPU、内存、磁盘、网络等进行监控和告警。

详见“[监控指标说明](https://support.huaweicloud.com/intl/zh-cn/ces_faq/ces_faq_2513.html)”。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0128.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
