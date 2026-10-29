<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0030.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# PERF03-10 选择合适的关系型数据库

- **风险等级** 中

- **关键策略** 华为云数据库提供了多款关系型数据库服务，包含GaussDB、TaurusDB、RDS（MySQL、PostgreSQL、SQL Server、MariaDB）；其中GaussDB、TaurusDB是华为推出的基于openGauss生态和MySQL生态的企业级关系型数据库，性能表现更好；RDS数据库服务可支持四种开源数据库引擎，RDS依托云计算平台，为用户提供了更稳定、更弹性、运维更便捷的在线云服务。 适用场景： GaussDB：基于华为主导的openGauss生态推出的企业级分布式关系型数据库，具有云上高可用、高可靠，高安全、弹性伸缩、一键部署、快速备份恢复等能力，适用于高并发、大数据量、以联机事务处理为主的交易型应用，如政务、金融、电商、O2O、电信CRM/计费等。 TaurusDB ：华为自研的最新一代企业级高扩展高性能云原生关系型数据库，完全兼容MySQL，具有高性能、高扩展性、高可靠性、高兼容性、低成本、非中间件式架构等特点，适用金融行业、游戏行业等需要高安全或高性能的行业。 RDS：具有低成本、高性能、高安全性、高可靠性等特点。 RDS for MySQL：MySQL是当前应用最广泛的开源关系型数据库。RDS for MySQL适用于网站业务、应用程序、中小型企业等场景。 RDS for PostgreSQL：PostgreSQL是一个开源对象云数据库管理系统，并侧重于可扩展性和标准的符合性。RDS for PostgreSQL适用于网站业务、位置应用系统、复杂数据对象处理等场景。 RDS for SQL Server：Microsoft SQL Server是老牌商用级数据库，成熟的企业级架构，轻松应对各种复杂环境；RDS for SQL Server适用于政府、金融、医疗、教育、游戏等领域。 RDS for MariaDB：MariaDB是当前比较主流开源社区数据库之一，对MySQL有较好的兼容性；RDS for MariaDB适用于各种规模的应用程序。 关系型数据库的选择建议： 场景一：基于兼容性原则 考虑平滑上云，上云前系统中数据库的选型已经过业务实践的检验，建议选取生态相同的关系型数据库服务进行平替，避免出现数据库层与应用层不兼容或数据库切换对业务架构中其他组件产生负面影响。 场景二：基于场景评估 如果是在云上新建业务系统或基于同数据库不同服务中选取时，建议结合业务的实际需要选取合适的数据库服务；例如RDS for MySQL和TaurusDB，在选取时应考虑更多因素，如性能等因素，这些因素可以从官方资料查看。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0030.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
