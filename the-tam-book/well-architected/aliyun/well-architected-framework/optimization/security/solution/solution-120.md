<!-- source: https://help.aliyun.com/zh/well-architected/solution-120 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929415 -->

# 多账号容器集群日志统一归集

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971911.png)

在多账号场景下，客户希望将不同云账号内容器集群的日志（包括集群本身的操作日志、集群审计日志及业务日志）统一采集到单个日志账号，便于进行集中式的日志管理以及安全审计。本方案会介绍如何使用阿里云日志服务产品来配置多账号的容器集群日志的统一归集和审计。

## 方案优势

### 集中式日志记录

本方案提供了多容器集群日志的统一采集方法，包括开启集群审计日志、集群操作日志及业务日志以及统一采集的方法。通过统一日志采集，方便用户在一个可自定义、用户友好地产品控制面板做集群日志的日志分析、可视化展示以及安全审计。

### 日志灵活查询可视化

支持查询SQL语法，支持用户定制的查询需求。另外SLS产品提供了丰富的报表制作能力，用户可以把查询结构按不同维度展示。

## 客户场景

### 多账号多集群日志收集分析

#### 场景描述

所有业务全部跑在公有云上的ACK托管版集群中，需要将集群的日志统一在中心日志账号进行管理。

#### 适用客户

- 公有云客户
- 每个账号下面的集群日志统一采集到一个日志账号

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971914.png)

**架构说明：**

