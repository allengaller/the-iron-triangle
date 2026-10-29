<!-- source: https://help.aliyun.com/zh/well-architected/solution-271 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929033 -->

# AccessKey风险检测与泄露应急方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968846.png)

访问密钥（AccessKey）是您调用阿里云API时用于完成身份验证的凭证，AccessKey泄露会对该账号下所有资源的安全带来威胁，产生非预期的费用以及恶意勒索等。本文介绍了AccessKey风险检测与泄露应急的方案，帮助您持续对AccessKey进行检测，及时识别风险并进行处理。同时在AccessKey发生泄漏后，通过应急处理方案，帮助您快速收敛泄露风险，避免造成更大范围的身份凭证冒用风险。

## 方案优势

### 实时开源代码检测

云安全中心AK泄露检测功能支持实时检测GitHub平台公开源代码（多为企业员工私自上传并不小心公开）中是否含有AccessKey信息，在发现AccessKey泄露时向您发送通知，帮助您及时发现外泄的风险。

### 快速收敛泄露面积

通过限制AccessKey调用的来源IP和拒绝高危权限等应急操作，您可以快速收敛泄露后AccessKey的暴露面积，将AccessKey调用来源控制在可信的网络环境内，并且只允许进行低风险操作，以此减少AccessKey泄露带来的危害。长期来看，您可以使用STS Token来代替AccessKey的使用，避免AccessKey的泄露风险。

## 客户场景

### 应对AccessKey泄露风险

#### 场景描述

企业使用AccessKey调用阿里云API访问云上资源，对AccessKey缺乏有效管控，存在或担心AccessKey泄露，对该账号下所有资源的安全带来威胁，产生非预期的费用以及恶意勒索等。希望对AccessKey进行风险检测，同时在出现泄露状况后，能够进行有效的应急处置，减少AccessKey泄露给企业带来的风险。

#### 适用客户

- 使用AccessKey调用阿里云API访问云上资源。

## 方案架构

