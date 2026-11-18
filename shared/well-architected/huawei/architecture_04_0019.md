<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0019.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# PERF03-03 使用弹性伸缩

- **风险等级** 中

- **关键策略** 如果工作负载能够支持弹性（例如：应用无状态化），请考虑具有自动缩放功能的计算服务，该功能可根据需求自动调整计算容量。自动缩放有助于确保在高峰期拥有足够的资源，并防止在低需求时段过度预配。虚拟机弹性伸缩和容器弹性伸缩都是实现应用自动化扩容和缩容的方式，但虚拟机弹性伸缩需要更多的资源和时间来启动和部署，而容器弹性伸缩可以更快速地响应变化，同时具有更高的资源利用率。虚拟机场景可以使用AS，容器场景充分考虑CA和HPA的弹性策略。 使用容器时弹性策略可参考下面内容： CCE的弹性伸缩能力分为如下两个维度： [工作负载弹性伸缩](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0290.html)：即调度层弹性，主要是负责修改负载的调度容量变化。例如，HPA是典型的调度层弹性组件，通过HPA可以调整应用的副本数，调整的副本数会改变当前负载占用的调度容量，从而实现调度层的伸缩。 [节点弹性伸缩](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0296.html)：即资源层弹性，主要是集群的容量规划不能满足集群调度容量时，会通过弹出ECS资源的方式进行调度容量的补充。 两个维度的弹性组件与能力可以分开使用，也可以结合在一起使用，并且两者之间可以通过调度层面的容量状态进行解耦。 详情请参见[使用HPA+CA实现工作负载和节点联动弹性伸缩](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0300.html)。 **工作负载弹性组件介绍** 类型 组件名称 组件介绍 参考文档 HPA [Kubernetes Metrics Server](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0205.html) Kubernetes内置组件，实现Pod水平自动伸缩的功能，即Horizontal Pod Autoscaling。在kubernetes社区HPA功能的基础上，增加了应用级别的冷却时间窗和扩缩容阈值等功能。 [HPA策略](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0208.html) CustomedHPA [CCE容器弹性引擎](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0240.html) 自研的弹性伸缩增强能力，主要面向无状态工作负载进行弹性扩缩容。能够基于指标（CPU利用率、内存利用率）或周期（每天、每周、每月或每年的具体时间点）。 [CustomedHPA策略](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0292.html) Prometheus [Prometheus](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0221.html) [云原生监控插件](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0406.html) 一套开源的系统监控报警框架，负责采集kubernetes集群中kubelet的公开指标项（CPU利用率、内存利用率）。 NA CronHPA [CCE容器弹性引擎](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0240.html) CronHPA可以实现在固定时间段对集群进行扩缩容，并且可以和HPA策略共同作用，定时调整HPA伸缩范围，实现复杂场景下的工作负载伸缩。 [CronHPA定时策略](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0415.html) **节点弹性伸缩组件介绍** 组件名称 组件介绍 适用场景 参考文档 [CCE集群弹性引擎](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0154.html) Kubernetes社区开源组件，用于节点水平伸缩，CCE在其基础上提供了独有的调度、弹性优化、成本优化的功能。 全场景支持，适合在线业务、深度学习、大规模成本算力交付等。 [节点自动伸缩](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0209.html) [CCE突发弹性引擎（对接CCI）](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0135.html) 将Kubernetes API扩展到无服务器的容器平台（如CCI），无需关心节点资源。 适合在线突增流量、CI/CD、大数据作业等场景。 [CCE容器实例弹性伸缩到CCI服务](https://support.huaweicloud.com/intl/zh-cn/usermanual-cce/cce_10_0295.html)
- **相关云服务和工具** 弹性伸缩 AS 云容器引擎 CCE 云容器实例 CCI

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0019.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
