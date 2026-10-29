<!-- source: https://help.aliyun.com/zh/well-architected/solution-267 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2927567 -->

# 本地开发和运维的临时凭证使用方案

针对研发、运维、产品等职能员工，需要在本地进行云上资源运维、管理以及应用程序调试等操作场景，本方案介绍了一种使用临时凭证代替AccessKey的使用方案，减少AccessKey的泄露风险。

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9076581571/p965749.png)

凭证管理是云上最容易出现风险的环节之一，管理不善将导致凭证泄漏，进而导致数据泄漏、资产损失等严重安全事故。当您的研发团队在本地进行应用程序的开发调试或者运维团队进行本地运维时，需要访问云上资源，传统的方式是将RAM用户的AccessKey明文放到本地，比如写在程序配置文件或者本地环境变量中，容易造成AK泄露，并且存在运维和追踪困难的问题。

本方案介绍一种在本地研发调试和运维的场景下，使用临时凭证STS Token代替固定AccessKey使用的方案。避免出现AccessKey硬编码在代码或者本地环境变量中，从而规避AK泄露，解决AccessKey颁发出去后难以管理追踪的难题。

## 方案优势

### 增强的安全性

**减少凭证泄露风险：** 传统方式中，AK/SK长期有效且容易暴露（例如存储在代码中、配置文件中）。通过SSO，用户不需要直接持有敏感的AK/SK，减少了凭证泄露的风险。SSO使用短期有效的临时凭证（STS Token），凭证一旦泄露，由于其有限的有效期和精细的权限控制，即使被盗用，风险也较低。

**多因素认证（MFA）支持：** 企业的SSO平台通常集成了多因素认证（MFA），即除了密码外，用户还需要提供其他形式的验证（如短信验证码、动态口令等），这大大增强了身份验证的安全性。这样即使密码泄露，攻击者也难以通过简单的凭证获取云服务访问权限。

**减少对AK/SK的暴露：** 用户的操作可以通过临时凭证来完成，不需要直接使用和管理AK/SK。系统后台通过SSO验证用户身份并自动生成有效期较短的凭证，从而减少了暴露的可能性。

### 统一的身份与 权限管理

**集中身份管理：** SSO系统能够统一管理所有用户的身份信息，管理员可以集中配置、维护和监控用户的访问权限。相比于单独管理每个用户的身份，SSO使得身份和权限管理更加高效、可靠。

**按角色分配权限：** 在SSO框架下，企业可以根据不同用户的角色和需求动态分配访问权限。例如，开发人员可以获取与开发相关的权限，运维人员可以获取与运维相关的权限，所有权限控制都基于身份和角色进行管理，避免了手动管理所带来的权限过大或不匹配的风险。

**自动化用户生命周期管理：** 在SSO系统中，用户的访问权限可以根据其角色、职位变动等自动调整。例如，当员工离职或岗位变动时，可以自动撤销其对云服务的访问权限，确保系统的安全性。

## 客户场景

### 本地开发/运维使用临时凭证

#### 场景描述

研发团队和运维团队通常需要频繁访问云资源以进行开发调试、测试或运维管理。传统场景下，开发人员和运维人员会使用固定凭据来访问云资源，将AccessKey和SecretKey保存在本地配置文件、环境变量中，或者硬编码到应用程序中，这会带来许多安全风险。一旦这些凭证泄露，可能导致未经授权的访问和数据泄露。为了解决这一问题，本地开发运维也推荐采用临时凭证（STS Token）的方案，通过RAM SSO或云SSO获取到临时凭证访问阿里云。

#### 适用客户

- **安全合规性要求高**：企业在云服务上部署了大量应用和基础设施，开发和运维人员需要频繁访问云资源。使用SSO通过临时凭证访问阿里云，避免了直接暴露敏感凭证（如AK/SK）给员工，降低了泄漏的风险。
- **复杂的权限和角色管理：** 如果企业内部存在复杂的权限和角色划分（如开发、运维、财务等），通过SSO可以根据不同的角色授予不同的云服务访问权限，确保资源访问遵循最小权限原则。
- **跨云平台访问：** 在多云或混合云环境中，企业往往需要访问不同云厂商的服务。SSO可以为用户提供跨多个云平台（如AWS、Azure、阿里云等）的统一身份认证和访问控制，避免了为每个平台单独管理AK/SK，提升了跨云操作的便捷性和安全性。
- **频繁离职和岗位变动的公司：** 在员工频繁离职或岗位变动的企业中，SSO能够确保员工离职后立即撤销其访问权限，避免延误，降低安全风险。企业可以实时调整员工的云服务访问权限，确保其仅在必要时能够访问相关资源。

