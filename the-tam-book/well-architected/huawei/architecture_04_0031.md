<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0031.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# PERF03-11 选择合适的非关系型数据库

- **风险等级** 中
- **关键策略** 华为云数据库提供了DDS、GeminiDB两种非关系型数据库服务。 DDS：文档数据库服务（Document Database Service）完全兼容MongoDB协议，提供安全、高可用、高可靠、弹性伸缩和易用的数据库服务，同时提供一键部署、弹性扩容、容灾、备份、恢复、监控和告警等功能，适用于游戏、物联网业务、互联网应用等多个场景。 GeminiDB Redis接口：GeminiDB Redis接口是一款基于华为自研的计算存储分离架构，兼容Redis生态的云原生NoSQL数据库，基于共享存储池的多副本强一致机制，支持久化存储，保证数据的安全可靠。具有高兼容、高性价比、高可靠、弹性伸缩、高可用、无损扩容等特点，适用于游戏、推荐、GIAmgGAP、推送等场景。 GeminiDB Influx接口：GeminiDB Influx 接口是一款基于华为自研的计算存储分离架构，兼容InfluxDB生态的云原生NoSQL时序数据库。提供大并发的时序数据读写，压缩存储和类SQL查询，并且支持多维聚合计算和数据可视化分析能力。具有高写入、灵活弹性、高压缩率和高查询等特点，适用于IoT、金融、软硬件设备实时监控、数据采集等场景。 GeminiDB Cassandra接口：GeminiDB Cassandra 接口是一款基于华为自研的计算存储分离架构，兼容Cassandra生态的云原生NoSQL数据库，支持类SQL语法CQL。具有安全可靠、超强读写、弹性扩展、便捷管理等特点，适用于互联网应用、工业数据采集等场景。 GeminiDB Mongo接口：GeminiDB Mongo 接口是一款基于华为自研的计算存储分离架构，兼容MongoDB生态的云原生NoSQL数据库。具有企业级性能、灵活弹性、高可靠、可视化管理等特点，广泛应用于游戏应用等场景。 GeminiDB HBase接口：GeminiDB HBase接口是一款兼容HBase生态的分布式NoSQL数据库，在Apache HBase的基础上进行扩展和优化，具有高性能、高可靠性、强大的扩展性和灵活的伸缩性等特点，适用于金融、电信、物流、游戏等场景。 同关系型数据库一样，非关系型数据的选择同样主要基于兼容性与场景评估两个原则： 场景一：基于兼容性原则 考虑平滑上云，上云前系统中数据库的选型已经过业务实践的检验，建议选取生态相同的关系型数据库服务进行平替，避免出现数据库层与应用层不兼容或数据库切换对业务架构中其他组件产生负面影响。 场景二：基于场景评估 如果是在云上新建业务系统或基于同数据库不同服务中选取时，建议结合业务的实际需要选取合适的数据库服务，如考虑性能、安全性等因素，产品详细介绍与规格信息可参考官方文档。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0031.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
