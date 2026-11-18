<!-- source: https://help.aliyun.com/zh/well-architected/solution-121 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929353 -->

# 多账号容器集群风险审计

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2676581571/p971073.png)

在多账号场景下，客户希望能够统一规划各个账号内容器集群的风险审计，同时希望能够将集群风险日志能够统一采集到日志账号中进行集中分析与事件告警。本方案会从三个层次来分析介绍如何利用配置审计（Config）、容器集群自带的组件、云安全中心等产品来实现多维度的集群风险审计。

## 方案优势

### 提供更全面的风险审计

本方案会围绕容器集群本身的配置、集群组件、APIServer执行指令等多个维度综合介绍容器集群的审计。相对于单一产品说明，本方案更偏客户视角，旨在提供更全面的风险审计能力。

### 统一管理与集中日志采集

借助于多账号管理方案，客户可以在资源管理账号（MA账号）集中维护配置审计规则，查看不合规资源项。同时还支持将各个成员账号内的风险审计日志集中采集到日志账号，进行综合分析与配置告警。

## 客户场景

### 多账号多集群风险审计

#### 场景描述

所有业务全部跑在公有云上的ACK集群中，需要考虑统一的集群合规审计。

#### 适用客户

- 公有云客户
- 关注容器集群风险审计

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2676581571/p971072.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 容器服务ACK | [阿里云容器服务Kubernetes版](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/product-overview/what-is-ack)（Alibaba Cloud Container Service for Kubernetes，简称容器服务ACK）是全球首批通过Kubernetes一致性认证的服务平台，提供高性能的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理，让您轻松高效地在云端运行Kubernetes容器化应用。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/ack/billing-information)。 |
| 日志服务 | [日志服务SLS](https://help.aliyun.com/zh/sls/what-is-log-service)是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/sls/billing-overview)。 |
| 资源目录 | [资源目录RD](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)（Resource Directory）是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费 |
| 配置审计 | [配置审计](https://help.aliyun.com/product/127306.html)（CloudConfig）是阿里云上的配置管理和IT治理服务。将您分散在各地域的资源整合为全局资源列表，您可以便捷地搜索全局资源。同时帮助您记录云上IT资源的配置变更历史，允许您将全量资源配置和配置历史文件持续收集到指定的存储空间。同时持续自动地评估云上资源配置的合规性，实现云上IT合规治理。 | 配置审计公测期间所有阿里云有效账号均可免费使用。但具体涉及到其他服务，详情计费[参考链接](https://help.aliyun.com/zh/document_detail/133951.html) |
| 云安全中心 | [云安全中心](https://help.aliyun.com/zh/security-center/what-is-security-center)作为一个实时识别、分析和预警安全威胁的统一安全管理系统，为您提供安全态势总览、防勒索、防病毒、防篡改、合规检查等安全能力，全方位检测和防护您的服务器和Web应用安全。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/security-center/billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| security-inspector | security-inspector 是容器服务ACK提供的集群配置安全风险扫描组件。security-inspector组件支持对Workload配置进行多维度扫描，帮助您实时了解当前状态下集群内应用是否存在安全隐患。 |
| Logtail-DS | Logtail-DS是日志服务提供的容器集群日志采集Agent，用于采集阿里云ECS、自建IDC、其他云厂商的集群日志。 |

## 安全性

### 日志服务安全性

日志服务具有丰富的安全防护能力，支持服务器端加密、细粒度权限管控、详细服务日志等特性，同时提供日志审计功能，针对主流云产品提供多账号下实时自动化、中心化采集云产品日志并实现审计。日志服务为您提供丰富的数据洞察能力，同时满足您企业数据的安全与合规要求。详情参见[安全与合规](https://help.aliyun.com/zh/sls/security-and-compliance)。

### 用户访问控制安全性

本方案里面涉及到多个账号，不同账号内的权限粒度也会有差异。以下是各个账号的RAM用户最小权限

| 账号 | RAM权限 | 备注 |
| --- | --- | --- |
| 资源管理账号 | AliyunConfigFullAccess | 管理配置审计的权限 |
| 业务账号 | AliyunCSFullAccess | 管理容器服务(CS)的权限 |
| AliyunYundunSASFullAccess | 管理云安全中心(SAS)的权限 |  |
| AliyunLogFullAccess | 管理日志服务(Log)的权限 |  |
| 自定义策略：**{"Statement":****[{"Action": ["cs:DescribePolarisConfig","cs:DescribePolarisJob","cs:DescribePolarisCronJob","cs:UpdatePolarisJob","cs:UpdatePolarisCronJob"],"Effect":"Allow","Resource":["acs:cs:*:*:cluster/<yourclusterID>"]}],"Version":"1"}** | ACK容器服务配置巡检页面授权 |  |
| 自定义策略：**{"Version":"1","Statement":[{"Action":["log:Get*","log:List*"],"Resource":"acs:log:*:*:project/<指定的Project名称>/*","Effect":"Allow"}]}** | 巡检报告功能查看的授权 |  |
| RBAC授权：授予子账号指定集群的管理员权限 | 确保子账号拥有操作配置巡检页面中涉及的Kubernetes资源的权限。 |  |
| 日志账号 | AliyunLogFullAccess | 管理日志服务(Log)的权限 |

## 注意事项

### 产品功能限制

- SLS在产品使用上面有些限制，具体可以查看[产品限制](https://help.aliyun.com/zh/sls/limits-1/)。
- Config在产品使用上面有些限制，具体可以查看[产品限制](https://help.aliyun.com/zh/document_detail/183384.html)。
- 集群巡检预警范围可以查看[产品文档](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/check-items-and-solutions)。
- 配置巡检检查集群的安全风险范围，可以查看[产品文档](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster)。

### SLS存储费用问题

跨账号采集集群审计日志，会在本账号的SLS中也会保存一份日志数据，为了最大化降低日志存储费用。建议在本账号的SLS中只做数据通道功能，可以把对应Logstore的数据保存时间可以设置成1天，同时关闭索引。这样能够最大化降低本账号审计日志的费用。

### 智能冷热分层存储

日志服务提供冷存储功能，降低您长周期存储的成本，并同时保证日志的查询、分析、可视化、告警、采集和加工等能力不受影响。冷存储数据的存储费用按照冷存储的存储空间计费，冷热数据转换不会产生费用。更多可以参考产品[链接](https://help.aliyun.com/zh/sls/enable-hot-and-cold-tiered-storage-for-a-logstore)。

## 实施步骤

### 场景规划

本文会介绍三个场景的实施步骤

- 场景1：通过配置审计检测容器集群本身配置。
- 场景2：通过集群巡检、配置巡检检测集群组件是否存在运维及安全方面风险。
- 场景3：APIServer执行异常指令：通过云安全中心检测是否有执行异常指令。

### 实施准备

- 确保所有账号在阿里云官网已经开通ACK服务。具体操作，请参见[官方文档](https://help.aliyun.com/product/85222.html)。
- 确保账号内的Kubernetes集群处于正常运行中状态（**集群列表**中集群状态为**运行中**）。
- 确保成员账号与日志账号在阿里云官网已经开通 SLS服务。具体操作，请参见[官方文档](https://help.aliyun.com/zh/sls/what-is-log-service)。
- 请确保在资源管理账号中已开通资源目录。具体操作，请参见[开通资源目录](https://help.aliyun.com/zh/document_detail/213775.html)。
- 确保已在「资源管理账号」中开通配置审计产品。具体操作，请参见[开通配置审计](https://help.aliyun.com/zh/document_detail/213775.html)。
- 确保成员账号开通云安全中心旗舰版，在云安全中心设置处打开K8s威胁检测，此步骤为授权云安全中心使用k8s审计日志进行威胁检测。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：30分钟。

### 操作步骤

#### 场景一：通过配置审计检测容器集群本身配置

具体操作，请查阅配置审计-[企业管理账号快速入门](https://help.aliyun.com/zh/document_detail/213775.html)。

针对容器服务场景，配置审计内置的规则如下表：

| 规则名称 | 适应场景 |
| --- | --- |
| ACK集群未设置公网连接端点 | ACK集群设置了公网连接端点会提升各类资源对象（例如：Pod、Service、ReplicaController等）在公网被攻击的风险，不建议您设置公网连接端点。 |
| ACK集群建议开启释放保护 | 对于有特定用途的ACK集群，开启释放保护能避免意外释放资源造成的业务中断，增强业务稳定性。 |
| ACK集群使用Terway网络插件 | 创建ACK集群时推荐选择Terway网络插件，通过Terway网络插件可以实现ACK集群内部的网络互通。 |
| ACK集群节点安装云监控插件 | 当您创建、变更、删除在ACK集群节点部署的应用时，插件会自动同步应用元数据到云监控，帮助您实现应用的容器监控与报警。 |

#### 场景二：通过集群巡检、配置巡检检测集群组件是否存在运维及安全方面风险

##### 集群巡检

容器服务ACK提供了集群巡检功能，您可以定时扫描集群运行状况，发现集群中潜在的风险，如云资源配额余量、Kuberrnetes集群关键资源水位等。

**配置集群巡检**

使用集群巡检功能时，系统将在您的集群节点上执行数据采集程序并收集检查结果，采集的信息包括系统版本、负载、Docker、Kubelet等运行状态及系统日志中关键错误信息。数据采集程序不会对您的业务信息及敏感数据进行采集。

配置集群巡检的具体步骤如下：

1. 登录[容器服务管理控制台](https://cs.console.aliyun.com/)。
2. 在控制台左侧导航栏中，单击**集群**。
3. 在**集群列表**页面中，选择目标集群，并在目标集群右侧的**操作**列下，选择**更多 > 集群检查**。
4. 在容器智能运维左侧导航栏中，选择**检查 > 定时巡检**。
5. 在**巡检规则**区域，单击**添加**。
6. 在**运行配置**配置向导中，配置相应的时区和定时规则。如果您已配置定时规则，可以在**定时巡检**页面的**巡检规则**区域，单击**删除**。删除已有规则后，重新配置新的规则。配置完成后，将按照指定的时间进行集群巡检。当发现集群中存在风险时，将在集群内生成异常事件。您可以通过[容器服务管理控制台](https://cs.console.aliyun.com/)，在集群**概览**页签的**事件**区域，查看异常事件。

**说明** 您也可以在**定时巡检**页面的**检查报告列表**区域，单击**执行巡检检查**进行手动巡检。

1. （可选）配置容器服务报警管理。您可以通过容器服务报警管理功能，第一时间了解集群的风险信息。具体操作，请参见[容器服务报警管理](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/alert-management)。

**查看集群巡检结果**

集群巡检配置完成后，将按照指定的时间进行集群巡检。查看集群巡检结果的具体步骤如下：

1. 登录[容器服务管理控制台](https://cs.console.aliyun.com/)。
2. 在控制台左侧导航栏中，单击**集群**。
3. 在**集群列表**页面中，选择目标集群，并在目标集群右侧的**操作**列下，选择**更多 > 集群检查**。
4. 在容器智能运维左侧导航栏中，选择**检查 > 定时巡检**。
5. 在**检查报告列表**区域，单击**操作**列下方的**查看详情**。

具体集群巡检预警参考，可以查看官方[帮助手册](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/check-items-and-solutions)。

##### 配置巡检

使用配置巡检功能来扫描集群中Workload配置的安全隐患和介绍巡检报告相关信息，帮助您实时了解当前状态下运行应用的配置是否有安全隐患。

**扫描集群Workload**

1. 登录[容器服务管理控制台](https://cs.console.aliyun.com/)。
2. 在控制台左侧导航栏中，单击**集群**。
3. 在**集群列表**页面中，单击目标集群名称或者目标集群右侧**操作**列下的**详情**。
4. 在集群管理页左侧导航栏选择**安全管理 > 配置巡检**。
5. 如果您未安装巡检组件的话，在**安装组件**下方单击**开始安装**。如果您已经安装请忽略此步骤。组件安装完成后，您也可以在**集群信息**页面的**概览**页签，单击**安全巡检**进入**配置巡检**页面。
6. 在**配置巡检**页面右上方，单击**立即执行巡检**。
7. 等待巡检扫描完成后，单击刷新图标查看相应的巡检报告。
8. **可选：**在**配置巡检**页面右上方，单击**巡检配置**，开启或禁用定期自动执行配置巡检的功能以及配置巡检时执行的检查项。

**巡检详情**

**巡检详情**页面通过表格化的方式展示不同工作负载的详细巡检结果，主要包括以下功能：

- 直观展示工作负载的巡检**通过项**和**风险项**数量。
- 在检查结果页面展示巡检结果的各个检查项的通过状态、检查项详细说明以及加固建议。
- 支持为工作负载设置检查项白名单。
- 支持**命名空间**、**工作负载类别**、**是否有风险**等条件对结果进行过滤查询。

**巡检报告**

巡检报告中主要展示最近执行的巡检扫描结果，主要包括以下几类信息：

- 扫描结果概览，包括总的检查条目数、检查各个资源项数目及百分比、整体的健康度。
- 各大类扫描结果统计，包括报告健康检查、镜像、网络、资源、安全等大类的结果。
- 各个Workload配置的详细扫描结果，包括资源类别、资源名称、命名空间、检查类型、检查项、检查结果等内容。

##### 配置巡检 - 高阶版

将成员账号内的集群风险日志跨账号投递到日志账号，进行集中日志管理。适用于能够对原始日志具备分析的用户。

**在成员账号中开启巡检**

1. 登录[容器服务管理控制台](https://cs.console.aliyun.com/)。
2. 在控制台左侧导航栏中，单击**集群**。
3. 在**集群列表**页面中，选择目标集群，并在目标集群右侧的**操作**列下，选择**更多 > 集群检查**。
4. 在容器智能运维左侧导航栏中，选择**检查 > 定时巡检**。
5. 在**巡检规则**区域，单击**添加**。
6. 在**运行配置**配置向导中，配置相应的时区和定时规则。如果您已配置定时规则，可以在**定时巡检**页面的**巡检规则**区域，单击**删除**。删除已有规则后，重新配置新的规则。配置完成后，将按照指定的时间进行集群巡检。当发现集群中存在风险时，将在集群内生成异常事件。您可以通过[容器服务管理控制台](https://cs.console.aliyun.com/)，在集群**概览**页签的**事件**区域，查看异常事件。**说明** 您也可以在**定时巡检**页面的**检查报告列表**区域，单击**执行巡检检查**进行手动巡检。
7. （可选）配置容器服务报警管理。您可以通过容器服务报警管理功能，第一时间了解集群的风险信息。具体操作，请参见[容器服务报警管理](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/alert-management)。

**在日志账号创建用于接收其他账号下集群风险审计日志的Project以及Logstore**

本步骤讲解如何创建用于接收其他账号下集群风险日志的Project以及Logstore。登录日志账号进行如下操作：

1. 创建Project登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表区域，单击**创建Project**。在**创建Project**面板中，配置相关参数，并单击**确定**。具体参数见[操作手册](https://help.aliyun.com/zh/sls/manage-a-project/)。
2. 创建Logstore登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表区域，单击目标Project。在**日志存储 > 日志库**页签中，单击**+**图标。在**创建Logstore**页面中，配置相关参数。具体参数见[操作手册](https://help.aliyun.com/zh/sls/manage-a-logstore)。

**将多个账号的集群风险日志统一采集到日志账号**

本步骤讲解如何将多个账号的集群风险日志统一采集到日志账号下，登录业务账号进行如下操作：

1. 创建SLS数据加工任务，将其他账号下的集群风险日志统一归集到单个账号下：登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表区域，单击需要归集的目标Project。在Logstore页面，单击目标Logstore（集群风险扫描日志Logstore的名称为`security-inspector-configaudit-{集群id前12位}`）。新建数据加工任务加工语句留空，单击保存数据加工按钮配置存储目标（这里假设需要将日志归集到日志账号下名为collect-logs的Project下的collect-cluster-security-logs Logstore中），单击确定提交加工任务，详情可以参考[多源Logstore数据汇总](https://help.aliyun.com/zh/sls/aggregate-data-from-multiple-source-logstores)：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2676581571/p971077.png)稍等片刻，即可在成员账号下的Logstore中看到归集过来的集群风险日志。

#### 场景三：APIServer执行异常指令：通过云安全中心检测是否有执行异常指令

##### 云安全中心开启容器K8s威胁检测

1. 登录[云安全中心控制台](https://yundun.console.aliyun.com/?p=sas)。在左侧导航栏，选择**系统配置 > 功能设置**。
2. 在**设置**页签**主机防护设置**子页签的**容器K8s威胁检测**区域，打开威胁检测开关。开启该功能后，如果检测到K8s容器集群中存在安全风险，会在**安全告警处理**页面展示相关告警，建议您及时查看并处理相关告警。具体操作，请参见[查看和处理告警事件](https://help.aliyun.com/zh/security-center/user-guide/view-and-handle-alert-events)。

##### 容器服务开启集群审计

1. 登录[容器服务控制台](https://cs.console.aliyun.com/#/k8s/cluster/list)。选择目标集群，点击进入集群详情页。
2. 在左侧导航栏，选择**安全管理 > 集群审计**。

##### APIServer某些异常指令测试用例

**Case：节点敏感目录挂载**

1. 使用以下yaml创建pod。可在ack控制台提交执行，也登录终端后保存内容为test-1.yaml并执行kubectl apply -f test-1.yaml`apiVersion: v1
kind: Pod
metadata:
 name: test-1
spec:
 containers:
 - image: nginx
 name: container
 volumeMounts:
 - mountPath: /host-root
 name: root-volume
 volumes:
 - hostPath:
 path: /root/
 name: root-volume`
2. 删除该pod，在ack控制台找到pod并删除，或者登录终端执行kubectl delete pod test-1

**测试结果**

**在云安全中心：检测响应-安全告警处理 ，可以看到有一条告警信息**

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2676581571/p971074.png)

查看详情：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2676581571/p971075.png)

也可以在容器服务控制台中查看告警信息。安全管理-安全监控。也可以查看到告警消息。

## 故障排除

### Logtail采集业务日志异常排查

- [如何排查容器日志采集异常](https://help.aliyun.com/zh/sls/what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers)
- [如何使用Logtail容器快速诊断工具](https://help.aliyun.com/zh/sls/user-guide/how-do-i-use-the-logtail-container-diagnostics-tool)

## 相关内容

- [日志服务数据加工功能使用文档](https://help.aliyun.com/zh/sls/data-transformation/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-121（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
