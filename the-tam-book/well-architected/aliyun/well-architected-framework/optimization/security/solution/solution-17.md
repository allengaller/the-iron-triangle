<!-- source: https://help.aliyun.com/zh/well-architected/solution-17 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929413 -->

# 基于云SSO实现多账号单点登录

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971881.png)当企业采用多账号的云上架构时，配置各个账号的人员身份和权限策略将变得非常繁琐耗时。此方案基于云SSO的产品能力，提供一种集中化管理企业多账号的身份权限的方式，简化了企业IT管理人员在身份配置上的复杂度，同时降低了因为身份管理不善导致的身份泄露、权限过大的风险。

## 方案优势

### 集中管理用户身份

借助SCIM协议从您的企业身份管理系统同步用户和用户组到云SSO身份目录中，降低身份管理的复杂度。

### 与企业身份管理系统进行SSO配置

与企业身份管理系统进行单点登录（SSO），以最大限度地优化用户体验，同时降低安全风险。

### 集中配置所有用户对RD账号的访问权限

借助与RD的深度集成，当使用RAM角色访问目标成员账号时，在云SSO中您可以统一配置用户或用户组对整个RD内的任意成员账号的访问权限。根据RD的组织结构，选择不同成员账号为其分配可访问的身份（用户或用户组）以及具体的访问权限，且该权限可以随时修改和删除。

## 客户场景

### 实现与企业身份系统集成登录云控制台

#### 场景描述

多账号场景的企业，客户可以将每个账号内的RAM角色与企业IdP进行集成，并要求企业用户使用SSO方式登录阿里云控制台。

#### 适用客户

企业内已有IdP的用户。

### 多账号下的人员身份统一管理

#### 场景描述

客户拥有一个中心IT或运维团队，需要统一管理云上的多个账号，存在一名员工需要访问多个账号，或多名员工需要访问同一个账号的情况。

#### 适用客户

企业中心IT团队希望实现集中化的身份权限管控。

## 方案架构

本方案会使用阿里云云SSO产品，会天然集成阿里云资源目录RD（Resource Directory）的多账号统一身份管理与访问控制。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971875.png)

### 以RAM角色登录

企业在云SSO集中管理访问阿里云的用户，通过访问配置和多账号授权，实现用户通过单点登录的方式登录到资源目录成员内的RAM角色，然后访问该RD成员中的云资源。优先以RAM角色登录，适用于[支持STS的云服务](https://help.aliyun.com/zh/ram/services-that-work-with-sts)。

### 以RAM用户登录

企业在云SSO集中管理访问阿里云的用户，通过RAM用户同步，实现用户登录到资源目录成员内的RAM用户，然后访问该RD成员中的云资源。以RAM用户登录适用于**不支持RAM角色的云服务**。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971874.png)

例如部分大数据产品、云效等云服务暂不支持RAM角色访问，此时可以使用云SSO的**RAM用户同步**功能，该功能支持在资源目录目标成员账号中快速批量创建与云SSO用户同名的RAM用户，将RAM用户加入大数据产品工作空间、加入云效成为其企业成员、关联云服务内部角色后进行访问。

