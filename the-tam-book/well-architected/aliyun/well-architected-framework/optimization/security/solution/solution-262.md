<!-- source: https://help.aliyun.com/zh/well-architected/solution-262 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2928328 -->

# 通过访问分析识别和收敛外部访问

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965886.png)

企业在日常用云的过程中，为保证业务的灵活性，通常会出现外部访问授权的情形，如账号A会将部分云资源授权给账号B乃至多个账号使用，运维团队对此难以及时跟踪，存在安全风险。为了既不影响业务协同的灵活性，又保障企业账号的安全，本方案介绍如何通过Access Analyzer访问分析服务来帮助企业及时发现存在跨账号访问权限的资源，从而判断该访问的合理性并收敛非必要的外部访问权限。

## 方案优势

### 持续分析识别非预期资源分享

Access Analyzer外部访问分析器会持续监测您的资源目录或当前账号内的资源策略，对存在共享给外部身份的资源生成分析结果，帮助您识别非预期的资源分享，降低企业安全风险。 每条分析结果都包含资源授予的外部身份以及授予的操作权限信息。

### 多账号统一分析

Access Analyzer支持在企业管理账号中基于资源目录搭建的多账号环境，进行统一的访问分析。资源目录内的所有账号的身份均被认为是可信的，方便企业进行统一的审计和治理。

### 支持串联自动化流程

可以通过EventBridge事件总线，监听消费Access Analyzer访问分析的分析结果。当发现非预期的资源分享后，自动触发您的自动化流程进行报警或修复。

## 客户场景

### 账号访问风险统一监控和收敛

#### 场景描述

企业在云账号的日常使用过程中，由于业务需要，经常会向外部账号授予访问权限，如供应商需要访问企业账号内的云资源上，运维团队希望对现有业务账号存在外部访问的权限做统一持续的监控和分析，根据检测出的结果与业务团队沟通，从而判断权限授予的必要性，对非必要的外部访问权限做相应的收敛，减小安全风险。

#### 适用客户

- 希望对账号的外部访问风险实时监控从而及时收敛治理访问权限的企业客户。

### OSS Bucket公共访问识别并自动修复

#### 场景描述

企业在日常用云过程中，由于缺乏管控手段等，存在OSS Bucket开启了非预期的公共访问，存在敏感数据泄露的风险。希望能够统一进行监控识别，并自动修复，关闭OSS Bucket的公共访问。

#### 适用客户

- 使用了OSS的企业客户，期望对非预期的公共访问进行监控和自动修复，以保证数据的安全性。

## 方案架构

本方案通过访问分析，实时分析并持续监测您的资源目录或当前账号内的资源策略，对存在共享给外部身份的资源生成分析结果，帮助您识别非预期的资源分享。您可以使用访问分析，创建分析范围为资源目录的外部访问分析器。资源目录内的所有账号的身份均被认为是可信的，资源目录外其他账号内身份被认为是非可信的。外部访问分析器会实时分析您所有账号下的RAM角色和OSS Bucket，判断其是否开放给了企业外的非可信账号（图中1）。您可以通过EventBridge事件总线监听并消费访问分析的分析结果（图中2、3）。根据分析结果，您可以及时对非预期的外部访问进行收敛，从而降低企业安全风险（图中4）。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965884.png)

