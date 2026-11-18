<!-- source: https://help.aliyun.com/zh/well-architected/solution-242 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929333 -->

# 通过FC函数角色实现临时凭证的获取和使用

本文介绍了一种部署在函数计算上的应用程序获取和使用临时凭证（STS Token）的方案。避免直接把AccessKey固化在程序中，引发泄露风险。

## 方案概述

![通过FC函数角色实现临时凭证的获取和使用V3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6507354571/p994643.png)

函数计算根据函数配置的角色，通过AssumeRole获取一个临时密钥（STS Token）。然后通过环境变量中的参数将临时密钥传递给您的函数。此临时密钥包含了您所配置的权限的所有资源，您可以在函数代码中使用其访问其他阿里云服务。

## 方案优势

该方案能够显著提升云上应用程序的安全性、灵活性和便捷性，同时降低维护成本和操作复杂性。

### 提高安全性

通过FC函数角色和RAM角色关联，使用STS Token访问云资源，避免了将访问密钥硬编码在代码中，从而消除AK泄露的风险。临时凭证（STS Token）的使用有效解决了永久凭证（AK/SK）可能带来的安全风险问题。

### 精细化管理权限

通过为不同FC函数赋予具有特定授权策略的RAM角色，确保函数仅能访问其所需的资源，实现权限最小化。

### 增强灵活性

部署在FC函数的程序可以通过阿里云官方SDK，设置函数角色认证方式，获取临时凭证STS Token。这种方式无需预先配置固定的访问凭证，可以根据需要动态获取和使用临时凭证。无需直接在FC函数上管理凭证，权限的调整仅需通过修改RAM角色的授权策略来实现，快捷地维护FC函数拥有的访问权限。

### 降低维护成本

使用临时凭证STS Token，无需频繁更新代码中的访问密钥，减少了维护成本和操作复杂性。 本方案提供Java/Python代码示例，客户能够快速完成应用改造，减少开发和部署的复杂度。

## 客户场景

### 部署在FC函数中的应用程序采用无AK架构

#### 场景描述

客户在FC函数上部署的应用程序需要访问其他云资源，传统的方式是客户将RAM用户的AK（Access Key）固化在函数中，如果将AK写在配置文件中，容易造成AK泄露，维护困难等问题。FC函数RAM角色通过将FC函数和RAM角色关联，使用STS Token（Security Token Service）访问云资源，解决永久凭证可能导致的安全风险问题。

#### 适用客户

- **需要高安全性**：客户需要确保AK不被暴露，以防止安全漏洞。
- **动态管理访问权限**：客户需要动态管理和临时授予实例访问其他资源的权限，避免长期凭证带来的风险。
- **简化运维管理**：客户希望简化运维过程中对凭证的管理，减少手动维护的复杂性。

## 方案架构

本方案通过FC函数角色实现临时凭证的获取和使用。该架构和流程通过动态管理和临时授予访问权限，避免了长期暴露AK的风险，提高了系统的安全性和灵活性。管理员仅需一次性配置角色和权限，后续函数在运行时即可动态获取和使用临时凭证，简化了运维管理工作。

