<!-- source: https://help.aliyun.com/zh/well-architected/solution-117 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929261 -->

# 容器集群分账最佳实践

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4386581571/p970309.png)

本文档提供一种成本治理FinOps解决方案来协助企业IT成本管理人员实现容器集群分账。方案提供了资源浪费检查、资源费用预测等功能，通过账单分析、用量统计与实时询价相结合的方式实现对Pod维度的准确估算。本方案从物理和逻辑两个维度进行聚合分析，物理维度包括集群的Node、节点池和资源组，逻辑维度包括Pod、应用负载和命名空间；并将物理维度的费用和逻辑维度的费用进行打通，建立完整的资源成本画像，能够更准确合理地进行IT成本治理。

## 方案优势

### 独有的云原生容器场景成本分摊与估算模型

为了解决容器场景下业务单元与计费单元生命周期不一致的问题，本方案提出了独有的计费与计量相结合的成本估算模型，并加入费用策略（付费类型、节省计划、代金券、用户折扣、竞价波动）、分摊因子（CPU、内存、GPU卡、GPU显存等）、资源形态（ECS\ECI\HPC）等因素的考量，实现针对Pod维度的成本估算以及集群占比的成本分摊。通过账单分析将集群在一个阶段内的所有资源成本进行聚合，再配合Pod维度的成本分摊能力实现了完整的云原生容器场景成本分摊与估算模型。

### 多维度的成本洞察、趋势预测、根因下钻

支持集群、命名空间、节点池、应用（label通配符匹配）四个维度的成本洞察，集群维度侧重在云资源的分布、资源成本的趋势变化、集群水位与浪费的比率以及集群成本费用的趋势与预测，可以协助IT管理员准确判断成本消费的趋势，防止超过预算的场景；命名空间侧重在费用的分摊，支持短周期的费用预估以及长周期的成本分摊，支持调度水位、资源用量、成本趋势的相关性分析，协助部门管理员进行成本估算，下钻分析成本浪费，提升部门资源利用率；节点池维度侧重在资源成本规划与治理，通过实例类型、单位核时、调度水位、利用率水位的相关性分析，协助IT资产管理员优化资源组合和付费策略。应用（label通配符匹配）维度侧重在领域场景成本优化，例如：大数据、AI、离线作业、在线应用等各种上层应用场景，都可以通过应用维度的成本洞察进行实时费用预估以及任务级别的成本核算。

### 全场景的成本优化能力、解决方案的覆盖

针对于不同企业的实际业务场景，本方案提供了全场景的资源画像建立、成本优化能力与解决方案：

