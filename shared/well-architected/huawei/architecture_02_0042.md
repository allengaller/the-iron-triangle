<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0042.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES05-04 预留IP资源以便扩展及高可用

云上网络需要满足可扩展以及高可用需求，以便在云上资源弹性伸缩或业务扩展时，有足够网络资源支撑业务发展。

- **风险等级** 高
- **关键策略** 云上网络规划设计应满足以下原则： 针对每个Region，根据业务需要规划不同的VPC，每个VPC使用独立的地址空间；并需要预留IP地址空间用于新建VPC。 针对每个VPC中，需要根据业务需要规划子网和IP地址空间；并需要预留IP地址空间用于新建子网。 针对每个子网，需要预留IP地址空间用于网络扩容。 当涉及与其他网络（如VPC、IDC或其他云）互连时，需要确保IP地址空间不重叠。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0042.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
