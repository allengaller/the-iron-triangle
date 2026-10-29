<!-- source: https://help.aliyun.com/zh/well-architected/solution-251 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929049 -->

# 通过角色扮演实现跨账号临时凭证的获取和使用

本文介绍了一种跨账号扮演角色获取和使用临时凭证（STS Token）的方案。避免直接把AccessKey固化在程序中，引发泄露风险。

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7076581571/p968997.png)

凭证管理是云上最容易出现风险的环节之一，管理不善将导致凭证泄漏，进而导致数据泄漏、资产损失等严重安全事故。当部署在阿里云上的应用需要访问其他账号的云资源时，传统的方式是将其他账号RAM用户的AccessKey固化在程序中，容易造成AccessKey的泄露，同时维护困难。通过角色链式扮演的方式，使应用基于STS临时凭证访问其他账号的云资源，保证全链路无需透露长期AccessKey，既可减少密钥泄露的风险，也可借助访问控制RAM精细化控制资源访问权限，避免权限过度分配。本方案主要介绍如何跨账号通过角色扮演的方式获取并使用临时访问凭证。

## 方案优势

该方案能够显著提升云上应用程序的安全性、灵活性和便捷性，同时降低维护成本和操作复杂性。

### 提升安全性

通过角色链式扮演的方式，使用临时凭证STS Token跨账号访问云资源，避免了将访问密钥AccessKey硬编码在代码中，从而消除AccessKey泄露的风险。临时凭证（STS Token）的使用有效解决了永久凭证（AK/SK）可能带来的安全风险问题。

### 增强灵活性

部署在阿里云上的应用程序可以通过阿里云官方SDK，获取临时凭证STS Token。这种方式无需预先配置固定的访问凭证，可以根据需要动态获取和使用临时凭证。权限的调整仅需通过修改RAM角色的授权策略来实现，快捷地维护应用程序拥有的访问权限。

### 降低维护成本

使用临时凭证STS Token，无需频繁更新代码中的访问密钥，减少了维护成本和操作复杂性。本方案提供了代码示例，客户能够快速完成应用改造，减少开发和部署的复杂度。

## 客户场景

### 企业跨账号统一运维

#### 场景描述

企业存在中心化的运维系统，需要跨账号访问企业的所有云账号，进行统一的运维管理操作。

#### 适用客户

- 使用多个阿里云账号的企业客户。
- 存在中心化的运维系统，需要跨账号进行自动化运维操作。
- 出于安全考虑，不希望使用长期固定AccessKey，以避免AccessKey泄露，带来安全风险。

## 方案架构

本方案通过角色扮演的方式，使应用基于STS临时凭证访问其他账号的云资源，保证全链路无需透露长期AccessKey。首先，如果您的应用程序部署在阿里云上，强烈建议您的应用程序本身是无AK的。如下图所示，以部署在运维账号下的ECS实例中的应用程序为例。运维管理员在ECS实例上绑定实例RAM角色，部署在该ECS上的应用程序可以通过阿里云官方SDK，获得代表实例角色的临时凭证STS Token（图中1、2、3），以保证应用程序无需透露长期固定AccessKey。然后运维管理员，批量在所需的业务账号中创建业务RAM角色，并授信给ECS实例角色（图中4），允许实例角色通过AssumeRole接口跨账号扮演业务角色，获取业务角色的STS临时凭证（图中5）。应用程序拿到其他账号下业务角色STS临时凭证后，使用临时凭证直接调用API访问其他账号的资源（图中6）。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7076581571/p968999.png)

