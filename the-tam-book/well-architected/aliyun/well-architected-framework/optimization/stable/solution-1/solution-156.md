<!-- source: https://help.aliyun.com/zh/well-architected/solution-156 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929426 -->

# 多账号统一监控告警方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972211.png)

云原生时代，企业IT基础设施的规模越来越大，越来越多的系统和服务被部署在云环境中。为了监控这些复杂的IT环境，企业通常会选择使用异构监控系统，例如Prometheus、云监控、日志服务等，以获取更全面的监控数据，以便更好地了解其IT基础设施的运行状况和性能表现。然而，这种异构监控系统也带来了一些问题，其中最显著的是告警信息分散。由于不同的监控系统可能会产生不同的告警信息，这些信息可能会分散在各个不同云账号下的系统中，导致企业很难全面了解其IT系统的告警状况。这使得响应告警变得更加困难，同时也增加了人工管理的复杂性和工作量。

另外随着企业将越来越多的系统部署在云环境，往往会选择多账号来隔离不同业务。用户在一个云账号中只能查看本账号的告警信息，无法处理跨账号的告警信息。但在运维部门（公司）同时使用多个云账号的场景下，运维人员则需要在每个云账号下单独处理该账号的告警，使得运维成本增加。

为了解决这些问题，企业需要一种更加统一和集中的告警管理方案，以确保告警信息能够及时到达正确的人员，以便他们能够快速采取必要的措施来应对潜在的问题。

## 方案优势

### 支持跨账号场景告警统一

对于使用多账号的企业客户来说，每个账号都会有相关告警信息，对于运维部门无法统一查看IT系统的告警信息，无法处理跨账号的告警信息。通过这个方案可以将不同账号内监控系统告警方式统一。

### 支持跨监控系统告警统一

对于使用了多种监控系统的用户来说，不同监控系统带来的告警信息比较分散，导致运维部门无法全面了解其IT系统的告警状况，通过这个方案可以将不同异构的监控系统告警方式统一。

## 客户场景

### 监控工具碎片化导致告警分散

#### 场景描述

系统资源层、云服务应用层、业务监控层，为了监控这些复杂的IT环境，由于各层资源分属不同的团队进行管理，导致采用了多种监控系统，例如 Prometheus、Grafana、Skywalking、阿里云云监控、阿里云 ARMS 等，以获取更全面的监控数据和更好的了解运行状态和性能表现。然而多种监控系统的并存带来的其中一个显著问题是告警信息的分散，不同的监控系统产生不同的告警信息，通过不一致的方式通报给告警处理人，而告警的排查通常需要多个团队共同合作进行处理，纵横交错的告警处理增加了人员响应的复杂性和工作量，疲于应付的程度往往远超出了告警处理人员的日常负荷。

#### 适用客户

- 使用了多款监控工具，希望将告警统一

### 多账号架构使得跨账号处理告警充满挑战

#### 场景描述

在阿里云，资源是按照账号进行租户隔离的。用户在一个云账号中只能查看本账号的告警信息，无法处理跨账号的告警信息。但在运维部门（公司）同时使用多个云账号的场景下，运维人员则需要在每个云账号下单独处理该账号的告警，使得运维成本增加。

#### 适用客户

- 使用多个阿里云账号的企业客户。
- 希望能够统一处理多账号内监控告警。

## 方案架构

### 统一告警方案

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972210.png)

告警统一集成管理分为默认告警集成和三方产品集成两部分。其中默认告警集成了ARMS各子产品的告警，如应用监控告警、前端监控告警、Prometheus告警、云拨测告警等。三方产品集成支持通过简单配置接入任意告警源产生的告警，从而在ARMS上一站式处理分布在各个云上云下IDC系统产生的告警，实现统一处理告警的目的。

##### 告警事件的数据结构

ARMS告警事件的数据结构参考开源AlertManager的数据结构，数据结构包括：

