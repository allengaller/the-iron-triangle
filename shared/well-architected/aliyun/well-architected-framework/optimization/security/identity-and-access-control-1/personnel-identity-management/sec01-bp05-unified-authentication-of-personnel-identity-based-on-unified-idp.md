<!-- source: https://help.aliyun.com/zh/well-architected/sec01-bp05-unified-authentication-of-personnel-identity-based-on-unified-idp -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706143 -->

# 基于统一的IdP实现人员身份的统一认证

通过集中化的身份提供商（Identity Provider，简称 IdP）来进行人员身份的统一认证，能够简化人员身份的管理，确保组织内在云上、云下的人员身份的一致性。当人员结构变更、人员入、离职时，能够在一个地方完成人员身份的配置。 对于云环境的使用者来说，也无需为其颁发额外的用户名和密码（如 RAM 用户名和密码），只需要保管好其在组织内的 IdP 中的身份和凭据即可。对于一些组织而言，通过一些网络上的访问控制措施，使其 IdP 仅能够在企业内网访问，给人员身份的认证过程增加了额外一个限制条件，进一步保障了企业人员身份的安全。

## 优先级

高

## 不推荐做法

- 不使用联合身份验证和单点登录。员工需要在云上创建单独的用户和登录密码凭证，增加密码泄露风险。
- 未实现员工身份的自动化生平周期管理。例如，当员工离职时，您需要手动删除其在云上使用的身份。

## 实施指南

### 1. 选择合适的SSO方式

阿里云目前支持两种SSO方式：

