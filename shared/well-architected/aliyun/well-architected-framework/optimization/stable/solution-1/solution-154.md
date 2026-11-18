<!-- source: https://help.aliyun.com/zh/well-architected/solution-154 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929427 -->

# 多账号全栈可观测大盘方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976581571/p972225.png)

可观测性指依据系统外部输出推断及衡量系统内部状态。通过建设可观测性平台，高效全面的收集系统运行状态数据，在此基础上将系统各个维度的指标统一展示，能够快速发现当前系统存在的风险。

本方案介绍基于Prometheus + Grafana + Arms应用监控 + SLS 构建覆盖应用全栈的统一可观测大盘，帮助客户基于Grafana来配置多账号全栈可观测大盘。

## 方案优势

### 使用阿里云丰富的开箱即用的产品能力

相比于通过开源组件自建监控体系，本方案使用阿里云成熟产品提供包括默认大盘、数据采集等功能，可以快速构建一套成熟的生产环境。

### 支持跨账号场景的数据聚合和可观测

对于使用多账号的企业客户来说，如何将多个账号内的数据打通实现统一聚合展示非常关键。本方案也提供了一种打通多个账号的数据源，实现综合可观测实践。

### 支持按部门团队确定权限范围

Grafana服务提供3种权限管理方式，来应对大型企业在权限管理的诉求。

## 客户场景

### 多账号指标统一可观测

#### 场景描述

为了获知系统的整体状态，需要从每个组件收集指标。同时还需要知道历史状态、在时间区间里状态是如何变化的。为了达到这个目的，就意味着需要不断地从组件中收集状态数据。一旦有了这些指标数据，就可以构建内容丰富的仪表盘视图了，比如Grafana大盘。

常见的指标包括：云服务、PaaS组件指标、应用性能指标、容器指标及业务指标等。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976581571/p972223.png)

#### 适用客户

- 通过指标进行可观测性的客户。
- 使用多个阿里云账号的企业客户。

### 多账号日志统一可观测

#### 场景描述

阿里云的日志服务可以收集各账号内系统日志（如硬件、操作系统日志），业务日志（如页面PV/UV等），云网络流量日志（VPCFlow日志），云产品日志（安全WAF日志、数据库日志等）。同时日志服务提供了日志存储、加工、检索、与复杂分析能力，可以基于客户的实际需求切割出不同的业务指标。

#### 适用客户

- 基于日志进行分析的企业客户。
- 使用多个阿里云账号的企业客户。

### 多账号资源巡检展示结果

#### 场景描述

阿里云的配置审计产品支持对多账号的资源进行巡检，识别风险。有些企业希望将资源的风险巡检结果也能够统一汇聚到Grafana大盘来展现。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976581571/p972224.png)

#### 适用客户

- 使用配置审计，并且希望将巡检结果放到Grafana大盘展示
- 使用多个阿里云账号的企业客户。

## 方案架构

### 统一可观测大盘方案

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976581571/p972226.png)

#### 可观测架构分层

从可观测的角度来看，系统架构可以粗略分为4个层次。自下而上分别是：系统层、中间件层、应用层、用户业务层。每层可以使用指标、链路、日志等可观测性方式进行监控。也可以将每一层的可观测指标数据汇聚到同一个Grafana大盘进行展示。

- **系统层可观测性**：这块主要依赖云监控，包含关键的云服务如ECS、RDS、SLB等，针对各个服务提供可用性和性能的各关键指标。
- **容器性能层可观测性**：指基于容器服务ACK构建系统的容器抽象层的可观测场景，包括集群的性能、事件等监控，容器的性能，以及容器组件等监控。
- **应用性能层可观测性**：指基于容器服务ACK构建系统的具体应用场景，包括应用指标性能（Metric）、系统调用链（Tracing）、日志监控（Logging）等，例如基于容器服务构建一个Java应用，JAVA应用的线程数指标等。
- **用户业务层可观测性：**基于容器服务ACK构建的业务系统的具体业务场景，例如基于容器服务构建一套高可用可扩展的网站，网站的业务运营数据PV、UV等，例如应用的成本审计场景等。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976581571/p972227.png)

### 多账号统一可观测架构

将各账号下的可观测数据通过Prometheus的GlobalView和Grafana来统一可视化。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976581571/p972229.png)

方案中包含3个账号

