<!-- source: https://help.aliyun.com/zh/well-architected/solution-222 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929435 -->

# 云上资源成本分摊方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972394.png)

无论企业业务处在稳定运行还是快速发展阶段，企业内管理层对于云上企业关注的核心指标之一就是用云成本。不仅需要了解整体的云上成本情况，也需要知道基于业务粒度、环境粒度的云上成本情况。当业务在不断增长时，才能够快速了解云上费用增加是否在合理的比例，从而能够向企业管理层汇报云上资源对于业务发展的支持情况。

本文档则介绍了如何对于云上资源进行成本分摊，指导客户组合使用不同产品和不同分摊方式。

## 方案优势

### 简化成本分摊方式

根据业务资源情况可以将业务使用实例和公用资源通过费用标签、组件进行标记，通过财务单元可以进行业务成本的归集，在分账账单中呈现业务分摊账单。

## 客户场景

### 应对企业内成本管理要求

#### 场景描述

企业上云之后，随着上云业务增加以及企业业务发展，云上成本出现快速成长的情况。企业管理层无法判断什么因素导致了云上成本增加，需要分摊成更细粒度的业务成本、应用成本、环境成本进行分析。

#### 适用客户

- 大规模用云的客户
- 多个业务在单个阿里云账号运行的客户
- 对于用云成本敏感的客户

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972393.png)

阿里云上产品种类很多，不同产品服务形态、计费方式都存在较大的差异性。根据成本分摊的准确度可以把阿里云上的成本分摊方案分为细粒度分摊和粗粒度分摊。

