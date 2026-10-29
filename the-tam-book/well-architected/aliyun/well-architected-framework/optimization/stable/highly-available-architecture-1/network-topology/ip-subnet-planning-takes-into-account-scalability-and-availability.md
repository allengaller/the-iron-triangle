<!-- source: https://help.aliyun.com/zh/well-architected/ip-subnet-planning-takes-into-account-scalability-and-availability -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2948830 -->

# IP子网规划时充分考虑到扩展性和可用性

企业在使用阿里云服务过程中，合理规划专有网络（VPC）及VPC 的IP地址空间和子网分配，是构建高可用、可扩展云网络架构的基础。通过合理规划 VPC及VPC 的 CIDR 块、子网划分、地址分配策略，确保网络架构具备良好的可扩展性、高可用性，并避免地址空间浪费或重新配置带来的业务中断风险。

## 优先级

中

## 不推荐做法

- 简化VPC及交换机规划，将多个系统部署在一个VPC或者一个VPC的一个交换机中，导致不同系统之间无法实施精细化安全管控。
- 网络IP地址段规划不当，如未预留足够IP段或分配不合理导致后续扩容困难或地址浪费 。初始规划时未预留足够地址，导致业务扩容时无法新增子网或分配IP。
- 忽略可用区冗余，导致把关键云服务部署在一个可用区内，可能会引发单可用区故障风险。

## 实施指南

### 1. VPC设计规划

VPC设计需要根据业务系统需求，选择正确的VPC部署形态和数量，合理规划VPC内交换机及安全组策略，降低安全风险。合理的VPC设计划分还可以保障高可用架构，并预留扩展空间以应对未来业务增长。

#### 1.1 单VPC与多VPC对比

| 维度 | 多VPC | 单VPC |
| --- | --- | --- |
| 安全性 | 高 | 低 |
| 管理复杂度 | 高 | 低 |
| 成本控制 | 更细 | 粗放 |
| 扩展性 | 强 | 有限 |
| 通信效率 | 依赖网络互连 | 内部高效 |
| 适用企业 | 中大型企业 | 小型或初创企业 |

#### 1.2 VPC实施指导

1. 选择地域，可用区，不同类型资源部署在不同可用区。
2. 同类型资源保证可用区冗余部署，避免任何情况下的单可用区部署。
3. 根据连接规划交换机：部署用于访问公网的公网交换机（Public vSwitch），仅有内网互访的私有交换机（Private vSwitch），用于VPN访问的VPN交换机，提供给网元部署使用的网元交换机。
4. 根据VPC划分和交换机设计，设计VPC的IP划分，注意VPC内地址冗余并避免IP地址重叠
5. 为不同资源部署相应安全组及ACL规则

具体架构设计可参考[同地域单VPC网络设计](https://help.aliyun.com/zh/cloud-network-well-architected-design/single-vpc-network-design-in-the-same-region)

### 2. IP地址规划

VPC部署前需要进行IP地址规划和设计，预留足够的IP地址空间 ，以应对业务扩展、故障转移或冗余架构的需求。为未来新增子网、弹性扩容或高可用部署预留地址池，避免因地址耗尽可能导致的网络重构。

#### 2.1 IP地址分配策略

- 子网划分策略：每个子网对应一个可用区，地址不重叠在VPC内划分子网时，需为每个子网分配大于当前需求的地址段 ，并预留10~20%地址空间供末来扩展。对需要大量IP地址的场景（如容器集群、临时实例），建议启用IPv6。
- IP地址管理使用IPAM工具自动化分配地址。[IP地址管理（IPAM）](https://help.aliyun.com/zh/vpc/ip-address-management-ipam/)。监控地址使用率并预警耗尽风险，确保冗余空间可控。

## 相关资源

### 相关文档

- [什么是专有网络VPC](https://help.aliyun.com/zh/vpc/what-is-vpc)
- [什么是云企业网](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/ip-subnet-planning-takes-into-account-scalability-and-availability（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