- [弹性伸缩](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/auto-scaling-of-nodes)
- 混部
- [智能资源画像](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/resource-profiling)
- [云原生大数据/AI](https://help.aliyun.com/zh/ack/cloud-native-ai-suite/product-overview/cloud-native-ai-suite-overview)
- [云原生工作流](https://help.aliyun.com/zh/ack/ags-workflow/)

此外，企业针对成本的优化策略，大部分是需要业务场景支撑的，很多场景下还会存在定制化和二次开发。因此，本方案提供的成本洞察能力与上层优化方案完全解耦的，可以通过四个维度的成本洞察能力，覆盖全场景的成本优化手段的衡量与评估。

### 多集群/多云/混合云全类型云成本管理能力

本方案通过提供统一的云服务厂商的账单与询价接入与默认实现，支持主流的云服务厂商、IDC自建机房的费用数据的接入。并通过一致的云原生容器场景成本分摊与估算模型进行成本管理。配合企业级云原生分布式云容器平台ACK One（Alibaba Cloud Distributed Cloud Container Platform）实现多云云管、资管统一的控制平面。

## 客户场景

### 云原生场景下企业部门分账

#### 场景描述

企业使用云原生上云后，由传统的静态资源供给转换为动态供给，导致业务单元和计费单元不能完全匹配，难以实现各部门之间的成本分摊。

#### 适用客户

- 使用云原生架构的企业客户。
- 使用Namespace划分部门/团队的企业客户。

### 云原生场景下企业业务分账

#### 场景描述

企业对各部门的应用浪费情况要求苛刻，需要掌握应用维度的成本消耗情况。

#### 适用客户

- 使用云原生架构的企业客户。
- 积极使用容器场景下超卖、弹性扩缩、抢占式实例等特性的企业客户。

## 客户案例

### 某互联网金融客户

#### 客户背景

某互联网金融客户X，国内互联网金融行业的领导者。

#### 客户痛点（或客户诉求）

- 业务资源的管理权限分散在各个团队，生产环境和测试环境下沉在业务团队，业务团队常常会为了部署临时业务使用了大量冗余资源。
- 部分业务有明显的周期性，峰谷容量相差较大，造成资源低负载运行时间较长。
- 压测环境单位时间内需要大量的临时机器，复用闲置资源需要腾挪机器、协调跨团队资源，流程和成本较高。
- 缺少可量化的指标发现业务的浪费，单纯的利用率指标不能作为浪费的评判标准。

#### 实施方案

- 通过命名空间进行多租业务的逻辑管理、财资拆分、浪费衡量。
- 全量路压测进行容量预估与可靠性验证。
- 建立成本浪费的衡量标准，发现浪费情况。
- 分时混部在线业务与临时业务错峰使用。
- 定时伸缩实现核心业务资源预供给。
- 闲置资源回收与业务弹性交付。

#### 客户收益

- 经过云成本优化的一系列措施，某业务容器化后，降低了约20%的服务器成本。
- 在进行了混部、业务高峰低谷的弹性伸缩等优化后，平均成本优化率可达约15%。

### 某智能制造客户

#### 客户背景

某智能制造客户X，领先的全球化智能科技公司。

#### 客户痛点（或客户诉求）

- 整体资源利用率较低，成本洞察粒度不足，无法驱动策略优化。
- 业务高速发展，传统容量规划的周期无法满足，影响业务使用。
- 临时作业/突发任务等短周期作业较多，对容量规划带来巨大挑战。
- 业务容量、成本预估困难，缺少数字化指标支撑降本增效。

#### 实施方案

- 先根据应用的具体类型进行分类，选择合适的机型、CPU内存的配置；与业务团队协商业务容量上限，并对业务进行全链路压测确定容量的画像和水位的情况。在压测的过程中，通过容器服务提供的成本分析功能，可以查看检查应用在当前容量规划的方案下的真实利用率；对于存在明显的周期性业务，采用定时伸缩的模型，降低在波谷时的资源成本；调整生产环境和测试环境的超卖比配置，将测试环境的超卖比调整为300%，牺牲一定稳定性提高集群的利用率。
- 定时查看、巡检集群中应用的利用率、资源水位的情况，汇总成本报表；通过云原生企业IT成本治理方案进行集群-部门-应用维度的成本实时预估，让部门可以时刻关注自身成本的趋势变化；开启HPA等自动伸缩策略与报警，保障业务在流量突增的场景的鲁棒性。
- 通过云原生企业IT成本治理方案提供的费用分摊功能，定期将拆分后的成本分析数据推送给事业部IT负责人、部门负责人、业务负责人等不同角色，并建立复盘机制，协同技术、财务、业务团队迭代优化成本画像的合理性。

#### 客户收益

- 通过云原生企业IT成本治理方案，该企业团队可以非常便捷地提供Kubernetes集群中的业务、组织等维度的成本数据，大大提升了部门之间的成本通晒的效率。
- 配合技术、业务、财务“战略同频”的云原生IT成本治理流程，为集团优化了10%闲置的资源，各类业务降低了30%的配额，每年节省近千万的IT成本投入。

## 方案架构

本方案主要介绍了企业如何进行IT成本治理，提供集群、应用、命名空间、节点池四个维度的成本洞察。方案提出了离线账单分析与实时费用估算两种模型相结合的方式进行Pod的费用估算。

方案中，估算一个Pod费用时通过比例拆解的方式折算，计算Pod的费用比例是通过实时费用估算的，通过Pod所在资源的实时费用核时单价乘以Pod运行时长和Pod计费单元（CPU、内存和GPU的申请值大小）来估算出模拟价格，再用单个Pod的模拟价格除以所有Pod的估算价格即可算出一个比较准确的比例。最后再用这个比例乘以这个时间段范围内账单的总价，即可进行比较准确的Pod维度的分摊。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4386581571/p970316.png)

企业在规划集群之初，需要提前规划好集群命名空间规范、各个命名空间内不同K8S资源的标签规范。具体这块可以参考《[容器集群规划方案](https://help.aliyun.com/zh/landing-zone/solution-122)》。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| Prometheus监控 | [Prometheus监控](https://help.aliyun.com/zh/arms/prometheus-monitoring/product-overview/what-is-prometheus)全面对接开源Prometheus生态，支持类型丰富的组件监控，提供多种开箱即用的预置监控大盘，且提供全面托管的Prometheus服务。 | 梯度收费，部分免费。详情参见[计费概述](https://help.aliyun.com/zh/arms/prometheus-monitoring/product-overview/billing-overview-2)。 |
| 容器集群（ACK） | 阿里云容器服务Kubernetes版是全球首批通过Kubernetes一致性认证的服务平台，提供高性能的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理，让您轻松高效地在云端运行Kubernetes容器化应用。 | 收费，详情参见[官网链接](https://help.aliyun.com/zh/ack/billing-information)。 |

## 安全性

### RAM授权策略

ACK成本分析需要用户在集群中授权成本数据的获取。在ACK集群控制台，集群信息,集群资源页面中，单击集群的Worker RAM 角色，如**KubernetesWorkerRole-*****，在**RAM控制台**完成RAM授权策略。

1. 在RAM角色基本信息的**权限管理**页签，单击**权限策略名称**列下的**k8sWorkerRole******。
2. 在**权限策略管理**页面的**策略内容**页签下，单击**修改策略内容**。
3. 在脚本编辑框中修改权限策略内容，增加以下授权规则，修改完成后单击**下一步：编辑基本信息**，然后单击**确定**。`{
 "Action": [
 "bssapi:QueryInstanceBill"
 ],
 "Resource": "*",
 "Effect": "Allow"
},
{
 "Action": [
 "ecs:DescribeDisks",
 "ecs:DescribeSpotPriceHistory",
 "ecs:DescribeInstances",
 "ecs:DescribePrice"
 ],
 "Resource": "*",
 "Effect": "Allow"
}`

## 实施步骤

### 实施准备

- Kubernetes集群的版本为1.18.8及以上，否则请升级集群。具体操作，请参见[升级ACK集群K8s版本](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/update-the-kubernetes-version-of-an-ack-cluster)。
- Kubernetes集群已开启ARMS Prometheus监控。具体操作，请参见[开启ARMS Prometheus监控](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster)。
- Kubernetes集群已安装ack-cost-exporter组件，请参见[开启成本分析功能](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/enable-cost-insights)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：10分钟。

### 操作步骤

#### 步骤一：从集群大盘获取集群总费用

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4386581571/p970310.png)

1. 单击左上角“Cluster”，进入集群大盘。
2. 左上角选择Cost为“Discounted Cost”，显示折后价格。
3. 查看集群费用。Daily Cost为昨日费用，Weekly Cost为上周费用，Monthly Cost为上月费用，Day-on-day Ratio为相对昨日费用的变化比率。当相对昨日费用的变化比率的字体颜色为绿色时，表示相比前一日的成本是降低的。当相对昨日费用的变化比率的字体颜色为红色时，表示相比前一日的成本是增涨的。

1. 查看集群费用趋势。在集群大盘右上角选择计费周期。查看计费周期内集群费用的变化趋势（Cost Trending - Cluster）。查看云产品费用趋势与比例（Cost Trending - Product）。

#### 步骤二：从节点池大盘获取各节点池费用

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4386581571/p970317.png)

1. 单击左上角“Node Pool”，进入节点池大盘。
2. 左上角选择NodePool，选择不同节点池，展示当前节点池费用情况。

#### 步骤三：从命名空间大盘获取部门/业务费用拆分

关于命名空间规范，推荐查看：《[容器集群规划方案](https://help.aliyun.com/zh/landing-zone/solution-122)》。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4386581571/p970318.png)

1. 单击左上角“Namespace”，进入命名空间大盘。
2. 左上角选择具体命名空间。
3. 在大盘右上角选择计量周期。
4. 查看命名空间费用。Cost - NS为命名空间的费用，Cost Radio - Namespace为该费用占集群总费用的比例。
5. 查看命名空间资源使用情况。CPU/Memory Request为分配的资源量，CPU/Memory Usage为真实消耗的资源量，Acutal CPU/Memory Utilization为实际的CPU利用率。
6. 查看命名空间中资源浪费最多的Pod。CPUUtilization为Pod的CPU利用率，MemoryUtilization为Pod的内存利用率，WasteRate为Pod的资源浪费率。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4386581571/p970319.png)

#### 步骤四：从应用大盘获取应用费用拆分

关于K8S资源的Label规范参考：

| 命名组成部分 | 说明 |
| --- | --- |
| **部署环境** | 资源支持的应用对应开发生命周期阶段。 示例：prod、dev、qa、stage、test、ops |
| **应用程序或服务名称** | 资源所属的应用程序或服务的名称。 示例：navigator、buy、tradeplatform |
| **架构层** | 资源在整个架构层面的功能模块示例：fontend、backend、cache |
| **版本标签** | 标识资源所处的版本示例：stable、beta |

企业在规划集群之初，就需要提前规划好各类K8S资源的标签规范。这样有利于按不同应用视角做容器分账。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4386581571/p970311.png)

