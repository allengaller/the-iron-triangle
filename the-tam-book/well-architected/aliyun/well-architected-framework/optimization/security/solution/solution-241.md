<!-- source: https://help.aliyun.com/zh/well-architected/solution-241 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929336 -->

# 通过容器服务RRSA实现临时凭证的获取和使用

本文介绍了一种部署在容器服务上的应用程序获取和使用临时凭证（STS Token）的方案。避免直接把AccessKey固化在程序中，引发泄露风险。

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9966581571/p970782.png)

基于RRSA功能，您可以在集群内实现应用隔离的RAM角色功能。在用户提交使用了服务账户令牌卷投影功能的应用Pod后，集群将会该应用Pod创建和挂载相应的服务账户OIDC Token文件。各个Pod内的应用可以使用挂载的OIDC Token文件，扮演独立的RAM角色并使用获取的临时凭证访问云资源，既可以避免将AK硬编码在代码中，规避AK泄露的风险，又可以实现应用RAM权限的最小化。

本方案主要介绍如何创建RAM角色并授权给服务账户，以及如何在集群内的应用程序中获取并使用临时凭证。

## 方案优势

该方案能够显著提升云上应用程序的安全性、灵活性和便捷性，同时降低维护成本和操作复杂性。

### 提高安全性

通过RRSA实现将RAM角色绑定到ACK集群服务账户或Pod，使用STS Token访问云资源，避免了将访问密钥硬编码在代码中，从而消除AK泄露的风险。临时凭证（STS Token）的使用有效解决了永久凭证（AK/SK）可能带来的安全风险问题。

### 精细化管理权限

通过为不同的ACK集群服务账户绑定具有特定授权策略的RAM角色，确保仅能访问其所需的资源，实现权限最小化。

### 增强灵活性

部署在ACK集群的程序可以通过阿里云官方SDK，设置RAM角色认证方式，获取临时凭证STS Token。这种方式无需预先配置固定的访问凭证，可以根据需要动态获取和使用临时凭证。无需直接在ACK集群上管理凭证，权限的调整仅需通过修改RAM角色的授权策略来实现，快捷地维护ACK集群拥有的访问权限。

### 降低维护成本

使用临时凭证STS Token，无需频繁更新代码中的访问密钥，减少了维护成本和操作复杂性。 本方案提供Java/Python代码示例，客户能够快速完成应用改造，减少开发和部署的复杂度。

## 客户场景

### 部署在ACK集群中的应用程序采用无AK架构

#### 场景描述

客户在ACK集群上部署的应用程序需要访问其他云资源，传统的方式是客户将RAM用户的AK（Access Key）固化在集群中，如果将AK写在配置文件中，容易造成AK泄露，维护困难等问题。容器服务RRSA通过将ACK集群服务账户和RAM角色关联，使用STS Token（Security Token Service）访问云资源，解决永久凭证可能导致的安全风险问题。

#### 适用客户

- **需要高安全性**：客户需要确保AK不被暴露，以防止安全漏洞。
- **动态管理访问权限**：客户需要动态管理和临时授予集群中的应用程序访问其他资源的权限，避免长期凭证带来的风险。
- **简化运维管理**：客户希望简化运维过程中对凭证的管理，减少手动维护的复杂性。

## 方案架构

本方案通过容器服务RRSA实现临时凭证的获取和使用。该架构和流程通过动态管理和临时授予访问权限，避免了长期暴露AK的风险，提高了系统的安全性和灵活性。管理员仅需一次性配置角色和权限，后续集群中应用程序在运行时即可动态获取和使用临时凭证，简化了运维管理工作。

