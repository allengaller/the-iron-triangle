<!-- source: https://help.aliyun.com/zh/well-architected/hub-and-spoke-rather-than-many-to-many-peer-to-peer-networks -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2948842 -->

# 组网方式采用Hub-Spoke网络代替点对点网络

在构建多 VPC、混合云或跨地域网络架构时，采用合理的网络拓扑结构对于提升网络的可管理性、安全性与可扩展性至关重要。

Hub-Spoke 网络 是一种集中式网络架构，由中心节点（Hub）和多个外围节点（Spoke）组成。所有 Spoke 节点仅通过 Hub 节点进行通信，Spoke 之间无直接连接路径。这种架构常用于企业网络或云环境中，实现资源集中管理、流量统一调度和安全策略控制 。

点对点网络 （Peer-to-Peer, P2P）是一种去中心化架构，所有节点（Peer）地位平等，既可作为客户端也可作为服务器，直接与其他节点交换数据，无需中心节点中转。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2612872771/p987185.png)

阿里云云上提供转发路由器作为同地域hub-spoke网络的核心节点。而VPC对等连接和VBR上联（不提供新购）提供点到点网络的配置能力。目前云上网络建议使用Hub-Spoke网络代替点对点网络。多个地域的转发路由器互相full-mesh连接构筑整个云上跨地域网络。基于转发路由器实现的全球组网架构示意图：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2612872771/p987187.png)

## 优先级

中

## 不推荐做法

- 构建复杂的网络对等规则，当VPC数量较多时，点对点网络路由运维配置难度大幅度提高。
- 末根据VPC的交换机所在可用区配置对应的转发节点，导致部分可用区存在流量绕行，末就近转发导致业务时延上升。
- 多个业务共用跨地域带宽且未设置流量调度功能，导致低优先级的数据同步流量占满跨地域带宽，影响高优先级的实时业务。

## 实施指南

### 1. 转发路由器多可用区冗余与就近转发

1. 如果企业版转发路由器在当前地域仅支持一个可用区，则需要在当前可用区选择一个交换机实例。
2. 如果企业版转发路由器在当前地域支持多个可用区，则需要在至少2个可用区中各选择一个交换机实例。在VPC和企业版转发路由器流量互通的过程中，这2个交换机实例可以实现可用区级别的容灾。
3. 推荐在每个可用区中都选择一个交换机实例，以减少流量绕行，体验更低传输时延以及更高性能。
4. 参考转发路由器配置相关文档。[转发路由器工作原理](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)

### 2. 跨地域连接带宽拆分

方案一：云上跨地域连接建议按照生产、测试、办公等业务类型构建不同的网络平面，各个网络平面使用自己独立的CEN，各个CEN可以独立部署自己的跨Region内网连接及带宽。[跨地域VPC互通](https://help.aliyun.com/zh/cen/getting-started/inter-region-vpc-interworking)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2612872771/p987247.png)

方案二：当多个业务共用CEN跨Region内网连接时，把各个业务划分独立的网段、然后使用CEN TR的流量调度功能能力进行带宽拆。[使用流量调度功能控制各类流量的跨地域带宽](https://help.aliyun.com/zh/cen/user-guide/use-traffic-scheduling-to-limit-bandwidth-for-inter-region-connections)。

## 相关资源

### 相关文档

- [什么是云企业网](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)
- [VPC对等连接](https://help.aliyun.com/zh/vpc/vpc-peer-to-peer-connection)

---

> 原页面：https://help.aliyun.com/zh/well-architected/hub-and-spoke-rather-than-many-to-many-peer-to-peer-networks（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
