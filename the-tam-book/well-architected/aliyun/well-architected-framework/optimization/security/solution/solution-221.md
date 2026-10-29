<!-- source: https://help.aliyun.com/zh/well-architected/solution-221 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929197 -->

# 通过OOS实现主机系统与软件配置自动化运维

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6276581571/p969545.png)

企业对于IT资产往往有一些合规要求，要求 ECS 主机实例保持一致的系统、软件配置基线，比如：主机内核参数、主机时区、软件版本等等。

本文档介绍了一种企业客户实现云上主机系统与软件配置的自动化运维的方案，满足多账号体系下，主机系统与软件配置集中扫描、监控和修复的运维需求。

## 方案优势

### 系统与软件配置集中运维

OOS 自动化流程定义在共享服务账号或者运维账号中，通过该自动化流程，自动、批量的给所有账号中指定的 ECS 实例运行自定义命令，修改系统与软件的配置，实现主机配置的自动化、中心化运维。同时接入人工审批和通知的流程，进一步保证运维流程的安全合规。

### 提升业务安全合规

基于配置审计，持续审计和保证主机系统、软件配置的合规情况，及时发现并处置不符合企业配置基线的 ECS 实例，确保所有业务的 ECS 实例符合企业整体配置基线的要求，避免业务主机实例未及时更新配置，造成安全合规风险。

## 客户场景

### 企业内部统一运维

#### 场景描述

企业内部需要维护统一的主机系统和软件的配置基线，确保所有主机实例都有一致的配置基线，并能够统一的监控、修复主机配置。

#### 适用客户

- 使用资源目录管理云上多个账号的企业客户。
- 使用多个阿里云账号的企业客户。
- 存在中心运维团队、安全团队的企业客户。
- 阿里云账号中存在多台 ECS 实例。

## 方案架构