本方案中为保证全链路无需透出长期固定AccessKey，应用程序通过角色链式扮演的方式，获取其他业务账号的RAM角色的STS临时凭证，通过STS临时凭证跨账号访问其他账号的云资源。其中，实例RAM角色至少需要具有`sts:AssumeRole`的权限，其他账号中的业务RAM角色的权限既应用程序跨账号操作时所需的具体权限，

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 访问控制RAM | [访问控制RAM（Resource Access Management）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |
| 阿里云资源编排服务ROS | [资源编排服务ROS（Resource Orchestration Service）](https://help.aliyun.com/zh/ros/)可以帮助您简化云计算资源的管理。自动完成所有资源的创建和配置，实现自动化部署和运维。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/ros/product-overview/billing-overview)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 运维账号 | 企业运维服务会部署在这个账号内。推荐这个账号的费用由统一的某个团队来承担，比如运维团队。 |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |
| ROS 模板 | 模板是一个JSON、YAML或Terraform格式的文本文件，使用UTF-8编码。您可以使用指定扩展名（如.json、.yaml、.template、.txt或.tf）保存这些文件。模板用于创建资源栈，是描述基础设施和架构的蓝图。模板编辑者在模板中定义阿里云资源和配置细节，并说明资源间的依赖关系。 |
| 资源栈 | 资源栈是针对ROS资源的管理单元。您可通过创建、更新和删除资源栈来创建、更新和删除一组资源。 |
| 资源栈组 | 资源栈组是针对ROS资源栈的管理单元。通过资源栈组，可使用一个ROS模板在多个阿里云账号中跨地域创建资源栈。每个资源栈中包含的所有资源由资源栈组的ROS模板定义。 |
| 实例RAM角色 | 当ECS实例或部署在ECS实例上的应用需要访问其他云资源时，必须配置访问凭证，阿里云服务会通过访问凭证验证您的身份信息和访问权限。实例RAM角色允许您将一个角色关联到ECS实例，实现在实例内部自动获取并刷新临时访问凭证，无需直接暴露AccessKey，减少密钥泄露的风险。 |
| 业务RAM角色 | 创建在其他账号中的RAM角色，通过扮演该角色获取STS临时凭证，使用临时凭证跨账号访问其他账号云资源完成业务操作。为方便区分，在本解决方案中，统一叫为业务RAM角色或者业务角色。 |

## 安全性

### 资源编排安全性

资源编排已与操作审计服务集成，您可以在操作审计中查询用户操作资源编排产生的管控事件。操作审计支持将管控事件投递到日志服务SLS的LogStore或对象存储OSS的存储空间中，满足实时审计、问题回溯分析等需求。

同时，资源编排服务支持对ROS模板进行资源创建前的合规性检测。关于支持合规预检的云服务，请参见[托管规则列表](https://help.aliyun.com/zh/document_detail/127404.html)。

## 注意事项

### 支持STS的云服务

详情参见[支持STS的云服务](https://help.aliyun.com/zh/ram/services-that-work-with-sts)。

## 自动化模板

### 模板介绍

您的应用程序需要跨账号角色扮演到其他账号，使用其他角色身份调用OpenAPI，首先您需要跨账号批量完成被扮演的角色的创建。本方案提供基于Terraform的自动化模板，为资源目录下的目标账号批量创建 RAM 角色。

### 模板地址

模板详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-cross-account-sts-token)。

## 实施步骤

### 实施准备

- 请确保您已经开通资源目录。具体操作，请参考[开通资源目录](https://help.aliyun.com/zh/resource-management/user-guide/enable-a-resource-directory#task-hyc-zp1-dhb)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 应用程序实现无AK架构（推荐）

为保证AccessKey凭证安全，避免因为AccessKey凭证泄露导致的安全问题，不管是运维账号（应用程序部署在该账号）还是其他业务账号（需要跨账号操作该账号资源），他们的固定AccessKey都不应该硬编码在您的应用程序中，建议您的应用程序实现无AK架构，使用STS临时凭证代替固定AccessKey。针对不同类型的云上应用部署方式，您可以选择相应的方案实现STS临时凭证的使用：

- 针对在ECS实例上部署的应用，[通过ECS实例角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-240)，将RAM角色跟实例进行绑定，应用程序中即可通过ECS实例RAM角色，获取实例RAM角色的STS临时授权访问凭证。
- 针对在ACK上部署的应用，在容器服务Kubernetes版中，一个集群可以部署多个服务，同一个容器节点可能包含多个不同服务的Pod，在多租户场景下，若部署不受信任的服务，该服务可直接访问ECS的元数据服务（Meta Data Server），获取Worker节点关联实例RAM角色的临时令牌STS Token，会造成身份权限的泄露。[通过容器服务RRSA实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-241)，在Pod维度即可扮演对应角色实现STS临时凭证的获取。
- 针对在函数计算中部署的Serverless应用，[通过FC函数角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-242)，将RAM角色跟函数进行绑定，应用程序中即可通过函数RAM角色，获取RAM角色的STS临时授权访问凭证。

对于必须使用固定AccessKey的场景，比如需要访问不支持STS临时凭证的云服务，建议对AccessKey进行集中化管控。推荐以下解决方案：

- [通过KMS实现固定AccessKey的集中管控](https://help.aliyun.com/zh/well-architected/solution-237)，通过该方式，可以实现AccessKey的集中化管控，当业务需要使用AccessKey时，可以为其托管一个RAM用户AccessKey，并可以设置自动轮转周期，降低AccessKey泄漏风险。轮转时凭据管家会调用访问控制RAM（Resource Access Management），先创建一个新的AccessKey，然后删除旧的AccessKey。同时KMS将新的AccessKey写入凭据值，并删除旧的AccessKey对应的凭据值。当您发现RAM凭据泄露时，可以通过立即轮转凭据进行应急处理，此时推荐将轮转时长设置为30分钟实现快速轮转，降低泄漏造成的损失。

本方案中，以部署在运维账号下的ECS实例中的应用程序为例，跨账号操作业务账号下的资源。接下来简单介绍在创建ECS实例时，如何为ECS实例绑定RAM角色。更详细的配置方式，您可以参考[通过ECS实例角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-240)。

1. 登入运维账号，前往[实例创建页](https://ecs-buy.aliyun.com/wizard/#/)。
2. 选择**自定义购买**页签。
3. 按需选择付费类型、地域、实例规格、镜像等配置。各配置项详细说明，请参考[配置项说明](https://help.aliyun.com/zh/ecs/user-guide/create-an-instance-by-using-the-wizard)。
4. 展开**高级选型（选填）**表单，在**实例RAM角色**中，选择要绑定的RAM角色。本方案中，以名为EcsInstanceRole的实例角色为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7076581571/p968998.png)
5. 在最终创建实例前，请在页面右侧检查实例的整体配置并配置使用时长等选项，确保各项配置符合您的要求。
6. 阅读并签署**《云服务器ECS服务条款》**等服务协议（若已签署，则无需重复签署，请以页面提示为准），然后单击**确认下单**。

创建实例一般需要3~5分钟，请您耐心等待。您可前往控制台的实例列表页面查看实例的状态，当实例状态变为**运行中**时，表示实例创建完成。

#### 配置实例角色权限

本方案中，以部署在运维账号下的ECS实例中的应用程序为例，您需要为ECS实例角色授予权限，允许ECS实例角色可以调用角色扮演的API，跨账号扮演到其他业务账号的RAM角色上。如果您使用的是容器服务RRSA、函数角色或者固定AccessKey的方案，也需要按照如下步骤，给对应的RAM角色和RAM用户配置权限策略。

1. 登入运维账号，前往[RAM控制台](https://ram.console.aliyun.com)。
2. 左侧导航栏中，单击**权限管理** > **权限策略**。
3. 单击**创建权限策略**按钮，进入创建权限策略页面，切换为**脚本编辑**。
4. 将以下策略内容复制到策略文档输入框中，注意将内容中的`<业务RAM角色的名称>`替换为下一章节**通过ROS跨账号批量创建角色**中，在其他业务账号中批量创建的业务RAM角色（既需要跨账号扮演的角色）的名称。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "acs:ram:*:*:role/<业务RAM角色的名称>"
 }
 ]
}`
5. 如果您有多个业务RAM角色需要扮演，可以在Resource中继续增加。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": [
 "acs:ram:*:*:role/<业务RAM角色1的名称>",
 "acs:ram:*:*:role/<业务RAM角色2的名称>"
 ]
 }
 ]
}`
6. 单击**继续编辑基本信息**，填写策略名称等基本信息，这里策略名称以EcsInstanceRolePolicy为例。
7. 单击**确定**，完成策略创建。
8. 在左侧导航栏，选择**身份管理** > **角色**。
9. 在角色页面，找到目标ECS实例RAM角色，既上一个章节中，为ECS实例绑定的RAM角色，本方案中，以名为EcsInstanceRole的实例角色为例，单击**操作**列的**新增授权**。
10. 在**新增授权**面板，为RAM角色授权。其中权限策略，选择刚刚创建出来的权限策略，这里以EcsInstanceRolePolicy为例
11. 单击**确认新增授权**，完成权限策略的绑定。

#### 通过ROS跨账号批量创建角色

您的应用程序需要跨账号角色扮演到其他账号，使用其他账号角色身份调用OpenAPI完成跨账号的资源操作。因此，您需要跨账号批量完成被扮演的角色的创建。您可以使用ROS模版创建资源栈组。通过该ROS模版和资源栈组为资源目录下的目标账号批量创建RAM角色。

##### 创建委派管理员

通过委派管理员账号，可以将组织管理任务与业务管理任务相分离，企业管理账号执行资源目录的组织管理任务，委派管理员账号执行ROS的业务管理任务，这符合安全最佳实践的建议。接下来将资源目录的共享服务账号或运维账号设置为委派管理员账号，从而作为ROS的管理员账号为成员账号部署资源栈。

1. 使用管理账号登录[资源管理控制台](https://resourcemanager.console.aliyun.com/?spm=a2c4g.11186623.0.0.1272250aoGn651)。
2. 在左侧导航栏，选择**资源目录 > 可信服务**。
3. 在**可信服务**页面，单击**资源编排(ROS)**服务**操作**列的**管理**。
4. 在**委派管理员账号**区域，单击**添加**。
5. 在**添加委派管理员账号**面板，选中成员(共享服务账号)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7076581571/p969000.png)
6. 单击**确定**。添加成功后，使用该委派管理员账号访问对应可信服务的多账号管理模块，即可进行资源目录组织范围内的管理操作。

##### 开启可信访问

当您开通了资源目录，使用资源目录的企业管理账号或委派管理员账号创建服务管理权限模式的资源栈组时，必须开启可信访问，授权服务管理权限。需要企业管理账号和委派管理员账号都开启可信访问。

1. 分别使用企业管理账号和共享服务账号（委派管理员）登录[资源编排控制台](http://ros.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源栈组**。
3. 在**资源栈组列表**页面，单击右上角的**开启可信访问**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7076581571/p969001.png)

##### 批量创建所需角色

1. 使用共享服务账号登录[资源编排控制台](https://ros.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源栈组**。
3. 在顶部菜单栏的地域下拉列表，选择资源栈组的所在地域。
4. 在**资源栈组列表**页面，单击**创建资源栈组**。
5. 在**指定模板**选择框中，勾选**选择已有模板**。
6. **模板录入方式**选择**输入模板**，**模板内容**选择**Terraform**。
7. 内容文本框右上角，选择打开本地文件夹。
8. 选择下载到本地的[部署代码](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-cross-account-sts-token/deployment/create-role-cross-account)，点击下一步。
9. 输入**资源栈组名称**和**资源栈组描述**，在**配置模板参数**页面，填写所需参数，然后单击下一步。参数名称参数值示例描述角色的名称CentralizedOperationRole批量创建的角色的名称策略名CentralizedOperationRolePolicy绑定到该角色的权限策略的名称策略内容{"Version":"1","Statement":[{"Action":"ecs:*","Resource":"*","Effect":"Allow"}]}绑定到该角色的权限策略内容。既跨账号资源操作的所有权限。角色可信的账号1254004********角色的可信账号，既允许扮演到该新建角色的账号，不填默认为当前账号（运维账号）授信对象类型RamRole可信账号下允许扮演该新建角色的对象的类型，枚举值：RamRole（RAM角色）、RamUser（RAM用户）可信账号下允许扮演的RAM角色或者RAM用户EcsInstanceRole可信账号下允许扮演该新建角色的对象的名称，如果授信对象类型为RamRole（RAM角色），那么请填写对应RAM角色名称，如果RamUser（RAM用户），那么请填写对应RAM用户名称。请确保填写的RAM角色或者RAM用户在可信账号下已经存在，否则会创建失败。
10. 在**配置资源栈组**页面，选择**服务管理权限**，然后单击**下一步**。
11. 在**设置部署选项**页面，**部署目标**选择资源目录的目标账号的资源夹，同时启用**自动部署**。
12. 根据实际情况填写**地域**、**资源组**、**标签**、**部署选项**等信息，更多信息，请参见[参数说明](https://help.aliyun.com/zh/ros/user-guide/step-3-create-a-stack-group)。然后单击**下一步**。
13. 在**检查并确认**页面，检查资源栈组信息无误后，单击**创建资源栈组**。
14. 创建完成后，在该资源栈组的详情页的**实例**页签中，可以查看实例的状态，**最新**表示已经在业务账号下完成了角色的创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7076581571/p969002.png)

#### 跨账号获取并使用临时凭证

如果您的应用程序实现了无AK架构，首先您需要获取运维账号下ECS实例角色的STS临时凭据，强烈推荐您使用阿里云的Credentials工具，帮助您轻松地获取和管理访问凭证：

- 基于实例RAM角色获取临时凭证时，Credentials工具会自动调用ECS的元数据服务（Meta Data Server）获取临时访问凭证。
- Credentials工具会自动维护实例RAM角色的临时凭证的生命周期，研发人员无需关心实例RAM角色的临时凭证的到期更新，Credentials工具会自动保证凭证的周期性更新。
- 借助Credentials工具的默认凭据链，可以用同一套代码，通过程序之外的配置来控制不同环境下的凭据获取方式

Credentials工具支持多种方式初始化凭据客户端，您可根据实际情况选择合适的方式进行凭据客户端初始化。更多信息，请参考[管理访问凭据](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials)。

您在获取到ECS实例角色的临时凭证以后，还需要跨账号角色扮演到其他账号，使用其他角色身份调用OpenAPI。需要以ECS实例RAM角色的身份调用STS服务的[AssumeRole](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)接口，设置Token的最大过期时间，即可换取到临时凭据STS Token，再使用该STS Token调用OpenAPI，实现跨账号的资源操作。

##### 阿里云V2.0 SDK

如果您使用V2.0版本的阿里云SDK，可以很方便的集成阿里云的Credentials工具，通过Credentials工具获取ECS实例角色的STS临时凭证，然后以ECS实例RAM角色的身份跨账号角色扮演到其他业务账号上进行资源操作。

以Java为例，通过Maven方式安装Credentials工具和STS服务依赖：

```
<!--STS服务SDK V2.0-->
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>sts20150401</artifactId>
    <version>1.1.4</version>
</dependency>
<!-- 推荐使用最新版本 -->
<!--获取所有已发布的版本列表，请参见https://github.com/aliyun/credentials-java/blob/master/ChangeLog.txt-->
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>credentials-java</artifactId>
    <version>LATEST</version>
</dependency>
```

###### 通过RAM Role Provider跨账号获取STS Token（推荐）

推荐您使用Credentials工具提供的RAM Role Provider来跨账号角色扮演到其他业务账号。

1. 首先，您需要初始化代表当前程序身份的Provider，建议您通过角色STS Token临时凭证的方式保证您当前程序身份是无AK架构。以ECS实例角色为例，您需要初始化Credentials工具提供的`EcsRamRoleCredentialProvider`，在`EcsRamRoleCredentialProvider`中指定ECS实例角色的名称。Credentials工具还提供了更多Provider来适配其他无AK架构场景，比如，如果您部署在ACK集群上的应用实现了无AK架构，您可以使用`OIDCRoleArnCredentialProvider`来定义当前应用程序身份。
2. 然后通过`EcsRamRoleCredentialProvider`初始化RAM Role Provider：`RamRoleArnCredentialProvider`。在`RamRoleArnCredentialProvider`定义需要跨账号扮演的业务角色。
3. 最后，使用`RamRoleArnCredentialProvider`来初始化凭据客户端Credentials Client，Credentials Client会自动使用当前程序身份（ECS实例角色）扮演到目标业务角色，获取业务角色的临时凭据STS Token。同时，支持自动刷新STS Token，研发人员无需关心跨账号获取到的STS Token的有效期和到期刷新的逻辑。

```
package org.example.sdk2_0;

import com.alibaba.fastjson2.JSON;
import com.aliyun.credentials.Client;
import com.aliyun.credentials.provider.EcsRamRoleCredentialProvider;
//import com.aliyun.credentials.provider.EnvironmentVariableCredentialsProvider;
//import com.aliyun.credentials.provider.OIDCRoleArnCredentialProvider;
import com.aliyun.credentials.provider.RamRoleArnCredentialProvider;
import com.aliyun.sts20150401.models.GetCallerIdentityResponse;
import com.aliyun.tea.TeaException;
import com.aliyun.teautil.models.RuntimeOptions;

public class RamRoleCredentialSample {

    public static void main(String[] args) throws Exception {
        // 初始化凭据Provider，代表应用程序当前的角色身份，保证您的应用程序本身是无AK的
        // 这里您需要根据具体场景，通过对应的Provider类进行初始化。常见的有以下几种：
        // 1. 使用ECS实例RAM角色
        EcsRamRoleCredentialProvider originalProvider = EcsRamRoleCredentialProvider.builder()
            // 请替换为绑定到ECS实例上的RAM角色名称
            .roleName("<EcsInsatnceRoleName>")
            .build();
        // 2. 使用环境变量
        //EnvironmentVariableCredentialsProvider originalProvider = new EnvironmentVariableCredentialsProvider();
        // 3. 使用OIDC RAM角色
        //OIDCRoleArnCredentialProvider originalProvider = OIDCRoleArnCredentialProvider.builder()
        //    .roleArn(System.getenv("ALIBABA_CLOUD_ROLE_ARN"))
        //    .oidcProviderArn(System.getenv("ALIBABA_CLOUD_OIDC_PROVIDER_ARN"))
        //    .oidcTokenFilePath(System.getenv("ALIBABA_CLOUD_OIDC_TOKEN_FILE"))
        //    // 角色会话名称，如果配置了ALIBABA_CLOUD_ROLE_SESSION_NAME这个环境变量，则无需设置
        //    .roleSessionName("<RoleSessionName>")
        //    // 设置更小的权限策略，非必填。示例值：{"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"}
        //    .policy("<Policy>")
        //    .roleSessionName("3600")
        //    .build();

        // 使用当前角色作为入参，初始化角色扮演的Provider，实现角色链式扮演，同时支持跨账号扮演角色
        RamRoleArnCredentialProvider provider = RamRoleArnCredentialProvider.builder()
            .credentialsProvider(originalProvider)
            .durationSeconds(3600)
            // 请替换为您实际要扮演的RAM角色ARN
            // 格式为 acs:ram::${账号 ID}:role/${角色名称}
            .roleArn("<RoleArn>")
            .build();

        // 通过Provider初始化凭据客户端，通过客户端获取角色扮演后最终的STS Token
        // 研发无需关心STS Token有效期和重新获取的逻辑，此方式支持自动刷新STS Token
        Client credentialClient = new Client(provider);

        // 调用API，跨账号进行资源操作
        // 以调用GetCallerIdentity获取当前调用者身份信息为例
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config()
            .setCredential(credentialClient)
            // 地域，以华东1（杭州）为例
            .setRegionId("cn-hangzhou");
        com.aliyun.sts20150401.Client stsClient = new com.aliyun.sts20150401.Client(config);
        RuntimeOptions runtimeOptions = new RuntimeOptions()
            // 开启自动重试机制，只会对超时等网络异常进行重试
            .setAutoretry(true)
            // 设置自动重试次数，默认3次
            .setMaxAttempts(3);

        try {
            GetCallerIdentityResponse getCallerIdentityResponse = stsClient.getCallerIdentityWithOptions(runtimeOptions);
            System.out.println(JSON.toJSONString(getCallerIdentityResponse));
        } catch (TeaException e) {
            // 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            e.printStackTrace();
            // 打印错误码
            System.out.println(e.getCode());
            // 打印错误信息，错误信息中包含 RequestId
            System.out.println(e.getMessage());
            // 打印服务端返回的具体错误内容
            System.out.println(e.getData());
        }
    }
}
```

详细代码示例请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-cross-account-sts-token/code-example/java/common/src/main/java/org/example/sdk2_0/RamRoleCredentialSample.java)。如果您需要使用JAVA异步SDK，和上述同步SDK不同的是，您需要依赖以下的Credentials工具，具体请参考[异步代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-cross-account-sts-token/code-example/java/common/src/main/java/org/example/sdk2_0/RamRoleCredentialAsyncSample.java)。

```
<!-- 推荐使用最新版本 -->
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-auth</artifactId>
  <version>0.2.16-beta</version>
</dependency>
```

除了以上的简单代码示例，本方案也提供了针对JAVA SpringBoot的代码示例，保证Credentials客户端作为单例进行复用。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-cross-account-sts-token/code-example/java/spring-boot/ram-role-credential/sdk-v2)。

###### 通过AssumeRole接口跨账号获取STS Token

该方式需要您自行关心STS Token的到期处理，建议您使用上述**通过RAM Role Provider跨账号获取STS Token**的方式，如此，实现STS Token的自动刷新，您的研发人员无需关心跨账号获取到的STS Token的有效期和到期刷新的逻辑。

您在获取到ECS实例角色的临时凭证以后，还需要跨账号角色扮演到其他业务账号，需要以ECS实例RAM角色的身份调用STS服务的[AssumeRole](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)接口，扮演到业务账号下的业务角色上，即可换取到业务角色的临时凭据STS Token，再使用该STS Token调用OpenAPI，实现跨账号的资源操作。

```
import com.aliyun.credentials.models.CredentialModel;
import com.aliyun.credentials.utils.ParameterHelper;
import com.aliyun.sts20150401.models.AssumeRoleRequest;
import com.aliyun.sts20150401.models.AssumeRoleResponse;
import com.aliyun.sts20150401.models.AssumeRoleResponseBody;
import com.aliyun.sts20150401.models.GetCallerIdentityResponse;
import com.aliyun.tea.TeaException;
import com.aliyun.teautil.models.RuntimeOptions;
// import com.alibaba.fastjson2.JSON;

public class AssumeRoleSample {

    public static void main(String[] args) throws Exception {
        // 初始化凭据客户端，使用Credentials工具，保证您的应用程序本身是无AK的
        // 借助Credentials工具的默认凭据链，您可以用同一套代码，通过程序之外的配置来控制不同环境下的凭据获取方式
        // 当您在初始化凭据客户端不传入任何参数时，Credentials工具将会尝试按照如下顺序查找相关凭据信息（优先级由高到低）：
        // 1. 使用系统属性
        // 2. 使用环境变量
        // 3. 使用OIDC RAM角色
        // 4. 使用配置文件
        // 5. 使用ECS实例RAM角色（需要通过环境变量 ALIBABA_CLOUD_ECS_METADATA 指定 ECS 实例角色名称；通过环境变量 ALIBABA_CLOUD_ECS_IMDSV2_ENABLE=true 开启在加固模式下获取STS Token）
        // 详情请参考：https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials#3ca299f04bw3c
        // 要使用默认凭据链，初始化 Client 时，必须使用空的构造函数，不能配置 Config 入参
        // 除了使用默认凭据链，您也可以在代码中显式配置，来初始化凭据客户端
        // 详情请参考：https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials#a9e9aa404bzfy
        com.aliyun.credentials.Client credentialClient = new com.aliyun.credentials.Client();

        // 跨账号角色扮演获取STS Token
        // 如果您缓存了该STS Token，需要特别注意STS Toke的到期时间，避免缓存时间过长而STS Token过期导致程序错误
        CredentialModel assumeRoleCredentialModel = createAssumeRoleCredential(credentialClient);

        // 调用API，跨账号进行资源操作
        // 以调用GetCallerIdentity获取当前调用者身份信息为例
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config()
            .setAccessKeyId(assumeRoleCredentialModel.getAccessKeyId())
            .setAccessKeySecret(assumeRoleCredentialModel.getAccessKeySecret())
            .setSecurityToken(assumeRoleCredentialModel.getSecurityToken())
            // 地域，以华东1（杭州）为例
            .setRegionId("cn-hangzhou");
        com.aliyun.sts20150401.Client stsClient = new com.aliyun.sts20150401.Client(config);
        RuntimeOptions runtimeOptions = new RuntimeOptions()
            // 开启自动重试机制，只会对超时等网络异常进行重试
            .setAutoretry(true)
            // 设置自动重试次数，默认3次
            .setMaxAttempts(3);

        try {
            GetCallerIdentityResponse getCallerIdentityResponse = stsClient.getCallerIdentityWithOptions(runtimeOptions);
            // System.out.println(JSON.toJSONString(getCallerIdentityResponse));
        } catch (TeaException e) {
            // 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            e.printStackTrace();
            // 打印错误码
            System.out.println(e.getCode());
            // 打印错误信息，错误信息中包含 RequestId
            System.out.println(e.getMessage());
            // 打印服务端返回的具体错误内容
            System.out.println(e.getData());
        }
    }

    public static CredentialModel createAssumeRoleCredential(com.aliyun.credentials.Client credentialClient) throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config()
            .setCredential(credentialClient)
            // 地域，以华东1（杭州）为例
            .setRegionId("cn-hangzhou");

        com.aliyun.sts20150401.Client stsClient = new com.aliyun.sts20150401.Client(config);
        RuntimeOptions runtimeOptions = new RuntimeOptions()
            // 开启自动重试机制，只会对超时等网络异常进行重试
            .setAutoretry(true)
            // 设置自动重试次数，默认3次
            .setMaxAttempts(3);
        AssumeRoleRequest assumeRoleRequest = new AssumeRoleRequest()
            // 请替换为您实际要扮演的RAM角色ARN
            // 格式为 acs:ram::${账号 ID}:role/${角色名称}
            .setRoleArn("<role-arn>")
            // 角色会话名称
            .setRoleSessionName("WellArchitectedSolutionDemo")
            // 设置会话权限策略，进一步限制STS Token 的权限，如果指定该权限策略，则 STS Token 最终的权限策略取 RAM 角色权限策略与该权限策略的交集
            // 非必填。示例值：{"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"}
            .setPolicy("{\"Statement\": [{\"Action\": [\"*\"],\"Effect\": \"Allow\",\"Resource\": [\"*\"]}],"
                + "\"Version\":\"1\"}")
            // STS Token 有效期，单位：秒
            .setDurationSeconds(3600L);
        AssumeRoleResponse assumeRoleResponse = stsClient.assumeRoleWithOptions(assumeRoleRequest, runtimeOptions);
        AssumeRoleResponseBody.AssumeRoleResponseBodyCredentials credentials = assumeRoleResponse.getBody().getCredentials();

        // 返回角色扮演获取到的STS Token
        return CredentialModel.builder()
            .accessKeyId(credentials.getAccessKeyId())
            .accessKeySecret(credentials.getAccessKeySecret())
            .securityToken(credentials.getSecurityToken())
            .expiration(ParameterHelper.getUTCDate(credentials.getExpiration()).getTime())
            .build();
    }
}
```

上述是一个简单的代码示例，详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-cross-account-sts-token/code-example/java/common/src/main/java/org/example/sdk2_0/AssumeRoleSample.java)。需要注意的是：

1. 千万不要频繁创建Credentials工具的客户端：`com.aliyun.credentials.Client`，比如，您每次请求阿里云API时，都创建一个Credentials工具的客户端。这样容易导致内存泄露的问题，影响您的业务稳定性。建议您创建唯一一个Credentials工具的客户端，作为单例进行复用。
2. 为减少对STS服务的依赖，提升响应处理效率，您在跨账号获取到业务RAM角色的STS Token后，可能会对该STS Token进行缓存，缓存时需要特别注意当前STS Toke的到期时间，您的缓存时间一定要小于STS Token有效期，避免缓存时间过长而STS Token过期导致程序错误。

除了以上的简单代码示例，本方案也提供了针对JAVA SpringBoot的代码示例，保证Credentials客户端作为单例进行复用，同时增加了缓存机制。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-cross-account-sts-token/code-example/java/spring-boot/assume-role/sdk-v2)。

##### 阿里云V1.0 SDK

阿里云V1.0 SDK是较早使用版本，稳定性良好，不少老用户习惯于V1.0 SDK的开发。对于新用户则建议直接使用V2.0 SDK，老用户也建议尽早迁移到新版SDK。迁移方式请参考[升级V1.0 SDK指南](https://help.aliyun.com/zh/sdk/developer-reference/upgrade-v1-sdk-guide)。

使用阿里云V1.0 SDK也可以集成阿里云的Credentials工具，通过Credentials工具获取ECS实例角色的STS临时凭证，保证全链路不会暴露固定AccessKey。

以Java为例，通过Maven方式安装Credentials工具和STS服务依赖：

```
<!--STS服务SDK V1.0-->
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-sts</artifactId>
    <version>3.1.2</version>
</dependency>
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>[4.0.0,5.0.0)</version>
</dependency>
<!-- 推荐使用最新版本 -->
<!--获取所有已发布的版本列表，请参见https://github.com/aliyun/credentials-java/blob/master/ChangeLog.txt-->
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>credentials-java</artifactId>
    <version>LATEST</version>
</dependency>
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>tea</artifactId>
  <version>LATEST</version>
</dependency>
```

###### 通过AssumeRole Provider跨账号获取STS Token

您在获取到ECS实例角色的临时凭证以后，还需要跨账号角色扮演到其他业务账号，您可以使用Credentials工具的客户端初始化AssumeRole Provider：STSAssumeRoleSessionCredentialsProvider，STSAssumeRoleSessionCredentialsProvider会帮您自动通过角色扮演跨账号获取业务角色STS Token，通过STSAssumeRoleSessionCredentialsProvider会自动刷新STS Token，研发人员无需关心跨账号获取到的STS Token的到期更新，然后通过该STSAssumeRoleSessionCredentialsProvider初始化SDK V1.0的客户端，即可调用阿里云API，完成跨账号的资源操作。

```
import com.aliyun.credentials.models.CredentialModel;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.auth.BasicSessionCredentials;
import com.aliyuncs.auth.STSAssumeRoleSessionCredentialsProvider;
import com.aliyuncs.exceptions.ClientException;
import com.aliyuncs.exceptions.ServerException;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.sts.model.v20150401.GetCallerIdentityRequest;
import com.aliyuncs.sts.model.v20150401.GetCallerIdentityResponse;
// import com.alibaba.fastjson2.JSON;

public class AssumeRoleSample {
    public static void main(String[] args) {
        // 初始化凭据客户端，使用Credentials工具，保证您的应用程序本身是无AK的
        // 借助Credentials工具的默认凭据链，您可以用同一套代码，通过程序之外的配置来控制不同环境下的凭据获取方式
        // 当您在初始化凭据客户端不传入任何参数时，Credentials工具将会尝试按照如下顺序查找相关凭据信息（优先级由高到低）：
        // 1. 使用系统属性
        // 2. 使用环境变量
        // 3. 使用OIDC RAM角色
        // 4. 使用配置文件
        // 5. 使用ECS实例RAM角色（需要通过环境变量 ALIBABA_CLOUD_ECS_METADATA 指定 ECS 实例角色名称；通过环境变量 ALIBABA_CLOUD_ECS_IMDSV2_ENABLE=true 开启在加固模式下获取STS Token）
        // 详情请参考：https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials#3ca299f04bw3c
        // 要使用默认凭据链，初始化 Client 时，必须使用空的构造函数，不能配置 Config 入参
        // 除了使用默认凭据链，您也可以在代码中显式配置，来初始化凭据客户端
        // 详情请参考：https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials#a9e9aa404bzfy
        com.aliyun.credentials.Client credentialClient = new com.aliyun.credentials.Client();

        // 以华东1（杭州）为例
        DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou");
        // 用凭据客户端初始化角色扮演的CredentialsProvider：STSAssumeRoleSessionCredentialsProvider，实现跨账号角色扮演
        // 该CredentialsProvider支持自动刷新STS Token
        STSAssumeRoleSessionCredentialsProvider provider = new STSAssumeRoleSessionCredentialsProvider(
            () -> {
                // 保证线程安全，从 CredentialModel 中获取 ak/sk/security token
                CredentialModel credentialModel = credentialClient.getCredential();
                String ak = credentialModel.getAccessKeyId();
                String sk = credentialModel.getAccessKeySecret();
                String token = credentialModel.getSecurityToken();
                return new BasicSessionCredentials(ak, sk, token);
            },
            // 请替换为您实际要扮演的RAM角色ARN
            // 格式为 acs:ram::${账号 ID}:role/${角色名称}
            "<role-arn>",
            profile
        )
        // 角色会话名称
        .withRoleSessionName("WellArchitectedSolutionDemo")
        // STS Token 有效期，单位：秒
        .withRoleSessionDurationSeconds(3600L);
        
        // 初始化SDK 1.0客户端
        IAcsClient iAcsClient =  new DefaultAcsClient(profile, provider);

        // 调用API，跨账号进行资源操作
        // 以调用GetCallerIdentity获取当前调用者身份信息为例
        GetCallerIdentityRequest getCallerIdentityRequest = new GetCallerIdentityRequest();
        try {
            GetCallerIdentityResponse getCallerIdentityResponse = iAcsClient.getAcsResponse(getCallerIdentityRequest);
            // System.out.println(JSON.toJSONString(getCallerIdentityResponse));
        } catch (ServerException e) {
            // 示例仅做打印展示。请重视异常处理，在工程项目中切勿直接忽略异常。
            // 打印整体的错误输出
            e.printStackTrace();
            // 打印错误码
            System.out.println(e.getErrCode());
            // 打印 RequestId
            System.out.println(e.getRequestId());
            // 打印错误信息
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            // 示例仅做打印展示。请重视异常处理，在工程项目中切勿直接忽略异常。
            // 打印整体的错误输出
            e.printStackTrace();
            // 打印错误码
            System.out.println(e.getMessage());
        }
    }
}
```

上述是一个简单的代码示例，详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-cross-account-sts-token/code-example/java/common/src/main/java/org/example/sdk1_0/AssumeRoleSample.java)。需要注意的是：

1. 千万不要频繁创建Credentials工具的客户端：`com.aliyun.credentials.Client`，比如，您每次请求阿里云API时，都创建一个Credentials工具的客户端。这样容易导致内存泄露的问题，影响您的业务稳定性。建议您创建唯一一个Credentials工具的客户端，作为单例使用。
2. 同理，对于V1.0 SDK的客户端：`com.aliyuncs.IAcsClient`，为防止内存泄露，建议您为每个业务账号初始化唯一一个IAcsClient客户端，作为单例复用。比如，您有两个业务账号，需要跨账号到业务账号里进行资源操作，此时，您可以创建两个IAcsClient客户端，分别对应这两个业务账号，每次需要跨账号操作时，都是复用对应的IAcsClient客户端。

除了以上的简单代码示例，本方案也提供了针对JAVA SpringBoot的代码示例，保证Credentials客户端和IAcsClient客户端作为单例进行复用。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-cross-account-sts-token/code-example/java/spring-boot/assume-role/sdk-v1)。

