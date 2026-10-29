<!-- source: https://help.aliyun.com/zh/well-architected/solution-260 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929478 -->

# 基于函数计算实现从IdP到IDaaS的人员定时同步方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973093.png)

企业想要实现员工从IdP到IDaaS的同步，做完首次初始同步后，每次新增员工后，如果必须手动到IDaaS触发同步，或IDaaS默认的同步周期无法满足企业要求时，可以采用此方案实现自动化定时同步。本文档介绍了一种通过函数计算定时调用IDaaS同步的OpenAPI，实现按照自定义周期进行人员自动从IdP到IDaaS同步的方法。

## 方案优势

本方案能够实现企业在从IdP到IDaaS同步过程中，对自动化、个性化、安全的多方位需求。

### IDaaS自动同步

通过函数计算调用云身份服务（IDaaS EIAM）的OpenAPI接口（RunSynchronizationJob），并通过配置定时触发器，实现从企业IdP到IDaaS的自动同步功能。

### 同步周期自定义

通过对函数定时触发器的时间间隔配置，实现同步周期的自定义，满足企业的个性化需求。

### 提高安全性

通过FC函数角色和RAM角色关联，使用STS Token访问云资源，避免了将访问密钥硬编码在代码中，从而消除AK泄露的风险。临时凭证（STS Token）的使用有效解决了永久凭证（AK/SK）可能带来的安全风险问题。

### 精细化管理权限

通过为不同FC函数赋予具有特定授权策略的RAM角色，确保函数仅能访问其所需的资源，实现权限最小化。

## 客户场景

### 从IdP到IDaaS的自定义周期同步

#### 场景描述

企业在从IdP到IDaaS的同步过程中，出于对成本和权限管理的考量，只想对部分人员进行同步，同时在日常维护过程中，想要对人员进行增删操作，但不想手动到云身份服务控制台触发同步。

#### 适用客户

- 部分人员需要同步到IDaaS的企业客户。
- 对云上资源访问安全性要求高的企业客户。
- 对成本有把控要求的企业客户。
- 对IDaaS同步时间间隔有个性化需求的企业客户。
- 对运维过程自动化要求高的企业客户。

## 方案架构

本方案通过函数计算实现自定义周期的从IdP到IDaaS的同步。该流程通过调用触发IDaaS同步的OpenAPI接口，实现从IdP到IDaaS的同步，通过将接口调用部署在函数计算中，实现该过程的自动化。通过临时授予访问权限，避免了AK暴露的风险，提高了系统的安全性。

