<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0031.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# SEC02-03 网络访问权限最小化

确保只有必要的人员或组件可以访问特定的网络资源。

- **风险等级** 高
- **关键策略** 通过配置安全组和网络访问控制列表（ACL），控制进出云资源的网络流量，确保只有授权的流量能够访问特定的服务和端口。根据业务实际情况优化每个网络区域的ACL，并保证访问控制规则数量最小化。 避免暴露多余的公网IP，同时不应对外开放或未最小化开放高危端口、远程管理端口。 安全组仅开放业务所需的网段及端口，禁止设置成对所有IP(0.0.0.0/0)都可访问。
- **相关云服务和工具** 虚拟私有云 VPC NAT网关 NAT 安全云脑 SecMaster：云服务基线核查

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0031.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