- 企业需要重点关注的三类容器场景日志：业务日志、集群操作日志、APIServer审计日志。
- 业务日志：通过Logtail-DS采集业务日志，按指定路径采集不同业务日志。
- 操作日志：通过操作审计采集集群层面的操作事件（如添加节点，关闭删除保护之类）。
- 集群审计日志：开启APIServer审计日志，能够将APIServer的操作事件统一归集。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 容器服务ACK | [阿里云容器服务Kubernetes版](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/product-overview/what-is-ack)（Alibaba Cloud Container Service for Kubernetes，简称容器服务ACK）是全球首批通过Kubernetes一致性认证的服务平台，提供高性能的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理，让您轻松高效地在云端运行Kubernetes容器化应用。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/ack/billing-information)。 |
| 日志服务 | [日志服务SLS](https://help.aliyun.com/zh/sls/what-is-log-service)是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/sls/billing-overview)。 |
| 资源目录 | [资源目录RD](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)（Resource Directory）是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费 |
| 操作审计 | [操作审计](https://help.aliyun.com/product/28802.html)（ActionTrail）是阿里云提供的云账号资源操作记录的查询和投递服务，可用于安全分析、资源变更追踪以及合规性审计等场景。 | 操作审计目前不收取任何费用。但由于需要把日志投递到日志服务（SLS），需要按照SLS的定价[单独付费](https://help.aliyun.com/zh/actiontrail/product-overview/billing-1)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| Logtail-DS | Logtail-DS是日志服务提供的容器集群日志采集Agent，用于采集阿里云ECS、自建IDC、其他云厂商的集群日志。 |

## 安全性

### 日志服务安全性

日志服务具有丰富的安全防护能力，支持服务器端加密、细粒度权限管控、详细服务日志等特性，同时提供日志审计功能，针对主流云产品提供多账号下实时自动化、中心化采集云产品日志并实现审计。日志服务为您提供丰富的数据洞察能力，同时满足您企业数据的安全与合规要求。详情参见[安全与合规](https://help.aliyun.com/zh/sls/security-and-compliance)。

## 注意事项

### 产品功能限制

SLS在产品使用上面有些限制，具体可以查看[产品限制](https://help.aliyun.com/zh/sls/limits-1/)。

### SLS存储费用问题

跨账号采集集群审计日志，会在本账号的SLS中也会保存一份日志数据，为了最大化降低日志存储费用。建议在本账号的SLS中只做数据通道功能，可以把对应Logstore的数据保存时间可以设置成1天，同时关闭索引。这样能够最大化降低本账号审计日志的费用。

### 业务日志规划问题

Logtail-DS是依据不同宿主机上目录的不同，定义不同的Logstore配置。需要提前规划好应用的日志目录。

### 智能冷热分层存储

日志服务提供冷存储功能，降低您长周期存储的成本，并同时保证日志的查询、分析、可视化、告警、采集和加工等能力不受影响。冷存储数据的存储费用按照冷存储的存储空间计费，冷热数据转换不会产生费用。更多可以参考产品[链接](https://help.aliyun.com/zh/sls/enable-hot-and-cold-tiered-storage-for-a-logstore)。

### 集群审计日志注意事项

- 对于大量冗余的kube-proxy watch请求，kubelet和system:nodes对于节点的get请求，kube组件在kube-system下对于endpoint的操作，以及API Server对于Namespaces的get请求等不作审计。
- 对于/healthz*，/version*及/swagger*等只读URL不作审计。
- 对于可能包含敏感信息或二进制文件的Secrets，ConfigMaps，tokenreviews接口的日志等级设为metadata，该level只记录请求事件的用户、时间戳、请求资源和动作，而不包含请求体和返回体。
- 对于一些如authentication、rbac、certificates、autoscaling、storage等敏感接口，根据读写记录相应的请求体和返回体。

## 实施步骤

### 场景规划

本文会介绍三个场景的实施步骤

- 场景1：采集多集群内的业务日志到日志账号
- 场景2：采集多集群内的集群审计日志到日志账号
- 场景3：采集集群本身的操作日志到日志账号

### 实施准备

- 确保所有账号在阿里云官网已经开通ACK服务。具体操作，请参见[官方文档](https://help.aliyun.com/product/85222.html)。
- 确保所有账号在阿里云官网已经开通 SLS服务。具体操作，请参见[官方文档](https://help.aliyun.com/zh/sls/what-is-log-service)。
- 请确保您已开通资源目录。具体操作，请参见[开通资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/enable-a-resource-directory)。
- 请确保您已经在操作审计创建了多账号跟踪，并将所有地域的事件采集到日志服务SLS中。具体操作，请参见[创建多账号跟踪](https://help.aliyun.com/zh/actiontrail/user-guide/create-a-multi-account-trail)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：30分钟。

### 操作步骤

#### 场景一：采集多集群内的业务日志到日志账号

##### 演示架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971910.png)

##### 业务账号中的ACK安装Logtail组件

**场景1：为已有的Kubernetes集群安装Logtail组件**

1. 登录[容器服务管理控制台](https://cs.console.aliyun.com/)。
2. 在左侧导航栏中，单击**集群**。
3. 在**集群列表**页面中，单击目标集群。
4. 在左侧导航栏中，选择**运维管理 > 组件管理**。
5. 在**日志与监控**页签中，找到Logtail-DS，然后单击**安装**。安装完成后，日志服务会自动生成名为**k8s-log -${your_k8s_cluster_id}（也支持自定义名称）**的Project，并在该Project下生成名为**k8s-group-${your_k8s_cluster_id}**的机器组和名为**config-operation-log**的Logstore。

**场景2：创建Kubernetes集群时安装Logtail组件**

1. 登录[容器服务管理控制台](https://cs.console.aliyun.com/)。
2. 在左侧导航栏中，单击**集群**。
3. 在**集群列表**页面中，单击**创建集群**。
4. 在**组件配置**配置项页中，选中**使用日志服务**。当选中**使用日志服务**后，会出现创建项目（Project）的提示。关于日志服务管理日志的组织结构，请参见[项目（Project）](https://help.aliyun.com/zh/sls/project)。有以下两种创建Project方式。**使用已有Project**您可以选择一个已有的Project来管理采集到的容器日志。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971913.png)**创建新Project**日志服务自动创建一个名为**k8s-log-{ClusterID}**的Project来管理采集到的容器日志。其中**ClusterID**为您新建的Kubernetes集群的唯一标识。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971912.png)安装完成后，在该Project下自动创建名为**k8s-group-${your_k8s_cluster_id}**的机器组和名为**config-operation-log**的Logstore。

##### 日志服务中配置跨账号采集ACK中业务日志

**步骤一：设置阿里云账号为用户标识**

1. 使用**业务账号**登录[容器服务管理控制台](https://cs.console.aliyun.com/)。
2. 设置**日志账号**为用户标识。在左侧导航栏中，单击**集群**。在**集群列表**页面中，单击目标集群。在左侧导航栏中，选择**配置管理 > 配置项**。选择**命名空间**为**kube-system**，然后在配置项列表中单击**alibaba-log-configuration**对应的**编辑**。在**编辑**面板中，完成如下操作，然后单击**确定**。在**log-ali-uid**配置项中增加阿里云账号A的ID，然后记录**log-machine-group**配置项的值（例如k8s-group-cc47****54428），在创建机器组时需设置**用户自定义标识**为该值。多个账号之间使用半角逗号（,）相隔，例如**17****397,12****456**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971915.png)
3. 重启Logtail-DS，使配置生效。在Logtail-DS详情页面，确认各个容器组的状态为**Running**且创建时间为您更新配置后的时间。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971920.png)在左侧导航栏中，选择**工作负载 > 进程守护集**。在守护进程集列表中，单击Logtail-DS对应的**编辑**。在**环境变量**区域，单击**新增**。新增一个任意内容的自定义变量（例如random_id：439157431651471905349）。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971917.png)单击**更新**。

**步骤二：创建机器组**

1. 使用**日志账号**登录[日志服务控制台](https://sls.console.aliyun.com/)。
2. 在Project列表区域，单击目标Project。
3. 在左侧导航栏中，选择**资源 > 机器组**。
4. 选择**机器组**右侧的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971916.png)**> 创建机器组**。
5. 在**创建机器组**对话框中，配置如下参数，然后单击**确定**。其中**用户自定义标识**需设置为您在步骤一：设置阿里云账号为用户标识中获取的机器组标识（例如k8s-group-cc47****54428）。其他参数说明，请参见[创建用户自定义标识机器组](https://help.aliyun.com/zh/sls/create-a-user-defined-identity-machine-group)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971921.png)
6. 检查机器组中的服务器心跳都为OK。在机器组列表中，单击目标机器组。在**机器组配置**页面，查看容器节点（ECS）的心跳状态。**心跳**为**OK**表示容器节点与日志服务的连接正常。如果显示**FAIL**请参见[Logtail机器组无心跳](https://help.aliyun.com/zh/sls/troubleshoot-the-errors-related-to-logtail-machine-groups)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971922.png)

**步骤三：创建Logtail采集配置**

1. 使用**日志账号**登录[日志服务控制台](https://sls.console.aliyun.com/)。
2. 在**数据接入**区域，单击**Kubernetes-文件**。
3. 选择目标Project和Logstore，单击**下一步**。
4. 单击**使用现有机器组**。
5. 选中您在步骤二：创建机器组中所创建的机器组，将该机器组从**源机器组**移动到**应用机器组**，单击**下一步**。
6. 设置Logtail采集配置，单击**下一步**。具体参数说明，请参见[通过DaemonSet-控制台方式采集容器文本日志](https://help.aliyun.com/zh/sls/use-the-log-service-console-to-collect-container-text-logs-in-daemonset-mode)。这一步需要关注下日志路径。
7. 预览数据及设置索引，单击**下一步**。日志服务默认开启全文索引。您也可以根据采集到的日志，手动或者自动设置字段索引。更多信息，请参见[配置索引](https://help.aliyun.com/zh/sls/create-indexes)。

#### 场景二：采集多集群内的集群审计日志到日志账号

##### 演示架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971918.png)

##### 开启阿里云上ACK集群的审计日志

本步骤讲解如何开启阿里云上ACK集群的审计日志。登录业务账号进行如下操作：

1. 登录[容器服务管理控制台](https://cs.console.aliyun.com/)。
2. 在控制台左侧导航栏中，单击**集群**。
3. 在**集群列表**页面中，单击目标集群名称或者目标集群右侧**操作**列下的**详情**。
4. 单击左侧导航栏中的**安全管理**，单击安全管理下的**集群审计**菜单。
5. 单击**开启集群审计功能**，选择**使用已有 Project**或者**创建新Project**后，单击**确定**。

##### 在日志账号创建用于接收其他账号下集群日志的Project以及Logstore

本步骤讲解如何创建用于接收其他账号下集群日志的Project以及Logstore。登录日志账号进行如下操作：

1. 创建Project登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表区域，单击**创建Project**。在**创建Project**面板中，配置相关参数，并单击**确定**。具体参数见[操作手册](https://help.aliyun.com/zh/sls/manage-a-project/)。
2. 创建Logstore登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表区域，单击目标Project。在**日志存储 > 日志库**页签中，单击**+**图标。在**创建Logstore**页面中，配置相关参数。具体参数见[操作手册](https://help.aliyun.com/zh/sls/manage-a-logstore)。

##### 将多个账号的集群审计日志统一归集到单个账号下

本步骤讲解如何将多个账号的集群审计日志统一归集到单个账号下。登录日志账号进行如下操作：

1. 创建SLS数据加工任务，将其他账号下的集群审计日志统一归集到单个账号下：登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表区域，单击需要归集的目标Project。在Logstore页面，单击目标Logstore（集群审计日志Logstore的名称为`audit-{集群id}`）新建数据加工任务![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971924.png)加工语句留空，单击保存数据加工按钮![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971923.png)配置存储目标（这里假设需要将日志归集到另一个账号下名为collect-logs的Project下的collect-cluster-audit-logs Logstore中），单击确定提交加工任务，详情可以参考[多源Logstore数据汇总](https://help.aliyun.com/zh/sls/aggregate-data-from-multiple-source-logstores)：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971919.png)注意！这里可以选择自定义角色或密钥的方式进行配置。具体可以查看官网[链接](https://help.aliyun.com/zh/sls/scenario-5-use-accesskey-pairs-to-transfer-data-across-accounts)。稍等片刻，即可在目标账号下的Logstore中看到归集过来的集群日志：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0676581571/p971925.png)

## 故障排除

### 当您使用Logtail采集业务日志遇到异常情况时，参见如下内容

- [如何排查容器日志采集异常](https://help.aliyun.com/zh/sls/what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers)
- [如何使用Logtail容器快速诊断工具](https://help.aliyun.com/zh/sls/user-guide/how-do-i-use-the-logtail-container-diagnostics-tool)

### 当采集集群审计日志到日志账号失败的可能原因及解决办法

- 为源Logstore配置了非法的AccessKey ID和AccessKey Secret。错误日志：`{
 "errorCode": "Unauthorized", 
 "errorMessage": "AccessKeyId not found: LTAI****************"
}
{ 
 "errorCode": "SignatureNotMatch", 
 "errorMessage": "signature uJf****************= not match"
}`排查方法：检查您所配置的源Logstore的AccessKey ID和AccessKey Secret是否存在且正确。

## 相关内容

- [日志服务数据加工功能使用文档](https://help.aliyun.com/zh/sls/data-transformation/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-120（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