在管理员账号下创建RAM角色，并授信给函数计算服务（图中1）。管理员创建只拥有调用IDaaS触发同步API的权限策略，为函数角色授予该自定义权限，并将该角色配置到对应的函数上，使函数与角色关联（图中2）。函数计算内根据上下文Context获取STS Token（图中3）。该函数调用IDaaS触发同步API，将企业IdP中的用户增删同步至IDaaS（图中4）。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973092.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云身份服务IDaaS | [云身份服务 IDaaS](https://help.aliyun.com/zh/idaas/eiam/product-overview/what-is-idaas)（英文名：Alibaba Cloud IDentity as a Service，简称 IDaaS）是阿里云为企业用户提供的云原生的、经济的、便捷的、标准的身份、权限管理体系。 | 分为免费版和企业收费版，详情参见[产品计费](https://help.aliyun.com/zh/idaas/eiam/product-overview/pricing)。 |
| 函数计算 | [函数计算（Function Compute）](https://www.alibabacloud.com/product/function-compute)函数计算是事件驱动的全托管计算服务。使用函数计算，您无需采购与管理服务器等基础设施，只需编写并上传代码。函数计算为您准备好计算资源，弹性地、可靠地运行任务，并提供日志查询、性能监控和报警等功能。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/functioncompute/product-overview/billing-overview)。 |
| RAM | [访问控制（RAM）](https://help.aliyun.com/product/28625.html)是阿里云提供的一项管理用户身份与资源访问权限的服务。使用RAM，您可以创建、管理RAM角色（例如员工、系统或应用程序），并可以控制这些RAM角色对资源的操作权限。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| IdP | Identity Provider，身份提供方。源自于 SAML 协议中定义，IdP 为进行用户认证、鉴权，并返回 SAML Response 结果信息给 SP 的身份提供方，后通用化指统一身份管理平台。 |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| RAM管理员 | RAM管理员具备账号下RAM资源的管理权限。RAM管理员可以是阿里云账号（主账号），也可以是主账号下拥有AliyunRAMFullAccess权限的RAM用户，强烈推荐您使用RAM用户充当RAM管理员。 |
| 访问密钥（AccessKey） | 访问密钥AccessKey（简称AK）是阿里云提供给用户的永久访问凭据，一组由AccessKey ID和AccessKey Secret组成的密钥对。发起的请求会携带AccessKey ID和AccessKey Secret加密请求内容生成的签名，进行身份验证及请求合法性校验。 |
| RAM角色（RAM role） | RAM角色是一种虚拟用户，可以被授予一组权限策略。与RAM用户不同，RAM角色没有永久身份凭证（登录密码或访问密钥），需要被一个可信实体扮演。扮演成功后，可信实体将获得RAM角色的临时身份凭证，即安全令牌（STS Token），使用该安全令牌就能以RAM角色身份访问被授权的资源。 |
| 函数RAM角色 | 函数通过函数RAM角色获得该角色拥有的权限，可以基于临时访问凭据STS（Security Token Service）访问指定云服务的API和操作指定的云资源，安全性更高。 |

## 安全性

### IDaaS

IDaaS采用“默认安全”的产品设计，在“可用性”和“安全性”难以两全的场景中，IDaaS 会优先保障“安全性”，在此基础上，尽可能追求“易用性”，详情参见[IDaaS默认安全设计](https://help.aliyun.com/zh/idaas/eiam/product-overview/default-security-solutions)。

### 传输

- **传输协议**：方案中相关产品使用业界标准的LDAP协议及SCIM协议保障数据安全传递，详情参见[LDAP](https://ldap.com/)及[SCIM](http://www.simplecloud.info/)。
- **传输加密**：IDaaS支持LDAP连接开启StartTLS，建议AD中配置证书并在数据同步时开启StartTLS提升传输安全性，详情参见[AD安全性配置](https://help.aliyun.com/zh/idaas/eiam/user-guide/bind-idaas-to-ad)。
- **数据权限**：需要准备AD管理员账户及密码，至少拥有只读权限，用于从AD同步身份数据。
- **公网访问**：目前企业IdP（如AD）需要**公网可访问**才能使用IDaaS免费版及企业版进行数据同步，建议在企业环境中开启针对AD的公网访问限制，并将IDaaS地址添加到白名单中。

### 函数计算服务关联角色

在某些场景下，函数计算为了完成自身的某个功能，需要获取其他云服务的访问权限，因此，函数计算创建了与云服务关联的角色，即服务关联角色（AliyunServiceRoleForFC）。函数计算3.0支持AliyunServiceRoleForFC和FaaS函数的绑定，实现最小授权范围内授予函数访问其他云服务的权限。

关于服务关联角色的更多信息，请参见[服务关联角色](https://help.aliyun.com/zh/ram/user-guide/service-linked-roles)。

### 函数计算安全性

阿里云函数计算是事件驱动的全托管计算服务。通过函数计算，用户无需管理服务器等基础设施，只需编写代码并上传。函数计算会为用户准备好计算资源，以弹性、可靠的方式运行用户的代码，并提供日志查询、性能监控和报警等功能。对于数据层面，在与用户通信时，函数计算使用TLS 1.2及以上协议加密传输调用请求及回包，内部通信使用私有协议防止信息泄露及篡改。对于管控层面，您可以通过阿里云访问控制（RAM）进行权限控制等等。关于函数计算安全性的详细信息，请参见[安全合规](https://help.aliyun.com/zh/functioncompute/security-and-compliance)。

## 注意事项

### 临时密钥有效期

函数计算根据函数配置的角色，通过AssumeRole获取一个临时密钥（STS Token）。该临时密钥的有效期为36小时，且不支持修改。函数的最大执行时间为24小时，因此，执行函数过程中，临时密钥不会过期。

### 支持STS的云服务

支持临时安全令牌（STS）的阿里云服务查询，请参见[支持STS的云服务](https://help.aliyun.com/zh/ram/services-that-work-with-sts)。函数计算在支持STS的云服务中，因此可以应用无AK方案。

### 自定义权限策略

为了收敛权限，确保函数仅能访问其所需的资源，创建的RAM角色只具有所需的特定策略的权限，因此需要自定义权限策略。

## 实施步骤

本方案实施步骤以钉钉为例，企业如果使用其他IdP，IDaaS绑定入方向身份提供方步骤可参考[基于IDaaS实现IdP用户同步至云SSO](https://help.aliyun.com/zh/well-architected/solution-146)。

### 实施准备

- 确保创建IDaaS实例，本示例使用免费版，详情可参见[免费开通实例](https://help.aliyun.com/zh/idaas/eiam/user-guide/eiam-sso-quick-start)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：30分钟。

### 操作步骤

#### 在IDaaS身份提供方绑定钉钉

1. 在[IDaaS控制台中](https://yundun.console.aliyun.com/?p=idaas#/overview/new/cn-hangzhou)单击已创建的**实例ID**或者单击操作列中的**访问控制台**，进入**云身份服务**控制台。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9886581571/p973118.png)
2. 在云身份服务控制台中，单击**快速入门**页面中的快速绑定钉钉，或者单击**身份提供方**页面中的快速绑定钉钉，然后单击**入方向**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973094.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973095.png)
3. 在快速绑定钉钉详情页面的第一步**绑定配置**中，同步目标选择**阿里云IDaaS**，禁用增量同步，启用钉钉扫码登录。在更多设置中，**不勾选触发一次全量同步**。然后单击下一步。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973096.png)
4. 在快速绑定钉钉详情页面的第二步中，使用企业钉钉管理员账户扫描屏幕上的二维码，开通IDaaS应用。开通后单击屏幕下方的下一步。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973097.png)
5. 在移动端，单击**立即开通**，在开通页面选择应用的**使用范围**，即选择特定的可以登录IDaaS的人员。单击**打开应用**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973119.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973098.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973120.png)
6. 在快速绑定钉钉详情页面的第三步中，在**移动端**单击**扫码绑定**后，扫描屏幕中的二维码。在PC端输入账户名和密码后单击登录，完成绑定。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973099.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973100.png)
7. 绑定成功后，单击**账户与组织**，即可查看已经**初始同步到IDaaS的人员**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973122.png)

#### 创建角色并授予自定义权限

1. 登录[RAM控制台](https://ram.console.aliyun.com/overview)，在左侧导航栏，单击**权限策略**，在权限策略页面中，单击**创建权限策略**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973101.png)
2. 单击**脚本编辑**，将下方代码复制粘贴，完成后单击**继续编辑基本信息**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973102.png)`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "eiam:RunSynchronizationJob",
 "Resource": "*"
 }
 ]
}`
3. 输入权限策略**名称**，单击**确定**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973123.png)
4. 单击左侧导航栏中的角色，单击创建角色。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973104.png)
5. 在**选择类型**页面，单击**阿里云服务**，进入下一步。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973103.png)
6. 在配置角色页面，单击**普通服务角色**，设置**角色名称**，并选择受信服务为**函数计算**。单击完成。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973124.png)
7. 创建角色完成后，单击**为角色授权**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973105.png)
8. 在选中的角色页面，单击**新增授权**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973106.png)
9. 在新增授权页面，单击**账号级别**，使用默认授权主体，搜索刚刚创建的自定义权限，并勾选。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973125.png)
10. 为了对函数计算触发器进行测试，增加**日志服务触发器调用函数计算**的权限策略。单击**确认新增授权**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973108.png)

