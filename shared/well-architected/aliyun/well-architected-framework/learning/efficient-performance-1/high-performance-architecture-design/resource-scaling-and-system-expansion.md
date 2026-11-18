<!-- source: https://help.aliyun.com/zh/well-architected/resource-scaling-and-system-expansion -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2536104 -->

# 资源伸缩和系统扩展

在云上架构设计过程中，需要考虑架构的可伸缩性和可扩展性，以实现高性能的云上架构。不同的应用部署方式需要使用不同的伸缩方案，常见的伸缩方案主要有以下几种：

## 云服务自动扩缩

在阿里云上进行自动伸缩依赖的云服务是弹性伸缩 ESS（Auto Scaling），是指根据业务需求和策略自动调整计算能力（即实例数量）的服务。目前支持ECS实例和ECI实例的弹性伸缩。弹性伸缩具有广泛的应用场景，不仅适合业务量不断波动的应用程序，同时也适合业务量稳定的应用程序。

### 适用场景

#### 无规律的业务量波动

某新闻网站播出了热点新闻，访问量突增，新闻的时效性降低后，访问量回落。由于该新闻网站的业务量波动无规律，访问量突增和回落的具体时间难以预测，所以手动调整实例很难做到及时性，而且调整数量也不确定。

此时可以利用弹性伸缩的报警任务，由阿里云自动根据CPU使用率等衡量指标进行弹性伸缩。

- 示例一：可以设置两个报警任务，报警任务执行的伸缩规则配置为简单规则类型。一个报警任务用于在实例的CPU使用率超过70%时，自动增加3台实例；另一个报警任务用于在实例的CPU使用率低于30%时，自动减少3台实例。
- 示例二：可以设置一个报警任务，报警任务执行的伸缩规则配置为目标追踪规则类型，使实例的CPU使用率一直维持在50%左右。

#### 有规律的业务量波动

某游戏公司每天18:00业务需求急速增长进入高峰期，到22:00业务需求降低，高峰期结束。该游戏公司的业务量波动有规律，但是每天手动调整计算能力浪费人力和时间成本。

此时可以利用弹性伸缩的定时任务，由阿里云定时自动进行弹性伸缩。可以设置两个定时任务，报警任务执行的伸缩规则是简单规则类型。一个定时任务用于在每天17:55自动为用户增加3台实例，另一个定时任务用于在每天22:05自动为用户减少3台实例。该方式可以很好地应对每天18:00~22:00高峰期的业务量，且在高峰期结束后及时释放实例，不浪费多余的实例资源和成本。

#### 无明显的业务量波动

某通信公司的业务支撑系统需要全天运作，业务量一段时间内无明显波动。如果现有计算资源突然出现故障，会导致业务受到影响，很难及时进行故障修复或者替换。

此时可以利用弹性伸缩的高可用优势，开启健康检查模式。阿里云会自动检查实例的健康状态，当发现存在实例不健康时，自动增加实例替换不健康的实例，确保故障的计算资源及时得到修复。而且伸缩组必须设置最小实例数，确保无论在哪种情况下，伸缩组内的实例数量都至少等于下限，确保业务可以运作。

#### 混合型的业务场景

如果某公司的业务场景比较复杂，日常业务量波动不明显，且在某个时间段内，业务量是在一定基础上波动的，用户已经订购了一部分包年包月的实例，只是想针对波动的业务量合理调整实例数量。

此时可以手动将已订购的包年包月实例加入伸缩组，再结合弹性伸缩的报警任务，由阿里云自动根据CPU使用率等衡量指标进行弹性伸缩，更经济、稳定地管理业务的计算能力。

除手动调整实例数量和报警任务，弹性伸缩还支持定时任务、健康检查等。此时可以根据业务场景灵活组合以上功能，从而在使用弹性伸缩的时候获得更丰富灵活的使用体验。

## 容器自动扩缩

容器越来越成为云计算的核心计算技术，越来越多的应用系统已经完成或正在进行容器化改造，运行在各种容器环境中。阿里云上对应的容器服务为容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）。对应的弹性伸缩典型场景包含在线业务弹性、大规模计算训练、深度学习GPU或共享GPU的训练与推理、定时周期性负载变化等。弹性伸缩分为两个维度：

- 调度层弹性，主要是负责修改负载的调度容量变化。例如，HPA是典型的调度层弹性组件，通过HPA可以调整应用的副本数，调整的副本数会改变当前负载占用的调度容量，从而实现调度层的伸缩。
- 资源层弹性，主要是集群的容量规划不能满足集群调度容量时，会通过弹出ECS或ECI等资源的方式进行调度容量的补充。

两层的弹性组件与能力可以分开使用，也可以结合在一起使用，并且两者之间是通过调度层面的容量状态进行解耦。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3166813961/p711637.png)

