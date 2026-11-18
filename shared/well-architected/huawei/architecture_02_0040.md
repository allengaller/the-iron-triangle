<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0040.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES05-02 避免暴露不必要的网络地址

网络地址对外暴露时，可能会引入安全风险，需要避免暴露不必要的网络地址。

- **风险等级** 高
- **关键策略** 通常对外网络地址需要尽可能集中管控，避免分散暴露，如使用网络服务ELB弹性负载均衡、公网NAT网关、Web云防火墙等作为公网访问入口。 对外的IP地址需要通过安全组、NAT等限制网络端口访问，减少安全风险。
- **相关云服务和工具** 虚拟私有云VPC：安全组 弹性负载均衡器 ELB NAT网关 NAT Web云防火墙 WAF

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0040.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
