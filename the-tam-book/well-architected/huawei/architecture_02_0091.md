<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0091.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES13-02 应用系统负载均衡，避免流量不均匀

针对无状态集群业务，通过负载均衡来保证业务均匀分发，可避免部分组件空闲，而部分组件过载而影响业务；同时还可以充分利用系统资源，提高系统性能，改善系统可靠性。

- **风险等级** 高
- **关键策略** 负载均衡分发业务粒度需避免过大，而导致部分组件过载。 负载均衡分发时需检查后端节点的负载状态，并根据各节点的负载进行业务分发。 在后端节点故障的情况下，需要自动将业务分发给其他健康节点处理，以避免业务失败。
- **相关云服务和工具** 弹性负载均衡 ELB：支持业务负载均衡处理，还支持后端服务器健康状态检测，自动隔离异常状态的ECS。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0091.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