#### 创建函数并绑定角色

以函数计算3.0为例

1. 登录函数计算控制台，在左侧导航栏，单击**函数**。进入函数详情页，单击**创建函数**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973126.png)
2. 单击**事件函数**，输入**函数名称**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973107.png)
3. 上传函数代码，代码详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-IDaaS-synchronization)。本方案提供Python的代码示例，帮助快速完成函数计算部署。代码上传后单击创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973127.png)
4. 单击刚刚创建的函数右侧的**配置**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973128.png)
5. 在函数详情页面，单击**权限**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9886581571/p973109.png)
6. 单击**编辑**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973111.png)
7. 搜索刚刚创建的角色**fc-sync-test**，单击**部署**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973129.png)
8. 在函数详情页，单击**代码**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973110.png)
9. 设置环境变量，其中，实例ID、同步目标 ID和同步目标类型可参考[OpenAPI-运行同步任务](https://api.aliyun.com/api/Eiam/2021-12-01/RunSynchronizationJob?spm=api-workbench.API%20Document.0.0.3b5e36fbKy68rq&RegionId=cn-hangzhou&tab=DEMO&lang=PYTHON)；IDaaS EIAM服务的Endpoint可参考[OpenAPI-IDaaS EIAM](https://api.aliyun.com/product/Eiam)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973130.png)实例ID可在EIAM云身份服务页面获取。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9886581571/p973131.png)同步目标 ID的获取方式：需在云身份服务-身份提供方页面，单击**触发同步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973112.png)单击**查看日志**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973132.png)单击**管理操作**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973113.png)获取**同步目标 ID**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973114.png)**同步目标类型**为identity_provider。
10. 单击测试函数，屏幕会显示执行成功。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973133.png)
11. 配置触发器。 函数详情页面，单击**触发器**，单击**创建触发器**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973116.png)
12. 在触发器类型下拉框中选择**定时触发器**，触发方式选择**时间间隔**，时间间隔可按企业实际需求设置。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973134.png)
13. 创建完成后，可在日志中查看函数调用时间和结果。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973115.png)

#### IDaaS查看同步结果

1. 登录[云身份服务控制台](https://yundun.console.aliyun.com/?spm=5176.b73997031.idaas-instances.13.27cf7508M80OSa&p=idaaseiam&instanceId=idaas_u5ubss5hrcbb63tqwbvn3vvpbe&regionId=cn-hangzhou#/overview/undefined)，单击已有实例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973117.png)
2. 单击**查看日志**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9886581571/p973135.png)
3. 即可看到历史同步结果。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8886581571/p973121.png)

## 源代码

### 代码介绍

本方案提供Python的代码示例，方便客户能够快速完成函数计算部署。

需要注意以下内容：

- 在函数创建时要勾选对应的运行环境。
- 需要配置以下环境变量： {'IDAAS_EIAM_ENDPOINT', 'INSTANCE_ID', 'TARGET_ID', 'TARGET_TYPE' }。

### 代码地址

代码详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-IDaaS-synchronization)。

## 故障排除

### 函数无法运行？

- 请检查函数计算版本是否为3.0
- 请检查相关权限是否配置正确
- 请检查依赖包版本是否正确

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-260（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
