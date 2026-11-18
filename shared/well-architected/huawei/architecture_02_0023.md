<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0023.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES02-02 自动数据备份

对于需要备份的数据，可根据该数据的RPO指标要求，设置定期备份策略进行自动备份。

- **风险等级** 高

- **关键策略** 使用华为云备份服务或第三方备份软件对数据进行备份，并可根据RPO要求设置自动备份频率。CBR云备份服务可对ECS/BMS/EVS/SFS Turbo以及文件目录等进行备份；大多数云服务，如RDS、DDS、DCS等具备原生的创建备份功能；云商店也有不少备份软件可以支持各种数据的备份。 华为云云服务提供了备份工作负载数据的功能，典型的备份有： 云备份CBR服务：CBR提供对磁盘（EVS）、服务器（ECS、Flexus、BMS）基于快照的备份和恢复能力，SFS Turbo文件系统备份，云服务器部署的MySQL或SAP HANA等数据库备份，以及混合云备份。CBR支持一次性备份和周期性备份两种配置方式。目前备份时间只支持整点，可以同时选择多个整点进行备份，即最小RPO=1小时，用户需要根据数据重要性选择合适的备份周期。 数据库自动备份：RDS、DDS、GaussDB等数据库服务提供了缺省自动备份功能，实例每5分钟自动进行一次增量备份，以保证数据库的可靠性。 DCS备份：DCS服务针对非单机实例提供了自动备份和手工备份功能，建议设置自动备份策略进行备份。 此外，用户也可使用第三方备份软件进行备份。 华为云中云服务的数据备份到OBS存储中，可高度保障用户的备份数据安全。

- **相关云服务和工具** 云备份 CBR 云数据库 RDS 分布式缓存服务 DCS

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0023.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
