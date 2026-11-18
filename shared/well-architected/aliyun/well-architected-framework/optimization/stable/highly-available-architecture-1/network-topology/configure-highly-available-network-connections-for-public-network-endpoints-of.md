<!-- source: https://help.aliyun.com/zh/well-architected/configure-highly-available-network-connections-for-public-network-endpoints-of -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2938773 -->

# 为工作负载公网端点配置高可用的网络连接

在构建面向公网访问的业务系统时，确保用户能够稳定、安全、高效地访问工作负载的公共端点，是保障整体系统可用性的关键环节。为此，需使用高可用的 DNS服务、内容分发网络（CDN）、API Gateway、负载均衡与弹性后端服务。

## 优先级

高

## 不推荐做法

- 末规划高可用DNS与末使用高可用公网资源
- 直接使用实例IP地址而非域名访问
- 使用A记录而非CNAME访问ALB，直接使A记录，当后端该IP或其负载均衡异常时，流量无法自动重定向至健康实例。
- 负载均衡后端服务器单可用区部署，所有后端ECS均部署在同一个可用区，若该可用区发生网络中断或硬件故障，整个服务将不可用，导致单点故障。
- 未进行公网资源拆分，将高优先级业务与低优先级业务混合在同一公网资源池中，未进行带宽或IP地址的隔离，导致某一业务的突发流量占用全部资源，从而影响高优先级业务。

## 实施指南

1. 使用高可用DNS服务：**阿里云云解析 DNS** 提供高可用、可扩展的 DNS 服务，确保域名可解析，配置健康检测（Health Check），仅将流量引导至健康的端口。有关更多信息，请参阅[什么是云解析DNS](https://help.aliyun.com/zh/dns/product-introduction-dns2-0)
2. 阿里云全局流量管理GTM提供统一的入口IP，优化全球访问路径。支持基于地理位置、网络运营商、延迟等维度的智能调度。有关更多信息，请参阅[什么是全局流量管理3.0？](https://help.aliyun.com/zh/dns/what-is-gtm-version3)。
3. 使用阿里云内容分发网络（CDN）构建CDN，提升静态资源访问速度与可用性，利用边缘缓存减少源站压力，提高响应速度。有关更多信息，请参阅[什么是阿里云CDN](https://help.aliyun.com/zh/cdn/product-overview/what-is-alibaba-cloud-cdn)。
4. 公网资源及LB实例拆分：根据业务类型（如核心业务、测试环境）、流量特征（如高并发、长连接）和稳定性要求拆分公网带资源：为高优先级业务（如支付、核心交易）分配独立带宽资源和业务IP，避免低优先级流量（如日志同步、后台管理）占用过多带宽。负载均衡（LB）实例拆分：将不同业务或客户群体的流量分配到独立的LB实例，避免单一实例故障影响全局。
5. 配置LB实例CNAME访问：使用自有域名，通过CNAME解析的方式将自有域名指向NLB/ALB实例域名，参考[为ALB配置CNAME解析](https://help.aliyun.com/zh/slb/application-load-balancer/configure-cname-resolution-for-alb)。当CNAME域名发生故障时可以将权威DNS解析的CNAME记录修改成A记录（NLB、ALB的服务EIP）进行故障恢复。当出现某个NLB/ALB公网IP不可用时，可申请新的EIP替换出现问题的NLB/ALB公网IP即可。
6. 接入层资源采用多可用区部署创建多可用区SLB实例创建后端服务器组, 保证服务器组内服务器分布在多个可用区配置监听规则，转发规则和健康检查。具体架构设计可参考[SLB构建应用交付网络](https://help.aliyun.com/zh/cloud-network-well-architected-design/use-slb-to-build-an-application-delivery-network/)

## 相关资源

### 相关文档

- [什么是应用型负载均衡ALB](https://help.aliyun.com/zh/slb/application-load-balancer/what-is-alb)
- [什么是全局流量管理？](https://help.aliyun.com/zh/dns/what-is-gtm-1)
- [什么是云解析DNS](https://help.aliyun.com/zh/dns/product-introduction-dns2-0)
- [什么是阿里云CDN](https://help.aliyun.com/zh/cdn/product-overview/what-is-alibaba-cloud-cdn)

---

> 原页面：https://help.aliyun.com/zh/well-architected/configure-highly-available-network-connections-for-public-network-endpoints-of（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
