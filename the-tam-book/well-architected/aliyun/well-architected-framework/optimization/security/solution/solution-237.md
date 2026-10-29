<!-- source: https://help.aliyun.com/zh/well-architected/solution-237 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929338 -->

# 通过KMS实现固定AccessKey的集中管控

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970835.png)

身份和权限管理是云上安全的重中之重；而凭证管理是云上最容易出现风险的环节之一，管理不善将导致凭证泄漏，进而导致数据泄漏、资产损失等严重安全事故。

本文档介绍了一种企业客户集中管控固定 AccessKey 的方案，实现固定 AccessKey 的统一管理、加密存储、自动轮转，降低凭证泄露风险，提升安全水位，满足规范要求。

## 方案优势

### 集中管控

企业运维可以通过 KMS 凭据管理的能力，托管 AccessKey，对其进行集中管控。同时通过资源共享的共享单元以及VPC网络互通等手段和能力，实现跨账号跨地域的访问 KMS，使用托管的 AccessKey，降低企业的 IT 采购成本和管理成本。

### 自动周期性轮转

通过 KMS 凭据管理，可以自动周期性的轮转 AccessKey，而无需人工轮转，整个轮转过程企业研发人员无需感知，通过自动轮转，降低实施难度，减免人工成本，极大提升安全水位。同时 KMS 凭据管理具备应急处置能力，当发生 AccessKey 泄露等安全问题时，您可以通过立即轮转的方式更新凭据，应用程序不受任何影响。

### 加密存储

在 KMS 凭据管理中，托管的 AccessKey 会加密存储，通过托管和加密，防止凭证硬编码和明文存在带来的凭证泄露，提升凭证安全性。

### 持续审计合规

基于配置审计，持续审计不再使用以及长期未轮转的 AccessKey，及时发现并处置不合规的 AccessKey，降低泄露风险，提升安全水位。

## 客户场景

### 固定 AccessKey 集中、安全管控

#### 场景描述

企业应用程序使用固定 AccessKey 访问阿里云，运维和安全团队需要对固定 AccessKey 进行集中和安全的管控，降低管理成本，同时避免 AccessKey 泄露造成严重的安全事故。

#### 适用客户

- 应用程序使用固定 AccessKey 访问阿里云资源
- AccessKey 配置信息分散在多个业务应用程序中，无法统一管理
- AccessKey 硬编码在代码中，无法及时更新轮转AK/SK
- AccessKey 以明文方式存在，易发生泄露问题，存在安全隐患

## 方案架构

企业应用程序访问阿里云存在如下几个场景：

1. 您的应用部署在阿里云上，本身没有多云诉求，此时建议您使用临时凭证（STS Token）的方案，以降低凭证泄露的风险，缩短凭证暴漏的时长。
2. 您的应用需要多云部署、云下 IDC 部署或者企业自有凭证管理方案，此时您需要使用固定 AccessKey 访问阿里云资源。本方案针对该场景，通过 KMS 实现固定 AccessKey 的加密、轮转和集中管控。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970849.png)