同时，针对OSS Bucket非预期的公共访问场景。您可以使用访问分析配合函数计算的能力，对开启了公共访问的OSS Bucket进行自动修复，避免数据泄露。当访问分析扫描到OSS Bucket有开启公共访问后（图中1），通过EventBridge事件总线自动触发函数计算的运行（图中2、3），函数计算根据分析结果对OSS Bucket进行自动修复，阻止公共访问（图中4）。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965883.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费 |
| 事件总线EventBridge | [事件总线EventBridge](https://help.aliyun.com/zh/eventbridge/?spm=a2c4g.11186623.0.0.55e537a90os0s6)是阿里云提供的一款无服务器事件总线服务，能够以标准化的CloudEvents 1.0协议在应用之间路由事件，帮助您轻松构建松耦合、分布式的事件驱动架构。 | 公测期间免费，详情参见[产品计费](https://help.aliyun.com/zh/eventbridge/product-overview/billing)。 |
| 访问控制RAM | [访问控制RAM](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)（Resource Access Management）是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费 |
| 函数计算FC | [函数计算FC](https://help.aliyun.com/zh/functioncompute/fc-3-0/product-overview/what-is-function-compute?spm=a2c4g.11186623.help-menu-2508973.d_0_2_0.1c9f7cf7k88UQJ)（Function Compute）是事件驱动的全托管计算服务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/functioncompute/fc-3-0/product-overview/billing-overview-1?spm=a2c4g.11186623.help-menu-2508973.d_0_3_0.25d5442bjXsGhU)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 权限策略 | 用于定义和控制RAM角色可以执行的操作和访问的资源的一种机制，权限策略可以分为系统策略和自定义策略。 |
| Bucket ACL | OSS提供Bucket级别的权限访问控制。Bucket目前有三种访问权限：public-read-write，public-read和private，对于private资源，需要获得授权才能访问。关于授权管理，可参考权限控制 。对于一个已经存在的Bucket，只有它的创建者可以通过OSS的Put Bucket Acl接口修改该Bucket的权限。 |
| Bucket Policy | OSS 推出的针对 Bucket 的授权策略，可以通过 Bucket Policy 授权子账户和其他账号访问指定的 OSS 资源。 |
| 访问分析 | 分析策略内容（RAM角色权限、Bucket ACL、Bucket Policy）来判定该账号或者资源目录是否存在外部访问权限。 |
| 外部访问 | 基于当前云账号，OSS Bucket和RAM角色授权范围包含其他账号就视为有外部访问权限。基于当前资源目录，OSS Bucket和RAM角色授权范围包含资源目录以外的账号就视为有外部访问权限。 |
| OSS Bucket公共访问 | 满足以下两种情况的任意一种，则被认为是允许公共访问：开启了OSS Bucket公开读或者公开写配置了OSS Bucket的Policy，授权对象是*或者含有公共访问语义。 |

## 安全性

### 使用RAM进行访问控制

如果您使用函数计算配合访问分析对外部访问的分析结果进行自动化处理，建议您对函数计算的访问权限进行精细化管控，详情参见使[用RAM进行访问控制](https://help.aliyun.com/zh/functioncompute/identity-management-and-access-control/)。

## 注意事项

### 支持外部访问分析器的资源类型

- OSS Bucket：对于OSS Bucket，外部访问分析器会分析Bucket的ACL和Bucket Policy，并结合“阻止公共访问”的配置生成最终分析结果。如果分析范围（即信任区）内的Bucket允许信任区外的实体访问，也包括匿名用户，分析器会为Bucket生成一条待处理的分析结果。
- RAM角色：对于RAM角色，外部访问分析器会分析角色的信任策略。信任策略是一种基于资源的策略，在创建RAM角色时指定。在信任策略中，可以指定允许扮演该RAM角色的可信实体。如果信任区内的RAM角色允许信任区外的实体访问，分析器会为角色生成一条待处理的分析结果。

### 外部访问分析器地域限制

外部访问分析器仅分析分析器所在地域的资源。如需分析其他地域资源，您需要在对应地域创建分析器。中心化部署的资源（如：RAM 角色）可被任意地域的分析器监测分析。

## 自动化模板

### 模板介绍

访问分析通过和事件总线集成，支持您使用事件总线接收访问分析的分析结果事件，并执行您自己的自动化程序，实现访问分析结果的自动修复和处理。这里针对最常见的OSS Bucket非预期公共访问的场景，通过访问分析、事件总线配合函数计算，实现自动化阻止OSS Bucket公共访问，避免非预期的公共访问，导致企业数据泄露，及时保证数据安全。本方案提供基于Terraform的自动化模板，为资源目录下的目标账号批量创建RAM角色并提供函数计算示例代码。

### 模板地址

模板详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-access-analyzer-external-access)。

## 实施步骤

### 实施准备

- 如果您基于资源目录进行多账号的访问分析，请提前开通资源目录并搭建多账号架构，详情参见[开通资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/enable-a-resource-directory)。
- 如果您需要通过EventBridge事件总线，将访问分析结果通知给您的运维团队或者发送给您的自动化处理流程，请提前开通事件总线，详情参见[开通事件总线EventBridge并授权](https://help.aliyun.com/zh/eventbridge/getting-started/activate-eventbridge-and-grant-permissions-to-a-ram-user)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟

### 操作步骤

#### 创建外部访问分析器

首先您需要在资源所在地域创建外部访问分析器，外部访问分析器仅分析分析器所在地域的资源。如需分析其他地域资源，您需要在对应地域创建分析器。其中，中心化部署的资源（如：RAM 角色）可被任意地域的分析器监测分析。

1. 登入企业管理主账号，使用RAM管理员进入[RAM控制台](https://ram.console.aliyun.com/overview?activeTab=overview)。在左侧导航栏，选择**访问分析 > 分析器**。
2. 在顶部菜单栏，选择地域。
3. 单击**创建分析器**，然后输入分析器名称、选择分析类型为**外部访问**、设置分析范围。分析范围选择**资源目录**，您也可以选择**当前账号**，只对当前账号进行访问分析。这里的分析范围就是分析器的**信任区**。分析器会监测信任区内支持分析的资源，并且认为信任区内身份对资源的访问是可信的。如果信任区是**当前账号**，则本账号内身份被认为是可信的，其他账号内身份被认为是非可信的。如果信任区是**资源目录**，则本账号所属资源目录内的所有账号的身份均被认为是可信的，资源目录外其他账号内身份被认为是非可信的。 最后单击**创建分析器。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965885.png)创建分析器后，会开始检测资源存在的外部访问情况，您需要等待一会才能看到分析结果。

#### 配置事件总线通知（可选）

您可以将访问分析的分析结果，通过EventBridge事件总线以邮箱等渠道，通知到您的运维团队。以便让您能够第一时间发现非预期的外部访问，降低企业安全风险。

1. 登入企业管理主账号，进入[事件总线控制台](https://eventbridge.console.aliyun.com/overview)。在左侧导航栏，选择**事件总线**。
2. 在顶部菜单栏，选择地域。需要注意的是，该地域需要和上一步中您创建的外部访问分析器所在地域相同。
3. 在云服务专用事件总线中，单击**创建规则**。
4. 输入规则名称配置基本信息，单击下一步配置事件模式。其中：事件源类型：选择**阿里云官方事件源**。事件源：选择**acs.accessanalyzer**访问分析。事件类型：选择**accessanalyzer:ExternalAccess:Finding**。模式内容：您可以通过模式内容继续对事件进行过滤，如下所示，您可以过滤出有效的访问分析事件（未归档、未删除的访问分析事件）。`{
 "source": [
 "acs.accessanalyzer"
 ],
 "type": [
 "accessanalyzer:ExternalAccess:Finding"
 ],
 "data": {
 "status": [
 "Active"
 ],
 "isDeleted": [
 false
 ]
 }
}`
5. 单击下一步配置事件目标。您可以使用邮箱或者钉钉等渠道，及时接收外部访问风险事件。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965887.png)

#### 查看并处理外部访问

1. 登入企业管理主账号，进入[RAM控制台](https://ram.console.aliyun.com/overview?activeTab=overview)。在左侧导航栏，选择**访问分析 > 分析器**。选择前面步骤创建的外部访问分析器，进入分析器详情。
2. 选择**分析结果**页签，查看外部访问的分析结果。这里，分别创建了一个授权给外部账号扮演的RAM角色和一个允许外部账号读写的OSS Bucket，以此为例。其中：RAM角色，通过信任策略开放给外部账号扮演。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965892.png)OSS Bucket，通过Bucket授权策略，开放给外部账号读写。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965889.png)通过外部访问分析，分析结果如下。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965890.png)您也可以前往**分析结果**页面，查看所有分析器的分析结果。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965894.png)
3. 单击结果ID，您可以进入具体扫描结果的详情页，查看是否公开、外部身份、访问操作、访问条件等详细内容。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965891.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965893.png)
4. 针对分析结果，您可以：对于符合您预期的资源共享行为，单击**归档结果**，直接将其归档。对于不符合您预期的资源共享行为，单击**前往治理**（当前账号内的资源）或**复制资源URL**（非当前账号内的资源），跳转到对应页面进行治理。
5. 对于RAM角色。进入对应RAM角色的详情页，切换到**信任策略**页签。修改信任策略，删除非预期的外部账号授权。
6. 对于OSS Bucket，进入该OSS Bucket的权限控制页面。如果您使用Bucket ACL，将OSS Bucket设置为了公共读、公共写或者权限策略中包含有公共访问的语义，那么，您可以在**阻止公共访问**页签，一键开启阻止公共访问。如果您使用Bucket授权策略，将OSS Bucket开放给某些外部用户访问，那么，需要修改Bucket授权策略，删除非预期的外部账号授权。

