<!-- source: https://help.aliyun.com/zh/well-architected/solution-146 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929412 -->

# 基于IDaaS实现IdP用户同步至云SSO

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971856.png)

使用云SSO能够便捷实现阿里云多账号身份管理及访问控制，快速实现多账号单点登录，但企业的用户信息通常存储在本地IdP（如AD）中，不支持通过产品化的方式将IdP中的用户同步到云SSO中，无法对用户身份进行统一管理、影响云SSO使用。本文档介绍了使用IDaaS将IdP用户同步到云SSO中的方法，便于企业在IdP中对用户身份进行统一管理，提升云上身份管理效率。

## 方案优势

### 用户身份便捷同步

通过引入IDaaS，使用产品化的方式将IdP中的用户快速同步到云SSO中，使用标准的LDAP及SCIM协议，无需单独开发同步程序。

### 用户身份统一管理

IdP用户信息同步到云SSO后，不需要在云SSO中单独新建用户，IDaaS支持增量同步，企业在IdP中能够对用户身份进行统一管理，提升云上身份管理效率。

## 客户场景

### 同步IdP用户信息到云SSO

#### 场景描述

企业已在IdP中进行用户身份管理，并已经或计划在阿里云上使用云SSO进行多账号单点登录，需要将IdP中的用户同步到云SSO中，希望避免在云SSO中单独维护用户信息、对用户身份在IdP中进行统一管理。

#### 适用客户

- 已经或计划使用云SSO，期望在IdP中统一管理身份的企业客户。
- 希望将IdP中的用户信息同步到云SSO中的企业客户。

### 同步IDaaS用户到云SSO

#### 场景描述

企业已在IDaaS中进行用户身份管理，并已经或计划在阿里云上使用云SSO进行多账号单点登录，需要IDaaS中的用户同步到云SSO中，希望避免在云SSO中单独维护用户信息、对用户身份在IDaaS中进行统一管理。

#### 适用客户

- 已经或计划使用云SSO，期望在IDaaS中统一管理身份的企业客户。
- 希望将IDaaS中的用户信息同步到云SSO中的企业客户。

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971854.png)

方案架构说明如下：

- IdP（方案中以AD为例）需支持LDAP协议，能够同步组织及用户信息。
- 在IDaaS中配置LDAP连接信息及IdP管理员账号（拥有只读权限）信息，IDaaS通过LDAP协议连接企业IdP，将IdP中的组织及用户信息同步到IDaaS。
- 在IDaaS中创建云SSO应用，通过SCIM协议将用户信息同步到云SSO中，支持增量同步。