本方案基于 KMS 实现固定 AccessKey 的集中管控。首先在共享服务账号中创建 KMS 实例，通过共享单元将该 KMS 实例共享给其他应用账号（图中1），同时，如果您的应用部署在阿里云多个地域的 VPC 内，您可以通过建立跨地域 VPC 间连接、云解析 PrivateZone 功能来实现跨地域访问 KMS 实例（图中2），如此，在多账号体系下，降低企业的管理成本和 IT 采购成本。如果您的企业有更高的安全要求，建议您为每一个应用单独创建一个 KMS 实例用于托管 AccessKey 和数据加密，保证各个应用之间的强隔离。接着，企业运维人员可以将 AccessKey，以 RAM 凭据形式托管到 KMS 中（图中3），同时对 AccessKey 进行加密和自动轮转。企业研发人员使用 KMS 官方提供的安全便捷的客户端接入方式，在应用程序中配置凭据名称并部署应用（图中5、6），当程序运行时，以无代码或者低代码的方式，动态获取并使用 AccessKey（图中7）。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970837.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 密钥管理服务KMS | [密钥管理服务KMS（Key Management Service）](https://help.aliyun.com/zh/kms/product-overview/what-is-key-management-service-1)是您的一站式密钥管理和数据加密服务平台、一站式凭据安全管理平台，提供简单、可靠、安全、合规的数据加密保护和凭据管理能力。KMS帮助您降低在密码基础设施、数据加解密产品和凭据管理产品上的采购、运维、研发开销，以便您只需关注业务本身。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/kms/product-overview/billing)。 |
| VPC | [专有网络VPC（Virtual Private Cloud）](https://help.aliyun.com/product/27706.html)是用户基于阿里云创建的自定义私有网络, 不同的专有网络之间二层逻辑隔离，用户可以在自己创建的专有网络内创建和管理云产品实例，比如ECS、SLB、RDS等。 | 免费，详情见[产品计费](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |
| 容器集群（ACK） | [阿里云容器服务 Kubernetes 版 ACK（Container Service for Kubernetes）](https://help.aliyun.com/zh/ack/product-overview/product-introduction)是全球首批通过Kubernetes一致性认证的服务平台，提供高性能的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理，让您轻松高效地在云端运行Kubernetes容器化应用。本文介绍什么是容器服务 Kubernetes 版以及其下不同的集群类型。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ack/billing-information)。 |
| 配置审计 | [配置审计（Cloud Config）](https://help.aliyun.com/zh/document_detail/127388.html)是一项资源审计服务，为您提供面向资源的配置历史追踪、配置合规审计等能力。面对大量资源，帮您轻松实现基础设施的自主监管，确保持续性合规。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/document_detail/133949.html)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |
| 访问密钥（AccessKey） | 访问密钥AccessKey（简称AK）是阿里云提供给用户的永久访问凭据，一组由AccessKey ID和AccessKey Secret组成的密钥对。用于通过开发工具（API、CLI、SDK、Terraform等）访问阿里云时，发起的请求会携带AccessKey ID和AccessKey Secret加密请求内容生成的签名，进行身份验证及请求合法性校验。 |
| 共享单元 | 共享单元是资源共享的实例。共享单元包括：资源所有者、资源使用者和共享的资源。 |
| RAM凭据 | RAM凭据是KMS支持的一种全托管类型的凭据。您可以使用RAM凭据托管RAM用户的访问密钥（AccessKey）。 |
| 应用接入点 | 应用接入点AAP（Application Access Point）是KMS提供的一种身份验证和访问控制机制，当自建应用使用密钥或凭据时，对其进行身份认证和行为鉴权。 |
| 用户主密钥CMK | 用户主密钥CMK（Customer Master Key）指的是由您自主创建和托管在KMS的密钥，简称为“主密钥”。主密钥由密钥ID、基本元数据以及密钥材料组成。 |

## 安全性

### 配置审计服务关联角色

为了完成配置审计的功能，需要获取其他云服务的访问权限而提供的RAM角色，详情参见[配置审计服务关联角色](https://help.aliyun.com/zh/document_detail/162994.html)。

### KMS安全与合规能力

KMS经过严格的安全设计和审核，保证您的密钥在阿里云得到最严格的保护。

- KMS仅提供基于TLS的安全访问通道，并且仅使用安全的传输加密算法套件，符合PCI DSS等安全规范。
- KMS支持监管机构许可和认证的密码设施。阿里云加密服务提供了经国家密码管理局检测和认证的硬件密码设备，取得了GM/T 0028 第二级认证。KMS支持集成您在阿里云加密服务中管理的加密机集群进行密钥管理和密码计算。关于阿里云加密服务的更多信息，请参见[什么是加密服务](https://help.aliyun.com/zh/hsm/product-overview/what-is-cloud-hardware-security-module#concept-lhk-wgd-xdb)。

### VPC 安全性

专有网络VPC具有安全可靠、灵活可控、灵活可用以及较强的可扩展性，详情参见[产品优势](https://help.aliyun.com/zh/vpc/product-overview/benefits)及[访问控制](https://help.aliyun.com/zh/vpc/access-control)。

## 注意事项

### KMS使用限制

- 在KMS托管RAM凭据，只支持托管RAM用户（子账号）的AccessKey，不支持托管阿里云账号（主账号）的AccessKey。
- 跨地域访问专属KMS实例仅用于用户自建应用集成专属KMS的使用场景，不适用云产品服务端加密集成KMS的使用场景。

### KMS实例共享注意事项

- 购买KMS实例后，您需要先启用实例，才可以通过资源共享将该KMS实例共享给其他应用账号
- 共享KMS实例会消耗KMS实例的访问管理数量的配额，共享时，需要保证该KMS实例的可用访问管理数量大于等于共享时资源使用者的数量。当KMS实例访问管理数量不足时，请及时升配，否则共享将无法成功。需要注意的是，KMS实例访问管理数量，除了包含共享KMS实例时资源使用者的数量，还包含实例关联的VPC数量，例如，您的KMS实例需要关联3个VPC，并共享给2个资源使用者，那么访问管理数量配额最少为5才能满足业务需求。如果您需要提升配额，请参见[升级KMS实例](https://help.aliyun.com/zh/kms/user-guide/manage-kms-instances#6c6e73b014d8y)。

## 自动化模板

### 模板介绍

本方案提供了基于 Terraform 的自动化部署模板，模板代码结构如下所示。

```
├── step1-share-vswitch					// 如果您需要跨账号使用 KMS 实例，通过资源共享，将需要访问 KMS 实例的 VPC 共享给共享服务账号（KMS 实例将创建在共享账号中）
├── step2-create-kms-instance		// 在共享服务账号中创建 KMS 实例
├── step3-share-kms-instance		// 如果您需要跨账号使用 KMS 实例，通过资源共享，将共享服务账号下的 KMS 实例共享给其他应用账号
└── step4-create-kms-aap				// 在应用账号下，给 KMS 实例创建应用接入点
```

### 模板地址

模板地址详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-kms-managed-accesskey/deployment)。

## 实施步骤

### 实施准备

- 共享服务账号中，确保在应用所在地域有1个VPC和1个交换机。建议您先登录[专有网络管理控制台](https://vpcnext.console.aliyun.com/vpc)，查看已有的VPC、交换机以及交换机所在的可用区，然后再启用KMS实例。也可以新创建VPC和交换机，具体操作，请参见[创建专有网络和交换机](https://help.aliyun.com/zh/vpc/create-and-manage-a-vpc)或[创建交换机](https://help.aliyun.com/zh/vpc/create-and-manage-vswitch)。
- 如需共享KMS实例给应用账号，需启用资源目录组织共享，使用资源目录管理账号登录[资源共享控制台](https://resourcemanager.console.aliyun.com/resource-share?spm=a2c4g.11186623.0.0.e3cb2079BBxpxK)。在左侧导航栏，选择**资源共享**>**设置**。单击**启用**。在**资源共享服务关联角色**对话框，单击**确定**。系统会自动创建一个名为AliyunServiceRoleForResourceSharing的服务关联角色，用于获取资源目录的组织信息。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 持续合规审计（可选）

您可以通过配置审计，持续审计闲置以及长时间未轮转的 AccessKey，及时发现并处置不合规的 AccessKey，减少 AccessKey 的泄露隐患，提升安全水位。

1. 登入企业管理主账号，进入[资源管理控制台](https://resourcemanager.console.aliyun.com/)，在左侧导航栏选择 **资源目录**> **可信服务**。选择配置审计，单击**管理**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970843.png)
2. 在**委派管理员账号**中，单击**添加**，将日志账号委派为配置审计服务的管理员
3. 登入日志账号，进入[配置审计控制台](https://config.console.aliyun.com/)，在左侧导航栏选择**账号组**。单击**创建账号组**，通过账号组，对资源目录中的成员账号进行集中合规管理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970839.png)
4. 创建账号组时，账号组类型，可以选择**全局**。全局账号组包含的成员将自动与资源目录保持一致。全局账号组会自动感知资源目录中成员的新增，并自动同步加入到该全局账号组中，确保合规管理的账号范围始终与资源目录保持一致。需要注意的是，您只能新建一个全局账号组。这里我们创建一个名为 ResourceDirectory 的全局账号组，以此为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970842.png)
5. 在左侧导航栏切换到需要合规管控的账号组中，这里以上一步创建的名为 ResourceDirectory 的账号组为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970850.png)
6. 在左侧导航栏选择**合规审计** > **规则**，单击**新建规则**。选择名为**RAM用户不存在闲置AccessKey、RAM用户的AccessKey在指定时间内轮换**等合规规则。单击**下一步**
7. 在**参数设置**中，规则参数进行设置，比如**RAM用户的AccessKey在指定时间内轮换**，您可以修改指定的轮转时间。
8. 单击**下一步**，您可以进一步设置规则生效的范围，比如，配置该规则只对某些资源组内的资源或者具有某些标签的资源生效。以此来对合规管控的资源范围进行更加精细化的管理
9. 创建完成后，在规则详情页，您可以看到当前账号组下，所有不合规的资源，既不符合要求的所有AccessKey。该规则，默认会每 24 个小时执行一次检测，您可以在创建规则或者修改规则时，配置该规则的触发频率
10. 最后，您还可以将不合规资源数据投递到其他云产品中，比如日志服务、对象存储等。方便您进一步对数据进行归档、处理、审计等操作。更多投递相关的信息，请参考[配置审计投递](https://help.aliyun.com/zh/document_detail/310163.html)。

#### 购买并启用KMS实例

如还未购买KMS实例，需先购买：

1. 使用共享服务账号登录[密钥管理服务控制台](https://yundun.console.aliyun.com/?spm=a2c4g.11186623.0.0.a71b6d72uwCaWQ&p=kms#/keyList/base)
2. 在顶部菜单栏选择地域，地域需要和您的应用所在地域保持一致。如果您的应用部署在多个地域，您可以选择其中任意一个地域创建KMS实例，通过后续章节**跨地域访问KMS实例**，实现KMS实例的跨地域访问。
3. 在左侧导航栏单击**资源 > 实例管理**。
4. 在**实例管理**页面单击**创建实例**，选择要购买的KMS实例规格，单击**立即购买**。

购买完成后：

1. 在**实例管理**页面，定位到目标KMS管理实例，单击**操作**列的**启用**。
2. 在**启用KMS实例**面板，完成各项配置后单击**确定**。需要注意的是，KMS实例访问管理数量，包含共享KMS实例时资源使用者的数量以及实例关联的VPC数量，例如，您的KMS实例需要关联3个VPC，并共享给2个资源使用者，那么访问管理数量配额最少为5才能满足业务需求。

请等待约30分钟，然后刷新页面，当状态变更为已启用时，表示KMS实例启用成功。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970841.png)

#### 跨账号访问KMS实例（可选）

在企业多账号场景下， 您可以通过资源共享将KMS实例共享给其他应用账号，以此实现统一的资源管理，降低企业的管理成本和 IT 采购成本。如果您的企业有更高的安全要求，建议您为每一个账号单独创建一个 KMS 实例用于托管 AccessKey 和数据加密，保证各个账号之间的强隔离。

##### 规划访问管理数量配额

在共享KMS实例前，您需要提前规划该KMS实例的访问管理数量。KMS实例访问管理数量，包含共享KMS实例时资源使用者的数量以及实例关联的VPC数量，例如，您的KMS实例需要关联3个VPC，并共享给2个资源使用者，那么访问管理数量配额最少为5才能满足业务需求。如果您需要提升配额，请参见[升级KMS实例](https://help.aliyun.com/zh/kms/user-guide/manage-kms-instances#6c6e73b014d8y)。

##### 多账号共享 KMS 实例

通过共享单元将该 KMS 实例共享给其他应用账号

1. 使用共享服务账号（KMS资源所有者账号）登录[资源共享控制台](https://resourcemanager.console.aliyun.com/resource-share)。
2. 在左侧导航栏，选择**资源共享**>**我的共享**。
3. 在顶部菜单栏左上角处，选择KMS实例所在的地域。
4. 单击**创建共享单元**。
5. 在**配置基本信息并添加资源**页面，输入共享单元名称，然后选中需要共享的KMS实例，最后单击**下一步**。
6. 在**关联权限**页面，选择共享权限**AliyunRSDefaultPermissionKMSInstance**，然后单击**下一步**。
7. 在**关联资源使用者**页面，添加资源使用者，然后单击**下一步**。在**使用者范围**区域，选择**仅允许资源目录内共享**。在**资源使用者类型**区域，选择**资源夹（组织单元）**。填入应用账号所在的资源夹ID，单击**添加**。
8. 在**确认并提交**页面，单击**确定**。共享成功后，该资源夹下的成员就可以访问资源所有者共享给自己的KMS实例。

资源的共享状态变为**已关联**，表明资源已经完成共享。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970854.png)

##### 同地域访问KMS实例

如果您的使用场景是同地域下的VPC访问KMS实例，您有如下两种方式实现KMS实例的访问：

1. 推荐您优先参考下述章节**通过绑定VPC实现KMS实例的访问**，使用KMS产品内置方案，实现KMS实例的访问。
2. 如果您已经完成了组网，实现了应用账号下需要访问KMS实例的VPC和共享服务账号下KMS实例所在的VPC之间的互通，出于降低IT服务采购费用的成本考虑，您可以考虑参考下述章节**通过VPC互连实现KMS实例的访问（可选）**，通过网络互通的方式，实现KMS实例的访问。

如果您的使用场景是不同地域下的VPC访问KMS实例，您可以参考下方章节**跨地域访问KMS实例（可选）**。

###### 通过绑定VPC实现KMS实例的访问

共享服务账号下的KMS实例共享给应用账号后，您还需要将应用账号下的VPC绑定到该KMS实例上，实现应用账号的VPC内对KMS实例的访问。需要注意的是：

- 要绑定的VPC和KMS实例必须在同一个地域。如果在不同地域，您可以参考下方章节**跨地域访问KMS实例**。
- 绑定VPC时需要选择一个交换机，请确保交换机下至少有一个可用IP。
- KMS实例每绑定一个VPC，就消耗一个访问管理总量配额。如果您需要提升配额，请参见[升级KMS实例](https://help.aliyun.com/zh/kms/user-guide/manage-kms-instances#6c6e73b014d8y)。

首先您需要通过共享单元将应用账号（KMS实例使用账号）VPC的任意交换机共享给共享服务账号（KMS实例所属账号）

1. 使用应用账号登录[资源共享控制台](https://resourcemanager.console.aliyun.com/resource-share)。
2. 在左侧导航栏，选择**资源共享**>**我的共享**。
3. 在顶部菜单栏左上角处，选择VPC所在的地域。
4. 单击**创建共享单元**。
5. 在**配置基本信息并添加资源**页面，输入共享单元名称，然后选中需要共享的交换机，最后单击**下一步**。
6. 在**关联权限**页面，选择共享权限**AliyunRSDefaultPermissionVSwitch**，然后单击**下一步**。
7. 在**关联资源使用者**页面，添加资源使用者，然后单击**下一步**。在**使用者范围**区域，选择**仅允许资源目录内共享**。在**资源使用者类型**区域，选择**阿里云账号**。填入共享服务账号的账号ID，单击**添加**。
8. 在**确认并提交**页面，单击**确定**。

资源的共享状态变为**已关联**，表明资源已经完成共享。完成共享后，您需要将该VPC绑定到KMS实例上。

1. 使用共享服务账号（KMS实例所属账号）登录[密钥管理服务控制台](https://yundun.console.aliyun.com/?p=kms#/keyList/base)，在顶部菜单栏选择地域后，在左侧导航栏单击**资源 > 实例管理**。
2. 在**实例管理**页面，根据您的KMS实例类型，单击**软件密钥管理**页签或**硬件密钥管理**页签。
3. 定位到目标KMS实例，单击**操作**列的**管理**，在页面最下方单击**多VPC**页签。
4. 单击**配置VPC**，在**配置专有网络**面板**待选专有网络**中，选择应用账号共享过来的VPC，单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970856.png)图标![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970844.png)
5. 在**请选择需要绑定VPC的交换机**对话框中，为每个VPC选择一个交换机，单击**确定**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970860.png)
6. 在**配置专有网络**页面，单击**确定**。

###### 通过VPC互连实现KMS实例的访问（可选）

前提条件：您已经完成了组网，实现了应用账号下需要访问KMS实例的VPC和共享服务账号下KMS实例所在的VPC之间的互通。

出于降低IT服务采购费用的成本考虑，您可以无需购买KMS实例的访问管理数量配额，直接通过云解析 PrivateZone 功能，实现KMS实例的访问。这里建议您还是优先使用KMS产品内置方案，参考上述章节**通过绑定VPC实现KMS实例的访问，**实现KMS实例的访问。

首先您需要获取KMS实例的私网IP：

1. 使用共享服务账号登录[云解析DNS控制台](https://dc.console.aliyun.com/dns/?spm=a2c4g.11186623.0.0.38b444274f96Vu)。
2. 在左侧导航栏单击**PrivateZone**，按照控制台指引开通PrivateZone。如果您已开通过，请跳过本步骤。
3. 在右上角单击**管理配置模式**
4. 单击**云产品域名**页签，选择**秘钥管理服务**或者输入**Zone名称**为**cryptoservice.kms.aliyuncs.com**进行搜索。
5. 定位到目标Zone，单击**操作**列的**查看解析**。
6. 在**解析记录**页面查看并记录**记录值**，即KMS实例的私网IP。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970855.png)

接着您需要使用获取到的KMS实例私网IP，通过PrivateZone在一个或多个VPC中配置KMS实例私有域名映射到其私网IP地址，可以使得您部署到其他VPC的应用访问该KMS实例：

1. 使用目标应用账号登录[云解析DNS控制台](https://dc.console.aliyun.com/dns/)。
2. 点击左侧导航栏中**内网DNS解析（PrivateZone）**，右上角选择**配置管理模式**，然后点击**内置权威**，在此页签下点击**用户域名**。
3. 在**用户域名**页签，点击**添加域名（Zone）**，在对话框中输入内置权威域名（**cryptoservice.kms.aliyuncs.com**），**域名类型**选择**内置权威加速区**，然后点击**确定**。
4. 在**用户域名**页面，选择创建好的域名Zone，在操作列单击**解析记录**。
5. 在**解析记录**页面，单击**添加记录**，输入配置项后单击**确定**。**记录类型**：选择**A**。**主机记录**：填写KMS实例ID。**记录值**：填写KMS实例的私网IP。**TTL值**：缓存时间，数值越小，修改记录各地址生效时间越快，默认为1分钟。您可以根据实际需求修改。
6. 将PrivateZone解析记录关联至应用账号下需要访问KMS实例的VPC。返回到**用户域名**页签，选择创建好的域名Zone，在操作列单击**生效范围设置**。在**域名设置**页签，选择您要关联的VPC，单击**确定**。

配置完成后，您可以进一步验证配置是否成功，在PrivateZone解析记录关联的VPC中的一台ECS上执行`ping ${kms_id}.cryptoservice.kms.aliyuncs.com`命令，如果解析出的私网IP地址与KMS实例私网IP地址相同，则表示配置成功。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970861.png)

#### 跨地域访问KMS实例（可选）

如果您的应用部署在阿里云多个地域的VPC内，您可以通过建立跨地域VPC间连接、云解析PrivateZone功能来实现跨地域访问 KMS 实例，降低企业的管理成本和 IT 采购成本。比如您的KMS实例创建在共享服务账号下的 cn-hangzhou 地域，您的应用账号下的应用跨地域部署在 cn-hangzhou 地域的 `vpc-cn-hangzhou` 和 cn-beijing 地域的 `vpc-cn-beijing`。首先您需要通过上述章节**跨账号访问KMS实例**，实现应用账号下 `vpc-cn-hangzhou`对KMS实例的访问。然后通过本章节，将应用账号下 `vpc-cn-hangzhou`和 `vpc-cn-beijing`进行网络打通并且通过云解析PrivateZone配置域名解析，实现应用账号下 `vpc-cn-beijing`对KMS实例的跨地域访问。

##### 查询KMS实例的私网IP

1. 使用目标应用账号登录[云解析DNS控制台](https://dc.console.aliyun.com/dns/?spm=a2c4g.11186623.0.0.38b444274f96Vu)。
2. 在左侧导航栏单击**PrivateZone**，按照控制台指引开通PrivateZone。如果您已开通过，请跳过本步骤。
3. 在右上角单击**管理配置模式**
4. 单击**云产品域名**页签，选择**秘钥管理服务**或者输入**Zone名称**为**cryptoservice.kms.aliyuncs.com**进行搜索。
5. 定位到目标Zone，单击**操作**列的**查看解析**。
6. 在**解析记录**页面查看并记录**记录值**，即KMS实例的私网IP。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970857.png)

##### 配置VPC间网络互通

VPC之间默认是不互通的，您需要将应用账号下与KMS实例关联的VPC和其他地域的VPC之间建立连接。

阿里云专有网络VPC产品提供了一些产品方案来支持VPC间连接需求，例如云企业网、VPC对等连接可用来实现跨地域、同账号或不同账号的VPC间连接。具体操作，您可以参考如下文档：

- [使用云企业网实现跨地域跨账号VPC互通（基础版）](https://help.aliyun.com/zh/cen/getting-started/use-basic-edition-transit-routers-to-connect-vpcs-across-regions#task-2293645)
- [使用云企业网实现跨地域跨账号VPC互通（企业版）](https://help.aliyun.com/zh/cen/getting-started/use-enterprise-edition-transit-routers-to-connect-vpcs-across-regions-and-accounts)
- [VPC对等连接概述](https://help.aliyun.com/zh/vpc/user-guide/overview-6#concept-2198116)

##### 通过PrivateZone配置域名解析

通过PrivateZone在一个或多个VPC中配置KMS实例私有域名映射到IP地址，可以使得您部署到其他地域的应用访问该KMS实例。接下来演示在应用账号中配置域名解析，从而能访问到共享服务账号的KMS：

1. 使用目标应用账号登录[云解析DNS控制台](https://dc.console.aliyun.com/dns/)。
2. 点击左侧导航栏中**内网DNS解析（PrivateZone）**，右上角选择**配置管理模式**，然后点击**内置权威**，在此页签下点击**用户域名**。
3. 在**用户域名**页签，点击**添加域名（Zone）**，在对话框中输入内置权威域名（**cryptoservice.kms.aliyuncs.com**），**域名类型**选择**内置权威加速区**，然后点击**确定**。
4. 在**用户域名**页面，选择创建好的域名Zone，在操作列单击**解析记录**。
5. 在**解析记录**页面，单击**添加记录**，输入配置项后单击**确定**。**记录类型**：选择**A**。**主机记录**：填写KMS实例ID。**记录值**：填写KMS实例的私网IP。**TTL值**：缓存时间，数值越小，修改记录各地址生效时间越快，默认为1分钟。您可以根据实际需求修改。
6. 将PrivateZone解析记录关联至VPC。返回到**用户域名**页签，选择创建好的域名Zone，在操作列单击**生效范围设置**。在**域名设置**页签，选择您要关联的VPC，单击**确定**。

##### 验证配置是否成功

在[通过PrivateZone配置域名解析](#nidkb)中新关联的VPC中一台ECS上执行`ping ${kms_id}.cryptoservice.kms.aliyuncs.com`命令，如果解析出的私网IP地址与[查询KMS实例的私网IP](#feV9o)中查询到的私网IP地址相同，则表示配置成功。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970846.png)

#### 托管 RAM 凭据

RAM凭据是指RAM用户的访问密钥（AccessKey），包括AccessKey ID和AccessKey Secret，用于RAM用户在调用阿里云API时完成身份验证。在KMS托管RAM凭据后，您无需在应用程序中配置AccessKey，只需配置凭据名称，通过凭据名称获取有效的AccessKey用于调用阿里云API，避免硬编码AccessKey导致泄露。同时RAM凭据也支持轮转，以降低AccessKey泄露的风险。接下来演示如何托管应用账号上RAM用户的AccessKey。

##### 授予KMS管理RAM用户AK的权限

1. 使用应用账号登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 在左侧导航栏，选择**权限管理 > 权限策略**。
3. 在**权限策略**页面，单击**创建权限策略**。
4. 选择**脚本编辑**并输入以下脚本。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ram:ListAccessKeys",
 "ram:CreateAccessKey",
 "ram:DeleteAccessKey",
 "ram:UpdateAccessKey"
 ],
 "Resource": "*"
 }
 ]
}`
5. 单击**继续编辑基本信息**，设置**名称**和备注。其中**名称**设置为**AliyunKMSManagedRAMCrendentialsRolePolicy**。
6. 单击**确定**。
7. 在左侧导航栏，选择**身份管理 > 角色**。
8. 在**角色**页面，单击**创建角色**。
9. 在**创建角色**页面，选择可信实体类型为**阿里云服务**，然后单击**下一步**。
10. 选择角色类型为**普通服务角色**。
11. 输入**角色名称**和**备注**。其中**角色名称**为**AliyunKMSManagedRAMCrendentialsRole**。
12. 选择受信服务为**密钥管理服务**，单击**完成**。
13. 单击**为角色授权**，被授权主体会自动填入。
14. 在**新增授权**面板，选择**自定义策略**，然后选中权限策略**AliyunKMSManagedRAMCrendentialsRolePolicy**，单击**确定**，然后单击**完成**。

##### 创建RAM用户的AccessKey

接下来创建密钥对，如已经创建（已有需要托管的AccessKey ID 和 AccessKey Secret），可跳过此步骤：

1. 使用应用账号登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 在左侧导航栏，选择**身份管理 > 用户**。
3. 在**用户**页面，单击目标RAM用户名称。
4. 在**AccessKey**区域，单击**创建AccessKey**。
5. 根据界面提示完成安全验证。
6. 在**创建AccessKey**对话框，查看AccessKey ID和AccessKey Secret。您可以单击**下载CSV文件**，下载AccessKey信息。单击**复制**，复制AccessKey信息。

##### 创建用户主密钥

在KMS实例中创建用于加密凭据的对称密钥，如已经创建（已有可用的用户主密钥），可跳过此步骤：

1. 使用应用账号登录[密钥管理服务控制台](https://yundun.console.aliyun.com/?p=kms#/keyList/base)，在顶部菜单栏选择地域后，在左侧导航栏单击**资源 > 密钥管理**。
2. 在**密钥管理**页面，单击**用户主密钥**页签，**实例ID**选择软件密钥管理实例，单击**创建密钥**。
3. 在**创建密钥**面板，完成配置项设置，然后单击**确定**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970858.png)

##### 创建RAM凭据

1. 登录[密钥管理服务控制台](https://yundun.console.aliyun.com/?p=kms#/keyList/base)，在顶部菜单栏选择地域后，在左侧导航栏单击**资源 > 凭据管理**。
2. 单击**RAM凭据**页签，选择**实例ID**后，单击**创建凭据**，完成各项配置后单击**确定**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970862.png)

#### 创建KMS应用接入点

应用接入点AAP（Application Access Point）是KMS提供的一种身份验证和访问控制机制，当自建应用使用密钥或凭据时，对其进行身份认证和行为鉴权。出于安全性考虑，建议用户使用接入点的权限策略和网络规则，来缩小暴露面积。

如果您是中心运维团队，需要统一管控KMS应用接入点，您可以使用共享服务账号登录阿里云控制台，完成本章节的配置。如果您需要各个应用账号自治，您可以使用应用账号各自登录阿里云控制台完成配置。

##### 创建网络规则

为了更高的安全性，通常建议您合理设置网络规则，基于来源IP限制访问。如果您需要在云下通过公网访问KMS，请务必设置网络规则，限制公网来源IP。

1. 登录[密钥管理服务控制台](https://yundun.console.aliyun.com/?p=kms#/keyList/base)，在顶部菜单栏选择地域后，在左侧导航栏单击**应用接入 > 接入点**。
2. 单击**网络规则，**然后单击**创建网络规则**。
3. 选择**网络类型**：如果您需要在云下通过公网访问，请选择**Public**如果您在云上VPC内访问，请选择**Private**
4. 填入**允许访问的源IP地址**，单击**确定。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970848.png)

##### 创建权限策略

如果您有多个应用需要复用同一个KMS实例，建议您为每一个应用创建单独的权限策略，进行权限隔离，保证权限的最小化。如果您需要在云下通过公网访问KMS，您也需要创建单独的权限策略，具体操作如下所示：

1. 登录[密钥管理服务控制台](https://yundun.console.aliyun.com/?p=kms#/keyList/base)，在顶部菜单栏选择地域后，在左侧导航栏单击**应用接入 > 接入点**。
2. 单击**权限策略**，然后单击**创建权限策略**。
3. 在**创建权限策略**面板，选择**作用域**：如果您需要在云下通过公网访问，请选择**KMS共享网关**如果您在云上VPC内访问，请选择**具体的KMS实例**
4. 选择**RBAC权限**：如果您需要在云下通过公网访问（即在上一步选择的是**KMS共享网关**作用域），请选择**SecretUser**如果您在云上VPC内访问（即在上一步选择的是**具体的KMS实例**作用域），请选择**CryptoServiceKeyUser**和**CryptoServiceSecretUser**
5. 勾选应用需要访问的密钥和凭据，如果在上一步选择作用域时，您选择的是**KMS共享网关**，那么这里您只需要勾选应用所需的凭据即可
6. 选择**网络控制规则**，您最多可以配置3个网络规则：如果您需要在云下通过公网访问（即在上一步选择的是**KMS共享网关**作用域），请选择[创建网络规则](#IxNUw)中创建的网络类型为**Public**的规则如果您在云上VPC内访问（即在上一步选择的是**具体的KMS实例**作用域），请选择[创建网络规则](#IxNUw)中创建的网络类型为**Private**的规则
7. 单击**确定**，完成创建。

##### 创建应用接入点

如果您有多个应用需要复用同一个KMS实例，建议您为每一个应用创建单独的应用接入点，隔离权限策略和网络规则，缩小暴露面积，保证单一职责原则。

1. 登录[密钥管理服务控制台](https://yundun.console.aliyun.com/?p=kms#/keyList/base)，在顶部菜单栏选择地域后，在左侧导航栏单击**应用接入 > 接入点**。
2. 在**应用接入**页签，单击**创建应用接入点**
3. 在**创建应用接入点**面板，创建模式选择**标准创建**，填写**应用接入点名称**
4. **认证方式**选择**ClientKey**，填写**Client Key加密口令**
5. 选择**权限策略**，您最多可配置3个策略，当您配置了多个权限策略时，只要满足其中一个权限策略，即可通过访问控制的鉴权。因此您可以为接入点同时绑定用于云下公网访问的权限策略和用于云上VPC内访问的权限策略，在云上云下使用同一份接入点配置。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1176581571/p970859.png)
6. 单击**确定**，浏览器会自动下载ClientKey。ClientKey用于对KMS资源访问者进行身份认证和行为鉴权，其包含**应用身份凭证内容（ClientKeyContent）**和**凭证口令（ClientKeyPassword）**。 **应用身份凭证内容（ClientKeyContent）**文件名默认为clientKey_****.json。**凭证口令（ClientKeyPassword）**文件名默认为clientKey_****_Password.txt。请妥善保管该ClientKey。

#### 应用程序集成 RAM 凭据

##### 代码示例

本方案提供了JAVA版本的代码示例，在该代码示例中，会通过SDK获取并使用托管到KMS上的AccessKey。代码地址详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-kms-managed-accesskey/code-example/java)。代码结构如下所示。

```
├── README.md
├── pom.xml
└── src
    ├── config
    │   └── prod-aliyun																					// 云上配置
    │       └── resources
    │           ├── application.properties
    │           └── managed_credentials_providers.properties		// KMS RAM凭据SDK配置文件
    └── main
        ├── java
        │   └── org
        │       └── example
        │           ├── AliyunSdkAKExpireHandler.java
        │           └── Main.java																// 主入口
        └── resources																						// 本地配置
            ├── application.properties
            └── managed_credentials_providers.properties				// KMS RAM凭据SDK配置文件
```

通过Maven的方式在项目中引入KMS RAM凭据SDK。建议您安装最新版本的SDK。

```
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-core</artifactId>
  <version>4.6.4</version>
</dependency>

<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-core-managed-credentials-provider</artifactId>
  <version>1.3.3</version>
</dependency>
```

RAM凭据SDK仅支持通过配置文件方式，配置运行参数。您需要在应用程序的运行目录中新增名为`managed_credentials_providers.properties`的配置文件，云上云下访问KMS所需的配置不同，在代码示例中会通过不同的Profile来区分，在打包时，通过指定Profile来构建相应的应用JAR包：

- 云下：`src/main/resources/managed_credentials_providers.properties`
- 云上：`src/config/prod-aliyun/resources/managed_credentials_providers.properties`

更多代码详情和运行说明，请参见[代码示例](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-kms-managed-accesskey/code-example/java)。

##### 云下集成配置

###### 注入ClientKey文件

将上一章节**创建KMS应用接入点**中，下载的接入点ClientKey文件放到本地项目中，以上述代码示例为例，您可以将ClientKey文件放到`src/main/resources`目录下。请谨慎使用您的ClientKey文件，不要和您的项目代码一起上传到任何公开的代码仓库中，以防泄露。同时强烈建议您，为该应用接入点配置网络规则，限制公网访问IP，参考上面章节[创建网络规则](#IxNUw)。

###### 设置SDK配置文件

云下获取凭证，需要通过KMS服务Endpoint通过公网获取凭据值，`managed_credentials_providers.properties`配置文件示例如下：

```
# 访问凭据类型
credentials_type=client_key

# 读取client key的解密密码：以文件读取为例
client_key_password_from_file_path=#your client key private key password file path#

# Client Key私钥文件路径
client_key_private_key_path=#your client key private key file path#

# 关联的KMS服务地域
cache_client_region_id=[{"regionId":"#regionId#"}]
```

相关配置说明如下：

| 配置项 | 说明 |
| --- | --- |
| cache_client_region_id | KMS实例所在地域ID。 |
| credentials_type | 访问凭据类型 |
| client_key_password_from_file_path | ClientKey文件（JSON格式）的绝对路径或相对路径。 |
| client_key_private_key_path | ClientKeyPassword文件（TXT格式）的绝对路径或相对路径。 |

##### 云上集成配置

###### 下载CA证书文件

KMS实例内置SSL证书，使用SSL/TLS协议用于身份验证和加密通信。

1. 登录[密钥管理服务控制台](https://yundun.console.aliyun.com/?p=kms#/keyList/base)，在顶部菜单栏选择地域后，在左侧导航栏单击**资源 > 实例管理**。
2. 在**应用接入指南**中，单击**获取实例CA证书**区域的**下载**。
3. 完成KMS实例CA证书的下载。

###### 注入ClientKey与CA证书文件

您需要将ClientKey文件和CA证书文件保存到您应用所部署的ECS实例或者容器集群上，这可能需要和您的应用部署或者资源供给的Pipeline进行集成，从而实现这些文件注入的自动化。

如果您的应用部署在容器集群上，本方案提供了通过保密字典和数据卷挂载实现文件注入的方式，供您参考。具体操作步骤如下所示。

1. 登录[容器服务管理控制台](https://cs.console.aliyun.com/)，在左侧导航栏选择**集群**。
2. 在**集群列表**页面，单击目标集群名称，然后在左侧导航栏，选择**工作负载 > 无状态**。
3. 在**无状态**页面中，单击**使用YAML创建资源**。
4. 选择示例模板或自定义，拷贝YAML内容，然后单击**创建**。您可以使用如下YAML示例模板创建保密字典。强烈建议您开启容器Secret的落盘加密，保证加密存储保密字段中的敏感数据，如何开启Secret落盘加密，请参考[使用阿里云KMS进行Secret的落盘加密](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2)。`apiVersion: v1
kind: Secret
metadata:
 name: kms-client-key
type: Opaque
data:
 PrivateKmsCA.pem: LS0t****== # CA证书文件内容，需要用Base64编码
 clientKey.json: ewog****0= # ClientKey身份凭证内容，需要用Base64编码
 clientKey_Password.txt: RWx****E= # ClientKey凭证口令，需要用Base64编码`
5. 接下来，您就可以使用保密字典配置Pod数据卷，将ClientKey与CA证书以文件形式挂载到容器Pod上。如下示例所示，kms-client-key保密字典的`PrivateKmsCA.pem`、`clientKey.json`和`clientKey_Password.txt`以文件方式保存在`/root/resources`目录下。`apiVersion: v1
kind: Pod
metadata:
 name: kms-ram-secret
spec:
 containers:
 - name: nginx
 image: nginx:1.7.9
 volumeMounts:
 - name: clientkey
 mountPath: "/root/resources"
 readOnly: true
 volumes:
 - name: clientkey
 secret:
 secretName: kms-client-key`

###### 设置SDK配置文件

云上获取凭证，需要通过KMS实例Endpoint通过VPC私网获取凭据值。`managed_credentials_providers.properties`配置文件示例如下：

```
cache_client_dkms_config_info=[{"regionId":"<your dkms region>","endpoint":"<your dkms endpoint>","passwordFromFilePath":"< your password file path >","clientKeyFile":"<your Client Key file path>","ignoreSslCerts":false,"caFilePath":"<your CA certificate file path>"}]
```

相关配置说明如下：

| 配置项 | 说明 |
| --- | --- |
| regionId | KMS实例所在地域ID。 |
| endpoint | KMS实例的域名地址，格式为{实例ID}.cryptoservice.kms.aliyuncs.com。 |
| clientKeyFile | ClientKey文件（JSON格式）的绝对路径或相对路径。 |
| passwordFromFilePath | ClientKeyPassword文件（TXT格式）的绝对路径或相对路径。 |
| ignoreSslCerts | 是否忽略KMS实例SSL证书的有效性检查。KMS实例内置SSL证书，使用SSL/TLS协议用于身份验证和加密通信。取值：true：表示忽略，不检查KMS实例SSL证书的有效性。(无需配置caFilePath)false：表示验证，检查KMS实例SSL证书的有效性。正式生产环境中，请将该值设置为false。 |
| caFilePath | KMS实例CA证书文件的绝对路径或相对路径。在**实例管理**页面，单击**获取实例CA证书**区域的**下载**，下载KMS实例的CA证书。 |

##### ClientKey到期更换

ClientKey到期前6个月、3个月、1个月、7天，阿里云会通过短信、邮件、站内信提醒您。您也可以设置云监控告警，在ClientKey到期前的180天、90天、30天、7天，阿里云会为您发送报警通知。详细内容，请参见[告警设置](https://help.aliyun.com/zh/kms/user-guide/alert-settings)。如果您的ClientKey即将到期，请您务必及时更换，否则应用将无法正常访问KMS。如何更换ClientKey，请参考[更换ClientKey](https://help.aliyun.com/zh/kms/user-guide/change-a-client-key)。

## 故障排除

### 为什么在应用账号中看不到被共享的 KMS 实例

如果您将KMS实例通过资源共享的共享单元共享给了其他应用账号，但是在应用账号中，看不到该KMS实例，请检查并进行如下操作步骤：

1. 请检查您的KMS实例，是否有足够的访问管理数量。KMS实例访问管理数量，包含共享KMS实例时资源使用者的数量以及实例关联的VPC数量，例如，您的KMS实例需要关联3个VPC，并共享给2个资源使用者，那么访问管理数量配额最少为5才能满足业务需求。如果您需要提升配额，请参见[升级KMS实例](https://help.aliyun.com/zh/kms/user-guide/manage-kms-instances#6c6e73b014d8y)。
2. 升级KMS实例，保证足够的访问管理数量后，您需要重建共享单元，将该KMS实例重新共享给所需应用账号。

### 为什么应用程序接入KMS报错

应用程序通过SDK接入的常见问题，请参考[应用接入常见问题](https://help.aliyun.com/zh/kms/developer-reference/application-access-faq)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-237（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
