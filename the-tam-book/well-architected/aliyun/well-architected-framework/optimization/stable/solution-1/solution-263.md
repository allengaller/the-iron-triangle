<!-- source: https://help.aliyun.com/zh/well-architected/solution-263 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929470 -->

# 通过ARMS告警管理实现统一告警

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972989.png)

在云原生时代，企业IT基础设施的规模越来越大，越来越多的系统和服务被部署在云环境中。为了监控这些复杂的IT环境，企业通常会选择使用异构监控系统，例如Prometheus、Grafana、Zabbix等，以获取更全面的监控数据，以便更好地了解其IT基础设施的运行状况和性能表现。

然而，这种异构监控系统也带来了一些问题，其中最显着的是告警信息的分散。由于不同的监控系统可能会产生不同的告警信息，这些信息可能会分散在各个系统中，导致企业很难全面了解其IT系统的告警状况。这使得响应告警变得更加困难，同时也增加了人工管理的复杂性和工作量。

本文档介绍了一种基于 ARMS 的统一和集中的告警管理方案，以确保告警信息能够及时到达正确的人员，以便他们能够快速采取必要的措施来应对潜在的问题。

## 方案优势

### 广泛的告警源支持

ARMS告警管理覆盖了10+种常见的告警源，包括云监控CMS、日志服务SLS、Prometheus、Grafana、Zabbix、Open-Falcon和Nagios等。此外，还提供了API接入能力，使得用户可以将任意告警源产生的告警信息进行统一处理，确保了企业能够在一个平台上集中管理和响应来自不同系统的告警，从而简化了运维流程。

### 与多种协同工具的集成

通过打通钉钉、企业微信、飞书、Aone、Jira以及PagerDuty等团队协作工具，ARMS告警管理允许直接在这些工具中处理告警事件，无需切换到其他平台或系统。这不仅提高了工作效率，也减少了因频繁切换账号而可能引发的安全风险。同时，它支持复用现有的账号体系，并提供灵活的权限分配方式，进一步增强了安全性与便捷性。

## 客户场景

### 企业迁移上云后，云上产品的告警不统一

当企业将业务迁移到云端时，可能会使用到多个阿里云产品（如ACK、ECS、RDS等）来构建其应用架构。每个产品都有自己的监控系统，这导致了告警信息分散在不同的平台中。ARMS告警管理能够整合这些来自不同系统的告警信息，提供一个统一的视图，简化配置过程，并支持更高效的告警处理流程。

### 多云或混合云架构下的异构监控系统告警不统一

对于采用多云策略或者同时维护私有云与公有云资源的企业来说，面临的挑战是如何有效地管理和响应跨环境的告警信号。ARMS告警管理通过支持手动接入更多类型的监控工具，帮助企业实现跨云平台的一体化告警管理，从而提高运维效率并减少潜在的风险点。

### 自研监控系统及自定义事件告警接入需求

随着应用程序复杂度增加，开发团队可能还会开发一些定制化的监控逻辑以满足特定需求。ARMS告警管理系统允许用户灵活地集成这些自定义监控源产生的告警信息，确保所有关键指标都能被及时监测到，并采取相应措施。

## 方案架构