- 用户SSO阿里云通过IdP颁发的SAML断言确定企业用户与阿里云RAM用户的对应关系 。企业用户登录后，使用该RAM用户访问阿里云资源。更多信息，请参见[用户SSO概览](https://help.aliyun.com/zh/ram/overview-of-user-based-sso#task-kwz-hrk-bhb)。
- 角色SSO支持基于SAML 2.0和OIDC的两种角色SSO：SAML角色SSO：阿里云通过IdP颁发的SAML断言确定企业用户在阿里云上可以使用的RAM角色。企业用户登录后，使用SAML断言中指定的RAM角色访问阿里云资源。请参见[SAML角色SSO概览](https://help.aliyun.com/zh/ram/overview-of-role-based-sso#task-zrv-2ny-zgb)。OIDC角色SSO：企业用户通过IdP签发的OIDC令牌（OIDC Token），调用阿里云API扮演指定角色并换取角色临时身份凭证（STS Token），然后使用STS Token安全地访问阿里云资源。更多信息，请参见[OIDC角色SSO概览](https://help.aliyun.com/zh/ram/overview-of-oidc-based-sso#concept-2118766)。

建议您优先考虑使用角色SSO的方式，除非您需要使用的云产品中有部分暂时不支持角色访问，此时您需要使用用户SSO的方式。支持角色访问（即通过STS访问）的云产品请参见[支持STS的云服务](https://help.aliyun.com/zh/ram/services-that-work-with-sts#concept-ofk-yt2-xdb)。

关于用户SSO与角色SSO的更多比较，请参见[SSO方式的适用场景](https://help.aliyun.com/zh/ram/scenarios-of-sso#concept-ft2-fvy-bhb)。

### 2. 跟企业IdP进行SSO集成

阿里云提供了多种产品和功能，方便您快速实现企业IdP和阿里云的SSO集成。不同的场景和企业IdP，您需要采取不同的SSO集成方案。您可以将IdP直接和RAM身份进行SSO集成，在一些特定场景下，也可以使用应用身份服务（IDaaS）（Identity as a Service）实现统一SSO登录，具体选择依据如下所示。

#### 直接和RAM身份SSO集成

对于只需要和RAM身份进行SSO集成进行云上资源管控，且IdP支持SAML 2.0协议的场景下，建议您直接使用标准的SAML协议和RAM身份进行SSO集成。根据不同的账号结构选择不同的方案：

- 单账号场景下，您可以使用访问控制 RAM（Resource Access Management）提供的[单点登录功能](https://help.aliyun.com/zh/ram/sso-overview)，实现阿里云与企业IdP的集成。
- 多账号场景（Landing Zone）下，推荐使用云SSO直接[跟企业IdP进行SSO集成](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso)，实现多个账号统一的身份管理和认证。详细方案，请参见《[基于云SSO实现多账号单点登录](https://help.aliyun.com/zh/well-architected/solution-17)》。

以下是常见的IdP跟阿里云RAM身份进行SSO集成的指南：

## Microsoft Entra ID

大多数情况下，您只需要和RAM身份进行SSO集成，进行云上资源管控，即您可以直接将Microsoft Entra ID和RAM身份进行SSO集成。

- 单账号场景RAM用户SSOSSO单点登录：[使用Azure AD进行用户SSO的示例](https://help.aliyun.com/zh/ram/implement-user-based-sso-by-using-azure-ad)。用户/组自动同步：暂不支持，您可以自行搭建代理程序，将Microsoft Entra ID的认证方式修改为RAM接收的OAuth认证的方式来实现SCIM同步。RAM角色SSOSSO单点登录：[使用Azure AD进行角色SSO的示例](https://help.aliyun.com/zh/ram/implement-role-based-sso-from-azure-ad)。
- 多账号场景，推荐使用云SSO直接[跟企业IdP进行SSO集成](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso)，实现多个账号统一的身份管理和认证。SSO单点登录：[Azure AD与云SSO进行单点登录的示例](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso-from-azure-ad-to-cloudsso)。用户/组自动同步：[通过SCIM同步Azure AD用户或用户组的示例](https://help.aliyun.com/zh/cloudsso/user-guide/synchronize-users-or-groups-in-azure-ad-by-using-scim)。

## Okta

大多数情况下，您只需要和RAM身份进行SSO集成，进行云上资源管控，即您可以直接将Okta和RAM身份进行SSO集成。

- 单账号场景RAM用户SSOSSO单点登录：[使用Okta进行用户SSO的示例](https://help.aliyun.com/zh/ram/implement-user-based-sso-by-using-okta)。用户/组自动同步：暂不支持。RAM角色SSOSSO单点登录：[使用Okta进行角色SSO的示例](https://help.aliyun.com/zh/ram/implement-role-based-sso-from-okta)。
- 多账号场景，推荐使用云SSO直接[跟企业IdP进行SSO集成](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso)，实现多个账号统一的身份管理和认证。SSO单点登录：[Okta与云SSO进行单点登录的示例](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso-logon-from-okta-to-cloudsso)。用户/组自动同步：[通过SCIM同步Okta用户或用户组的示例](https://help.aliyun.com/zh/cloudsso/user-guide/synchronize-users-or-groups-in-okta-by-using-scim)。

## AD FS

如果您没有在AD FS侧进行二次校验（如MFA）的安全需求，那么您可以直接将AD FS和RAM身份进行SSO集成。

- 单账号场景RAM用户SSOSSO单点登录：[使用AD FS进行用户SSO的示例](https://help.aliyun.com/zh/ram/implement-user-based-sso-from-ad-fs).用户/组自动同步：因为AD FS没有官方提供SCIM协议的支持，只能通过其他开源工具替代实现。RAM角色SSOSSO单点登录：[使用AD FS进行角色SSO的示例](https://help.aliyun.com/zh/ram/implement-role-based-sso-from-ad-fs).
- 多账号场景，推荐使用云SSO直接[跟企业IdP进行SSO集成](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso)，实现多个账号统一的身份管理和认证。SSO单点登录：[AD FS与云SSO进行单点登录的示例](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso-logon-from-ad-fs-to-cloudsso).用户/组自动同步：因为AD FS没有官方提供SCIM协议的支持，只能通过其他开源工具替代实现。比如您可以参考阿里云提供的开源工具[ldap2scim](https://github.com/aliyunmaker/ldap2scim)进行同步机制的实现。

## 飞书

如果您不需要自动同步飞书通讯录，只需要和RAM身份进行SSO集成，进行云上资源管控的话，您可以通过标准的SAML协议直接将飞书和RAM身份进行SSO集成。

- 单账号场景，您可以使用访问控制 RAM（Resource Access Management）提供的[单点登录功能](https://help.aliyun.com/zh/ram/sso-overview)，实现阿里云与企业IdP的集成。
- 多账号场景，推荐使用云SSO直接[跟企业IdP进行SSO集成](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso)，实现多个账号统一的身份管理和认证。

需要注意的是，没有出现在上述指南中的IdP，并不代表该IdP一定无法跟阿里云进行SSO集成，只要支持SAML 2.0协议的IdP（如Google Workspace、Auth0、Keycloak等）都可以跟阿里云的RAM身份进行SSO集成。

#### 使用IDaaS进行SSO集成

以下场景，建议您使用应用身份服务（IDaaS）（Identity as a Service）实现统一SSO登录。更多关于IDaaS的信息和产品费用，请参见[什么是IDaaS EIAM？](https://help.aliyun.com/zh/idaas/eiam/product-overview/what-is-idaas)。

- 您在阿里云上有多个用户体系，比如：RAM身份、堡垒机用户、无影云桌面用户等，需要实现和企业IdP的统一SSO集成。此时，您可以使用IDaaS作为不同用户体系之间的桥接。
- 您的IdP不支持标准的SAML协议，比如：钉钉、企微或者其他支持LDAP协议的IdP。此时，您可以使用IDaaS和钉钉、企微、LDAP IdP集成绑定，再通过IDaaS桥接到其他云上用户体系。
- 您希望实现IdP用户的自动同步，但是您的IdP不支持标准SCIM协议，比如：飞书。此时，您可以使用IDaaS作为桥接，实现将IdP的用户自动同步为云上身份。
- 出于安全考虑，您需要在用户登录时进行二次认证，比如多因素认证MFA，但是您的IdP不支持。此时，您可以通过IDaaS使用MFA进行二次身份验证。
- 您企业内当前没有一个企业IdP，需要一个IdP的场景满足多个应用集成的场景，您可以把IDaaS作为您企业内的IdP使用。

如果您没有上述的场景，建议优先考虑直接将企业IdP和阿里云的RAM身份集成，简化架构和维护成本。

针对常见的企业IdP，您可以参考以下实施步骤，实现企业IdP和阿里云的SSO集成。

## Microsoft Entra ID

如果您满足以下任意一个场景，建议您使用应用身份服务（IDaaS）（Identity as a Service）实现Microsoft Entra ID的SSO集成：

- 在阿里云上有多个用户体系，比如RAM身份、堡垒机用户、无影云桌面用户等，需要实现和Microsoft Entra ID的统一SSO集成**。**

详细实施步骤如下：

- SSO单点登录：首先您需要将IDaaS和Microsoft Entra ID集成绑定，实现Microsoft Entra ID通过OIDC协议登录到IDaaS用户。具体操作，请参考[绑定Microsoft Entra ID（Azure AD）](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-microsoft-entra-id-azure-ad)。然后将IDaaS和其他用户体系进行SSO集成，比如RAM用户、RAM角色、堡垒机用户、无影云桌面用户等等。如此，通过IDaaS作为不同用户体系间的桥接，实现多个用户体系的统一SSO集成登录。您可以参考以下几个常见的身份场景进行SSO集成配置。RAM身份SSO单账号场景下，IDaaS可以直接和RAM进行SSO集成：[阿里云用户 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-user-based-sso)、[阿里云角色SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-role-based-sso)多账号场景下，通过IDaaS和云SSO的集成，实现多个账号统一的身份管理和认证。具体操作，请参考[阿里云云SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/cloud-sso)。[堡垒机 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/bastionhost-sso)[阿里云无影云桌面 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-wuying-workspace-sso)[阿里云-云效 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-cloud-effect-sso)**说明**更多用户体系的SSO集成，请参考IDaaS[常用应用配置](https://help.aliyun.com/zh/idaas/eiam/user-guide/common-application-configurations/)。
- 用户/组自动同步：首先您需要将Microsoft Entra ID的账户同步为IDaaS账户。在将IDaaS和Microsoft Entra ID集成绑定时，您可以在[选择场景](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-oidc-identity-provider/#d8eb7724949ac)中，开启**自动创建账户**，当Microsoft Entra ID通过OIDC登录时，如果Microsoft Entra ID账户未绑定IDaaS账户，则可自动创建IDaaS账户。后续每次通过OIDC登录都将更新账户信息。然后将IDaaS账户同步到其他用户体系，实现企业IdP到多个用户体系的自动用户同步。具体操作，请参考[账户同步-事件回调](https://help.aliyun.com/zh/idaas/eiam/user-guide/provision-accounts-idaas-event-callback)。堡垒机用户同步，请参见《[通过IDaaS实现堡垒机用户集中管理](https://help.aliyun.com/zh/well-architected/solution-259)》。**说明**需要注意的是，IDaaS目前不支持组同步。

## Okta

如果您满足以下任意一个场景，建议您使用应用身份服务（IDaaS）（Identity as a Service）实现Okta的SSO集成：

- 在阿里云上有多个用户体系，比如RAM身份、堡垒机用户、无影云桌面用户等，需要实现和Okta的统一SSO集成**。**

详细实施步骤如下：

- SSO单点登录：首先您需要将IDaaS和Okta集成绑定，实现Okta通过OIDC协议登录到IDaaS用户。具体操作，请参考[绑定Okta](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-okta)。然后将IDaaS和其他用户体系进行SSO集成，比如RAM用户、RAM角色、堡垒机用户、无影云桌面用户等等。如此，通过IDaaS作为不同用户体系间的桥接，实现多个用户体系的统一SSO集成登录。您可以参考以下几个常见的身份场景进行SSO集成配置。RAM身份SSO单账号场景下，IDaaS可以直接和RAM进行SSO集成：[阿里云用户 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-user-based-sso)、[阿里云角色SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-role-based-sso)多账号场景下，通过IDaaS和云SSO的集成，实现多个账号统一的身份管理和认证。具体操作，请参考[阿里云云SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/cloud-sso)。[堡垒机 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/bastionhost-sso)[阿里云无影云桌面 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-wuying-workspace-sso)[阿里云-云效 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-cloud-effect-sso)**说明**更多用户体系的SSO集成，请参考IDaaS[常用应用配置](https://help.aliyun.com/zh/idaas/eiam/user-guide/common-application-configurations/)。
- 用户/组自动同步：首先您需要将Okta的账户同步为IDaaS账户。在将IDaaS和Okta集成绑定时，您可以在[选择场景](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-oidc-identity-provider/#d8eb7724949ac)中，开启**自动创建账户**，当Okta通过OIDC登录时，如果Okta账户未绑定IDaaS账户，则可自动创建IDaaS账户。后续每次通过OIDC登录都将更新账户信息。然后将IDaaS账户同步到其他用户体系，实现企业IdP到多个用户体系的自动用户同步。具体操作，请参考[账户同步-事件回调](https://help.aliyun.com/zh/idaas/eiam/user-guide/provision-accounts-idaas-event-callback)。堡垒机用户同步，请参见《[通过IDaaS实现堡垒机用户集中管理](https://help.aliyun.com/zh/well-architected/solution-259)》。**说明**需要注意的是，IDaaS目前不支持组同步。

## AD FS

如果您满足以下任意一个场景，建议您使用应用身份服务（IDaaS）（Identity as a Service）实现AD FS的SSO集成：

- 在阿里云上有多个用户体系，比如RAM身份、堡垒机用户、无影云桌面用户等，需要实现和AD FS的统一SSO集成**。**
- 您需要在用户登录时进行二次认证，比如多因素认证MFA。
- 需要将AD中的用户同步到阿里云上，并且希望使用托管的产品功能或方案进行同步，而非开源自建方案。

详细实施步骤如下：

- SSO单点登录：首先您需要将IDaaS和AD集成绑定。具体操作，请参考[绑定AD](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-ad)。如果您的AD FS部署在阿里云上，只允许在VPC私网内进行通信，请创建专属端点，并在IDaaS绑定AD时，选择专属端点作为IDaaS的网络端点。详见：[网络端点](https://help.aliyun.com/zh/idaas/eiam/user-guide/network-access-endpoints)。**说明**您需要使用企业版实例才可选购专属端点，详见，[专属端点计费说明](https://help.aliyun.com/zh/idaas/eiam/product-overview/pricing#c803216006rlh)。
- 然后将IDaaS和其他用户体系进行SSO集成，比如RAM用户、RAM角色、堡垒机用户、无影云桌面用户等等。如此，通过IDaaS作为不同用户体系间的桥接，实现多个用户体系的统一SSO集成登录。您可以参考以下几个常见的身份场景进行SSO集成配置。RAM身份SSO单账号场景下，IDaaS可以直接和RAM进行SSO集成：[阿里云用户 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-user-based-sso)、[阿里云角色SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-role-based-sso)多账号场景下，通过IDaaS和云SSO的集成，实现多个账号统一的身份管理和认证。具体操作，请参考[阿里云云SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/cloud-sso)。[堡垒机 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/bastionhost-sso)[阿里云无影云桌面 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-wuying-workspace-sso)[阿里云-云效 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-cloud-effect-sso)**说明**更多用户体系的SSO集成，请参考IDaaS[常用应用配置](https://help.aliyun.com/zh/idaas/eiam/user-guide/common-application-configurations/)。
- 用户/组自动同步：首先您需要将AD的用户同步为IDaaS账户。在将IDaaS和Okta集成绑定时，您可以在[第二步：选择场景](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-ad#p-0uq-ss2-f3i)中，开启**增量同步**，IDaaS将监听AD的用户或组织数据，每10分钟左右执行一次同步，将有变动的数据导入到IDaaS中。如果单次增量同步的数据量较大，可能会延迟处理。建议定期执行一次全量同步，以确保对齐两边数据。然后将IDaaS账户同步到其他用户体系，实现企业IdP到多个用户体系的自动用户同步。具体操作，请参考[账户同步-事件回调](https://help.aliyun.com/zh/idaas/eiam/user-guide/provision-accounts-idaas-event-callback)。堡垒机用户同步，请参见《[通过IDaaS实现堡垒机用户集中管理](https://help.aliyun.com/zh/well-architected/solution-259)》。**说明**需要注意的是，IDaaS目前不支持组同步。

## LDAP IdP

如果您的IdP只支持LDAP协议，您需要使用IDaaS进行SSO集成。

- SSO单点登录：首先您需要将IDaaS和LDAP IdP集成绑定。具体操作，请参考[绑定OpenLDAP](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-openldap)。然后将IDaaS和其他用户体系进行SSO集成，比如RAM用户、RAM角色、堡垒机用户、无影云桌面用户等等。如此，通过IDaaS作为不同用户体系间的桥接，实现多个用户体系的统一SSO集成登录。您可以参考以下几个常见的身份场景进行SSO集成配置。RAM身份SSO单账号场景下，IDaaS可以直接和RAM进行SSO集成：[阿里云用户 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-user-based-sso)、[阿里云角色SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-role-based-sso)多账号场景下，通过IDaaS和云SSO的集成，实现多个账号统一的身份管理和认证。具体操作，请参考[阿里云云SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/cloud-sso)。[堡垒机 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/bastionhost-sso)[阿里云无影云桌面 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-wuying-workspace-sso)[阿里云-云效 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-cloud-effect-sso)**说明**更多用户体系的SSO集成，请参考IDaaS[常用应用配置](https://help.aliyun.com/zh/idaas/eiam/user-guide/common-application-configurations/)。
- 用户/组自动同步：首先您需要将LDAP IdP的用户同步为IDaaS账户。在将IDaaS和LDAP IdP集成绑定时，您可以在[第二步：选择场景](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-openldap#a261edd0302c4)中，开启**定时校验**，由于LDAP不支持查询增量数据，IDaaS将于每日凌晨自动全量同步LDAP来源节点下的全量数据。然后将IDaaS账户同步到其他用户体系，实现企业IdP到多个用户体系的自动用户同步。具体操作，请参考[账户同步-事件回调](https://help.aliyun.com/zh/idaas/eiam/user-guide/provision-accounts-idaas-event-callback)。堡垒机用户同步，请参见《[通过IDaaS实现堡垒机用户集中管理](https://help.aliyun.com/zh/well-architected/solution-259)》。**说明**IDaaS目前不支持组同步。LDAP不支持查询增量数据，开启定时校验后，IDaaS将于每日凌晨自动全量同步LDAP来源节点下的全量数据。

## 钉钉/企业微信

如果您使用钉钉或者企业微信管理员工身份，您需要使用IDaaS进行SSO集成。

- SSO单点登录：首先您需要将IDaaS和钉钉/企微集成绑定。具体操作，请参考[绑定钉钉-入方向](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-dingtalk-inbound)、[绑定企业微信](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-wecom)。然后将IDaaS和其他用户体系进行SSO集成，比如RAM用户、RAM角色、堡垒机用户、无影云桌面用户等等。如此，通过IDaaS作为不同用户体系间的桥接，实现多个用户体系的统一SSO集成登录。您可以参考以下几个常见的身份场景进行SSO集成配置。RAM身份SSO单账号场景下，IDaaS可以直接和RAM进行SSO集成：[阿里云用户 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-user-based-sso)、[阿里云角色SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-role-based-sso)多账号场景下，通过IDaaS和云SSO的集成，实现多个账号统一的身份管理和认证。具体操作，请参考[阿里云云SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/cloud-sso)。[堡垒机 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/bastionhost-sso)[阿里云无影云桌面 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-wuying-workspace-sso)[阿里云-云效 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-cloud-effect-sso)**说明**更多用户体系的SSO集成，请参考IDaaS[常用应用配置](https://help.aliyun.com/zh/idaas/eiam/user-guide/common-application-configurations/)。
- 用户/组自动同步：首先您需要将钉钉/企微通讯录的员工同步为IDaaS账户。在将IDaaS和钉钉集成绑定时，您可以在[第一步：选择场景](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-dingtalk-inbound#h3-zzu-aid-hep)中，开启**增量同步**，启用后，IDaaS 调用钉钉接口，监听钉钉通讯录事件。钉钉通讯录有变动，可实时将变动数据同步到 IDaaS 中。在将IDaaS和企微集成绑定时，您可以在[步骤三：选择场景](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-wecom#6d590060165wi)中，开启**定时校验**，由于企业微信不支持查询增量数据，IDaaS将于每日凌晨自动全量同步企业微信来源节点下的全量数据。然后将IDaaS账户同步到其他用户体系，实现企业IdP到多个用户体系的自动用户同步。具体操作，请参考[账户同步-事件回调](https://help.aliyun.com/zh/idaas/eiam/user-guide/provision-accounts-idaas-event-callback)。CloudSSO用户同步，请参见《[基于IDaaS实现企微与飞书用户同步至云SSO](https://help.aliyun.com/zh/well-architected/solution-258)》。堡垒机用户同步，请参见《[通过IDaaS实现堡垒机用户集中管理](https://help.aliyun.com/zh/well-architected/solution-259)》。**说明**IDaaS目前不支持组同步。企业微信不支持查询增量数据，IDaaS将于每日凌晨自动全量同步企业微信来源节点下的全量数据。配置用户同步时，支持在钉钉/企微侧设置同步范围，在同步范围中的通讯录员工才会被同步到IDaaS中。需要注意的是，钉钉/企微侧的可见范围的变更，不会触发IDaaS的增量同步。只有通讯录里的员工新增、删除（从通讯录里完全删除）、更新时，才会触发增量同步，否则您需要手动触发全量同步。如果有需要，您可以参考解决方案《基于函数计算实现从IdP到IDaaS的人员定时同步方案》定时自动进行全量同步。

## 飞书

如果您满足以下任意一个场景，建议您使用应用身份服务（IDaaS）（Identity as a Service）实现飞书的SSO集成：

- 在阿里云上有多个用户体系，比如RAM身份、堡垒机用户、无影云桌面用户等，需要实现和飞书的统一SSO集成**。**
- 您希望实现飞书用户的自动同步。

详细实施步骤如下：

- SSO单点登录：首先您需要将IDaaS和飞书集成绑定。具体操作，请参考[绑定飞书](https://help.aliyun.com/zh/idaas/eiam/user-guide/binding-fly-book)。然后将IDaaS和其他用户体系进行SSO集成，比如RAM用户、RAM角色、堡垒机用户、无影云桌面用户等等。如此，通过IDaaS作为不同用户体系间的桥接，实现多个用户体系的统一SSO集成登录。您可以参考以下几个常见的身份场景进行SSO集成配置。RAM身份SSO单账号场景下，IDaaS可以直接和RAM进行SSO集成：[阿里云用户 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-user-based-sso)、[阿里云角色SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-role-based-sso)多账号场景下，通过IDaaS和云SSO的集成，实现多个账号统一的身份管理和认证。具体操作，请参考[阿里云云SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/cloud-sso)。[堡垒机 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/bastionhost-sso)[阿里云无影云桌面 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-wuying-workspace-sso)[阿里云-云效 SSO](https://help.aliyun.com/zh/idaas/eiam/user-guide/alibaba-cloud-cloud-effect-sso)**说明**更多用户体系的SSO集成，请参考IDaaS[常用应用配置](https://help.aliyun.com/zh/idaas/eiam/user-guide/common-application-configurations/)。
- 用户/组自动同步：首先您需要将飞书通讯录的员工同步为IDaaS账户。在将IDaaS和飞书集成绑定时，您可以在[第三步：选择场景](https://help.aliyun.com/zh/idaas/eiam/user-guide/binding-fly-book#ee138f5b35i8f)中，开启**定时校验**，IDaaS将于每日凌晨自动全量同步飞书数据。然后将IDaaS账户同步到其他用户体系，实现企业IdP到多个用户体系的自动用户同步。具体操作，请参考[账户同步-事件回调](https://help.aliyun.com/zh/idaas/eiam/user-guide/provision-accounts-idaas-event-callback)。CloudSSO用户同步，请参见《[基于IDaaS实现企微与飞书用户同步至云SSO](https://help.aliyun.com/zh/well-architected/solution-258)》。堡垒机用户同步，请参见《[通过IDaaS实现堡垒机用户集中管理](https://help.aliyun.com/zh/well-architected/solution-259)》。**说明**IDaaS目前不支持组同步。IDaaS目前不支持飞书数据的增量同步。

#### 注意事项

需要特别注意的是，如果您实现了企业IdP到阿里云RAM用户的自动同步，当您在IdP侧删除了某个用户，那么SCIM同步过来的RAM用户也会被删除，此时如果该RAM用户创建有AccessKey，那么也会被一并删除，有可能导致您使用该AccessKey的业务功能受损。因此，建议您严格遵守身份的单一职责原则：

- 对于员工登录阿里云控制台使用的RAM用户，不要创建AccessKey。
- 使用单独的RAM用户，创建AccessKey给应用程序调用阿里云API使用，同时关闭该RAM用户的控制台登录。具体操作，请参见[修改控制台登录设置](https://help.aliyun.com/zh/ram/manage-console-logon-settings-for-a-ram-user-1#section-xhr-6rv-o2a)。

## 相关资源

### 相关方案

- 《[基于云SSO实现多账号单点登录](https://help.aliyun.com/zh/well-architected/solution-17)》
- 《[基于IDaaS实现IdP用户同步至云SSO](https://help.aliyun.com/zh/well-architected/solution-146)》
- 《[通过IDaaS实现堡垒机用户集中管理](https://help.aliyun.com/zh/well-architected/solution-259)》
- 《[基于IDaaS实现企微与飞书用户同步至云SSO](https://help.aliyun.com/zh/well-architected/solution-258)》
- 《[基于CloudSSO实现多账号ACK集群统一身份权限管理](https://help.aliyun.com/zh/well-architected/solution-114)》

---

> 原页面：https://help.aliyun.com/zh/well-architected/sec01-bp05-unified-authentication-of-personnel-identity-based-on-unified-idp（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