- Labels（标签）：告警元数据，一组标签唯一标识一个事件，标签相同的事件为同一个事件，重复上报会进行合并，例如：“alertname: 告警名称 ”。
- Annotations（注释）：注释是告警事件的附加描述，注释不属于元数据。例如：“message: 告警内容”。
- StartsAt（告警开始时间）：告警事件开始时间。
- EndsAt（告警结束时间）：告警事件结束时间。
- GeneratorUrl（事件URL地址）：告警事件URL地址。

##### 告警事件去重、降噪

快速接入各类告警信息，通过自动去重、规则压缩、算法降噪，帮助运维团队减少告警，避免告警风暴。通过分派、排班、通知等功能，快速实现告警流程化管理，帮助运维团队更快响应告警，恢复告警，提升告警管理能力。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| ARMS | [ARMS](https://help.aliyun.com/product/34364.html) Prometheus监控全面对接开源Prometheus生态，支持类型丰富的组件监控，提供多种开箱即用的预置监控大盘，且提供全面托管的Prometheus服务。借助ARMS Prometheus监控，用户无需自行搭建Prometheus监控系统，因而无需关心底层数据存储、数据展示、系统运维等问题。 | 收费，详情参见[产品计费](https://www.aliyun.com/ntms/price/detail/arms_detail) |
| 云监控 | [云监控](https://help.aliyun.com/product/28572.html)（CloudMonitor） 是一项针对阿里云资源和互联网应用进行监控的服务。云监控服务可用于收集获取阿里云资源的监控指标，探测互联网服务可用性，以及针对指标设置警报。 | 部分功能免费，高级功能收费。具体可以查看[产品计费](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/billing-overview)。 |
| 日志服务 | [日志服务](https://help.aliyun.com/product/28958.html)（SLS）是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[产品计费](https://www.aliyun.com/price/detail/sls) |

## 安全性

### ARMS访问控制

借助访问控制RAM的RAM用户，您可以实现权限分割的目的，按需为RAM用户赋予不同权限，并避免因暴露阿里云账号密钥造成的安全风险。具体可以参考[官网文档](https://help.aliyun.com/zh/arms/security-and-compliance/overview-8)。

### 云监控访问控制

对于各业务账号内配置云监控告警相关配置，需要借助访问控制RAM。可以分配以下的系统权限

**系统策略**：从**权限策略名称**列表，选择需要的权限。

| **权限策略名称** | **说明** |
| --- | --- |
| AliyunCloudMonitorFullAccess | 管理云监控的权限。 |
| AliyunCloudMonitorReadOnlyAccess | 只读访问云监控的权限。 |

### 日志服务告警管理访问控制

#### 极简授权

使用阿里云账号登录[RAM控制台](https://ram.console.aliyun.com/)，为RAM用户授予日志服务管理权限（AliyunLogFullAccess）。具体操作，请参见[为RAM用户授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-the-ram-user)。

#### 自定义权限策略

可以参考[授予RAM用户告警操作权限](https://help.aliyun.com/zh/sls/user-guide/authorize-a-ram-user-to-manage-alerts?spm=a2c4g.11186623.0.0.37eb59af2cWWQ2)

## 注意事项

### 重复报警问题

云监控里面会有报警通知，如果配置了账号内的告警转发，那当前账号内云监控的报警就需要关闭掉。但云监控目前还不具备这个能力，可以分配一个空的联系人。这样通知策略就无法正常下发到联系人。

## 实施步骤

### 实施准备

已经按照LandingZone的多账号标准架构实施完成多账号环境。对应演示的多账号架构环境如下：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972207.png)

本方案会在运维账号内创建统一告警，将账号A、账号B内的告警信息统一在运维账号完成。部分账号说明：

- 运维账号（C账号）：会在这个账号内完成集中的ARMS告警规则，定义报警相关通知策略。
- 业务账号（A、B账号）：已经使用了企业云监控或者ARMS应用监控、日志监控服务或者其他自建的监控系统，用于采集云服务及业务相关指标。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长60分钟。

### 场景规划

本文会列举常见的几个场景来介绍实施步骤

- 场景1：ARMS告警集成
- 场景2：云监控告警集成
- 场景3：日志服务告警集成

#### 场景1：ARMS告警集成

ARMS告警集成的范围包含以下ARMS产品（应用监控、前端监控、可观测监控Prometheus版、应用安全、云拨测等），完成集成后，ARMS子产品的告警都会转发到指定账号下的ARMS告警中心。

##### 步骤一：创建跨账号集成

在C账号下创建ARMS告警管理的集成，并获取集成密钥。

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 集成**。
2. 在**集成**页面的**告警集成**页签单击**ARMS**。
3. 在**新建ARMS集成**对话框输入集成名称、描述和告警事件自动恢复时间，然后单击**保存**。**说明：**告警事件自动恢复时间：当告警事件在设置的时间内都没有再触发，告警事件将会自动恢复。配置完成后，在**告警集成**页签可以查看已创建的ARMS集成。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972214.png)
4. 在**告警集成**页签，复制并保存ARMS集成地址。

##### 步骤二：配置跨账号集成

1. 使用B账号和C账号分别登录[ARMS控制台](https://arms.console.aliyun.com/#/home)。
2. 在左侧导航栏选择**告警管理 > 集成**。
3. 在**告警集成**页签的**ARMS-DEFAULT**集成右侧**操作**列，单击**转发告警**。
4. 在弹出的**ARMS-DEFAULT转发告警**对话框，输入A账号的集成地址，然后单击**确认**。配置完成后，**ARMS-DEFAULT**集成右侧新增**停止转发**。**说明：**单击**停止转发**，在弹出的对话框中单击**确认**，然后单击**保存**。可以停止将B账号或C账号的ARMS告警上报至A账号中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972215.png)

##### 步骤三：配置C账号下的通知策略

通过设置通知策略，可以制定针对告警事件的匹配规则。当匹配规则被触发时，系统会以您指定的通知方式向通知对象发送告警信息，以提醒通知对象采取必要的问题解决措施。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972208.png)

按照这个流程完成通知策略配置。具体可以参考：[ARMS通知策略](https://help.aliyun.com/zh/arms/alarm-operation-center/create-and-manage-notification-policies)。

#### 场景2：云监控告警集成

##### 步骤一：创建云监控跨账号集成

在C账号下创建云监控告警管理的集成，并获取集成密钥。

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 集成**。
2. 在**告警集成**页签单击**云监控**。
3. 在**新建云监控集成**对话框输入云监控集成的名称、描述和告警事件自动恢复时间。**说明：**告警事件自动恢复时间：当告警事件在设置的时间内都没有再触发，告警事件将会自动恢复。
4. 在**接入告警事件的产品**的**全部产品**区域，显示了云监控支持接入告警管理的产品，选择需要接入告警的产品，单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972216.png)图标，然后单击**保存**。**说明：**此功能会自动遍历选中的产品中配置的所有告警规则，在这些规则上自动修改告警的回调地址为**https://alerts.aliyuncs.com/api/v1/cm/callback/{{token}}**，其中，**{{token}}**为集成创建时自动生成的密钥。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972217.png)配置完成后，在**告警集成**页签可以查看已创建的云监控集成。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972218.png)

##### 步骤二：配置云监控跨账号集成

将A账号和B账号的云监控中产生的告警上报至C账号的告警管理中。

1. 在**集成**页面的**告警集成**页签，复制目标云监控集成的集成地址。
2. 登录[云监控控制台](https://cloudmonitor.console.aliyun.com/)。
3. 在左侧导航栏，选择**报警服务 > 报警规则**。
4. 在**报警规则**页面，单击目标报警规则**操作**列的**修改**。
5. 在弹出的面板的**高级设置**区域设置报警回调地址为云监控集成的集成地址。
6. 单击**确认**。

##### 步骤三：配置C账号下的通知策略

通过设置通知策略，可以制定针对告警事件的匹配规则。当匹配规则被触发时，系统会以您指定的通知方式向通知对象发送告警信息，以提醒通知对象采取必要的问题解决措施。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972209.png)

按照这个流程完成通知策略配置。具体可以参考：[ARMS通知策略](https://help.aliyun.com/zh/arms/alarm-operation-center/create-and-manage-notification-policies)

#### 场景3：日志服务告警集成

##### 步骤一：创建日志服务跨账号集成

在C账号下创建日志服务告警管理的集成，并获取集成密钥。

1. 登录[ARMS控制台](https://arms.console.aliyun.com/#/home)，在左侧导航栏选择**告警管理 > 集成**。
2. 在**集成**页面的**告警集成**页签单击**日志服务**。
3. 在弹出的对话框输入日志服务集成的名称、描述和告警事件自动恢复时间。**说明：**告警事件自动恢复时间：当告警事件在设置的时间内都没有再触发，告警事件将会自动恢复。
4. 在**接入告警事件的Project**的**全部Project**区域，显示了阿里云日志服务的所有Project，选择需要接入告警的Project，单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972219.png)图标，然后单击**保存**。**说明：**此功能会自动遍历选中的Project中配置的所有告警规则，在这些规则上自动新增告警的请求地址为**https://alerts.aliyuncs.com/api/v1/events/{{token}**，其中，**{{token}}**为集成创建时自动生成的密钥。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972220.png)配置完成后，在**告警集成**页签可以查看已创建的日志服务集成。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972212.png)

##### 步骤二：配置日志服务跨账号集成

将A账号和B账号的日志服务中产生的告警上报至C账号的告警管理中。

1. 在**集成**页面的**告警集成**页签，复制目标日志服务集成的集成地址。
2. 登录[日志服务控制台](https://sls.console.aliyun.com/)。
3. 单击目标Project，然后在左侧导航栏单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972221.png)图标，即告警图标。
4. 在**告警中心**页面选择**告警管理 > Webhook集成**，然后在**Webhook集成**页面单击**新建**。
5. 在弹出的对话框中添加ARMS告警管理的通用Webhook。其中，名称设置为**ARMS告警管理**，类型选择**通用Webhook**，其他参数可按照界面提示进行相关配置。
6. 在**告警中心**页面选择**告警管理 > 内容模板**，然后单击目标模板**操作**列的**修改**，在弹出的对话框中单击**WebHook-自定义**页签，并配置如下所示的发送内容，然后单击**确认**。`{
 "uid": "{{ alert.aliuid }}",
 "project": "{{ alert.project }}(https://sls.console.aliyun.com/#/project/{{ alert.project }}/categoryList)",
 "trigger": "{{ alert.alert_name }}",
 "condition": "{{ alert.condition }}",
 "context": "{{ alert.results[0].raw_results }}",
 "message": " [Uid] {{ alert.aliuid }}\n\n> [Project] [{{ alert.project }}](https://sls.console.aliyun.com/#/project/{{ alert.project }}/categoryList)\n\n> [Trigger] {{ alert.alert_name }}\n\n> [Condition] {{ alert.alert_name }}\n\n> [Message] 通知内容\n\n> [Context] {{ alert.results[0].raw_results }}\n\n> [查看详情]({{ alert.query_url }})"
}`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972213.png)
7. 在**告警中心**页面单击**规则/事务**页签，然后单击目标规则**操作**列的**编辑**，在弹出的对话框中展开**高级配置**，然后在**告警策略**区域选择**极简模式**，并根据界面提示配置通用Webhook的通知渠道，配置完成后单击**确定**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1086581571/p972222.png)

## 相关内容

- 应用实时监控ARMS-[链路追踪](https://help.aliyun.com/zh/arms/tracing-analysis/preparations)
- [ARMS Prometheus监控](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-managed-service-for-prometheus-to-monitor-an-ack-cluster)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-156（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
