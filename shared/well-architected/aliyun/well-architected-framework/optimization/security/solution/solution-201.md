<!-- source: https://help.aliyun.com/zh/well-architected/solution-201 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929410 -->

# 通过配置审计和函数计算实现云主机风险巡检

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971757.png)

企业对于IT资产往往有一些合规要求，要求 ECS 主机实例的系统漏洞尽快修复从而避免收到安全攻击，或者保持一致的系统、软件配置基线，比如：主机内核参数、主机时区、软件版本等等。因此需要能够持续并且及时的发现这些安全、合规、配置等方面的主机风险。

本文档介绍了一种企业客户实现云上主机自动化风险巡检的方案，满足多账号体系下，主机风险的持续巡检和统一监控。

## 方案优势

### 巡检维度层次完善

本方案基于配置审计与函数计算产品实现云主机配置，补丁基线，主机进程/软件配置等方面的巡检，实现完整的资源巡检能力。

### 巡检平台免运维

相较于企业自建巡检平台，通过配置审计与函数计算进行资源巡检，依托于云平台自身的系统稳定性，无需客户自身运维，可以享受更高的系统稳定性。

### 巡检规则可拓展

本方案通过配置审计自定义规则的能力，支持客户自定义资源巡检规则，支持客户根据自身情况对巡检规则进行灵活拓展。

### 巡检结果可观测

基于Grafana实现多账号巡检结果统一可观测大盘，将多账号下的巡检结果集成在同一个大盘中，便于统一观察与配置告警。

## 客户场景

### 企业统一监控运维

#### 场景描述

企业内部对主机的资源配置、操作系统、系统和软件的配置等需要维护统一的安全合规基线，为确保所有主机实例都有一致的配置基线，需要能够持续的对主机资源进行风险巡检，并能够进行统一的可视化监控。

#### 适用客户

- 使用资源目录管理云上多个账号的企业客户。
- 使用多个阿里云账号的企业客户。
- 存在中心运维团队、安全团队的企业客户。
- 阿里云账号中存在多台 ECS 实例。

### 方案架构

