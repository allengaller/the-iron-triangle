<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0134.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 可靠性功能

#### 集群HA

ELB采用集群化部署，支持多可用区的同城多活容灾，无缝实时切换。

#### 后端服务器健康检查

ELB弹性负载均衡支持定期向后端服务器发送请求以测试其运行状态。当判断后端服务器健康检查异常后，就不会将流量分发到异常后端服务器，而是分发到健康检查正常的后端服务器，从而提高了业务的可靠性。当异常的后端服务器恢复正常运行后，负载均衡器会将其自动恢复到负载均衡服务中，承载业务流量。

详见“[健康检查介绍](https://support.huaweicloud.com/intl/zh-cn/usermanual-elb/elb_ug_hc_0001.html)”。

#### 跨AZ容灾

ELB采用集群化部署，支持多可用区的同城多活容灾，无缝实时切换。

ELB支持后端服务器多AZ部署，当某个AZ出现故障时，ELB仍可将流量转发到其他AZ的后端ECS处理，提高应用系统容灾能力。

#### 监控告警

配合CES服务，支持对ELB的连接数、带宽、错误响应等进行监控和告警。

详见“[监控指标说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-elb/elb_ug_jk_0001.html)”。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0134.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
