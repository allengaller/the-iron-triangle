<!-- source: https://help.aliyun.com/zh/well-architected/solution-280 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929429 -->

# 面向ACK容器客户的全量账单分账方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6386581571/p972309.png)

在阿里云平台上，企业通常基于财务单元将云资源账单分摊到各个成本中心，以此实现通用的成本分摊方案。然而，由于部分产品的分摊逻辑较为复杂，其分账策略无法与其他产品完全打通。例如，ACK容器服务需要依赖成本套件来进行分账，而网络资源则依赖财务单元进行分账。这种差异化的分账机制可能导致平台层面生成一套分摊账单，而在具体产品层面又存在另一套独立的分摊账单，增加了对账和管理的复杂性。

本文档介绍了一种通过MaxCompute聚合ACK分账数据与平台分账数据的方法，旨在解决这一问题，实现更统一、更清晰的成本分摊视图。

## 方案优势

### 云账单集中分析

通过统一的成本分析面板，整合ACK容器服务与平台现有的成本拆分逻辑，实现对云上所有产品成本中心的集中化查看与管理。这一方案不仅能够有效聚合分散的分账数据，还为企业提供了全局视角下的成本分布视图，助力更高效的成本分析与决策。同时，统一的面板设计显著降低了多套分账逻辑并存带来的复杂性，提升了财务管理的透明度与一致性。

## 客户场景

### 云原生场景下企业部门分账

#### 场景描述

企业使用云原生上云后，由传统的静态资源供给转换为动态供给，导致业务单元和计费单元不能完全匹配，难以实现各部门之间的成本分摊。

#### 适用客户

- 使用云原生架构的企业客户。
- 使用Namespace划分部门/团队的企业客户。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| Prometheus监控 | [Prometheus监控](https://help.aliyun.com/zh/arms/prometheus-monitoring/product-overview/what-is-prometheus)全面对接开源Prometheus生态，支持类型丰富的组件监控，提供多种开箱即用的预置监控大盘，且提供全面托管的Prometheus服务。 | 梯度收费，部分免费。详情参见[计费概述](https://help.aliyun.com/zh/arms/prometheus-monitoring/product-overview/billing-overview-2)。 |
| 容器集群（ACK） | 阿里云容器服务Kubernetes版是全球首批通过Kubernetes一致性认证的服务平台，提供高性能的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理，让您轻松高效地在云端运行Kubernetes容器化应用。 | 收费，详情参见[官网链接](https://help.aliyun.com/zh/ack/billing-information)。 |
| Maxcompute | [MaxCompute](https://help.aliyun.com/zh/maxcompute/user-guide/what-is-maxcompute)是适用于数据分析场景的企业级SaaS（Software as a Service）模式云数据仓库，以Serverless架构提供快速、全托管的在线数据仓库服务，消除了传统数据平台在资源扩展性和弹性方面的限制，最小化用户运维投入，使您可以经济并高效地分析处理海量数据。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/maxcompute/overview-31)。 |
| 智能商业分析 Quick BI | [Quick BI](https://help.aliyun.com/zh/quick-bi/product-overview/introduction-to-quick-bi-1)——阿里云旗下产品，大数据的高效分析与展现平台。通过对数据源的连接，和数据集的创建，可对数据进行即时分析与查询。并通过电子表格或仪表板功能，以拖拽的方式进行数据的可视化呈现。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/quick-bi/product-overview/billing-methods-of-quick-bi)。 |

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

## 注意事项

### 账单数据延时

- 开通订阅成功之后，表结构在Maxcompute空间中立即可见，但是数据要等第2天才会推送；
- 可以订阅历史周期的数据，数据推送第2天推送；
- 订阅成功之后，数据每天下午18点前完成前一天的数据推送；

## 实施步骤

### 实施准备

1. 客户需要开通Maxcompute订阅账单（同步会开通Maxcompute、Dataworks 产品）；
2. 如若界面化呈现，客户需要购买QuickBI 高级版；
3. 需要开通ack成本分析套件；

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：90分钟。

### 操作步骤

#### 1. 容器财务单元规则数据处理

##### 1.1. 下载财务单元结构数据

费用中心的财务单元结构数据主要用来定义财务账单结构的一致性

操作路径：费用与成本--成本--成本分摊--财务单元--总览（[链接地址](https://billing-cost.console.aliyun.com/finance/finance-unit/list)）

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6386581571/p972307.png)

建议打开 金额按财务单元层级汇总 功能，这样可以获得在费用中心更完整的财务单元配置数据。

获取的结构样式如下：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6386581571/p972308.png)

只保留财务单元名称字段在excel数据表类似如下：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6386581571/p972310.png)

##### 1.2. 处理容器财务单元规则数据

通过excel处理成如下格式：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6386581571/p972311.png)

样例excel：

- B、C、D、E分别为规则列，同一行中这几列的值不为空时，关系是and的关系。比如 ClusterID为NULL，Namespace为 space1 ， LabelKey:LabelValue值为 key1: ，含义为：pod 的所有集群，Namespace=space1 并且 LabelKey=key1 的所有账单数据；
- 每列的值为多个时，用英文分号分隔；
- 当要把账单分拆到费用中心不存在的财务单元时，直接添加财务单元名称并编制对应的规则；

##### 1.3. 把处理好的容器财务单元规则数据上传到Maxcompute

操作路径：数据准备--数据上传，[链接](https://maxcompute.console.aliyun.com/cn-shanghai/data/upload)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6386581571/p972312.png)

- 把1.2中处理好的excel拖动到选择文件的地方；
- 选择项目名称：建议直接选择阿里云订阅账单直接存放的项目空间内；
- 目标表：选择新建表，因为本次是第一次上传容器的财务单元规则数据；
- 表名：固定为 cost_unit_rule，后面操作手册中会使用该表，如果名字不一样，需要替换；
- 表类型：选择非分区表，因为规则数据量不大，不用做分区；
- 生命周期：永久，数据量不大，又为规则数据，要一直使用，选择永久比较合适；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6386581571/p972314.png)

预览数据无问题后，点击上传

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6386581571/p972316.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6386581571/p972318.png)