本方案基于ARMS告警管理，集成ARMS、日志服务SLS、云监控CMS、自建Prometheus等告警源，并通过事件处理流对收集到的告警进行压缩、降噪、去重等处理，以及配置通知对象和通知策略，实现了告警信息的全流程管理，从收集、处理到精准通知，有助于提高运维效率和告警处理的准确性。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972977.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| ARMS告警管理 | [ARMS告警管理](https://help.aliyun.com/zh/arms/alarm-operation-center/product-overview/alarm-management-overview)提供了可靠的告警收敛、通知、自动升级等功能，帮助您快速检测和修复业务告警。本文主要介绍了告警管理的实现原理和优势。 | 部分通知渠道收费，详情参见[产品计费](https://help.aliyun.com/zh/arms/alarm-operation-center/product-overview/alert-management-1/)。 |
| ARMS Prometheus监控 | [ARMS Prometheus监控](https://help.aliyun.com/zh/arms/prometheus-monitoring/product-overview/what-is-prometheus)全面对接开源Prometheus生态，支持类型丰富的组件监控，提供多种开箱即用的预置监控大盘，且提供全面托管的Prometheus服务。借助ARMS Prometheus监控，用户无需自行搭建Prometheus监控系统，因而无需关心底层数据存储、数据展示、系统运维等问题。 | 收费，详情参见[产品计费](https://www.aliyun.com/ntms/price/detail/arms_detail)。 |
| 云监控 | [云监控](https://help.aliyun.com/product/28572.html)（CloudMonitor） 是一项针对阿里云资源和互联网应用进行监控的服务。云监控服务可用于收集获取阿里云资源的监控指标，探测互联网服务可用性，以及针对指标设置警报。 | 部分功能免费，高级功能收费。具体可以查看[产品计费](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/billing-overview)。 |
| 日志服务 | [日志服务](https://help.aliyun.com/product/28958.html)（SLS）是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[产品计费](https://www.aliyun.com/price/detail/sls)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 环比上升/下降% | 若β为最近N分钟的数据（可选择为平均值、总和、最大值和最小值），α为前2N分钟到前N分钟的数据， 环比为β与α做比较。 |
| 同比上升/下降% | 以与上小时同比为例，若β为最近N分钟的数据（可选择为平均值、总和、最大值和最小值），α为上小时最近N分钟的数据，与上小时同比为β与α做比较。 |
| 通知策略 | 通知策略确定了如何将事件汇总到单一告警中，以及如何将分配的告警通知发送给联系人。您可以通过设置电话，短信，邮件或钉群等方式，将需要解决或需要联系人知晓的告警1分钟内通知到他。 |
| 升级策略 | 在告警升级超时，告警管理会依次通知升级规则定义的不同批次的联系人。升级策略可以添加到特定的通知策略中。 |

## 安全性

### 安全设置

为了确保自定义机器人使用过程的安全性，建议在告警机器人的安全设置中添加**自定义关键词**。例如添加了一个自定义关键词：**报警**，则这个机器人所发送的消息，必须包含**报警**这个词，才能发送成功。

### 访问控制

借助访问控制RAM的RAM用户，您可以实现权限分割的目的，按需为RAM用户赋予不同权限，并避免因暴露阿里云账号密钥造成的安全风险。要通过自定义授权策略为RAM用户授权，请参见[告警管理自定义RAM授权策略](https://help.aliyun.com/zh/arms/alarm-operation-center/security-and-compliance/create-custom-policies-for-alert-management)。

## 注意事项

### 免费告警通知额度限制

未开通ARMS告警管理服务的账号每天提供15次免费短信通知，3次电话通知，用量超过免费额度将导致告警通知发送失败。如您需要更多告警通知次数，请[开通告警管理服务](https://common-buy.aliyun.com/?commodityCode=arms_alert_public_cn#/buy)。

## 实施步骤

### 实施准备

- 确保已在需要集成的告警源（如云监控、ARMS、日志服务）中配置告警。
- 如需创建钉钉/企业微信/飞书（Lark）告警机器人，需确保已在对应客户端创建告警群。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 集成告警源

##### 集成ARMS告警

ARMS告警管理已默认集成ARMS，您可以直接在**告警管理 > 集成**中搜索`ARMS-DEFAULT`来查看ARMS集成。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972990.png)

##### 集成日志服务告警

ARMS告警管理支持通过Webhook的方式将日志服务产生的告警接入告警管理，以便您对接入的这些告警统一起来集中处理。

日志服务接入ARMS告警管理的方法有以下两种：

- 将日志服务**指定Project下的所有告警**接入ARMS告警管理，请参见[创建集成并接入日志服务](#wWc7B)。
- 将日志服务下的**指定告警**接入ARMS告警管理，请参见[接入日志服务指定报警规则](#TJCyR)。

###### 创建集成并接入日志服务

1. 登录[ARMS控制台](https://arms.console.aliyun.com/?spm=a2c4g.11186623.0.0.765058f3azy8AB#/home)，在左侧导航栏选择**告警管理 > 集成**。
2. 在**集成**页面的**告警集成**页签单击**日志服务**。
3. 在弹出的对话框输入日志服务集成的名称、描述和告警事件自动恢复时间。
4. 在**接入告警事件的Project**的**全部Project**区域，显示了阿里云日志服务的所有Project，选择需要接入告警的Project，单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972991.png)图标，然后单击**保存**。此功能会自动遍历选中的Project中配置的所有告警规则，在这些规则上自动新增告警的请求地址为`https://alerts.aliyuncs.com/api/v1/events/{{token}}`，其中，`{{token}}`为集成创建时自动生成的密钥。

配置完成后，在**告警集成**页签可以查看已创建的日志服务集成。

###### 接入日志服务指定告警规则

1. 在**集成**页面的**告警集成**页签，复制目标日志服务集成的集成地址。
2. 登录[日志服务控制台](https://sls.console.aliyun.com/)。
3. 在**Project列表**区域单击目标Project，然后在左侧导航栏单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972993.png)图标，即告警图标。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972978.png)
4. 在**告警中心**页面选择**通知对象 > Webhook集成**，然后在**Webhook集成**页面单击**创建**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972994.png)
5. 在弹出的对话框中添加ARMS告警管理的通用Webhook。其中，名称设置为**ARMS告警管理**，类型选择**通用Webhook**，其他参数可按照界面提示进行相关配置。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972995.png)
6. 在**告警中心**页面选择**通知策略 > 内容模板**，然后单击**创建**，在弹出的对话框中单击**WebHook-自定义**页签，发送方式选择**逐条发送**，并配置如下所示的发送内容，然后单击**确认**。`{
 "uid": "{{ alert.aliuid }}",
 "project": "{{ alert.project }}(https://sls.console.aliyun.com/#/project/{{ alert.project }}/categoryList)",
 "trigger": "{{ alert.alert_name }}",
 "condition": "{{ alert.condition }}",
 "context": {{ alert.results[0].raw_results | to_json | quote }},
 "message": " [Uid] {{ alert.aliuid }}\n\n> [Project] [{{ alert.project }}](https://sls.console.aliyun.com/#/project/{{alert.project }}/categoryList)\n\n> [Trigger] {{ alert.alert_name }}\n\n> [Condition] {{ alert.alert_name }}\n\n> [Message] 通知内容\n\n> [Context] {{ alert.results[0].raw_results | to_json | quote | removeprefix('"') | removesuffix('"') }}\n\n> [查看详情]({{ alert.query_url }})"
}`
7. 在**告警中心**页面单击**告警规则**页签，然后单击目标规则**操作**列的**编辑**，在弹出的对话框中展开**高级配置**，然后在**输出目标**区域选择**SLS通知**，**告警策略**区域选择**极简模式**，并根据界面提示配置通用Webhook的通知渠道，配置完成后单击**确定**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972979.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972997.png)

##### 集成云监控告警

ARMS告警管理支持通过WebHook的方式将云监控产生的告警接入告警管理。告警接入告警管理后可以统一进行处理，解决传统告警配置分散在各个系统中，不同系统提供的告警处理能力各不相同的问题。

云监控接入ARMS告警管理的方法有以下两种：

- 将云监控**指定产品下的所有告警**接入ARMS告警管理，请参见[创建集成并接入云监控](#r0eSh)。
- 将云监控下的**指定告警**接入ARMS告警管理，请参见[接入云监控指定报警规则](#uW9a6)。

###### 创建集成并接入云监控

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 集成**。
2. 在**告警集成**页签单击**云监控**。
3. 在**新建云监控集成**对话框输入云监控集成的名称、描述和告警事件自动恢复时间。
4. 在**接入告警事件的产品**的**全部产品**区域，显示了云监控支持接入告警管理的产品，选择需要接入告警的产品，单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972996.png)图标，然后单击**保存**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972980.png)

配置完成后，在**告警集成**页签可以查看已创建的云监控集成。

###### 接入云监控指定报警规则

在接入指定的云监控报警规则之前，需要先创建云监控集成，具体步骤请参见[创建集成并接入云监控](#r0eSh)。

1. 在**集成**页面的**告警集成**页签，复制目标云监控集成的集成地址。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972998.png)
2. 登录[云监控控制台](https://cloudmonitor.console.aliyun.com/)。
3. 在左侧导航栏，选择**报警服务 > 报警规则**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972999.png)
4. 在**报警规则**页面，单击目标报警规则**操作**列的**修改**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973000.png)
5. 在弹出的面板的**高级设置**区域设置报警回调地址为云监控集成的集成地址。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973001.png)
6. 单击**确认**。

###### 编辑集成

ARMS告警管理预设了日志服务告警源与ARMS告警管理之间字段的映射，您也可以根据需要在**编辑集成**页面新增或修改字段的映射关系。

1. 在**告警集成**页签单击目标集成右侧**操作**列的**编辑**。
2. 在**事件映射**区域左侧单击**发送测试数据**。
3. 在**发送测试数据**对话框，输入第三方告警源的JSON格式的告警内容，然后单击**发送**。如果显示`上传成功，但未生成事件，请根据原始数据配置事件映射规则!`，表示告警源与ARMS告警事件的字段没有映射，实际发送数据会被保存在左侧记录框中，以便配置映射时可以直接选取对应告警源字段。如果显示`上传成功！`，则表明对应的告警内容已上报至告警事件历史页面。更多信息，请参见[查看告警事件历史](https://help.aliyun.com/zh/arms/alarm-operation-center/view-historical-alert-events)。
4. 在**发送测试数据**对话框单击**关闭**。
5. 在**事件映射**区域左侧单击并展开需要建立映射的告警数据。
6. 在**事件映射**区域右侧配置告警源字段与ARMS告警的映射。**可选：**在**选择根节点**区域选择是否使用批处理。当告警数据存在数组节点时，可以指定目标数组节点作为根节点，将对应根节点下的数据进行批处理。选择**使用批处理**后，选择需要批处理的数组节点作为根节点。当告警数据存在多个数组节点时，ARMS告警管理仅支持选择其中一个数组节点进行批处理。**可选：**选中**配置告警恢复事件**，然后设置恢复字段条件。系统收到事件后会根据恢复字段查询告警事件，包含指定字段的事件会自动进行恢复。用于指定恢复事件的字段必须选择原事件中等价于告警等级的字段，且不可使用`$.severity`字段。例如恢复字段为`{$.eventType="resolved"}`，则系统会自动恢复该集成下**eventType**为*resolved*的所有告警。在**将源字段映射到目标字段**区域将告警源字段映射到ARMS告警字段上。单击映射图标，可以修改字段映射方式。直接：告警源指定字段直接映射为ARMS中对应的告警字段。串联：将多个告警源字段通过指定分隔符串联为一个字段，然后将这一个字段映射为ARMS中对应的告警字段。分隔符仅支持特殊字符。条件：当告警字段值满足指定条件后，设置的字段才会映射到ARMS目标字段上。映射表：设置告警源的告警等级与ARMS中的告警等级的映射，仅告警等级（severity）字段需要设置映射表。ARMS告警字段说明：**ARMS告警字段****说明****告警名称（alertname）**自定义告警的名称。**告警等级（severity）**设置告警等级的映射字段。该字段需要设置告警等级映射表，且映射方式必须设置为直接映射。**告警描述（message）**告警事件的详细信息，用于告警通知。最多支持15000字符。**告警样本值（value）**监控指标的样本值。**告警图片（imageUrl）**指标折线图URL，用于映射Grafana指标折线图。**检查项（check）**告警检查项。例如：CPU、JVM、Application Crash、Deployment。**来源（source）**告警事件的来源。**分类（class）**告警事件的对象类型，例如：主机。**服务（service）**与业务相关的来源服务，例如：Login Service。**开始时间（startat）**事件开始时间的时间戳。**结束时间（endat）**事件结束时间的时间戳。**事件地址（generatorUrl）**事件详细信息地址。
7. 设置事件去重。为了减少重复数据，系统使用相关字段作为去重依据。ARMS告警管理支持预览**事件映射**区域中的历史事件数据的去重分组结果，您可根据需要调整去重字段。事件去重仅针对未恢复状态下的事件。在**编辑集成**页面的**事件去重**区域选择需要去重的字段。当选择的字段的值相同时，对应的多个事件将会合并为一个告警通知。单击**去重测试**，可以预览去重后的告警分组。去重测试针对的是**事件映射**左侧区域中上传的最近10条测试数据。
8. 配置完成后，单击**保存**。

##### 集成自建Prometheus告警

开源Prometheus支持将报警上报到Alertmanager中，通过配置Prometheus.yaml文件中的**<alertmanager_config>**可以将报警上报到云端的报警中心，更多信息，请参考[[alertmanager_config]](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alertmanager_config)。

ARMS告警管理提供了与开源完全兼容的Alertmanager报警通知能力，通过集成Prometheus可以将自建Prometheus报警上报到ARMS告警管理中。

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 集成**。
2. 在**告警集成**页签单击**Prometheus**。
3. 在**新建Prometheus集成**对话框输入Prometheus集成的名称、描述和告警事件自动恢复时间，然后单击**保存**。告警事件自动恢复时间：当告警事件在设置的时间内都没有再触发，告警事件将会自动恢复。
4. 根据不同的Prometheus实例选择接入Prometheus的方法，然后单击**确定**。

###### 使用Prometheus-Operator管理的Prometheus实例

1. 在本地创建`arms-alertmanager-config.yaml`文件，然后将以下内容粘贴到创建的文件中。`- scheme: https
 bearer_token: ******
 static_configs:
 - targets: ['alerts.aliyuncs.com']`请在控制台获取`bearer_token`的值。
2. 通过`arms-alertmanager-config.yaml`文件创建名为`arms-am-config`的secret。`kubectl create secret generic arms-am-config --from-file=arms-alertmanager-config.yaml`
3. 在本地创建`prometheus-patch.yaml`文件，然后将以下内容粘贴到创建的文件中。`spec:
 additionalAlertManagerConfigs:
 key: arms-alertmanager-config.yaml
 name: arms-am-config`
4. 执行以下命令获取Prometheus对象。`kubectl get prometheus`返回示例：`NAME VERSION REPLCAS AGE
prometheus-operator-160879-prometheus v2.18.2 1 4d1h`
5. 执行以下命令将`prometheus-patch.yaml`文件更新到Prometheus对象中。`kubectl patch prometheus prometheus-operator-160879-prometheus --patch "$(cat prometheus-patch.yaml)" --type=merge`

###### 其他方式自行搭建的Prometheus实例

1. 修改`prometheus.yaml`配置文件。此处以2.35版本Prometheus为例添加配置如下，更多版本的配置格式，请参见[Prometheus官方文档](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)。`alerting:
 alertmanagers:
 - api_version: v1
 authorization:
 type: Bearer
 credentials: ${token}
 scheme: https
 static_configs:
 - targets: ["alerts.aliyuncs.com"]`请在控制台获取`bearer_token`的值。
2. 在浏览器中访问Prometheus的配置页面，检查`prometheus.yaml`文件是否已修改。

###### 其他类Prometheus可观测系统集成ARMS告警

Thanos通过`thanos rule`命令的参数`--alertmanagers.config`指定alertmanager配置文件，参照上文填写上述集成的地址和Token，配置详情请参见[Thanos文档](https://thanos.io/tip/components/rule.md/#configuration)。

VictoriaMetric通过`./bin/vmalert`命令的参数`-notifier.config`指定notifier配置文件，参照上文填写上述集成的地址和Token，配置详情请参见[VictoriaMetric文档](https://docs.victoriametrics.com/vmalert.html#notifier-configuration-file)。

#### 创建事件处理流

使用ARMS告警管理集成多个告警源后，您可以通过设置事件处理流将告警源产生的事件进行过滤和分类。

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)。
2. 在左侧导航栏中选择**告警管理 > 事件处理流**。
3. 在**事件处理流**页面单击右上角的**新建处理流**。
4. 在**新建处理流**页面的**基本信息**区域输入处理流名称。
5. 在**流动作配置**区域设置事件处理流程。将**可用流程动作**区域的动作拖至**事件处理流**区域。在最右侧区域设置事件处理流中各动作的执行条件。动作配置完成后可以在**测试数据**区域对告警字段进行测试，验证动作是否配置成功。**动作****说明****示例****触发条件**满足触发条件的事件才会执行当前处理流。**场景**名称为**容器CPU使用率告警**的集成执行当前处理流。**动作配置**设置条件为`_aliyun_arms_integration_name等于容器CPU使用率告警`。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972981.png)**过滤事件**满足过滤条件的事件将会跳过当前事件流，执行下一个事件流，未过滤的事件将会继续执行当前处理流。如果您的告警规则还未产生事件，此时只能选择到ARMS预置的`_aliyun_arms_integration_id`和`_aliyun_arms_integration_name`字段进行配置。如果您需要使用severity、alertname等事件字段，可以通过以下两种方式配置：手动输入字段。添加告警规则，使其产生告警事件。产生事件后，即可以在此选择事件字段值。**场景**P4等级的告警事件不执行当前处理流。**动作配置**设置条件为`severity等于P4`。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973002.png)**识别事件类型**根据选择的事件字段值，通过算法识别出事件对象分类（Class）和事件类型（Type），用于事件和告警查询统计。支持识别的事件对象分类（Class）如下：网络（Network）存储（Storage）计算（Compute）操作系统（OS）应用（Application）数据库（Database）变更（Change）支持识别的事件类型（Type）如下：可用性（Availability）时延容量（Capacity）错误未知（Unknown）**场景**通过`alertname`和`message`字段值识别事件的对象分类（Class）和事件类型（Type）。**动作配置**设置**识别分类字段**为`alertname`和`message`。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973003.png)**执行结果**系统会将智能识别结果写入`class`和`type`标签。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972982.png)**设置事件等级**将执行当前处理流的事件等级设置为特定值。**场景**将核心服务网络类型的告警事件的等级设置为P1。**动作配置**设置**触发条件**动作为`class等于network`。将**设置事件等级**动作设置为P1。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973004.png)**执行结果**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973005.png)**设置业务标签**为执行当前处理流的事件设置业务标签（Label），用于事件和告警统计查询。字段：将事件中的字段值作为`label`字段值。值：为`label`字段设置固定值。**场景**将告警等级作为告警标签，以便之后统计各等级的事件。**动作配置**设置业务标签为`字段：severity`。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972983.png)**执行结果**告警事件中将会新增`label`字段，`label`字段值为`severity`字段值。**删除字段**删除事件中的某些字段。**场景**告警事件中存在`location`和`region`字段，`location`字段中已包含Region信息，需要删除`region`字段。**动作配置**设置删除字段为`region`。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973006.png)**提取内容**通过正则表达式，提取事件中某字段的内容，填充到新的字段中。**场景**告警字段：`cn-hangzhou-hz4`提取`location`字段的地域和具体位置信息填充到`region`和`datacenter`字段中。**动作配置**待提取字段：`location`提取正则表达式：`([a-zA-z]+-[a-zA-z]+)-(.*)`填充的字符：`region`、`datacenter`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973007.png)**执行结果**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973008.png)**匹配更新**当系统检测到事件的指定字段中存在某段内容时，就将设置的字段值填充到目标字段中。**场景**告警字段：`"message":"ping to i-bp1e42d0ydxf7pstuepz > 100ms"`当`message`中包含`ping`时表示当前事件为网络事件，则需要将当前事件标记为网络类型。**动作配置**匹配字段：`message`满足下面条件时更新字段值：包含`ping`输出`network`**。**包含的值可以使用实际字段å值或正则表达式。填充到字段：`class`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973009.png)**执行结果**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972984.png)**字段丰富**通过调用API或者查询本地Excel数据源的方式，将得到的结果填充到目标字段中。目前数据源功能仍在灰度中，请联系告警钉钉答疑号（`d9j_rg9e4062f`）协助添加。**场景**根据告警事件中的IP字段，通过查询上传的Excel数据源，将得到的主机名填充到事件的`hostname`字段中。**动作配置**选择数据源：**获取Host数据源-excel**匹配更新模式：`ip`（匹配Excel中列名）等于`ip`（对应Excel中列值）填充到字段：`$.hostName`（Excel查询返回结果得到的列名） 填充到`hostname`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973010.png)**替换内容**查找并替换指定字段中的字段内容，可以正则表达式查找对指定字段内容。**场景**将告警事件中的`d.b.`字符串替换为`database`字符串。**动作配置**需要替换的内容片段：`message`将内容片段：`d\.b\.`**说明**可以使用实际字段值或正则表达式。替换为：`database`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973011.png)**执行结果**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973012.png)**分割内容**通过分割字符对字段进行拆分，拆分结果填充到多个目标字段中。**场景**告警字段：`"message":"myhostid_myuserid_myruleid"`将`message`字段中的字段值拆分为`hostid`、`userid`、`ruleid`并分别填充到新的字段中。**动作配置**需要拆分的字段：`message`分割字符：`_`拆分结果填充字段：`hostId`、`userId`、`ruleId`拆分后的字段将会按照顺序填充。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973013.png)**执行结果**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972985.png)**填充模板**填入一段模板内容（如：类型`${class}`的事件来源是`${source}`），变量名为事件集成后的字段名，模板渲染后填充到目标字段中。**场景**告警字段：`"source":"server", "class":"network"`将`message`字段设置为`类型${class}的事件来源是${source}`，其中需要引用`class`和`source`字段值。**动作配置**填充的模板：`类型${class}的事件来源是${source}`填充到字段：`message`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973014.png)**执行结果**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973015.png)**丢弃**丢弃执行当前处理流的事件，丢弃动作只能作为当前事件处理流最后一个节点，且无需设置。无
6. 在**测试数据**区域左侧输入测试字段和字段值，或者单击**从事件中选择**，从已有的告警事件中选择测试事件，然后单击**点击测试**。
7. 设置完成后，单击**保存**。处理流新建完成后，集成的告警源将会按处理流顺序完成事件的过滤，过滤后的事件可以在告警事件历史页面查看。更多信息，请参见[查看告警事件历史](https://help.aliyun.com/zh/arms/alarm-operation-center/view-historical-alert-events)。

#### 创建告警通知对象

ARMS告警管理支持通过电话、短信、邮件、钉钉、企业微信、飞书和Webhook方式向联系人发送告警通知。

##### 联系人

###### 新建联系人

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 通知对象**。
2. 在**联系人**页签单击**新建联系人**。在**新建联系人**对话框中根据实际需求设置以下参数，然后单击**确认**。**参数****说明****姓名**自定义联系人姓名。**手机号**设置联系人的手机号码后，可以通过电话和短信的方式接收告警通知。**邮箱**设置联系人的邮箱地址后，可以通过邮箱接收告警通知。**联系人组**选择联系人需要加入的联系人组。创建联系人组的操作，请参见[新建联系人组](#d0V6l)。**电话通知失败补发类型**选择电话通知失败后，通知补发类型。**用户标识**在企业内使用的IM工具（目前支持钉钉、飞书、企业微信）对应的用户ID，如钉钉号、企微号等。该字段可用于群内告警卡片@联系人的功能。如您需要使用该功能，请正确填写对应IM工具的ID号。目前飞书、企业微信的@联系人功能必须依赖该字段，钉钉暂不依赖该字段。注意：仅验证过的手机号可以在通知策略中使用电话的通知方式，验证手机号的操作，请参见[验证手机号](https://help.aliyun.com/zh/arms/alarm-operation-center/contacts)。

###### 新建联系人组（可选）

创建通知策略时，您可以将联系人组指定为通知对象，当通知策略的匹配规则被触发时，ARMS告警管理会向该联系人组中的所有通知对象通过电话、短信、邮件、钉钉等方式发送告警通知。

注：您需要在创建联系人或钉钉/企业微信/飞书机器人后，再创建联系人组。

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 通知对象**。
2. 在**联系人**页签单击**新建联系人组**。
3. 在**新建联系组**对话框中输入**组名**，选择**告警联系人**，并单击**确认**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972986.png)创建完成后，对应的联系人组将显示在**联系人**页签的左侧列表中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973016.png)

