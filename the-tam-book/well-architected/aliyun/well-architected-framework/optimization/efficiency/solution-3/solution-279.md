<!-- source: https://help.aliyun.com/zh/well-architected/solution-279 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929475 -->

# 通过EventBridge和账号工厂实现账号基线配置自动化

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973053.png)

在云治理中心中，企业通过账号工厂创建新账号时，虽然系统已支持多项默认基线项（如结算关系和防护规则），但这些基线项往往无法完全符合客户的个性化需求，例如默认 RAM 用户的配置和云防火墙多账号统一管理的设置。这种局限性可能会影响企业在账号创建过程中的灵活性和效率。为了解决这一问题，本方案通过将事件总线（EventBridge）与账号工厂相结合，扩展基线配置能力，以实现对新建账号的自动化配置。通过该方案，企业能够实时监听新账号创建事件，并自动应用预定的配置，从而满足个性化需求，提升账号管理的自动化程度与一致性。

本文档介绍了一种通过事件总线和函数计算实现自动化为在云治理中心新建的账号添加统一配置的方法，旨在帮助企业有效应对个性化需求，优化账号管理流程。

## 方案优势

### 增强基线配置的灵活性

通过将事件总线（EventBridge）与账号工厂相结合，企业可以在创建新账号时，实时监听新账号创建事件，并自动应用预定的配置。这使得企业能够根据自身的个性化需求，灵活地调整和扩展基线配置，而不仅仅是依赖于默认的基线项。

### 支持复杂依赖关系的配置

某些资源配置可能存在依赖关系（如安全组依赖VPC）。通过脚本或模板（如Terraform、ROS模板）可以按照正确的顺序完成配置，确保资源间的依赖关系得到妥善处理。

### 实时监听与自动化执行

事件总线能够实时捕获新账号创建事件，并自动触发目标服务（如函数计算或OOS）执行预定义的配置任务。这种自动化流程大幅减少了手动操作的时间和人力成本，提升了账号创建的整体效率

## 客户场景

### 对新建账号做统一自动化处理

#### 场景描述

企业需要频繁创建新账号以支持业务发展，同时希望在账号创建时自动完成安全配置和个性化设置。通过结合阿里云的多账号管理工具（如资源目录、云安全中心、云防火墙等）以及事件总线EventBridge，可以实现新建账号的统一自动化处理。

#### 适用客户

- 拥有多个业务单元，需要对不同的新建账号进行统一管理和个性化配置。
- 云上资源的安全性有严格要求，需要在账号创建时即应用特定的安全配置。
- 业务发展迅速，需要频繁创建新账号以支持新业务上线。

## 方案架构

