<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0026.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# PERF03-07 选择合适的Kafka

- **风险等级** 中
- **关键策略** 根据生产流量、消费流量、老化时间、副本数等指标，计算业务所需的规格，选择合适的Kafka规格。 规格测算： 性能容量维度所需最小节点数 = max（（存储带宽需求 / 单节点存储带宽），（网络带宽需求 / 单节点网络基准带宽）） 磁盘容量维度所需最小节点数 = max（总磁盘容量需求 / 单节点磁盘容量上限） 详细规格选择参考[官方文档](https://support.huaweicloud.com/intl/zh-cn/productdesc-kafka/Kafka-specification.html)。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0026.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