1. 单击左上角“Application”，进入应用大盘。
2. 坐上脚本选择命名空间，输入LabelSelector。注意：“Key”和“Value”之间使用英文冒号相连。
3. 在应用大盘右上角选择计费周期。
4. 查看应用费用。Cost为计费周期内的费用，Cost Per Core*Hour为每核时的单位价格。
5. 查看应用资源使用情况。Pod Num包括该应用峰/谷值的副本数，Utilization为CPU和内存的利用率，Uptime是应用的运行时间，Core*Hour是应用总消耗的核时资源数，Utilization Statistic是应用占整个集群/命名空间的资源利用率。
6. 查看应用内每个Pod的成本和资源信息。Utilization为Pod的CPU和内存的利用率，Cost Per Core*Hour为Pod每核时的单位价格，Cost Evaluation为Pod的费用，Core*Hours是Pod总消耗的核时资源数，Uptime是Pod的运行时间。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4386581571/p970320.png)

## 故障排除

### 为什么开启成本可视化后没有数据显示？

检查RAM角色授权操作已完成。具体操作，参考开启成本分析功能的步骤5。 成本分析需要集群的监控数据和费用数据，监控数据在开启后3 min内即可开始采集，费用相关的数据需要从集群开启成本分析后的第二天08: 00才有数据显示。

### 为什么命名空间的费用相加与实际的费用账单不相等？

命名空间的费用是通过成本估算来进行核算的，并非直接通过账单分析得出。因此，在做费用估算的时候，是通过目录价进行计算的，当集群的花费包含代金券、折扣、节约计划等抵扣策略的时候，会出现一定的数据偏差。但是，可以通过命名空间的比例乘以集群的总费用进行费用的分账。

### 为什么有些节点上的Pod数据无法获取成本数据？

检查RAM角色授权操作已完成，并确认授权策略中包含"ecs:DescribeDisks"权限。具体操作，参考[开启成本分析功能](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/enable-cost-insights)。

### 如何查看空余资源的费用使用情况？

首先集群除去各namespace分摊的成本比例后，剩余空闲未分配的资源（idle）的成本比例，可以在这里看出：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4386581571/p970322.png)

## 相关内容

- [托管与专有容器集群ACK成本分析概述](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/cost-insights-1/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-117（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