## 方案架构

本方案介绍一种在本地研发调试和运维的场景下，使用临时凭证STS Token代替固定AccessKey进行认证授权的方案。开发或运维团队人员通过命令行工具saml2alibabacloud或云SSO CLI以SSO的方式登录阿里云，获取到临时凭证信息（STS Token）（图中1）。该过程中会调用AssumeRoleWithSAML接口，以身份提供商（IdP）的身份扮演RAM角色，从RAM/STS服务获取STS Token，该过程对于用户而言无感知（图中i）。 开发或运维团队使用获取到的STS Token来调用目标云资源服务的API。此时，将使用凭证进行认证和授权（图中2）。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9076581571/p965750.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 访问控制RAM | [访问控制RAM（Resource Access Management）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |
| 云SSO | [云SSO](https://help.aliyun.com/zh/cloudsso/product-overview/what-is-cloudsso)提供基于阿里云资源目录RD（Resource Directory）的多账号统一身份管理与访问控制。使用云SSO，您可以统一管理企业中使用阿里云的用户，一次性配置企业身份管理系统与阿里云的单点登录，并统一配置所有用户对RD账号的访问权限。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 访问密钥（AccessKey） | 访问密钥AccessKey（简称AK）是阿里云提供给用户的永久访问凭据，一组由AccessKey ID和AccessKey Secret组成的密钥对。发起的请求会携带AccessKey ID和AccessKey Secret加密请求内容生成的签名，进行身份验证及请求合法性校验。 |
| RAM用户（RAM User） | RAM用户也叫RAM账号，是RAM的一种实体身份类型，有确定的身份ID和身份凭证，它通常与某个确定的人或应用程序一一对应。 |
| RAM角色（RAM Role） | RAM角色是一种虚拟用户，可以被授予一组权限策略。与RAM用户不同，RAM角色没有永久身份凭证（登录密码或访问密钥），需要被一个可信实体扮演。扮演成功后，可信实体将获得RAM角色的临时身份凭证，即安全令牌（STS Token），使用该安全令牌就能以RAM角色身份访问被授权的资源。 |
| 服务提供商（SP） | 利用IdP的身份管理功能，为用户提供具体服务的应用。SP会使用IdP提供的用户信息。一些非SAML协议的身份系统（例如：OpenID Connect），也把服务提供商称作IdP的信赖方。 |
| 身份提供商（IdP） | 一个包含有关外部身份提供商元数据的RAM实体，身份提供商可以提供身份管理服务。企业本地IdP：Microsoft Active Directory Federation Service（AD FS）以及Shibboleth等。Cloud IdP：Azure AD、Google G Suite、Okta以及OneLogin等。 |
| 安全断言标记语言（SAML 2.0） | 实现企业级用户身份认证的标准协议，它是SP和IdP之间实现沟通的技术实现方式之一。SAML 2.0已经是目前实现企业级SSO的一种事实标准。 |
| 单点登录（SSO） | 阿里云支持基于SAML 2.0和OIDC的SSO（Single Sign On，单点登录），也称为身份联合登录。 |

## 安全性

### 云SSO服务关联角色

服务关联角色（AliyunServiceRoleForCloudSSO）具有操作RAM角色、权限策略和服务提供商等的权限，方便云SSO进行RD统一权限配置。关于服务关联角色的更多信息，请参见[服务关联角色](https://help.aliyun.com/zh/ram/user-guide/service-linked-roles)。

## 注意事项

### 支持RAM/STS的云服务

阿里云RAM/STS服务已经支持大部分云产品，例如：云服务器ECS、 云数据库RDS、对象存储OSS、专有网络VPC、负载均衡和容器服务Kubernetes版等。在此基础上，RAM/STS服务也在不断扩展对其他云服务的支持。企业可以根据云服务是否支持RAM/STS，决定采用的SSO类型。更多信息，请参见[支持RAM的云服务](https://help.aliyun.com/zh/ram/product-overview/services-that-work-with-ram)和[支持STS的云服务](https://help.aliyun.com/zh/ram/services-that-work-with-sts)。

### AccessKey网络访问限制使用限制

通过指定允许AccessKey调用的来源地址，限制AccessKey只能从这些网络地址调用阿里云API，将AccessKey调用来源控制在可信的网络环境内，提升AccessKey的安全性。目前存在如下限制：

- AccessKey网络访问限制策略功能目前处于邀测阶段，请先联系阿里云的服务经理，申请体验资格后才能进行试用。
- AccessKey网络访问限制策略对除云消息队列RocketMQ版、云消息队列RabbitMQ版、云消息队列MQTT版、事件总线EventBridge、轻量消息队列、云监控（通过HTTP上报事件监控数据功能）、实时数仓Hologres以外的所有云产品生效，未支持的云产品上线时间由云产品另行通知。
- 云账号和单个AccessKey均支持最多添加8条网络访问限制策略，其中公网策略最多添加1条。
- 每条策略最多包含50个IP地址或IP地址段。

## 实施步骤

### 实施准备

**单账号场景**：

- 确保已在云账号内配置角色SSO，并按职能为员工分配RAM角色。更多信息，请参见[角色SSO](https://help.aliyun.com/zh/ram/role-based-sso/)。
- 已安装[saml2alibabacloud](https://github.com/aliyun/saml2alibabacloud)工具。

**多账号场景**：

- 确保企业已集成云SSO，支持基于SAML 2.0的单点登录（SSO登录），即企业员工可以使用IdP中的用户身份直接登录云SSO。更多信息，请参见[云SSO单点登录](https://help.aliyun.com/zh/cloudsso/user-guide/overview)。
- 已安装云SSO CLI，详情参见[安装CLI](https://www.alibabacloud.com/help/zh/cloudsso/user-guide/use-alibaba-cloud-cli-to-access-cloudsso-and-alibaba-cloud-resources#section-zvq-a07-i4h)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：30分钟。

### 操作步骤

#### 基于SSO获取临时凭证

##### 单账号场景

员工可以在命令行中使用[saml2alibabacloud](https://github.com/aliyun/saml2alibabacloud)工具，完成IdP侧的认证后，即可获取到STS Token。本示例以Okta为例。

1. 执行以下命令，开始配置IdP账号信息`-a`设置IdP账号的名称，当需要配置多个账号时，可以作为区分标识`-p`设置配置的名称，当存在多个配置时，可以作为区分标识`saml2alibabacloud configure -a dev -p dev`
2. 根据交互式的命令行指引，完成相关信息填写`? Please choose a provider: Okta
? Please choose an MFA Auto
? URL https:************
? Username ************
? Password ************
? Confirm ************

account {
 URL: ************
 Username: ************
 Provider: Okta
 MFA: Auto
 SkipVerify: false
 SessionDuration: 3600
 Profile: dev
 RoleARN:
 Region:
}

Configuration saved for IDP account: dev`
3. 执行以下命令，登录配置好的IdP账号，并且获取到STS保存到身份凭证配置文件`profile`中。身份凭证配置文件`profile`是一个可自定义名称的设置集，所有身份凭证与设置项均以JSON格式存储在`config.json`文件中。该文件位于您个人用户目录下的`.aliyun`文件夹中，个人用户目录位置因操作系统而异。Windows环境：`C:\Users\ < USERNAME> \.aliyun`Linux或macOS：`~/.aliyun``saml2alibabacloud login -a dev -p dev`
4. 执行以下命令查看临时凭证信息，结果以环境变量的方式输出，方便设置为环境变量使用。`saml2alibabacloud script -a dev -p dev

export ALIBABA_CLOUD_ACCESS_KEY_ID="STS.NTh..............8xN"
export ALIBABA_CLOUD_ACCESS_KEY_SECRET="CYc................T5M"
export ALIBABA_CLOUD_SESSION_TOKEN=""
export ALIBABA_CLOUD_SECURITY_TOKEN="CAI................xxP"
export ALICLOUD_ACCESS_KEY="STS.NTh................8xN"
export ALICLOUD_SECRET_KEY="CYc................T5M"
export ALICLOUD_SECURITY_TOKEN="CAI................xxP"
export ALICLOUD_PROFILE="dev"
export SAML2ALIBABA_CLOUD_PROFILE="dev"`

##### 多账号场景

建议使用云SSO进行多账号的单点登录配置。配置完成后，员工即可使用云SSO CLI通过SSO方式登录并获取到STS Token。

**配置云SSO登录信息**：

1. 执行以下命令，配置云SSO登录信息。`acs-sso configure`
2. 输入用户登录地址`signinUrl`。（用户登录地址`signinUrl`获取方法：登录[云SSO控制台](https://cloudsso.console.aliyun.com/)，在概览页面的右侧，获取用户登录URL）配置成功后返回`configuration done!``acs-sso configure
? please input 'signinUrl': https://signin-******.alibabacloudsso.com/device/login

configuration done!`

**云SSO用户登录阿里云**：

1. 执行以下命令，开始登录。当存在多个RD账号和访问配置所对应的SSO登录信息时，可以通过指定**登录配置名称**来区分。您可以使用`--profile`指定云SSO的不同登录配置名称（登录配置不存在时会新建）。不指定`--profile`时，默认使用的登录配置名称是default。`acs-sso login --profile log-archive`
2. 在弹出的浏览器窗口中，根据界面提示，完成云SSO用户登录，登录成功后请关闭浏览器窗口。（如果浏览器窗口未弹出，您可以根据CLI的提示信息，手动复制登录URL和用户码完成登录）`If your default browser is not opened automatically, please use the following URL to finish the signin process.

Signin URL: https://signin-****.alibabacloudsso.com/device/code
User Code: *********`
3. 如果当前用户被授予了多个RD账号的访问权限，CLI会交互式地提醒您选择要使用的RD账号和访问配置，并最终生成相应的阿里云访问密钥。`You have logged in.
? You have xx accounts, please select one: log-archive(122479502903****)
Used account: log-archive(122479502903****)
Used access configuration: Administrator(ac-00pnro8rbbtrwit7****)
{
 "mode": "StsToken",
 "access_key_id": "STS.****",
 "access_key_secret": "****",
 "sts_token": "****"
}`

登录成功后，`profile`会绑定该RD账号和访问配置。下次登录时，将会使用本次缓存的RD账号和访问配置直接登录。您可以通过执行以下命令，获取登录配置列表：

```
acs-sso profile --list
```

输出示例如下：

```
┌───────────────┬──────────────────┬─────────────────────────┬───────────┐
│ Profile       │ Access ID        │ Access Configuration ID │ Status    │
├───────────────┼──────────────────┼─────────────────────────┼───────────┤
│ default       │ 192519502903**** │ ac-00pnro8rbbtrwit7**** │ Expired   │
├───────────────┼──────────────────┼─────────────────────────┼───────────┤
│ security      │ 168729502902**** │ ac-00pnro8rbbtrwit7**** │ Expired   │
├───────────────┼──────────────────┼─────────────────────────┼───────────┤
│ net           │ 137409502931**** │ ac-00pnro8rbbtrwit7**** │ Expired   │
├───────────────┼──────────────────┼─────────────────────────┼───────────┤
│ log-archive * │ 122479502903**** │ ac-00pnro8rbbtrwit7**** │ Available │
└───────────────┴──────────────────┴─────────────────────────┴───────────┘
```

#### 使用临时凭证（STS）场景

##### 阿里云CLI

阿里云CLI（Alibaba Cloud Command Line Interface）是基于[OpenAPI](https://help.aliyun.com/zh/openapi/what-is-openapi)建立的通用命令行工具，您可以借助阿里云CLI实现与阿里云产品的交互，在Shell工具中管理您的阿里云产品。如果您还未安装阿里云CLI，请参见[安装指南](https://help.aliyun.com/zh/cli/installation-guide/)。

在使用阿里云CLI之前，您需要配置调用阿里云资源所需的凭证信息、地域、语言等。阿里云CLI支持多种身份凭证，详情请参见[身份凭证类型](https://help.aliyun.com/zh/cli/configure-credentials/)。

对于**单账号场景**，通过上述[saml2alibabacloud获取到临时凭证](#ADTDr)章节完成配置，即可直接使用阿里云CLI调用API

1. 使用如下命令登录获取临时凭证`saml2alibabacloud login -a dev -p dev`
2. 登录成功后会直接将身份凭证配置写入配置文件中`Authenticating as ******@alibaba-inc.com ...
Selected role: acs:ram::129049502683****:role/okta-admin
Requesting AlibabaCloud credentials using SAML assertion
Logged in as: acs:ram::129049502683****:role/okta-admin/******@alibaba-inc.com

Your new access key pair has been stored in the AlibabaCloud CLI configuration
To use this credential, call the AlibabaCloud CLI with the --profile option (e.g. aliyun --profile dev sts GetCallerIdentity --region=cn-hangzhou).`
3. 使用阿里云CLI时，在命令后通过`--profile`选项，以使用指定的身份凭证配置。以调用`sts`服务的`GetCallerIdentity`接口为例：。`aliyun --profile dev sts GetCallerIdentity --region=cn-hangzhou`

对于**多账号场景**，通过上述[云SSO CLI获取临时凭证](#e1nRW)。在使用阿里云CLI时，建议配置**External**类型凭证，阿里云CLI在使用时会执行程序命令，获取返回结果作为凭证。另外，通过`--profile`选项，以使用指定的身份凭证配置。建议您在阿里云CLI和云SSO CLI指定相同的`profile`名称，这样当有多个云SSO登录配置时，可以多次配置CLI凭证，并匹配不同的云SSO登录配置。

1. 调用`aliyun configure set`命令，使用非交互式方式配置凭证，命令示例如下：`aliyun configure set \
 --profile log-account \
 --region cn-hangzhou \
 --mode External \
 --process-command 'acs-sso login --profile log-account'``--profile`：指定配置名称。如果指定的配置存在，则修改配置。若不存在，则创建配置。`--region`：指定默认地域。详情请参见[地域和可用区](https://help.aliyun.com/zh/ecs/user-guide/regions-and-zones)。`--mode`：指定配置的凭证类型，默认为**AK**类型。更多关于支持类型的详细信息，请参见[身份凭证类型](https://help.aliyun.com/zh/cli/configure-credentials/)。`--process-command`：指定用于获取凭证的外部程序命令。
2. 配置成功后，可以使用`aliyun configure list`命令获取身份凭证列表，更多信息，请参见[配置凭证相关命令](https://help.aliyun.com/zh/cli/other-configure-command-operations)。`Profile | Credential | Valid | Region | Language
--------- | ------------------ | ------- | ---------------- | --------
akProfile * | AK:**** | Valid | **** | en
stsTokenProfile | StsToken:**** | Valid | **** | en
ramRoleArnProfile | RamRoleArn:**** | Valid | **** | en
ecsRamRoleProfile | EcsRamRole:**** | Valid | **** | zh`
3. 配置成功后，即可通过CLI调用阿里云服务，以`sts`服务的`GetCallerIdentity`接口为例：。`# 使用log-archive配置的凭证进行调用
aliyun sts GetCallerIdentity --profile log-archive

# 使用shared-services配置的凭证进行调用
aliyun sts GetCallerIdentity --profile shared-services`

##### ossbrowser

[ossbrowser](https://help.aliyun.com/zh/oss/developer-reference/ossbrowser-2-0-overview/)是一款用于管理OSS的免费图形化桌面客户端。该客户端支持Windows、macOS和Linux操作系统，提供直观的图形用户界面，使您能够高效地执行各种操作，包括文件的上传、下载和删除。ossbrowser支持STS登录方式。您可以使用saml2alibabacloud工具或云SSO CLI获取到的临时凭证进行登录。

1. 在登录框单击**AK登录**，并填写临时访问凭证中`AccessKey ID`、`AccessKey Secret`和`SecurityToken`进行登录。（**AccessKeyID**文本框信息符合`STS.*****`格式后，**STS Token**文本框才显示）![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9076581571/p965748.png)

##### ossutil

[ossutil](https://help.aliyun.com/zh/oss/developer-reference/ossutil-overview/)支持通过Windows、Linux和macOS系统以命令行方式管理OSS数据。您可以使用saml2alibabacloud工具或云SSO CLI获取到的临时凭证进行登录。通过命令行方式配置需要传入访问密钥，可能会被日志系统记录，存在密钥泄露的风险，请谨慎使用。建议通过环境变量的方式配置访问凭证。

```
export OSS_ACCESS_KEY_ID=STS.LTAI4Fw2NbDUCV8z********
export OSS_ACCESS_KEY_SECRET=67DLVBkH7EamOjy2W5RVAH********
export OSS_SESSION_TOKEN=yourSecurityToken
export OSS_REGION=cn-hangzhou
```

##### 本地开发调试

本地开发调试需要使用凭证信息访问阿里云时，您可以将saml2alibabacloud工具或云SSO CLI获取到的临时凭证配置为环境变量，在程序中使用。

对于**单账号场景**，先参考[saml2alibabacloud获取临时凭证](#ADTDr)章节完成配置。

1. 使用如下命令登录获取临时凭证`saml2alibabacloud login -a dev -p dev`
2. 登录成功后通过如下命令输出临时凭证信息，将所需的内容配置为环境变量即可`saml2alibabacloud script -a dev -p dev`

对于**多账号场景**，通过上述[云SSO CLI获取临时凭证](#e1nRW)章节完成配置。

1. 使用如下命令登录获取临时凭证`acs-sso login --profile account1 --env`
2. 登录成功后输出临时凭证信息（三种命名格式），将所需的内容配置为环境变量即可`export ALIBABA_CLOUD_ACCESS_KEY_ID=STS.NUyPeEoab****
export ALIBABA_CLOUD_ACCESS_KEY_SECRET=GBubpmh****
export ALIBABA_CLOUD_SECURITY_TOKEN=CAIS****

export ALIBABACLOUD_ACCESS_KEY_ID=STS.NUyPeEoab****
export ALIBABACLOUD_ACCESS_KEY_SECRET=GBubpmh****
export SECURITY_TOKEN=CAIS****

export ALICLOUD_ACCESS_KEY=STS.NUyPeEoab****
export ALICLOUD_SECRET_KEY=GBubpmh****
export ALICLOUD_SECURITY_TOKEN=CAIS****`

#### 使用固定凭证（AK）场景

当您未使用SSO，或者使用的云服务目前暂不支持STS（详情请参见[支持STS的云服务](https://help.aliyun.com/zh/ram/services-that-work-with-sts)）。依然只能使用固定AccessKey时。请尽量遵循以下AccessKey在本地环境下的最佳使用原则：

- 推荐企业通过KMS实现固定AccessKey的统一管理、加密存储、自动轮转，降低凭证泄露风险。为了更高的安全性，通常建议您合理设置网络规则，基于来源IP限制访问。更多信息，请参见解决方案[通过KMS实现固定AccessKey的集中管控](https://help.aliyun.com/zh/well-architected/solution-237)。
- 如果您使用一些配置中心服务来集中管理AccessKey（例如Nacos、Apollo等）：请确保不要直接将 AccessKey存储为明文配置，可以进行加密后再存储。需要为配置中心设置严格的权限控制。确保只有有权限的应用、服务或人员能够访问敏感配置。为了更高的安全性，建议在配置中心服务器前端的网络设备（如防火墙、路由器或负载均衡器）上配置相应的访问控制规则，例如IP白名单。配置中心中的 AccessKey 信息应该定期轮换。可以使用自动化的工具或脚本进行轮换，减少密钥泄漏的风险。
- 如果没有实现集中的AccessKey管理，建议通过环境变量配置并使用AccessKey，禁止将AccessKey硬编码到代码中。
- 该AccessKey只应该用于本地运维/开发使用，不同应用之间不混用，应用不同环境之间不混用。
- 遵循最小化权限原则，只赋予该AccessKey所需的最小权限。
- 为该AccessKey设置IP白名单，保证只能企业内部环境（本地调试环境）调用。具体操作请参见[AccessKey网络访问限制策略](#fOX5b)。

##### AccessKey网络访问限制策略

该功能目前处于邀测阶段，请先联系阿里云的服务经理，申请体验资格后才能进行试用。更多限制，参考[使用限制](#oMVjg)。

通过指定允许AccessKey调用的来源地址，限制AccessKey只能从这些网络地址调用阿里云API，将AccessKey调用来源控制在可信的网络环境内，提升AccessKey的安全性。

RAM提供以下两种AccessKey网络访问限制策略：

- **账号级AccessKey网络访问限制策略：**该策略默认对云账号内所有AccessKey生效，包括主账号AccessKey和RAM用户AccessKey，但对设置了AccessKey级网络访问限制策略的AccessKey不生效。
- **AccessKey级网络访问限制策略：**该策略对单个AccessKey生效，当一个AccessKey设置了AccessKey级网络访问控策略后，账号级AccessKey网络访问限制策略对该AccessKey不生效。

网络访问限制策略配置后会立即生效，建议您在配置前参考AccessKey审计记录，结合企业网络管理信息，梳理可信的网络地址列表，确保访问策略地址准确和完整。

**账号级AccessKey网络访问限制策略**具体配置步骤如下：

1. 使用RAM管理员登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 在**设置**页面的**网络访问限制**区域，单击**允许通过AccessKey访问的来源网络地址**右侧的**修改**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9076581571/p965751.png)
3. 在**账号级网络访问限制策略**对话框，设置账号级公网策略和专有网络策略。公网策略：需填入公网IP地址或IP地址段，支持IPv4和IPv6格式。不创建公网策略代表所有公网IP来源均可通过。因此，若要拒绝所有公网访问，需要填入非公网地址，例如：`127.0.0.1`。专有网络策略：需填入VPC ID和VPC内的IP地址或IP地址段，支持IPv4和IPv6格式。不创建专有网络策略代表所有来自专有网络的调用均可通过。创建专有网络策略，在IP列表中填入`0.0.0.0/0`或`::/0`，表示允许该VPC内的所有IP地址的访问。支持一条策略中输入多个IP地址或IP地址段，多个IP地址使用空格、半角逗号（,）或半角分号（;）分隔。

**AccessKey级网络访问限制策略**具体配置步骤如下：

1. 使用RAM管理员登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 在左侧导航栏，选择**身份管理 > 用户**。
3. 在**用户**页面，单击目标RAM用户名称。
4. 在**认证管理**页签下的**AccessKey**区域，单击目标AccessKey操作列的**网络访问限制策略**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9076581571/p965753.png)
5. 在**AccessKey级网络访问限制策略**对话框，设置AccessKey级公网策略和专有网络策略。公网策略：需填入公网IP地址或IP地址段，支持IPv4和IPv6格式。不创建公网策略代表所有公网IP来源均可通过。因此，若要拒绝所有公网访问，需要填入非公网地址，例如：`127.0.0.1`。专有网络策略：需填入VPC ID和VPC内的IP地址或IP地址段，支持IPv4和IPv6格式。不创建专有网络策略代表所有来自专有网络的调用均可通过。创建专有网络策略，在IP列表中填入`0.0.0.0/0`或`::/0`，表示允许该VPC内的所有IP地址的访问。支持一条策略中输入多个IP地址或IP地址段，多个IP地址使用空格、半角逗号（,）或半角分号（;）分隔。

## 故障排除

### AccessKey专有网络限制策略不生效

如果配置了AccessKey专有网络限制策略，但发现策略未生效，可能的原因是访问阿里云服务时使用了公网Endpoint。使用公网Endpoint时，程序的请求会通过公网进行访问，而不是通过专有网络VPC的IP地址，这样就无法与配置的专有网络IP白名单匹配，导致访问限制策略未能正确应用。

### AccessKey账号级网络限制策略不生效

如果配置了AccessKey账号级网络限制策略，但发现策略未生效，请检查是否配置了AccessKey级网络访问限制策略，该策略的优先级更高，若来源IP不在AccessKey级网络访问限制白名单内，则会被拦截。您可以参考下方AccessKey网络访问限制策略判断规则来进行故障排除。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9076581571/p965752.png)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-267（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
