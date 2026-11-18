<!-- source: https://help.aliyun.com/zh/well-architected/solution-240 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929195 -->

# 通过ECS实例角色实现临时凭证的获取和使用

本文介绍了一种部署在ECS实例上的应用程序获取和使用临时凭证（STS Token）的方案。避免直接把AccessKey固化在程序或实例中，引发泄露风险。

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969535.png)

凭证管理是云上最容易出现风险的环节之一，管理不善将导致凭证泄漏，进而导致数据泄漏、资产损失等严重安全事故。当ECS实例或部署在ECS实例上的应用需要访问其他云资源时，必须先通过访问凭证来验证身份信息和访问权限。实例RAM角色允许您将一个角色关联到ECS实例，使ECS实例及其上的应用基于STS临时凭证访问其他云资源，无需透露长期AccessKey，既可减少密钥泄露的风险，也可借助访问控制RAM精细化控制资源访问权限，避免权限过度分配。本方案主要介绍如何创建实例RAM角色并授予给ECS实例，以及如何基于实例RAM角色获取临时访问凭证。

## 方案优势

该方案能够显著提升云上应用程序的安全性、灵活性和便捷性，同时降低维护成本和操作复杂性。

### 提高安全性

通过ECS实例角色和RAM角色关联，使用STS Token访问云资源，避免了将访问密钥硬编码在代码中，从而消除AK泄露的风险。临时凭证（STS Token）的使用有效解决了永久凭证（AK/SK）可能带来的安全风险问题。

### 精细化管理权限

通过为不同ECS实例赋予具有特定授权策略的RAM角色，确保实例仅能访问其所需的资源，实现权限最小化。

### 增强灵活性

部署在ECS实例的程序可以通过阿里云官方SDK，设置实例角色认证方式，获取临时凭证STS Token。这种方式无需预先配置固定的访问凭证，可以根据需要动态获取和使用临时凭证。无需直接在ECS实例上管理凭证，权限的调整仅需通过修改RAM角色的授权策略来实现，快捷地维护ECS实例拥有的访问权限。

### 降低维护成本

使用临时凭证STS Token，无需频繁更新代码中的访问密钥，减少了维护成本和操作复杂性。本方案提供Java/Python代码示例，客户能够快速完成应用改造，减少开发和部署的复杂度。

## 客户场景

### 部署在ECS中的应用程序采用无AK架构

#### 场景描述

客户在ECS实例上部署的应用程序需要访问其他云资源，传统的方式是客户将RAM用户的AK（Access Key）固化在实例中，如果将AK写在配置文件中，容易造成AK泄露，维护困难等问题。ECS实例RAM角色通过将ECS实例和RAM角色关联，使用STS Token（Security Token Service）访问云资源，解决永久凭证可能导致的安全风险问题。

#### 适用客户

- **需要高安全性**：客户需要确保AK不被暴露，以防止安全漏洞。
- **动态管理访问权限**：客户需要动态管理和临时授予实例访问其他资源的权限，避免长期凭证带来的风险。
- **简化运维管理**：客户希望简化运维过程中对凭证的管理，减少手动维护的复杂性。

## 方案架构

本方案通过ECS实例角色实现临时凭证的获取和使用。该架构和流程通过动态管理和临时授予访问权限，避免了长期暴露AK的风险，提高了系统的安全性和灵活性。管理员仅需一次性配置角色和权限，后续实例在运行时即可动态获取和使用临时凭证，简化了运维管理工作。