### 适用场景

在选择具体的弹性方案时，需要考虑相应弹性维度下不同组件和方案的适用场景、资源交付速度和使用限制等。

**调度层弹性**

| **组件名称** | **组件介绍** | **适用场景** | **使用限制** | **参考文档** |
| --- | --- | --- | --- | --- |
| HPA | Kubernetes内置组件，主要面向在线业务。 | 在线业务 | 适用于Deployment、StatefulSet等实现scale接口的对象。 | [使用容器水平伸缩（HPA）](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/horizontal-pod-autoscaling#task-1830087) |
| VPA（alpha） | 开源社区组件，主要面向大型单体应用。 | 大型单体应用 | 适用于无法水平扩展的应用，通常是在Pod出现异常恢复时生效。 | [使用容器垂直伸缩（VPA）](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/vertical-pod-autoscaling#task-2455855) |
| CronHPA | ACK开源的组件，主要面向应用资源使用率存在周期性变化的场景。 | 周期性负载业务 | 适用于Deployment、StatefulSet等，实现了scale接口的对象。此外CronHPA提供了HPA对象的兼容能力，您可以同时使用CronHPA与HPA。 | [使用容器定时水平伸缩（CronHPA）](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/cronhpa#task-2391975) |
| Elastic-Workload | ACK组件，主要面向精细化角度场景，例如希望在不同的可用区进行负载分布。 | 精细调度场景 | 适用于在线业务精细化控制的场景。例如，一个Deployment部分的应用运行在ECS上，而超出的部分运行在ECI上。 | [通过Elastic Workload将弹性负载的Pod调度到ECI（停止维护）](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/install-ack-kubernetes-elastic-workload#task-2565096) |

**资源层弹性**

| **组件名称** | **组件介绍** | **适用场景** | **资源交付速度** | **参考文档** |
| --- | --- | --- | --- | --- |
| cluster-autoscaler | Kubernetes社区开源组件，节点水平伸缩组件，阿里云提供了调度、弹性优化、成本优化的功能。 | 全场景支持，适合在线业务、深度学习、大规模成本算力交付等。 | 以100节点为一个交付批次为例：标准模式：120s极速模式：60s标准模式-Qboot镜像：90s极速模式-Qboot镜像：45s关于Qboot镜像的更多信息，请参见[什么是Alibaba Cloud Linux](https://help.aliyun.com/zh/alinux/product-overview/alibaba-cloud-linux-overview#section-to6-5lp-7d6)。 | [启用节点自动伸缩](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/auto-scaling-of-nodes#task-1893824) |
| virtual-node | ACK开源组件，提供无服务器运行时环境。开发者无需关心节点资源，只需针对Pod按量付费即可。 | 部分场景支持，主要包括在线突增流量、CI/CD、大数据作业。 | 以1000个Pod为一个交付批次为例：未开启镜像缓存：30s已开启镜像缓存：15s | [将Pod调度到ECI上运行](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/deploy-the-virtual-node-controller-and-use-it-to-create-elastic-container-instance-based-pods#task-1443354) |
| virtual-kubelet-autoscaler | ACK服务组件，提供无服务弹性伸缩能力。 | 部分场景支持，主要包括在线突增流量、CI/CD、大数据作业。 | 以1000个Pod为一个交付批次为例：未开启镜像缓存：30s已开启镜像缓存：15s | [将调度失败的Pod重新调度到ECI](https://help.aliyun.com/zh/ack/install-virtual-kubelet-autoscaler#task-2564804) |

## Serverless

对于用户来说，云服务和容器的伸缩都需要用户一定程度上参与基础设施层面的资源管理和维护。而Serverless技术则无需用户关心基础设施层面的伸缩扩容。Serverless相关的云产品有弹性快（毫秒级扩容），成本优（按实际使用量付费），开发效率高（不用关心底层云资源）三大特性。截止目前阿里云Serverless架构的核心云产品已经达到20余款，具备完整的从Serverless计算，到Serverless应用开发的服务能力。

### 函数计算

函数计算 FC（Function Compute）是事件驱动的全托管计算服务，用户无需采购与管理服务器等基础设施，只需编写并上传代码或镜像。函数计算准备好计算资源，弹性地、可靠地运行任务，并提供日志查询、性能监控和报警等功能。

### Serverless应用引擎SAE

Serverless 应用引擎 SAE（Serverless App Engine）是一个全托管、免运维、高弹性的通用 PaaS 平台。SAE 支持 Spring Boot、Spring Cloud、Dubbo、HSF、Web 应用和 XXL-JOB、ElasticJob 任务的全托管、零改造迁移、无门槛容器化、并提供了开源侧诸多增强能力和企业级高级特性。

---

> 原页面：https://help.aliyun.com/zh/well-architected/resource-scaling-and-system-expansion（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