本方案基于配置审计和函数计算，在多账号环境下，实现主机风险的巡检和监控。首先在日志账号中通过配置审计的官方规则和自定义规则对资源目录下所有成员账号进行主机风险巡检。其中自定义规则使用自定义的函数计算实现，使用函数计算调用云助手或者 OOS 补丁基线等云服务 API，对 ECS 主机内部的操作系统和软件配置等进行检测（图中1、2）。您还可以将巡检结果通过事件总线进行通知，或者投递到日志服务中进行统一查询分析（图中3）。最后，在运维账号中，消费日志服务中的巡检日志，通过 Grafana 建立统一可观测大盘（图中4），对 ECS 主机实例的资源配置、操作系统补丁、主机进程/软件配置等进行实时监控和告警。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971750.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 配置审计 | [配置审计](https://help.aliyun.com/product/127306.html)（CloudConfig）是阿里云上的配置管理和IT治理服务。将您分散在各地域的资源整合为全局资源列表，您可以便捷地搜索全局资源。同时帮助您记录云上IT资源的配置变更历史，允许您将全量资源配置和配置历史文件持续收集到指定的存储空间。同时持续自动地评估云上资源配置的合规性，实现云上IT合规治理。 | 配置审计公测期间所有阿里云有效账号均可免费使用。但具体涉及到其他服务，详情计费[参考链接](https://help.aliyun.com/zh/document_detail/133951.html) |
| 函数计算 | [函数计算（Function Compute）](https://www.alibabacloud.com/product/function-compute)函数计算是事件驱动的全托管计算服务。使用函数计算，您无需采购与管理服务器等基础设施，只需编写并上传代码。函数计算为您准备好计算资源，弹性地、可靠地运行任务，并提供日志查询、性能监控和报警等功能。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/functioncompute/fc-2-0/product-overview/billing-overview)。 |
| 日志服务 | [日志服务](https://help.aliyun.com/product/28958.html)（SLS）是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。在该方案中配置审计会把合规扫描后发现的不合规问题以日志方式推送给日志服务，在日志服务中可以进一步消费和分发这些不合规结果信息。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/sls/billing-overview)。 |
| 系统运维管理OOS | [系统管理与运维服务（CloudOps Orchestration Service, OOS）](https://help.aliyun.com/zh/oos/product-overview/introduction-to-oos)，是阿里云提供的云上自动化运维服务，能够自动化管理和执行任务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/oos/product-overview/billing-1/)。 |
| 可观测可视化 Grafana 版 | [可观测可视化 Grafana 版](https://help.aliyun.com/zh/grafana/?spm=a2c4g.11174283.0.0.4cae2effj9f5Yo)可以帮助您在高效分析与查看指标、日志和跟踪的同时，无需关注服务器配置、软件更新等繁杂工作，有效降低运维复杂性与工作量，并借助阿里云强大的云原生能力，全面提升Grafana的安全性与可用性。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/grafana/product-overview/billing-4)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 日志账号 | 聚合所有成员账号日志，统一收集，统一管理。 |
| 运维账号 | 部署运维相关工具，如统一监控平台、CMP、CMDB之类。 |
| 配置审计规则 | 规则指用于判断资源配置是否合规的规则函数。配置审计使用函数计算中的函数来承载规则代码。规则绑定资源类型后，当该资源类型中的资源发生配置变更时，自动触发规则评估，检查本次配置变更的合规性。您也可以设置规则定时触发，配置审计定时为您检查所有资源的合规性。 |
| 配置审计账号组 | 账号组是一组成员的集合。在一个资源目录中，管理账号可以选择所有或部分成员形成一个管理单元进行集中的合规管理，这个管理单元就是账号组。从资源维度上讲，账号组是多个成员中的资源汇聚而成的资源池。管理账号可以查看账号组中所有成员中的资源列表、资源详情、资源配置时间线、资源合规时间线和关联资源，还可以在账号组中新建规则与合规包。这些规则和合规包将对该账号组中所有成员下的资源生效，进行持续地合规评估。 |

## 安全性

### 配置审计服务关联角色

为了完成配置审计的功能，需要获取其他云服务的访问权限而提供的RAM角色，详情参见[配置审计服务关联角色](https://help.aliyun.com/zh/document_detail/162994.html)。

### 日志服务安全性

阿里云日志服务具有丰富的安全防护能力，支持服务器端加密、细粒度权限管控、详细服务日志等特性，同时提供日志审计功能，针对主流云产品提供多账号下实时自动化、中心化采集云产品日志并实现审计。日志服务为您提供丰富的数据洞察能力，同时满足您企业数据的安全与合规要求。

### 创建RAM用户及授权

在实际的应用场景中，阿里云账号可能需要将日志服务的运营维护工作交予其名下的RAM用户，由RAM用户对日志服务进行日常维护工作。或者阿里云账号名下的RAM用户可能有访问日志服务资源的需求。此时，阿里云账号需要对其名下的RAM用户进行授权，授予其访问或者操作日志服务的权限。出于安全性的考虑，建议您将RAM用户的权限设置为需求范围内的最小权限。关于RAM用户的详细信息，请参见[入门概述](https://help.aliyun.com/zh/ram/getting-started/)。

### 函数计算安全性

阿里云函数计算是事件驱动的全托管计算服务。通过函数计算，用户无需管理服务器等基础设施，只需编写代码并上传。函数计算会为用户准备好计算资源，以弹性、可靠的方式运行用户的代码，并提供日志查询、性能监控和报警等功能。对于数据层面，在与用户通信时，函数计算使用TLS 1.2及以上协议加密传输调用请求及回包，内部通信使用私有协议防止信息泄露及篡改。对于管控层面，您可以通过阿里云访问控制（RAM）进行权限控制等等。关于函数计算安全性的详细信息，请参见[安全合规](https://help.aliyun.com/zh/functioncompute/security-and-compliance)。

## 注意事项

### 配置审计账号组使用限制

资源目录中的管理账号或委派管理员账号可以在配置审计控制台新建账号组，在账号组中集中地管理多个成员的资源、合规包和规则。配置审计支持的账号组类型有两种：

| 名称 | 说明 |
| --- | --- |
| 全局账号组 | 全局账号组包含的成员将自动与资源目录保持一致。管理账号或委派管理员账号选中全局账号组之后，该账号组会自动感知资源目录中成员的新增，并自动同步加入到该全局账号组中，确保合规管理的账号范围始终与资源目录保持一致。 |
| 自定义账号组 | 管理账号或委派管理员账号新建自定义账号组时，主动从资源目录中选择所有或部分成员。当资源目录中新增成员时，自定义账号组并不会自动同步，需要管理账号或委派管理员账号手动将新增的成员加入到自定义账号组中。 |

需要注意的是，您只能创建唯一一个全局账号组，如果未选中全局账号组，则配置审计默认为自定义账号组，即使新建账号组时选择了资源目录中的所有成员，仍然是自定义账号组。

### 函数计算使用限制

函数计算在服务资源、函数运行资源、触发器、层、地域、镜像大小及GPU卡数等相关资源的使用上存在限制。详细信息，请参见[使用限制](https://help.aliyun.com/zh/functioncompute/limits-of-usage)。

### 云助手与本地执行命令的差异

云助手与在 ECS 实例本地执行命令，从支持功能、环境变量、命令执行结果等方面存在差异，针对不同操作系统，存在不同差异和解决方案，使用前请详细阅读并确认：

- [Linux 实例](https://help.aliyun.com/zh/ecs/user-guide/differences-between-running-commands-remotely-and-locally-on-linux-instances)
- [Windows 实例](https://help.aliyun.com/zh/ecs/user-guide/differences-between-running-commands-remotely-and-locally-on-windows-instances)

### OOS 补丁基线使用限制

OOS 补丁管理服务针对每一种操作系统都配置了预定义的默认补丁基线，您可以选择自定义的补丁基线为操作系统默认的补丁基线，从而应用自定义的补丁扫描和安装规则。使用补丁基线时有如下限制：

- 对一种操作系统，有且只能有一条默认的补丁基线。
- 补丁扫描和安装时，完全根据默认补丁基线定义的规则进行，您无法指定其他非默认的补丁基线。

## 实施步骤

### 实施准备

- 请确保已在「企业管理主账号」中开通资源目录。具体操作，请参考[开通资源目录](https://help.aliyun.com/zh/resource-management/user-guide/enable-a-resource-directory#task-hyc-zp1-dhb)。
- 请确保已在「日志账号」中开启了函数计算服务，请参考[快速创建函数](https://help.aliyun.com/zh/functioncompute/use-event-functions-to-handle-oss-file-upload-events)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 创建委派管理员

通过委派管理员账号，可以将组织管理任务与业务管理任务相分离，企业管理账号执行资源目录的组织管理任务，委派管理员账号执行配置审计的管理任务，这符合安全最佳实践的建议。接下来将资源目录的日志账号设置为配置审计服务的委派管理员账号，从而作为配置审计的管理员账号创建规则对成员账号进行风险巡检。

1. 使用管理账号登录[资源管理控制台](https://resourcemanager.console.aliyun.com/?spm=a2c4g.11186623.0.0.1272250aoGn651)。
2. 在左侧导航栏，选择**资源目录 > 可信服务**。
3. 在**可信服务**页面，单击**配置审计**服务**操作**列的**管理**。
4. 在**委派管理员账号**区域，单击**添加**。
5. 在**添加委派管理员账号**面板，选中成员(日志账号)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971759.png)
6. 单击**确定**。添加成功后，使用该委派管理员账号访问对应可信服务，既可进行资源目录组织范围内的管理操作。

#### 创建配置审计账号组

1. 登入日志账号，进入[配置审计控制台](https://config.console.aliyun.com/)，在左侧导航栏，选择**账号组**。
2. 在**账号组**页面，单击**创建账号组**。
3. 在**新建账号组**页面，先设置账号组名称和描述，再选择账号组类型。需要注意的是，您只能创建唯一一个全局账号组。如果不同部门的业务账号需要应用不同的合规规则，您可以根据资源目录资源夹或者手动选取相应的成员账号，来创建多个账号组，以此实现更加精细化的合规管理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971760.png)
4. 单击**提交**。在账号组列表中，目标账号组的状态为**创建完成**，说明新建账号组成功。您还可以查看目标账号组的名称、描述、成员数量、账号组类型和创建时间。

#### 主机资源配置巡检

您可以通过配置审计提供的合规包模版，在账号组下，快速创建针对 ECS 主机实例的合规规则，持续对 ECS 主机实例的资源配置进行合规检测，比如检测 ECS 实例是否开启了删除保护、预付费 ECS 实例是否快要到期等等。

##### 配置合规包

1. 登入日志账号，进入[配置审计控制台](https://config.console.aliyun.com/)。
2. 在左侧导航栏上方，选择需要巡检的目标账号组
3. 在左侧导航栏，选择**合规审计** > **合规包**。
4. 在**合规包**页面，选择**ECS合规管理最佳实践。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971761.png)
5. 设置合规包基本属性，选择合规包的生效范围，例如指定地域/资源组标签等。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971751.png)
6. 选择生效的审计规则。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971762.png)
7. 设置规则参数，例如到期检查/开放端口等。然后单击**确定**，完成合规包的创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971764.png)

##### 查看不合规资源

1. 登入日志账号，进入[配置审计控制台](https://config.console.aliyun.com/)。在左侧导航栏，选择**合规审计** > **合规包**。
2. 在**合规包**页面，您可以看到当前已经启用的合规包以及该合规包对应的不合规资源数等信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971765.png)
3. 单击目标合规包ID或目标合规包对应**操作**列的**详情**。
4. 在**规则检测结果**页签，您可以从规则维度查看不合规资源数。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971752.png)

#### 主机数据平面巡检

除了对 ECS 主机实例的资源配置进行合规巡检，企业对主机的数据平面往往也有一些合规要求，要求 ECS 主机实例的系统漏洞尽快修复从而避免收到安全攻击，或者保持一致的系统、软件配置基线，比如：主机内核参数、主机时区、软件版本等等。

通过函数计算和配置审计的自定义规则，您可以对 ECS 主机实例的数据平面实现持续的合规巡检，比如检测 ECS 实例的操作系统是否缺少必要的补丁、ECS 主机实例的时区是否正确等等。本方案提供两类自定义规则巡检方式：

1. 主机进程&软件配置巡检：使用[云助手](https://help.aliyun.com/zh/ecs/user-guide/overview-10)，在目标 ECS 主机实例上运行您的自定义命令脚本，对系统、软件配置，比如：主机内核参数、主机时区、软件版本等进行检测。
2. 操作系统补丁基线巡检：使用 OOS 的[补丁管理](https://help.aliyun.com/zh/oos/getting-started/patch-manager-overview)，根据补丁基线，对 ECS 主机实例的操作系统进行补丁扫描，及时发现操作系统缺失的补丁。

首先，您需要统一创建所需的角色，角色的扮演链路如下图所示。首先您需要先在日志账号创建一个受信实体为函数计算的服务角色，函数计算将通过该服务角色的身份运行您自定义的巡检逻辑。在您自定义的函数计算巡检逻辑中，需要通过角色的链式扮演方式，扮演到其他成员账号的角色上，实现跨账号的巡检操作。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971766.png)

##### 创建函数计算服务角色

首先您需要先在日志账号创建一个受信实体为函数计算的服务角色，函数计算将通过该服务角色的身份运行您自定义的巡检逻辑。

1. 登入日志账号，进入 [RAM 控制台](https://ram.console.aliyun.com/)。在左侧导航栏，选择**身份管理 > 角色**。
2. 在**角色**页面，单击**创建角色**。
3. 在**创建角色**页面，选择可信实体类型为**阿里云服务**，然后单击**下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971767.png)
4. 角色类型选择**普通服务角色**，输入角色名称，以 AliyunCustomConfigRuleRole 为例，选择授信服务为**函数计算，**点击**完成。**

接下来，您需要为该角色分配权限。

1. 登入日志账号，进入 [RAM 控制台](https://ram.console.aliyun.com/)。在左侧导航栏，选择**权限管理 > 权限策略**。
2. 在**权限策略**页面，点击**创建权限策略。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971753.png)
3. 通过**脚本编辑**模式，将配置框中的原有脚本替换为如下内容。需要注意的是，该策略内容至少需要授予 `config:PutEvaluations`和 `sts:AssumeRole`的权限。在您自定义的函数计算巡检逻辑中，需要通过角色的链式扮演方式，扮演到其他成员账号的角色上，实现跨账号的巡检操作。同时巡检结果，需要通过配置审计的接口，显式上报给配置审计。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "config:PutEvaluations",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "*"
 }
 ]
}`
4. 点击**继续编辑基本信息**，输入自定义权限策略名称。以 AliyunCustomConfigRuleRolePolicy 为例。点击**确定**完成创建。
5. 创建完成后，在角色页面，找到上述步骤创建的角色 AliyunCustomConfigRuleRole。点击**新建授权**按钮。
6. **自定义策略**选择 AliyunCustomConfigRuleRolePolicy，即您在上述步骤中创建的策略。
7. 点击**确定**完成创建。

##### 批量创建巡检角色

您可以使用 ROS 模版创建资源栈组。通过该 ROS 模版和资源栈组为资源目录下的业务账号批量创建 RAM 角色。同时对于资源栈组，可以设置自动部署功能，此时当目标资源夹中成员账号变动时，可以自动部署资源栈，方便您统一管理成员账号中的资源栈。您也可以根据需要变更自动部署设置。

###### 创建 ROS 委派管理员

接下来将资源目录的共享服务账号或运维账号设置为委派管理员账号，从而作为ROS的管理员账号为成员账号部署资源栈。

1. 登入管理账号，进入[资源管理控制台](https://resourcemanager.console.aliyun.com/?spm=a2c4g.11186623.0.0.1272250aoGn651)。
2. 在左侧导航栏，选择**资源目录 > 可信服务**。
3. 在**可信服务**页面，单击**资源编排(ROS)**服务**操作**列的**管理**。
4. 在**委派管理员账号**区域，单击**添加**。
5. 在**添加委派管理员账号**面板，选中成员(共享服务账号)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971768.png)
6. 单击**确定**。添加成功后，使用该委派管理员账号访问对应可信服务的多账号管理模块，即可进行资源目录组织范围内的管理操作。

###### 开启 ROS 可信访问

您开通了资源目录，使用资源目录的企业管理账号或委派管理员账号创建服务管理权限模式的资源栈组时，必须开启可信访问，授权服务管理权限。需要企业管理账号和委派管理员账号都开启可信访问。

1. 分别使用企业管理账号和共享服务账号（委派管理员）登录[资源编排控制台](http://ros.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源栈组**。
3. 在**资源栈组列表**页面，单击右上角的**开启可信访问**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971754.png)

###### 使用资源栈组创建巡检角色

1. 登入共享服务账号，进入[资源编排控制台](https://ros.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源栈组**。
3. 在顶部菜单栏的地域下拉列表，选择资源栈组的所在地域。
4. 在**资源栈组列表**页面，单击**创建资源栈组**。
5. 在**指定模板**选择框中，勾选**选择已有模板**。
6. **模板录入方式**选择**输入模板**，**模板内容**选择 **ROS** > **YAML**。
7. 针对操作系统补丁基线巡检和主机进程&软件配置巡检两个场景，本方案提供了如下的对应的 ROS 模版，复制相应的模版文本内容到文本框中，然后单击**下一步**。[主机进程&软件配置巡检 ROS 模版](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-compliance-audit-for-data-plane/source/ros/create-cross-account-command-inspection-role.yaml)[操作系统补丁基线巡检 ROS 模版](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-compliance-audit-for-data-plane/source/ros/create-cross-account-patch-inspection-role.yaml)
8. 输入**资源栈组名称**和**资源栈组描述**，在**配置模板参数**页面，参数可保持默认值，或根据实际情况修改，然后单击下一步。参数名称参数值示例描述角色的名称EcsCommandInspectionRole新创建的巡检角色的名称策略名EcsCommandInspectionRolePolicy新创建的巡检策略名称，该策略会授权给巡检角色角色可信的账号1002504xxxxxxx新创建的巡检角色的可信账号 ID。默认是当前账号，这里需要填写日志账号的账号 ID。可信账号下允许扮演的角色AliyunCustomConfigRuleRole可信账号下，允许扮演巡检角色的角色。这里需要填写函数计算的服务角色。
9. 在**配置资源栈组**页面，选择**服务管理权限**，然后单击**下一步**。
10. 在**设置部署选项**页面，**部署目标**选择资源目录的目标账号的资源夹，同时启用**自动部署**。
11. 根据实际情况填写**地域**、**资源组**、**标签**、**部署选项**等信息，更多信息，请参见[参数说明](https://help.aliyun.com/zh/ros/user-guide/step-3-create-a-stack-group)。然后单击**下一步**。
12. 在**检查并确认**页面，检查资源栈组信息无误后，单击**创建资源栈组**。
13. 创建完成后，在该资源栈组的详情页的**实例**Tab中，可以查看实例的状态，**最新**表示已经在业务账号下完成了角色的创建。

##### 主机进程&软件配置巡检

使用[云助手](https://help.aliyun.com/zh/ecs/user-guide/overview-10)，在目标 ECS 主机实例上运行您的自定义命令脚本，对系统、软件配置，比如：主机内核参数、主机时区、软件版本等进行检测。这里我们以巡检 ECS 主机时区为例。

###### 创建函数计算

1. 登入日志账号，进入[函数计算](https://fc.console.aliyun.com/)控制台，在左侧导航栏，选择**服务及函数**。
2. 单击**创建服务**。后续其他自定义规则都可以放到同一个服务下面，方便管理。在创建服务侧边栏中，单击**显示高级选项**按钮，**服务角色**一项，选择之前在日志账号创建的服务角色`AliyunCustomConfigRule`，**允许函数访问公网**一项选择**是**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971769.png)
3. 服务创建完成后，在**服务列表**页面，单击目标服务。在**函数管理**页面，单击**创建函数**。在**创建函数**页面，选择创建函数的方式为**使用内置运行时创建**，函数名称可以写一个规则相关的名称，这里以检查 ECS 主机时区为例，函数命名为 ecs-timezone，本方案提供的[示例代码](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-compliance-audit-for-data-plane/source/function/ecs-timezone)使用 NodeJS 编写，这里选择 NodeJS 运行环境，您可以根据需要选择不同的运行环境。上传[示例代码](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-compliance-audit-for-data-plane/source/function/ecs-timezone)，然后单击**创建**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971770.png)

###### 创建巡检规则

1. 进入配置审计控制台，在左侧导航栏上方，选择需要巡检的目标账号组。
2. 在左侧导航栏，选择**合规审计** > **规则**。在**规则**页面，单击**新建规则**。
3. 在**新建规则**页面，创建方式**选择基于函数计算自定义**，选择上一步新建的函数服务和函数实例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971755.png)
4. 单击**下一步**，在**设置基本属性**页面。先填写规则名称，再单击**添加规则入参**，配置规则参数，以上述检查 ECS 主机时区为例，该规则入参配置如下所示。最后配置规则触发机制，需要注意的是，需要将**配置变更**与**周期执行**全部勾选上。参数名称参数值示例描述configFcExecutionRoleNameEcsCommandInspectionRole必填。该参数会传入到函数计算实例当中，函数计算通过扮演该角色跨账号对其他成员账号下的资源进行巡检。这里填写上文中创建的针对主机进程&软件配置场景的巡检角色。timezoneAsia/Shanghai (CST, +0800)必填。该参数会传入到函数计算实例当中，用于校验是否为对应的时区。tagScopes[{"TagKey":"InspectionType","TagValue":"TimeZone"}]非必填。基于标签对巡检资源进行过滤，请填写有效的 JSON 字符串，命中了数组中任意一对标签键值对的资源既为有效资源，会对该资源进行巡检，否则会忽略。如果改参数未配置，则对所有资源进行巡检。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971771.png)
5. 单击**下一步**，在**设置生效范围**页面，**资源类型**选择 **ECS 实例**。
6. 单击**下一步**。在**设置修正**页面，单击**提交**。完成规则创建。
7. 等待规则扫描资源（也可以在规则详情页面单击**重新审计**触发一次扫描），即可看到不合规资源。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971756.png)

##### 操作系统补丁基线巡检

使用 OOS 的[补丁管理](https://help.aliyun.com/zh/oos/getting-started/patch-manager-overview)，根据补丁基线，对 ECS 主机实例的操作系统进行补丁扫描，及时发现操作系统缺失的补丁。该巡检规则的操作步骤，除了函数计算代码和巡检规则入参外，其他部分和上文**主机进程&软件配置巡检**基本一致。

###### 创建函数计算

1. 登入日志账号，进入[函数计算](https://fc.console.aliyun.com/)控制台，在左侧导航栏，选择**服务及函数**。
2. 单击**创建服务**。如果您已经创建了对应服务，那么可以忽略这一步。后续其他自定义规则都可以放到同一个服务下面，方便管理。在创建服务侧边栏中，单击**显示高级选项**按钮，**服务角色**一项，选择之前在日志账号创建的服务角色`AliyunCustomConfigRule`，**允许函数访问公网**一项选择**是**。
3. 服务创建完成后，在**服务列表**页面，单击目标服务。在**函数管理**页面，单击**创建函数**。在**创建函数**页面，选择创建函数的方式为**使用内置运行时创建**，函数名称可以写一个规则相关的名称，本方案提供的[示例代码](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-compliance-audit-for-data-plane/source/function/ecs-patch-baseline)使用 NodeJS 编写，这里选择 NodeJS 运行环境，您可以根据需要选择不同的运行环境。
4. 上传[示例代码](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-compliance-audit-for-data-plane/source/function/ecs-patch-baseline)，然后单击**高级配置**。配置执行超时时间，由于补丁基线的扫描耗时较久，建议您配置较大的执行超时时间，比如 3600 秒。

###### 创建巡检规则

1. 进入配置审计控制台，在左侧导航栏上方，选择需要巡检的目标账号组。
2. 在左侧导航栏，选择**合规审计** > **规则**。在**规则**页面，单击**新建规则**。
3. 在**新建规则**页面，创建方式**选择基于函数计算自定义**，选择上一步新建的函数服务和函数实例
4. 单击**下一步**，在**设置基本属性**页面。先填写规则名称，再单击**添加规则入参**，配置规则参数，该规则入参配置如下所示。最后配置规则触发机制，需要注意的是，需要将**配置变更**与**周期执行**全部勾选上。参数名称参数值示例描述configFcExecutionRoleNameEcsPatchBaselineInspectionRole必填。该参数会传入到函数计算实例当中，函数计算通过扮演该角色跨账号对其他成员账号下的资源进行巡检。这里填写上文中创建的针对操作系统补丁基线场景的巡检角色。tagScopes[{"TagKey":"InspectionType","TagValue":"PatchBaseline"}]非必填。基于标签对巡检资源进行过滤，请填写有效的 JSON 字符串，命中了数组中任意一对标签键值对的资源既为有效资源，会对该资源进行巡检，否则会忽略。如果改参数未配置，则对所有资源进行巡检。
5. 单击**下一步**，在**设置生效范围**页面，**资源类型**选择 **ECS 实例**。
6. 单击**下一步**。在**设置修正**页面，单击**提交**。完成规则创建。
7. 等待规则扫描资源（也可以在规则详情页面单击**重新审计**触发一次扫描），即可看到不合规资源。
8. 在规则详情页，**检测结果**下的资源列表中，单击相应的资源ID，进入**资源详情**页面，在**最新审计结果**列表中，选择该规则，鼠标移动到**合规结果**列的**更多**上，会展示出该 ECS 实例缺少的补丁数量。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971772.png)

#### 配置审计日志投递

##### 配置日志投递

1. 登录日志账号，进入[配置审计控制台](https://config.console.aliyun.com/)。
2. 切换到对应的账号组中。
3. 在左侧导航栏，单击**投递**。
4. 在**投递**页面，单击左上角的**新建投递**。
5. 在**新建投递**页面，先输入**投递名称**，再选择**投递渠道**为**日志服务SLS**，然后设置日志服务SLS的相关参数。您可以在当前企业管理账号中新建日志项目，也可以选择当前企业管理账号或其他成员账号中已有日志项目。该日志项目用于接收企业管理账号和所有成员账号的资源投递数据。详细的操作步骤见[产品链接](https://help.aliyun.com/zh/document_detail/179275.html)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971773.png)
6. 为投递目标logstore开启SLS日志索引，这里为了后续方便配置可观测大盘，将巡检相关的全部字段都开启了统计。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971758.png)

#### 配置Grafana可观测大盘（可选）

##### 创建RAM用户

1. 登录日志账号，进入 [RAM 控制台](https://ram.console.aliyun.com/)，在**权限策略**页面，新建一个权限策略。名称以`GrafanaEcsTimeZoneLogStoreAccess`为例。权限策略包含了读取SLS指定LogStore的权限。内容如下：`{
 "Version": "1",
 "Statement": [
 {
 "Action": [
 "log:ListProject"
 ],
 "Resource": "acs:log:*:*:project/*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "log:List*"
 ],
 "Resource": "acs:log:*:*:project/<指定的Project名称>/logstore/*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "log:Get*",
 "log:List*"
 ],
 "Resource": [
 "acs:log:*:*:project/<指定的Project名称>/logstore/<指定的Logstore名称>"
 ],
 "Effect": "Allow"
 }
 ]
}`
2. 在 RAM 控制台新建RAM用户，用于Grafana读取SLS日志。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971775.png)
3. 记录下所创建的RAM用户的AK,SK。
4. 创建完成后，将权限策略`GrafanaEcsTimeZoneLogStoreAccess`绑定到RAM用户。

##### 添加数据源

添加日志服务SLS数据源，将之前所创建的用于访问配置审计投递日志的日志账号AK，SK配置进去，具体参见[官方文档](https://help.aliyun.com/zh/grafana/user-guide/add-and-use-a-log-service-data-source?spm=a2c4g.11186623.0.0.4b7f2d43H7EorP)。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971774.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6576581571/p971763.png)

## 故障排除

### 为什么无法使用 ROS 服务管理权限模式？

- 如果使用资源目录成员账号执行ROS的业务管理任务，您需要将资源目录的成员账号设置为委派管理员账号，从而作为 ROS 的管理员账号为成员账号部署资源栈。关于 ROS 委派管理员，请参见[设置委派管理员账号](https://help.aliyun.com/zh/ros/user-guide/step-1-create-a-delegated-administrator-account)。
- 当您开通了资源目录，使用资源目录的企业管理账号或委派管理员账号创建服务管理权限模式的资源栈组时，必须开启可信访问，授权服务管理权限。关于可信访问，请参见[开启可信访问](https://help.aliyun.com/zh/ros/user-guide/step-2-enable-trusted-access)。

### 为什么配置审计自定义规则没有把资源信息推送到函数计算中

在创建配置审计自定义规则时，规则触发机制，必须选择上**配置变更**的触发方式，此时，该配置审计规则，触发函数计算时，就会推送相应的资源信息，否则在触发函数计算时，只会以账号维度进行一次无资源的推送。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-201（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