##### 告警机器人

###### 钉钉机器人

在创建钉钉机器人之前，您需要完成以下步骤：

- 已在钉钉客户端创建用于接收告警通知的钉钉群。
- 已添加自定义钉钉机器人并获取Webhook地址，具体操作，请参见[获取钉钉机器人Webhook地址](https://help.aliyun.com/zh/arms/alarm-operation-center/obtain-the-webhook-url-of-a-dingtalk-chatbot)。

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 通知对象**。
2. 单击**钉钉/飞书/企微**页签，然后单击**钉钉**。
3. 在弹出的面板设置以下参数，然后单击**确定**。**参数****说明****名称**自定义钉钉机器人的名称。**签名密钥**可选，如配置了密钥则会通过加签的方式进行钉钉认证。如果没有配置密钥，默认使用关键字白名单的方式进行认证，白名单关键字为**告警**。更多信息，请参见[钉钉官方文档](https://open.dingtalk.com/document/robots/customize-robot-security-settings)。**机器人地址**输入钉钉机器人的Webhook地址。**机器人是否发送每日统计**选中后，需要输入每日统计信息发送的时间点，使用英文逗号（,）分隔多个发送时间点，时间点格式为`HH:SS`。ARMS告警管理将在设置的时间点发送今日产生告警的总数、解决数和待解决数。**卡片内容配置**自定义告警通知卡片样式和内容。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973017.png)

###### 企业微信机器人

在ARMS告警管理中创建企业微信机器人后，您可以在通知策略中指定对应的企业微信群用于接收告警。当通知策略的匹配规则被触发时，系统会自动向您指定的企业微信群发送告警通知。企业微信群收到通知后，您可以在企业微信群中对告警进行管理。

在创建企业微信机器人之前，请确认您已在企业微信中创建用于接收告警通知的企业微信群。

由于企业微信对应用服务商的授权许可限制，ARMS仅提供不超过20个企业微信接口调用许可。请您合理安排在企业微信内处理告警的值班人员，非强需求人员建议在ARMS控制台处理告警。

第一步，获取机器人Webhook地址：

1. 打开并登录企业微信。
2. 单击企业微信群右上角的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972987.png)图标，然后单击**群机器人**。
3. 在**群机器人**页面，单击**添加机器人**，然后在**机器人**页面，单击**添加**。
4. 在**添加机器人**页面自定义机器人名称，然后单击**添加**。
5. 单击**复制**，保存企业微信机器人的Webhook地址。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973018.png)