IDaaS分为免费版和企业收费版，本方案中使用免费版。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云身份服务IDaaS | [云身份服务 IDaaS](https://help.aliyun.com/zh/idaas/eiam/product-overview/what-is-idaas)（英文名：Alibaba Cloud IDentity as a Service，简称 IDaaS）是阿里云为企业用户提供的云原生的、经济的、便捷的、标准的身份、权限管理体系。 | 分为免费版和企业收费版，详情参见[产品计费](https://help.aliyun.com/zh/idaas/eiam/product-overview/pricing)。 |
| 云SSO | [云SSO](https://help.aliyun.com/zh/cloudsso/product-overview/what-is-cloudsso)提供基于阿里云资源目录RD（Resource Directory）的多账号统一身份管理与访问控制。使用云SSO，您可以统一管理企业中使用阿里云的用户，一次性配置企业身份管理系统与阿里云的单点登录，并统一配置所有用户对RD账号的访问权限。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/cloudsso/product-overview/billing-methods)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| IdP | Identity Provider，身份提供方。源自于 SAML 协议中定义，IdP 为进行用户认证、鉴权，并返回 SAML Response 结果信息给 SP 的身份提供方，后通用化指统一身份管理平台。 |
| LDAP | LDAP（轻型目录访问协议）是一种软件协议，使任何人都可以在公共互联网或公司内网上查找网络中的组织，个人和其他资源（例如文件和设备）的数据。 |
| SCIM | System for Cross-domain Identity Management，跨域身份管理系统，专用于不同系统之间账户、组织同步的国际通用规范，国内外有大量应用支持接收 SCIM 协议同步请求，以实现不同系统身份的互用性。 |

## 安全性

### IDaaS安全性

IDaaS采用“默认安全”的产品设计，在“可用性”和“安全性”难以两全的场景中，IDaaS 会优先保障“安全性”，在此基础上，尽可能追求“易用性”，详情参见[IDaaS默认安全设计](https://help.aliyun.com/zh/idaas/eiam/product-overview/default-security-solutions)。

### 传输安全性

- **传输协议**：方案中相关产品使用业界标准的LDAP协议及SCIM协议保障数据安全传递，详情参见[LDAP](https://ldap.com/)及[SCIM](http://www.simplecloud.info/)。
- **传输加密**：IDaaS支持LDAP连接开启StartTLS，建议AD中配置证书并在数据同步时开启StartTLS提升传输安全性，详情参见[AD安全性配置](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-ad)。
- **数据权限**：需要准备AD管理员账户及密码，至少拥有只读权限，用于从AD同步身份数据。
- **公网访问**：目前企业IdP（如AD）需要**公网可访问**才能使用IDaaS免费版及企业版进行数据同步，建议在企业环境中开启针对AD的公网访问限制，并将IDaaS地址添加到白名单中。

## 注意事项

方案中从企业IdP（以AD为例）同步身份信息到IDaaS，目前需要IdP（以AD为例）支持公网访问，请阅读**安全性章节**内容以保障数据安全。

## 实施步骤

### 实施准备

本示例的实施准备工作说明如下：

- 已拥有AD，可公网访问，AD中已创建域及OU、已配置证书，已准备管理员账户（至少拥有只读权限）。
- 已创建IDaaS实例，本示例使用免费版，详情可参见[免费开通实例](https://help.aliyun.com/zh/idaas/eiam/user-guide/eiam-sso-quick-start)。
- 已开通及使用云SSO，详情参见[开始使用云SSO](https://help.aliyun.com/zh/cloudsso/getting-started/getting-started-with-cloudsso)。

### 实施规划

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971855.png)

本次示例部署说明如下：

- IdP使用AD，使用LDAP协议将AD中的`landingzone.cc`域、`hangzhou OU`中的用户同步到IDaaS的组织`hangzhou`中。
- 将IDaaS中的用户通过SCIM协议同步到云SSO中。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：45分钟。

### 操作步骤

操作步骤整体内容包括从AD同步用户到IDaaS、从IDaaS同步用户到云SSO两部分。如果仅希望将IDaaS中已有用户同步到云SSO中，可从“**在云SSO中开启SCIM同步”**这一步骤开始操作。

#### 在IDaaS中创建组织

在[IDaaS控制台中](https://yundun.console.aliyun.com/?p=idaas#/overview/new/cn-hangzhou)单击已创建的实例，进入账户与组织页面，创建组织`landingzone.cc`，在landingzone.cc组织下创建组织`hangzhou`。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971859.png)

#### 同步AD用户到IDaaS

1. 进入**身份提供方**页面，单击绑定AD，填写AD配置信息。本示例操作以AD为例，如果需要绑定OpenLDAP可参考文档[绑定OpenLDAP](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-openldap)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971858.png)字段说明如下：**显示名称**：用户在登录、使用 IDaaS 时可能看到。**服务器地址**：AD 所在的服务器地址，AD 一般使用 389 端口，开启 ldaps 或 StartTLS 时一般使用 636 端口。**本操作示例填写AD公网IP地址，**如`139.xx.xx.1:389`。**ldaps/StartTLS**：开启后可以大幅提高连接的安全性，推荐开启。请在 [AD安全性配置](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-ad)中了解如何开启。本操作示例选择**开启StartTLS、通过证书指纹验证，单击一键获取按钮获取证书指纹**。**出口IP**：如果您希望只有 IDaaS 可以请求该 AD，请在服务器中配置 IP 白名单。**建议对AD公网访问进行限制，并添加IDaaS IP白名单**。**管理员账户**：IDaaS 使用该 AD 管理员账户读取 AD 信息来完成数据同步或委托认证，该账户需要至少拥有**读取权限**，支持使用 UPN 格式（example@example.com）和 DN 格式（cn=admin,ou=技术部,dc=example,dc=com）。**本示例管理员账户使用账户名。****管理员密码**：输入该账户的登录密码。
2. 单击下一步，填写同步配置，字段说明如下：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971857.png)**同步方向**：同步来源所选的 AD 的用户/组织数据将会导入到 IDaaS 的这个节点之下。【来源节点】需要填写 AD 节点的 DN，AD 根节点的 DN 一般为 dc=example,dc=com（即您的域）。**本示例填写**`OU=hangzhou,DC=landingzone,DC=cc`**，目标节点选择之前在IDaaS中创建的组织节点**`hangzhou`。**说明**目前仅支持入方向 AD 的同步，暂不支持出方向。**增量同步**：IDaaS 将监听 AD 的用户/组织数据，每 10 分钟左右执行一次同步，将有变动的数据导入到 IDaaS 中。如果单次增量同步的数据量较大，可能会延迟处理。建议定期执行一次全量同步，以确保对齐两边数据，**本示例选择开启**。您可以在字段映射中设置映射标识，使用 IDaaS 账户的某个字段（如手机号）与 AD 用户的某个字段（如手机号）进行匹配，如果匹配成功，将绑定并覆盖更新；否则将创建 IDaaS 账户。在首次进行增量同步时，将自动执行一次全量同步。如果单条账户数据无法导入，不影响其他数据导入。失败信息可在【同步日志】中查看。需要开启 AD 回收站才可接收 AD 删除类型的事件的消息。请在 [增量同步](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-ad)中了解如何开启。**委托认证**：用户可以使用 AD 用户/密码登录到 IDaaS。**自动更新密码**：用户通过 AD 委托认证到 IDaaS 时，如果 IDaaS 账户的密码为空，则更新为 AD 用户的密码。AD 密码需满足 IDaaS 密码策略的要求，否则将无法自动更新。**高级配置****用户/组织ObjectClass**：通过 ObjectClass 可以定义哪种类型的对象是用户/组织，例如将查询结果中 ObjectClass=user 的对象视作用户。一般无需修改。**用户登录标识**：用户在使用 AD 委托认证登录 IDaaS 时，IDaaS 将根据这些属性去 AD 中查询用户并匹配密码，密码正确则允许用户登录 IDaaS。可以使用半角逗号对多个属性进行分割，此时为或关系，即可以使用任一属性登录。请确保多个属性对应同一个 AD 用户，否则将无法登录。
3. 单击完成创建，开始用户同步，可以单击查看详情查看同步日志。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971860.png)
4. 在账户与组织页面中可查看已同步过来的用户信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971862.png)

#### 在云SSO中开启SCIM同步

1. 登录 [云SSO 控制台](https://cloudsso.console.aliyun.com/)，在左侧导航栏，单击**设置**。
2. 单击SICM用户同步配置下方按钮，**开启 SCIM 同步**，**复制保存SCIM服务端地址**备用。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971861.png)
3. 点击**生成密钥**，该密钥只显示一次，请**复制后妥善保存**，用于填写 IDaaS 侧 Bearer Token 密钥。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971864.png)

#### 在IDaaS中配置云SSO同步

1. 在IDaaS实例控制台 应用 界面，点击 添加应用 进入 应用市场 ，选择 云SSO 应用模板进行添加。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971866.png)
2. 切换至**账户同步**界面，打开 IDaaS 同步到应用 按钮。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971863.png)
3. 选择同步范围后**单击保存**，推送模式选择 SCIM 协议 。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971865.png)
4. 填写云SSO中的配置信息。配置字段说明如下：**SCIM Base URL：**在**云SSO开启SCIM同步**这一步骤中复制的SCIM服务端地址。**接口授权：**选择 BearerToken 模式**Bearer Token 密钥模式：**在**云SSO开启SCIM同步**这一步骤中复制的密钥。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971867.png)
5. 配置操作调用以及字段映射，配置说明如下：**操作调用：**管理员可以选择性地订阅希望关注的变更事件，获取即时推送。当 IDaaS 中发生了对应变更后，将会自动触发同步，将变更即时更新至应用中。**字段映射：**用于展示和编辑 SCIM 同步过程中的字段映射关系，暂不支持修改。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971869.png)
6. 在配置完成后**单击保存**，建议您通过**测试连接**功能检查配置是否正确。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971870.png)

