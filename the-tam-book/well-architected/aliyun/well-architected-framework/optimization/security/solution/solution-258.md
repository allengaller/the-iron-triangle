<!-- source: https://help.aliyun.com/zh/well-architected/solution-258 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929048 -->

# 基于IDaaS实现企微与飞书用户同步至云SSO

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968952.png)

使用云SSO能够便捷实现阿里云多账号身份管理及访问控制，快速实现多账号单点登录，但企业的用户信息通常存储在现存的IdP（企业微信与飞书）中，不支持通过产品化的方式将IdP中的用户同步到云SSO中，无法对用户身份进行统一管理、影响云SSO使用。本文档介绍了使用IDaaS将企业微信与飞书用户同步到云SSO中的方法，便于企业在IdP中对用户身份进行统一管理，提升云上身份管理效率。

## 方案优势

### 用户身份便捷同步

通过引入IDaaS，使用产品化的方式将企业在企业微信/飞书中的用户快速同步到云SSO中，使用标准的HTTPS及SCIM协议，无需单独开发同步程序。

### 用户身份统一管理

企业微信与飞书的用户信息同步到云SSO后，不需要在云SSO中单独新建用户，IDaaS支持增量与定时同步，企业在企业微信与飞书中能够对用户身份进行统一管理，提升云上身份管理效率。

## 客户场景

### 同步企微/飞书用户信息到云SSO

#### 场景描述

企业已在企业微信/飞书中进行用户身份管理，并已经或计划在阿里云上使用云SSO进行多账号单点登录，需要将企业微信/飞书中的用户同步到云SSO中，希望避免在云SSO中单独维护用户信息，对用户身份在企业微信/飞书中进行统一管理。

#### 适用客户

- 已经在使用企业微信/飞书，有迁移至阿里云意向的企业客户。
- 已经或计划使用云SSO，期望在企业微信/飞书中统一管理身份的企业客户。
- 希望将企业微信/飞书中的用户信息同步到云SSO中的企业客户。

### 同步IDaaS用户到云SSO

#### 场景描述

企业已在IDaaS中进行用户身份管理，并已经或计划在阿里云上使用云SSO进行多账号单点登录，需要IDaaS中的用户同步到云SSO中，希望避免在云SSO中单独维护用户信息、对用户身份在IDaaS中进行统一管理。

#### 适用客户

- 已经或计划使用云SSO，期望在IDaaS中统一管理身份的企业客户。
- 希望将IDaaS中的用户信息同步到云SSO中的企业客户。

### 应对企业外审要求与内部运维问题

#### 场景描述

多名员工需要访问阿里云控制台，有对阿里云账户与资源统一管理、违法员工操作审计需求，或出现人员凭证泄漏的企业客户。

#### 适用客户

- 使用资源目录管理云上多个账号的企业客户。
- 使用多个阿里云账号的企业客户。

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968954.png)

方案架构说明如下：

- 企业微信与飞书需授权能够同步组织及用户信息。
- 在IDaaS中配置HTTPS接口连接信息及企业微信与飞书侧管理员账号（拥有只读权限）信息，IDaaS通过HTTPS协议连接企业微信与飞书通过API调取用户信息，将企业微信与飞书中的组织及用户信息同步到IDaaS。
- 在IDaaS中创建云SSO应用，通过SCIM协议将用户信息同步到云SSO中，支持增量同步。