##### Terraform

如果您基于IaC的方式使用Terraform来管理您的云上资源，阿里云的Terraform Provider：[Alibaba Cloud Provider](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs)同样支持通过角色扮演的方式跨账号操作云资源。

1. 如果您的Terraform代码运行在阿里云ECS实例上，您可以使用ECS实例角色跨账号扮演到其他业务账号的业务角色上，进行跨账号资源操作，实现全链路无AK。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-cross-account-sts-token/code-example/terraform/ecs-instance-role)。`# 配置provider，跨账号扮演角色
provider "alicloud" {
 # ECS实例角色名称
 ecs_role_name = "EcsInstanceRole"
 # 地域，以华东1（杭州）为例
 region = "cn-hangzhou"
 assume_role {
 # 请替换为您实际要扮演的RAM角色ARN
 # 格式为 acs:ram::${账号 ID}:role/${角色名称}
 role_arn = "<role-arn>"
 # 设置会话权限策略，进一步限制STS Token 的权限，如果指定该权限策略，则 STS Token 最终的权限策略取 RAM 角色权限策略与该权限策略的交集
 # 非必填。示例值：{"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"}
 policy = "{\"Statement\": [{\"Action\": [\"*\"],\"Effect\": \"Allow\",\"Resource\": [\"*\"]}],\"Version\":\"1\"}"
 # 角色会话名称
 session_name = "WellArchitectedSolutionDemo"
 # STS Token 有效期，单位：秒
 session_expiration = 3600
 }
}

# 跨账号进行资源操作
# 以获取当前调用者身份信息为例
data "alicloud_caller_identity" "current" {
}

output "caller_identity" {
 value = data.alicloud_caller_identity.current
}`
2. 如果您的Terraform代码运行在阿里云ACK集群上，您可以通过ACK RRSA的功能，使用和Pod绑定的RAM角色跨账号扮演到其他业务账号的业务角色上，进行跨账号资源操作，实现全链路无AK。其中，OIDC身份提供商的配置信息，您可以通过环境变量获取，详情请参考解决方案[通过容器服务RRSA实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-241)，然后在执行Terraform模版时，通过模版入参的形式进行传递，比如，您可以通过命令`TF_VAR_oidc_provider_arn=$ALIBABA_CLOUD_OIDC_PROVIDER_ARN TF_VAR_oidc_role_arn=$ALIBABA_CLOUD_ROLE_ARN TF_VAR_oidc_token_file=$ALIBABA_CLOUD_OIDC_TOKEN_FILE terraform apply`执行Terraform模版。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-cross-account-sts-token/code-example/terraform/ack-rrsa)。`# OIDC身份提供商的ARN
# 格式为 acs:ram::${账号ID}:oidc-provider/ack-rrsa-${集群ID}
variable "oidc_provider_arn" {
 type = string
}

# Pod绑定的RAM角色ARN
# 格式为 acs:ram::${账号ID}:role/${角色名称}
variable "oidc_role_arn" {
 type = string
}

# 集群生成的OIDC Token的文件路径
variable "oidc_token_file" {
 type = string
}

# 配置provider，跨账号扮演角色
provider "alicloud" {
 region = "cn-hangzhou"
 assume_role_with_oidc {
 oidc_provider_arn = var.oidc_provider_arn
 role_arn = var.oidc_role_arn
 oidc_token_file = var.oidc_token_file
 role_session_name = "WellArchitectedSolutionDemo"
 }
 assume_role {
 # 请替换为您实际要扮演的RAM角色ARN
 # 格式为 acs:ram::${账号ID}:role/${角色名称}
 role_arn = "<role-arn>"
 # 设置会话权限策略，进一步限制STS Token 的权限，如果指定该权限策略，则 STS Token 最终的权限策略取 RAM 角色权限策略与该权限策略的交集
 # 非必填。示例值：{"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"}
 policy = "{\"Statement\": [{\"Action\": [\"*\"],\"Effect\": \"Allow\",\"Resource\": [\"*\"]}],\"Version\":\"1\"}"
 # 角色会话名称
 session_name = "WellArchitectedSolutionDemo"
 # STS Token 有效期，单位：秒
 session_expiration = 3600
 }
}

# 跨账号进行资源操作
# 以获取当前调用者身份信息为例
data "alicloud_caller_identity" "current" {
}

output "caller_identity" {
 value = data.alicloud_caller_identity.current
}`
3. 当然您也可以使用固定AccessKey，跨账号扮演到其他业务账号的业务角色上，进行跨账号资源操作（不推荐）。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-cross-account-sts-token/code-example/terraform/long-term-ak)。`# 配置provider，跨账号扮演角色
provider "alicloud" {
 # 该AK需要具有RAM AssumeRole权限
 access_key = "<your-access-key-id>"
 secret_key = "<your-access-key-secret>"
 # 地域，以华东1（杭州）为例
 region = "cn-hangzhou"
 assume_role {
 # 请替换为您实际要扮演的RAM角色ARN
 # 格式为 acs:ram::${账号 ID}:role/${角色名称}
 role_arn = "<role-arn>"
 # 设置会话权限策略，进一步限制STS Token 的权限，如果指定该权限策略，则 STS Token 最终的权限策略取 RAM 角色权限策略与该权限策略的交集
 # 非必填。示例值：{"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"}
 policy = "{\"Statement\": [{\"Action\": [\"*\"],\"Effect\": \"Allow\",\"Resource\": [\"*\"]}],\"Version\":\"1\"}"
 # 角色会话名称
 session_name = "WellArchitectedSolutionDemo"
 # STS Token 有效期，单位：秒
 session_expiration = 3600
 }
}

# 跨账号进行资源操作
# 以获取当前调用者身份信息为例
data "alicloud_caller_identity" "current" {
}

output "caller_identity" {
 value = data.alicloud_caller_identity.current
}`

