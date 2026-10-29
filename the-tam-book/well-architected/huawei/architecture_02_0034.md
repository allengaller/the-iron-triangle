<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0034.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES04-02 部署容灾系统以满足容灾目标

针对不同应用系统的容灾目标，需要综合考虑中断概率、容灾成本等因素，来决定采用什么样的容灾方案来实现这些目标。

- **风险等级** 高

- **关键策略** 面向跨Region/跨云容灾场景，可基于不同的可用性目标要求，采用不用的容灾方案，如远程备份、主备容灾、双活容灾等，其中生产站点根据场景不同可能为其他云或IDC或华为云Region： 远程备份：生产站点内的重要数据，备份到异地华为云灾备Region，当生产站点发生灾难时，需要在异地灾备Region新部署一套业务系统并使用最新备份数据恢复数据，并恢复业务。 主备容灾：生产站点与华为云灾备Region各部署一套业务系统，并将生产站点的重要数据异步复制到灾备Region；平常只有生产站点提供业务，当生产站点发生灾难时，将灾备Region提升为主，并将业务流量切换到灾备Region并由其提供业务。 双活/多活容灾：生产站点与华为云灾备Region各部署一套业务系统，并将各自站点的重要数据异步复制到其他站点；每个站点都同时提供业务，通过全局负载均衡器进行流量分发；当一个站点发生灾难时，则将业务流量全部分发到其他站点来接管其业务。 以跨Region主备容灾为例，对于已在一个Region部署应用系统后，增加支持跨Region主备容灾能力的实施步骤建议如下： 选择另一个Region作为灾备Region，部署一套相同的应用系统，包括工作负载、数据库实例等。 针对应用系统内的关键数据，利用云服务或应用系统自身实现跨Region的数据复制。 若云服务实例支持跨Region容灾，则配置生产站点与灾备Region之间的复制，如对于RDS数据库实例，需申请DRS实例对主Region与灾备Region的数据库进行实时复制；对于OBS桶，需要配置主Region中的OBS桶到灾备Region中OBS桶的复制。 若云服务实例不支持跨Region容灾，但数据比较关键，则需要应用层实现跨Region的数据双写，以进行数据同步。 接入侧主Region与灾备Region各自申请外部IP，并通过DNS域名解析到主Region，在主Region故障时，将DNS域名对应IP地址修改为灾备Region中的外部IP。 申请MAS多活高可用服务，进行容灾编排，以便在灾难场景快速主备切换恢复业务。
- **相关云服务和工具** 云备份 CBR：支持跨区域复制与恢复 数据复制服务 DRS：支持RDS for MySQL、GaussDB for MySQL等数据库的实时灾备，支持跨Region/跨云容灾场景 对象存储服务 OBS：支持跨区域复制与双活

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0034.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