管理员创建一个受信给函数计算的Role（角色），并对该角色授予相应的权限。角色权限包含访问需要的云资源的权限（图中1）。管理员将创建好的角色配置到对应的FC函数上，使函数与角色关联（图中2）。客户应用程序从函数环境变量中获取临时安全凭证（STS Token）（图中3），该过程中函数计算会使用云服务的身份调用AssumeRole接口，从RAM/STS服务获取STS Token（图中i）。 客户应用程序使用获取到的STS Token来调用目标云资源服务的API（图中4）。资源服务API处理请求并返回访问结果，客户端应用程序接收到返回的结果后完成相应的业务逻辑。 ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6507354571/p994651.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| RAM | [访问控制（RAM）](https://help.aliyun.com/product/28625.html)是阿里云提供的一项管理用户身份与资源访问权限的服务。使用RAM，您可以创建、管理RAM角色（例如员工、系统或应用程序），并可以控制这些RAM角色对资源的操作权限。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |
| 函数计算 | [函数计算（Function Compute）](https://www.alibabacloud.com/product/function-compute)函数计算是事件驱动的全托管计算服务。使用函数计算，您无需采购与管理服务器等基础设施，只需编写并上传代码。函数计算为您准备好计算资源，弹性地、可靠地运行任务，并提供日志查询、性能监控和报警等功能。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/functioncompute/product-overview/billing-overview)。 |
| 配置审计 | [配置审计（Cloud Config）](https://help.aliyun.com/zh/document_detail/127388.html)是一项资源审计服务，为您提供面向资源的配置历史追踪、配置合规审计等能力。面对大量资源，帮您轻松实现基础设施的自主监管，确保持续性合规。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/document_detail/133951.html)。 |
| 操作审计 | [操作审计（ActionTrail）](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)是阿里云提供的云账号资源操作记录的查询和投递服务，可用于安全分析、资源变更追踪以及合规性审计等场景。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/actiontrail/product-overview/billing-1)。 |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| RAM管理员 | RAM管理员具备账号下RAM资源的管理权限。RAM管理员可以是阿里云账号（主账号），也可以是主账号下拥有AliyunRAMFullAccess权限的RAM用户，强烈推荐您使用RAM用户充当RAM管理员。 |
| 访问密钥（AccessKey） | 访问密钥AccessKey（简称AK）是阿里云提供给用户的永久访问凭据，一组由AccessKey ID和AccessKey Secret组成的密钥对。发起的请求会携带AccessKey ID和AccessKey Secret加密请求内容生成的签名，进行身份验证及请求合法性校验。 |
| RAM角色（RAM role） | RAM角色是一种虚拟用户，可以被授予一组权限策略。与RAM用户不同，RAM角色没有永久身份凭证（登录密码或访问密钥），需要被一个可信实体扮演。扮演成功后，可信实体将获得RAM角色的临时身份凭证，即安全令牌（STS Token），使用该安全令牌就能以RAM角色身份访问被授权的资源。 |
| 函数RAM角色 | FC函数通过函数RAM角色获得该角色拥有的权限，可以基于临时安全令牌STS（Security Token Service）访问指定云服务的API和操作指定的云资源，安全性更高。 |

## 安全性

### 函数计算服务关联角色

在某些场景下，函数计算为了完成自身的某个功能，需要获取其他云服务的访问权限，因此，函数计算创建了与云服务关联的角色，即服务关联角色（AliyunServiceRoleForFC）。函数计算3.0支持AliyunServiceRoleForFC和FaaS函数的绑定，实现最小授权范围内授予函数访问其他云服务的权限。

关于服务关联角色的更多信息，请参见[服务关联角色](https://help.aliyun.com/zh/ram/user-guide/service-linked-roles)。

### 函数计算安全性

阿里云函数计算是事件驱动的全托管计算服务。通过函数计算，用户无需管理服务器等基础设施，只需编写代码并上传。函数计算会为用户准备好计算资源，以弹性、可靠的方式运行用户的代码，并提供日志查询、性能监控和报警等功能。对于数据层面，在与用户通信时，函数计算使用TLS 1.2及以上协议加密传输调用请求及回包，内部通信使用私有协议防止信息泄露及篡改。对于管控层面，您可以通过阿里云访问控制（RAM）进行权限控制等等。关于函数计算安全性的详细信息，请参见[安全合规](https://help.aliyun.com/zh/functioncompute/security-and-compliance)。

## 注意事项

### 临时密钥有效期

函数计算根据函数配置的角色，通过AssumeRole获取一个临时密钥（STS Token）。该临时密钥的有效期为36小时，且不支持修改。函数的最大执行时间为24小时，因此，执行函数过程中，临时密钥不会过期。

### 持续合规审计函数计算版本限制

配置审计规则 ：**函数计算服务配置了服务角色**只支持审计函数计算2.0的函数计算服务实例。

### 支持STS的云服务

支持临时安全令牌（STS）的阿里云服务查询，请参见[支持STS的云服务](https://help.aliyun.com/zh/ram/services-that-work-with-sts)。

## 实施步骤

### 实施准备

如您需要审计函数是否绑定了函数角色，请确保已经开通了配置审计。具体操作，请参考[开通配置审计服务](https://help.aliyun.com/zh/document_detail/2399579.html)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：30分钟。

### 操作步骤

#### 持续合规审计（可选）

您可以通过配置审计，持续审计函数计算服务的服务角色配置情况，及时发现未配置服务角色的函数计算服务。

注意：【配置审计规则 - 函数计算服务配置了服务角色】只支持审计函数计算2.0的函数计算服务实例。

##### 创建账号组（可选）

如果您当前为多账号环境，希望对多个成员账号进行集中的合规管理，可以使用企业管理账号将资源目录中的所有或部分成员账号加入到同一个账号组中，账号组将作为一个跨账号合规管理的管理单元。如果您是单账号环境，可跳过本步骤。

1. 登入企业管理主账号，进入[资源管理控制台](https://resourcemanager.console.aliyun.com/)，在左侧导航栏选择 **资源目录**> **可信服务**。选择配置审计，单击**管理**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970753.png)
2. 在**委派管理员账号**中，单击**添加**，将日志账号委派为配置审计服务的管理员。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970763.png)
3. 登入日志账号，进入[配置审计控制台](https://config.console.aliyun.com/)，在左侧导航栏选择**账号组**。单击**创建账号组**，通过账号组，对资源目录中的成员账号进行集中合规管理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970754.png)
4. 创建账号组时，账号组类型，可以选择**全局**。全局账号组包含的成员将自动与资源目录保持一致。全局账号组会自动感知资源目录中成员的新增，并自动同步加入到该全局账号组中，确保合规管理的账号范围始终与资源目录保持一致。需要注意的是，您只能新建一个全局账号组。这里我们创建一个名为 ResourceDirectory 的全局账号组，以此为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970756.png)

##### 创建规则

1. 进入[配置审计控制台](https://config.console.aliyun.com/)。若您使用上述步骤中的账号组进行多账号合规管控，需要在左侧导航栏中切换到需要合规管控的账号组中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970757.png)
2. 在左侧导航栏选择**合规审计** > **规则**，单击**新建规则**。选择名为**函数计算服务配置了服务角色**的规则。单击**下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970764.png)
3. 在**设置基本属性**中，可以对规则的风险等级、触发机制和触发频率进行设置。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970761.png)
4. 单击**下一步**，您可以进一步设置规则生效的范围，比如，配置该规则只对某些资源组内的资源或者具有某些标签的资源生效。以此来对合规管控的资源范围进行更加精细化的管理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970759.png)
5. 创建完成后，在规则详情页，您可以看到当前账号组下，所有不合规的资源，即未配置服务角色的函数计算服务列表。该规则，默认会每 24 个小时执行一次检测，您可以在创建规则或者修改规则时，配置该规则的触发频率。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970765.png)
6. 最后，您还可以将不合规资源数据投递到其他云产品中，比如日志服务、对象存储等。方便您进一步对数据进行归档、处理、审计等操作。更多投递相关的信息，请参考[配置审计投递](https://help.aliyun.com/zh/document_detail/310163.html)。

#### 创建并绑定函数角色

##### 函数计算 3.0 版本

1. 登录[函数计算控制台](https://fcnext.console.aliyun.com/)，在左侧导航栏，单击**函数**。
2. 在顶部菜单栏，选择地域，然后在**函数**页面，单击目标函数操作列的**配置**。
3. 在函数详情页面，选择**配置**页签，然后在左侧导航栏选择**权限**，单击**编辑**，在编辑权限面板，单击**创建角色**跳转至RAM控制台，根据界面提示创建角色并为角色授予所需权限。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970766.png)

您也可以使用已有的角色，如果权限不足，单击**编辑策略**根据需要添加权限策略。具体操作，请参见[为RAM角色授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-a-ram-role)。

1. 在[RAM控制台](https://ram.console.aliyun.com/)的**角色**页面，单击**创建角色**。
2. 在**选择类型**页签，选择可信实体类型为**阿里云服务**，然后单击**下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970768.png)
3. 在**配置角色**页签，选择**普通服务角色**，设置角色名称（本文示例为fc-test-role），**选择受信服务**为**函数计算**，然后单击**完成**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970769.png)
4. 在**创建完成**页签，单击**为角色授权**，然后单击目标角色右侧操作列的**新增授权**。
5. 在授权页面，选择**授权范围**，**授权主体**默认为选择的目标角色，选择所需系统策略或自定义策略，单击添加到右侧已选择列表，然后单击**确定**。更多信息，请参见[权限策略及示例](https://help.aliyun.com/zh/fc/policies)。**整个云账号**：权限在当前阿里云账号内生效。**指定资源组**：权限在指定的资源组内生效。指定资源组授权生效的前提是该云服务已支持资源组。更多信息，请参见[支持资源组的云服务](https://help.aliyun.com/zh/resource-management/product-overview/services-that-work-with-resource-group#concept-flc-p3m-4fb)。
6. 为目标函数绑定上一步创建的新角色fc-test-role，并单击底部部署按钮。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970762.png)

##### 函数计算 2.0 版本

1. 登录[函数计算控制台](https://fcnext.console.aliyun.com/)，在左侧导航栏，单击**服务及函数**。
2. 在顶部菜单栏，选择地域，然后在**服务及函数**页面，单击目标服务操作列的**配置**。
3. 在**编辑服务**页面，在**角色配置**面板，单击**创建角色**跳转至RAM控制台，根据界面提示创建角色并为角色授予所需权限。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970771.png)

您也可以使用已有的角色，如果权限不足，单击**编辑策略**根据需要添加权限策略。具体操作，请参见[为RAM角色授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-a-ram-role)。

1. 在[RAM控制台](https://ram.console.aliyun.com/)的**角色**页面，单击**创建角色**。
2. 在**选择类型**页签，选择可信实体类型为**阿里云服务**，然后单击**下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970770.png)
3. 在**配置角色**页签，选择**普通服务角色**，设置角色名称（本文示例为fc-test-role），**选择受信服务**为**函数计算**，然后单击**完成**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970773.png)
4. 在**创建完成**页签，单击**为角色授权**，然后单击目标角色右侧操作列的**新增授权**。
5. 在授权页面，选择**授权范围**，**授权主体**默认为选择的目标角色，选择所需系统策略或自定义策略，单击添加到右侧已选择列表，然后单击**确定**。更多信息，请参见[权限策略及示例](https://help.aliyun.com/zh/fc/policies)。**整个云账号**：权限在当前阿里云账号内生效。**指定资源组**：权限在指定的资源组内生效。指定资源组授权生效的前提是该云服务已支持资源组。更多信息，请参见[支持资源组的云服务](https://help.aliyun.com/zh/resource-management/product-overview/services-that-work-with-resource-group#concept-flc-p3m-4fb)。
6. 为目标函数绑定上一步创建的新角色fc-test-role，并单击底部保存按钮。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970767.png)

#### 基于函数角色获取并使用临时凭证

您可以利用临时凭证执行已授权给函数角色fc-test-role的操作。在以下步骤中，您可以调用GetCallerIdentity来查看当前调用者的身份信息。

##### 编写并部署代码

在函数列表，单击目标函数，然后选择**代码**页签，在**代码**页签的代码编辑器中，编写代码或上传代码，然后单击**部署代码**。

您可以使用阿里云SDK，基于函数角色从环境变量中获取临时凭证，并使用该临时凭证调用阿里云OpenAPI。

###### Node.js

以下是Node.js标准运行时代码：

```
'use strict';

const RPCClient = require('@alicloud/pop-core').RPCClient;
const httpModule = require('https');

const keepAliveAgent = new httpModule.Agent({
    keepAlive: false,
});
const requestOption = {
    method: 'POST',
    formatParams: false,
    timeout: 10000,
    agent: keepAliveAgent,
};

exports.handler = (event, context, callback) => {
    main(context)
        .then((res) => {
            callback(null, JSON.stringify(res));
        })
        .catch((err) => callback(err));
};

async function main(context) {

    // 从系统预留环境变量中获取 AK/SK/Security Token，初始化请求 OpenAPI 的 Client
    const client = new RPCClient({
        accessKeyId: process.env.ALIBABA_CLOUD_ACCESS_KEY_ID,
        accessKeySecret: process.env.ALIBABA_CLOUD_ACCESS_KEY_SECRET,
        securityToken: process.env.ALIBABA_CLOUD_SECURITY_TOKEN,
        endpoint: 'https://sts.cn-hangzhou.aliyuncs.com',
        apiVersion: '2015-04-01'
    });

    const result = await client.request('GetCallerIdentity', {
        pageSize: 1
    }, requestOption);
    return result;
}
```

###### Python

以下是Python标准运行时代码：

```
import os
from aliyunsdksts.request.v20150401.GetCallerIdentityRequest import GetCallerIdentityRequest
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import StsTokenCredential

def handler(event, context):
    
    # 从系统预留环境变量获取凭证信息，创建凭证对象
    credentials = StsTokenCredential(
        os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID'),
        os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
        os.environ.get('ALIBABA_CLOUD_SECURITY_TOKEN')
    )

    # 初始化客户端，设置地区等信息
    client = AcsClient(region_id='cn-hangzhou', credential=credentials)

    # 创建请求对象
    request = GetCallerIdentityRequest()

    # 设置参数，例如可以设置过滤条件等，这里只展示最基本的调用
    request.set_accept_format('json')

    # 发起请求并获取响应
    response = client.do_action_with_exception(request)

    # 打印响应结果
    return(str(response, encoding='utf-8'))
```

###### Java

以下是Java代码及其Maven依赖：

```
<dependency>
  <groupId>com.aliyun.fc.runtime</groupId>
  <artifactId>fc-java-core</artifactId>
  <version>1.4.1</version>
</dependency>

<dependency>
  <groupId>com.aliyun.fc.runtime</groupId>
  <artifactId>fc-java-event</artifactId>
  <version>1.2.0</version>
</dependency>

<!--建议使用最新发布的Credentials版本。-->
<!--获取所有已发布的版本列表，请参见https://github.com/aliyun/credentials-java/blob/master/ChangeLog.txt-->
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>credentials-java</artifactId>
  <version>LATEST</version>
</dependency>

<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>sts20150401</artifactId>
  <version>1.1.4</version>
</dependency>

<dependency>
  <groupId>com.alibaba.fastjson2</groupId>
  <artifactId>fastjson2</artifactId>
  <version>2.0.51</version>
</dependency>
```

```
import java.io.InputStream;
import java.io.OutputStream;

import com.alibaba.fastjson2.JSON;
import com.aliyun.credentials.utils.AuthConstant;
import com.aliyun.fc.runtime.Context;
import com.aliyun.fc.runtime.StreamRequestHandler;
import com.aliyun.sts20150401.Client;
import com.aliyun.sts20150401.models.GetCallerIdentityResponse;
import com.aliyun.teaopenapi.models.Config;

public class App implements StreamRequestHandler {

    @Override
    public void handleRequest(InputStream inputStream, OutputStream outputStream, Context context) {
        try {
            com.aliyun.credentials.Client credentialClient = createCredential();
            Config config = new Config().setRegionId("cn-hangzhou").setCredential(credentialClient);

            // 查看当前调用者身份
            Client stsClient = new Client(config);
            GetCallerIdentityResponse getCallerIdentityResponse = stsClient.getCallerIdentity();
            outputStream.write(JSON.toJSONString(getCallerIdentityResponse).getBytes());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static com.aliyun.credentials.Client createCredential() {
        com.aliyun.credentials.models.Config config = new com.aliyun.credentials.models.Config();

        config.type = AuthConstant.STS;
        // 从系统预留环境变量中获取凭证信息
        config.accessKeyId = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID");
        config.accessKeySecret = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET");
        config.securityToken = System.getenv("ALIBABA_CLOUD_SECURITY_TOKEN");

        return new com.aliyun.credentials.Client(config);
    }
}
```

- 临时密钥是从环境变量中获取的，为避免混淆，设置环境变量时，请不要使用同名的系统预留环境变量。
- 临时密钥的有效期为36小时，且不支持修改。函数的最大执行时间为24小时，因此，执行函数过程中，临时密钥不会过期。

除了以上给出的三种语言示例之外，更多语言运行时示例详见[代码开发概述](https://help.aliyun.com/zh/functioncompute/code-development-overview#section-crb-wcw-8j4)。

##### 查看结果

单击**测试函数**，点击详细信息查看结果。

##### OSS SDK

您也可以使用OSS SDK，来获取和管理访问凭证，并完成API调用。

注意：您需要为该函数配置的函数角色授予**AliyunOSSFullAccess**权限。

###### Python

以下是Python标准运行时代码：

```
import json
import oss2
import os

def handler(event, context):
    endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'
    bucket = 'web****'
    object = 'myObj'
    message = 'test-message'
    
    # 从系统预留环境变量获取凭证信息，构造OSS SDK的凭证
    auth = oss2.StsAuth(
        os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID'),
        os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
        os.environ.get('ALIBABA_CLOUD_SECURITY_TOKEN')
    )

    # 调用OpenAPI
    bucket = oss2.Bucket(auth, endpoint, bucket)
    bucket.put_object(object, message)

    return 'success'
```

上述示例中，bucket需替换为与函数相同的地域下您已创建的bucket名称。

###### Java

阿里云OSS的SDK及FC相关依赖如下：

```
<dependencies>
  <dependency>
    <groupId>com.aliyun.oss</groupId>
    <artifactId>aliyun-sdk-oss</artifactId>
    <version>3.17.4</version>
  </dependency>
  
  <dependency>
    <groupId>com.aliyun.fc.runtime</groupId>
    <artifactId>fc-java-core</artifactId>
    <version>1.4.1</version>
  </dependency>
  
  <dependency>
    <groupId>com.aliyun.fc.runtime</groupId>
    <artifactId>fc-java-event</artifactId>
    <version>1.2.0</version>
  </dependency>

  <dependency>
  <groupId>com.alibaba.fastjson2</groupId>
  <artifactId>fastjson2</artifactId>
  <version>2.0.51</version>
  </dependency>
</dependencies>
```

Java代码如下：

```
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.List;

import com.alibaba.fastjson2.JSON;
import com.aliyun.fc.runtime.Context;
import com.aliyun.fc.runtime.StreamRequestHandler;
import com.aliyun.oss.ClientBuilderConfiguration;
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.common.auth.CredentialsProvider;
import com.aliyun.oss.common.auth.DefaultCredentialProvider;
import com.aliyun.oss.common.auth.Credentials;
import com.aliyun.oss.common.auth.DefaultCredentials;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.Bucket;

public class App implements StreamRequestHandler {

    @Override
    public void handleRequest(InputStream inputStream, OutputStream outputStream, Context context) throws IOException {

        // 从系统预留环境变量获取凭证信息，构造OSS的Credentials
        Credentials ossCreds = new DefaultCredentials(
            System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
            System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
            System.getenv("ALIBABA_CLOUD_SECURITY_TOKEN")
        );

        CredentialsProvider credentialsProvider = new DefaultCredentialProvider(ossCreds);

        // Bucket所在地域对应的Endpoint。以华东1（杭州）为例。
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Endpoint对应的Region信息，例如cn-hangzhou。
        String region = "cn-hangzhou";
        // 建议使用更安全的V4签名算法，则初始化时需要加入endpoint对应的region信息，同时声明SignVersion.V4
        // OSS Java SDK 3.17.4及以上版本支持V4签名。
        ClientBuilderConfiguration configuration = new ClientBuilderConfiguration();
        configuration.setSignatureVersion(SignVersion.V4);

        OSS ossClient = OSSClientBuilder.create()
            .endpoint(endpoint)
            .credentialsProvider(credentialsProvider)
            .clientConfiguration(configuration)
            .region(region)
            .build();

        // 调用OpenAPI
        List<Bucket> buckets = ossClient.listBuckets();
        outputStream.write(JSON.toJSONString(buckets).getBytes());
    }
}
```

##### SLS SDK

您也可以使用SLS SDK，来获取和管理访问凭证，并完成API调用。

注意：您需要为该函数配置的函数角色授予**AliyunLogReadOnlyAccess**权限。

###### Python

以下是Python标准运行时代码：

```
import os
from aliyun.log import LogClient

def handler(event, context):
    endpoint = 'cn-hangzhou.log.aliyuncs.com'

    # 从系统预留环境变量获取凭证信息，初始化 LogClient
    client = LogClient(
        endpoint,
        os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID'),
        os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
        os.environ.get('ALIBABA_CLOUD_SECURITY_TOKEN')
    )

    # 调用ListProject接口
    response = client.list_project()

    return response.get_projects()
```

###### Java

阿里云SLS的SDK及FC相关依赖如下：

```
<dependencies>
  <dependency>
    <groupId>com.aliyun.fc.runtime</groupId>
    <artifactId>fc-java-core</artifactId>
    <version>1.4.1</version>
  </dependency>

  <dependency>
    <groupId>com.aliyun.fc.runtime</groupId>
    <artifactId>fc-java-event</artifactId>
    <version>1.2.0</version>
  </dependency>

  <dependency>
    <groupId>com.aliyun.openservices</groupId>
    <artifactId>aliyun-log</artifactId>
    <version>0.6.107</version>
  </dependency>

  <dependency>
    <groupId>com.alibaba.fastjson2</groupId>
    <artifactId>fastjson2</artifactId>
    <version>2.0.51</version>
  </dependency>
</dependencies>
```

Java代码如下：

```
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.List;

import com.alibaba.fastjson2.JSON;
import com.aliyun.fc.runtime.Context;
import com.aliyun.fc.runtime.StreamRequestHandler;
import com.aliyun.openservices.log.Client;
import com.aliyun.openservices.log.common.Project;
import com.aliyun.openservices.log.common.auth.Credentials;
import com.aliyun.openservices.log.common.auth.CredentialsProvider;
import com.aliyun.openservices.log.common.auth.DefaultCredentials;
import com.aliyun.openservices.log.common.auth.StaticCredentialsProvider;
import com.aliyun.openservices.log.exception.LogException;

public class App implements StreamRequestHandler {

    @Override
    public void handleRequest(InputStream inputStream, OutputStream outputStream, Context context) throws IOException {

        // 从系统预留环境变量获取凭证信息，构造SLS的Credentials
        Credentials slsCreds = new DefaultCredentials(
            System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
            System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
            System.getenv("ALIBABA_CLOUD_SECURITY_TOKEN")
        );

        CredentialsProvider credentialsProvider = new StaticCredentialsProvider(slsCreds);

        // SLS endpoint，以杭州为例
        String endpoint = "https://cn-hangzhou.log.aliyuncs.com";

        Client slsClient = new Client(endpoint, credentialsProvider);

        // 调用OpenAPI
        try {
            List<Project> projects = slsClient.ListProject().getProjects();
            outputStream.write(JSON.toJSONString(projects).getBytes());
        } catch (LogException e) {
            throw new RuntimeException(e);
        }
    }
}
```

##### 代码示例

###### 代码介绍

本方案提供使用阿里云SDK、OSS SDK及SLS SDK从环境变量中获取临时凭证的FC代码示例，包括Java和Python语言，方便客户能够快速完成应用改造。

###### 代码地址

代码详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-fc-sts-token)。

#### 函数角色操作审计（可选）

若您需要对FC函数角色进行操作审计，例如使用该FC函数角色的身份做了什么操作，您可以使用您的日志审计账号进入[操作审计控制台](https://actiontrail.console.aliyun.com/)，在 **事件 > 事件查询**中找到该实例角色的操作事件，点击查看事件详情。

审计的事件中，`stsTokenPrincipalName`为一个固定的格式：`${函数角色名称}/FunctionCompute`。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970774.png)

若您的账号开启了审计日志投递，可以在 **事件 > 高级查询**中运行下方所示的查询SQL语句快速查找出实例使用实例角色身份的进行的所有操作：

```
requestParameters.stsTokenPrincipalName:${函数角色名称}/FunctionCompute
```

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1076581571/p970772.png)

## 故障排除

### 为什么执行函数失败？

在“运行环境”为 Java 时，出现`Cannot find the class example.App in your zip file and please make sure it is in the right path 'example/App'`错误，请确认**配置>运行时>请求处理程序**的格式为 [package].[class]::[method]。例如，当前值为 example.HelloFC::handleRequest，那么在函数被触发时，将执行 example 包中 HelloFC 类中的 handleRequest 函数。

更多使用 FC 的常见问题，请参见 [FC 服务支持](https://help.aliyun.com/zh/functioncompute/support/faq/)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-242（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