IDaaS分为免费版和企业收费版，本方案中使用免费版。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费 |
| 云身份服务IDaaS | [云身份服务 IDaaS](https://help.aliyun.com/zh/idaas/eiam/product-overview/what-is-idaas)（英文名：Alibaba Cloud IDentity as a Service，简称 IDaaS）是阿里云为企业用户提供的云原生的、经济的、便捷的、标准的身份、权限管理体系。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 云SSO | [云SSO](https://help.aliyun.com/zh/cloudsso/product-overview/what-is-cloudsso)提供基于阿里云资源目录RD（Resource Directory）的多账号统一身份管理与访问控制。使用云SSO，您可以统一管理企业中使用阿里云的用户，一次性配置企业身份管理系统与阿里云的单点登录，并统一配置所有用户对RD账号的访问权限。 | 免费 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| SCIM | System for Cross-domain Identity Management，跨域身份管理系统，专用于不同系统之间账户、组织同步的国际通用规范，国内外有大量应用支持接收 SCIM 协议同步请求，以实现不同系统身份的互用性。 |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |

## 安全性

#### HTTPS及SCIM协议

方案中使用业界标准的HTTPS协议及SCIM协议保障数据安全传递，相关介绍详情[SCIM](http://www.simplecloud.info/)协议。

#### IDaaS安全性

IDaaS采用“默认安全”的产品设计，在“可用性”和“安全性”难以两全的场景中，IDaaS 会优先保障“安全性”，在此基础上，尽可能追求“易用性”，详情参见[IDaaS默认安全设计](https://help.aliyun.com/zh/idaas/eiam/product-overview/default-security-solutions)。

#### 开启MFA

为提升安全性，云SSO默认开启多因子身份认证[MFA](https://help.aliyun.com/zh/account/support/what-is-the-mfa)，建议持续开启，云SSO相应管理操作参见[MFA管理](https://help.aliyun.com/zh/cloudsso/user-guide/manage-mfa)。

#### 注意事项

方案中从**飞书**同步身份信息到IDaaS，授信过程可能存在风险，目前需要飞书支持API调用组织信息查看权限，注意不要泄漏API的ID与Secret，请阅读飞书**安全性章节**内容以保障数据安全。

## 实施步骤

### 实施准备

本示例的实施准备工作说明如下：

- 已经在使用企业微信与飞书的员工管理系统，已准备管理员账户（至少拥有只读权限）。
- 已经拥有阿里云账号
- 已创建IDaaS实例，本示例使用免费版，详情可参见[免费开通实例](https://help.aliyun.com/zh/idaas/eiam/user-guide/eiam-sso-quick-start)。
- 已开通及使用云SSO，详情参见[开始使用云SSO](https://help.aliyun.com/zh/cloudsso/getting-started/getting-started-with-cloudsso)。

### 实施规划

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968953.png)

本次实施将完成：

1. 将企业微信中的用户及用户信息通过HTTPS协议同步至IDaaS
2. 将飞书中的用户及用户信息通过API同步至IDaaS
3. 将IDaaS同步至云SSO
4. 使用云SSO登录阿里云账号下的角色

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：

- 企业微信同步云SSO：1小时
- 飞书同步云SSO：30分钟

### 操作步骤

#### 企业微信同步

##### 企业微信测配置

1. 登录[企业微信控制台](https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome)并点击创建应用![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968958.png)
2. 创建应用，应收敛权限注意限制企业内应用可见范围![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968955.png)
3. 配置可信域名。在应用详情->开发者接口->网页授权及JS-SDK->可信域名配置![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968960.png)这一步为可信鉴权用途。需要在企业域名挂载的存储实例（例OSS）挂载该页面所提供的域名归属认证txt文件并允许公网访问。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968961.png)完成授权认证后如下图![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968962.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968956.png)
4. 在应用详情->开发者接口->企业可信IP。您需要使用网络端点的专属公网访问（操作文档：[配置专属公网出口IP](https://help.aliyun.com/zh/idaas/eiam/user-guide/network-access-endpoints)）实现IDaaS EIAM实例使用您的IP访问企业微信。查看专属网络地域与可用区![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968964.png)绑定弹性公网IP：首先需要EIP与NAT网关，如果没有需要前往[NAT网关控制台](https://vpc.console.aliyun.com/buy/nat?regionId=cn-hangzhou)一并购买开通。在[专有网络-公网NAT网关](https://vpc.console.aliyun.com/nat?spm=a2c4g.11186623.0.0.74665d51Rl0Gvp)中，选择和专有网络地域相同的地域下的公网NAT网关，单击**立即绑定**弹性公网IP，开始绑定流程。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968963.png)关联上步骤中的交换机![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968957.png)查看NAT网关实例并找到绑定的EIP，复制下该IP，此IP为我们要获取的企业可信IP![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968965.png)返回企业微信页面将该IP填入企业可信IP中![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968968.png)
5. 在应用详情->开发者接口->企业微信授权登录。前往IDaaS控制台获取授权回调域![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968959.png)复制该域名到企业微信中的授权回调域中![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968969.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968970.png)至此企业微信侧的网页授权、企业可信IP、企业微信授权登录配置完成

##### IDaaS侧配置接入企业微信

1. 提供IDaaS工作台接入企业微信所需要的参数
2. 前往企业微信->我的企业->获取企业ID![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968971.png)
3. 前往企业微信->应用管理->获取agentID与Secret![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968967.png)
4. 查看NAT网关实例并找到绑定的EIP，复制下该IP，此IP为我们要获取的企业可信IP
5. 前往[IDaaS控制台](https://yundun.console.aliyun.com/?spm=5176.b73997031.idaas-instances.13.46007508OueBLp&p=idaaseiam&instanceId=idaas_rzpm34cpir2wlb6cg6z7sfn4ri&regionId=cn-hangzhou#/IdentityProvider/cn-hangzhou)->身份提供方->其他身份提供商->企业微信。在界面中填写我们的企业ID、AgentID、Secret、选择企业可信IP![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968972.png)
6. 检验企业微信用户到IDaaS是否同步完成。这里可以保存企微扫码登录地址![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968973.png)前往[IDaaS控制台](https://yundun.console.aliyun.com/?spm=5176.b73997031.idaas-instances.13.46007508OueBLp&p=idaaseiam&instanceId=idaas_rzpm34cpir2wlb6cg6z7sfn4ri&regionId=cn-hangzhou#/IdentityProvider/cn-hangzhou)->身份提供方->账户->账户与组织查看我们从企业微信同步过来的用户与组织![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968974.png)

#### 飞书同步

##### 飞书侧配置

1. 创建飞书应用。前往[飞书开放平台](https://open.feishu.cn/)，登录开发者后台。在开发者后台中创建企业自建应用。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968978.png)
2. 创建并发布应用![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968975.png)
3. 获取IDaaS测配置所需企业与应用信息
4. 点击左侧**凭证与基础信息**菜单，获取**App ID和App Secret**，后续会填写到IDaaS中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968981.png)
5. 在[飞书管理后台](http://www.feishu.cn/admin)中获取企业编号![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968976.png)

1. 分配飞书API权限。在飞书应用详情页，点击**权限管理**菜单，在 API 权限中，分别进行如下授权。这些均属于通讯录的查询权限，以实现数据同步和用户登录。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968990.png)权限名称权限值获取通讯录基本信息contact:contact.base:readonly获取用户 user IDcontact:user.employee_id:readonly获取部门基础信息contact:department.base:readonly获取通讯录部门组织架构信息contact:department.organize:readonly获取用户组织架构信息contact:user.department:readonly获取用户基本信息（可选）contact:user.base:readonly获取用户邮箱信息（可选）contact:user.email:readonly获取用户手机号（可选）contact:user.phone:readonly
2. 分配飞书数据权限。在**权限管理 > 数据权限**中，选择通讯录权限范围进行数据权限授权。这个范围决定哪些用户、组织数据可以同步到IDaaS并使用飞书登录。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968977.png)

##### IDaaS侧配置接入飞书

1. 前往[IDaaS控制台](https://yundun.console.aliyun.com/?spm=5176.b73997031.idaas-instances.13.46007508OueBLp&p=idaaseiam&instanceId=idaas_rzpm34cpir2wlb6cg6z7sfn4ri&regionId=cn-hangzhou#/IdentityProvider/cn-hangzhou)->身份提供方->其他身份提供商->飞书。在界面中填写我们的企业ID、APP ID、APP Secret，并点击下一步进行通路检验。注意这里的ID以及Secret的**泄漏风险**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968979.png)
2. 填入企业信息并选择要同步入的组织![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968991.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968980.png)能力说明：同步目标：飞书的通讯录数据将会导入到IDaaS的这个节点之下。定时校验：IDaaS将于每日凌晨自动全量同步企业微信来源节点下的全量数据。未来将支持增量同步能力。您可以在字段映射中设置映射标识，使用IDaaS账户的某个字段（如账户名）与飞书用户的某个字段（如`userid`）进行匹配，如果匹配成功，将绑定并覆盖更新；否则将创建IDaaS账户。如果需要及时同步数据，请手动触发全量同步。IDaaS内置了同步保护能力， 当30个以上的账户或10个以上的组织需要被删除时，自动取消同步任务，以防止数据被误删除。建议根据企业规模调整同步保护设置。扫码登录：开启后，会在登录菜单中创建飞书扫码登录，并处于启用状态，可直接扫码登录。如果在上一步配置了应用主页，则支持在飞书工作台中免登到IDaaS。
3. 配置同步字段映射。如果您在 IDaaS 中已存在存量数据，需要飞书成员/部门和IDaaS账户/组织绑定，或者希望使用飞书中成员的某些字段数据作为IDaaS账户的数据，例如将飞书用户的姓名作为IDaaS账户的显示名，则需要在第四步配置字段映射。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968982.png)
4. 检验飞书用户到IDaaS是否同步完成![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968983.png)前往[IDaaS控制台](https://yundun.console.aliyun.com/?spm=5176.b73997031.idaas-instances.13.46007508OueBLp&p=idaaseiam&instanceId=idaas_rzpm34cpir2wlb6cg6z7sfn4ri&regionId=cn-hangzhou#/IdentityProvider/cn-hangzhou)->身份提供方->账户->账户与组织查看我们从飞书同步过来的用户与组织![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968992.png)

#### 将IDaaS的用户同步至SSO

1. 登录 [云SSO 控制台](https://cloudsso.console.aliyun.com/)，在左侧导航栏，单击**设置**。单击SCIM用户同步配置下方按钮，**开启SCIM同步**，**复制保存SCIM服务端地址**备用。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968984.png)
2. 创建用户同步应用
3. 访问[IDaaS实例](https://yundun.console.aliyun.com/?spm=5176.21213202.J_5253785160.2.41476a01AOlxtn&p=idaas#/overview/new/cn-hangzhou)
4. 在左侧点击应用
5. 添加应用并选择添加阿里云云SSO应用 ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968993.png)
6. 使用应用进行IDaaS与云SSO的同步任务推送![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968986.png)
7. 同步成功并去日志页面验证![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968985.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968987.png)
8. 前往[云SSO控制台](https://cloudsso.console.aliyun.com/cn-shanghai/users)检验用户是否成功同步![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2966581571/p968994.png)

#### 为云SSO用户分配登录权限或角色

1. 需手动操作逐个用户重置密码，或者使用自动化工具。点击用户重置密码，建议配合上控制栏左侧“设置”中的限制强密码策略并勾选上“要求用户下次登录时重置密码”![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968988.png)
2. 为SSO用户分配权限或赋予角色。可参考最佳实践文档[云SSO配置角色&用户指南](https://help.aliyun.com/zh/cloudsso/user-guide/perform-basic-operations-1)
3. 使用云SSO登录账号并验证![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968989.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1966581571/p968995.png)

### 故障排除

#### IDaaS无法连接到飞书/企业微信

- 请确认配置可信域名以及企业可信IP
- 请确认IP地址、端口、应用ID填写正确，管理员账户密码填写正确并具有相应权限。

#### IDaaS无法连接到云SSO

- 请确认IDaaS中云SSO的SCIM服务端地址填写正确。
- 请确认IDaaS中云SSO的Bearer Token填写正确，尝试在云SSO中重新生成密钥更新到IDaaS中，配置页面**单击保存**后再尝试连接。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-258（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
