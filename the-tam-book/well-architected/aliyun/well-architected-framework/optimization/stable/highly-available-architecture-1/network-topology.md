<!-- source: https://help.aliyun.com/zh/well-architected/network-topology/ -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2925040 -->

# 网络拓扑

在阿里云卓越架构的稳定性支柱中，高可用架构的网络拓扑设计至关重要。工作负载通常存在于多种环境中，包括公共可访问的云环境和私有云环境，以及您现有的数据中心基础设施。因此，规划必须考虑网络因素，如内系统和跨系统的连接性，公共IP地址管理，私有IP地址管理，以及域名解析。

在设计基于IP地址的网络系统时，必须提前规划网络拓扑和地址分配，以应对可能的故障，并适应未来的增长和与其他系统及其网络的集成。阿里云提供了一系列最佳实践，帮助您在阿里云环境中构建稳定而高效的网络架构，为业务的持续增长和有效运营提供坚实的支持。

## 最佳实践

- [为工作负载公网端点配置高可用的网络连接](https://help.aliyun.com/zh/well-architected/configure-highly-available-network-connections-for-public-network-endpoints-of)
- [为本地机房与云上环境之间的私有网络配置冗余连接](https://help.aliyun.com/zh/well-architected/configure-redundant-connections-for-the-private-network-between-the-local)
- [IP子网规划时充分考虑到扩展性和可用性](https://help.aliyun.com/zh/well-architected/ip-subnet-planning-takes-into-account-scalability-and-availability)
- [组网方式采用Hub-Spoke网络代替点对点网络](https://help.aliyun.com/zh/well-architected/hub-and-spoke-rather-than-many-to-many-peer-to-peer-networks)
- [自动分配与管理IP地址以避免IP地址冲突](https://help.aliyun.com/zh/well-architected/automatically-allocate-and-manage-ip-addresses-to-avoid-ip-address)

---

> 原页面：https://help.aliyun.com/zh/well-architected/network-topology/（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