管理员启用ACK的RRSA（RAM Roles for Service Accounts，适用于服务账户的RAM角色）功能（图中1）。管理员创建一个授信给OIDC的Role（角色），并对该角色授予相应的权限，角色权限包含应用程序访问需要的云资源的权限（图中2）。通过注解的方式将该RAM角色和ServiceAccount进行关联，然后将ServiceAccount绑定到相应的Pod上（图中3）。ACK的RRSA功能将会自动生成OIDC Token文件并定时刷新OIDC Token（图中i）。接下来，您的应用程序就可以使用OIDC Token调用AssumeRoleWithOIDC接口，扮演绑定的RAM角色，从RAM/STS服务获取STS Token（图中4）。 最后，应用程序使用获取到的STS Token来调用目标云资源服务的API（图中5）。资源服务API处理请求并返回访问结果，客户端应用程序接收到返回的结果后完成相应的业务逻辑。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8966581571/p970790.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| RAM | [访问控制（RAM）](https://help.aliyun.com/product/28625.html)是阿里云提供的一项管理用户身份与资源访问权限的服务。使用RAM，您可以创建、管理RAM用户（例如员工、系统或应用程序），并可以控制这些RAM用户对资源的操作权限。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |
| 容器集群（ACK） | [阿里云容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）](https://help.aliyun.com/zh/ack/product-overview/product-introduction)是全球首批通过Kubernetes一致性认证的服务平台，提供高性能的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理，让您轻松高效地在云端运行Kubernetes容器化应用。本文介绍什么是容器服务 Kubernetes 版以及其下不同的集群类型。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ack/billing-information)。 |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 配置审计 | [配置审计（Cloud Config）](https://help.aliyun.com/zh/document_detail/127388.html)是一项资源审计服务，为您提供面向资源的配置历史追踪、配置合规审计等能力。面对大量资源，帮您轻松实现基础设施的自主监管，确保持续性合规。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/document_detail/133951.html)。 |
| 操作审计 | [操作审计（ActionTrail）](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)是阿里云提供的云账号资源操作记录的查询和投递服务，可用于安全分析、资源变更追踪以及合规性审计等场景。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/actiontrail/product-overview/billing-1)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| RAM管理员 | RAM管理员具备账号下RAM资源的管理权限。RAM管理员可以是阿里云账号（主账号），也可以是主账号下拥有AliyunRAMFullAccess权限的RAM用户，强烈推荐您使用RAM用户充当RAM管理员。 |
| 访问密钥（AccessKey） | 访问密钥AccessKey（简称AK）是阿里云提供给用户的永久访问凭据，一组由AccessKey ID和AccessKey Secret组成的密钥对。发起的请求会携带AccessKey ID和AccessKey Secret加密请求内容生成的签名，进行身份验证及请求合法性校验。 |
| RAM角色（RAM role） | RAM角色是一种虚拟用户，可以被授予一组权限策略。与RAM用户不同，RAM角色没有永久身份凭证（登录密码或访问密钥），需要被一个可信实体扮演。扮演成功后，可信实体将获得RAM角色的临时身份凭证，即安全令牌（STS Token），使用该安全令牌就能以RAM角色身份访问被授权的资源。 |
| 适用于服务账户的RAM角色（RRSA） | 适用于服务账户的RAM角色（RAM Roles for Service Accounts，简称RRSA）。基于这个功能，您可以在集群内实现Pod维度的OpenAPI权限隔离，从而实现云资源访问权限的细粒度隔离，降低安全风险。 |

## 安全性

### 容器服务ACK服务角色

开通容器服务时，您需要为服务账号授予系统服务角色。只有正确授予该角色权限后，容器服务才能正常地调用相关服务（ECS、OSS、NAS、SLB等）、创建集群以及保存日志等。容器服务ACK包含的服务角色的详细信息，请参见[帮助文档](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/ack-default-roles)。

## 注意事项

### 集群版本限制

RRSA功能目前仅支持1.22及以上版本的集群，即ACK集群基础版、ACK集群Pro版、ACK Serverless集群基础版和ACK Serverless集群Pro版。

### RRSA启用时机建议

启用 RRSA 会导致 API Server 的短暂重启。若业务依赖 API Server，建议在业务低峰期操作。

### 服务账户RAM角色限制

- 一个服务账户只能关联一个RAM角色。
- 一个RAM角色可以被多个服务账户复用，操作方式详见[创建RAM角色并授权](#a9ecf)。

### 支持STS的云服务

支持临时安全令牌（STS）的阿里云服务查询，请参见[支持STS的云服务](https://help.aliyun.com/zh/ram/services-that-work-with-sts)。

## 实施步骤

### 实施准备

- 如您需要审计ACK集群RRSA功能的启用情况，请确保已经开通配置审计服务。具体操作，请参考[开通配置审计服务](https://help.aliyun.com/zh/document_detail/2399579.html)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 持续合规审计（可选）

您可以通过配置审计，持续审计ACK集群RRSA功能的启用情况，及时发现未开启RRSA功能的ACK集群并为其开启RRSA功能，以实现云资源访问权限的细粒度隔离，降低安全风险。

##### 创建账号组（可选）

如果您当前为多账号环境，希望对多个成员账号进行集中的合规管理，可以使用企业管理账号将资源目录中的所有或部分成员账号加入到同一个账号组中，账号组将作为一个跨账号合规管理的管理单元。如果您是单账号环境，可跳过本步骤。

1. 登入企业管理主账号，进入[资源管理控制台](https://resourcemanager.console.aliyun.com/)，在左侧导航栏选择 **资源目录**> **可信服务**。选择配置审计，单击**管理**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8966581571/p970794.png)
2. 在**委派管理员账号**中，单击**添加**，将日志账号委派为配置审计服务的管理员。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8966581571/p970792.png)
3. 登入日志账号，进入[配置审计控制台](https://config.console.aliyun.com/)，在左侧导航栏选择**账号组**。单击**创建账号组**，通过账号组，对资源目录中的成员账号进行集中合规管理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9966581571/p970795.png)
4. 创建账号组时，账号组类型，可以选择**全局**。全局账号组包含的成员将自动与资源目录保持一致。全局账号组会自动感知资源目录中成员的新增，并自动同步加入到该全局账号组中，确保合规管理的账号范围始终与资源目录保持一致。需要注意的是，您只能新建一个全局账号组。这里我们创建一个名为 ResourceDirectory 的全局账号组，以此为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9966581571/p970799.png)

##### 创建规则

1. 进入[配置审计控制台](https://config.console.aliyun.com/)。若您使用上述步骤中的账号组进行多账号合规管控，需要在左侧导航栏中切换到需要合规管控的账号组中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8966581571/p970801.png)
2. 在左侧导航栏选择**合规审计** > **规则**，单击**新建规则**。选择名为**ACK集群启用RRSA功能**的规则。单击**下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9966581571/p970797.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9966581571/p970802.png)
3. 在**设置基本属性**中，可以对规则的风险等级、触发机制和触发频率进行设置。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9966581571/p970808.png)
4. 单击**下一步**，您可以进一步设置规则生效的范围，比如，配置该该规则只对某些资源组内的资源或者具有某些标签的资源生效。以此来对合规管控的资源范围进行更加精细化的管理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8966581571/p970809.png)
5. 创建完成后，在规则详情页，您可以看到当前账号组下，所有不合规的资源，即未开启RRSA功能的ACK集群列表。该规则，默认会每 24 个小时执行一次检测，您可以在创建规则或者修改规则时，配置该规则的触发频率。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9966581571/p970810.png)
6. 最后，您还可以将不合规资源数据投递到其他云产品中，比如日志服务、对象存储等。方便您进一步对数据进行归档、处理、审计等操作。更多投递相关的信息，请参考[配置审计投递](https://help.aliyun.com/zh/document_detail/310163.html)。

#### 启用RRSA功能

1. 登录[容器服务管理控制台](https://cs.console.aliyun.com/)。
2. 在控制台左侧导航栏，单击**集群**。
3. 在**集群列表**页面，单击目标集群名称或者目标集群右侧**操作**列下的**详情**。
4. 在集群详情页面，单击**基本信息**页签，然后在**集群信息**区域单击**RRSA OIDC**对应的**启用RRSA**。
5. 在弹出的**启用RRSA**对话框，单击**确定**。

在**基本信息**区域，当集群状态由**更新中**变为**运行中**后，表明该集群的RRSA特性已变更完成，**RRSA OIDC**右侧将显示OIDC提供商的URL链接和ARN信息。

注意：启用 RRSA 会导致 API Server 的短暂重启。若业务依赖 API Server，建议在业务低峰期操作。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8966581571/p970816.png)

集群开启RRSA功能后，ACK将在后台执行如下操作。

- 自动创建一个集群专用的OIDC Issuer服务。该服务由ACK托管，无需您运维。更多信息，请参见[OIDC Issuer](https://openid.net/specs/openid-connect-discovery-1_0.html)。
- 修改当前集群的服务账户令牌卷投影功能的配置，使用本次创建的OIDC Issuer配置合并集群已有的service-account-issuer参数的值。更多信息，请参见[部署服务账户令牌卷投影](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/enable-service-account-token-volume-projection)。
- 在您的账号下创建一个使用该OIDC Issuer的OIDC身份提供商，名称为ack-rrsa-<cluster_id>，其中 *<cluster_id>*为您的集群ID。更多信息，请参见[管理OIDC身份提供商](https://help.aliyun.com/zh/ram/manage-an-oidc-idp)。

#### 安装ack-pod-identity-webhook组件

1. 在**集群列表**页面，单击目标集群名称，然后在左侧导航栏，选择**运维管理 > 组件管理**。
2. 在**组件管理**页面，单击**安全**页签，找到ack-pod-identity-webhook组件，单击组件右下方的**安装**。
3. 在提示对话框确认组件信息后，单击**确定**。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8966581571/p970814.png)

ack-pod-identity-webhook组件会为Pod自动注入如下配置：

| **类别** | **配置项名称** | **配置项说明** |
| --- | --- | --- |
| 环境变量 | ALIBABA_CLOUD_ROLE_ARN | 需要扮演的RAM角色ARN。 |
| ALIBABA_CLOUD_OIDC_PROVIDER_ARN | OIDC身份提供商的ARN。 |  |
| ALIBABA_CLOUD_OIDC_TOKEN_FILE | 包含OIDC Token的文件路径。 |  |
| VolumeMount | rrsa-oidc-token | 挂载OIDC Token的配置。 |
| Volume | rrsa-oidc-token | 挂载OIDC Token的配置。 |

如果您希望通过不安装ack-pod-identity-webhook组件的方式使用RRSA功能，您可以手动修改应用模板挂载应用所需的OIDC Token文件并配置相关环境变量。具体操作，请参见[手动修改应用模板使用RRSA功能（可选）](#smc2J)。

#### 创建RAM角色并授权

创建一个RAM角色，并授予应用程序所需的云资源操作权限。

1. 使用阿里云账号登录[RAM控制台](https://ram.console.aliyun.com/?spm=a2c4g.11186623.0.0.772113earTZgGv)。
2. 在左侧导航栏，选择**身份管理 > 角色**，然后在**角色**页面，单击**创建角色**。
3. 在**创建角色**面板，选择可信实体类型为**身份提供商**，然后单击**下一步**。
4. 在**配置角色**页面，配置如下角色信息后，单击**完成**。**配置项****描述****角色名称**<your_role_name>。**备注**选填有关该角色的备注信息。**身份提供商类型****OIDC**。**选择身份提供商**ack-rrsa-<cluster_id>。其中，<cluster_id>为您的集群ID。**限制条件****oidc:iss**：保持默认。**oidc:aud**：选择**sts.aliyuncs.com**。**oidc:sub**：条件判定方式选择**StringEquals**，值的格式为`system:serviceaccount:<namespace>:<serviceAccountName>`。<namespace>：应用所在的命名空间。<serviceAccountName>：服务账户名称。根据示例应用的信息，此处需要填入`system:serviceaccount:rrsa-demo:demo-sa`。如果有配置多个服务账户的需求：可以条件判断方式选择**StringEquals**，点击右侧「添加」输入多个值。也可以条件判断方式选择**StringLike**，通过通配符批量受信给多个命名空间和服务账号，如`system:serviceaccount:*:prefix*`。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8966581571/p970822.png)
5. 为创建的角色授予权限，指定这个RAM角色可以访问的云资源（如：示例应用所需的AliyunCSReadOnlyAccess系统策略权限）。具体操作，请参见[为RAM角色授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-a-ram-role)。

注意这个角色就是应用程序实际扮演的角色，需要赋上对应云资源操作权限。

如果您希望使用已存在的RAM角色，不创建新的RAM角色，您可以为已有RAM角色新增相关权限。具体操作，请参见[使用已存在的RAM角色并授权（可选）](#AqDGg)。

#### 应用程序中获取并使用临时凭证

当您通过阿里云SDK调用OpenAPI进行资源操作时，必须正确配置凭证信息。强烈推荐您使用阿里云的Credentials工具，帮助您轻松地获取和管理访问凭证：

- 基于OIDC RAM角色获取临时凭证时，Credentials工具会自动获取ServiceAccount绑定的OIDC RAM角色，并调用AssumeRoleWithOIDC获取临时访问凭证
- Credentials工具会自动维护临时凭证的生命周期，研发人员无需关心临时凭证的到期更新，Credentials工具会自动保证凭证的周期性更新。
- 借助Credentials工具的默认凭据链，可以用同一套代码，通过程序之外的配置来控制不同环境下的凭据获取方式

##### 阿里云V2.0 SDK（推荐）

目前，[阿里云V2.0 SDK](https://help.aliyun.com/zh/sdk/product-overview/differences-between-v1-and-v2-sdks)已经内置了支持使用RRSA OIDC Token进行OpenAPI认证的功能，所有基于V2.0 SDK生成并且支持STS Token认证的云产品SDK都将默认支持RRSA OIDC Token认证。

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

Credentials工具支持多种方式初始化凭据客户端，您可根据实际情况选择合适的方式进行凭据客户端初始化。下面介绍显式配置OIDC RAM角色和默认凭据链的方式，更多方式，请参考[初始化凭据客户端](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials)。

注意：使用Credentials工具要求Java版本 >= 1.8。

###### 显式配置OIDC RAM角色（推荐）

推荐您使用该方式，在代码中明确的显式配置，避免运行环境中的环境变量、配置文件等带来非预期的结果。您可以通过判断环境类型来设置Credentials Config的值。实现一套代码，支持多种场景：ECS实例角色、ACK RRSA、环境变量等。其中ACK对应的配置类型为`oidc_role_arn`，Credentials工具会自动获取OIDC RAM角色，调用AssumeRoleWithOIDC换取STS Token，完成凭据客户端初始化。

Java代码示例如下，详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-ack-sts-token/code-example/java/common/src/main/java/org/example/sdk2_0/CredentialsOIDCRoleArnSample.java)。

```
import com.aliyun.credentials.Client;
import com.aliyun.credentials.models.Config;
// import com.alibaba.fastjson2.JSON;
// import com.aliyun.sts20150401.models.GetCallerIdentityResponse;

/**
 * 通过Credentials工具初始化，使用OIDCRoleArn
 */
public class CredentialsOIDCRoleArnSample {
    public static void main(String[] args) throws Exception {
        // 初始化凭据客户端
        Config credentialConfig = new Config();
        credentialConfig.setType("oidc_role_arn");
        credentialConfig.setRoleArn(System.getenv("ALIBABA_CLOUD_ROLE_ARN"));
        credentialConfig.setOidcProviderArn(System.getenv("ALIBABA_CLOUD_OIDC_PROVIDER_ARN"));
        credentialConfig.setOidcTokenFilePath(System.getenv("ALIBABA_CLOUD_OIDC_TOKEN_FILE"));
        // 角色会话名称，如果配置了ALIBABA_CLOUD_ROLE_SESSION_NAME这个环境变量，则无需设置
        credentialConfig.setRoleSessionName("<RoleSessionName>");
        // 设置更小的权限策略，非必填。示例值：{"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"}
        credentialConfig.setPolicy("<Policy>");
        // Not required, the external ID of the RAM role
        // This parameter is provided by an external party and is used to prevent the confused deputy problem.
        credentialConfig.setExternalId("<ExternalId>");
        // 设置session过期时间
        credentialConfig.setRoleSessionExpiration(3600);
        Client credentialsClient = new Client(credentialConfig);

        // 调用API，以GetCallerIdentity获取当前调用者身份信息为例
        // com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        // config.setCredential(credentialsClient);
        // config.setEndpoint("sts.cn-hangzhou.aliyuncs.com");
        // com.aliyun.sts20150401.Client stsClient = new com.aliyun.sts20150401.Client(config);
        // GetCallerIdentityResponse getCallerIdentityResponse = stsClient.getCallerIdentity();
        // System.out.println(JSON.toJSONString(getCallerIdentityResponse));
    }
}
```

更多语言代码示例，请参见[帮助文档](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services)。

###### 默认凭据链

当您在初始化凭据客户端不传入任何参数时，Credentials工具会使用默认凭据链方式初始化客户端。借助Credentials工具的默认凭据链，您可以用同一套代码，通过程序之外的配置来控制不同环境下的凭据获取方式。除非您清楚的知道默认凭据链中凭据信息查询优先级以及您的程序运行的各个环境中凭据信息配置方式，否则不建议您使用默认凭据链，推荐您使用显式配置OIDC RAM角色方式，避免运行环境中的环境变量、配置文件等带来非预期的结果。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-ack-sts-token/code-example/java/common/src/main/java/org/example/sdk2_0/CredentialsDefaultSample.java)。

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

使用默认凭据链的方式，Credentials工具会按照优先级依次查找相关凭据的信息，请避免环境变量维护不当导致获取到了非预期的凭据。

如果您需要从长期固定AccessKey的使用方式进行迁移，只需修改少量代码即可完成，如下图所示，左侧一栏是使用固定AccessKey初始化阿里云SDK，右侧一栏是使用Credentials工具初始化阿里云SDK。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9966581571/p970823.png)

##### 阿里云V1.0 SDK（不推荐）

阿里云V1.0 SDK是较早使用版本，稳定性良好，不少老用户习惯于原版SDK的开发，本章节则是给这部分用户提供一个简练的使用指南。对于新用户，我们强烈建议直接采用新版SDK，同时也建议老用户尽早迁移到新版SDK。

要初始化SDK客户端，可以使用Credentials工具。以Java为例，通过Maven方式安装Credentials工具：

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

下述代码演示了先初始化凭据客户端，再使用凭据客户端的凭据信息初始化V1.0 SDK客户端。关于凭据客户端的初始化的更多方式，请参考[管理访问凭据](https://help.aliyun.com/zh/sdk/developer-reference/credentials)。详细代码请参考[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-ack-sts-token/code-example/java/common/src/main/java/org/example/sdk1_0/CredentialsDefaultSample.java)。

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

public class Main {

    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou");
        // 初始化凭据客户端
        Client credentialClient = new Client();
        // 用凭据客户端初始化SDK1.0客户端
        IAcsClient client = createAcsClientByCredentials(profile, credentialClient);

        // 调用API，以GetCallerIdentity获取当前调用者身份信息为例
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

##### OSS SDK

您也可以使用阿里云OSS的SDK，实现临时凭证的获取和使用。在集成OSS SDK后，您需要初始化OSS客户端。

需要集成阿里云的Credentials工具，目前支持的SDK有

| OSS SDK 语言 | 推荐版本 |
| --- | --- |
| Java | >= 3.11.3 |
| Python | >= 2.14.0 |
| PHP | >= 2.6.0 |
| Golang | >= 3.0.2 |

以Java为例，通过Maven方式安装Credentals工具以及OSS SDK：

```
<!--建议使用最新发布的Credentials版本。-->
<!--获取所有已发布的版本列表，请参见https://github.com/aliyun/credentials-java/blob/master/ChangeLog.txt-->
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>credentials-java</artifactId>
  <version>LATEST</version>
</dependency>

<dependency>
  <groupId>com.aliyun.oss</groupId>
  <artifactId>aliyun-sdk-oss</artifactId>
  <version>3.17.4</version>
</dependency>
```

下述代码演示了先初始化凭据客户端，再使用凭据客户端的凭据信息初始化OSS客户端。关于凭据客户端的初始化方式，可以参考[阿里云V2.0 SDK](#g3nBW)章节中介绍的两种方式，更多方式，请参考[初始化凭据客户端](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials)。

```
import com.aliyun.credentials.Client;
import com.aliyun.credentials.models.CredentialModel;
import com.aliyun.oss.ClientBuilderConfiguration;
import com.aliyun.oss.ClientConfiguration;
import com.aliyun.oss.OSSClient;
import com.aliyun.oss.common.auth.Credentials;
import com.aliyun.oss.common.auth.CredentialsProvider;
import com.aliyun.oss.common.auth.DefaultCredentials;
import com.aliyun.oss.common.comm.SignVersion;

public class Main {
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

您也可以使用阿里云SLS的SDK，实现临时凭证的获取和使用。在集成SLS SDK后，您需要初始化SLS客户端。

需要集成阿里云的Credentials工具，目前支持的SDK有

| SLS SDK 语言 | 推荐版本 |
| --- | --- |
| Java | >= 0.6.88 |
| Python | >= 0.9.3 |
| PHP | >= 0.6.4 |
| Golang | >= 0.1.55 |

以Java为例，通过Maven方式安装Credentials工具以及SLS SDK：

```
<!--建议使用最新发布的Credentials版本。-->
<!--获取所有已发布的版本列表，请参见https://github.com/aliyun/credentials-java/blob/master/ChangeLog.txt-->
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>credentials-java</artifactId>
  <version>LATEST</version>
</dependency>

<dependency>
  <groupId>com.aliyun.openservices</groupId>
  <artifactId>aliyun-log</artifactId>
  <version>0.6.107</version>
</dependency>
```

下述代码演示了先初始化凭据客户端，再使用凭据客户端的凭据信息初始化SLS客户端。关于凭据客户端的初始化方式，可以参考[阿里云V2.0 SDK](#g3nBW)章节中介绍的两种方式，更多方式，请参考[初始化凭据客户端](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials)。

```
import com.aliyun.credentials.models.CredentialModel;
import com.aliyun.openservices.log.Client;
import com.aliyun.openservices.log.common.auth.DefaultCredentials;

public class Main {
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

##### 代码示例

###### 代码介绍

本方案提供使用阿里云SDK、OSS SDK及SLS SDK使用Credentials工具获取临时凭证的代码示例，包括Java和Python语言，方便客户能够快速完成应用改造。

###### 代码地址

代码地址详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-ack-sts-token)。

#### 部署应用

如下YAML示例中，**为命名空间增加标签**`pod-identity.alibabacloud.com/injection: 'on'`，并**为服务账户增加注解**`pod-identity.alibabacloud.com/role-name: demo-role-for-rrsa`，启用ack-pod-identity-webhook组件的配置自动注入功能。

```
---
apiVersion: v1
kind: Namespace
metadata:
  name: rrsa-demo
  labels:
    pod-identity.alibabacloud.com/injection: 'on'

---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: demo-sa
  namespace: rrsa-demo
  annotations:
    pod-identity.alibabacloud.com/role-name: demo-role-for-rrsa
    pod-identity.alibabacloud.com/service-account-token-expiration: '3600' # 设置该服务账户的Pod挂载的OIDC Token的有效期

---
apiVersion: v1
kind: Pod
metadata:
  name: demo
  namespace: rrsa-demo
  annotations:
    pod-identity.alibabacloud.com/service-account-token-expiration: '3600' # 设置该Pod挂载的OIDC Token的有效期
spec:
  serviceAccountName: demo-sa
  containers:
    - image: <your_image>
      imagePullPolicy: "Always"
      name: demo
  restartPolicy: OnFailure
```

可以通过**为服务账户增加注解**`pod-identity.alibabacloud.com/service-account-token-expiration`来指定使用该服务账户的Pod挂载的OIDC Token的有效期。取值范围：[600, 43200]，单位：秒。默认值为3600，当配置值无效时，将使用3600作为此配置项的值。

也可以在Pod中添加注解`pod-identity.alibabacloud.com/service-account-token-expiration`，当服务账户和Pod上都存在该配置项时，服务账户上的配置将会被忽略。

关于ack-pod-identity-webhook组件配置的更多说明，请参见[ack-pod-identity-webhook](https://help.aliyun.com/zh/ack/product-overview/ack-pod-identity-webhook)。

#### 手动修改应用模板使用RRSA功能（可选）

您可以通过手动修改应用模板挂载应用所需的OIDC Token文件以及配置相关环境变量，在不安装ack-pod-identity-webhook组件的情况下使用RRSA功能。

应用模板示例代码如下。

```
apiVersion: v1
kind: Pod
metadata:
  name: demo
  namespace: rrsa-demo
spec:
  containers:
    env:
    - name: ALIBABA_CLOUD_ROLE_ARN
      value: <role_arn>
    - name: ALIBABA_CLOUD_OIDC_PROVIDER_ARN
      value: <oid_provider_arn>
    - name: ALIBABA_CLOUD_OIDC_TOKEN_FILE
      value: /var/run/secrets/ack.alibabacloud.com/rrsa-tokens/token
    image: <your_image>
    imagePullPolicy: Always
    name: demo
    volumeMounts:
    - mountPath: /var/run/secrets/ack.alibabacloud.com/rrsa-tokens
      name: rrsa-oidc-token
      readOnly: true
  restartPolicy: OnFailure
  serviceAccount: demo-sa
  serviceAccountName: demo-sa
  volumes:
  - name: rrsa-oidc-token
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          audience: sts.aliyuncs.com
          expirationSeconds: 3600
          path: token
```

**重要**：请替换应用模板示例代码中的如下字段。

- **<oid_provider_arn>**：替换为当前集群的OIDC提供商ARN。该ARN可在[容器服务管理控制台](https://cs.console.aliyun.com/) > 集群信息 > 基本信息获取。
- **<role_arn>**：需要替换为当前应用使用的RAM角色ARN。该ARN可在[RAM控制台](https://ram.console.aliyun.com/) > 角色 > 角色详情页面获取。
- **audience**：字段值需为`sts.aliyuncs.com`。
- **expirationSeconds**：单位为秒，取值范围为`[600, 43200]`，即10分钟~12小时。如果设置的值大于43200（12小时），实际的OIDC Token的过期时间仍为12小时。

部署修改后的应用模板后，应用内程序可以使用容器内挂载的OIDC Token（环境变量`ALIBABA_CLOUD_OIDC_TOKEN_FILE`指向的文件内容）、角色的ARN（环境变量`ALIBABA_CLOUD_ROLE_ARN`配置的值）以及OIDC身份提供商的ARN（环境变量`ALIBABA_CLOUD_OIDC_PROVIDER_ARN`配置的值），调用STS的`AssumeRoleWithOIDC`接口，获取一个扮演指定RAM角色的临时凭证，然后使用该临时凭证访问云资源OpenAPI。应用参考代码，请参见[阿里云官方SDK使用RRSA OIDC Token的参考代码](https://help.aliyun.com/zh/ack/serverless-kubernetes/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services)。

#### 使用已存在的RAM角色并授权（可选）

如果您的应用需要使用已存在的RAM角色，而非创建新的单独RAM角色，您可以修改RAM角色的信任策略，新增一条允许使用指定的服务账户的应用有权限通过扮演此RAM角色获取临时凭证的信任策略。更多信息，请参见[修改RAM角色的信任策略](https://help.aliyun.com/zh/ram/user-guide/edit-the-trust-policy-of-a-ram-role)。

RAM角色信任策略中新增的Statement条目内容示例如下。

```
{
  "Action": "sts:AssumeRole",
  "Condition": {
    "StringEquals": {
      "oidc:aud": "sts.aliyuncs.com",
      "oidc:iss": "<oidc_issuer_url>",
      "oidc:sub": "system:serviceaccount:<namespace>:<service_account>"
    }
  },
  "Effect": "Allow",
  "Principal": {
    "Federated": [
      "<oidc_provider_arn>"
    ]
  }
}
```

**重要：**请替换Statement条目内容示例中的如下字段。

- **<oidc_issuer_url>**：替换为当前集群的OIDC提供商URL。该URL可在[容器服务管理控制台](https://cs.console.aliyun.com/) > 集群信息 > 基本信息获取。
- **<oidc_provider_arn>**：替换为当前集群的OIDC提供商ARN。该ARN可在[容器服务管理控制台](https://cs.console.aliyun.com/) > 集群信息 > 基本信息获取。
- **<namespace>**：替换为应用所在的命名空间。
- **<service_account>**：替换为应用使用的服务账户。

#### OIDC RAM角色操作审计（可选）

若您需要对OIDC RAM角色进行操作审计，例如使用该角色的身份做了什么操作。您可以使用您的日志审计账号进入[操作审计控制台](https://actiontrail.console.aliyun.com/)，在**事件>事件查询**中找到该角色的操作事件，点击查看事件详情，可以通过事件记录中的`requestParameters.stsTokenPrincipalName`来区分该操作来自于哪一个角色 Session，该字段是一个固定的格式：${角色名称}/${角色 Session}。

注：角色 Session可以通过环境变量ALIBABA_CLOUD_ROLE_SESSION_NAME来指定，也可以在代码里的credentials config中设置。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8966581571/p970825.png)

若您的账号开启了审计日志投递，可以在**事件>高级查询**中运行下方所示的查询SQL语句快速查找出使用特定角色身份在特定角色Session下进行的所有操作：

```
event.requestParameters.stsTokenPrincipalName:${角色名称}/${角色 Session}
```

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8966581571/p970827.png)

## 故障排除

### 为什么通过阿里云官方SDK使用RRSA OIDC Token报错？

使用阿里云官方SDK使用RRSA OIDC Token出现报错信息的解决方法，请参见[帮助文档](https://help.aliyun.com/zh/ack/serverless-kubernetes/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-241（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
