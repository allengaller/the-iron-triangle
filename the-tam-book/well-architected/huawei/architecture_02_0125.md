<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0125.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 可靠性功能

#### 数据备份和恢复

使用CBR云备份服务可对ECS的备份保护服务，支持基于多云硬盘一致性快照技术的备份服务，并支持利用备份数据恢复ECS数据。

详见“[云备份概述](https://support.huaweicloud.com/intl/zh-cn/usermanual-ecs/ecs_03_1501.html)”。

#### 故障自愈

当ECS支持自动恢复时，可以开启自动恢复能力，当物理服务器损坏时以冷迁移方式重启ECS实例，使弹性云服务器具备高可靠性和强大的动态迁移能力。当弹性云服务器所在的硬件出现故障时，系统会自动将弹性云服务器迁移至正常的物理机，保障业务受到的影响最小，该过程会导致云服务器重启。

详见“[物理机故障时，弹性云服务器是否会自动恢复](https://support.huaweicloud.com/intl/zh-cn/ecs_faq/ecs_faq_0103.html)”。

当检测到弹性云服务所在的硬件出现亚健康时，系统会自动化将弹性云服务器热迁移到其他物理服务器上继续运行，迁移过程中会导致业务处理性能下降，业务中断时间小于1s。

#### 反亲和

通过云服务器组，支持创建ECS实例时尽量分散在不同主机上以提高业务的可靠性。

详见“[管理云服务器组](https://support.huaweicloud.com/intl/zh-cn/usermanual-ecs/ecs_03_0150.html)”。

#### 集群HA

配合共享云硬盘，可以构建AZ内集群或HA关键应用。一块共享云硬盘最多可同时挂载至16台ECS。并需要搭建共享文件系统或类似的集群管理系统，例如Windows MSCS集群、Veritas VCS集群和CFS集群等。

为确保业务可靠性，建议将共享云硬盘挂载至位于同一个反亲和性云服务器组内的ECS。

详见“[共享云硬盘及使用方法](https://support.huaweicloud.com/intl/zh-cn/productdesc-evs/zh-cn_topic_0032860759.html)”。

#### 负载均衡

配合弹性负载均衡ELB服务，可以实现多ECS实例的负载均衡。

#### 健康检查

通过弹性负载均衡ELB服务，可对ECS实例进行健康检查。

详见“[修改健康检查配置](https://support.huaweicloud.com/intl/zh-cn/usermanual-elb/elb_ug_hc_0005.html)”。

#### 弹性伸缩

配合动态伸缩AS服务，可以实现跨AZ的ECS实例重建或均衡。

#### 跨AZ容灾

配合ELB服务，可以实现跨AZ的故障切换。

#### 监控告警

配合CES服务，支持对ECS的CPU、内存、磁盘、网络等进行监控和告警。

详见“[监控弹性云服务器](https://support.huaweicloud.com/intl/zh-cn/usermanual-ecs/ecs_03_1001.html)”。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0125.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
