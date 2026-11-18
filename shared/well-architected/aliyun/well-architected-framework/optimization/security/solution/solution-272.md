<!-- source: https://help.aliyun.com/zh/well-architected/solution-272 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2928774 -->

# 通过访问分析识别和收敛过度授权

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967963.png)

合理的权限设置能够阻止未经授权的访问，保护云上资产和数据的安全。因此，云上的权限管理的核心原则就是权限最小化，只给身份授予必要的权限，确保权限最小够用。本方案通过RAM访问分析，帮助您识别过度授权的云上身份，及时收敛闲置权限，避免过度授权带来的云上资产和数据的安全风险。

## 方案优势

### 持续分析识别过度授权

Access Analyzer过度授权分析器可以帮助您识别资源目录或当前账号内过度授权的身份。分析器会持续监测您的资源目录或当前账号内的所有RAM身份（RAM用户和RAM角色），对存在过度授权的身份生成对应的分析结果。

### 多账号统一分析

Access Analyzer支持在企业管理账号中基于资源目录搭建的多账号环境，进行统一的访问分析，方便企业进行统一的审计和治理。

### 支持分析结果的实时通知

您可以通过EventBridge事件总线，监听消费Access Analyzer访问分析的分析结果，并通过短信、邮件等渠道通知到您的运维、安全团队，保证您可以及时的进行权限治理。

## 客户场景

### 身份权限统一监控和收敛

#### 场景描述

企业在云账号的日常使用过程中，权限管理比较粗放，存在过度授权，从而使云上身份拥有了其职责外的权限，尤其是一些特权权限。企业希望能够统一识别过度授权的云上身份，及时进行权限收敛，避免过度授权带来的云上资产和数据的安全风险。

#### 适用客户

- 存在中心运维团队、审计团队的企业客户。
- 有独立合规团队的企业客户。
- 权限管理粗放，希望进行精细化权限管理的企业客户。

## 方案架构