#### 通过函数计算自动阻止OSS Bucket公共访问（可选）

访问分析通过和事件总线集成，支持您使用事件总线接收访问分析的分析结果事件，并执行您自己的自动化程序，实现访问分析结果的自动修复和处理。这里针对最常见的OSS Bucket非预期公共访问的场景，通过访问分析、事件总线配合函数计算，实现自动化阻止OSS Bucket公共访问，避免非预期的公共访问，导致企业数据泄露，及时保证数据安全。

首先您需要登入企业管理主账号，根据**创建外部访问分析器**章节，完成外部访问分析器的创建。这里我们以分析范围为资源目录的多账号访问分析为例。对于分析范围为资源目录的多账号访问分析，自动修复时，您需要进行跨账号资源操作。这里，我们使用跨账号角色扮演的方式，实现跨账号的修复操作。

##### 创建函数RAM角色

您需要创建一个RAM角色，用于后续步骤中为函数计算实例绑定RAM角色，该角色后续统称为函数RAM角色。如此，避免在函数计算代码中透露出明文AK，减少AK泄露的风险。如已创建，可跳过本步骤。

1. 使用企业管理账号登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 在左侧导航栏，选择**身份管理 > 角色**。
3. 在**角色**页面，单击**创建角色**。
4. 在**创建角色**页面，选择可信实体类型为**阿里云服务**，然后单击**下一步**。
5. 选择角色类型为**普通服务角色**。输入**角色名称**和**备注**，以名为`AccessAnalyzerFcRole`的角色为例。选择可信服务为**函数计算**。单击**完成**。