本方案通过云安全中心、操作审计、云治理中心，从攻击视角、账号调用、历史行为等角度对AccessKey进行风险检测，及时识别风险并进行处理。同时您可以在云安全中心配置报警，在发生AccessKey泄露后，及时收到报警信息。AccessKey泄露后，您首先需要通过操作审计确认该AccessKey的使用情况。对于业务没有真实使用的AccessKey（比如闲置的AccessKey），您可以直接禁用该AccessKey。而对于业务真实使用的AccessKey，首先通过限制来源IP和拒绝高危权限进行应急处理，快速收敛泄露后AccessKey的暴露面积，将AccessKey调用来源控制在可信的网络环境内，并且只允许进行低风险操作，以此减少AccessKey泄露带来的危害。应急处理完后，您需要尽快完成AccessKey的轮转，禁用掉发生泄露的AccessKey。长期来看，建议您使用STS Token来代替AccessKey的使用，彻底避免AccessKey的泄露风险。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968849.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 访问控制RAM | [访问控制RAM（Resource Access Management）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |
| 操作审计 | [操作审计（ActionTrail）](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)是阿里云提供的云账号资源操作记录的查询和投递服务，可用于安全分析、资源变更追踪以及合规性审计等场景。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/actiontrail/product-overview/billing-1)。 |
| 云治理中心 | [云治理中心](https://help.aliyun.com/zh/cgc/product-overview/what-is-cloud-governance-center)是企业在阿里云上进行多账号集中IT治理的平台。通过步骤式向导和自动化流程帮助企业快速搭建Landing Zone，建立安全合规的多账号环境，并对企业在云上的多账号环境进行持续治理。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/cgc/product-overview/billing/)。 |
| 云安全中心 | [云安全中心](https://help.aliyun.com/zh/security-center/what-is-security-center)是一款集持续监测、深度防御、全面分析、快速响应能力于一体的云上安全管理平台。基于云原生架构优势，提供云上资产管理、配置核查、主动防御、安全加固、云产品配置评估和安全可视化等能力，可有效发现和阻止病毒传播、黑客攻击、勒索加密、漏洞利用、AK泄漏等风险事件，帮助您实现一体化、自动化的安全运营闭环，保护多云环境下的主机、容器、虚拟机等工作负载安全性，同时满足监管合规要求。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/security-center/billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 访问密钥（AccessKey） | 访问密钥AccessKey（简称AK）是阿里云提供给用户的永久访问凭据，一组由AccessKey ID和AccessKey Secret组成的密钥对。发起的请求会携带AccessKey ID和AccessKey Secret加密请求内容生成的签名，进行身份验证及请求合法性校验。 |
| 安全令牌（STS Token） | 阿里云STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。RAM提供RAM用户和RAM角色两种身份。其中，RAM角色不具备永久身份凭证，而只能通过STS获取可以自定义时效和访问权限的临时身份凭证，即安全令牌（STS Token）。 |
| 程序身份 | 身份是指在云环境中执行操作的实体。云上主要有两种身份类型：人员身份和程序身份。程序身份代表应用程序或服务，往往是使用AccessKey或者STS Token通过阿里云的 OpenAPI 来访问云上的资源和数据。 |

## 安全性

### 云治理中心服务关联角色

云治理中心服务关联角色（AliyunServiceRoleForGovernance）具有资源目录、RAM、配置审计等产品的操作权限，方便云治理中心对您的账号进行IT成熟度治理检测。关于服务关联角色的更多信息，请参见[云治理中心服务关联角色](https://help.aliyun.com/zh/cgc/security-and-compliance/service-linked-roles-in-cloud-governance-center)。

### 云安全中心服务关联角色

在特定场景中，为了顺利执行某个功能，云安全中心需要借助服务关联角色获取对其他云服务的访问权限。关于服务关联角色的更多信息，请参见[云安全中心服务关联角色](https://help.aliyun.com/zh/security-center/security-and-compliance/service-linked-roles-for-security-center)。

## 注意事项

### AccessKey网络访问限制策略

- AccessKey网络访问限制策略功能目前处于邀测阶段，请先联系阿里云的服务经理，申请体验资格后才能进行试用。
- AccessKey网络访问限制策略对除云消息队列RocketMQ版、云消息队列RabbitMQ版、云消息队列MQTT版、事件总线EventBridge、轻量消息队列、云监控（通过HTTP上报事件监控数据功能）、实时数仓Hologres以外的所有云产品生效，未支持的云产品上线时间由云产品另行通知。
- 如果您需要通过专有网络策略限制VPC内的IP地址访问，请确保您是通过VPC接入地址访问阿里云API，否则依然会通过公网访问阿里云，不受专有网络策略限制。

### 操作审计AccessKey审计支持的云服务及事件

AccessKey审计当前支持的事件与操作审计支持的事件相同，后续将持续增加新的事件。操作审计支持的事件列表，请参见[操作审计支持的事件](https://help.aliyun.com/zh/actiontrail/product-overview/services-that-work-with-actiontrail)。

## 实施步骤

### 实施准备

- 本方案会使用云治理中心对云上资源进行全方位检测，包括AccessKey的安全使用。请确保您已经开通了云治理中心，详情参见[开通云治理中心](https://help.aliyun.com/zh/cgc/getting-started/activate-cloud-governance-center)。
- 本方案会使用操作审计的审计事件洞察（Insight）能力，基于历史行为分析调用率异常的AccessKey，及时发现异常行为。请确保您已经开通了操作审计审计事件洞察功能，详情参见[Insights事件概览](https://help.aliyun.com/zh/actiontrail/user-guide/overview-of-insights-events)。
- 如果您需要使用操作审计内置的告警，监控AccessKey异常调用。请确保您将本账号所有的操作日志投递到日志服务(SLS)，详情参见[事件告警概述](https://help.aliyun.com/zh/actiontrail/user-guide/overview-3)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### AccessKey操作事件审计

无论是AccessKey风险检测还是AccessKey的泄露处置，都离不开对AccessKey使用情况的深度审查。通过查询AccessKey的基本信息、访问的云服务及相关IP地址和资源，帮助您及时发现和检查异常调用行为或者为确认AccessKey是否在真实使用以及AccessKey的轮转提供决策参考。您可以通过操作审计服务配合云产品自有的日志审计功能，实时追溯AccessKey的使用信息。

1. 首先，您需要对AccessKey最后使用时间以及调用的云服务进行审计，初步判断AccessKey的调用情况。以下几种情况，需要您特别关注。AccessKey没有最后使用时间或者最后使用时间距今已经比较久远，那么该AccessKey大概率已经闲置，建议您尽快确认并进行清理。AccessKey访问的云服务列表中，存在非业务预期的服务调用，那么该AccessKey可能存在非预期的滥用甚至泄露风险，建议您尽快确认，并按照下文措施采取相应应急处理。
2. 然后，您需要对AccessKey调用的每个云服务的操作行为事件进行审计，进一步明确AccessKey的调用行为，比如使用AccessKey从哪里（来源IP）对什么（云资源）进行了哪些操作（调用的API）。以下几种情况，需要您特别关注。AccessKey调用的事件列表中，存在敏感操作，比如遍历资源列表、资源删除和创建操作、[特权操作](https://help.aliyun.com/zh/ram/identify-over-authorization)等，建议您配合来源IP以及调用时间来判断其调用行为是否符合预期。AccessKey的调用时间中，存在非预期时间范围中的调用。比如，您的运维团队使用AccessKey进行本地运维，对于非工作时间段的调用行为就需要您进行关注，配合具体的调用事件和来源IP来判断其调用行为是否符合预期。AccessKey调用的来源IP列表中，存在非业务预期的IP地址，那么该AccessKey可能存在非预期的滥用甚至泄露风险。

阿里云的AccessKey的事件审计，只是帮助您追溯AccessKey的使用信息，您的运维团队和业务团队需要共同参与，对AccessKey的真实使用情况进行决策。AccessKey操作事件审计的详细操作，如下所示。

##### AccessKey最后使用时间和调用服务审计

您可以使用操作审计AccessKey审计，查询AccessKey最后使用时间和调用的云服务。AccessKey审计支持所有可以使用AccessKey访问的云服务。

1. 登录[操作审计控制台](https://actiontrail.console.aliyun.com/)。
2. 在左侧导航栏，单击**AccessKey审计**。
3. 在**AccessKey审计**页面，输入AccessKey ID，然后单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968847.png)图标。
4. 在**基本信息**区域，查询**AccessKey ID**、**账号ID**（阿里云账号ID或RAM用户ID）、**用户名**、**最后使用时间**和**最后使用服务**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968848.png)

##### 管控面操作事件审计

对于云服务管控面操作，您依然可以使用操作审计AccessKey审计，进一步查看该云服务下，AccessKey访问的所有事件列表、IP列表和资源列表。

1. 登录[操作审计控制台](https://actiontrail.console.aliyun.com/)。
2. 在左侧导航栏，单击**AccessKey审计**。
3. 在**AccessKey审计**页面，输入AccessKey ID，然后单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968850.png)图标。
4. 在**访问的云服务**区域，查询AccessKey访问的云服务列表、事件列表、IP列表和资源列表。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968851.png)

##### 数据面操作事件审计

对于云服务数据面操作，比如向OSS Bucket中上传下载文件，此类数据面操作事件操作审计暂未接入支持。比如下图所示，在操作审计的事件列表中，存在**未支持事件**。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968852.png)

因此需要您使用对应云产品自己的日志审计功能进行查询，比如下述常见的使用AccessKey操作数据面的云服务。

###### 对象存储OSS

使用OSS的实时日志查询功能，允许您在OSS控制台直接查询OSS的访问日志，帮助您完成OSS访问的操作审计、访问统计、异常事件回溯和问题定位等工作。具体操作，请参见[实时OSS日志查询](https://help.aliyun.com/zh/oss/user-guide/real-time-log-query/)。开启了实时OSS日志查询后，您可以通过查询语句`* and __topic__: oss_access_log and access_id: ${您的AccessKey ID}`搜索具体AccessKey的操作日志。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968854.png)

其中在日志信息中，您可以重点关注以下字段：

1. client_ip：来源IP。
2. operation：调用的操作行为。
3. bucket、object：操作的OSS Bucket和文件。

###### 日志服务SLS

使用CloudLens for SLS监测日志服务，包括Project内所有资产的创建、修改、更新、删除操作日志和数据读写日志等。具体操作，请参见[日志服务的监控方式概述](https://help.aliyun.com/zh/sls/user-guide/overview-of-log-service-monitoring-methods)。开启了CloudLens for SLS后，您可以通过以下操作步骤对日志服务的数据面操作事件进行审计。

1. 打开[日志服务控制台](https://sls.console.aliyun.com)，在日志应用中，点击CloudLens for SLS，进入SLS数据洞察。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968853.png)
2. 在左侧导航栏，单击**接入管理**，选择**SLS采集规则列表**页签，单击**创建采集规则**，创建日志类型为**详细日志**的采集规则。如果已经创建，则该步可以跳过。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968855.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968856.png)
3. 选择**存储目标库**页签。在目标库列表中，选择**详细日志**类型的日志库，点击日志库名称，查看不同地域下的操作日志。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968857.png)
4. 在日志库中，选择名为`internal-operation_log`的logstore，您可以通过查询语句`* and AccessKeyId: ${您的AccessKey ID}`搜索具体AccessKey的操作日志。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968858.png)

其中在日志信息中，您可以重点关注以下字段：

1. SourceIP：来源IP。
2. Method：调用的操作行为。
3. Project、LogStore：操作的SLS Project和LogStore。

#### AccessKey风险检测

##### 通过云治理中心进行配置巡检

云治理中心治理成熟度检测会从安全、效率、稳定和成本等维度对您的云资源进行全方位的检测，帮助您及时发现治理缺失和潜在风险，并提供友好的治理引导，帮助您完善云上IT治理的配置，降低云上IT治理的风险。其中就包括程序身份管理风险，比如：是否存在闲置的AccessKey、是否存在长时间未轮转的AccessKey等等。

1. 登录[云治理中心控制台](https://governance.console.aliyun.com)，在左侧导航栏，选择**卓越架构 > 治理成熟度检测**。
2. 在下方检测项列表筛选栏中，选择**凭据安全**。过滤AccessKey凭据相关的检测项。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968859.png)
3. 对于有风险的检测项，单击检测项名称，查看不合规的资源列表以及相关的修复指引。帮助您进行进一步的治理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968860.png)

##### 通过云安全中心检测GitHub开源代码中的AccessKey泄露

云安全中心支持实时检测GitHub平台公开源代码（多为企业员工私自上传并不小心公开）中是否含有AccessKey信息，在发现AccessKey泄露时向您发送通知，帮助您及时发现外泄的风险。该功能是云安全中心默认提供的，不需要额外付费使用。

只有AccessKey ID和AccessKey Secret（以下简称SK）同时泄露时，该访问密钥才可以被第三方利用。云安全中心在检测到阿里云账号或RAM用户的AccessKey信息泄露时，会根据SK是否有效，采用不同的方式向对应的阿里云账号发送通知，支持的通知方式如下：

- AccessKey泄露检测页面告警：只要检测到AK泄露，无论SK是否有效，都会提供告警。
- 语音通知：只有在检测到泄露的SK信息有效时，会根据您设置的接收人实时发送语音通知。
- 控制台弹框提示：在检测到泄露的SK信息有效时，您访问阿里云控制台首页或多数云产品控制台时会弹框提示。
- 根据通知设置发送告警通知：只有检测到泄露的SK信息有效时，才会根据您设置的通知方式（站内信、邮件或短信）发送通知。

强烈建议您配置好云安全中心的AccessKey泄露告警通知，避免发生AccessKey泄露时，无法及时收到告警消息。您需要从两个方面完善告警配置：

1. 通知设置：云安全中心默认开启AccessKey泄露告警通知，通知的方式包括短信、语音、邮件、站内信。您可以根据需要，在云安全中心控制台**通知设置**页面**短信/邮件/站内信**页签中，自定义**AccessKey 泄露情报**的**通知方式**。设置后，您只能通过已选中的方式收到通知。由于AccessKey泄露的安全风险高，为了能及时接收到通知，建议您选中所有通知方式。具体操作，请参见[通知设置](https://help.aliyun.com/zh/security-center/use-the-notification-feature)。
2. 联系人设置：默认情况下，仅账号联系人会收到通知，如果您有统一的安全联系人需要接收通知，您可以手动添加联系人。短信、邮件、站内信：在[基本接收管理](https://notifications.console.aliyun.com/?/subscribeMsg#/subscribeMsg)页面**安全消息 > 云盾安全信息通知**区域，修改消息接收人。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968861.png)语音：在[语音接收管理](https://notifications.console.aliyun.com/subscribeTtsMsg)页面**账号安全告警**区域，修改消息接收人。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968863.png)

如果您通过资源目录搭建了多账号架构，推荐您使用云治理中心账号工厂，批量设置和下发联系人，保证一致的配置基线，提高设置效率。详情请参见[账号工厂](https://help.aliyun.com/zh/cgc/user-guide/account-factory/)。

##### 持续检测AccessKey异常调用

除了GitHub开源代码导致的AccessKey泄露外，企业存在其他更多的泄露渠道，建议您持续关注AccessKey调用异常，及时发现潜在泄露事件的发生，以及在泄露发生时快速响应，缩小事件影响范围。您可以通过以下几种方式检测AccessKey的异常调用。

###### 通过云安全中心从攻击视角监测AccessKey异常调用

云安全中心根据多年沉淀的安全攻防经验和大模型，可以检测常见的AccessKey调用异常，例如调用AccessKey的IP地址在近期发起过攻击行为、该IP在云上批量调用多个用户的AccessKey、调用的API较为敏感且该AccessKey出现过泄露等。该功能是云安全中心默认提供的，您不需要为此额外付费使用。

1. [登录云安全中心控制台](https://yundun.console.aliyun.com/?p=sas)。在左侧导航栏，选择**风险治理 > AK泄露检测**。
2. 查看是否存在AccessKey异常调用告警。如果存在AccessKey异常调用告警，您需要查看告警详情，及时确认该AccessKey调用是否为正常行为。
3. （可选）配置安全告警通知。您可以在云安全中心控制台**系统配置>通知设置**页面，配置**安全告警**的通知方式，以便能及时收到AccessKey调用异常告警。免费版仅支持配置站内信通知方式。具体操作，请参见[通知设置](https://help.aliyun.com/zh/security-center/use-the-notification-feature)。

###### 通过操作审计配置异常告警

操作审计服务提供了内置告警，您可以在操作审计控制台进行启用，以便能在出现AccessKey异常调用时收到通知。目前，建议您使用的内置告警有：

- AK使用的异常频率告警：每15分钟检查一次，过去30分钟内，使用AccessKey异常的次数超过指定阈值后，告警触发。触发阈值可在规则参数中配置。
- Root账号AK使用检测：每15分钟检测一次，触发条件为：过去30分钟内存在Root账号AK的使用记录。Root账号不应该创建和使用AK（AccessKey）密钥，否则会触发告警。

具体操作，请参见[启用并设置事件告警](https://help.aliyun.com/zh/actiontrail/user-guide/enable-and-configure-alerts)。

###### 基于历史行为检测AccessKey异常调用

操作审计服务提供的审计事件洞察（Insights事件）功能，可以基于历史行为分析调用率异常的AccessKey，及时发现异常行为。操作审计会分析您阿里云账号中的全部写事件，其基于API的调用率并结合数学模型来分析API当前调用与历史调用行为相较是否发生显著变化，并生成Insights事件。

1. 登录[操作审计控制台](https://actiontrail.console.aliyun.com/)。
2. 在左侧导航栏，单击**审计事件洞察**。
3. 在**审计事件洞察**页面，单击**开通Insights**。
4. 开通完后，在顶部导航栏，选择您想查询事件的地域。
5. 在**审计事件洞察**页面，设置**事件类型**为AccessKey异常调用事件，然后单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968862.png)图标。
6. 单击目标Insights事件右侧操作列下的**查看事件详情**。
7. 在**Insights事件列表**区域，单击目标Insights事件记录。在**Insights事件**页签，您可以查看目标Insights事件记录的**基本信息**和**多维度聚合分析**。在**相关操作事件**页签，您可以查看目标Insights事件记录的所有相关操作事件及其详情。**Insights事件记录**页签，您可以查看目标Insights事件记录的JSON格式的事件内容。

##### 识别AccessKey泄露

当发现AccessKey异常调用后，您需要进一步确认该AccessKey的异常调用行为是否符合预期，以此判断AccessKey是否疑似泄露，是否需要采取应急处理措施。具体操作请参见上文**AccessKey操作事件审计**章节。

建议您重点关注以下的审计信息，辅助您判断AccessKey是否疑似泄露。

- 异常调用发生的时间，是否是真实业务系统的调用时间。
- 异常调用的访问IP，是否是真实业务系统的出口IP。
- 异常调用的操作，是否是真实业务系统需要的操作行为。尤其是敏感操作，比如资源的遍历、创建和删除的操作行为。

#### 云账号AccessKey泄露处理

如果云账号AccessKey发生泄露，首先您需要确认该AccessKey是否真实在使用中，这需要您的运维和业务团队共同参与。具体操作请参见上文**AccessKey操作事件审计**章节。

您可以通过调用发生时间、调用的云产品和操作行为、调用的来源IP等信息，判断AccessKey的调用行为是否是真实业务调用。比如，如果AccessKey在泄露发生后才开始出现调用行为，那么大概率该AccessKey并未在业务中真实使用，配合业务团队的进一步排查，您可以快速确定AccessKey的使用情况。

- 若确认AccessKey不在使用中，请访问[AccessKey管理页面](https://ram.console.aliyun.com/manage/ak)，直接禁用和删除AccessKey。
- 若确认AccessKey在使用中，请访问[AccessKey管理页面](https://ram.console.aliyun.com/manage/ak)，尽快轮转AccessKey。您可以先创建一个新的AccessKey，妥善保管AccessKey Secret。将原AccessKey替换为新的AccessKey，验证正常运行后，禁用和删除AccessKey。

由于云账号AccessKey具有账号的完全权限，且不能做权限控制，因此很难在泄露发生时及时进行应急处置。如果因保管和使用不当，导致云账号AccessKey被他人利用，将会对账号资源造成巨大的安全威胁。如果当前你正在使用云账号AccessKey，强烈建议您立即进行优化处理。

- 优先采用STS Token临时凭证方案进行程序访问。[了解更多](https://help.aliyun.com/zh/ram/use-cases/best-practices-for-using-access-credentials-to-access-alibaba-cloud-openapi)。
- 必须使用AccessKey的情况，建议使用RAM用户AccessKey，并进行最小化授权。 [了解更多](https://help.aliyun.com/zh/ram/user-guide/create-an-accesskey-pair-1#section-rjh-18m-7kp)。

#### RAM用户AccessKey泄露处理

当RAM用户AccessKey疑似泄露时，您可以按照下面流程进行处理。

1. 应急处理。考虑到轮转AccessKey需要一定的梳理和改造时间，建议您按照以下步骤首先降低AccessKey泄露的影响。如果您使用AccessKey调用的来源IP是固定的或者可枚举的，请尽快配置AccessKey的网络访问限制策略，阻止不可信的访问来源。尽快缩小泄露AccessKey的权限，限制高风险权限，降低业务和资费受损的风险。您需要同步的确认AccessKey的使用情况，这需要您的运维和业务团队配合，确认AccessKey是否业务真实使用。您可以通过调用发生时间、调用的云产品和操作行为、调用的来源IP等信息，辅助您确认AccessKey的使用情况。
2. 若确认AccessKey不在使用或者非真实业务使用，访问[RAM控制台](https://ram.console.aliyun.com/)，直接禁用RAM用户的AccessKey，观察对业务无影响后，删除RAM用户的AccessKey。具体操作，请参见[禁用RAM用户的AccessKey](https://help.aliyun.com/zh/ram/user-guide/disable-an-accesskey-pair-of-a-ram-user)、[删除RAM用户的AccessKey](https://help.aliyun.com/zh/ram/user-guide/delete-an-accesskey-pair-of-a-ram-user)。按照最佳实践，建议您账号下所有控制台访问用户开启多因素认证，降低子用户被盗用的风险。检查泄露的AccessKey是否有异常操作行为，以及排查是否有其他疑似泄露的身份。检查费用中心确认是否有异常的费用产生，结合上一步的异常操作行为排查，对有异常费用产生的资源实例进行处理，比如，对于AccessKey泄露导致创建了非预期的资源实例，进行删除。
3. 短期处理。若确认AccessKey在真实业务中正在使用，短期内请尽快完成AccessKey的轮转。
4. 长期方案。强烈建议您采取临时凭据的方案，使用STS Token代替AccessKey的使用。

详细的操作步骤，您可以参考下文，完成AccessKey的泄露处理。

##### 应急处理

###### 1. 配置AccessKey的网络访问策略

如果您使用AccessKey调用的来源IP是不固定的，比如，您将AccessKey放到您的移动端APP或者小程序中使用，其调用的来源IP无法固定。这种情况下，无法通过IP限制访问来源，无法通过该措施进行应急处理。

首先，您需要明确AccessKey调用的可信来源IP。比如，如果您只从您的公司内部使用AccessKey调用阿里云，那么来源IP就是您公司的公网出口IP。需要注意的是，如果您需要通过专有网络策略限制VPC内的IP地址访问，请确保您是通过VPC接入地址访问阿里云API，否则依然会通过公网访问阿里云，不受专有网络策略限制。您可以通过操作审计的AccessKey审计的功能，查看该AccessKey的所有调用来源IP，帮助您梳理并确认可信来源IP。在确认了可信来源IP后，您就可以通过AccessKey的网络访问策略来限制访问来源。

1. 使用RAM管理员登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 在左侧导航栏，选择**身份管理 > 用户**。
3. 在**用户**页面，单击目标RAM用户名称。
4. 在**认证管理**页签下的**AccessKey**区域，单击目标AccessKey操作列的**网络访问限制策略**。
5. 在**AccessKey级网络访问限制策略**对话框，设置AccessKey级公网策略和专有网络策略。公网策略：需填入公网IP地址或IP地址段，支持IPv4和IPv6格式。不创建公网策略代表所有公网IP来源均可通过。因此，若要拒绝所有公网访问，需要填入非公网地址，例如：`127.0.0.1`。专有网络策略：需填入VPC ID和VPC内的IP地址或IP地址段，支持IPv4和IPv6格式。不创建专有网络策略代表所有来自专有网络的调用均可通过。创建专有网络策略，在IP列表中填入`0.0.0.0/0`或`::/0`，表示允许该VPC内的所有IP地址的访问。

###### 2. 限制AccessKey的高危权限

您需要先明确业务场景，在不影响当前业务运行的前提下，尽快缩小疑似泄露的AccessKey权限，限制高风险权限，降低业务和资费受损的风险。在AccessKey禁用和删除之前请不要解除该策略（限制高风险权限）的授权。建议限制的高风险权限，例如：禁止该RAM用户在访问控制（RAM）中创建新的RAM用户及授权，禁止ECS、RDS、OSS、SLS资源的释放，禁止发送短信等。以下提供了一个禁用高风险权限的自定义权限策略示例，请您充分评估影响，根据业务情况设置。具体操作，请参见[创建自定义权限策略](https://help.aliyun.com/zh/ram/create-a-custom-policy)、[为RAM用户授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-the-ram-user)。

```
{
  "Version": "1",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "ram:AddUserToGroup",
        "ram:AttachPolicyToGroup",
        "ram:AttachPolicyToRole",
        "ram:AttachPolicyToUser",
        "ram:ChangePassword",
        "ram:CreateAccessKey",
        "ram:CreateLoginProfile",
        "ram:CreatePolicyVersion",
        "ram:CreateRole",
        "ram:CreateUser",
        "ram:DetachPolicyFromUser",
        "ram:PassRole",
        "ram:SetDefaultPolicyVersion",
        "ram:UpdateAccessKey",
        "ram:SetPasswordPolicy",
        "ram:UpdateRole",
        "ram:UpdateLoginProfile",
        "ram:UpdateUser"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": [
        "ecs:DeleteInstance",
        "ecs:DeleteInstances",
        "ecs:DeregisterManagedInstance",
        "ecs:ReleaseDedicatedHost"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": [
        "rds:DeleteAccount",
        "rds:DeleteDatabase",
        "rds:DeleteDBInstance",
        "rds:DestroyDBInstance"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": [
        "oss:DeleteBucket",
        "oss:DeleteObject",
        "oss:PutBucketAcl",
        "oss:PutBucketPolicy"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": [
        "log:DeleteLogStore",
        "log:DeleteProject",
        "log:PutProjectPolicy",
        "log:DeleteProjectPolicy"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": [
        "dysms:CreateProductNew",
        "dysms:CreateSmsTemplateNew",
        "dysms:AddSmsTemplate",
        "dysms:SendSms",
        "dysms:SendBatchSms"
      ],
      "Resource": "*"
    }
  ]
}
```

###### 3. 确认AccessKey使用情况，禁用未使用的AccessKey

在通过上述措施进行应急处理的同时，您可以同步确认该AccessKey是否真实在使用中，这需要您的运维和业务团队共同参与。具体操作请参见上文**AccessKey操作事件审计**章节。

您可以通过调用发生时间、调用的云产品和操作行为、调用的来源IP等信息，判断AccessKey的调用行为是否是真实业务调用。比如，如果AccessKey在泄露发生后才开始出现调用行为，那么大概率该AccessKey并未在业务中真实使用，配合业务团队的进一步排查，您可以快速确定AccessKey的使用情况。

若确认AccessKey不在使用或者非真实业务使用，您可以访问[RAM控制台](https://ram.console.aliyun.com/)，直接禁用RAM用户的AccessKey，观察对业务无影响后，删除RAM用户的AccessKey。具体操作，请参见[禁用RAM用户的AccessKey](https://help.aliyun.com/zh/ram/user-guide/disable-an-accesskey-pair-of-a-ram-user)、[删除RAM用户的AccessKey](https://help.aliyun.com/zh/ram/user-guide/delete-an-accesskey-pair-of-a-ram-user)。

无论该AccessKey是否真实业务在使用，都建议继续按照下文所述措施，进行应急处理，进一步减少泄露风险，保证云上安全。

###### 4. 开启RAM用户的MFA

按照最佳实践，建议您阿里云账号下所有用于控制台访问的RAM用户开启多因素认证（MFA）。

1. 设置主账号下的RAM用户登录控制台必须开启MFA。具体操作，请参见[管理RAM用户登录设置](https://help.aliyun.com/zh/ram/manage-console-logon-settings-for-a-ram-user-1)。
2. 为用户绑定MFA设备。具体操作，请参见[为RAM用户绑定MFA设备](https://help.aliyun.com/zh/ram/bind-an-mfa-device-to-a-ram-user-1)。

###### 5. 检查AccessKey异常操作

您需要进一步检查AccessKey是否存在异常操作行为，以及排查是否有其他疑似泄露的身份，比如：第三方使用泄露的AccessKey新建RAM用户供自己使用，以此来绕过您对AccessKey进行的限制措施。具体操作请参见上文**AccessKey操作事件审计**章节。

建议您重点关注异常的访问IP、非业务需要的资源创建或删除操作等。然后，您需要进一步排查，除了已知存在泄露风险的AccessKey之外，是否还有其他RAM用户和AccessKey存在异常操作行为。若发现存在异常行为，与相关人员确认操作是否由本人执行，若存在疑似泄露风险，建议按以下方式处理：

- RAM用户如果需要继续使用，建议您立即修改RAM用户密码并开启多因素认证（MFA）。
- RAM用户并非正常创建的，或确认为闲置用户不需要继续使用的，可进行删除。RAM用户删除后会进入回收站，观察业务是否受到影响，如有影响该RAM用户可快速恢复。
- AccessKey异常操作，参照上文（1、2、3、4）所述方法进行处理和限制。

###### 6. 检查费用异常

在[费用与成本](https://billing-cost.console.aliyun.com/)控制台，检查是否存在异常的费用产生，结合上一步的异常操作行为排查，对有异常费用产生的资源实例进行处理。比如，第三方使用泄露的AccessKey购买了ECS、ACK等多个资源，发现异常操作和异常费用后，需要及时对多余资源进行释放操作，避免异常费用的持续产生。

##### 短期处理：轮转AccessKey

完成应急处置后，对于业务还在真实使用的AccessKey，您需要尽快进行轮转替换。

1. 创建用于轮转的第二个AccessKey。具体操作，请参见[创建RAM用户的AccessKey](https://help.aliyun.com/zh/ram/user-guide/create-an-accesskey-pair)。
2. 在使用AccessKey的所有应用程序或系统中，更新正在使用的AccessKey为新创建的第二个AccessKey。您可以登录[RAM控制台](https://ram.console.aliyun.com/)，在用户详情页的用户AccessKey列表中，查看AccessKey的最后使用时间，以此初步判断第二个AccessKey是否已经被使用，原来的AccessKey是否已经不用。
3. 禁用原来的AccessKey。具体操作，请参见[禁用RAM用户的AccessKey](https://help.aliyun.com/zh/ram/user-guide/disable-an-accesskey-pair-of-a-ram-user)。
4. 验证使用AccessKey的所有应用程序或系统是否正常运行。如果运行正常，说明AccessKey更新成功，您可以放心地删除原来的AccessKey。如果运行异常，您需要暂时激活原来的AccessKey，然后重复步骤2~4的操作，直至更新成功。

1. 删除原来的AccessKey。具体操作，请参见[删除RAM用户的AccessKey](https://help.aliyun.com/zh/ram/user-guide/delete-an-accesskey-pair-of-a-ram-user)。

##### 长期方案：使用STS Token代替AccessKey的使用

通过给RAM用户或云账号的Root身份创建AccessKey供程序调用，都属于固定凭据类型。一旦创建出来，在删除之前，就是由固定的AccessKey ID和AccessKey Secret组成了该凭据。不合理地使用固定凭据会造成很多风险，比如应用研发人员将固定AccessKey明文写入了代码中，并将其上传到了GitHub等公开仓库，造成了AccessKey泄漏，最终导致业务受损。在阿里云上，建议尽可能通过角色扮演的方式获取临时凭据STS Token，代替固定AccessKey的使用。每个STS Token生成后，在超过角色最大会话时间（小时级）后，自动失效，能够极大降低凭据泄漏的可能。强烈建议您将使用STS Token作为长期方案，对已有业务系统进行改造，并作为新业务系统的研发规范，在组织层面推进STS Token的使用，以减少使用AccessKey可能带来的安全风险。详情请参见[使用临时凭据替代固定凭据](https://help.aliyun.com/zh/well-architected/sec02-bp02-prefer-temporary-credentials)。

## 故障排除

### AccessKey专有网络限制策略不生效

如果配置了AccessKey专有网络限制策略，但发现策略未生效，可能的原因是访问阿里云服务时使用了公网Endpoint。使用公网Endpoint时，程序的请求会通过公网进行访问，而不是通过专有网络VPC的IP地址，这样就无法与配置的专有网络IP白名单匹配，导致访问限制策略未能正确应用。

### AccessKey账号级网络限制策略不生效

如果配置了AccessKey账号级网络限制策略，但发现策略未生效，请检查是否配置了AccessKey级网络访问限制策略，该策略的优先级更高，若来源IP不在AccessKey级网络访问限制白名单内，则会被拦截。您可以参考下方AccessKey网络访问限制策略判断规则来进行故障排除。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5176581571/p968864.png)

### 操作审计AccessKey审计中存在调用事件查询不到

操作审计支持查询AccessKey访问过的所有阿里云服务，但AccessKey访问云服务的具体事件仅支持查询操作审计支持的云服务和事件。更多信息，请参见[操作审计支持的云服务和事件](https://help.aliyun.com/zh/actiontrail/product-overview/services-that-work-with-actiontrail)。

如果在查询过程中发现AccessKey已经访问云服务，但事件列表、IP列表和资源列表中无具体信息或最后时间无法对应，说明该云服务或事件暂未支持。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-271（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
