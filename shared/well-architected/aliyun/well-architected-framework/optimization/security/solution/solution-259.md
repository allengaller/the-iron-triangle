<!-- source: https://help.aliyun.com/zh/well-architected/solution-259 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929046 -->

# 通过IDaaS实现堡垒机用户集中管理

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968888.png)

使用[堡垒机](https://help.aliyun.com/zh/bh/bastionhost/product-overview/what-is-bastionhost)进行多账号主机统一运维方案，可以帮助多账号的企业从统一运维入口管理云主机，但是部分企业使用的IdP（比如Okta）不支持直接和堡垒机做多账号集成，影响对多账号主机的统一运维。本文档介绍了使用IDaaS将用户同步到堡垒机中做多账号统一管理的方法，提升云上运维效率和整体安全性。

## 方案优势

本方案能够帮助企业通过IDaaS实现IdP到堡垒机的多用户集中管理，对多账号主机进行统一运维，满足运维的安全、效率、可观测可管控等多方位需求。

### 自动化用户身份同步

通过阿里云IDaaS与企业身份提供商（如Okta、AD）的集成，利用标准协议（如SAML、OAuth2.0）认证用户，并在IDaaS控制台内设定详细的同步策略，包括同步范围、模式和触发条件，从而实现高效的身份数据自动化流转。对于新用户可以自动绑定/创建账户，减少手动创建新员工账户的时间成本和可能的安全风险。

### 用户身份统一管理

通过IDaaS和企业IdP的集成实现企业多账号的统一管理，IdP用户信息同步后，不需要单独新建用户，IDaaS支持增量同步，企业在IdP中能够对用户身份进行统一管理，提升云上身份管理效率。

### 精细化管理权限

同步至IDaaS的用户及用户组可以在堡垒机端进一步细化其访问权限，利用内置的角色管理和授权机制，为不同角色分配合适的权限级别，确保只有经过授权的操作才能被执行，从而实现统一且精细的用户身份管理。

## 客户场景

### 通过IDaaS实现堡垒机用户集中管理

#### 场景描述

企业需要通过堡垒机实现多账号下的ECS统一运维管理，而用户使用堡垒机需要创建RAM用户或者手动将用户导入到堡垒机中，这样操作一方面无法做集中化管理，另一方面增加新员工需要重新创建新的RAM用户和分配用户名密码，存在安全风险。

#### 适用客户

- 有自己IdP的企业用户
- 使用堡垒机的用户

### 客户背景

某全球领先的多元化娱乐和媒体集团，业务涵盖主题公园、影视娱乐、媒体网络、消费品等多个领域。

### 客户诉求

对于有多个阿里云账号并且希望利用阿里云堡垒机实现多账号主机统一运维的客户，之前对于员工的流动需要手动创建/删除RAM用户来登录堡垒机，需要使用/删除相应的用户名和密码，存在安全风险，客户希望能够通过自己的第三方企业管理IdP和阿里云的产品进行集成，实现统一的认证和人员身份管理，使得员工可以通过自己的企业IdP账号密码登录堡垒机进行主机运维管理。

### 实施方案

- 使用IDaaS实现客户IdP和阿里云的堡垒机做集成，实现用户同步和多账号云主机的统一管理。
- 在IDaaS中设置同步策略，对用户进行细粒度的访问权限配置，防止非合规运维操作，并通过堡垒机的日志监控运维状态。

### 客户收益

- 通过IDaaS自动同步用户信息，降低管理成本和手动操作带来的延迟和操作错误。
- 过IDaaS集中管理用户身份，确保所有用户信息的一致性和准确性，结合堡垒机的权限管理功能，实现对用户的细粒度权限分配，防止越权访问和高危操作。

## 方案架构

本方案通过阿里云IDaaS实现企业IdP（如Okta、AD等）与堡垒机之间的用户同步，从而支持多账号主机的统一运维管理。该流程首先需要企业将其使用的身份提供商（IdP），例如Okta或Active Directory (AD)，与阿里云IDaaS进行集成。这一步骤可以通过IDaaS提供的标准协议（如SAML、OAuth2.0等）完成。在IDaaS中配置相应的连接器，确保能够正确地从IdP获取用户信息。管理员在IDaaS控制台内设置同步策略，包括但不限于同步范围（哪些用户/组）、同步模式（全量同步还是增量同步）、触发条件（定时任务或事件驱动）以及具体的同步规则。配置完成后，IDaaS将根据设定的策略自动执行用户数据从IdP到IDaaS的同步操作。对于已经同步至IDaaS中的用户及用户组，在堡垒机端进一步细化其对特定资产的访问权限。利用堡垒机内置的角色管理和授权机制，为不同角色分配合适的权限级别，确保只有经过授权的操作才能被执行。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968885.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云身份服务IDaaS | [云身份服务 IDaaS](https://help.aliyun.com/zh/idaas/eiam/product-overview/what-is-idaas)（英文名：Alibaba Cloud IDentity as a Service，简称 IDaaS）是阿里云为企业用户提供的云原生的、经济的、便捷的、标准的身份、权限管理体系。 | 分为免费版和企业收费版，详情参见[产品计费](https://help.aliyun.com/zh/idaas/eiam/product-overview/pricing)。 |
| 堡垒机 | [堡垒机](https://help.aliyun.com/zh/bh/bastionhost/product-overview/what-is-bastionhost)是阿里云提供的核心系统运维和安全审计的管控平台，可集中管理资产权限，全程管控操作行为，实时还原运维场景，保障云端运维行为身份可鉴别、权限可管控、操作可审计，解决众多资产难管理、运维职责权限不清晰以及运维事件难追溯等问题， 助力企业满足等保合规需求。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/bh/bastionhost/product-overview/pricing/)。 |
| RAM | [访问控制（RAM）](https://help.aliyun.com/product/28625.html)是阿里云提供的一项管理用户身份与资源访问权限的服务。使用RAM，您可以创建、管理RAM角色（例如员工、系统或应用程序），并可以控制这些RAM角色对资源的操作权限。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |
| 资源目录 | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| IdP | Identity Provider，身份提供方。源自于 SAML 协议中定义，IdP 为进行用户认证、鉴权，并返回 SAML Response 结果信息给 SP 的身份提供方，后通用化指统一身份管理平台。 |
| OIDC | OpenID Connect (OIDC) 是一种基于OAuth 2.0协议的身份验证层。它允许客户端应用程序对最终用户进行身份验证，并从身份提供者（IdP）获取基本的用户信息。OIDC通过在OAuth 2.0之上添加一个身份层来实现这一点，从而使得应用能够验证用户的身份并获取其基本信息，如用户名、电子邮件地址等。OIDC定义了一组标准的声明（claims），这些声明描述了用户的属性，例如姓名、电子邮件地址等。此外，它还支持多种认证流程，包括授权码流（Authorization Code Flow）、隐式流（Implicit Flow）等，以适应不同的应用场景需求。 |
| SCIM | System for Cross-domain Identity Management，跨域身份管理系统，专用于不同系统之间账户、组织同步的国际通用规范，国内外有大量应用支持接收 SCIM 协议同步请求，以实现不同系统身份的互用性。 |
| Okta | Okta 是一家提供企业级身份管理服务的公司，主要功能包括单点登录（SSO）、多因素认证（MFA）、生命周期管理和API访问管理等。Okta帮助企业管理和保护员工及客户的身份信息，并支持与各种云服务、本地应用以及其他第三方系统的集成。Okta也可以作为OIDC的身份提供商（IdP）使用。 |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |

## 安全性

通过将企业的IdP（如Okta、AD等）与IDaaS集成，这种集中化的管理方式减少了多点登录的风险，确保了用户身份的一致性和准确性。在IDaaS中配置细粒度的访问权限策略，确保每个用户或用户组只能访问其被授权的资源。通过这种方式，可以有效防止越权行为和非合规运维操作。堡垒机支持基于角色的访问控制（RBAC），管理员可以根据业务需求定义不同的角色，并为每个角色分配相应的权限。这样可以灵活地管理用户的访问权限，同时保持系统的安全性和可维护性。

### 运维安全

堡垒机**基础版**具备基础的运维审计能力，如双因子认证、运维授权、高危命令阻断、运维审计等功能，可满足中小企业的基础运维安全及网络安全等级保护合规需求。**高可用版**适用于对运维业务安全要求较高或业务规模较大的企业，如政企、金融、游戏、在线教育、技术开发等。高可用版除具有基础版的基础运维安全能力外，还可满足更高的业务运维安全需求，详情参见[功能特性](https://help.aliyun.com/zh/bh/bastionhost/product-overview/functions-and-features)。

建议开启堡垒机双因子认证提升安全性，详情参见[开启双因子认证](https://help.aliyun.com/zh/bh/bastionhost/user-guide/enable-two-factor-authentication)。

### 云资源授权

首次使用堡垒机服务前，需要先完成允许堡垒机访问云资源的授权，堡垒机需要访问云服务器ECS和专有网络VPC等云服务的资源，详情参见[授权堡垒机访问云资源](https://help.aliyun.com/zh/bh/bastionhost/user-guide/authorize-bastionhost-to-access-cloud-resources)。

### IDaaS安全性

IDaaS采用“默认安全”的产品设计，在“可用性”和“安全性”难以两全的场景中，IDaaS 会优先保障“安全性”，在此基础上，尽可能追求“易用性”，详情参见[IDaaS默认安全设计](https://help.aliyun.com/zh/idaas/eiam/product-overview/default-security-solutions)。

### SAML及SCIM协议

方案中使用业界标准的SAML协议及SCIM协议保障数据安全传递，相关介绍详情[SAML 2.0](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)及[SCIM](http://www.simplecloud.info/)。

## 注意事项

### 堡垒机版本

堡垒机分为基础版及高可用版，请根据实际情况进行选择，详情参见[功能特性](https://help.aliyun.com/zh/bh/bastionhost/product-overview/functions-and-features)。

### 服务条款

使用堡垒机前请先了解相应的服务条款，详情参见[堡垒机服务条款](https://help.aliyun.com/zh/bh/bastionhost/support/bastionhost-terms-of-service)。

### IDaaS版本

IDaaS EIAM 2.0分为免费版和企业版，使用前请先了解不同版本的功能特性，生产环境建议使用企业版，详情参见[IDaaS版本](https://help.aliyun.com/zh/idaas/eiam/product-overview/pricing)。

## 实施步骤

本方案实施步骤以Okta为例，企业如果使用的是其他支持OIDC协议的IDP，操作步骤类似。

### 实施准备

- 确保创建IDaaS实例，本示例使用免费版，详情可参见[免费开通实例](https://help.aliyun.com/zh/idaas/eiam/user-guide/eiam-sso-quick-start)。
- 以Okta为例，确保已经创建Okta账户和实例，本方案后续以开发者实例为例，详情可以参考[Okta Developer](https://developer.okta.com/signup/) 。
- 按照Landing Zone推荐账号架构进行部署，已完成下列部署：账号类型部署内容共享服务账号/运维账号创建运维VPC及交换机。购买堡垒机。配置CEN，加载网络实例、与业务账号网络连通。业务账号开通并创建业务VPC。开通并创建ECS。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：30分钟。

### 操作步骤

#### 在IDaas身份提供方绑定Okta

1. 使用共享服务账号在[IDaaS控制台中](https://yundun.console.aliyun.com/?p=idaas#/overview/new/cn-hangzhou)单击已创建的**实例ID**或者单击操作列中的**访问控制台**，进入**云身份服务**控制台。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968887.png)
2. 在身份提供方菜单中单击**其他身份提供方-OIDC身份提供方**，开始绑定流程。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968886.png)
3. 填写**显示名称**，**认证模式**选择任意一个均可。PKCE是额外的安全验证，您可以选择性勾选，Okta PKCE的Code Challenge生成方式仅支持SHA256。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968890.png)
4. 在表单最下方**复制IDaaS 授权回调 Redirect URI**。Okta将向该地址发送认证请求和ID token。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968889.png)

##### 创建Okta应用

1. 企业管理员在Okta中登录**管理门户（admin）。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968892.png)
2. 在**应用（Applications）**菜单中，单击创建**应用集成（Create App Integration）。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968893.png)
3. **单点登录方式（Sign-in method）**选择**OIDC-OpenID Connect**，应用类型（Application type）选择网页应用**（Web Application）**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968891.png)
4. 在登录**重定向地址（Sign-in redirect URIs）**中，填入前面步骤中复制的**IDaaS 授权回调 Redirect URI**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968895.png)
5. 在**访问控制（Controlled access）**中设置应用的访问权限，如果用于测试或无特殊的管控需求，可选择所有人均可访问（Allow everyone in your organization to access）。如果选择其他选项，则需要为用户或组授权。确认无误后，单击保存（Save）。保存后将自动进入应用详情页。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968894.png)

##### 填写OIDC身份提供方信息

1. 在Okta应用详情页中获取如下信息，填入到IDaaS绑定 OIDC 身份提供方表单中。**Client ID：**在通用（General）选项卡中，单击复制Client ID，填写到IDaaS表单中。如果在第一步中勾选了**PKCE**，则需要在Okta中勾选Require PKCE as additional verification。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968897.png)**Client Secret：**依然在通用（General）选项卡中，单击复制Client Secret，填写到IDaaS表单中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968898.png)**Issuer：**在登录（Sign On）选项卡中，下滑找到**OpenID Connect ID Token，**单击编辑（Edit），将Issuer修改为Okta URL，并复制该地址，填写到IDaaS表单中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968896.png)在IDaaS表单中单击**解析Issuer**，即可自动填充各端点信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968901.png)确认无误后，单击**下一步**，进入选择场景流程。

##### 选择场景

在**选择场景**中，可以选择需要使用的能力，推荐开启自动绑定账户功能，当有新员工加入时，可以只给新员工配置基于企业IdP的登录方式，新用户通过OIDC登录IDaaS的时候，会自动创建新账户。

- **联邦认证**：开启后，用户可以使用OIDC登录方式登录到IDaaS。
- **手动绑定账户**：开启后，用户使用OIDC登录IDaaS时，如果当前OIDC账户未绑定IDaaS账户，可手动使用其他登录方式验证IDaaS账户。绑定成功后，之后可使用该 OIDC账户登录IDaaS。
- **自动绑定账户**：开启后，用户使用OIDC登录IDaaS时，如果当前OIDC账户未绑定IDaaS账户，且IDaaS字段与OIDC账户字段的值相同，则自动绑定账户。您可以使用**选择字段**，直接选择`id_token`里的某个字段，也可以使用表达式自定义字段（详情参考[高级：账户字段表达式](https://help.aliyun.com/zh/idaas/eiam/use-cases/use-advanced-expressions-in-sso-attributes)）。绑定成功后，之后可使用该OIDC账户登录 IDaaS。
- **自动创建账户：**通过OIDC登录时，如果OIDC账户未绑定IDaaS账户，可自动创建IDaaS账户。每次通过OIDC登录都将更新账户信息。
- **指定账户的组织**： 通过OIDC登录时，没有所属组织的IDaaS账户将自动归属于该组织。该字段在配置时默认选择根组织，您可搜索或下拉选择组织。
- **自动更新信息**：用户使用OIDC登录时，根据字段映射自动更新IDaaS账户信息。

确认无误后，单击**确定**，即可创建OIDC身份提供方。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968902.png)

##### 字段映射（可选）

开启自动创建账户后，用户通过OIDC登录时可以使用`id_token`中的字段数据作为IDaaS账户的字段值，实现IDaaS账户字段值的自动修改。例如将`id_token`中的 `name`作为IDaaS账户的显示。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968899.png)

##### 用户登录流程

完成后面的IDaaS和堡垒机的集成配置之后，运维人员使用运维账号可以通过堡垒机的运维门户登录。在[堡垒机控制台](https://yundun.console.aliyun.com/?p=bastion)顶部菜单栏，选择堡垒机所在的地域，然后在堡垒机实例列表，定位到目标实例，单击**管理**。在**概览**页面，获取运维门户地址。然后通过配置的

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968904.png)

在浏览器中，输入获取到的运维门户地址，在**云盾堡垒机**登录页面，输入IDaaS用户的用户名和密码进行登录。因为配置了Okta，可以在登录时看到该登录方式。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968900.png)

单击登录方式后，将前往Okta进行验证。如果Okta账号未登录，则出现登录页面；如果已登录，则重定向至IDaaS。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968905.png)