本方案通过RAM访问分析，帮助您识别资源目录或当前账号内过度授权的身份。分析器会持续监测您的资源目录或当前账号内的所有RAM身份（RAM用户和RAM角色），对存在过度授权的身份生成对应的分析结果。首先，您可以在企业管理账号中，通过RAM访问分析，创建过度授权分析器，对企业组织内所有账号的所有RAM用户和角色进行权限扫描，对其闲置权限、特权权限等进行分析（图中1）。然后通过EventBridge事件总线监听并消费访问分析的分析结果，通过短信、邮箱等渠道通知到您的运维、安全等团队（图中2、3）。根据访问分析结果，您可以及时进行权限收敛，比如，拒绝特权权限、清理闲置权限等等，从而降低企业安全风险（图中4）。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8176581571/p967962.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费 |
| 事件总线EventBridge | [事件总线EventBridge](https://help.aliyun.com/zh/eventbridge/?spm=a2c4g.11186623.0.0.55e537a90os0s6)是阿里云提供的一款无服务器事件总线服务，能够以标准化的CloudEvents 1.0协议在应用之间路由事件，帮助您轻松构建松耦合、分布式的事件驱动架构。 | 公测期间免费，详情参见[产品计费](https://help.aliyun.com/zh/eventbridge/product-overview/billing)。 |
| 访问控制RAM | [访问控制RAM](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)（Resource Access Management）是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 权限策略 | 用于定义和控制RAM身份可以执行的操作和访问的资源的一种机制，权限策略可以分为系统策略和自定义策略。 |
| 访问分析-过度授权分析器 | 过度授权分析器可以帮助您识别和查看资源目录或当前账号内过度授权的身份。分析器会持续监测您的资源目录或当前账号内的所有RAM身份（RAM用户和RAM角色），对存在过度授权的身份生成对应的分析结果。分析器产生的分析结果包含超级管理员用户/角色、特权用户/角色、不活跃的用户/角色、过度授权的用户/角色。每条分析结果还会进一步提供身份拥有的权限，以及权限的最近访问信息。 |
| 权限审计 | 权限审计功能可以帮助您识别RAM身份所拥有的权限，以及权限的最近访问时间。您可以基于此信息识别未使用的权限，并将其安全地删除，从而遵循RAM身份的最小授权原则。 |
| 超级管理员用户/角色 | 拥有账号内所有资源管理权限的RAM身份（RAM用户或RAM角色）。例如，被授予AdministratorAccess权限策略的RAM用户或RAM角色。 |
| 特权用户/角色 | 拥有高危特权的RAM身份（RAM用户或RAM角色）。拥有这类特权的RAM身份往往可以为自己或其他RAM身份提升权限，使得他们获得更高的访问权限。详细的特权列表，请参见[特权列表](https://help.aliyun.com/zh/ram/identify-over-authorization)。 |
| 不活跃的用户/角色 | 在指定的**闲置访问周期**内，没有任何权限访问活动的RAM身份（RAM用户或RAM角色）。 |
| 过度授权的用户/角色 | 在指定的**闲置访问周期**内，拥有未使用的服务粒度和操作粒度权限的RAM身份（RAM用户或RAM角色）。 |
| 普通角色 | 普通角色允许客户自主创建和管理，需要客户自定义角色名称，选择可信实体，并自定义权限策略。普通角色又可以简单分为以下两类。普通用户角色：普通角色类型的一种，一般由客户自主创建，授信给用户或者身份提供商，供客户自己或身份提供商扮演使用，比如实现RAM角色SSO单点登录。普通服务角色：普通角色类型的一种，需要客户自定义角色名称，选择可信实体为云服务，并自定义权限策略。该角色授信给云服务，由云服务扮演，云服务一般用来完成其某项功能而使用，比如阿里云容器服务使用到的`AliyunCSDefaultRole`、`AliyunCSKubernetesAuditRole`等角色。 |
| 云服务保留角色 | 该角色带有`AliyunReserved`前缀，其生命周期的管理托管在对应云服务中，客户需要在对应云服务中对角色进行操作，不允许在RAM控制台或者通过RAM API进行管理操作。 |

## 安全性

### 访问分析安全性

访问分析不会对您现有的RAM身份和策略进行任何修改，并且完全不会影响您的RAM鉴权行为。请您放心使用。

## 注意事项

### 访问分析过度授权分析器的支持范围

访问分析过度授权类型的分析器会查看资源目录或当前账号内所有RAM身份（服务关联角色除外）的权限审计信息，并使用权限审计信息产生分析结果。权限审计功能提供了RAM身份所拥有的权限，以及权限的最近访问时间。因此，过度授权分析器所支持的策略类型、云服务列表及审计粒度与权限审计保持一致。具体信息，请参见[权限审计概览](https://help.aliyun.com/zh/ram/overview-of-permissions-audit)。

### 权限审计注意事项

在使用访问分析权限审计功能分析并处理RAM身份权限时，请务必仔细阅读如下注意事项。更多使用须知，请参见[权限审计概览](https://help.aliyun.com/zh/ram/overview-of-permissions-audit)。

#### 权限审计跟踪期

访问的跟踪期于2024-02-01开始，早于此时间的访问将不会被记录。最近访问时间的数据延迟不超过24小时。

#### 权限审计支持的策略类型

权限审计仅分析基于身份的策略，即授予RAM用户、RAM用户组、RAM角色的权限策略。权限审计不会分析其他类型的权限策略，包括基于资源的策略（例如：OSS Bucket Policy）、资源目录的管控策略和会话策略。

#### 权限审计支持的审计粒度

- 服务级别：在云服务维度对RAM身份的权限和访问进行分析。您可以查看RAM身份被授予的云服务的权限，访问过的云服务及访问云服务的最后时间。以此用来撤销无需使用的系统策略，或者将管理员权限收敛成具体云服务的管理权限。支持服务级别审计的云服务，请参见[支持权限审计的云服务](https://help.aliyun.com/zh/ram/cloud-services-that-support-permission-auditing)。
- 操作级别：在服务级别的基础上，进一步细化到具体的API操作（Action），在操作维度对RAM身份的权限和访问进行分析。您可以查看RAM身份被授予的具体API操作的权限，访问过的API操作及访问API操作的最后时间。以此用来对应用程序进行精细化权限管控，或者对高危权限进行收敛。支持操作级别审计的云服务，请参见[支持权限审计的云服务](https://help.aliyun.com/zh/ram/cloud-services-that-support-permission-auditing)**审计粒度**列标识为**操作级别**的云服务。

权限审计仅支持云服务已接入操作审计管控平面的操作，不支持存储在云服务中的数据平面的操作（例如：OSS 的 GetObject）。

## 实施步骤

### 实施准备

- 如果您基于资源目录进行多账号的访问分析，请提前开通资源目录并搭建多账号架构，详情参见[开通资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/enable-a-resource-directory)。
- 如果您需要通过EventBridge事件总线，将访问分析结果通知给您的运维团队，请提前开通事件总线，详情参见[开通事件总线EventBridge并授权](https://help.aliyun.com/zh/eventbridge/getting-started/activate-eventbridge-and-grant-permissions-to-a-ram-user)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 创建过度授权分析器

目前，您可以在任意地域创建过度授权分析器，对于RAM角色和RAM用户这种中心化部署的资源可被任意地域的分析器监测分析。分析结果不受地域影响。

1. 登入企业管理主账号，使用RAM管理员进入[RAM控制台](https://ram.console.aliyun.com/overview?activeTab=overview)。在左侧导航栏，选择**访问分析 > 分析器**。
2. 在顶部菜单栏，选择地域。
3. 单击**创建分析器**，然后输入分析器名称、选择分析类型为**过度授权**、设置闲置访问周期和分析范围。其中，**闲置访问周期**是用来确定闲置的判断范围，取值范围为1~365天，默认值为90天。 例如：将**闲置访问周期**设置为90，意味着超过90天未使用的权限将被判定为闲置。分析范围选择**资源目录**，您也可以选择**当前账号**，只对当前账号进行访问分析。最后单击**创建分析器。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967964.png)

创建分析器后，会开始检测RAM身份及权限，您需要等待一会才能查看分析结果。

#### 配置事件总线通知（可选）

您可以将访问分析的分析结果，通过EventBridge事件总线以短信、邮箱等渠道，通知到您的运维、安全团队。以便让您能够第一时间发现非预期的过度授权行为，降低企业安全风险。

1. 登入企业管理主账号，进入[事件总线控制台](https://eventbridge.console.aliyun.com/overview)。在左侧导航栏，选择**事件总线**。
2. 在顶部菜单栏，选择地域。需要注意的是，该地域需要和上一步中您创建的过度授权分析器所在地域相同。
3. 在云服务专用事件总线中，单击**创建规则**。
4. 输入规则名称配置基本信息，单击下一步配置事件模式。其中：事件源类型：选择**阿里云官方事件源**。事件源：选择**acs.accessanalyzer**访问分析。事件类型：不同的分析结果对应不同的事件类型，您可以根据需要进行选择，建议您将以下类型全部勾选。
5. accessanalyzer:InactiveRole:Finding/accessanalyzer:InactiveUser:Finding：不活跃的角色/用户。
6. accessanalyzer:OverPrivilegedRole:Finding/accessanalyzer:OverPrivilegedUser:Finding：过度授权的角色/用户。
7. accessanalyzer:PrivilegeEscalationRole:Finding/accessanalyzer:PrivilegeEscalationUser:Finding：特权角色/用户。
8. accessanalyzer:SuperRole:Finding/accessanalyzer:SuperUser:Finding：超级管理员角色/用户。模式内容：您可以通过模式内容继续对事件进行过滤，如下所示，您可以过滤出有效的访问分析事件（未归档、未删除的访问分析事件）。`{
 "source": [
 "acs.accessanalyzer"
 ],
 "type": [
 "accessanalyzer:InactiveRole:Finding",
 "accessanalyzer:InactiveUser:Finding",
 "accessanalyzer:OverPrivilegedRole:Finding",
 "accessanalyzer:OverPrivilegedUser:Finding",
 "accessanalyzer:PrivilegeEscalationRole:Finding",
 "accessanalyzer:PrivilegeEscalationUser:Finding",
 "accessanalyzer:SuperRole:Finding",
 "accessanalyzer:SuperUser:Finding"
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

1. 单击下一步配置事件目标。您可以使用邮箱或者钉钉等渠道，及时接收过度授权风险事件。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967965.png)

#### 查看分析结果

分析器产生的分析结果包含4个过度授权的场景类型，分别是：

- 超级管理员用户/角色：拥有账号内所有资源管理权限的RAM身份（RAM用户或RAM角色）。例如，被授予AdministratorAccess权限策略的RAM用户或RAM角色。
- 特权用户/角色：拥有高危特权的RAM身份（RAM用户或RAM角色）。拥有这类特权的RAM身份往往可以为自己或其他RAM身份提升权限，使得他们获得更高的访问权限。详细的特权列表，请参见[特权列表](https://help.aliyun.com/zh/ram/identify-over-authorization)。
- 不活跃的用户/角色：在指定的**闲置访问周期**内，没有任何权限访问活动的RAM身份（RAM用户或RAM角色）。
- 过度授权的用户/角色：在指定的**闲置访问周期**内，拥有未使用的服务粒度和操作粒度权限的RAM身份（RAM用户或RAM角色）。

您可以通过以下两种方式，查看分析结果。首先您可以通过**分析器**页面查看。

1. 登入企业管理主账号，使用RAM管理员进入[RAM控制台](https://ram.console.aliyun.com/overview?activeTab=overview)。在左侧导航栏，选择**访问分析 > 分析器**。
2. 选择上文**创建过度授权分析器**章节中，创建的过度授权分析器，单击分析器名称，进入分析器详情页。
3. 在分析结果页签中，查看分析结果。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8176581571/p967966.png)

其次，您可以通过**分析结果**页面查看分析结果。

1. 登入企业管理主账号，使用RAM管理员进入[RAM控制台](https://ram.console.aliyun.com/overview?activeTab=overview)。在左侧导航栏，选择**访问分析 > 分析结果**。
2. 选择上文**创建过度授权分析器**章节中，创建的过度授权分析器，单击分析器名称。
3. 在结果列表页签中，查看分析结果。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967967.png)
4. 分析结果页面中，还提供了图像化的数据概览，单击**数据概览**页签，查看图像化的结果展示。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967969.png)

#### 分析并处理过度授权

对于分析结果中，待处理的资源（RAM用户/角色），您需要进入分析结果的详情页，通过访问记录，进一步确认该RAM身份上的授权行为是否符合预期。

1. 进入上文**查看分析结果**章节中的分析结果页面。
2. 在分析结果列表中，单击**结果ID**，查看相应资源（RAM用户/角色）的分析结果详情。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8176581571/p967971.png)

通过详细信息页签中的访问记录，您可以详细的分析特权授予与权限闲置的情况，以此判断授权行为是否符合预期。在访问记录列表中，建议您重点关注：

- 最近访问时间为**没有访问**，那么该云服务的权限大概率为闲置权限，建议您根据该RAM用户/角色使用者的身份，进一步评估是否符合预期。需要注意的是，访问分析的跟踪期于2024-02-01开始，早于此时间的访问将不会被记录。
- 云服务名称后面存在**特权**标识，则表明您授予了该RAM身份特权权限。此时，您可以单击操作列中的**查看鉴权操作**，查看云服务具体操作的调用情况。建议您重点关注鉴权操作列表中带有**特权**标识的操作，结合操作的最后访问时间，进一步评估该RAM身份持有此特权权限是否符合预期。

针对分析结果，您可以：

- 对于符合您预期的授权行为，单击**归档结果**，直接将其归档。
- 对于不符合您预期的授权行为，单击**前往治理**（当前账号内的资源）或**复制资源URL**（非当前账号内的资源），跳转到对应页面进行治理。

当然，不同场景类型的分析结果，对应的处理方式不同，您需要根据分析结果，结合企业实际使用情况，配合操作审计信息，辅助您收敛过度授权。您可以根据以下的顺序，针对不同的过度授权的场景，逐个进行持续处理。

##### 前置准备

###### 确认RAM用户使用情况

在处理RAM用户过度授权时，首先，您需要明确该RAM用户的使用情况，来辅助您进行决策，包含以下信息：

1. RAM用户是否登录过控制台。您可以进入该RAM用户的详情页，在**认证管理**页签下，查看**上次登录控制台时间**，如果存在上次登录控制台时间，则表明该RAM用户登录过控制台。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967968.png)
2. RAM用户是否创建有AccessKey。您可以进入该RAM用户的详情页，在**认证管理**页签下，查看AccessKey列表中是否创建有AccessKey。
3. 如果RAM用户创建有AccessKey，您需要进一步确认该AccessKey是否使用过。您可以在AccessKey列表中，查看**最后使用云服务 / 时间**，如果存在最后使用的云服务和时间，则表明该RAM用户的AccessKey有使用过。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967973.png)

###### RAM角色处理路径

访问分析中，会对以下两种类型的角色进行分析。

- 普通角色：普通角色允许客户自主创建，需要客户自定义角色名称，选择可信实体，并自定义权限策略。普通角色又可以简单分为以下两类。普通用户角色：普通角色类型的一种，一般由客户自主创建，授信给用户或者身份提供商，供客户自己或身份提供商扮演使用，比如实现RAM角色SSO单点登录。普通服务角色：普通角色类型的一种，需要客户自定义角色名称，选择可信实体为云服务，并自定义权限策略。该角色授信给云服务，由云服务扮演，云服务一般用来完成其某项功能而使用，比如阿里云容器服务使用到的`AliyunCSDefaultRole`、`AliyunCSKubernetesAuditRole`等角色。
- 云服务保留角色：该角色带有`AliyunReserved`前缀，其生命周期的管理托管在对应云服务中，客户需要在对应云服务中对角色进行操作，不允许在RAM控制台或者通过RAM API进行管理操作。

不同类型的角色，处理路径不同：

- 普通用户角色：客户在RAM控制台可以自主对角色的生命周期进行管理操作。这类角色，可以直接在RAM控制台或通过RAM API进行过度授权的处理优化。详细的处理优化操作请参见下文所述。
- 普通服务角色：除非您明确知道该云服务您后续不再使用，否则，不建议您进行任何修改和删除，以防对您使用的云服务产生影响。对于这类角色的分析结果，建议您可以直接将分析结果进行归档处理。
- 云服务保留角色：这类角色，需要前往对应云服务中进行过度授权的处理优化。建议您根据云服务的功能形态来决策是否需要对此类角色进行处理，尤其是云SSO的访问配置，您在云SSO中部署访问配置时，会在您所有要部署的账号下创建一个名为`AliyunReservedSSO-<访问配置名称>`的RAM角色，这些部署在不同账号下的同名角色，同样具有相同的权限配置。因此，您无法在访问分析中，通过某一个账号的分析结果，来决策该云SSO访问配置整体的使用情况。因此，对于这类角色的分析结果，建议您可以直接将分析结果进行归档处理。当然您也可以自行根据角色名称，对多个账号进行聚合分析，如果您能够明确其过度授权的情况并需要进行处理，您需要在云SSO中，调整对应访问配置的权限设置。详细信息，请参阅[访问配置概述](https://help.aliyun.com/zh/cloudsso/user-guide/overview-1)。

另外，对于普通服务角色和云服务保留角色，如果您确定后续无需处理优化，需要在分析结果中忽略此类角色。您可以通过归档规则，将此类角色的分析结果自动归档。

1. 在分析结果页面，添加以下两个筛选条件对结果进行筛选。筛选条件：资源、匹配方式：包含、筛选值：aliyun筛选条件：资源类型、匹配方式：等于、筛选值：访问控制 - 角色
2. 单击**保存为归档规则**，如此设置完规则后，会对新产生的符合归档规则的分析结果进行自动归档。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967972.png)
3. 但是，设置规则前的分析结果不会自动归档，如您需要，可以在分析器详情页面单击应用归档规则，将其归档。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967970.png)

##### 超级管理员用户/角色

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967975.png)

在分析结果列表中，结果类型为超级管理员用户/角色，则表示该RAM用户/角色拥有账号内所有资源管理权限。例如，被授予AdministratorAccess权限策略的RAM用户或RAM角色。

针对这类分析结果，首先，您的运维团队需要确认该RAM身份是否必须拥有Administrator权限，一般来说，企业内只有个别身份需要被授予账号内所有资源管理权限，比如企业的运维负责人等。建议您将拥有Administrator权限的RAM身份控制在3个及以下，避免给过多的RAM身份授予Administrator权限，以免身份泄露对业务造成影响。

- 如果您确认该超级管理员用户/角色符合预期，那么您可以在分析结果中，单击**归档结果**，直接将其归档。
- 如果不符合预期，那么对于RAM用户和RAM角色，您可以按照下文所述，分别进行处理。您对RAM用户和角色的修改，会触发访问分析的重新运行，一般会有3-5分钟的触发延时，处理完成后，您可以稍后在访问分析的分析结果中，查看该RAM身份过度授权的问题是否真实得到解决。

###### RAM用户

针对不同使用情况的RAM用户，建议您采取下文所述步骤，进行针对性的处理。

###### 1. RAM用户登录过控制台

使用该RAM用户的企业员工一般是负责企业云上运维管理的人员，建议通过权限模版，对其权限进行降级。您可以使用超级用户的权限模版，让其可创建、查看、操作所有的云服务，但是不能管理身份权限、账号架构、使用财务关联。

1. 创建新的自定义权限策略，在创建权限策略页面，单击**导入策略**，根据企业员工职能，选择并导入对应的权限模版。详细操作，请参见[创建自定义权限策略](https://help.aliyun.com/zh/ram/create-a-custom-policy)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967976.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967977.png)除了超级用户的权限模版，目前阿里云也提供以下几个常用的企业员工职能权限模版，如果使用该RAM用户的企业员工具有明确的工作职能，建议您通过权限模版基于其职能进行授权：超级用户：负责企业的云上运维管理，可创建、查看、操作所有的云服务，不能管理身份权限、不能管理账号架构、不能使用财务关联。财务人员：负责企业的财务工作，可查看账单、充值付款、开取发票等，可使用财务分析功能，拥有财账系统的全部权限。网络管理员：负责企业的网络架构搭建和管理，可开通和购买创建网络服务，拥有网络服务的所有权限和 ECS 安全组的权限。数据库管理员：负责企业的数据库运维管理，可开通和购买创建数据库服务，拥有数据库服务的所有权限。安全管理员：负责企业云上安全，可开通和购买云安全服务，制定并实施安全规则，拥有安全服务的所有权限。审计管理员：具有配置审计、操作审计和日志管理的全部权限，同时可以查询所有阿里云资源现状。
2. 将新建的自定义权限策略，授予RAM用户，同时解除具有Administrator的权限策略（包括AdministratorAccess系统策略和包括Administrator语义的自定义策略）。详细操作，请参考[为RAM用户授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-the-ram-user)、[为RAM用户移除权限](https://help.aliyun.com/zh/ram/revoke-permissions-from-a-ram-user)。
3. 如果该RAM用户同时创建有AccessKey，则违背了单一职责原则，建议您尽快进行迁移，保证一个RAM用户只用来进行控制台登录或者只用来创建和使用AccessKey。

###### 2. RAM用户未登录过控制台，但是该RAM用户创建有AccessKey。

1. 如果AccessKey未曾使用。此类RAM用户大概率是闲置用户，建议您及时进行清理。禁用控制台登录。您可以在RAM用户详情页，在**认证管理**页签下的**控制台登录管理**区域，单击**修改登录设置**，将控制台访问设置为禁用。详细操作，请参考[管理RAM用户登录设置](https://help.aliyun.com/zh/ram/manage-console-logon-settings-for-a-ram-user-1)。禁用AccessKey。建议您优先禁用该AccessKey，避免该AccessKey发生泄露从而导致安全风险。如果后续发现您的业务团队有使用该AccessKey的需要，您也可以在控制台上一键启用。详细操作，请参考[禁用RAM用户的AccessKey](https://help.aliyun.com/zh/ram/user-guide/disable-an-accesskey-pair-of-a-ram-user)。在观察一段时间，确认AccessKey无需使用后，建议您删除AccessKey，并进一步删除该RAM用户。详细操作，请参考[删除RAM用户的AccessKey](https://help.aliyun.com/zh/ram/user-guide/delete-an-accesskey-pair-of-a-ram-user)、[删除RAM用户](https://help.aliyun.com/zh/ram/user-guide/delete-a-ram-user)。
2. 否则（AccessKey使用过），建议您按如下步骤进行权限收敛。禁用控制台登录。您可以在RAM用户详情页，在**认证管理**页签下的**控制台登录管理**区域，单击**修改登录设置**，将控制台访问设置为禁用。详细操作，请参考[管理RAM用户登录设置](https://help.aliyun.com/zh/ram/manage-console-logon-settings-for-a-ram-user-1)。收敛闲置权限。阿里云提供了权限审计功能可以帮助您识别RAM身份所拥有的权限，以及权限的最近访问时间。需要注意的是权限审计的访问跟踪期于2024-02-01开始，如果AccessKey最后使用时间早于2024-02-01，那么在权限审计中将不会有记录。因此，无论在权限审计中，该RAM用户是否有权限访问活动，您的运维团队和业务团队都需要一起参与，确认该AccessKey在具体的业务场景中，需要使用到的操作权限，将未使用或无需使用的权限安全的删除，从而遵循RAM身份的最小授权原则。
3. 您可以在过度授权分析器的分析结果页面，单击**前往治理**（当前账号内的资源）或**复制资源URL**（非当前账号内的资源），跳转到该RAM用户的权限审计页面。通过权限审计，确认存在访问的云服务，同时，对于支持操作级别审计的云服务，您可以单击**操作**列的**查看鉴权操作**，查看存在调用的API操作。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967978.png)
4. 建议您的运维团队和业务团队共同参与，确认AccessKey在业务中真实调用的云服务和API，配合上一步权限审计的结果，确认AccessKey所需的真实最小的权限。
5. 新建自定义权限策略，策略内容为上一步中确认的收敛后的权限。然后将自定义权限策略，授予RAM用户，同时解除具有Administrator的权限策略（包括AdministratorAccess系统策略和包括Administrator语义的自定义策略）。详细操作，请参考[创建自定义权限策略](https://help.aliyun.com/zh/ram/create-a-custom-policy)、[为RAM用户授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-the-ram-user)、[为RAM用户移除权限](https://help.aliyun.com/zh/ram/revoke-permissions-from-a-ram-user)。收敛过程建议您逐步进行，首先收敛到云服务级别，根据AccessKey真实调用的云服务，授予对应云服务的FullAccess权限。观察对业务无影响后，再进一步将权限收敛到API操作级别。在此过程中，您需要密切关注业务情况，如果对业务运行产生了影响，请立刻使用权限策略的版本功能进行回滚（详细操作，请参见[管理自定义权限策略版本](https://help.aliyun.com/zh/ram/manage-custom-policy-versions)）或者在RAM用户上绑定原来的具有Administrator权限的策略。

###### 3. RAM用户未登录过控制台，并且该RAM用户未创建有AccessKey。

此类RAM用户大概率是闲置用户，建议您及时进行清理。

1. 禁用控制台登录。您可以在RAM用户详情页，在**认证管理**页签下的**控制台登录管理**区域，单击**修改登录设置**，将控制台访问设置为禁用。详细操作，请参考[管理RAM用户登录设置](https://help.aliyun.com/zh/ram/manage-console-logon-settings-for-a-ram-user-1)。
2. 删除RAM用户。如果确认该RAM用户未真实使用，建议您直接删除该RAM用户。详细操作，请参考[删除RAM用户](https://help.aliyun.com/zh/ram/user-guide/delete-a-ram-user)。

###### RAM角色

目前，阿里云暂时无法识别最近一次扮演RAM角色的时间，从而无法准确确定RAM角色的使用情况，因此对RAM角色的过度授权优化，需要依赖客户的自主决策。您可以在过度授权分析器的分析结果页面，单击**前往治理**（当前账号内的资源）或**复制资源URL**（非当前账号内的资源），跳转到该RAM角色的权限审计页面。通过权限审计，确认该RAM角色是否存在访问过的云服务，以此辅助您进行决策。

- 如果RAM角色是普通服务角色或者云服务保留角色，除非您明确知道该角色的使用情况，否则，不建议您进行任何修改，您可以直接将分析结果进行归档处理。您可以按照前文**前置准备-RAM角色处理路径**章节，通过归档规则将此类角色的分析结果自动归档。
- 对于其他普通用户角色，如果确认RAM角色未真实使用或者后续不再使用，建议您直接删除该RAM角色。详细操作，请参考[删除RAM角色](https://help.aliyun.com/zh/ram/user-guide/delete-a-ram-role)。
- 否则，建议您尽快收敛闲置权限。建议您的运维团队和业务团队共同参与，确认RAM角色在业务中真实调用的云服务和API，配合权限审计的结果，确认RAM角色所需的真实最小的权限。对于普通用户角色，您需要在RAM控制台创建新的权限策略，将权限收敛为真实所需权限，并绑定到RAM角色身上，同时解除具有Administrator的权限策略（包括AdministratorAccess系统策略和包括Administrator语义的自定义策略）。详细操作，请参考[创建自定义权限策略](https://help.aliyun.com/zh/ram/create-a-custom-policy)、[为RAM角色授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-a-ram-role)、[为RAM角色移除权限](https://help.aliyun.com/zh/ram/remove-permissions-from-a-ram-role)。

收敛过程建议您逐步进行，首先收敛到云服务级别，根据RAM角色真实使用的云服务，授予对应云服务的FullAccess权限。观察对业务无影响后，再进一步将权限收敛到API操作级别。在此过程中，您需要密切关注业务情况，如果对业务运行产生了影响，请立刻进行回滚或者重新绑定原来的具有Administrator权限的策略。

##### 特权用户/角色

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967980.png)

进入分析结果详情页，通过详细信息页签中的访问记录，您可以详细的分析特权授予情况。如果云服务名称后面存在**特权**标识，则表明您授予了该RAM身份的权限中包含有特权权限，详细的特权列表，请参见[特权列表](https://help.aliyun.com/zh/ram/identify-over-authorization)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967981.png)

此时，您可以单击操作列中的**查看鉴权操作**，查看云服务具体操作的调用情况。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967982.png)

您需要重点关注鉴权操作列表中带有**特权**标识的操作，结合操作的最后访问时间，进一步评估该RAM身份持有此特权权限是否符合预期。在进行处理时，您可以在过度授权分析器的分析结果页面，单击**前往治理**（当前账号内的资源）或**复制资源URL**（非当前账号内的资源），跳转到该RAM身份的权限审计页面。通过权限审计列表中的**授予权限的策略**信息，确认该特权权限定义在哪个权限策略中，方便您后续进行优化处理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967983.png)

针对不同的RAM身份，处理方式略有不同，详细处理操作请参考下文所述。处理过程中，您需要密切关注业务情况，如果对业务运行产生了影响，请立刻进行回滚。

###### RAM用户

- 如果特权操作最近访问时间为**没有访问**，则该操作自2024-02-01后没有调用访问过，建议您进行收敛。首先，您可以在分析结果详情页，切换到**治理建议**页签，访问分析会根据分析结果给出治理建议，对于在闲置访问周期内，不存在权限访问的权限策略，提供一键解除授权的能力，帮助您快速收敛闲置权限（需要注意的是，只有分析结果的资源拥有者才能执行治理操作）。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967974.png)如果特权操作的权限，并不在上一步未使用的权限策略中定义。既包含特权操作的权限策略在闲置访问周期内存在权限访问行为。您需要进一步解除或者拒绝特权操作。
- 如果授予该特权权限的策略是自定义权限策略，并且在自定义权限策略中直接明确显式的定义，比如下述的权限策略示例，明确指定授予了`ram:UpdateAccessKey`权限。此时，建议您直接修改自定义策略，在策略内容中删除特权权限。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ram:UpdateAccessKey"
 ],
 "Resource": "*"
 }
 ]
}`
- 如果授予该特权权限的策略是自定义权限策略，但是在自定义策略中通过通配符的方式未明确显式指定。此时，建议您通过Deny方式，拒绝特权权限。如下示例所示。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ram:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "ram:UpdateAccessKey"
 ],
 "Resource": "*"
 }
 ]
}`
- 如果授予该特权权限的策略是系统权限策略，建议您新建自定义权限策略，在策略内容中，通过Deny方式，拒绝特权权限。然后将自定义权限策略绑定到RAM用户上。详细操作，请参考[创建自定义权限策略](https://help.aliyun.com/zh/ram/create-a-custom-policy)、[为RAM用户授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-the-ram-user)、[为RAM用户移除权限](https://help.aliyun.com/zh/ram/revoke-permissions-from-a-ram-user)。
- 如果特权操作存在最近访问时间，既该特权操作最近被调用过。您需要确认该特权权限是否符合预期。
- 如果该RAM用户存在控制台访问，那么您需要确认使用该RAM用户的企业员工，其工作职能是否确实需要该特权权限。
- 如果该RAM用户创建有AccessKey，那么您需要确认使用该AccessKey的业务场景和应用程序，是否确实需要调用该特权操作。

确认过程，需要您的运维和业务团队共同参与，进行决策。

- 如果特权操作确认需要保留，那么您可以直接将分析结果进行归档处理。
- 如果特权操作确认不再需要，建议您进行收敛。具体操作参考前文特权操作没有调用访问过的处理方式。

###### RAM角色

- 如果RAM角色是普通服务角色或者云服务保留角色，除非您明确知道该角色的使用情况，否则，不建议您进行任何修改，您可以直接将分析结果进行归档处理。您可以按照前文**前置准备-RAM角色处理路径**章节，通过归档规则将此类角色的分析结果自动归档。
- 其他类型的RAM角色（普通用户角色），处理方式请参考前文的RAM用户。您可以直接在RAM控制台或通过RAM API进行优化处理。

##### 不活跃的用户/角色

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967984.png)

在分析结果列表中，结果类型为不活跃的用户/角色，则表示该RAM用户/角色在指定的闲置访问周期内，没有任何权限访问活动。这并不一定代表该RAM身份是闲置的，您需要根据进一步确认RAM身份的使用情况，从而进行相应的处理。

针对不同的RAM身份，处理方式略有不同，详细处理操作请参考下文所述。

###### RAM用户

针对不同使用情况的RAM用户，建议您采取下文所述步骤，进行针对性的处理。

###### 1. RAM用户创建有AccessKey

1. 如果AccessKey未曾使用。此类RAM用户大概率是闲置用户，建议您及时进行清理。禁用控制台登录。您可以在RAM用户详情页，在**认证管理**页签下的**控制台登录管理**区域，单击**修改登录设置**，将控制台访问设置为禁用。详细操作，请参考[管理RAM用户登录设置](https://help.aliyun.com/zh/ram/manage-console-logon-settings-for-a-ram-user-1)。禁用AccessKey。建议您优先禁用该AccessKey，避免该AccessKey发生泄露从而导致安全风险。如果后续发现您的业务团队有使用该AccessKey的需要，您也可以在控制台上一键启用。详细操作，请参考[禁用RAM用户的AccessKey](https://help.aliyun.com/zh/ram/user-guide/disable-an-accesskey-pair-of-a-ram-user)。在观察一段时间，确认AccessKey无需使用后，建议您删除AccessKey，并进一步删除该RAM用户。详细操作，请参考[删除RAM用户的AccessKey](https://help.aliyun.com/zh/ram/user-guide/delete-an-accesskey-pair-of-a-ram-user)、[删除RAM用户](https://help.aliyun.com/zh/ram/user-guide/delete-a-ram-user)。
2. 否则（AccessKey使用过），建议您按如下步骤进行权限收敛。禁用控制台登录。您可以在RAM用户详情页，在**认证管理**页签下的**控制台登录管理**区域，单击**修改登录设置**，将控制台访问设置为禁用。详细操作，请参考[管理RAM用户登录设置](https://help.aliyun.com/zh/ram/manage-console-logon-settings-for-a-ram-user-1)。收敛闲置权限。阿里云提供了权限审计功能可以帮助您识别RAM身份所拥有的权限，以及权限的最近访问时间。需要注意的是权限审计的访问跟踪期于2024-02-01开始，如果AccessKey最后使用时间早于2024-02-01，那么在权限审计中将不会有记录。因此，无论在权限审计中，该RAM用户是否有权限访问活动，您的运维团队和业务团队都需要一起参与，确认该AccessKey在具体的业务场景中，需要使用到的操作权限，将未使用或无需使用的权限安全的删除，从而遵循RAM身份的最小授权原则。
3. 如果该RAM用户身上绑定有自定义策略，建议您直接修改该自定义策略，策略内容为收敛后的权限。同时将该RAM用户身上其他的系统策略解绑。在此过程中，您需要密切关注业务情况，如果对业务运行产生了影响，请立刻使用权限策略的版本功能进行回滚（详细操作，请参见[管理自定义权限策略版本](https://help.aliyun.com/zh/ram/manage-custom-policy-versions)）并重新将解绑的系统策略绑定回去。
4. 如果该RAM用户身上只绑定有系统策略，建议您新建自定义权限策略，策略内容为收敛后的权限，然后将自定义权限策略，授予RAM用户，同时解除系统策略。详细操作，请参考[创建自定义权限策略](https://help.aliyun.com/zh/ram/create-a-custom-policy)、[为RAM用户授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-the-ram-user)、[为RAM用户移除权限](https://help.aliyun.com/zh/ram/revoke-permissions-from-a-ram-user)。在此过程中，您需要密切关注业务情况，如果对业务运行产生了影响，请立刻在RAM用户上绑定回原来的系统权限策略。

###### 2. RAM用户未创建有AccessKey

1. RAM用户登录过控制台。建议您禁用控制台登录。您可以在RAM用户详情页，在**认证管理**页签下的**控制台登录管理**区域，单击**修改登录设置**，将控制台访问设置为禁用。详细操作，请参考[管理RAM用户登录设置](https://help.aliyun.com/zh/ram/manage-console-logon-settings-for-a-ram-user-1)。
2. RAM用户未登录过控制台。此类RAM用户大概率是闲置用户，建议您及时进行清理。禁用控制台登录。您可以在RAM用户详情页，在**认证管理**页签下的**控制台登录管理**区域，单击**修改登录设置**，将控制台访问设置为禁用。详细操作，请参考[管理RAM用户登录设置](https://help.aliyun.com/zh/ram/manage-console-logon-settings-for-a-ram-user-1)。删除RAM用户。如果确认该RAM用户未真实使用，建议您直接删除该RAM用户。详细操作，请参考[删除RAM用户](https://help.aliyun.com/zh/ram/user-guide/delete-a-ram-user)。

###### RAM角色

目前，阿里云暂时无法识别最近一次扮演RAM角色的时间，从而无法准确确定RAM角色的使用情况，因此对不活跃的RAM角色的优化，需要依赖客户的自主决策。

- 如果RAM角色是普通服务角色或者云服务保留角色，除非您明确知道该角色的使用情况，否则，不建议您进行任何修改，您可以直接将分析结果进行归档处理。您可以按照前文**前置准备-RAM角色处理路径**章节，通过归档规则将此类角色的分析结果自动归档。
- 其他类型的RAM角色（普通用户角色），处理方式请参考前文的RAM用户创建有AccessKey情况下的权限收敛方式。您可以直接在RAM控制台或通过RAM API进行优化处理。

##### 过度授权的用户/角色

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967985.png)

在分析结果列表中，结果类型为过度授权的用户/角色，则表示该RAM用户/角色在指定的闲置访问周期内，拥有未使用的服务粒度和操作粒度权限。您可以在过度授权分析器的分析结果页面，单击**前往治理**（当前账号内的资源）或**复制资源URL**（非当前账号内的资源），跳转到该RAM身份的权限审计页面。通过权限审计，确认闲置权限。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967986.png)

其中，在审计列表中，您需要关注的有：

1. 最近访问时间。如果最近访问时间为**没有访问**，则表明该RAM身份在2024-02-01后，并没有对于该云服务的权限访问活动。
2. 授予权限的策略。通过授予权限的策略信息，您可以确认该云服务的权限定义在哪个权限策略中。方便您定位并进行收敛优化。
3. 对于支持操作级别审计的云服务，您可以单击**操作**列的**查看鉴权操作**，查看该云服务下具体API的访问情况。为进一步将权限收敛到具体的API操作，提供辅助决策。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8176581571/p967979.png)

基于权限审计提供的权限访问信息，您的运维团队和业务团队需要一起参与，确认该RAM身份在具体的业务场景中，需要使用到的操作权限，将未使用或无需使用的权限安全的删除，从而遵循RAM身份的最小授权原则。

1. 首先，您可以在分析结果详情页，切换到**治理建议**页签，访问分析会根据分析结果给出治理建议，对于在闲置访问周期内，不存在权限访问的权限策略，提供一键解除授权的能力，帮助您快速收敛闲置权限（需要注意的是，只有分析结果的资源拥有者才能执行治理操作）。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7176581571/p967987.png)
2. 然后，您可以进一步将权限收敛到操作级别。如果该RAM身份上绑定有自定义策略，建议您直接修改该自定义策略，策略内容为收敛后的权限。同时将该RAM身份上其他的系统策略解绑。在此过程中，您需要密切关注业务情况，如果对业务运行产生了影响，请立刻使用权限策略的版本功能进行回滚（详细操作，请参见[管理自定义权限策略版本](https://help.aliyun.com/zh/ram/manage-custom-policy-versions)）并立刻在RAM用户上绑定回原来的系统权限策略。如果该RAM身份上只绑定有系统策略，建议您新建自定义权限策略，策略内容为收敛后的权限，然后将自定义权限策略，授予RAM身份，同时解绑系统策略。详细操作，请参考[创建自定义权限策略](https://help.aliyun.com/zh/ram/create-a-custom-policy)、[为RAM用户授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-the-ram-user)、[为RAM用户移除权限](https://help.aliyun.com/zh/ram/revoke-permissions-from-a-ram-user)、[为RAM角色授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-a-ram-role)、[为RAM角色移除权限](https://help.aliyun.com/zh/ram/remove-permissions-from-a-ram-role)。在此过程中，您需要密切关注业务情况，如果对业务运行产生了影响，请立刻在RAM身份上绑定回原来的系统权限策略。

其中对于RAM角色来说，处理方式上存在以下些许差异：

- 如果RAM角色是普通服务角色或者云服务保留角色，除非您明确知道该角色的使用情况，否则，不建议您进行任何修改，您可以直接将分析结果进行归档处理。您可以按照前文**前置准备-RAM角色处理路径**章节，通过归档规则将此类角色的分析结果自动归档。
- 其他类型的RAM角色（普通用户角色），处理方式和上文相同。您可以直接在RAM控制台或通过RAM API进行优化处理。

## 故障排除

### 为什么修改RAM角色时报错：NotSupport.AliyunReservedRole？

此类角色是云服务保留角色，该角色带有`AliyunReserved`前缀，客户需要在对应云服务中对角色进行管理操作，不允许在RAM控制台或者通过RAM API进行管理。比如云SSO的访问配置，您在云SSO中部署访问配置时，会在您相应的账号下创建一个名为`AliyunReservedSSO-<访问配置名称>`的RAM角色，该角色无法从RAM控制台进行任何修改、删除操作（包括其身上绑定的权限策略），如需修改，您需要在云SSO中，修改对应访问配置。详细信息，请参阅[访问配置概述](https://help.aliyun.com/zh/cloudsso/user-guide/overview-1)。

### 为什么对云服务访问没有成功，访问分析里依然有记录？

权限审计中的最近访问包含对云服务API的所有访问请求，而不仅是访问成功的请求。它包含通过阿里云控制台、通过CLI、SDK或直接访问API的所有尝试。权限审计中出现非预期的访问并不意味着您的账号已被泄露，因为该访问请求有可能已被拒绝。对于请求的详细信息，请查看您的操作审计日志。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-272（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