成功创建函数RAM角色后，该RAM角色没有任何权限，您需要为该RAM角色授权，该函数RAM角色需要跨账号扮演到其他业务账号下的修复使用的RAM角色上，因此至少需要具有`AliyunSTSAssumeRoleAccess`的权限，建议您同时配置上`AliyunLogFullAccess`权限，以便进行日志记录和追踪。具体操作，请参见[为RAM角色授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-a-ram-role)。

##### 通过ROS跨账号批量创建修复RAM角色

您可以通过ROS模版和资源栈组为资源目录下的目标账号批量创建RAM角色。该RAM角色（后续统称为修复RAM角色）用来供上一步创建的函数RAM角色扮演，对本账号下的开启了公共访问的OSS Bucket进行修复。

###### 创建委派管理员

通过委派管理员账号，可以将组织管理任务与业务管理任务相分离，企业管理账号执行资源目录的组织管理任务，委派管理员账号执行ROS的业务管理任务，这符合安全最佳实践的建议。接下来将资源目录的共享服务账号或运维账号设置为委派管理员账号，从而作为ROS的管理员账号为成员账号部署资源栈。

1. 使用管理账号登录[资源管理控制台](https://resourcemanager.console.aliyun.com/?spm=a2c4g.11186623.0.0.1272250aoGn651)。
2. 在左侧导航栏，选择**资源目录 > 可信服务**。
3. 在**可信服务**页面，单击**资源编排(ROS)**服务**操作**列的**管理**。
4. 在**委派管理员账号**区域，单击**添加**。
5. 在**添加委派管理员账号**面板，选中成员(共享服务账号)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965895.png)
6. 单击**确定**。添加成功后，使用该委派管理员账号访问对应可信服务的多账号管理模块，即可进行资源目录组织范围内的管理操作。