规则表就完成了

#### 2. 集群资源账单分拆到Pod粒度

##### 2.1. 把Pod拆分比例同步到Maxcompute

1. 先建立一张表到 cost_mgt_xxx项目中，创建表sql如下：`CREATE TABLE PodUsage (
 Pod VARCHAR(255) NOT NULL,
 `Start` DATETIME NOT NULL,
 `End` DATETIME NOT NULL,
 Cost DECIMAL(10, 2) NOT NULL,
 CostRatio DECIMAL(5, 2) NOT NULL,
 Controller VARCHAR(255),
 ControllerKind VARCHAR(50),
 Node VARCHAR(255),
 NameSpace VARCHAR(255),
 ProviderId VARCHAR(255),
 Labels TEXT,
 CpuCoreUsageAverage DECIMAL(10, 2),
 RamByteUsageAverage BIGINT,
 Cluster VARCHAR(255),
 PRIMARY KEY (Pod, `Start`, `End`) -- Assuming Pod with its start and end time as unique identifier
);`
2. 通过tunnelSDK的方式，把pod拆分比例同步到Maxcompute中；tunnelSDK的逻辑有如下两种集群的空闲部分作为单独的一行：获取如下接口的数据：[接口链接](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/call-the-cost-v2-api-to-query-cost-data)；接口入参：window：每个小时的起始时间，如：2024-03-26T10:00:00Z,2024-03-26T11:00:00Z返回数据参考：PodStartEndCostCostRatioControllerControllerKindNodeProviderIdLabelsCpuCoreUsageAverageRamByteUsageAverageClusterkube-system/node-local-dns-zzqf22024-12-19T15:15:40+08:002024-12-19T16:15:40+08:000.0070.000739node-local-dnsdaemonsetap-southeast-1.10.119.37.14ap-southeast-1.i-t4nbqhs6ulfzd76ru54w{"controller_revision_hash":"65bcb447b8","k8s_app":"node-local-dns","pod_template_generation":"1"}0.00443507712c192bc09387d44475a06dc1ef9532ab20kube-system/terway-eniip-z5tp72024-12-19T15:15:40+08:002024-12-19T16:15:40+08:000.1090.011514terway-eniipdaemonsetap-southeast-1.10.119.37.14ap-southeast-1.i-t4nbqhs6ulfzd76ru54w{"app":"terway-eniip","controller_revision_hash":"5847545467","pod_template_generation":"1"}0.002115678549.3c192bc09387d44475a06dc1ef9532ab20kube-system/kube-proxy-worker-sx4n52024-12-19T15:15:40+08:002024-12-19T16:15:40+08:000.0310.003275kube-proxy-workerdaemonsetap-southeast-1.10.103.113.127ap-southeast-1.i-t4nizfun1k5v1dagljti{"controller_revision_hash":"f9cc878f9","k8s_app":"kube-proxy-worker","pod_template_generation":"1"}0.013141806250.7c192bc09387d44475a06dc1ef9532ab20集群的空闲的比例按每个pod占比权重分拆到每个pod：获取如下接口的数据：[接口链接](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/call-the-cost-v2-api-to-query-cost-data)；接口入参：window：每个小时的起始时间，如：2024-03-26T10:00:00Z,2024-03-26T11:00:00ZshareIdle：true返回数据参考：PodStartEndCostCostRatioControllerControllerKindNodeProviderIdLabelsCpuCoreUsageAverageRamByteUsageAverageClusterkube-system/node-local-dns-zzqf22024-12-19T15:15:40+08:002024-12-19T16:15:40+08:000.0070.000739node-local-dnsdaemonsetap-southeast-1.10.119.37.14ap-southeast-1.i-t4nbqhs6ulfzd76ru54w{"controller_revision_hash":"65bcb447b8","k8s_app":"node-local-dns","pod_template_generation":"1"}0.00443507712c192bc09387d44475a06dc1ef9532ab20kube-system/terway-eniip-z5tp72024-12-19T15:15:40+08:002024-12-19T16:15:40+08:000.1090.011514terway-eniipdaemonsetap-southeast-1.10.119.37.14ap-southeast-1.i-t4nbqhs6ulfzd76ru54w{"app":"terway-eniip","controller_revision_hash":"5847545467","pod_template_generation":"1"}0.002115678549.3c192bc09387d44475a06dc1ef9532ab20kube-system/kube-proxy-worker-sx4n52024-12-19T15:15:40+08:002024-12-19T16:15:40+08:000.0310.003275kube-proxy-workerdaemonsetap-southeast-1.10.103.113.127ap-southeast-1.i-t4nizfun1k5v1dagljti{"controller_revision_hash":"f9cc878f9","k8s_app":"kube-proxy-worker","pod_template_generation":"1"}0.013141806250.7c192bc09387d44475a06dc1ef9532ab20