目前**对RAM用户的授权需要在目标成员账号中操作**，建议将某个云SSO用户设置为权限管理员，专门用来为目标RD账号中同步的RAM用户权限。用户可以在云SSO创建访问配置（包含AliyunRAMFullAccess权限），然后为权限管理员在多个目标RD成员账号上部署该访问配置，实现权限管理员可以为目标RD账号中的RAM用户授权。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云SSO | [云SSO](https://help.aliyun.com/zh/cloudsso/product-overview/what-is-cloudsso)提供基于阿里云资源目录RD（Resource Directory）的多账号统一身份管理与访问控制。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/cloudsso/product-overview/billing-methods)。 |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 访问控制RAM | [访问控制（RAM）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |

### 名词解释

| 多因素认证（MFA） | 多因素认证MFA（Multi-Factor Authentication）是一种简单有效的最佳安全实践，在用户名和密码之外再额外增加一层安全保护。当云SSO用户使用用户名和密码登录时，默认开启多因素认证。目前，云SSO支持MFA设备作为多因素认证方式。更多信息，请参见[管理MFA](https://help.aliyun.com/zh/cloudsso/user-guide/manage-mfa)。 |
| --- | --- |
| 身份同步 | 云SSO服务支持基于SCIM协议的用户和用户组同步，称为身份同步，也可以称其为身份部署或身份推送等。使用身份同步，您只需在您的企业身份管理系统中管理身份，而不必在云SSO中手工管理用户、用户组及其成员关系，提升管理效率和安全性。 |
| 单点登录（SSO） | 云SSO支持基于SAML 2.0的单点登录SSO（Single Sign On）。阿里云是服务提供商（SP），而企业自有的身份管理系统则是身份提供商（IdP）。通过单点登录，企业员工可以使用IdP中的用户身份直接登录云SSO。IdP和SP的具体含义如下：身份提供商IdP（Identity Provider）可以提供身份管理服务。常见的IdP：Microsoft Active Directory Federation Service （AD FS）、Azure AD、Okta以及KeyCloak等。服务提供商SP（Service Provider）是利用IdP的身份管理功能，为用户提供具体服务的应用。SP会使用IdP提供的用户信息。一些非SAML协议的身份系统（例如：OpenID Connect），也把服务提供商称作IdP的信赖方。更多信息，请参见[单点登录概述](https://help.aliyun.com/zh/cloudsso/user-guide/overview)。 |

## 安全性

### 云SSO服务关联角色

服务关联角色（AliyunServiceRoleForCloudSSO）具有操作RAM角色、权限策略和服务提供商等的权限，方便云SSO进行RD统一权限配置。关于服务关联角色的更多信息，请参见[服务关联角色](https://help.aliyun.com/zh/ram/user-guide/service-linked-roles)。

### SAML及SCIM协议

方案中使用业界标准的SAML协议及SCIM协议保障数据安全传递，相关介绍详情[SAML 2.0](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)及[SCIM](http://www.simplecloud.info/)。

### 开启MFA

为提升安全性，建议跟企业IdP集成联合登录，并在IdP侧开启MFA。如果没有跟IdP集成，使用账号密码方式，云SSO默认开启多因子身份认证[MFA](https://help.aliyun.com/zh/account/support/what-is-the-mfa)，建议持续开启，云SSO相应管理操作参见[MFA管理](https://help.aliyun.com/zh/cloudsso/user-guide/manage-mfa)。

## 注意事项

### 云SSO使用限制

云SSO相关限制详情参见[使用限制](https://help.aliyun.com/zh/cloudsso/product-overview/limits)。

## 实施步骤

### 实施准备

客户侧需要有支持SAML协议的身份管理系统（IdP）才能与阿里云进行SSO配置，常见的IdP有：

- ADFS，配置AD及ADFS请查看[链接](https://bp.aliyun.com/detail/88?spm=a2cls.b8387508.0.0.4e784a2125kzbt)。
- OKTA，配置OKTA请查看 [链接](https://www.okta.com/?spm=a2c4g.11186623.2.12.76f553aagHR7RX)。
- AAD，配置AAD请查看 [链接](https://docs.microsoft.com/zh-cn/azure/active-directory/fundamentals/?spm=a2c4g.11186623.2.10.bfb729c8KpCRLC)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：45分钟。

### 操作步骤

分如下几个模块来编写操作过程。

#### 原生身份管理与认证

##### 1. 开通服务，创建目录

使用云SSO的前提是账号需要开通资源目录，只有资源目录管理账号才能使用云SSO服务。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971882.png)

需要具备云SSO服务使用权限，请配置账号对应的RAM权限。

##### 2. 创建目录

首次使用时需要创建云SSO目录，只能创建一个目录。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971876.png)

需要选择一个地域，所有数据只保存在此地域，无任何跨地域数据传输。

##### 3. 用户和用户组管理

这个场景，我们通过控制台直接创建用户和用户组。

- 创建云SSO用户
- 创建云SSO用户组并添加用户

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971884.png)

##### 4. 登录方式配置

云SSO用户将由独立的入口登录（域名为alibabacloudsso.com），需为其设置登录的方式，测试阶段可以先配置为用户名密码登录（默认选项），配置是否需要MFA登录(建议开启)，待IdP侧准备完成后可以参照下一节完成身份集成操作。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971886.png)

为云SSO用户重置密码。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971878.png)

##### 5. 创建访问配置

访问配置是用户访问RD中账号的配置模板，访问配置是一个“模板”，可以用于任意用户对任意账号的访问授权。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971879.png)

##### 6. 授权用户/用户组对RD账号进行访问

**授权的三个要素：**

- 身份：云SSO用户或用户组。
- 权限：访问配置“模板”中规定的权限。
- 资源范围：RD中的某个账号。

**授权的实现机制**

- 将访问配置“模板”中的要素部署（Provision）到相关RD账号中：创建一个SAML Provider用于角色SSO登录。创建一个RAM Role作为RD账号中的访问身份（Identity）。为上述RAM Role绑定系统策略。如果访问配置中有内置策略，则创建一个自定义策略，并与上述RAM Role绑定。

当云SSO用户需要访问RD账号时，发起针对该账号的角色SSO，并以上述RAM Role的身份登录到RD账号中，“授权”即意味着允许此用户使用该RAM Role身份。

**授权的控制台操作步骤**

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971887.png)

- 选择不超过10个RD账号（可以是管理账号或成员账号）。
- 选择不超过10个身份。
- 选择不超过5个访问配置。
- 开始授权，针对每个（账号、身份、访问配置）组合生成一个异步任务，最终完成授权。
- 可以在“历史任务”页面查看所有任务的详情。

**权限的查看**

- 在用户/用户组详情页查看该身份对哪些账号有哪些访问权限。
- 在访问配置详情页查看该访问配置被部署在了哪些账号，以及哪些身份拥有使用此访问配置的权限。
- 在RD账号详情页可以查看哪些身份对此账号有哪些访问权限。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971888.png)

##### 7. 云SSO用户访问阿里云

根据登录方式的配置，使用用户名密码或SSO登录，进入云SSO用户门户。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971880.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971883.png)

根据权限配置，用户可以列出自己有权访问的所有账号列表，并可以进一步列出每个账号中所拥有的权限（即不同的访问配置）及其跳转链接。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971889.png)