第二步，在ARMS控制台中创建机器人：

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 通知对象**。
2. 单击**钉钉/飞书/企微**页签，然后单击**企业微信**。
3. 在新建机器人面板设置以下参数，然后单击**确定**。**配置项****说明****名称**自定义企业微信机器人的名称。**机器人地址**输入企业微信机器人的Webhook地址。**机器人是否发送每日统计**选中后，需要输入每日统计信息发送的时间点，使用英文逗号（,）分隔多个发送时间点，时间点格式为`HH:SS`。ARMS告警管理将在设置的时间点发送今日产生告警的总数、解决数和待解决数。**卡片内容配置**自定义告警通知卡片样式和内容。

###### 飞书（Lark）机器人

在ARMS告警管理中创建飞书（Lark）机器人后，您可以在通知策略中指定对应的飞书（Lark）群用于接收告警。当通知策略的匹配规则被触发时，系统会自动向您指定的飞书（Lark）群发送告警通知。飞书（Lark）群收到通知后，您可以在群中对告警进行管理。

第一步，获取机器人Webhook地址：

1. 打开并登录飞书（Lark）。
2. **（可选）**单击**+**图标，然后单击**创建群组**，新建一个用于发送告警的群组。
3. 在飞书群右上角选择![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973019.png)**> 设置**，然后单击**群机器人**。
4. 在**群机器人**面板单击**添加机器人**，然后选择自定义机器人。
5. 在机器人配置页设置机器人名称和描述，然后单击**添加**。
6. 复制Webhook地址，然后选中**自定义关键词**并输入关键词为`告警`。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973020.png)