本方案基于多账号体系实现主机系统与软件配置的自动化运维。运维工作再共享服务账号或者运维账号中运行。通过配置审计，您可以持续审计业务账号中所有主机实例的配置合规情况（图中1），您还可以将审计结果通过事件总线进行通知或者通过日志服务集成到监控系统中。当需要对主机配置进行修复时，您可以触发系统运维管理服务的自动化任务来进行（图中4），执行过程中，还可以接入人工审批（图中2）和通知（图中3）的流程，进一步保证运维流程的安全合规。最后，通过下发标签策略（图中5），确保业务账号下的 ECS 主机实例都绑定了配置运维所需的标签。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6276581571/p969584.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 配置审计 | 配置审计是一项面向资源的审计服务。在面对大量资源时，配置审计可以帮助您实现持续的基础设施的合规监管。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/document_detail/133951.html)。 |
| 访问控制RAM | [访问控制RAM（Resource Access Management）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务 | 免费。 |
| 系统运维管理OOS | [系统管理与运维服务（CloudOps Orchestration Service, OOS）](https://help.aliyun.com/zh/oos/product-overview/introduction-to-oos)，是阿里云提供的云上自动化运维服务，能够自动化管理和执行任务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/oos/product-overview/billing-1/)。 |
| 阿里云资源编排服务ROS | [资源编排服务ROS（Resource Orchestration Service）](https://help.aliyun.com/zh/ros/)可以帮助您简化云计算资源的管理。遵循ROS定义的模板规范，您可以定义所需云计算资源的集合及资源间的依赖关系。ROS可以自动完成所有资源的创建和配置，实现自动化部署和运维。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/ros/product-overview/billing-overview)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |
| ROS 模板 | 模板是一个JSON、YAML或Terraform格式的文本文件，使用UTF-8编码。您可以使用指定扩展名（如.json、.yaml、.template、.txt或.tf）保存这些文件。模板用于创建资源栈，是描述基础设施和架构的蓝图。模板编辑者在模板中定义阿里云资源和配置细节，并说明资源间的依赖关系。 |
| 资源栈 | 资源栈是针对ROS资源的管理单元。您可通过创建、更新和删除资源栈来创建、更新和删除一组资源。 |
| 资源栈组 | 资源栈组是针对ROS资源栈的管理单元。通过资源栈组，可使用一个ROS模板在多个阿里云账号中跨地域创建资源栈。每个资源栈中包含的所有资源由资源栈组的ROS模板定义。 |
| OOS 模板 | 一个YAML或JSON格式的文件，包括一个或多个任务。 |

## 安全性

### 资源编排安全性

资源编排已与操作审计服务集成，您可以在操作审计中查询用户操作资源编排产生的管控事件。操作审计支持将管控事件投递到日志服务SLS的LogStore或对象存储OSS的存储空间中，满足实时审计、问题回溯分析等需求。

同时，资源编排服务支持对ROS模板进行资源创建前的合规性检测。关于支持合规预检的云服务，请参见[托管规则列表](https://help.aliyun.com/zh/document_detail/127404.html)。

## 注意事项

### 云助手与本地执行命令的差异

云助手与在 ECS 实例本地执行命令，从支持功能、环境变量、命令执行结果等方面存在差异，针对不同操作系统，存在不同差异和解决方案，使用前请详细阅读并确认：

- [Linux 实例](https://help.aliyun.com/zh/ecs/user-guide/differences-between-running-commands-remotely-and-locally-on-linux-instances)
- [Windows 实例](https://help.aliyun.com/zh/ecs/user-guide/differences-between-running-commands-remotely-and-locally-on-windows-instances)

## 自动化模板

### 模板介绍

本方案提供了基于 Terraform 和资源编排（ROS） 的自动化模板，模板代码结构如下所示。

```
├── step1-preparation						       // 在共享服务账号中创建所需角色和权限，并委派 ROS 管理员给共享服务账号。
└── step2-create-cross-account-role    // 使用 ROS 模版在共享服务账号中创建资源编排（ROS）的资源栈组，跨账号给所有需要统一运维的业务账号创建所需角色。
└── step3-automation-deployment	       // 在共享服务账号中创建 OOS 自定义任务模版。
```

### 模板地址

模板地址详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-ecs-system-configuration-maintenance)。

## 实施步骤

### 实施准备

- 请确保您已经开通资源目录。具体操作，请参考[开通资源目录](https://help.aliyun.com/zh/resource-management/user-guide/enable-a-resource-directory#task-hyc-zp1-dhb)。
- 请确保已在「企业管理主账号」中开启了管控策略功能，请参考资源目录[开启管控策略功能](https://help.aliyun.com/zh/resource-management/user-guide/enable-the-control-policy-feature)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 前置准备

##### 创建委派管理员

通过委派管理员账号，可以将组织管理任务与业务管理任务相分离，企业管理账号执行资源目录的组织管理任务，委派管理员账号执行ROS的业务管理任务，这符合安全最佳实践的建议。接下来将资源目录的共享服务账号或运维账号设置为委派管理员账号，从而作为ROS的管理员账号为成员账号部署资源栈。

1. 使用管理账号登录[资源管理控制台](https://resourcemanager.console.aliyun.com/?spm=a2c4g.11186623.0.0.1272250aoGn651)。
2. 在左侧导航栏，选择**资源目录 > 可信服务**。
3. 在**可信服务**页面，单击**资源编排(ROS)**服务**操作**列的**管理**。
4. 在**委派管理员账号**区域，单击**添加**。
5. 在**添加委派管理员账号**面板，选中成员(共享服务账号)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6276581571/p969550.png)
6. 单击**确定**。添加成功后，使用该委派管理员账号访问对应可信服务的多账号管理模块，即可进行资源目录组织范围内的管理操作。

##### 开启可信访问

当您开通了资源目录，使用资源目录的企业管理账号或委派管理员账号创建服务管理权限模式的资源栈组时，必须开启可信访问，授权服务管理权限。需要企业管理账号和委派管理员账号都开启可信访问。

1. 分别使用企业管理账号和共享服务账号（委派管理员）登录[资源编排控制台](http://ros.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源栈组**。
3. 在**资源栈组列表**页面，单击右上角的**开启可信访问**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6276581571/p969551.png)

#### 资源与运维规划（可选）

整个主机配置运维的过程，需要业务团队和运维团队共同参与。每个业务应用通常部署在多个环境中，比如开发、测试（预发验收等）和生产环境。业务团队和运维团队需要为每个环境规划主机配置运维的时间窗口，因此当命令执行到生产环境时，它应该已经经过开发、测试环境的测试，并确定不会对生产环境的业务应用造成不利影响。由此可见，进行合理的资源规划，对业务应用的环境进行严格划分，是整个主机配置运维的基础。本方案采用标签的方式来对资源进行环境划分，以下流程提供了一个示例，说明如何为部署在多个环境中的业务应用规划运维窗口，以及如何配置标签。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6276581571/p969552.png)

1. 运维团队需要和业务团队共同为不同环境中的资源（ECS 主机实例）规划运维时间窗口，并且为这些 ECS 实例配置用于资源分组的标签。同时需要保证相同标签分组中的资源，允许相同的运维窗口时间段。如果您有多种操作系统的 ECS 实例，建议您根据操作系统继续配置相应的标签，有助于确保正确的脚本命令部署到正确的 ECS 实例中。
2. 通过主机配置巡检（请参考[持续合规审计](#bqh3L)章节），发现不合规的主机配置后，您可以根据 ECS 主机的操作系统，自定义配置修复的脚本命令，该脚本命令会通过云助手在 ECS 主机实例上运行。
3. 当需要运行自定义脚本命令时，您应该首先将脚本命令运行到开发环境，执行完成后，业务团队需要测试应用程序并验证其是否正常工作。如果应用程序在命令执行过程中遇到任何问题，业务团队需要要求运维团队暂停当前的配置修复工作。
4. 开发环境命令应用成功后，将脚本命令执行到其他非生产环境。与开发环境一样，其中的应用程序需要经过测试和验证。
5. 当所有非生产环境命令执行成功后，就可以将脚本命令应用到生产环境。

更多资源规划的内容，请参见[基于资源组和标签管理单账号云资源](https://help.aliyun.com/zh/well-architected/solution-13)。

#### 持续合规审计（可选）

##### 资源规划审计

在云上IT管理中，要求云上的IT资源必须具备某个或某些标签，在后续的权限隔离、账单划分和自动化运维等场景中需基于这些标签来管理资源。可以通过配置审计服务来持续审计资源合规情况：

1. 使用管理账号登录[配置审计控制台](https://config.console.aliyun.com/)。
2. 在左侧导航栏，单击**合规审计**>**规则**>**新建规则**。
3. 选择**基于模板创建**，搜索「标签」，可以通过创建「至少存在一个指定标签」、「存在所有指定标签」、「匹配指定标签」等规则来对资源的打标情况进行合规审计。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6276581571/p969553.png)

##### 主机软件配置巡检

企业内部对主机的资源配置、操作系统、系统和软件的配置等需要维护统一的安全合规基线，为确保所有主机实例都有一致的配置基线，需要能够持续的对主机资源进行风险巡检，并能够进行统一的可视化监控。详情参考[通过配置审计和函数计算实现云主机风险巡检](https://help.aliyun.com/zh/well-architected/solution-201)。

#### 配置标签策略（可选）

标签策略是用来帮助企业实施标签规范化的一种策略。通过标签策略，企业可以限定资源上必须绑定的合规标签。合规标签可以提升企业在标签分账、标签分权、自动化运维等场景的管理效率。标签策略支持当前账号标签策略和资源目录标签策略两种，可以满足企业在不同阶段对标签规范化管控的需求。

创建资源后，忘了绑定标签；只绑定了部分标签；绑定的标签拼写错误等。这些问题会导致企业在自动化运维时，出现不能自动化执行的资源。标签策略将在以下场景提供解决方案：

- **标签自动检测**资源创建后，您可以通过标签策略监听资源变更情况，及时发现绑定了不合规标签的资源。
- **标签自动修复**基于标签自动检测的结果，如果您的规则符合自动修复的条件，并开启了自动修复，则无需人工操作，标签策略会对不合规资源的标签进行自动修复。
- **不合规标签事前拦截**通过标签策略，实现资源创建时就强制绑定合规标签，拦截不合规标签。
- **资源组标签自动继承到组内资源**为资源组绑定标签后，当在资源组中创建资源或者将资源加入到资源组时，该资源会自动继承资源组的标签。

关于如何启用和创建标签策略，请参考[标签策略快速入门](https://help.aliyun.com/zh/resource-management/user-guide/getting-started)。

#### 统一创建所需角色

##### 创建自动化运维角色

您需要创建 RAM 角色，OOS 自动化任务会使用该角色身份来运行自动化运维任务。

1. 使用共享服务账号登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 在左侧导航栏，选择**身份管理 > 角色**。
3. 在**角色**页面，单击**创建角色**。
4. 在**创建角色**页面，选择可信实体类型为**阿里云服务**，然后单击**下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6276581571/p969557.png)
5. 角色类型选择**普通服务角色**，输入角色名称，例如EcsCommandRunningAutomationTriggerRole，选择授信服务为**系统运维管理，**点击**完成。**

接下来，您需要为该角色分配权限，系统运维管理服务（OOS） 会扮演该角色来触发自动化运维模板执行。

1. 使用共享服务账号登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 选择权限策略菜单，点击**创建权限策略。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6276581571/p969558.png)
3. 通过**脚本编辑**模式，将配置框中的原有脚本替换为如下内容。注意请根据实际情况替换内容中的`${oos_cross_account_assume_role}`，例如EcsCommandRunningAutomationRole。该策略允许上述步骤创建的自动化运维角色（EcsCommandRunningAutomationTriggerRole）跨账号扮演到此处配置的脚本命令执行角色（在[批量创建脚本命令执行角色](#pTG8y)章节完成创建），来执行运维脚本命令。`{
 "Version": "1",
 "Statement": [
 {
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "acs:ram:*:*:role/${oos_cross_account_assume_role}",
 "Effect": "Allow"
 }
 ]
 }`
4. 点击**继续编辑基本信息**，输入自定义权限策略名称。例如EcsCommandRunningAutomationTriggerRolePolicy。点击**确定**完成创建。
5. 创建完成后，在角色页面，找到上述步骤创建的角色，点击**新建授权**按钮。
6. **授权范围**选择**整个云账号**。权限在当前阿里云账号内生效。**授权主体**选择。**EcsCommandRunningAutomationTriggerRole**，即您在上述步骤中创建的角色。**自定义策略**选择**EcsCommandRunningAutomationTriggerRolePolicy**，即您在上述步骤中创建的策略。
7. 点击**确定**完成创建。

##### 批量创建脚本命令执行角色

您需要使用 ROS 模板创建资源栈组。通过该 ROS 模板和资源栈组为资源目录下的需要统一运维的业务账号批量创建所需 RAM 角色。OOS 会扮演该角色跨账号执行脚本命令，完成配置运维。

1. 使用共享服务账号登录[资源编排控制台](https://ros.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源栈组**。
3. 在顶部菜单栏的地域下拉列表，选择资源栈组的所在地域。
4. 在**资源栈组列表**页面，单击**创建资源栈组**。
5. 在**指定模板**选择框中，勾选**选择已有模板**。
6. **模板录入方式**选择**输入模板**，**模板内容**选择 **ROS** > **YAML**。
7. 复制[该ROS模板](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-ecs-system-configuration-maintenance/step2-create-cross-account-role/stack-group-template.yaml)的文本内容到文本框中，然后单击**下一步**。
8. 输入**资源栈组名称**和**资源栈组描述**，在**配置模板参数**页面，参数可保持默认值，或根据实际情况修改，然后单击下一步。
9. 在**配置资源栈组**页面，选择**服务管理权限**，然后单击**下一步**。
10. 在**设置部署选项**页面，**部署目标**选择资源目录的目标账号的资源夹，同时启用**自动部署**。
11. 根据实际情况填写**地域**、**资源组**、**标签**、**部署选项**等信息，更多信息，请参见[参数说明](https://help.aliyun.com/zh/ros/user-guide/step-3-create-a-stack-group)。然后单击**下一步**。
12. 在**检查并确认**页面，检查资源栈组信息无误后，单击**创建资源栈组**。
13. 创建完成后，在该资源栈组的详情页的**实例**Tab中，可以查看实例的状态，**最新**表示已经在业务账号下完成了角色的创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6276581571/p969561.png)

#### 统一自动化运维

##### 部署自动化运维模板

该步骤通过 Terraform 代码完成自动化部署，进入到[源代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-ecs-system-configuration-maintenance/step3-automation-deployment)，获取该目录下（step3-automation-deployment）的源代码，您可以新建 tfvars.json 文件并配置参数，并通过`terraform apply -var-file=tfvars.json`命令进行部署。

1. 请确保您的运行时环境能够运行 Terraform
2. 请使用共享服务账号的身份运行

有关参数配置说明如下：

| 参数名称 | 参数值示例 | 描述 |
| --- | --- | --- |
| region | cn-shanghai | 自动化运维模板部署地域 |
| oss_assume_role | EcsCommandRunningAutomationTriggerRole | step1 中创建的共享服务账号中的角色。OOS 会扮演该角色来触发自动化运维模板 |
| oos_cross_account_assume_role | EcsCommandRunningAutomationRole | step2 中在需要统一运维的其他业务账号中创建的角色。OOS 会扮演该角色跨账号执行脚本命令，完成配置运维 |
| approverRamUserName | approver | 允许审批运维流程的 RAM 用户。您也可以直接授予其 AliyunOOSFullAccess 权限。该 RAM 用户可以批准/拒绝运维流程。您可以在触发运维流程时修改该参数。 |
| approverWebHookUrl | 有效的 WebHook 链接 | 在需要人工审批时，会通过该 WebHook 发送消息通知。您可以在触发运维流程时修改该参数。 |
| commandRunningWebHookUrl | 有效的 WebHook 链接 | 在运维流程运行时，会通过该 WebHook 发送消息通知，您可以使用该 WebHook 给业务团队发送通知。 |

另外，也可以选择使用资源编排服务（ROS）进行部署：

1. 使用共享服务账号登录[资源编排控制台](https://ros.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源栈**。
3. 在顶部菜单栏的地域下拉列表，选择资源栈的所在地域。
4. 在**资源栈列表**页面，单击**创建资源栈**，选择**使用Terraform**。
5. 在**指定模板**选择框中，选择**选择已有模板**。
6. **模板录入方式**选择**输入模板**，**模板内容**选择**Terraform**。
7. 复制[Terraform文件](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-ecs-patching/step4-automation-deployment/main.tf)的文本内容到文本框中。
8. 在目录栏，单击 +，单击创建文件，填入文件名称`variable.tf`，复制[Terraform文件](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-ecs-patching/step4-automation-deployment/variables.tf)的文本内容到文本框中，单击下一步。
9. 输入**资源栈名称**，在配置模板参数区块，请根据实际情况完成所需参数的填写。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6276581571/p969564.png)
10. 单击**创建**。资源栈创建成功后，**状态**列显示**创建成功**。

##### 执行自动化运维流程

1. 使用共享服务账号登录[系统运维管理控制台](https://oos.console.aliyun.com/)。
2. 在左侧导航栏，单击**自定义任务模板**。
3. 在顶部菜单栏的地域下拉列表，选择模板的所在地域，可以看到在[部署自动化运维模板](#HCMB1)步骤中创建的任务模板，单击**创建执行**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6276581571/p969566.png)
4. 在**基本信息**页面，执行模式选择**失败暂停**模式，单击**下一步**。
5. 根据提示信息，设置必填参数，单击**下一步**。
6. 检查信息无误后，单击**创建**，完成主机系统与软件配置自动化运维任务的创建。后续会依次进行：人工审批、发送自动化运维通知、执行自动化运维脚本命令。

以下是整个自动化流程的架构图。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6276581571/p969590.png)

您可以通过多种方式触发脚本命令的执行流程，您可以手动触发、定时触发或者在您的 CI-CD 中通过 API 触发。该自动化流程的工作原理如下。

1. 触发执行脚本命令任务时，审批信息通过 WebHook 进行消息通知（图中1）。审批人接到通知后，可以批准/拒绝执行命令的流程。
2. 批准后，会将命令执行的消息通过 WebHook 通知给对应的业务团队（图中2）。业务团队需要及时测试应用程序并验证其是否正常工作。如果应用程序在命令执行过程中遇到任何问题，业务团队需要要求运维团队暂停当前的执行工作。
3. 通过扮演业务账号中的 RAM 角色，跨账号执行云助手命令。云助手会分批在指定的 ECS 实例运行自定义命令（图中3）。分批执行时，建议运维团队选择每批暂定的并发控制模式，方便业务团队及时对应用程序进行测试和验证。

## 故障排除

### 为什么无法开通资源目录？

可能有如下两个原因：

- 当前账号没有进行企业实名认证。关于企业实名认证，请参见[企业实名认证](https://help.aliyun.com/zh/account/verify-your-identity-enterprise-account/)。
- 当前账号已经在资源目录内，无法重复开通。

### 为什么无法使用 ROS 服务管理权限模式？

- 如果使用资源目录成员账号执行ROS的业务管理任务，您需要将资源目录的成员账号设置为委派管理员账号，从而作为 ROS 的管理员账号为成员账号部署资源栈。关于 ROS 委派管理员，请参见[设置委派管理员账号](https://help.aliyun.com/zh/ros/user-guide/step-1-create-a-delegated-administrator-account)。
- 当您开通了资源目录，使用资源目录的企业管理账号或委派管理员账号创建服务管理权限模式的资源栈组时，必须开启可信访问，授权服务管理权限。关于可信访问，请参见[开启可信访问](https://help.aliyun.com/zh/ros/user-guide/step-2-enable-trusted-access)。

### 为什么执行 OOS 运维任务失败？

使用 OOS 的常见问题，请参见 [OOS 服务支持](https://help.aliyun.com/zh/oos/support/faq)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-221（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