#### 同步用户至云SSO

1. 单击**一键推送**，配置的**同步范围**内的账户会同步至云SSO。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971868.png)
2. 推送成功后系统会提示**任务成功**，可以前往**日志-同步日志-任务执行**中查看日志。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971871.png)
3. 在[云SSO控制台](https://cloudsso.console.aliyun.com/cn-shanghai/users)用户页面可查看已同步过来的用户信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866581571/p971872.png)

#### 配置单点登录

- 如果使用AD FS与云SSO进行单点登录，操作步骤请参考[AD FS单点登录示例](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso-logon-from-ad-fs-to-cloudsso)。
- 如果使用IDaaS作为云上IdP，通过AD/LDAP认证与云SSO进行单点登录可参考[使用AD/LDAP认证登录三方应用](https://help.aliyun.com/zh/idaas/eiam/use-cases/use-ad-or-ldap-to-log-on-to-a-third-party-application)及[云SSO单点登录](https://help.aliyun.com/zh/cloudsso/user-guide/sso-logon/)。

## 故障排除

### IDaaS无法连接到AD

- 请确认绑定的AD允许公网访问。
- AD访问如果有白名单限制请将IDaaS出口IP添加至白名单。
- 请确认AD地址及端口填写正确，管理员账户密码填写正确并具有相应权限。

### IDaaS无法连接到云SSO

- 请确认IDaaS中云SSO的SCIM服务端地址填写正确。
- 请确认IDaaS中云SSO的Bearer Token填写正确，尝试在云SSO中重新生成密钥更新到IDaaS中，配置页面**单击保存**后再尝试连接。

### IDaaS可以同步AD中的OU吗？

可以，请在绑定AD时在**同步方向**中按实际需求选择AD来源节点及IDaaS中的目的节点。

## 相关内容

- [云SSO集成外部身份](https://help.aliyun.com/zh/cloudsso/user-guide/external-identity-integration/)
- [IDaaS最佳实践](https://help.aliyun.com/zh/document_detail/450513.html)
- [IDaaS常用应用配置](https://help.aliyun.com/zh/idaas/eiam/user-guide/common-application-configurations/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-146（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