- 细粒度分摊：成本分摊方式主要由云原生产品或者阿里云平台提供，可以基于实例将成本精确分摊到具体业务。
- 粗粒度分摊：成本分摊方式需要客户基于非计费数据确定比例，由于部分产品的计费方式无法根据实例进行拆分，所以需要客户根据业务用量、规模计算敲定合适的拆分比例。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 标签Tag | [标签（Tag）](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview)是云资源的标识，可以帮助您从不同维度对具有相同特征的云资源进行分类、搜索和聚合，让资源管理变得更加轻松。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 财务单元 | [财务单元](https://help.aliyun.com/zh/user-center/cost-center-overview)是用户对费用进行归类的单位，支持所有费用可分配，且可以根据组织需要自定义层级结构。可以在财务单元中建立自己的费用分组，在账单明细中查看每个财务单元的费用明细和统计。 | 免费 |
| 分账账单 | [分账账单](https://help.aliyun.com/zh/user-center/splitting-bill)是指客户将总费用基于某种视角划分为更细粒度，分账账单展示拆分后更细粒度的账单。费用的分账需要依赖财务单元、费用标签等功能，财务单元和费用标签的设置需参考财务单元与费用标签的介绍文档。 | 免费 |

## 安全性

### 费用中心RAM策略

阿里云费用中心接入RAM访问控制，提供基于RAM的权限策略控制，详情参见[费用中心RAM策略介绍](https://help.aliyun.com/zh/user-center/ram-policies-for-billing-management)。

## 注意事项

### 支持费用标签的云服务

阿里云费用标签服务已经支持一系列核心基础设施，例如：云服务器ECS、 云数据库RDS、对象存储OSS、专有网络VPC、负载均衡和容器服务Kubernetes版等。在此基础上，标签服务也在不断扩展对其他云服务的支持。更多信息，请参见[支持标签的云服务](https://help.aliyun.com/zh/resource-management/tag/product-overview/services-that-work-with-tag)。

### 分账账单支持分拆的云服务

对于云产品的出账粒度不等于资源管理粒度的云产品，分账账单中专门预留了账单分拆项ID作为成本分拆依据。目前支持的云服务信息，请参见[分账账单支持的云服务](https://help.aliyun.com/zh/user-center/splitting-bill)

## 实施步骤

### 实施准备

1. 梳理企业上云的组织架构
2. 梳理企业云上的成本规划，比如不同团队人员之间的成本权责、云上成本的分摊规则
3. 基于云上成本的分摊规则，做好费用标签规划
4. 在[成本分析](https://usercenter2.aliyun.com/expense-manage/expense-analyze)按照费用从高到低对阿里云产品进行排序，按照产品区分优先级。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972395.png)

### 实施规划

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972396.png)

本次实施重点演示不同成本分摊方式的操作步骤，包括费用标签、云原生组件、固定比例、用量比例。分别以ACK、SLS、资源包、云安全中心作为示例产品，将四款产品拆分到客户的电商、官网、IT三个业务团队成本中。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：2小时。

### 操作步骤

#### 设置财务单元

进入[财务单元](https://usercenter2.aliyun.com/finance/finance-unit/list)根据企业云上成本单元，创建企业需要的财务单元

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972397.png)

#### 成本分摊操作

##### 云原生组件（ACK 成本套件）

目前仅有容器集群产品提供了云原生成本套件。

1. 一个Kubernetes下所有的云资源都会通过默认的集群ID（ack.aliyun.com:cluster-id-A）作为系统标签自动打标。
2. 需要在[阿里云用户中心费用标签页面](https://usercenter2.aliyun.com/finance/tags)按照页面提示开启ack.aliyun.com标签和ack.alibabacloud.com/nodepool-id标签的分析统计功能。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972398.png)容器集群产品更细粒度基于命名空间、节点池、应用的成本分摊情况需要进入ACK 成本套件开启成本洞察功能查看
3. 在财务单元中设置自动分配规则，绑定标签ack.aliyun.com![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972400.png)

##### 费用标签/资源组

**通过费用标签分账**

1. 在[资源管理](https://resourcemanager.console.aliyun.com/tags?regionId=cn-hangzhou&route=tagList&tab=functions)中查看SLS产品是否支持费用标签![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972399.png)
2. 对SLS project进行打标操作方式1：在SLS产品界面中选择对应的project进行打标方式2：在[资源管理](https://resourcemanager.console.aliyun.com/metatags)的标签页中绑定资源
3. 确认[费用标签](https://usercenter2.aliyun.com/finance/tags)功能处在打开状态![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972403.png)
4. 在财务单元中设置自动分配规则，绑定费用标签

**通过资源组分账**

1. 查看[支持资源组的云服务](https://help.aliyun.com/zh/resource-management/product-overview/services-that-work-with-resource-group?spm=a2c4g.11186623.0.i98)是否包含SLS产品
2. 为SLS project分配资源组方式1：在SLS project创建时指定资源组方式2：在SLS产品界面中选择对应的project设置资源组
3. 在财务单元中设置自动分配规则，绑定资源组![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972401.png)

##### 固定比例

阿里云上存在一些共享型的产品，无法按照业务进行明确的资源管理划分。这类云产品的明细账单出账粒度太粗，一般不满足企业内部管理需求。比较典型的就是云安全产品，如需要对这类产品进行成本拆分，建议可以以某一项全年费用各业务的比例，通过财务单元进行固定比例拆分。比如以云安全中心为例，云安全中心核心成本是基础服务费用，按照服务的ECS/容器数量进行收费。

1. 在[成本分析](https://usercenter2.aliyun.com/expense-manage/expense-analyze)中时间粒度选择1年时间，产品项筛选出“云服务器ECS”、“容器镜像服务”，分类维度选择“财务单元”![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972402.png)
2. 根据1年内财务单元的合计，计算出在服务器上各个业务之间的成本比例。
3. 在[财务单元](https://usercenter2.aliyun.com/finance/finance-unit/list)中新增一个“云安全中心”单元，绑定云安全中心产品费用。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972406.png)
4. 进入财务单元--总览页面，编辑公摊费用拆分规则![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972404.png)
5. 根据计算出的比例情况，设置各个目标业务财务单元分摊的比例![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972405.png)

##### 用量比例

云产品的出账粒度不等于资源管理粒度的云产品，这类云产品的明细账单出账粒度太粗，一般不满足企业内部管理需求。比如共享带宽产品，明细账单的粒度是带宽包，但是资源管理粒度是eip。

**a. 共享带宽包（预付费）**

1. 进入[用量明细](https://usercenter2.aliyun.com/finance/usage)，产品选择“弹性公网IP”，导出csv
2. 在CSV筛选出共享带宽绑定的IP，在本地分拆

**b. 共享带宽包（后付费）**

1. 进入[分账账单](https://usercenter2.aliyun.com/finance/split-bill)，产品筛选共享带宽包以及共享带宽包实例ID![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972407.png)
2. 点击右上角导出账单CSV，根据分拆项ID在本地分拆

#### 成本分摊报告配置

1. 进入[成本分析](https://usercenter2.aliyun.com/expense-manage/expense-analyze?groupTypeList%5B0%5D%5Bcode%5D=UNIT&groupTypeList%5B0%5D%5Btype%5D=dimensions&metrics=REQUIRE_AMOUNT&periodType=DAY&startPeriod=1706716800000&endPeriod=1709222399999&chartType=LINE)页面，分类维度选择“财务单元”，筛选条件选择目标业务财务单元![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972410.png)
2. 点击保存为报告，如业务分摊![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972408.png)
3. 后续查看报告可以直接在成本分析界面切换到对应的报告![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2386581571/p972409.png)

## 产品支持说明

| 类型 | 产品 | 云原生组件 | 标签/资源组 | 用量比例 | 固定比例 |
| --- | --- | --- | --- | --- | --- |
| 网络 | CEN |  |  |  | ✓ |
| NAT |  | ✓ |  | ✓ |  |
| 共享带宽包 |  |  | ✓ | ✓ |  |
| CDN |  |  | ✓ | ✓ |  |
| 存储 | OSS |  | ✓ | ✓ | ✓ |
| SLS |  | ✓ |  | ✓ |  |
| 容器 | ACK | ✓ | ✓ |  | ✓ |
| 安全 | 堡垒机 |  |  |  | ✓ |
| WAF |  |  |  | ✓ |  |
| 云防火墙 |  |  |  | ✓ |  |
| DDoS |  |  |  | ✓ |  |
| 计算 | 资源包 |  |  | ✓ | ✓ |
| 快照 |  | ✓ | ✓ | ✓ |  |
| 大数据 | Dataworks |  |  |  | ✓ |
| hologres |  | ✓ |  | ✓ |  |
| Elasticsearch |  | ✓ |  | ✓ |  |
| MaxCompute |  | ✓ |  | ✓ |  |
| PAI |  | ✓ |  | ✓ |  |
| 其他 | 短信 |  | ✓ | ✓ | ✓ |

## 故障排除

### 成本分析中为什么看不到资源费用？

- 成本分析自开通后延迟48小时可使用，其中预测数据仅供参考，支持查看近12个月数据。
- 当月数据在明细账单出具后延迟48小时更新，当月最终数据在次月4日12点后支持查看（月中会发生包括但不限于以下少数场景：延迟出账、退款、调账、欠费核销等）。
- 当月数据中不包含未结算（未出账，累账中）的后付费数据。

### 分账账单数据为什么看不到分拆型云产品？

- 分账账单数据相对于实际费用消耗延迟48小时更新，其中分拆型云产品（例如：CDN、OSS、共享带宽等）各个分拆项（例如：域名、Bucket、EIP等）的具体费用延迟72小时更新。

## 相关内容

[分账账单](https://help.aliyun.com/zh/user-center/splitting-bill)

[财务单元](https://help.aliyun.com/zh/user-center/user-guide/cost-center?spm=a2c4g.11186623.0.0.59f174e0YTryRa)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-222（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