- 业务账号A：业务A拥有的账号，运行A业务所需要的云资源，包括ECS，SLB，ACK，RDS等，承担A业务所需的可观测费用支出。
- 业务账号B：业务B所拥有的账号。
- 运维账号C：由Cloud Admin部门所拥有的账号，负责统一的监控运维、应用CI/CD等。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| ARMS | [ARMS](https://help.aliyun.com/product/34364.html) Prometheus监控全面对接开源Prometheus生态，支持类型丰富的组件监控，提供多种开箱即用的预置监控大盘，且提供全面托管的Prometheus服务。借助ARMS Prometheus监控，用户无需自行搭建Prometheus监控系统，因而无需关心底层数据存储、数据展示、系统运维等问题。 | 收费，详情参见[产品计费](https://www.aliyun.com/ntms/price/detail/arms_detail) |
| 云监控 | [云监控](https://help.aliyun.com/product/28572.html)（CloudMonitor） 是一项针对阿里云资源和互联网应用进行监控的服务。云监控服务可用于收集获取阿里云资源的监控指标，探测互联网服务可用性，以及针对指标设置警报。 | 部分功能免费，高级功能收费。具体可以查看[产品计费](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/billing-overview)。 |
| 日志服务 | [日志服务](https://help.aliyun.com/product/28958.html)（SLS）是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[产品计费](https://www.aliyun.com/price/detail/sls) |
| 配置审计（Config） | 配置审计（Cloud Config）是一项资源审计服务，为您提供面向资源的配置历史追踪、配置合规审计等能力。面对大量资源，帮您轻松实现基础设施的自主监管，确保持续性合规。 | 配置审计产品本身免费，详情参见[产品计费](https://help.aliyun.com/zh/document_detail/133951.html) |

## 安全性

### ARMS访问控制

借助访问控制RAM的RAM用户，您可以实现权限分割的目的，按需为RAM用户赋予不同权限，并避免因暴露阿里云账号密钥造成的安全风险。具体可以参考[官网文档](https://help.aliyun.com/zh/arms/security-and-compliance/overview-8)。

### Grafana身份安全

Grafana中存在多种结构用于组织资源和权限，当公司存在多个团队、部门或客户需要服务时，需要考虑如下场景的身份安全问题：

- 部门A不应该看到部门B的信息，该如何分配账号并管理权限。
- 不同部门对身份验证、插件等有很大不同，如何配置隔离。
- 当需要对客户展示公共内容时如何使用户免鉴权查看。

具体可以参考[官网文档](https://help.aliyun.com/zh/arms/observable-visualization-grafana-edition/organize-resources-and-manage-permissions-in-grafana)。

### 多账号管控策略

通过多账号管控策略可以限制成员账号内的RAM用户去配置监控大盘。这样就可以收敛各个账号内的用户统一到指定运维账号中进行查看。

关于管控策略，可以参考产品[官网文档](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)。

## 注意事项

### Grafana登录问题

拥有Admin权限的账号不具备直接创建账号的能力，只有Admin账号可以直接创建账号。Admin账号登录方式：

- 使用Admin账号和创建工作区时设置的Admin密码登录Grafana。如果忘记密码，您可以在控制台的**账号管理**页面重置Admin密码。
- 登录创建工作区的阿里云账号（主账号），然后在Grafana登录页单击**Sign in with Alibaba Cloud**直接使用当前阿里云账号登录Grafana。

### 费用分摊

对于多账号企业来说，通过将各业务部署在相应的账号下，可以很方便地将成本归属到不同账号。对于运维账号内的Grafana工作区的费用，可以通过LandingZone中按比例分摊到不同的业务团队。

### 权限管理

各业务账号可以且只有本业务部门的可观测数据读写权限， 而运维账号拥有所有业务部门的查看权限。具体可以参考[官网文档](https://help.aliyun.com/zh/arms/observable-visualization-grafana-edition/organize-resources-and-manage-permissions-in-grafana)。

## 实施步骤

### 实施准备

已经按照LandingZone的多账号标准架构实施完成多账号环境。对应演示的多账号架构环境如下：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976581571/p972230.png)

本方案会在运维账号内创建统一观测大盘，将账号A、账号B及全局的审计结果汇聚展示。相关账号说明：

- 管理账号：会在这个账号内开启多账号的配置审计，并且将不合规事件及资源投递到日志账号中的日志服务（SLS）
- 日志账号：会在这个账号内开启日志服务，用于接收不合规资源事件及账号A、账号B内的业务日志
- 运维账号：会在这个账号内创建Grafana大盘，并将账号A、账号B内的指标数据及日志账号的日志数据统一展示
- 业务账号：开通企业云监控及ARMS实例，用于采集云服务指标。配置跨账号的日志投递，将业务日志投递到日志账号内。
- 使用企业管理员或企业管理员的拥有管理员权限的RAM角色调用[OpenAPI](https://next.api.aliyun.com/api/ResourceDirectoryMaster/2022-04-19/RegisterDelegatedAdministrator?sdkStyle=old)，为想要创建跨账号GlobalVIew实例的成员（本方案中请选择运维账号）设置可信服务的委派管理员角色，其参数及说明如下：服务地址：中国内地选择华东2（上海），国外选择新加坡。AccountId：填写需要创建跨账号GlobalVIew实例的成员用户ID（本方案中选择运维账号）。ServicePrincipal：填写**prometheus.aliyuncs.com**。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长60分钟。

### 场景规划

本文会列举常见的几个场景来介绍实施步骤

- 场景1：云服务指标统一可观测
- 场景2：资源巡检结果统一可观测展示

#### 场景1：云服务指标可观测

##### 业务账号云服务监控

业务账号下的基础云服务的监控数据，包括ECS，SLB，RDS等，通过Prometheus监控中云服务监控，采集到各自账号下的Prometheus实例。

登录业务账号A、B里面完成云服务监控配置。具体可以参考[产品文档](https://help.aliyun.com/zh/arms/prometheus-monitoring/create-prometheus-instances-to-monitor-alibaba-cloud-services)

##### 统一监控数据

在运维账号下创建如下globalview实例

- 云服务监控，通过globalview中资源目录的集成，加入业务账号A和B中的Prometheus云服务监控实例，统一管理云服务监控相关的大盘。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976581571/p972231.png)参数说明：全局聚合实例名称：填写企业易识别的实例名选择聚合的实例：选择资源目录里面相应成员账号及相关实例

具体可以参考[产品文档](https://help.aliyun.com/zh/arms/prometheus-monitoring/create-global-aggregation-instance-across-alibaba-cloud-accounts)

##### 统一数据可视化

在运维账号下创建grafana工作区，配置与Prometheus集成。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976581571/p972232.png)

登录grafana，可以看到已经内置了云服务的Dashboard

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976581571/p972233.png)

#### 场景2：资源巡检结果统一可观测展示

#### 开启多账号配置审计

首先在企业管理账号中完成配置审计的开通与配置

##### 新建全局账号组

1. 登录[配置审计控制台](https://config.console.aliyun.com/)。
2. 在左侧导航栏，单击**账号组**。
3. 在**账号组**页面，单击**新建账号组**。
4. 在**新建账号组**页面，先设置账号组名称和描述，再选择**账号组类型**为**全局**。
5. 单击**提交**。在**账号组**列表中，目标账号组的状态为**创建完成**，说明新建账号组成功。您还可以查看目标账号组的名称、描述、成员账号数量、账号组类型和创建时间。

##### 设置投递数据到日志服务SLS

1. 登录[配置审计控制台](https://config.console.aliyun.com/)。
2. 在左侧导航栏，单击**投递**。
3. 在**投递**页面，单击左上角的**新建投递**。
4. 在**新建投递**页面，先输入**投递名称**，再选择**投递渠道**为**日志服务SLS**，然后设置日志服务SLS的相关参数。您可以在当前企业管理账号中新建日志项目，也可以选择当前企业管理账号或其他成员账号中已有日志项目。该日志项目用于接收企业管理账号和所有成员账号的资源投递数据。

详细的操作步骤见产品[链接](https://help.aliyun.com/zh/document_detail/179275.html)。

这样配置之后，就可以将多账号内不合规资源事件统一投递到日志账号的特定SLS Project中。

#### 在运维账号配置Grafana

首先创建一个工作区，单独购买一个独立的工作区，如果用户当前已经有一个独立工作区那可以直接使用无须再购买。

##### 添加数据源

添加日志服务SLS数据源，参数[链接](https://help.aliyun.com/zh/arms/observable-visualization-grafana-edition/add-and-use-the-sls-data-source-in-log-service)

选择类型：Type: log-service-datasource

##### 创建大盘面板

首先创建第一块大屏：按账号维度统计不同账号的不合规条目数

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976581571/p972234.png)

Query语法：

```
*| select regexp_extract("evaluationResultIdentifier", '"resourceOwnerId":(.*?),',1) as account,count(*) as number group by account
```

再创建第二块大屏：按审计规则来统计不同规则有多少条不合规的资源数

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976581571/p972228.png)

Query语法：

```
*| select regexp_extract("evaluationResultIdentifier", '"sourceIdentifier":"(.*?)",',1) as rule,count(*) as number group by rule
```

## 相关内容

- 应用实时监控ARMS-[链路追踪](https://help.aliyun.com/zh/arms/tracing-analysis/preparations)
- [ARMS Prometheus监控](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-154（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