###### 开启可信访问

当您开通了资源目录，使用资源目录的企业管理账号或委派管理员账号创建服务管理权限模式的资源栈组时，必须开启可信访问，授权服务管理权限。需要企业管理账号和委派管理员账号都开启可信访问。

1. 分别使用企业管理账号和共享服务账号（委派管理员）登录[资源编排控制台](http://ros.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源栈组**。
3. 在**资源栈组列表**页面，单击右上角的**开启可信访问**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965896.png)

###### 批量创建所需角色

1. 使用共享服务账号登录[资源编排控制台](https://ros.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源栈组**。
3. 在顶部菜单栏的地域下拉列表，选择资源栈组的所在地域。
4. 在**资源栈组列表**页面，单击**创建资源栈组**。
5. 在**指定模板**选择框中，勾选**选择已有模板**。
6. **模板录入方式**选择**输入模板**，**模板内容**选择**Terraform**。
7. 内容文本框右上角，选择打开本地文件夹。
8. 选择下载到本地的[部署代码](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-access-analyzer-external-access/ros/create-role-cross-account)，点击下一步。
9. 输入**资源栈组名称**和**资源栈组描述**，在**配置模板参数**页面，填写所需参数，然后单击下一步。**参数****说明**角色的名称批量创建的角色的名称，以名称`AccessAnalyzerAssumeRole`为例策略名绑定到该角色的权限策略的名称策略内容绑定到该角色的权限策略内容角色可信的账号允许扮演到该角色的账号，不填默认为当前账号可信账号下允许扮演的角色允许可信账号下扮演到该角色的角色名称，既前文**创建函数RAM角色**章节中创建的函数RAM角色名称。请确保该角色在可信账号下已经存在，否则会创建失败。其中的策略内容，针对本方案的场景，您可以填写如下策略内容，保证该角色具有阻止OSS Bucket阻止公共访问的权限。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "oss:PutBucketPublicAccessBlock"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`
10. 在**配置资源栈组**页面，选择**服务管理权限**，然后单击**下一步**。
11. 在**设置部署选项**页面，**部署目标**选择资源目录的目标账号的资源夹，同时启用**自动部署**。
12. 根据实际情况填写**地域**、**资源组**、**标签**、**部署选项**等信息，更多信息，请参见[参数说明](https://help.aliyun.com/zh/ros/user-guide/step-3-create-a-stack-group)。然后单击**下一步**。
13. 在**检查并确认**页面，检查资源栈组信息无误后，单击**创建资源栈组**。
14. 创建完成后，在该资源栈组的详情页的**实例**页签中，可以查看实例的状态，**最新**表示已经在业务账号下完成了角色的创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965897.png)

##### 部署函数计算

您可以通过事件总线自动触发函数计算的执行，在企业管理账号中通过函数计算统一对所有业务账号下开启了公共访问的OSS Bucket进行修复。以下步骤使用的是函数计算2.0，如果您使用的是函数计算3.0，请根据[函数计算3.0和2.0版本差异及兼容性说明](https://help.aliyun.com/zh/functioncompute/fc-3-0/product-overview/feature-updates-in-function-compute-3)进行相应调整。

1. 登入企业管理主账号，进入[函数计算控制台](https://fcnext.console.aliyun.com/cn-hangzhou/services)。在左侧导航栏，选择**服务及函数**。
2. 在顶部菜单栏，选择地域。需要注意的是，该地域需要和前文步骤中您创建的外部访问分析器所在地域相同。
3. 创建函数服务，需要注意的是，服务角色需要选择前文**创建函数RAM角色**章节中，创建的函数RAM角色。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0276581571/p965898.png)
4. 在函数服务中，创建函数，选择**使用内置运行时创建**的方式创建函数，其中：请求处理程序类型，选择**处理事件请求**。函数代码运行环境，选择**Java 8**。代码上传方式，选择通过**JAR包**上传代码。您可以从[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-access-analyzer-external-access/fc/java)中下载示例代码并通过`mvn -U clean package`命令打包成JAR包，上传到函数代码包一栏。在**高级配置**一栏中，**请求处理程序**请修改为`org.example.Main::handleRequest`。在**环境变量**一栏中，添加如下两个环境变量：
5. REGION：填写当前函数所在地域ID即可。
6. ASSUME_ROLE_NAME：跨账号扮演到的RAM角色名称，既前文**通过ROS跨账号批量创建修复RAM角色**章节中，创建的修复RAM角色的名称，以`AccessAnalyzerAssumeRole`为例。在**触发器配置**一栏中，进行如下配置：
7. 触发器类型，选择`acs.accessanalyzer`
8. 事件类型，选择**自定义事件类型**，对事件类型进行过滤，选择`accessanalyzer:ExternalAccess:Finding`
9. 事件模式内容，填写如下内容，过滤出未处理的开放了公共访问的OSS Bucket资源事件。`{
 "source": [
 "acs.accessanalyzer"
 ],
 "type": [
 "accessanalyzer:ExternalAccess:Finding"
 ],
 "data": {
 "resourceType": [
 "ACS::OSS::Bucket"
 ],
 "isPublic": [
 true
 ],
 "status": [
 "Active"
 ],
 "isDeleted": [
 false
 ]
 }
}`
10. 单击**创建**，完成函数的创建。如此，当您的账号下创建了开启公共访问的OSS Bucket时，外部访问分析器会通过事件总线，触发函数计算的执行，函数计算根据推送过来的资源事件信息，对该OSS Bucket进行修复，阻止其公共访问。

## 故障排除

### 为什么无法使用 ROS 服务管理权限模式？

- 如果使用资源目录成员账号执行ROS的业务管理任务，您需要将资源目录的成员账号设置为委派管理员账号，从而作为 ROS 的管理员账号为成员账号部署资源栈。关于 ROS 委派管理员，请参见[设置委派管理员账号](https://help.aliyun.com/zh/ros/user-guide/step-1-create-a-delegated-administrator-account)。
- 当您开通了资源目录，使用资源目录的企业管理账号或委派管理员账号创建服务管理权限模式的资源栈组时，必须开启可信访问，授权服务管理权限。关于可信访问，请参见[开启可信访问](https://help.aliyun.com/zh/ros/user-guide/step-2-enable-trusted-access)。

### 为什么执行函数失败？

在“运行环境”为 Java 时，出现`Cannot find the class example.App in your zip file and please make sure it is in the right path 'example/App'`错误，请确认**配置>运行时>请求处理程序**的格式为 [package].[class]::[method]。例如，当前值为`org.example.Main::handleRequest`，那么在函数被触发时，将执行org.example包中Main类中的 handleRequest 函数。

更多使用 FC 的常见问题，请参见 [FC 服务支持](https://help.aliyun.com/zh/functioncompute/support/faq/)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-262（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