管理员创建一个ECS实例类型的Role（角色），并对该角色授予相应的权限。角色权限包含访问需要的云资源的权限（图中1）。管理员将创建好的角色配置到对应的ECS实例上，使实例与角色关联（图中2）。客户应用程序通过调用ECS Meta服务的接口，获取临时安全凭证（STS Token）（图中3）。该过程中ECS Meta Server会调用AssumeRole接口，以云服务的身份扮演RAM角色，从RAM/STS服务获取STS Token，该过程对于用户而言无感知（图中i）。 客户应用程序使用获取到的STS Token来调用目标云资源服务的API。此时，应用程序使用临时凭证进行认证和授权（图中4）。资源服务API处理请求并返回访问结果，客户端应用程序接收到返回的结果后完成相应的业务逻辑。 ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969536.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 访问控制RAM | [访问控制RAM（Resource Access Management）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |
| 配置审计 | [配置审计（Cloud Config）](https://help.aliyun.com/zh/document_detail/127388.html)是一项资源审计服务，为您提供面向资源的配置历史追踪、配置合规审计等能力。面对大量资源，帮您轻松实现基础设施的自主监管，确保持续性合规。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/document_detail/133949.html)。 |
| 系统运维管理OOS | [系统管理与运维服务（CloudOps Orchestration Service, OOS）](https://help.aliyun.com/zh/oos/product-overview/introduction-to-oos)，是阿里云提供的云上自动化运维服务，能够自动化管理和执行任务。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/oos/product-overview/billing-1/)。 |
| 阿里云资源编排服务ROS | [资源编排服务ROS（Resource Orchestration Service）](https://help.aliyun.com/zh/ros/)可以帮助您简化云计算资源的管理。自动完成所有资源的创建和配置，实现自动化部署和运维。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/ros/product-overview/billing-overview)。 |
| 操作审计 | [操作审计（ActionTrail）](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)是阿里云提供的云账号资源操作记录的查询和投递服务，可用于安全分析、资源变更追踪以及合规性审计等场景。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/actiontrail/product-overview/billing-1)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |
| RAM管理员 | RAM管理员具备账号下RAM资源的管理权限。RAM管理员可以是阿里云账号（主账号），也可以是主账号下拥有AliyunRAMFullAccess权限的RAM用户，强烈推荐您使用RAM用户充当RAM管理员。 |
| 访问密钥（AccessKey） | 访问密钥AccessKey（简称AK）是阿里云提供给用户的永久访问凭据，一组由AccessKey ID和AccessKey Secret组成的密钥对。发起的请求会携带AccessKey ID和AccessKey Secret加密请求内容生成的签名，进行身份验证及请求合法性校验。 |
| RAM角色（RAM role） | RAM角色是一种虚拟用户，可以被授予一组权限策略。与RAM用户不同，RAM角色没有永久身份凭证（登录密码或访问密钥），需要被一个可信实体扮演。扮演成功后，可信实体将获得RAM角色的临时身份凭证，即安全令牌（STS Token），使用该安全令牌就能以RAM角色身份访问被授权的资源。 |
| 实例RAM角色 | ECS实例通过实例RAM角色获得该角色拥有的权限，可以基于临时安全令牌STS（Security Token Service）访问指定云服务的API和操作指定的云资源，安全性更高。 |
| 实例启动模板 | 包含了ECS实例的配置信息，使用实例启动模板创建ECS实例可以免去重复配置的操作。 |

## 安全性

### 元数据服务器访问模式

默认情况下，实例元数据服务器可同时通过普通模式和加固模式访问。为了进一步增强安全性，您可以设置实例元数据服务器访问模式为**仅加固模式**。采用ECS实例的元数据加固策略来获取RAM角色的初始化凭据，相较于普通模式，此方式采纳了一种更为严谨的安全逻辑：首先在ECS实例内部自动生成一个具有时效限制的token，利用此token作为凭据，向元数据服务（Metadata Server）请求获得STS（Security Token Service）临时凭证。这一系列操作构成了凭据客户端的安全初始化流程。什么是加固模式请参见[加固模式](https://help.aliyun.com/zh/ecs/user-guide/view-instance-metadata/)的介绍。

## 注意事项

### ECS实例角色限制

为ECS实例授予实例RAM角色存在以下限制：

- ECS实例的网络类型必须是专有网络VPC。
- 一台ECS实例只能授予一个实例RAM角色。

### ECS实例启动模板限制

- 一个账号在每个地域最多可创建30个实例启动模板。
- 创建实例启动模板时，所有参数都是可选的。但是，如果实例启动模板中未包含必要参数（例如实例规格、镜像等），则在使用该模板创建实例时还需要补充该必要参数。
- 模板一旦创建，不可修改，但支持创建新的版本。

### 元数据服务器加固模式限制

需确保实例的cloud-init版本为23.2.2。

- 部分最新发布的公共镜像支持cloud-init 23.2.2版本。在通过API接口[RunInstances](https://help.aliyun.com/zh/ecs/developer-reference/api-ecs-2014-05-26-runinstances)或[CreateInstance](https://help.aliyun.com/zh/ecs/developer-reference/api-ecs-2014-05-26-createinstance)创建新实例时，可以指定ImageId选择cloud-init 23.2.2版本的镜像，选用这些公共镜像创建的实例支持加固模式访问元数据。支持cloud-init 23.2.2版本的公共镜像信息，请参见[公共镜像发布记录](https://help.aliyun.com/zh/ecs/release-notes-2/)。
- 如果已有实例的cloud-init版本不满足要求，您可以升级cloud-init版本，从而支持加固模式。检查cloud-init版本及升级方法，请参见[安装cloud-init](https://help.aliyun.com/zh/ecs/user-guide/install-cloud-init)。

### 支持STS的云服务

详情参见[支持STS的云服务](https://help.aliyun.com/zh/ram/services-that-work-with-sts)。

### 通过ECS实例角色获取的临时凭证有效期

通过ECS实例角色获取的临时凭证STS Token的有效期固定为6小时，并且不支持修改。同时该有效期不受实例角色的最大会话时间限制，比如您的实例角色最大会话时间设置的是1小时，但是通过ECS实例角色获取的STS Token有效期依然是6小时。

## 自动化模板

### 模板介绍

若您的应用程序在获取到ECS实例角色的临时凭据以后，还需要跨账号角色扮演到其他账号，使用其他角色身份调用OpenAPI，同时您希望跨账号批量完成被扮演的角色的创建。本方案提供基于Terraform的自动化模板，为资源目录下的目标账号批量创建 RAM 角色。

### 模板地址

模板详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-ecs-sts-token)。

## 实施步骤

### 实施准备

如您需要审计ECS实例是否绑定实例角色，请确保已在「企业管理主账号」中开通配置审计。具体操作，请参考[开通配置审计服务](https://help.aliyun.com/zh/document_detail/2399579.html)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 持续合规审计（可选）

您可以通过配置审计，审计ECS实例是否绑定实例角色，保证临时凭据的使用落实。

##### 创建账号组（可选）

如果您当前为多账号环境，希望对多个成员账号进行集中的合规管理，可以使用企业管理账号将资源目录中的所有或部分成员账号加入到同一个账号组中，账号组将作为一个跨账号合规管理的管理单元。如果您是单账号环境，可跳过本步骤。

1. 登入企业管理主账号，进入[资源管理控制台](https://resourcemanager.console.aliyun.com/)，在左侧导航栏选择 **资源目录**> **可信服务**。选择配置审计，单击**管理**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969537.png)
2. 在**委派管理员账号**中，单击**添加**，将日志账号委派为配置审计服务的管理员。
3. 登入日志账号，进入[配置审计控制台](https://config.console.aliyun.com/)，在左侧导航栏选择**账号组**。单击**创建账号组**，通过账号组，对资源目录中的成员账号进行集中合规管理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969538.png)
4. 创建账号组时，账号组类型，可以选择**全局**。全局账号组包含的成员将自动与资源目录保持一致。全局账号组会自动感知资源目录中成员的新增，并自动同步加入到该全局账号组中，确保合规管理的账号范围始终与资源目录保持一致。需要注意的是，您只能新建一个全局账号组。填入**名称**和**描述**后单击**提交**完成账号组的创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969539.png)

##### 创建规则

1. 进入[配置审计控制台](https://config.console.aliyun.com/)。若您使用上述步骤中的账号组进行多账号合规管控，需要在左侧导航栏中切换到需要合规管控的账号组中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969571.png)
2. 在左侧导航栏选择**合规审计** > **规则**，单击**新建规则**。选择名为**ECS实例被授予实例RAM角色**的规则。单击**下一步**。
3. 在**设置基本属性**中，设置**风险等级**、**触发机制**，**触发频率**等。然后单击**下一步**。
4. 默认选中**云服务器 ECS**作为规则关联的资源类型。您可以进一步设置规则生效的范围，比如，配置该规则只对某些资源组内的资源或者具有某些标签的资源生效。以此来对合规管控的资源范围进行更加精细化的管理。然后单击**下一步**。
5. 单击**提交**进行创建，创建完成后，在规则详情页，您可以看到当前账号组下，所有不合规的资源，即未被授予实例RAM角色的所有ECS主机实例。该规则默认会每 24 个小时执行一次检测，您可以在创建规则或者修改规则时，配置该规则的触发频率。
6. 最后，您还可以将不合规资源数据投递到其他云产品中，比如日志服务、对象存储等。方便您进一步对数据进行归档、处理、审计等操作。更多投递相关的信息，请参考[配置审计投递](https://help.aliyun.com/zh/document_detail/310163.html)。

#### 创建RAM角色（可选）

您需要创建一个RAM角色，用于后续步骤中为ECS实例绑定RAM角色，如已创建，可跳过本步骤。

1. 使用ECS实例所属账号登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 在左侧导航栏，选择**身份管理 > 角色**。
3. 在**角色**页面，单击**创建角色**。
4. 在**创建角色**页面，选择可信实体类型为**阿里云服务**，然后单击**下一步**。
5. 选择角色类型为**普通服务角色**。输入**角色名称**和**备注**。选择可信服务为**云服务器**。单击**完成**。

成功创建RAM角色后，该RAM角色没有任何权限，您需要为该RAM角色授权，使其拥有相关的资源访问或操作权限。具体操作，请参见[为RAM角色授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-a-ram-role)。

#### 为增量ECS实例绑定RAM角色

接下来介绍在创建ECS实例时，如何为ECS实例绑定RAM角色。有多种方式可以完成ECS的创建，例如：控制台创建、使用实例启动模板、弹性伸缩创建。为增量ECS实例绑定RAM角色需确保已存在待绑定的RAM角色，如需新建RAM角色，请参考[创建RAM角色（可选）](#Yqv7q)章节。

##### 控制台创建

1. 前往[实例创建页](https://ecs-buy.aliyun.com/wizard/#/)。
2. 选择**自定义购买**页签。
3. 按需选择付费类型、地域、实例规格、镜像等配置。各配置项详细说明，请参考[配置项说明](https://help.aliyun.com/zh/ecs/user-guide/create-an-instance-by-using-the-wizard)。
4. 展开**高级选型（选填）**表单，在**实例RAM角色**中，选择要绑定的RAM角色。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969540.png)
5. 在最终创建实例前，请在页面右侧检查实例的整体配置并配置使用时长等选项，确保各项配置符合您的要求。
6. 阅读并签署**《云服务器ECS服务条款》**等服务协议（若已签署，则无需重复签署，请以页面提示为准），然后单击**确认下单**。

创建实例一般需要3~5分钟，请您耐心等待。您可前往控制台的实例列表页面查看实例的状态，当实例状态变为**运行中**时，表示实例创建完成。

##### 实例启动模板创建

###### 创建实例启动模板

您可以提前创建启动模板（如已有启动模板可跳过本步骤），便于后续使用模板快速创建ECS实例、弹性伸缩组或者弹性供应组。通过在模板中指定授予的RAM角色，确保通过该模板创建出来的实例都关联了指定的RAM角色。

1. 登录[ECS管理控制台](https://ecs.console.aliyun.com/)。
2. 在左侧导航栏，选择**部署与弹性 >**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969578.png)**> 实例启动模板**。
3. 在页面顶部，选择目标资源所在的资源组和地域。
4. 单击**创建模板**。
5. 完成基础配置和高级配置，详细的参数配置及说明信息，请参见[自定义购买实例](https://help.aliyun.com/zh/ecs/user-guide/create-an-instance-by-using-the-wizard)。
6. 在**高级配置**页面，找到**高级选项**。在此处配置实例RAM角色。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969541.png)
7. 在**配置确认**页面，输入模板名称和模板版本描述，并单击**创建启动模板**。

###### 修改已有的实例启动模板

如果您已经创建了实例启动模板，并且想要变更已有的模板，例如在模板中配置实例RAM角色。您可以通过创建启动模板的新版本来更改配置参数。在通过实例启动模板创建ECS实例时，您可以使用任何版本的实例启动模板。需要注意的是，如果您未指定某一版本，则会使用默认版本。

1. 登录[ECS管理控制台](https://ecs.console.aliyun.com/)。
2. 在左侧导航栏，选择**部署与弹性 >**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969579.png)**> 实例启动模板**。
3. 在页面顶部，选择目标资源所在的资源组和地域。
4. 在目标模板的**操作**列中，单击**新建版本**。您也可以选中一个模板，在**版本信息**中单击**新建版本**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969580.png)
5. 在**启动模板**页面，自定义配置参数。您可以在**模板克隆**区域选择已有的模板和版本，在此基础上配置参数。详细的参数配置及说明信息，请参见[自定义购买实例](https://help.aliyun.com/zh/ecs/user-guide/create-an-instance-by-using-the-wizard)。
6. 在**高级配置**页面，找到**高级选项**。在此处配置实例RAM角色。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969581.png)
7. 在**配置确认**页面选中**创建新版本**，并选择要保存到哪一个模板。
8. 单击**创建启动模板**。在弹出的对话框中，单击**查看新版本**前往控制台查看已创建的新版本。
9. 如需将其设置为默认版本，在**启动模板**页面，选中一个模板，在**版本信息**的操作列中单击**设为默认**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969583.png)

###### 使用实例启动模板创建实例

您可以使用指定的模板的任意一个版本快速创建ECS实例，提升效率及使用体验。在模板中配置好RAM角色后，通过该模板创建出来的实例都会关联上指定的RAM角色。

1. 登录[ECS管理控制台](https://ecs.console.aliyun.com/)。
2. 在左侧导航栏，选择**部署与弹性 >**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969549.png)**> 实例启动模板**。
3. 在**启动模板**页面，找到目标模板，**在操作**列中单击**创建实例**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969555.png)
4. 在**自定义购买**页面，选择模板和版本，待配置信息加载完成，检查所有配置信息。
5. 创建实例。如果您选择的是包年包月实例，则选择购买时长并勾选服务协议，单击**确认下单**。如果您选择的是按量付费实例，则勾选服务协议，单击**确认下单**。

实例创建成功后，您可以前往ECS控制台**实例**页面查看新创建的实例。单击目标ECS实例ID，在实例详情页面下方**其他信息**中，查看实例绑定的RAM角色。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969585.png)

##### 弹性伸缩创建

如果您使用弹性伸缩（Elastic Scaling Service，简称ESS）来根据设定的策略自动调整计算资源数量（即业务所需的实例数量），需要确保使用的伸缩配置正确配置了实例RAM角色，否则由弹性伸缩新创建出来的实例没有绑定RAM角色，导致业务故障。

1. 登录[弹性伸缩控制台](https://essnew.console.aliyun.com/)。
2. 在左侧导航栏中，单击**伸缩组管理**。
3. 在顶部菜单栏处，选择地域。
4. 找到待操作的伸缩组，在**操作**列，单击**查看详情**。
5. 在页面上方，单击**实例配置来源**页签。

实例配置来源是伸缩组扩容ECS实例时使用的实例配置模板。自动扩容时，伸缩组根据实例配置来源创建ECS实例，并将创建的实例添加到伸缩组。实例配置来源包括**实例启动模板**和**伸缩配置**两种。伸缩组内只能有一项生效的实例配置来源。例如，选用一条新的伸缩配置后，当前生效的启动模板或伸缩配置会失效。

如果您希望通过**实例启动模板**来伸缩扩容ECS实例：

1. 在**启动模板**页签下，查看当前伸缩组所应用的启动模板，检查该启动模板对应的版本是否正确配置了实例RAM角色，若未配置RAM实例角色，参考[实例启动模板创建](#Fk3Sp)章节完成配置。然后，点击**操作**列的**修改**按钮，选择对应的启动模板和版本。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7966581571/p969559.png)

如果您希望通过**伸缩配置**来伸缩扩容ECS实例：

若还没有伸缩配置：

1. 在**伸缩配置**页签下，单击**创建伸缩配置**。
2. 完成相关参数配置。（在**高级设置**中，配置实例RAM角色）![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969587.png)
3. 单击**创建**，确认参数配置无误，然后单击**确认创建**。
4. 单击**启用配置**。

若已有伸缩配置：

1. 在**伸缩配置**页签下，找到对应的伸缩配置，在**操作**列，单击**修改**。
2. 完成相关参数配置。（在**高级设置**中，配置实例RAM角色）
3. 单击**修改**，确认参数配置无误，然后单击**确认修改**。
4. 对应的伸缩配置**状态**列变为**生效**后表示配置成功，弹性伸缩会使用该伸缩配置创建ECS实例。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969560.png)

#### 为存量ECS实例绑定RAM角色

接下来介绍如何为已有的ECS实例绑定RAM角色，您有多种方式可以完成角色的绑定，例如：在控制台手动配置、通过API批量绑定、通过OSS批量绑定。为存量ECS实例绑定RAM角色需确保已存在待绑定的RAM角色，如需新建RAM角色，请参考[创建RAM角色（可选）](#Yqv7q)章节。

##### 通过控制台绑定

1. 登录[ECS管理控制台](https://ecs.console.aliyun.com/)。
2. 在左侧导航栏，选择**实例与镜像 > 实例**。
3. 在页面顶部，选择目标资源所在的资源组和地域。
4. 找到要操作的ECS实例，在操作列单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969563.png)后，单击**实例设置 > 授予/收回RAM角色**。
5. 在对话框中，选择创建好的实例RAM角色，单击**确定**完成授予。

##### 通过API批量绑定

1. 通过 [AttachInstanceRamRole](https://next.api.aliyun.com/document/Ecs/2014-05-26/AttachInstanceRamRole) API为ECS实例批量绑定RAM角色。
2. 通过 [DescribeInstanceRamRole](https://next.api.aliyun.com/document/Ecs/2014-05-26/DescribeInstanceRamRole) API查询ECS实例上的RAM角色。
3. 通过 [DetachInstanceRamRole](https://next.api.aliyun.com/document/Ecs/2014-05-26/DetachInstanceRamRole) API回收ECS实例上的RAM角色。

接下来以Java为例，演示如何调用API为存量ECS实例绑定实例RAM角色，首先需要集成SDK：

```
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>ecs20140526</artifactId>
  <version>5.1.8</version>
</dependency>
```

下述代码演示了调用AttachInstanceRamRole API，为已有的ECS实例（i-bp139vch042zn1c5tq9b）绑定实例RAM角色（my-ecs-role）：

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用AK&SK初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.ecs20140526.Client createClient() throws Exception {
        // 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
        // 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html。
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config()
        // 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。
        .setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"))
        // 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        .setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
        // Endpoint 请参考 https://api.aliyun.com/product/Ecs
        config.endpoint = "ecs-cn-hangzhou.aliyuncs.com";
        return new com.aliyun.ecs20140526.Client(config);
    }

    public static void main() throws Exception {
        com.aliyun.ecs20140526.Client client = Sample.createClient();
        // 为杭州地域的i-bp139vch042zn1c5tq9b实例绑定my-ecs-role角色
        com.aliyun.ecs20140526.models.AttachInstanceRamRoleRequest attachInstanceRamRoleRequest = new com.aliyun.ecs20140526.models.AttachInstanceRamRoleRequest()
        .setRegionId("cn-hangzhou")
        .setRamRoleName("my-ecs-role")
        .setInstanceIds("[\"i-bp139vch042zn1c5tq9b\"]");
        com.aliyun.teautil.models.RuntimeOptions runtime = new com.aliyun.teautil.models.RuntimeOptions();
        try {
            // 复制代码运行请自行打印 API 的返回值
            client.attachInstanceRamRoleWithOptions(attachInstanceRamRoleRequest, runtime);
        } catch (TeaException error) {
            // 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            // 错误 message
            System.out.println(error.getMessage());
            // 诊断地址
            System.out.println(error.getData().get("Recommend"));
            com.aliyun.teautil.Common.assertAsString(error.message);
        } catch (Exception _error) {
            TeaException error = new TeaException(_error.getMessage(), _error);
            // 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            // 错误 message
            System.out.println(error.getMessage());
            // 诊断地址
            System.out.println(error.getData().get("Recommend"));
            com.aliyun.teautil.Common.assertAsString(error.message);
        }        
    }
}
```

##### 通过OOS批量绑定

以下步骤需要在ECS实例所属账号执行。建议您创建一个RAM角色，用于OOS批量授予实例RAM角色时使用该角色身份来运行任务：

1. 进入[RAM控制台](https://ram.console.aliyun.com/)。
2. 在左侧导航栏，选择**身份管理 > 角色**。
3. 在**角色**页面，单击**创建角色**。
4. 在**创建角色**页面，选择可信实体类型为**阿里云服务**，然后单击**下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969568.png)
5. 角色类型选择**普通服务角色**，输入角色名称，例如oss-AttachInstanceRamRole-role，选择授信服务为**系统运维管理，**点击**完成。**

接下来，您需要为该角色分配权限：

1. 进入[RAM控制台](https://ram.console.aliyun.com/)。
2. 选择权限策略菜单，点击**创建权限策略。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969591.png)
3. 通过**脚本编辑**模式，将配置框中的原有脚本替换为如下内容。`{
 "Version": "1",
 "Statement": [
 {
 "Action": [
 "ecs:AttachInstanceRamRole",
 "ecs:DescribeInstances"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "ram:PassRole"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "oos:StartExecution"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`
4. 点击**继续编辑基本信息**，输入自定义权限策略名称。例如BulkyAttachInstanceRamRolePolicy。点击**确定**完成创建。
5. 创建完成后，在角色页面，找到上述步骤创建的角色，点击**新建授权**按钮。
6. **授权范围**选择**整个云账号**。权限在当前阿里云账号内生效。**授权主体**选择您在上述步骤中创建的角色。**自定义策略**选择BulkyAttachInstanceRamRolePolicy，即您在上述步骤中创建的策略。
7. 点击**确定**完成创建。

接下来通过OOS为存量ECS实例绑定RAM角色：

1. 使用ECS实例所属账号进入[系统运维管理控制台](https://oos.console.aliyun.com/)。
2. 在**自动化任务 >** **任务执行管理**页面点击**创建**。
3. 在**创建任务**页面，设置**基本信息**。本示例中参数说明如下：参数描述模板类别选择**公共任务模板**模板选择选择**ACS-ECS-BulkyAttachInstanceRamRole**执行模式选择**失败暂停**，当子任务执行有失败时，执行会暂停，等待您调整并决定是否继续执行。如果需要分批执行，每批暂停，此处也需选择**失败暂停**。
4. 单击**下一步：设置参数**。设置为完成后单击**下一步：确定**。本示例中参数说明如下：参数描述Ram角色名称填写待授予ECS的RAM实例角色名地域ID选择ECS实例所在的地域目标实例选择授予RAM实例角色的ECS实例任务执行的并发比率根据需要选择并发控制或批次控制，本例中选择批次控制：批次速率数组：[1, 5%, 10%]循环并发控制：每批暂停最大错误次数：0OOS扮演的RAM角色选择指定RAM角色，使用改角色的权限：选择上述步骤中创建的RAM角色，本例中为oss-AttachInstanceRamRole-role![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969592.png)
5. 参数确认完毕后点击**创建**。
6. 若在上述步骤中选择每批暂停，待执行状态变为**等待中**后，确认无误，单击**继续**按钮。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969569.png)
7. 待执行状态变为**成功**后，表明已完成批量授予实例RAM角色任务。

#### 基于实例RAM角色获取并使用临时凭证

当您通过阿里云SDK调用OpenAPI进行资源操作时，必须正确配置凭证信息。强烈推荐您使用阿里云的Credentials工具，帮助您轻松地获取和管理访问凭证：

- 基于实例RAM角色获取临时凭证时，Credentials工具会自动调用ECS的元数据服务（Meta Data Server）获取临时访问凭证。
- Credentials工具会自动维护临时凭证的生命周期，研发人员无需关心临时凭证的到期更新，Credentials工具会自动保证凭证的周期性更新。
- 借助Credentials工具的默认凭据链，可以用同一套代码，通过程序之外的配置来控制不同环境下的凭据获取方式

##### 阿里云V2.0 SDK

如果您使用V2.0版本的阿里云SDK，可以很方便的集成阿里云的Credentials工具。

以Java为例，通过Maven方式安装Credentials工具：

```
<!--建议使用最新发布的Credentials版本。-->
<!--获取所有已发布的版本列表，请参见https://github.com/aliyun/credentials-java/blob/master/ChangeLog.txt-->
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>credentials-java</artifactId>
  <version>LATEST</version>
</dependency>
```

Credentials工具支持多种方式初始化凭据客户端，您可根据实际情况选择合适的方式进行凭据客户端初始化。下面介绍显式配置ECS角色（推荐）和默认凭据链的方式，更多方式，请参考[初始化凭据客户端](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials)。

###### 显式配置实例角色（推荐）

推荐您使用该方式，在代码中明确指定实例角色，避免运行环境中的环境变量、配置文件等带来非预期的结果。该方式显式设置类型为`ecs_ram_role`，Credentials工具会自动获取ECS实例绑定的RAM角色，调用ECS的元数据服务（Meta Data Server）换取STS Token，完成凭据客户端初始化。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-ecs-sts-token/code-example/java/common/src/main/java/org/example/sdk2_0/CredentialsRoleConfigSample.java)。

```
import com.aliyun.credentials.Client;
import com.aliyun.credentials.models.Config;
// import com.alibaba.fastjson2.JSON;
// import com.aliyun.sts20150401.models.GetCallerIdentityResponse;

public class DemoTest {
    public static void main(String[] args) {
        Config credentialConfig = new Config();
        credentialConfig.setType("ecs_ram_role");
        // 选填，该ECS角色的角色名称，不填会自动获取，建议加上以减少请求次数
        credentialConfig.setRoleName("RoleName");
        // 在加固模式下获取STS Token，强烈建议开启
        credentialConfig.setEnableIMDSv2(true);
        Client credentialClient = new Client(credentialConfig);

        // 调用API，以调用GetCallerIdentity获取当前调用者身份信息为例
        // com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config()
        //     .setCredential(credentialsClient)
        //     .setEndpoint("sts.cn-hangzhou.aliyuncs.com");
        // com.aliyun.sts20150401.Client stsClient = new com.aliyun.sts20150401.Client(config);

        // GetCallerIdentityResponse getCallerIdentityResponse = stsClient.getCallerIdentity();
        // System.out.println(JSON.toJSONString(getCallerIdentityResponse));
    }
}
```

上述代码在通过ECS实例RAM角色初始化客户端时，设置`enable_imds_v2`的值为true，表示使用数据加固模式。相较于普通模式，此方式采纳了一种更为严谨的安全逻辑：首先在ECS实例内部自动生成一个具有时效限制的token，利用此token作为凭据，向元数据服务（Metadata Server）请求获得STS（Security Token Service）临时凭证。这一系列操作构成了凭据客户端的安全初始化流程。加固模式的核心优势在于，ECS实例内部产生的token不仅具备动态性，还严格限制了有效时间，大大降低了外部攻击者通过预测或伪造token来非法访问元数据服务的可能性，从而有效抵御了服务器端请求伪造（SSRF, Server-Side Request Forgery）等多种网络安全隐患。

默认情况下，实例元数据服务器可同时通过普通模式和加固模式访问。为了进一步增强安全性，您可以设置实例元数据服务器访问模式为**仅加固模式**。

对于**新创建实例**，可以通过API设置。通过API接口[RunInstances](https://next.api.aliyun.com/api/Ecs/2014-05-26/RunInstances)或[CreateInstance](https://help.aliyun.com/zh/ecs/developer-reference/api-ecs-2014-05-26-createinstance)创建实例时，通过HttpTokens参数设置实例元数据服务器访问模式。该参数取值范围：

- `optional`：默认不强制使用加固模式，支持通过普通模式或加固模式访问实例元数据。
- `required`：强制使用加固模式，即仅加固模式。设置该取值后，无法通过普通模式访问实例元数据。

对于**已有实例**，可以通过控制台手动修改或API方式修改。

控制台方式：

1. 在实例列表页，找到待操作的实例，在**操作**列，选择![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969572.png)**> 实例设置 > 修改实例元数据访问信息**。
2. 开启**是否启用实例元数据访问通道**，并设置**实例元数据访问模式**。

- 普通：支持通过普通模式或加固模式查看实例元数据。
- 仅加固模式（推荐）：仅支持通过加固模式查看实例元数据，普通模式无法访问实例元数据。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969593.png)

API方式：通过[ModifyInstanceMetadataOptions](https://next.api.aliyun.com/api/Ecs/2014-05-26/ModifyInstanceMetadataOptions) 修改元数据信息时，通过`HttpTokens`参数设置实例元数据访问模式。该参数取值范围：

- `optional`：默认不强制使用加固模式，支持通过普通模式或加固模式访问实例元数据。
- `required`：强制使用加固模式，即仅加固模式。设置该取值后，普通模式无法访问实例元数据。

###### 默认凭据链

当您在初始化凭据客户端不传入任何参数时，Credentials工具会使用默认凭据链方式初始化客户端。借助Credentials工具的默认凭据链，您可以用同一套代码，通过程序之外的配置来控制不同环境下的凭据获取方式。除非您清楚的知道默认凭据链中凭据信息查询优先级以及您的程序运行的各个环境中凭据信息配置方式，否则不建议您使用默认凭据链，推荐您使用显式配置实例角色方式，避免运行环境中的环境变量、配置文件等带来非预期的结果。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-ecs-sts-token/code-example/java/common/src/main/java/org/example/sdk2_0/CredentialsDefaultSample.java)。

```
import com.aliyun.credentials.Client;
// import com.alibaba.fastjson2.JSON;
// import com.aliyun.sts20150401.models.GetCallerIdentityResponse;

public class DemoTest {
    public static void main(String[] args) throws Exception{
        // 不指定参数
        Client credentialClient = new Client();

        // 调用API，以调用GetCallerIdentity获取当前调用者身份信息为例
        // com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config()
        //     .setCredential(credentialsClient)
        //     .setEndpoint("sts.cn-hangzhou.aliyuncs.com");
        // com.aliyun.sts20150401.Client stsClient = new com.aliyun.sts20150401.Client(config);

        // GetCallerIdentityResponse getCallerIdentityResponse = stsClient.getCallerIdentity();
        // System.out.println(JSON.toJSONString(getCallerIdentityResponse));
    }
}
```

当使用默认凭据链方式初始化客户端时，以Java SDK为例，会尝试按照如下顺序查找相关凭据信息（优先级由高到低）。

1. 系统属性
2. 环境变量
3. OIDC RAM角色
4. 配置文件
5. ECS实例RAM角色

详细信息请参考[Java SDK默认凭据链](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials)。

其中，对于**ECS实例RAM角色**，Credentials工具会在环境变量中获取**ALIBABA_CLOUD_ECS_METADATA**（ECS实例RAM角色名称），若存在，程序将会通过ECS的元数据服务（Meta Data Server）获取ECS实例RAM角色的STS Token作为默认凭据信息。强烈建议配置环境变量`ALIBABA_CLOUD_ECS_IMDSV2_ENABLE=true`开启在[加固模式](https://help.aliyun.com/zh/ecs/user-guide/view-instance-metadata/)下获取STS Token。

需要注意的是：

- 使用默认凭据链的方式，Credentials工具会按照优先级依次查找相关凭据的信息，请避免环境变量维护不当导致获取到了非预期的凭据。
- 如果您在运行在ECS中的Docker环境中使用Credentials工具请确保Docker中可以正常访问到ECS Meta Service，您可以在Docker环境中，执行命令：`url http://100.100.100.200/latest/meta-data/ram/security-credentials/${实例角色名称}`，如果正确返回临时凭证，那么您的Docker环境可以正常访问ECS Meta Service。如果您使用的是Credentials工具的默认凭据链，请确保您在Docker环境中已经配置了上述所需的环境变量，而不是将环境变量配置到ECS实例上。

如果您需要从长期固定AccessKey的使用方式进行迁移，只需修改少量代码即可完成，如下图所示，左侧一栏是使用固定AccessKey初始化阿里云SDK，右侧一栏是使用Credentials工具初始化阿里云SDK。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969594.png)

##### 阿里云V1.0 SDK（不推荐）

阿里云V1.0 SDK是较早使用版本，稳定性良好，不少老用户习惯于原版SDK的开发，本章节则是给这部分用户提供一个简练的使用指南。对于新用户则建议直接使用新版SDK，老用户也建议尽早迁移到新版SDK。

接下来介绍SDK客户端的初始化方式，可以通过Credentials工具初始化（推荐）、通过环境变量初始化、通过实例角色初始化。

###### 通过Credentials工具初始化

使用阿里云V1.0 SDK也可以集成阿里云的Credentials工具，优先推荐使用该方式，以Java为例，通过Maven方式安装Credentials工具：

```
<!--建议使用最新发布的Credentials版本。-->
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

下述代码演示了先初始化凭据客户端，再使用凭据客户端的凭据信息初始化V1.0 SDK客户端。关于凭据客户端的初始化方式，可以参考[阿里云V2.0 SDK](#pAEew)章节中介绍的两种方式，更多方式，请参考[初始化凭据客户端](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials)。使用该方式可以通过ECS实例元数据加固模式获取RAM角色的凭证。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-ecs-sts-token/code-example/java/common/src/main/java/org/example/sdk1_0/CredentialsSample.java)。

```
import com.aliyun.credentials.Client;
import com.aliyun.credentials.models.CredentialModel;
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.auth.BasicSessionCredentials;
import com.aliyuncs.profile.DefaultProfile;
// import com.alibaba.fastjson2.JSON;
// import com.aliyuncs.sts.model.v20150401.GetCallerIdentityRequest;
// import com.aliyuncs.sts.model.v20150401.GetCallerIdentityResponse;

public class DemoTest {

    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou");
        // 初始化凭据客户端
        Client credentialClient = new Client();
        // 用凭据客户端初始化SDK1.0客户端
        IAcsClient client = createAcsClientByCredentials(profile, credentialClient);

        // 调用API，以调用GetCallerIdentity获取当前调用者身份信息为例
        // GetCallerIdentityRequest getCallerIdentityRequest = new GetCallerIdentityRequest();
        // GetCallerIdentityResponse getCallerIdentityResponse = client.getAcsResponse(getCallerIdentityRequest);
        // System.out.println(JSON.toJSONString(getCallerIdentityResponse));
    }

    public static IAcsClient createAcsClientByCredentials(DefaultProfile profile, Client credentialClient) {
        return new DefaultAcsClient(profile, () -> {
            // 保证线程安全，从 CredentialModel 中获取 ak/sk/security token
            CredentialModel credentialModel = credentialClient.getCredential();
            String ak = credentialModel.getAccessKeyId();
            String sk = credentialModel.getAccessKeySecret();
            String token = credentialModel.getSecurityToken();
            return new BasicSessionCredentials(ak, sk, token);
        });
    }
}
```

值得注意的是，在使用凭据客户端初始化V1.0 SDK客户端过程中，为保证线程安全，需要先获取`CredentialModel`，再从`CredentialModel`获取凭据信息。不能直接从凭据客户端`credentialClient`中获取凭据信息，因为Credentials工具会自动获取并更新凭据，会导致`CredentialModel`对象发生变化，若直接从凭据客户端获取，可能获取到的AccessKeyId/AccessKeySecret/SecurityToken不属于同一套凭据，从而产生错误。

###### 通过环境变量初始化

使用环境变量的方式，如果定义了环境变量**ALIBABA_CLOUD_ECS_METADATA**且不为空，程序会将该环境变量的值作为角色名称，通过ECS的元数据服务（Meta Data Server）获取ECS实例RAM角色的STS Token作为默认凭据信息。注意，该方式默认通过普通模式访问实例元数据服务器，不支持加固模式。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-ecs-sts-token/code-example/java/common/src/main/java/org/example/sdk1_0/EnvConfigSample.java)。

```
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
// import com.alibaba.fastjson2.JSON;
// import com.aliyuncs.sts.model.v20150401.GetCallerIdentityRequest;
// import com.aliyuncs.sts.model.v20150401.GetCallerIdentityResponse

public class Main {
    public static void main(String[] args) {
        IAcsClient client = new DefaultAcsClient("<YOUR-REGION-ID>");

        // 调用API，以调用GetCallerIdentity获取当前调用者身份信息为例
        // GetCallerIdentityRequest getCallerIdentityRequest = new GetCallerIdentityRequest();
        // GetCallerIdentityResponse getCallerIdentityResponse = client.getAcsResponse(getCallerIdentityRequest);
        // System.out.println(JSON.toJSONString(getCallerIdentityResponse));
    }
}
```

###### 通过实例角色初始化

V1.0 SDK客户端支持通过实例角色初始化，通过`InstanceProfileCredentialsProvider`来初始化客户端。注意，该方式默认通过普通模式访问实例元数据服务器，不支持加固模式。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-ecs-sts-token/code-example/java/common/src/main/java/org/example/sdk1_0/RoleConfigSample.java)。

```
import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.auth.InstanceProfileCredentialsProvider;
import com.aliyuncs.profile.DefaultProfile;
// import com.alibaba.fastjson2.JSON;
// import com.aliyuncs.sts.model.v20150401.GetCallerIdentityRequest;
// import com.aliyuncs.sts.model.v20150401.GetCallerIdentityResponse;

public class DemoTest {
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("<YOUR-REGION-ID>");
        InstanceProfileCredentialsProvider provider = new InstanceProfileCredentialsProvider(
            "<YOUR-ROLE-NAME>"
        );
        DefaultAcsClient client = new DefaultAcsClient(profile, provider);

        // 调用API，以调用GetCallerIdentity获取当前调用者身份信息为例
        // GetCallerIdentityRequest getCallerIdentityRequest = new GetCallerIdentityRequest();
        // GetCallerIdentityResponse getCallerIdentityResponse = client.getAcsResponse(getCallerIdentityRequest);
        // System.out.println(JSON.toJSONString(getCallerIdentityResponse));
    }
}
```

##### OSS SDK

如果您需要在阿里云的云服务器ECS中访问您的OSS，您可以通过ECS实例RAM角色的方式访问OSS。在集成OSS SDK后，您需要初始化OSS客户端。接下来介绍通过Credentials工具初始化的方式。

###### 通过Credentials工具初始化

使用该方式需要集成阿里云的Credentials工具，优先推荐使用该方式，目前支持该方式的 OSS SDK有

| OSS SDK 语言 | 推荐版本 |
| --- | --- |
| Java | >= 3.11.3 |
| Python | >= 2.14.0 |
| PHP | >= 2.6.0 |
| Golang | >= 3.0.2 |

通过Maven方式安装Credentals工具（确保 Credentals SDK version >= 0.3.2）：

```
<!--建议使用最新发布的Credentials版本。-->
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

下述代码演示了先初始化凭据客户端，再使用凭据客户端的凭据信息初始化OSS客户端。关于凭据客户端的初始化方式，可以参考[阿里云V2.0 SDK](#pAEew)章节中介绍的两种方式，更多方式，请参考[初始化凭据客户端](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials)。使用该方式可以通过ECS实例元数据加固模式获取RAM角色的凭证。

```
import com.aliyun.credentials.Client;
import com.aliyun.credentials.models.CredentialModel;
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.Credentials;
import com.aliyun.oss.common.auth.CredentialsProvider;
import com.aliyun.oss.common.auth.DefaultCredentials;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.Bucket;

public class CredentialsDefaultSample {
    public static void main(String[] args) {
        // 初始化凭据客户端
        Client credentialClient = new Client();

        // Bucket所在地域对应的Endpoint。以华东1（杭州）为例。
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Endpoint对应的Region信息，例如cn-hangzhou。
        String region = "cn-hangzhou";
        // 建议使用更安全的V4签名算法，则初始化时需要加入endpoint对应的region信息，同时声明SignVersion.V4
        // OSS Java SDK 3.17.4及以上版本支持V4签名。
        ClientBuilderConfiguration configuration = new ClientBuilderConfiguration();
        configuration.setSignatureVersion(SignVersion.V4);

        // 用凭据客户端初始化OSS客户端
        OSS ossClient = OSSClientBuilder.create()
            .endpoint(endpoint)
            .credentialsProvider(new CredentialsProvider() {
                @Override
                public void setCredentials(Credentials credentials) {
                }

                @Override
                public Credentials getCredentials() {
                    // 保证线程安全，从 CredentialModel 中获取 ak/sk/security token
                    CredentialModel credentialModel = credentialClient.getCredential();
                    String ak = credentialModel.getAccessKeyId();
                    String sk = credentialModel.getAccessKeySecret();
                    String token = credentialModel.getSecurityToken();
                    return new DefaultCredentials(ak, sk, token);
                }
            })
            .clientConfiguration(configuration)
            .region(region)
            .build();

        // 调用OSS API
        // ossClient.listBuckets();

        // 关闭OSSClient。
        ossClient.shutdown();
    }
}
```

值得注意的是，在使用凭据客户端初始化OSS客户端过程中，为保证线程安全，需要先获取`CredentialModel`，再从`CredentialModel`获取凭据信息。不能直接从凭据客户端`credentialClient`中获取凭据信息，因为Credentials工具会自动获取并更新凭据，会导致`CredentialModel`对象发生变化，若直接从凭据客户端获取，可能获取到的AccessKeyId/AccessKeySecret/SecurityToken不属于同一套凭据，从而产生错误。

##### SLS SDK

如果您需要在阿里云的云服务器ECS中访问您的SLS，您可以通过ECS实例RAM角色的方式访问SLS。在集成SLS SDK后，您需要初始化SLS客户端。接下来介绍通过Credentials工具初始化的方式。

###### 通过Credentials工具初始化

使用该方式需要集成阿里云的Credentials工具，优先推荐使用该方式，目前支持的SDK有

| SLS SDK 语言 | 推荐版本 |
| --- | --- |
| Java | >= 0.6.88 |
| Python | >= 0.9.3 |
| PHP | >= 0.6.4 |
| Golang | >= 0.1.55 |

以Java为例，通过Maven方式安装Credentials工具：

```
<!--建议使用最新发布的Credentials版本。-->
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

下述代码演示了先初始化凭据客户端，再使用凭据客户端的凭据信息初始化SLS客户端。关于凭据客户端的初始化方式，可以参考[阿里云V2.0 SDK](#pAEew)章节中介绍的两种方式，更多方式，请参考[初始化凭据客户端](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials)。使用该方式可以通过ECS实例元数据加固模式获取RAM角色的凭证。

```
import com.aliyun.credentials.models.CredentialModel;
import com.aliyun.openservices.log.Client;
import com.aliyun.openservices.log.common.auth.DefaultCredentials;

public class DemoTest {
    public static void main(String[] args) {

        // 日志服务的服务接入点。以杭州为例，
        String endpoint = "cn-hangzhou.log.aliyuncs.com";

        // 初始化凭据客户端
        com.aliyun.credentials.Client credentialClient = new com.aliyun.credentials.Client();

        // 用凭据客户端初始化SLS客户端
        Client slsClient = createSlsClientByCredentials(endpoint, credentialClient);

        // 调用SLS API
        // slsClient.ListProject();

        //关闭SLS客户端
        slsClient.shutdown();
    }

    public static Client createSlsClientByCredentials(String endpoint, com.aliyun.credentials.Client credentialClient) {
        return new Client(endpoint, () -> {
            // 保证线程安全，从 CredentialModel 中获取 ak/sk/security token
            CredentialModel credentialModel = credentialClient.getCredential();
            String ak = credentialModel.getAccessKeyId();
            String sk = credentialModel.getAccessKeySecret();
            String token = credentialModel.getSecurityToken();
            return new DefaultCredentials(ak, sk, token);
        });
    }
}
```

值得注意的是，在使用凭据客户端初始化SLS客户端过程中，为保证线程安全，需要先获取`CredentialModel`，再从`CredentialModel`获取凭据信息。不能直接从凭据客户端`credentialClient`中获取凭据信息，因为Credentials工具会自动获取并更新凭据，会导致`CredentialModel`对象发生变化，若直接从凭据客户端获取，可能获取到的AccessKeyId/AccessKeySecret/SecurityToken不属于同一套凭据，从而产生错误。

###### 其他SDK

| SDK名称 | SDK说明 | 使用方式 |
| --- | --- | --- |
| JindoSDK | JindoSDK是访问JindoData组件的标准客户端。其中JindoData是阿里云开源大数据团队自研的数据湖存储加速套件，面向大数据和AI生态，为阿里云和业界主要数据湖存储系统提供全方位访问加速解决方案。详细信息请参考[JindoData使用文档](https://aliyun.github.io/alibabacloud-jindodata/)。 | 请参考JindoSDK[免密访问](https://help.aliyun.com/zh/emr/emr-on-ecs/user-guide/deploy-jindosdk-in-an-environment-other-than-emr)。 |

##### 通过元数据服务获取

某些场景，如果您没有适配Credentials工具，或需要在脚本中基于实例RAM角色来获取资源临时访问凭证，可直接在实例内部访问元数据服务器获取。

对于Linux类型实例，登录到实例内部，执行以下命令：

```
# 获取元数据服务器的访问凭证用于鉴权
TOKEN=`curl -X PUT "http://100.100.100.200/latest/api/token" -H "X-aliyun-ecs-metadata-token-ttl-seconds:<元数据服务器访问凭证有效期>"` 
# 获取实例RAM角色的临时授权访问凭证
curl -H "X-aliyun-ecs-metadata-token: $TOKEN" http://100.100.100.200/latest/meta-data/ram/security-credentials/<实例RAM角色名称>
```

对于Windows实例，登录到实例内部，打开Powershell执行以下命令：

```
# 获取元数据服务器的访问凭证用于鉴权，以加强数据安全
$token = Invoke-RestMethod -Headers @{"X-aliyun-ecs-metadata-token-ttl-seconds" = "<元数据服务器的访问凭证有效期>"} -Method PUT –Uri http://100.100.100.200/latest/api/token

# 获取实例RAM角色的临时授权访问凭证
Invoke-RestMethod -Headers @{"X-aliyun-ecs-metadata-token" = $token} -Method GET -Uri http://100.100.100.200/latest/meta-data/ram/security-credentials/<实例RAM角色名称>
```

参数说明如下：

| 参数 | 说明 |
| --- | --- |
| <元数据服务器的访问凭证有效期> | 在获取实例RAM角色的STS Token（临时凭证）之前，需要先获取元数据服务器的访问凭证并设置其有效期，以加强数据安全。有效期取值范围为1~21600，单位为秒。在有效期内可重复使用实例元数据访问命令访问任何元数据信息；超过有效期后，凭证失效需要重新获取，否则无法访问实例元数据。访问凭证仅适用于一台实例，如果将凭证复制到其他实例使用，会被拒绝访问。 |
| <实例RAM角色名称> | 替换为具体的实例RAM角色名称。 |

返回结果如下所示：

```
{
   "AccessKeyId" : "STS.*******6YSE",
   "AccessKeySecret" : "aj******jDU",
   "Expiration" : "2017-11-01T05:20:01Z", 
   "SecurityToken" : "CAISng********",
   "LastUpdated" : "2023-07-18T14:17:28Z",
   "Code" : "Success"
}
```

##### 链式角色扮演

若您在获取到ECS实例角色的临时凭据以后，还需要跨账号角色扮演到其他账号，使用其他角色身份调用OpenAPI。可以以ECS实例RAM角色的身份调用STS服务的[AssumeRole](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)接口，设置Token的最大过期时间，即可换取到临时凭据STS Token，再使用该STS Token初始化凭据客户端。

```
import com.aliyun.credentials.Client;
import com.aliyun.credentials.models.Config;
import com.aliyun.sts20150401.models.AssumeRoleRequest;
import com.aliyun.sts20150401.models.AssumeRoleResponse;
import com.aliyun.sts20150401.models.AssumeRoleResponseBody;
// import com.alibaba.fastjson2.JSON;
// import com.aliyun.sts20150401.models.GetCallerIdentityResponse;

public class DemoTest {
    public static void main(String[] args) throws Exception {

        // 通过ECS实例元数据加固模式获取RAM角色初始化凭据客户端
        Config credentialConfig = new Config();
        credentialConfig.setType("ecs_ram_role");
        credentialConfig.setRoleName("<YOUR-ROLE-NAME>");
        credentialConfig.setEnableIMDSv2(true);
        Client credential = new Client(credentialConfig);

        // 跨账号角色扮演到其他账号初始化凭据客户端
        Client assumeRoleCredential = createAssumeRoleCredential(credential);

        // 调用API，以调用GetCallerIdentity获取当前调用者身份信息为例
        // com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config()
        //     .setCredential(assumeRoleCredential)
        //     .setEndpoint("sts.cn-hangzhou.aliyuncs.com");
        // com.aliyun.sts20150401.Client stsClient = new com.aliyun.sts20150401.Client(config);

        // GetCallerIdentityResponse getCallerIdentityResponse = stsClient.getCallerIdentity();
        // System.out.println(JSON.toJSONString(getCallerIdentityResponse));
    }

    public static Client createAssumeRoleCredential(Client credentialClient) throws Exception {
        om.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config()
            .setCredential(credentialClient)
            // 地域
            .setRegionId("<region-id>");

        com.aliyun.sts20150401.Client stsClient = new com.aliyun.sts20150401.Client(config);
        AssumeRoleRequest assumeRoleRequest = new AssumeRoleRequest()
            // 要扮演的RAM角色ARN，acs:ram::${账号 ID}:role/${角色名称}
            .setRoleArn("<role-arn>")
            // 角色会话名称
            .setRoleSessionName("<role-session-name>")
            // 设置更小的权限策略，非必填。示例值：{"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"}
            .setPolicy("<session-policy>")
            // STS Token 有效期，单位：秒
            .setDurationSeconds(3600L);
        AssumeRoleResponse assumeRoleResponse = stsClient.assumeRole(assumeRoleRequest);
        AssumeRoleResponseBody.AssumeRoleResponseBodyCredentials credentials = assumeRoleResponse.getBody().getCredentials();

        // 使用STS Token初始化凭据客户端
        Config credentialConfig = new Config();
        credentialConfig.setType("sts");
        credentialConfig.setAccessKeyId(credentials.getAccessKeyId());
        credentialConfig.setAccessKeySecret(credentials.getAccessKeySecret());
        credentialConfig.setSecurityToken(credentials.getSecurityToken());
        return new Client(credentialConfig);
    }
}
```

注意：在角色链式扮演的场景下（如上代码所示，通过ECS实例角色的身份又去扮演了其他角色），不能使用`ram_role_arn`的方式来初始化凭据客户端，因为Credentials SDK有自动刷新扮演对象的STS Token的机制，可能在刷新时，当前角色（扮演者）的STS Token过期了，从而导致错误。因此，在角色链式扮演的场景下，建议您每次通过AssumeRole API从当前角色去扮演其他角色获取相应的STS Token，通过上述示例代码中`sts`的方式初始化凭据客户端，同时需要注意STS Token的有效期。如下为错误代码示例，`createAssumeRoleCredential`方法使用了`ram_role_arn`的方式，可能会因为ECS实例角色的STS Token过期而导致错误。

```
// 错误代码示例
public static Client createAssumeRoleCredential(Client credentialClient) throws Exception {
    Config credentialConfig = new Config();
    credentialConfig.setType("ram_role_arn");
    credentialConfig.setAccessKeyId(credentialClient.getAccessKeyId());
    credentialConfig.setAccessKeySecret(credentialClient.getAccessKeySecret());
    credentialConfig.setSecurityToken(credentialClient.getSecurityToken());
    credentialConfig.setRoleArn("<role-arn>");
    credentialConfig.setRoleSessionName("<role-session-name>");
    credentialConfig.setPolicy("<session-policy>");
    credentialConfig.setRoleSessionExpiration(3600);
    return new Client(credentialConfig);
}
```

##### 代码示例

###### 代码介绍

本方案提供Java和Python的代码示例，方便客户能够快速完成应用改造。若您的应用程序在获取到ECS实例角色的临时凭据以后，还需要跨账号角色扮演到其他账号，使用其他角色身份调用OpenAPI，同时您希望跨账号批量完成被扮演的角色的创建。本方案提供Terraform代码，为资源目录下的目标账号批量创建 RAM 角色。

###### 代码地址

代码详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-ecs-sts-token)。

#### 通过ROS跨账号批量创建角色（可选）

若您的应用程序在获取到ECS实例角色的临时凭据以后，还需要跨账号角色扮演到其他账号，使用其他角色身份调用OpenAPI，同时您希望跨账号批量完成被扮演的角色的创建。您可以使用ROS模板创建资源栈组。通过该ROS模板和资源栈组为资源目录下的目标账号批量创建 RAM 角色。

##### 创建委派管理员

通过委派管理员账号，可以将组织管理任务与业务管理任务相分离，企业管理账号执行资源目录的组织管理任务，委派管理员账号执行ROS的业务管理任务，这符合安全最佳实践的建议。接下来将资源目录的共享服务账号或运维账号设置为委派管理员账号，从而作为ROS的管理员账号为成员账号部署资源栈。

1. 使用管理账号登录[资源管理控制台](https://resourcemanager.console.aliyun.com/?spm=a2c4g.11186623.0.0.1272250aoGn651)。
2. 在左侧导航栏，选择**资源目录 > 可信服务**。
3. 在**可信服务**页面，单击**资源编排(ROS)**服务**操作**列的**管理**。
4. 在**委派管理员账号**区域，单击**添加**。
5. 在**添加委派管理员账号**面板，选中成员(共享服务账号)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969574.png)
6. 单击**确定**。添加成功后，使用该委派管理员账号访问对应可信服务的多账号管理模块，即可进行资源目录组织范围内的管理操作。

##### 开启可信访问

当您开通了资源目录，使用资源目录的企业管理账号或委派管理员账号创建服务管理权限模式的资源栈组时，必须开启可信访问，授权服务管理权限。需要企业管理账号和委派管理员账号都开启可信访问。

1. 分别使用企业管理账号和共享服务账号（委派管理员）登录[资源编排控制台](http://ros.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源栈组**。
3. 在**资源栈组列表**页面，单击右上角的**开启可信访问**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969575.png)

##### 批量创建所需角色

1. 使用共享服务账号登录[资源编排控制台](https://ros.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源栈组**。
3. 在顶部菜单栏的地域下拉列表，选择资源栈组的所在地域。
4. 在**资源栈组列表**页面，单击**创建资源栈组**。
5. 在**指定模板**选择框中，勾选**选择已有模板**。
6. **模板录入方式**选择**输入模板**，**模板内容**选择**Terraform**。
7. 内容文本框右上角，选择打开本地文件夹。
8. 选择下载到本地的[部署代码](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-ecs-sts-token/deployment/create_role_cross_account)，点击下一步。
9. 输入**资源栈组名称**和**资源栈组描述**，在**配置模板参数**页面，填写所需参数，然后单击下一步。**参数****说明**角色的名称批量创建的角色的名称策略名绑定到该角色的权限策略的名称策略内容绑定到该角色的权限策略内容角色可信的账号允许扮演到该角色的账号，不填默认为当前账号可信账号下允许扮演的角色允许可信账号下扮演到该角色的角色名称
10. 在**配置资源栈组**页面，选择**服务管理权限**，然后单击**下一步**。
11. 在**设置部署选项**页面，**部署目标**选择资源目录的目标账号的资源夹，同时启用**自动部署**。
12. 根据实际情况填写**地域**、**资源组**、**标签**、**部署选项**等信息，更多信息，请参见[参数说明](https://help.aliyun.com/zh/ros/user-guide/step-3-create-a-stack-group)。然后单击**下一步**。
13. 在**检查并确认**页面，检查资源栈组信息无误后，单击**创建资源栈组**。
14. 创建完成后，在该资源栈组的详情页的**实例**页签中，可以查看实例的状态，**最新**表示已经在业务账号下完成了角色的创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969595.png)

#### 实例角色操作审计（可选）

若您需要对ECS实例角色进行操作审计，例如使用该ECS实例角色的身份做了什么操作。您可以使用您的日志审计账号进入[操作审计控制台](https://actiontrail.console.aliyun.com/)，在**事件>事件查询**中找到该实例角色的操作事件，点击查看事件详情，可以通过事件记录中的`requestParameters.stsTokenPrincipalName`来区分该操作来自于哪个ECS实例，该字段是一个固定的格式：${角色名称}/vm-ram-${MetaServer版本}-${实例ID}。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6966581571/p969576.png)

若您的账号开启了审计日志投递，可以在**事件>高级查询**中运行下方所示的查询SQL语句快速查找出实例使用实例角色身份的进行的所有操作：

```
event.requestParameters.stsTokenPrincipalName:${角色名称}/vm-ram-${MetaServer版本}-${实例ID}
```

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7966581571/p969577.png)

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

### 为什么 Credentials SDK 报错：not found credentials？

- 请确保您已经为您的ECS绑定了RAM实例角色，您可以登录到ECS实例上，执行命令：`curl http://100.100.100.200/latest/meta-data/ram/security-credentials/${实例角色名称}`，如果正确返回临时凭证，那么您已成功绑定了RAM实例角色。
- 如果您使用的是JAVA的Credentials SDK，请确保您的SDK版本>=0.3.2。
- 如果您使用的是Credentials工具的默认凭据链，请确保您已经配置了环境变量**ALIBABA_CLOUD_ECS_METADATA**，该环境变量的值配置为RAM实例角色的名称。
- 如果您在运行在ECS中的Docker环境中使用Credentials工具请确保Docker中可以正常访问到ECS Meta Service，您可以在Docker环境中，执行命令：`url http://100.100.100.200/latest/meta-data/ram/security-credentials/${实例角色名称}`，如果正确返回临时凭证，那么您的Docker环境可以正常访问ECS Meta Service。如果您使用的是Credentials工具的默认凭据链，请确保您在Docker环境中已经配置了环境变量**ALIBABA_CLOUD_ECS_METADATA**，该环境变量的值配置为RAM实例角色的名称。需要注意的是，这里不要把环境变量配置到ECS实例上。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-240（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