#### 多账号统一管理

##### 通过成员账号管理

1. 管理账号需要开启**资源目录功能**，登录[资源管理控制台](https://resourcemanager.console.aliyun.com/overview)，在资源目录中创建新的成员账号，或者将已有的账号添加到资源目录。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968906.png)
2. 在**可信服务**里找到**【堡垒机】**，点击**管理**，为堡垒机委派管理员，委派管理员账号下的堡垒机中可以导入成员账号下的资产（例如ECS、RDS实例等）。导入成员账号资产详见后续步骤。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968907.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968908.png)

##### 通过RAM用户管理

1. 如果通过RAM用户管理堡垒机，需要创建相应的**RAM用户**并做授权。在[RAM控制台](https://ram.console.aliyun.com/overview?activeTab=overview)的左侧导航栏，选择**身份管理> 用户**；可以创建一个新用户来负责管理，也可以对已有账号授予相应的权限。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968903.png)
2. 选择要授予权限的**RAM用户右侧>添加权限。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968909.png)
3. 在**添加权限面板**，为堡垒机RAM用户添加权限。选择授权应用范围，授权主体和相应的权限（**管理、只读、堡垒机运维员、堡垒机审计员**）。
4. ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968910.png)

#### 堡垒机和IDaaS多账号同步

1. 使用共享服务账号进入[堡垒机控制台](https://yundun.console.aliyun.com/?spm=5176.28366559.console-base_search-panel.dtab-product_bastionhost.211e336a0M6Gnv&p=bastion#/overview/cn-hangzhou)，根据需要选择基础版&企业双擎版 或者 开发者版& 轻量版；考虑多可用区情况，推荐使用**基础版&企业双擎版**。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968911.png)

1. **购买堡垒机实例**后，首次登录堡垒机控制台时，堡垒机页面会提示**创建服务关联角色**的流程。当单击确认创建后，阿里云将自动创建**堡垒机服务关联角色AliyunServiceRoleForBastionhost**；点击确认创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968914.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968912.png)
2. 选择**启用实例**，并在启用面板，配置启动项选择**专有网络、交换机和安全。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968915.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968916.png)**【专有网络】**建议堡垒机实例与被运维的ECS使用同一个专有网络，保证内网连通。**【交换机】**主可用区交换机和备可用区交换机需要在**同一个专有网络下的不同可用区**，基础版实例会占用交换机3个可用IP，在选择交换机时，需**保证交换机有足够的可用IP。****【安全组】**堡垒机至少要加入一个普通安全组后才能启用，堡垒机加入普通安全组后会自动生成访问规则，允许堡垒机访问该安全组内的ECS资产。
3. **启动成功，**堡垒机实例的**初始化需要10-15min。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968913.png)
4. 实例启动成功之后，点击右上角**【管理】**进入堡垒机控制台。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968918.png)
5. 在控制台左侧目录栏选择**【系统设置】**，然后选择根据需要选择**IDaaS认证或AD/LDAP认证，**本次选择IDaaS，选择**绑定前面创建的实例**，可以选择**同步范围、SSO发起方**等设置。绑定IDaaS实例后，可前往[IDaaS控制台](https://yundun.console.aliyun.com/?spm=5176.28366559.console-base_search-panel.dtab-product_idaas.211e336a0M6Gnv&p=idaas#/overview/new/cn-hangzhou)配置将**IDaaS账户一键推送到堡垒机**，或在**人员管理-用户页**手动将IDaaS导入到堡垒机。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968919.png)
6. 同步成功之后，可以在左侧导航栏的**【人员管理】-【用户】**中查看同步情况，因为IDaaS同步有时间间隔，也可以**手动导入**RAM用户和其他身份提供商的用户。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968920.png)
7. 在左侧导航栏的**【资产管理】**中可以做各种云资源的导入，包括ECS、数据库等；以ECS为例，可以导入该账号下的所有实例，支持按照地域搜索；也可以选择其他来源导入。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968921.png)
8. 在**【人员管理】-【用户】**下面可以选择给不同的用户授权可以管理的云资源。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9866581571/p968917.png)

## 故障排除

### 堡垒机问题

堡垒机常见问题详情参见[售前常见问题](https://help.aliyun.com/zh/bh/faq-1)及[功能使用常见问题](https://help.aliyun.com/zh/document_detail/71375.html)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-259（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