##### 代码示例

###### 代码介绍

本方案提供常用语言的代码示例，覆盖阿里云SDK V1.0、SDK V2.0、Terraform等，方便客户能够快速完成应用改造。

###### 代码地址

代码详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-cross-account-sts-token)。

## 故障排除

### 为什么无法开通资源目录？

可能有如下两个原因：

- 当前账号没有进行企业实名认证。关于企业实名认证，请参见[企业实名认证](https://help.aliyun.com/zh/account/verify-your-identity-enterprise-account/)。
- 当前账号已经在资源目录内，无法重复开通。

### 为什么无法使用ROS服务管理权限模式？

- 如果使用资源目录成员账号执行ROS的业务管理任务，您需要将资源目录的成员账号设置为委派管理员账号，从而作为 ROS 的管理员账号为成员账号部署资源栈。关于 ROS 委派管理员，请参见[设置委派管理员账号](https://help.aliyun.com/zh/ros/user-guide/step-1-create-a-delegated-administrator-account)。
- 当您开通了资源目录，使用资源目录的企业管理账号或委派管理员账号创建服务管理权限模式的资源栈组时，必须开启可信访问，授权服务管理权限。关于可信访问，请参见[开启可信访问](https://help.aliyun.com/zh/ros/user-guide/step-2-enable-trusted-access)。

### 为什么创建ROS资源栈组时，报错：ServiceManagedPermissionAccountNotSupported

如果您委派了ROS的管理员，那么作为管理员的成员账号不允许成为ROS资源栈组的部署目标。既如果您创建资源栈组时，选择的部署目标中包含了作为管理员的成员账号，那么就会报错：ServiceManagedPermissionAccountNotSupported。此时，您可以：

- 如果您选择的部署目标是资源目录资源夹，您可以在资源目录控制台，将ROS管理账号移动到其他资源夹下，不要和其他业务账号混放到一起。
- 您也可以在部署目标中，直接手动选择具体的成员账号，此时，不要选择管理员账号即可。

### 为什么Credentials SDK报错：not found credentials？

如果您的应用程序部署在ECS上，并且通过ECS实例角色实现了无AK架构。

- 请确保您已经为您的ECS绑定了RAM实例角色，您可以登录到ECS实例上，执行命令：`curl http://100.100.100.200/latest/meta-data/ram/security-credentials/${实例角色名称}`，如果正确返回临时凭证，那么您已成功绑定了RAM实例角色。
- 如果您使用的是JAVA的Credentials SDK，请确保您的SDK版本>=0.3.4。
- 如果您使用的是Credentials工具的默认凭据链，请确保您已经配置了环境变量**ALIBABA_CLOUD_ECS_METADATA**，该环境变量的值配置为RAM实例角色的名称。
- 如果您在运行在ECS中的Docker环境中使用Credentials工具请确保Docker中可以正常访问到ECS Meta Service，您可以在Docker环境中，执行命令：`url http://100.100.100.200/latest/meta-data/ram/security-credentials/${实例角色名称}`，如果正确返回临时凭证，那么您的Docker环境可以正常访问ECS Meta Service。如果您使用的是Credentials工具的默认凭据链，请确保您在Docker环境中已经配置了环境变量**ALIBABA_CLOUD_ECS_METADATA**，该环境变量的值配置为RAM实例角色的名称。需要注意的是，这里不要把环境变量配置到ECS实例上。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-251（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