第二步，在ARMS控制台中创建机器人：

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 通知对象**。
2. 单击**钉钉/飞书/企微**页签，然后单击**飞书/Lark**。
3. 在新建机器人面板设置以下参数，然后单击**确定**。**参数****说明****名称**自定义飞书（Lark）机器人的名称。**机器人地址**输入飞书机器人的Webhook地址。**机器人是否发送每日统计**选中后，需要输入每日统计信息发送的时间点，使用英文逗号（,）分隔多个发送时间点，时间点格式为`HH:SS`。ARMS告警管理将在设置的时间点发送今日产生告警的总数、解决数和待解决数。**卡片内容配置**自定义告警通知卡片样式和内容。

##### 通过Webhook自定义告警通知对象

创建通知策略时，您可以将告警通知发送到自定义的Webhook地址中。ARMS告警管理支持对第三方通知对象发送Webhook告警，本文以飞书为例，介绍如何创建Webhook告警。

第一步，获取Webhook地址：

请在PC端配置飞书Webhook机器人。

1. 打开并登录飞书。
2. 单击**+**图标，然后单击**创建群组**，新建一个用于发送告警的群组。
3. 单击群组设置图标，然后单击**群机器人**页签。
4. 在**群机器人**页签单击**添加机器人**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972988.png)
5. 在**添加机器人**面板选择**Custom Bot**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973021.png)
6. 在配置页设置**显示名称**和**描述**，然后单击**添加**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973022.png)
7. 在**添加情况**区域单击**复制**，然后单击**完成**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p973023.png)

