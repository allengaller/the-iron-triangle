<!-- source: https://help.aliyun.com/zh/well-architected/configure-redundant-connections-for-the-private-network-between-the-local -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2948810 -->

# 为本地机房与云上环境之间的私有网络配置冗余连接

企业在从本地数据中心（IDC）迁移到阿里云过程中要确保本地数据中心与阿里云 VPC 之间的网络连接具备高可用性，是保障业务连续性和系统可靠性的关键要素之一。通过部署冗余网络连接、使用双隧道 IPsec-VPN、配置高速通道与 IPsec-VPN 主备链路等方式，确保本地数据中心与阿里云 VPC 之间的网络连接具备高可用性，从而提升整体系统的可靠性和容错能力。

## 优先级

高

## 不推荐做法

- 生产业务与离线大数据业务共用1条/组专线混跑，未进行业务拆分，当离线传输的数据量突发、占满专线带宽，导致实时业务丢包受损。
- 仅采用单专线接入或单条IPSec-VPN接入，单点故障，网络中断将导致业务不可用。
- 所有连接部署在同一可用区或者单运营商接入，无法抵御可用区或单一运营商设备故障。
- 忽略带宽限制和性能瓶颈，导致专线隧道容量不足，影响数据传输。

## 实施指南

### 1. 拆分专线带宽

不同业务共享专线网络带宽时，可能会导致流量抢占，相互影响，一个业务流量突然可能会导致其他业务不可用。需要对专线带宽进行拆分。

- 方案一：不同等级的业务各自使用独立的专线线路。
- 方案二：当多个业务共用专线线路时，把各个业务划分独立的网段、然后使用专线QoS能力进行带宽拆分[QoS策略](https://help.aliyun.com/zh/express-connect/user-guide/qos-policy)。
- 方案三：同专线情况下，不同的业务使用不用的VBR，并设置VBR带宽的能力实现专线带宽的拆分。参考以下文档设置VBR带宽[创建和管理边界路由器](https://help.aliyun.com/zh/express-connect/user-guide/create-and-manage-a-vbr)。

### 2. 专线冗余保护

专线的冗余保护是指通过部署多条独立链路或备用链路，确保在主链路发生故障时能够自动切换至备用链路，从而保障云和线下机房（IDC）之间的通信的连续性和高可用性。

1. 多接入点：用户IDC通过至少两个独立的云专线接入点连接至至少2个不同的阿里云接入点，实现物理链路的冗余和负载分担，多接入点接入时尽量选择不同运营商。
2. 多专线接入：在多接入点接入的基础上，在每个接入点可以增加更多的专线接入，专线需要选择不同运营商，接入路由，园区线路尽量不同。
3. 多专线使用ECMP等价模式接入：相对于主备路由多专线接入模式，ECMP等价路由模式具备故障快速收敛，横向扩展性强，资源利用率高（偶发流量场景）等优势，建议业务无源进源出等限制的场景，多专线接入优先使用ECMP等价路由模式。
4. VPN作为专线备份：在企业版TR场景下，VPN支持备份专线，可使用VPN网关对专线进行冗余备份，保证专线全部中断下混合云连接依然可用。部署架构可参考高速通道最佳实践[本地IDC通过ECR实现主备专线链路上云](https://help.aliyun.com/zh/express-connect/use-cases/the-local-idc-can-use-ecr-to-access-the-cloud)。

### 3. IPSec连接冗余保护

IPsec连接的冗余保护是指通过配置多条独立IPsec隧道或链路，在主链路故障时自动切换至备用链路，保障云上和云下加密通信的连续性和高可用性。

- VPN双隧道模式：阿里云VPN网关采用双可用区部署，双公网出口。TR采用多可用区集群化部署。VPN网关支持主备双隧道模式，TR支持主主双隧道模式。当单个IPsec VPN隧道因网络中断、设备故障等问题失效时，流量会自动切换至另一隧道，保障业务连续性。
- VPN ECMP模式：企业可以在本地IDC和阿里云之间建立多条IPsec-VPN连接，实现本地IDC上云，然后通过云企业网产品将多条IPsec-VPN连接和VPC实例连接起来，多条IPsec-VPN连接加入云企业网后可以自动组成ECMP链路，实现本地IDC和VPC实例之间的相互通信以及流量的负载分担。具体可参考以下部署指导[IPsec-VPN实践教程](https://help.aliyun.com/zh/vpn/use-cases/ipsec-vpn-practice-tutorial)

## 相关资源

### 相关文档

- [什么是高速通道](https://help.aliyun.com/zh/express-connect/product-overview/what-is-express-connect/)
- [什么是IPsec-VPN](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/product-overview/what-is-ipsec-vpn)
- [什么是云企业网](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)
- [阿里云网络高可用性白皮书](https://help.aliyun.com/zh/cloud-network-well-architected-design/?scm=20140722.S_help%40%40%E6%96%87%E6%A1%A3%40%402856621._.ID_help%40%40%E6%96%87%E6%A1%A3%40%402856621-RL_%E9%98%BF%E9%87%8C%E4%BA%91%E7%BD%91%E7%BB%9C%E5%8D%93%E8%B6%8A%E6%9E%B6%E6%9E%84-LOC_doc%7EUND%7Eab-OR_ser-PAR1_2102029c17528234456328100d6339-V_4-RE_new8-P0_1-P1_0&spm=a2c4g.11174283.help-search.4)

---

> 原页面：https://help.aliyun.com/zh/well-architected/configure-redundant-connections-for-the-private-network-between-the-local（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