##### 2.2. 把集群账单拆分到pod粒度

拆分逻辑如下：

1. 先从cost_mgt_xxx项目中 找到表：split_item_detail_for_billing_period （分账账单明细表）；
2. 根据条件 instance_tag like '%ack.aliyun.com%' 筛选出容器集群的分账账单数据，此数据为A，该表中剩余的数据即为非容器集群的账单数据，数据为B；
3. 根据A的数据，加工集群ID字段（cluster_ID），加工逻辑为 把 instance_tag 中 key='ack.aliyun.com' 的value值，为集群ID字段的值；
4. 根据加工好的A数据，使用2.1中上传好的Pod拆分比例表进行拆分，拆分所有的金额字段（portfolio_discount、unit_convert_flowpack_deduct、ri_deduct_quantity、original_amount、discount_amount、coupon_pay_amount、require_amount、adjust_amount），并新增如下字段，split_podID、split_podName、nameSpace、controller、controller_kind、Node、pod_labels,这几个字段的取值是从Pod拆分比例表中直接获取后拼接到A表中，主要作用是为了将来排查问题方便；注意：在把集群分账账单拆分为pod粒度账单时，最后一条pod粒度账单的所有金额字段，要用减法实现，否则会出现分拆完的金额和原始分账账单金额不一致的问题；减法逻辑为：比如应付金额，集群+ecs实例1 的应付金额=1元，要把这1元拆到3个pod上，拆分比例分别为0.33,0.33,0.34,前面两条的拆分逻辑为1元*拆分比例，最后一条的应付金额逻辑为：1元-前两条的应付金额的拆分金额=0.34元；A中的账单按集群拉；
5. 把A数据中的财务单元字段全部置为NULL;
6. 以上拆分好的数据即为pod粒度的集群账单；

#### 3. 按财务单元规则处理分账获得财务单元纬度的分账账单

##### 3.1. 按容器财务单元规则，把Pod粒度的账单按容器财务单元规则归属

目标：根据2拆分好的pod粒度的分账账单，按照1中上传的财务单元规则开始按规则顺序把Pod粒度的分账账单明细归属到规则对应的财务单元数据中；

处理逻辑如下：

1. 把1中上传的财务单元规则，按RulePriorityNum 从小到大开始排序；
2. 排序好的财务单元规则，按规则顺序到pod粒度的分账账单中，找对应的账单数据，找到之后，重写财务单元字段到pod粒度的分账账单中；
3. 遍历完财务单元规则之后，若还存在未分配的pod粒度的分账账单，则针对这部分数据重写财务单元字段为 未分配；
4. 此数据即为容器集群部分的财务单元纬度的分账账单；

##### 3.2. 合并容器集群的分账数据和非容器集群的分账数据，形成一张全量消费账单的分账数据

目标：合并非容器集群数据和容器集群数据到一张表；

处理逻辑：

1. 根据2.2 中分拆的B数据（非容器集群的分账数据），针对B数据，增加字段：split_podID、split_podName、nameSpace、controller、controller_kind、Node、pod_labels、cluster_ID，这些字段的值为NULL；
2. 拼接B表数据和3.1中的数据，获得全量消费账单的分账数据；

#### 4. 可视化分析分账结果

**使用QuickBI模版分析分账数据**

参考文档：[云上自助成本分析方案](https://help.aliyun.com/zh/well-architected/solution-273)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-280（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