第二步，创建Webhook联系人：

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 通知对象**。
2. 单击**Webhook集成**页签，然后单击**新建Webhook**。
3. 在**新建Webhook**对话框中输入以下配置信息。**参数****说明**Webhook名称必填，自定义Webhook名称。Post和Get必填，设置请求方法。URL不可超过256个字符。此例中选择**Post**，并将第一步中保存的Webhook地址粘贴至右侧文本框。Header和Param非必填，设置请求头，不可超过200个字符。 单击**+添加**，可以添加其他Header信息或Param信息。默认请求头为**Content-Type: text/plain; charset=UTF-8**，Header和Param个数总数不能超过6个。此例中设置以下两个**Header**：Arms-Content-Type : jsonContent-Type : application/json通知模板告警触发时发送的通知模板，非必填，在Post方法下出现，可使用$content占位符输出通知内容，不可超过500个字符。更多信息，请参见[配置通知模板和Webhook模板](https://help.aliyun.com/zh/arms/alarm-operation-center/configure-notification-templates-and-webhook-templates)。通知模板如下：`{
 "告警名称":"{{ .commonLabels.alertname }}{{if .commonLabels.clustername }}",
 "集群名称":"{{ .commonLabels.clustername }} {{ end }}{{if eq "app" .commonLabels._aliyun_arms_involvedObject_kind }}",
 "应用名称":"{{ .commonLabels._aliyun_arms_involvedObject_name }} {{ end }}",
 "通知策略":"{{ .dispatchRuleName }}",
 "告警时间":"{{ .startTime }}",
 "告警内容":"{{ for .alerts }} {{ .annotations.message }} {{ end }}"
}`此处以飞书为例可以设置如下文本格式：`{
 "msg_type": "text",
 "content": {
 "text": "告警名称: {{ .commonLabels.alertname }}\n{{if .commonLabels.clustername }}集群名称: {{ .commonLabels.clustername }}\n{{ end }}{{if eq "app" .commonLabels._aliyun_arms_involvedObject_kind }}应用名称: {{ .commonLabels._aliyun_arms_involvedObject_name }}\n{{ end }}通知策略: {{ .dispatchRuleName }} \n告警时间: {{ .startTime }} \n告警内容: {{ for .alerts }} {{ .annotations.message }}\n {{ end }}"
 }
}`恢复模板告警恢复时发送的通知模板，非必填，在Post方法下出现，可使用$content占位符输出通知内容，不可超过500个字符。更多信息，请参见[配置通知模板和Webhook模板](https://help.aliyun.com/zh/arms/alarm-operation-center/configure-notification-templates-and-webhook-templates)。恢复模板如下：`{
 "告警名称":"{{ .commonLabels.alertname }}{{if .commonLabels.clustername }}",
 "集群名称":"{{ .commonLabels.clustername }} {{ end }}{{if eq "app" .commonLabels._aliyun_arms_involvedObject_kind }}",
 "应用名称":"{{ .commonLabels._aliyun_arms_involvedObject_name }} {{ end }}",
 "通知策略":"{{ .dispatchRuleName }}",
 "恢复时间":"{{ .endTime }}",
 "告警内容":"{{ for .alerts }} {{ .annotations.message }} {{ end }}"
}`此处以飞书为例可以设置如下文本格式：`{
 "msg_type": "text",
 "content": {
 "text": "告警名称: {{ .commonLabels.alertname }}\n{{if .commonLabels.clustername }}集群名称: {{ .commonLabels.clustername }}\n{{ end }}{{if eq "app" .commonLabels._aliyun_arms_involvedObject_kind }}应用名称: {{ .commonLabels._aliyun_arms_involvedObject_name }}\n{{ end }}恢复时间: {{ .startTime }} \n通知策略: {{ .dispatchRuleName }} \n恢复告警内容: {{ for .alerts }} {{ .annotations.message }}\n {{ end }}"
 }
}`
4. **可选：**单击**发送测试**，验证配置是否成功。
5. 单击**确定**。

#### 通知策略管理

##### 通知策略

通过设置通知策略，您可以制定针对告警事件的匹配规则。当匹配规则被触发时，系统会以您指定的通知方式向通知对象发送告警信息，以提醒通知对象采取必要的问题解决措施。

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 通知策略**。
2. 在**通知策略**页面单击**新建通知策略**。
3. 在**新建通知策略**页面顶部设置通知策略名称。
4. 在**匹配规则**区域设置告警事件的匹配规则。选择数据来源。指定来源：通知策略会针对指定来源（集成）的告警事件进行匹配规则过滤并发送通知。无预设来源：通知策略会针对所有告警事件进行匹配规则过滤并发送通知。设置匹配规则表达式，您可以自定义标签或选择已有的标签。已有的标签包括：告警规则表达式指标中携带的标签。可观测监控 Prometheus 版告警规则创建标签的操作，请参见[Prometheus告警规则](https://help.aliyun.com/zh/arms/prometheus-monitoring/create-an-alert-rule-for-a-prometheus-instance)。ARMS系统自带的默认标签，默认标签说明如下。**分类****标签****说明**常用字段alertname告警名称。clustername集群名称。severity告警等级：P1P2P3P4默认namespace[命名空间](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)。pod_name[Pod名称](https://kubernetes.io/docs/concepts/workloads/pods/)。系统预置字段_aliyun_arms_integration_name集成名称，ARMS默认上报的告警集成名称为ARMS-DEFAULT。_aliyun_arms_involvedObject_id告警对象ID。_aliyun_arms_involvedObject_name告警对象名称。_aliyun_arms_region_id地域ID。_aliyun_arms_alert_rule_id告警规则ID。_aliyun_arms_alert_type告警规则类型：101：Prometheus告警5：应用监控告警4：前端监控告警如果需同时满足**多个**匹配规则才告警，则单击**添加条件**编辑第二条匹配规则条件。如果需满足**任意一个**匹配告警事件规则就告警，则单击**添加规则**编辑第二条匹配规则。单击**下一步**。
5. 在**事件分组**区域，设置告警事件是否需要分组，然后单击**下一步**。不需要分组：所有告警事件会以一条告警信息发送给处理人。设置分组字段：字段内容相同的告警事件会汇总到同一告警发送通知。
6. 在**通知对象**区域，设置以下参数。单击**+添加通知对象**选择通知对象。通知对象类型：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3086581571/p972992.png)联系人：选择具体联系人后还需选择使用电话、短信或邮件的通知方式。联系人组：选择具体联系人组后还需选择使用电话、短信或邮件的通知方式。排班：选择具体排班后还需选择使用电话、短信或邮件的通知方式。钉钉/飞书/企微：通过钉钉、飞书或企业微信发送告警通知。通用Webhook：通过Webhook发送告警通知。选择告警恢复后是否发送恢复通知。发送恢复通知：当告警下面全部事件都恢复时，告警状态是否自动恢复为已解决。当告警恢复时，系统将会发送通知给告警处理人。设置通知模板，更多信息，请参见[配置通知模板和Webhook模板](https://help.aliyun.com/zh/arms/alarm-operation-center/configure-notification-templates-and-webhook-templates)。设置通知时段，告警会在设置的通知时段内发送告警通知。**可选：**选择告警需要推送到的工单系统。集成工单系统的操作，请参见[通知集成](https://help.aliyun.com/zh/arms/alarm-operation-center/overview-10)。单击**下一步**。
7. 在**重复/升级/恢复策略**区域设置告警是否需要重复通知或使用升级策略，然后单击**下一步**。告警是否需要重复通知：如果需要重复通知，设置重复频率。当告警未恢复时，告警会以设置的重复频率循环发送告警信息直至告警恢复。告警是否配置升级策略：不需要升级策略，告警未恢复状态下只发送一次。选择升级策略后，告警未恢复状态下，告警通知将会根据升级策略发送通知给其他通知对象。告警是否开启手动恢复：开启手动恢复后，当告警事件在告警集成中设置的自动恢复时间内都没有再触发，告警不会自动恢复，必须人工干预调整状态。
8. 在**行动集成**区域可以设置告警触发或恢复后自动执行的行动。更多信息，请参见[通过ARMS行动集成执行告警预案](https://help.aliyun.com/zh/arms/alarm-operation-center/implement-alarm-plan-through-arms-action-integration)。
9. 设置完成后，单击**保存**。

##### 静默策略

ARMS告警管理的静默策略可以收敛告警，减少告警风暴的产生。通过设置静默策略，您可以制定针对告警事件的匹配规则。当规则被触发时，对应的事件将会被静默，不会被通知策略匹配到。

静默策略优先于通知策略，即已被静默策略匹配到的告警事件将会被静默，无法再进行通知策略的事件匹配。

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 静默策略**。
2. 在**静默策略**页面单击**新建静默策略**。
3. 在**新建静默策略**页面设置静默策略名称。
4. 在**静默事件匹配规则**区域设置静默事件的匹配规则。
5. 设置**静默规则生效时间**。持续生效循环生效：选择**每天**或**每周**循环，然后单击**添加**，设置静默规则生效时间段。自定义时间段：单击**添加**，设置静默规则生效时间段。

1. 设置完成后，单击**保存**。

##### 升级策略

对于长期未解决的告警，可以选择升级通知来提醒联系人及时解决。在通知策略中添加升级策略后，系统会以您指定的通知方式向处理人发送告警信息，以提醒处理人采取必要的问题解决措施。

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 升级策略**。
2. 在**升级策略**页面单击**创建升级策略**。
3. 在右侧区域顶部文本框中输入升级策略名称。
4. 在升级规则区域，设置通知条件，即当告警在一段时间内未被认领或未被解决时发送告警通知。例如：当告警10分钟未认领时发送升级通知。**参数****说明****通知人/排班**选择通知对象。创建通知对象的操作，请参见[创建告警通知对象](#m5NVJ)。**通知方式**通知方式支持钉钉、邮件、WebHook、短信和电话，可以同时选择多种方式。**说明：**未验证手机号的联系人无法使用电话通知方式。验证手机号的操作，请参见[验证手机号](https://help.aliyun.com/zh/arms/alarm-operation-center/contacts)。**通知时段**满足通知条件的告警会在设置的通知时段内发送告警通知。**重复次数**重复发送告警通知的次数。当告警不满足通知条件后，告警通知将不再发送。**说明：**至少发送一次告警，即设置为0时也会发送一次告警。
5. 设置完成后，单击**保存**。

## 故障排除

### 为什么告警选择了不指定通知策略，还是能收到告警通知？

无论告警规则中是否指定了通知策略，告警都会发送到告警管理。只要该告警满足了其他通知策略的分派条件就会通过其他通知策略进行通知。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-263（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