点击链接即可以访问配置对应的RAM Role身份进入目标账号的控制台，并获得相应权限。

可以在云SSO用户门户选择其他账号或其他访问配置，但不能与之前的登录同时生效，以最后一次跳转为准。

#### 身份集成

##### 基于SAML协议实现单点登录

云SSO支持基于SAML 2.0的单点登录（SSO登录）。阿里云是服务提供商（SP），而企业自有的身份管理系统则是身份提供商（IdP）。通过SSO登录，企业员工可以使用IdP中的用户身份直接登录云SSO。云SSO可以一次性配置企业身份管理系统与阿里云的SSO登录，配置方式非常简单。

**使用流程**

1. 在企业IdP中配置阿里云为可信SAML SP并进行SAML断言属性的配置（**NameID**）。不同企业IdP的配置方法不同。具体操作，请参见各企业IdP的帮助文档。
2. 在云SSO中配置企业IdP为可信SAML IdP。您需要上传企业IdP元数据文件，并启用SSO登录功能。具体操作，请参见[启用单点登录](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso)。
3. 通过SCIM同步用户或在云SSO中创建IdP的同名用户。如果IdP中有大量用户，且IdP支持SCIM协议，推荐直接将IdP中的用户同步到云SSO，简化后续管理操作。人员离职后，IdP侧人员删除后也会自动同步到云SSO。如果IdP侧同时支持用户组同步，也建议将用户组同步到云SSO，便于后续集中化授权。SCIM同步示例，请参见[通过SCIM同步Azure AD用户或用户组的示例](https://help.aliyun.com/zh/cloudsso/user-guide/synchronize-users-or-groups-in-azure-ad-by-using-scim)。如果IdP侧不支持SCIM协议或者需要访问阿里云侧的人员较少且不经常变动，也可以直接在云SSO创建IdP的同名用户，即将SAML断言属性中的**NameID**值设置为云SSO用户的用户名。具体操作，请参见[创建用户](https://help.aliyun.com/zh/cloudsso/user-guide/perform-basic-operations)。
4. 使用企业IdP的用户SSO登录阿里云。

**集成方式**

- 跟企业的AD FS实现的单点登录，详细配置参见[链接](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso-logon-from-ad-fs-to-cloudsso)。
- 跟企业的AAD实现单点登录，详细配置参见[链接](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso-from-azure-ad-to-cloudsso)。
- 跟企业的Okta实现单点登录，详细配置参见[链接](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso-logon-from-okta-to-cloudsso)。

##### 基于SCIM协议实现用户数据同步

您可以从支持SCIM 2.0的外部IdP同步用户或用户组到云SSO。当IdP中有大量用户，且IdP支持SCIM协议，您可以直接将IdP中的用户同步到云SSO。

**集成方式**

- 通过SCIM同步AAD用户或用户组的数据，详细配置参见[链接](https://help.aliyun.com/zh/cloudsso/user-guide/synchronize-users-or-groups-in-azure-ad-by-using-scim)。
- 通过SCIM同步Okta用户或用户组的数据，详细配置参见[链接](https://help.aliyun.com/zh/cloudsso/user-guide/synchronize-users-or-groups-in-okta-by-using-scim)。
- 通过SCIM同步ADFS用户或用户组的数据，详细操作参见[链接](https://bp.aliyun.com/detail/248)。 目前云SSO还**不支持直接从ADFS中同步数据**，需要编写程序先从ADFS中读取用户或用户组的数据，再通过标准的SCIM协议将数据写入云SSO。

#### CLI登录

如果企业员工有需要使用CLI、本地代码访问阿里云API进行云产品运维管控操作，则推荐通过CLI发起云SSO登录，登录成功后，会自动获得一个临时访问凭据STS Token用于访问阿里云API。使用该方式无需单独为员工创建固定AccessKey，降低固定AccessKey泄漏风险。

**通过CLI发起云SSO登录**详情参考[链接](https://help.aliyun.com/zh/cloudsso/user-guide/use-alibaba-cloud-cli-to-access-cloudsso-and-alibaba-cloud-resources)。

#### 存量RAM用户迁移到云SSO

很多企业目前仍在大量使用RAM用户作为访问阿里云资源的身份，往往面临这一些挑战，例如：

- 管理复杂：多个账号需要分别独立管理用户，包括用户名、密码、权限等，如果要配置单点登录（SSO），也需要每个账号逐个配置。账号越多，管理越复杂。
- 安全性不易保障：例如一个用户离职，需要到多个账号中删除RAM用户，如果遗漏就会造成安全隐患。
- 使用效率较低且容易出错：如果一个用户需要访问多个账号执行操作，需要频繁退出登录，再换用其他用户名重新登录到其他账号。

使用云SSO可以较好的解决上述问题，但是对很多已经习惯使用RAM用户的企业来说，需要一条平滑的迁移路径。这里介绍迁移的最佳实践，企业可以根据自身需要进行定制。

注：为程序使用而创建的，且持有AccessKey的RAM用户无需迁移。但如果AccessKey是为了人员使用CLI，则可以迁移（人员使用参考上面CLI登录一节）。

##### 1. 中心运维、安全团队人员迁移

一般，企业的中心运维和安全等团队负责管理所有云账号的基础运维、安全防护等，每位成员都需要访问多个云账号，并且有比较固定的权限（如AdministratorAccess，AliyunYundunFullAccess等），因此可以较为容易的迁移到云SSO。具体的迁移步骤为：

1. 首先按照(5.1) - (5.3)的步骤搭建云SSO系统，并为运维和安全团队成员创建用户、用户组，根据角色不同创建访问配置，为用户组绑定相应的访问配置（授权为所有账号），然后将用户添加到对应用户组中。
2. 这类人员开始使用云SSO访问云资源，包括控制台登录和CLI。保留原RAM用户备用。
3. 待使用稳定后，清理散落在多个账号中的这些人员使用的RAM用户。清理方案：先禁用控制台登录， 静默一段时期后（如1个月）后删除这些账号。

##### 2. 按照业务团队逐个迁移

如果RAM用户较多，整体迁移工作量太大，建议按照业务团队逐个进行迁移。迁移的步骤包括：

1. 人员梳理。梳理团队成员，统一创建云SSO用户或通过SCIM进行用户同步，可以将所有需要相同权限的用户放在同一个用户组中。
2. 权限梳理。根据不同的人员角色创建访问配置，并针对用户和用户组，在对应账号上配置访问权限。如果企业的每个业务团队或项目使用不同的阿里云账号，那么人员在这些账号中的权限设置相对比较简单，通常只需要使用系统策略即可完成。因此，只要将不同人员划分为不同角色，并按照角色创建访问配置，使用系统策略和内置策略授予合适的权限，即可较为简单的完成授权工作。如果企业有较为复杂的权限设计，可能不能简单的进行迁移，详情在下面“限制条件”章节进行讨论。
3. 如果企业使用的产品中有部分需要单独设置权限，例如容器服务、MaxCompute等，需要将访问配置部署到对应账号中，并在这些产品中针对访问配置部署后的角色（命名格式为AliyunReservedSSO_<访问配置名称>）进行授权。
4. 与步骤1类似，该团队人员开始使用云SSO访问云资源，并逐步禁用和删除原RAM用户。

限制条件：在以下情况下，可能需要额外步骤

- 由于历史原因，部分企业有多个业务团队共用一个阿里云账号，并对不同人员进行资源实例维度的精细化权限控制。这时人员角色无法进行统一划分，只能为每个用户对应创建一个访问配置，并添加与该用户完全对等的权限。由于访问配置可以支持的内置策略数量和长度有限，企业需要确认是否能够满足所有人员的精细化管理要求，只有确保可行时才进行迁移。不过，对这类企业我们建议先采用资源组、资源标签等方式调整资源管理方式，减少大量使用自定义权限，再进行云SSO迁移，不建议直接迁移。
- 云SSO的授权范围是一个云账号，如果在迁移过程中，还需要保留在资源组范围内的授权，需要使用以下步骤：在云SSO的访问配置中，使用内置策略并添加acs:ResourceGroupId条件来提供针对某个具体资源组的权限控制。例如下面是授权访问某个资源组下的ECS资源的内置策略。

```
{    
    "Version": "1",
    "Statement": [
        {
         
            "Action": "ecs:*",
            "Resource": "*",
            "Effect": "Allow",
            "Condition": {
                "StringEquals": {
                    "acs:ResourceGroupId": "rg-aek2bfc33wn****"
                }
            }
        }
    ]
}
```

- 使用该访问配置在资源组所在的账号上进行授权，那么被授权的用户将只在资源组范围内拥有权限。同时此访问配置无法用于其他账号。因此建议在访问配置命名时使用特定规则，标注该访问配置适用的账号和资源组。如 `RDSAdmin-账号ID（或对应业务名）-资源组名`。
- 需要注意，在此访问配置中不能同时再添加AliyunECSFullAccess系统策略，否则账号级权限将会覆盖资源组权限。
- 如果企业使用的产品中有部分不支持RAM角色访问（支持RAM角色访问的产品列表详见[文档](https://help.aliyun.com/zh/ram/services-that-work-with-sts)），使用这部分产品的人员参考下文**RAM角色跟RAM用户共存场景。**

##### 3. 清理残留权限

当所有可迁移的RAM用户都已经迁移到云SSO，并且已经删除后，在所有账号下进行清理工作，以免后续被误用：

1. 删除所有不存在任何用户的用户组。
2. 删除所有未绑定任何用户或用户组的自定义策略。

#### RAM角色跟RAM用户共存场景

企业里面购买了像云效、QuickBI这样的SaaS产品，目前只支持使用RAM用户访问，账号内会出现RAM角色跟RAM用户共存的场景。针对这种SSO场景我们的方案推荐的做法是：

- 在未出现这类产品的云账号内使用RAM角色，统一在云SSO中管理。
- 针对出现这类产品的云账号使用云SSO的[RAM用户同步](https://help.aliyun.com/zh/cloudsso/user-guide/overview-of-a-ram-user-provisioning)功能，拥有云SSO用户后，RAM用户同步功能可以批量快速在目标账号中创建与云SSO用户同名的RAM用户，授予相应权限后，在云SSO中实现以RAM用户登录目标账号并访问云服务。

下面介绍如何使用云SSO的RAM用户同步功能，通过云SSO实现RAM用户登录访问相关账号。本文提供一个示例，通过配置RAM用户同步，在RD成员（Sandbox Account）中创建一个与云SSO用户（user1）同名的RAM用户（user1@xxx.onaliyun.com），然后为RAM用户（user1@xxx.onaliyun.com）授予云原生大数据计算服务MaxCompute的管理权限（AliyunMaxComputeFullAccess），实现通过RAM用户（user1@xxx.onaliyun.com）身份访问RD成员（Sandbox Account）中的云原生大数据计算服务MaxCompute。

##### 1. 配置RAM用户同步

使用RD管理账号在云SSO中配置RAM用户同步。

1. 登录[云SSO控制台](https://cloudsso.console.aliyun.com/)。
2. 在左侧导航栏，单击**多账号权限配置**。
3. 在**多账号权限配置**页面，选择目标RD账号。本示例中，选择RD成员（Sandbox Account）。
4. 单击**配置RAM用户同步**。
5. 在**配置RAM用户同步**面板，选择目标用户或用户组，然后单击**下一步**。本示例中，选择云SSO用户（user1）。
6. 设置以下基本信息，然后单击**下一步**。输入RAM用户同步的描述。配置**冲突策略**和**删除策略**。您可以将**处理模式**设置为**逐条处理**或**批量处理**，表示为多个RD账号逐个配置或统一配置冲突策略和删除策略。需要配置的具体策略项如下：**冲突策略**：当目标RD账号内存在同名RAM用户时的处理策略。**替换**：新创建的RAM用户会覆盖已存在的RAM用户。**两者都保留**：新创建的RAM用户会被系统重命名，新旧两个RAM用户会同时保留。**删除策略**：删除RAM用户同步时，对已同步的RAM用户的处理策略。**保留**：删除RAM用户同步时，会保留已同步的RAM用户。**删除**：删除RAM用户同步时，会删除已同步的RAM用户。
7. 在**处理模式**区域，选择**逐条处理**或**批量处理**。**逐条处理**：为多个RD账号逐条配置冲突策略和删除策略。**批量处理**：为多个RD账号统一配置冲突策略和删除。
8. 单击**提交**。
9. 单击**完成**。配置成功后，会在目标RD账号内创建一个同名的RAM用户。本示例中，将会在RD成员（Sandbox Account）中同步创建一个与云SSO用户（user1）同名的RAM用户（user1@xxx.onaliyun.com）。

##### 2. 为RAM用户授权

访问RD成员（Sandbox Account），为RAM用户（user1@xxx.onaliyun.com）授予云原生大数据计算服务MaxCompute的管理权限（AliyunMaxComputeFullAccess）。

1. 访问RD成员（Sandbox Account）。具体操作，请参见[访问成员](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/use-a-member-to-log-on-to-the-alibaba-cloud-management-console)。
2. 为RAM用户（user1@xxx.onaliyun.com）授权。本示例中，将授予RAM用户（user1@xxx.onaliyun.com）云原生大数据计算服务MaxCompute的管理权限（AliyunMaxComputeFullAccess）。具体操作，请参见[为RAM用户授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-the-ram-user)。

除上述操作方法外，为了方便您的操作，推荐您将某个云SSO用户设置为权限管理员，专门用来为目标RD账号中同步的RAM用户权限。您可以在云SSO创建访问配置（包含AliyunRAMFullAccess权限），然后为权限管理员在多个目标RD成员账号上部署该访问配置，实现权限管理员可以为目标RD账号中的RAM用户授权。具体操作，请参见[创建访问配置](https://help.aliyun.com/zh/cloudsso/user-guide/create-an-access-configuration)和[在RD账号上授权](https://help.aliyun.com/zh/cloudsso/user-guide/assign-access-permissions-on-the-accounts-in-a-resource-directory)。

##### 3. 云SSO用户访问阿里云

云SSO用户（user1）通过RAM用户（user1@xxx.onaliyun.com）身份访问RD成员（Sandbox Account）中的云原生大数据计算服务MaxCompute。

1. 云SSO用户（user1）登录云SSO用户门户。具体操作，请参见[步骤一：获取用户门户访问地址](https://help.aliyun.com/zh/cloudsso/user-guide/log-on-to-the-cloudsso-user-portal-and-access-alibaba-cloud-resources)和[步骤二：登录云SSO用户门户](https://help.aliyun.com/zh/cloudsso/user-guide/log-on-to-the-cloudsso-user-portal-and-access-alibaba-cloud-resources)。
2. 以RAM用户身份访问RD成员（Sandbox Account）中的云原生大数据计算服务MaxCompute。具体操作，请参见步骤三：访问RD账号资源中的[以RAM用户登录](https://help.aliyun.com/zh/cloudsso/user-guide/log-on-to-the-cloudsso-user-portal-and-access-alibaba-cloud-resources)章节。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5866581571/p971885.png)

## 相关内容

- [RAM角色集成企业AD FS身份认证](https://bp.aliyun.com/detail/88)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-17（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
