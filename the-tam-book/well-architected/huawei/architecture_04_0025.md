<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0025.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# PERF03-06 选择合适的消息队列

- **风险等级** 中
- **关键策略** 三种不同版分布式消息服务的适用场景如下： Kafka：兼容开源Kafka，适用构建实时数据管道、流式数据处理、第三方解耦、流量削峰去谷等场景，有大规模、高可靠、高并发访问、可扩展且完全托管的特点。 RocketMQ：兼容开源RocketMQ，提供顺序、延迟、定时、重投、死信、事务与会话消息等功能，适用电商、金融场景。 RabbitMQ：兼容开源RabbitMQ，支持广播、事务消息、消息路由、死信队列、优先级队列等，适用于流控、系统解耦等场景。 详细版本对比可参考[官方文档](https://support.huaweicloud.com/intl/zh-cn/productdesc-kafka/kafka_pd_0003.html)。
- **相关云服务和工具：** 分布式消息服务Kafka版 分布式消息服务RocketMQ版 分布式消息服务RabbitMQ版

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0025.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