本方案通过事件总线（EventBridge）监听账号工厂的新账号创建事件，触发函数计算调用阿里云OpenAPI，完成对新建账号的自动化配置。事件总线捕获“账号创建完成”事件后，将事件路由至函数计算服务，函数计算根据预定义逻辑执行个性化配置任务，例如RAM用户创建、云防火墙启用、安全组规则配置等。方案中使用阿里云SDK实现API调用，确保配置的一致性和安全性。同时，通过云治理中心的账号基线功能，预先定义默认基线项，并结合自定义基线扩展能力，满足企业个性化需求。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973052.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 事件总线 | [事件总线（EventBridge）](https://help.aliyun.com/zh/eventbridge/product-overview/what-is-eventbridge)是阿里云提供的一款无服务器事件总线服务，支持阿里云服务、自定义应用、SaaS应用以标准化、中心化的方式接入，并能够以标准化的CloudEvents 1.0协议在这些应用之间路由事件，帮助您轻松构建松耦合、分布式的事件驱动架构。 | 公测期间免费，详情参见[产品计费](https://help.aliyun.com/zh/eventbridge/product-overview/eventbridge-billing/)。 |
| 函数计算 | [函数计算（Function Compute）](https://www.alibabacloud.com/product/function-compute)函数计算是事件驱动的全托管计算服务。使用函数计算，您无需采购与管理服务器等基础设施，只需编写并上传代码。函数计算为您准备好计算资源，弹性地、可靠地运行任务，并提供日志查询、性能监控和报警等功能。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/functioncompute/product-overview/billing-overview)。 |
| 云防火墙 | [阿里云云防火墙](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/product-overview/what-is-cloud-firewall)是一款云平台SaaS（Software as a Service）化的防火墙，可针对您云上网络资产的互联网边界、VPC边界及主机边界实现三位一体的统一安全隔离管控，是您业务上云的第一道网络防线。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/billing) |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 事件总线 | 负责接收来自事件源的事件，包括以下类型：云服务专用总线：一个无需创建且不可修改的内置事件总线，用于接收您的阿里云官方事件源的事件。阿里云官方事件源的事件只能发布到云服务专用总线。自定义总线：需要您自行创建并管理的事件总线，用于接收自定义应用或存量消息数据的事件。自定义应用或存量消息数据的事件只能发布到自定义总线。 |
| 事件规则 | 事件规则用于过滤和转换接收到的事件，能将CloudEvents转换为事件目标可以接收的格式。当发生匹配事件时，事件会被路由到与事件规则关联的事件目标。规则可以与一个或多个事件目标关联。 |
| 事件源 | 事件源是事件的来源，负责将生产的事件发布到事件总线EventBridge。事件总线EventBridge支持阿里云官方事件源和自定义事件源。 |
| 事件追踪 | 您可以通过事件追踪功能查看发布到事件总线EventBridge的事件内容，即事件详情，也可以查看事件在事件总线EventBridge中的处理轨迹，即事件轨迹。 |
| 函数RAM角色 | FC函数通过函数RAM角色获得该角色拥有的权限，可以基于临时安全令牌STS（Security Token Service）访问指定云服务的API和操作指定的云资源，安全性更高。 |

## 安全性

### 使用RAM进行访问控制

RAM用户需要由阿里云账号（即主账号）或拥有管理员权限的RAM用户、RAM角色来创建，且必须在获得授权后才能登录控制台或使用API访问阿里云账号下的资源。关于使用RAM的更多信息，请参见[使用RAM进行访问控制](https://help.aliyun.com/zh/eventbridge/use-ram-for-access-control/)。

### 数据保护与数据安全

事件总线EventBridge具有丰富的安全防护能力，通过多项合规认证，支持服务器端加密、客户端加密、细粒度权限管控等特性，为您的云端数据安全进行全方位的保驾护航，满足您企业数据的安全与合规要求。更多信息请参见[事件总线数据安全和保护](https://help.aliyun.com/zh/eventbridge/data-protection-and-security)

## 注意事项

### 函数计算使用限制

函数计算在服务资源、函数运行资源、触发器、层、地域、镜像大小及GPU卡数等相关资源的使用上存在限制。详细信息，请参见[使用限制](https://help.aliyun.com/zh/functioncompute/limits-of-usage)。

### 事件总线使用限制

事件总线EventBridge对某些具体指标进行了约束和规范，您在使用事件总线EventBridge时请不要超过相应的限制，以免程序出现异常，具体详见[使用限制](https://help.aliyun.com/zh/eventbridge/product-overview/limits)。

## 实施步骤

### 实施准备

- 确保已在「企业管理账号」下开通云治理中心，并在账号工厂中配置统一的账号基线。具体详见[开通云治理中心](https://help.aliyun.com/zh/cgc/getting-started/activate-cloud-governance-center)和[配置账号基线](https://help.aliyun.com/zh/cgc/user-guide/configure-the-account-baseline)。

### 实施规划

本方案以云防火墙的多账号统一管理为例，针对当前云防火墙无法自动识别新建成员账号的问题，利用事件总线，实时监测来自云治理中心账号工厂的新成员账号创建事件。一旦检测到相关事件，系统将通过函数计算自动调用云防火墙的 OpenAPI，从而实现成员账号的自动添加。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：30分钟。

### 操作步骤

#### 配置函数计算

本方案通过函数计算，使用无AK的方式调用云产品OpenAPI以实现对新账号更多的自定义操作。详情参考[通过FC函数角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-242)。

若您需要触发其余自定义操作，如发送邮件、短信等，可跳过本步骤。

##### 创建函数计算服务角色

**步骤 1** 首先需要先在企业管理主账号（以下简称MA账号）中创建一个受信实体为函数计算的服务角色，函数计算将通过该服务角色的身份使用无AK的方式运行您自定义的函数逻辑。

1. 登入MA账号，进入 [RAM 控制台](https://ram.console.aliyun.com/)。在左侧导航栏，选择**身份管理 > 角色**。
2. 在**角色**页面，单击**创建角色**。
3. 在**创建角色**页面，选择信任主体类型为**阿里云服务**，信任主体名称为**函数计算**，然后单击**下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973054.png)
4. 输入角色名称，以 **fc-role**为例，点击**完成。**

**步骤 2** 创建自定义权限策略

1. 登入MA账号，进入 [RAM 控制台](https://ram.console.aliyun.com/)。
2. 选择 **权限管理 > 权限策略**，点击**创建权限策略**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973055.png)
3. 按照实际业务需要分配权限，本示例通过**脚本编辑**模式，将配置框中的原有脚本替换为如下内容，点击 **确定** 创建自定义权限策略 **AddInstanceMemberAccess**。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "yundun-cloudfirewall:AddInstanceMembers",
 "Resource": "*"
 }
 ]
}`

**步骤 3** 接下来，需要为该角色分配权限。

1. 登入MA账号，进入 [RAM 控制台](https://ram.console.aliyun.com/)。在左侧导航栏，选择**身份管理 > 角色**，点击上一步创建的角色 **fc-role**。
2. 在**角色**页面，点击**新增授权。**
3. 在**新增授权**侧边栏中，为角色分配自定义权限策略 **AddInstanceMemberAccess**。您也可以根据自己对应的需求场景来进行精细化授权。
4. 点击 **确认新增授权** 为角色完成权限分配。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973056.png)

##### 创建函数

**步骤 4** 根据需要，配置自定义的函数内容。本方案以将指定定账号加入到云防火墙多账号管理中为例，在开始本步骤之前，请先完成步骤 [配置云防火墙多账号统一管理](#i67Zo)。

1. 登入MA账号，进入[函数计算控制台](https://fcnext.console.aliyun.com/overview)，第一次使用系统会提示您授权对应的函数计算服务关联角色，点进**确定**后进入。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973060.png)
2. 在左侧导航栏，选择 **函数** **>** **创建函数**。
3. 在**创建函数**页面，选择**任务函数**，依次填写函数名称，函数运行环境（本方案使用 python 3.10），上传代码`function_compute_python`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973057.png)
4. 下滑进入**高级配置**，在 **请求处理程序** 处填写 `[代码所在文件名称].[入口函数名称]`（若使用示例代码需填写`add_instance_member_by_sts.handler`），选择 **步骤1** 创建的**函数角色**，点击 **创建**。
5. 创建完成后，可在左侧导航栏，点击 **函数** 进行查看。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973062.png)

###### 示例代码

本代码基于Python3.10，提供使用阿里云SDK，从上下文中获取临时凭证并调用云防火墙OpenAPI的FC代码示例，方便客户能够快速完成应用改造。

```
import json

from alibabacloud_cloudfw20171207.client import Client as Cloudfw20171207Client
from alibabacloud_cloudfw20171207 import models as cloudfw_20171207_models
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import StsTokenCredential
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_openapi import models as open_api_models 

# 函数计算入口
def handler(event, context):
    # 从上下文获取凭证信息
    creds = context.credentials

    config = open_api_models.Config(
        access_key_id=creds.access_key_id,
        access_key_secret=creds.access_key_secret,
        security_token=creds.security_token
    )
    # Endpoint 请参考 https://api.aliyun.com/product/Cloudfw
    config.endpoint = f'cloudfw.aliyuncs.com'

    # 初始化客户端，设置地区等信息
    client = Cloudfw20171207Client(config)

    evt = json.loads(event)
    members_0 = cloudfw_20171207_models.AddInstanceMembersRequestMembers(
        member_uid=evt['accountId']
    )
    add_instance_members_request = cloudfw_20171207_models.AddInstanceMembersRequest(
        members=[
            members_0
        ] 
    )
    runtime = util_models.RuntimeOptions()
    try:
        client.add_instance_members_with_options(add_instance_members_request, runtime)
        return "success"
    
    except Exception as error:
        # 错误 message
        print(error.message)
        print(error.data.get("Recommend"))
        return "failed"
```

##### 部署函数环境

**步骤 4** 接下来需要为函数配置相应的依赖，并将代码部署到函数计算中。

1. 在左侧导航栏，点击 **函数**，选择 **步骤3** 中创建好的函数，点击进入函数详情页面。
2. 在**函数详情页**中，点击 **代码 > Ternimal > New Terminal**
3. 在新建的 Terminal 中运行以下两条指令，为代码添加相应的依赖（您可根据需要自行在在线编辑器中）`pip install alibabacloud_cloudfw20171207 -t .
pip install --upgrade pyOpenSSL cryptography -t .`
4. 添加完依赖后，需要点击**部署代码**才能在函数计算中生效。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973064.png)
5. 配置测试参数，点击 **测试函数**右侧的下拉箭头，选择 **配置测试参数**。
6. 在配置测试参数页面，填入如下参数，注意，此处 `accountId` 需要填MA账号下的一个成员账号，点击 **确定**完成配置。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973066.png)
7. 最后在页面上点击 **测试函数**，将会使用配置好的测试参数进行测试
8. **返回结果**处显示 success 即配置成功。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973058.png)

#### 配置事件总线

##### 开通事件总线

1. 登入MA账号，进入[事件总线控制台](https://eventbridge.console.aliyun.com/overview)，点击 **免费开通**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973068.png)
2. 根据需要，勾选对应的服务关联角色，本方案使用到 **AliyunServiceRoleForEventBridgeSendToFC** 和 **AliyunServiceRoleForEventBridgeSourceActionTrail**。(其余服务关联角色，可在[RAM控制台](https://ram.console.aliyun.com/overview?activeTab=overview)自行添加)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973067.png)
3. 下滑到页面底部，点击 **一键授权** 进行授权。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973059.png)

##### 创建事件规则

1. 点击 **事件总线**，在顶部菜单栏，选择地域（与云治理中心开通地域一致），点击云服务专用事件总线**default**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973070.png)
2. 进入到事件总线 **default** 页面，在左侧导航栏，点击 **事件规则** > **创建规则**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973061.png)
3. 在创建规则页面，完成以下操作。在 **配置基本信息** 配置向导，在名称文本框输入**规则名称**，在描述文本框输入**规则描述**，然后点击 **下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973069.png)在 **配置事件模式**配置向导，**事件源类型**选择阿里云官方事件源，**事件源**选择 `acs.governance` 云治理中心，事件类型选择 `governance:AccountFactory:CreateAccount`创建账号完成，使用默认**事件模式**，点击 **下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973071.png)在 **配置事件目标** 配置向导，**服务类型**选择函数计算，**函数**选择之前创建好的函数，**事件**选择部分事件，**版本**选择指定版本 > LATEST，然后点击 **创建**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973063.png)
4. 该事件规则将会监听**事件源**，即云治理中心账号工厂的创建账号事件，当账号工厂成功创建新账号后，事件规则自动触发用户配置的**事件目标**，即运行函数计算，将该账号添加至云防火墙多账号统一管理中。具体详见[事件源](https://help.aliyun.com/zh/eventbridge/user-guide/event-source/)和[事件目标](https://help.aliyun.com/zh/eventbridge/user-guide/event-target-overview)。

#### 配置云防火墙多账号统一管理

如已经配置过本步骤，可跳过，直接进行结果验证。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973072.png)

1. 登入MA账号，进入[云防火墙控制台](https://yundun.console.aliyun.com/cfw)。
2. 在左侧导航栏，选择**系统设计 > 多账号统一管理**。
3. 进入多账号统一管理页面，点击 **立即升级**，按照需求选择配购买版本、配置。
4. 点击 **立即购买**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973065.png)
5. 开通后可点击 **添加成员账号** 进行手动添加。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973073.png)
6. 也可使用云防火墙[OpenAPI](https://next.api.aliyun.com/api/Cloudfw/2017-12-07/AddInstanceMembers)来添加成员账号。

#### 结果验证

**步骤 1** 查看当前云防火墙多账号统一管理对应的成员账号列表。

1. 登入MA账号，进入[云防火墙控制台](https://yundun.console.aliyun.com/cfw)。
2. 在左侧导航栏，选择**系统设置 > 多账号统一管理**。
3. 查看当前成员账号列表。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973075.png)

**步骤 2** 通过云治理中心的账号工厂创建新账号。

1. 登入MA账号，进入[云治理中心控制台](https://governance.console.aliyun.com/)。
2. 在左侧导航栏，选择**Landing Zone > 账号工厂**。
3. 进入账号工厂页面，点击 **创建账号**，按照需要创建一个新账号。详见[使用账号基线创建账号](https://help.aliyun.com/zh/cgc/user-guide/create-an-account)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973074.png)
4. 等待创建完成。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973076.png)

**步骤 3** 验证云防火墙多账号统一管理中，新成员账号是否添加成功。

1. 登入MA账号，进入[云防火墙控制台](https://yundun.console.aliyun.com/cfw)。
2. 在左侧导航栏，选择**系统设置 > 多账号统一管理**。
3. 查看新建账号已被添加至成员账号列表中进行统一管理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5586581571/p973077.png)

## 相关内容

- [通过FC函数角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-242)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-279（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
