<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0143.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 可靠性功能

#### 集群HA

Kafka实例通过副本冗余方式实现实例容灾，当检测到leader副本故障后，快速完成副本选主，保障Kafka实例持续提供服务。

RabbitMQ集群提供镜像队列，通过镜像在其他节点同步数据。单节点宕机时，仍可通过唯一的访问地址对外提供服务。

RocketMQ使用一主两备架构，备节点通过数据同步的方式保持数据一致。当节点故障时，通过Raft协议自动切换主备关系，保持数据强一致性。

#### 跨AZ容灾

Kafka、RabbitMQ、RocketMQ实例支持跨AZ容灾部署，要求至少3个AZ，当一个AZ异常时，不影响实例持续提供服务。

#### 监控告警

Kafka：配合CES服务，支持对Kafka实例、实例节点、实例主题、实例分区、实例分区的消费组、实例队列的消费组、实例的消费组等进行监控和告警。

详见“[支持的监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-kafka/kafka-ug-180413002.html)”。

RabbitMQ：配合CES服务，支持对RabbitMQ实例、实例节点、实例队列进行监控和告警等进行监控和告警。

详见“[支持的监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-rabbitmq/rabbitmq-ug-180413002.html)”。

RocketMQ：配合CES服务，支持对RocketMQ实例、实例节点、实例队列、实例消费组、实例队列消费组、实例的死信队列进行监控和告警。

详见“[支持的监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-hrm/hrm-ug-018.html)”。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0143.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
