<!-- source: https://help.aliyun.com/zh/well-architected/solution-165 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929343 -->

# 通过SLS实现云产品日志统一归集与审计

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970912.png)

日志审计既是企业安全合规的基础，也是国内外法律法规的刚性要求。在多账号体系下，审计日志的统一采集与归档，既可以确保相关法律法规的落地，也是企业安全防护的重要一环。

本文档介绍了一种企业客户实现云上审计日志自动化的统一采集、归档和消费的方案，满足在多账号体系下，企业在云上的相关审计和安全需求。

## 方案优势

### 自动化、中心化采集日志

支持将资源目录范围内所有账号下的日志，集中采集到日志账号下。采集到的日志会存储到某个地域的中心化 SLS Project 中，方便后续查询分析、可视化与告警、二次开发等。同时一次性配置采集策略后，即可完成跨账号自动实时发现新资源（例如新创建的 RDS、SLB、OSS Bucket 实例等）并实时采集日志。

### 丰富的审计功能

日志审计服务继承了日志服务现有的所有功能，包括查询分析、加工、报表、告警、导出等功能，支持审计场景下中心化的审计等需求。同时支持与开源软件、阿里云大数据产品、第三方 SOC 软件无缝对接，充分发挥数据价值。

### 通过日志智能存储分层与冷归档降低存储成本

日志服务提供智能分层存储功能，支持按需将数据进行热存储、低频存储和归档存储。通过存储策略将审计日志自动转移为归档存储，降低存储成本，同时保证日志的查询、分析、可视化、告警、投递和加工等能力不受影响。最后将审计日志导入到对象存储 OSS 中进行冷归档存储，进一步降低持久化存储的成本。

## 客户场景

### 应对企业外审要求

#### 场景描述

企业受外部审计机构要求，必须留存180天及以上的审计日志，在企业接受评估时需能够呈现该审计日志。

#### 适用客户

- 使用资源目录管理云上多个账号的企业客户。
- 使用多个阿里云账号的企业客户。
- 存在中心运维团队、审计团队的企业客户。
- 有独立合规团队的企业客户。

### 企业内部运维问题

#### 场景描述

企业面对内部的运维问题，如疑似AK泄露、异常的停机宕机、计划外的资源增删、违法员工操作盘查、故障排查、资源生命周期追溯、异地登录、异常操作、高危操作等，需要依赖审计日志进行排查和分析。

#### 适用客户

- 使用资源目录管理云上多个账号的企业客户。
- 使用多个阿里云账号的企业客户。
- 存在中心运维团队、审计团队的企业客户。
- 有独立合规团队的企业客户。

## 方案架构

本方案基于多账号体系实现云上审计日志自动化、中心化采集。您可以在日志账号中，开启并配置日志审计服务（图中1），将资源目录范围内所有账号下的云产品审计日志，统一采集到日志账号下，采集到的日志会存储到日志账号下某个地域的中心化 SLS Project 中，基于采集到的审计日志，您可以进一步配置智能存储分层、查看审计报表、配置告警通知等。对于日志审计服务不支持的数据源，您可以通过数据加工的方式，跨账号投递到日志账号的中心化 SLS Project 中（图中2）。然后，如果您需要更长周期或者持久化的存储审计日志，可以将审计日志导出到对象存储 OSS Bucket 中，进行冷归档存储（图中3）。通过下发管控策略（图中4），确保日志审计相关的存储资源不会被误删除。最后，企业自有的审计系统就可以统一对接并消费中心化的审计日志（图中5），完成企业内部基于审计日志的相关操作。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970915.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 日志服务 | [日志服务SLS](https://help.aliyun.com/zh/sls/what-is-log-service)是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/sls/billing-overview)。 |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 访问控制RAM | [访问控制RAM（Resource Access Management）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务 | 免费。 |
| 对象存储OSS | [阿里云对象存储OSS（Object Storage Service）](https://help.aliyun.com/zh/oss/product-overview/what-is-oss)是一款海量、安全、低成本、高可靠的云存储服务 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/oss/product-overview/billing)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |
| 项目（Project） | 项目是日志服务的资源管理单元，是进行多用户隔离与访问控制的主要边界。更多信息，请参见[项目（Project）](https://help.aliyun.com/zh/sls/product-overview/project#concept-t3x-hqn-vdb)。 |
| 日志库（Logstore） | 日志库是日志服务中日志数据的采集、存储和查询单元。更多信息，请参见[日志库（Logstore）](https://help.aliyun.com/zh/sls/product-overview/logstore#concept-btb-4qn-vdb)。 |
| 地域（Region） | 地域是日志服务的数据中心所在物理位置。您可以在创建Project时指定地域，一旦指定之后就不允许更改。更多信息，请参见[开服地域](https://help.aliyun.com/zh/sls/product-overview/supported-regions#reference-2084283)。 |
| SIEM | 安全信息与事件管理系统（Security Information and Event Management），如Splunk，IBM QRadar等。 |

## 安全性

### 日志服务

阿里云日志服务具有丰富的安全防护能力，支持服务器端加密、细粒度权限管控、详细服务日志等特性，同时提供日志审计功能，针对主流云产品提供多账号下实时自动化、中心化采集云产品日志并实现审计。日志服务为您提供丰富的数据洞察能力，同时满足您企业数据的安全与合规要求。

### 创建RAM用户及授权

在实际的应用场景中，阿里云账号可能需要将日志服务的运营维护工作交予其名下的RAM用户，由RAM用户对日志服务进行日常维护工作。或者阿里云账号名下的RAM用户可能有访问日志服务资源的需求。此时，阿里云账号需要对其名下的RAM用户进行授权，授予其访问或者操作日志服务的权限。出于安全性的考虑，建议您将RAM用户的权限设置为需求范围内的最小权限。关于RAM用户的详细信息，请参见[入门概述](https://help.aliyun.com/zh/ram/introduction)。

### 管控策略

通过使用管控策略（Control Policy），限制 Application 目录下的业务成员账号等其他账号不允许删除审计日志的 SLS Project，不允许删除日志库， 不允许删除服务日志，不允许删除日志投递任务等。

## 注意事项

### 管控策略工作原理

因管控策略的工作原理和特性，在实际使用过程中，会出现以下现象：

- 无法限制成员账号的 Root 身份。在成员账号中，管控策略能够限制成员账号的 RAM 用户和 RAM 角色，如果开启了成员账号的 Root 权限并使用 Root 身份创建 ECS，则不受管控策略限制。
- 管控策略对服务关联角色不生效。当云产品使用服务关联角色进行资源操作时，不受管控策略限制。

其他特性请参见[管控策略工作原理](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)。

## 自动化模板

### 模板介绍

基于 SLS 日志审计服务，在多账号体系下，实现云产品审计日志的自动化中心化采集、分析与归档。本方案提供了基于 Terraform 的自动化模板，模板代码结构如下所示。

```
├── step1-create-log-audit-application    // 开启 SLS 日志审计
├── step2-delivery-to-central-logarchive  // 跨账号将其他数据源日志投递到中心日志库
├── step3-cold-archive-to-oss             // 日志冷归档到 OSS
└── step4-add-control-policy              // 设置管控策略
```

### 模板地址

模板地址详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-log-audit-using-sls)。

## 实施步骤

### 实施准备

- 确保已在「企业管理主账号」中开启了管控策略功能，请参考资源目录[开启管控策略功能](https://help.aliyun.com/zh/resource-management/user-guide/enable-the-control-policy-feature)。
- 如果需要完成跨账号数据流转，确保已创建并获取源Logstore名称及Project名称。具体操作，请参见[管理Logstore](https://help.aliyun.com/zh/sls/user-guide/manage-a-logstore#concept-xkb-zh5-vdb)和[管理Project](https://help.aliyun.com/zh/sls/user-guide/manage-a-project#concept-mxk-414-vdb)。
- 如果需要完成跨账号数据流转，确保已创建RAM用户，并授予RAM用户数据加工操作权限。具体操作，请参见[授予RAM用户数据加工操作权限](https://help.aliyun.com/zh/sls/user-guide/authorize-a-ram-user-to-manage-a-data-transformation-job#task-2005445)。
- 如果需要将日志投递到OSS，确保已在日志服务Project所在的地域创建Bucket。具体操作，请参见[控制台创建存储空间](https://help.aliyun.com/zh/oss/getting-started/create-buckets-6)。注意，日志服务投递数据到OSS为同地域投递，即日志服务Project所在的地域和OSS Bucket所在地域相同。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 委派管理员

使用 RD master 账号，登录到**资源管理**控制台，进入**可信服务**页面，点击**日志审计服务**栏的**管理**，将日志账号/安全账号**添加**为委派管理员。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970904.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970916.png)

#### 开启日志审计服务

##### 首次配置

1. 登录上述设置为委派管理员的账号，进入[日志服务控制台](https://sls.console.aliyun.com/)。
2. 在**日志应用**区域的**审计与安全**页签下，单击**日志审计服务**。
3. 根据页面提示完成授权。完成授权后，日志审计服务将使用服务关联角色AliyunServiceRoleForSLSAudit进行云产品的日志采集。更多信息，请参见[管理服务关联角色AliyunServiceRoleForSLSAudit](https://help.aliyun.com/zh/sls/manage-the-aliyunserviceroleforslsaudit-service-linked-role)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970905.png)

##### 开启日志采集功能

1. 在日志审计服务的左侧导航栏中，选择**云产品接入 > 全局配置**。
2. 在**中心项目Project所在区域**下拉列表中，选择日志中心化存储的目标地域。中国：华北1（青岛）、华北2（北京）、华北5（呼和浩特）、华东1（杭州）、华东2（上海）、华南1（深圳）、中国（香港）海外：新加坡、日本（东京）、德国（法兰克福）、印度尼西亚（雅加达）
3. 在云产品列表中，选择需开启日志采集功能的云产品，并配置存储时间。如果是SLB 7层访问日志、ALB 7层访问日志、OSS访问日志、PolarDB-X 1.0审计日志、VPC流日志和内网DNS日志，还可以选择**同步到中心**。开启**同步到中心**后，区域化Project将作为中转，控制台会自动将区域化的存储时间调整成推荐的时间。
4. 单击**保存**。配置完成后，等待1分钟左右，可在**云产品接入 > 接入状态**页面中查看日志接入状态。如果出现异常，请根据页面提示信息进行调整。更多信息，请参见[开启日志采集功能](https://help.aliyun.com/zh/sls/user-guide/enable-log-collection-1#section-7az-6wh-x2p)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970906.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970911.png)

##### 开启多账号

日志审计服务支持跨账号采集云产品日志（除K8s相关日志外）到当前账号下的Logstore中。本方案采用**资源目录管理模式**配置多账号采集。

1. 在**日志审计服务**左侧导航栏中，选择**多账号配置 > 全局配置**。
2. 在**资源目录管理模式**页签中，单击**修改**。
3. 在**添加账号**面板中，选择目标账号，然后单击**确认**。资源目录管理模式支持全员方式和自定义方式。全员：日志审计服务自动将资源目录下的所有成员纳入到采集名单中，并采集这些成员中已开启日志采集功能的云产品的日志。自定义：您可以自定义选择目标成员到采集名单中，日志审计服务会采集这些成员中已开启日志采集功能的云产品的日志。
4. 配置完成后，等待2分钟左右，可在**云产品接入 > 接入状态**页面中查看日志接入状态。如果出现异常，请根据页面提示信息进行调整。更多信息，请参见[开启日志采集功能](https://help.aliyun.com/zh/sls/user-guide/enable-log-collection-1#section-7az-6wh-x2p)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970921.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970923.png)

##### 查看审计报表

在完成上述步骤后，接下来介绍日志审计服务在采集到日志后的审计操作。

1. 在**日志审计服务**左侧导航栏中，单击**审计报表**。
2. 单击目标报表，进入**审计中心**。您可以在审计中心查看数据报表，仪表盘操作请参见[仪表盘](https://help.aliyun.com/zh/sls/user-guide/overview-of-visualization#concept-tnt-lgj-kgb)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970924.png)

##### 使用审计查询

1. 在左侧导航栏中，单击**审计查询**。
2. 单击目标云产品，进入查询与分析页面。具体的查询、分析操作请参见[查询与分析](https://help.aliyun.com/zh/sls/user-guide/log-search-overview#concept-wjl-x3q-zdb)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970925.png)

##### 配置审计告警

日志审计服务已内置告警规则，您开启对应的告警实例即可实时监控日志审计服务。接下来介绍设置告警的相关操作。

1. 在**日志审计服务**左侧导航栏中，选择**审计告警 > 用户管理 > 用户管理**。
2. 创建用户，单击**创建**。
3. 在**添加用户**对话框中，配置如下参数，单击**确认**。参数描述标识符用户唯一标识，不可重复。姓名用户姓名。手机号用户手机号。国家号-手机号码格式，例如86-1381111*****。打开**可收短信**开关，表示允许日志服务按告警相关配置通过短信通知用户。打开**可接电话**开关，表示允许日志服务按告警相关配置通过语音电话通知用户。邮箱用户邮箱地址。单击**添加**可以配置多个邮箱地址。启用打开**启用**开关，表示允许日志服务给该用户发送告警通知。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970926.png)
4. 在左侧导航栏中，选择**审计告警 > 用户管理 > 用户组管理**。
5. 在用户组列表中，单击**SLS审计内置用户组**对应的**修改**。
6. 在**修改用户组**中，将已创建的用户从**待添加成员**区域添加到**已添加成员**区域，然后单击**确认**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970927.png)
7. 在左侧导航栏中，选择**审计告警 > 规则配置 > 告警规则**。
8. 在告警规则列表中，找到目标告警规则，单击**开启**。开启告警实例后，日志服务开始实时监控日志审计服务。如果您需要开启多个告警实例，可单击**添加**。告警规则的参数说明请见[告警规则总览](https://help.aliyun.com/zh/sls/user-guide/overview-26?spm=a2c4g.11186623.0.i70#concept-2023815)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970929.png)

如果您希望根据实际场景自定义告警资源，您可以自行[创建内容模板](https://help.aliyun.com/zh/sls/user-guide/create-an-alert-template#task-2045388)以及[创建行动策略](https://help.aliyun.com/zh/sls/user-guide/create-an-action-policy#task-2045212)。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970928.png)

如果您要使用自定义的行动策略，则在创建行动策略后，需在告警策略页面，修改SLS审计内置告警策略的所绑定的行动策略。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970930.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970932.png)

#### 跨账号数据流转

对于SLS还未接入的云产品，即无法自动采集多账号的此云产品日志到目标账号下的中心项目的日志库中，您可以通过数据加工完成跨账号的日志数据流转。接下来为您介绍使用自定义角色的方式完成跨账号的日志数据流转。

##### 前提条件

- 已创建并获取源Logstore名称及Project名称。具体操作，请参见[管理Logstore](https://help.aliyun.com/zh/sls/user-guide/manage-a-logstore#concept-xkb-zh5-vdb)和[管理Project](https://help.aliyun.com/zh/sls/user-guide/manage-a-project#concept-mxk-414-vdb)。
- 已创建RAM用户，并授予RAM用户数据加工操作权限。具体操作，请参见[授予RAM用户数据加工操作权限](https://help.aliyun.com/zh/sls/user-guide/authorize-a-ram-user-to-manage-a-data-transformation-job#task-2005445)。

如下图所示，希望将阿里云账号1（日志源账号）的日志数据流转到阿里云账号2（目标账号）的Logstore中。跨账号场景下，使用RAM用户创建数据加工任务，角色A需要具有源Logstore的读数据权限，角色B需要具有目标Logstore的写权限。因为数据加工任务运行于阿里云账号1之下，您需要修改阿里云账号2下角色B的信任策略对阿里云账号1进行授信。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970931.png)

##### 创建目标Logstore

本步骤将基于上述[开启日志审计](#DIN99)步骤所创建的SLS Project，在其中创建一个用于接受**源Logstore**数据的**目标Logstore**，如果您已经创建好了目标Logstore，可跳过此步骤。

1. 使用目标账号RAM用户登录[日志服务控制台](https://sls.console.aliyun.com/)。
2. 在**Project列表**中点击日志审计创建的Project![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970933.png)
3. 在**日志存储 > 日志库**页签中，单击**+**图标。
4. 在**创建Logstore**页面中，填入**基础信息**和**Logstore属性**，点击**确认**完成创建。有关参数的详细信息，请参见[创建Logstore](https://help.aliyun.com/zh/sls/user-guide/manage-a-logstore#section-v52-2jx-ndb)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970935.png)

##### 使用源账号创建角色A

1. 使用您的源账号登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 创建角色，选择可信实体类型为**阿里云服务**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970934.png)
3. 角色类型选择**普通服务角色**，输入角色名称，例如role-A，选择授信服务为**日志服务**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970940.png)

##### 赋予角色A读数据权限

改权限策略用于读取源Logstore中的数据。

1. 使用您的源账号登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 选择权限策略菜单，点击**创建权限策略**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970942.png)
3. 通过**脚本编辑**模式，将配置框中的原有脚本替换为如下内容。注意请根据实际情况替换内容中的`${源Project名称}`和`${源Logstore名称}`。`{
 "Version": "1",
 "Statement": [
 {
 "Action": [
 "log:ListShards",
 "log:GetCursorOrData",
 "log:GetConsumerGroupCheckPoint",
 "log:UpdateConsumerGroup",
 "log:ConsumerGroupHeartBeat",
 "log:ConsumerGroupUpdateCheckPoint",
 "log:ListConsumerGroup",
 "log:CreateConsumerGroup"
 ],
 "Resource": [
 "acs:log:*:*:project/${源Project名称}/logstore/${源Logstore名称}",
 "acs:log:*:*:project/${源Project名称}/logstore/${源Logstore名称}/*"
 ],
 "Effect": "Allow"
 }
 ]
}`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970936.png)
4. 点击**继续编辑基本信息**，输入自定义权限策略名称。例如ori_read。点击**确定**完成创建
5. 创建完成后，在角色页面，找到上述步骤创建的角色，点击**新建授权**按钮![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970937.png)
6. **授权范围**选择**整个云账号**。权限在当前阿里云账号内生效。**授权主体**选择**role-A**。即您在上述步骤中创建的角色。**自定义策略**选择**ori_read**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970943.png)
7. 完成创建后，在该角色的基本信息中获取RAM角色标识（ARN）。例如acs:ram::1379******44:role/role-a![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970938.png)

##### 使用目标账号创建角色B

1. 使用目标账号登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 创建角色B。具体操作请参见[创建角色A](#pGtwT)，其中关键参数配置如下：关键参数说明选择可信实体类型选择**阿里云服务**。角色类型选择**普通服务角色**。角色名称输入角色名称，例如role-B。选择授信服务选择**日志服务**。

##### 赋予角色B写数据权限

1. 使用目标账号登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 通过脚本编辑模式，创建自定义权限策略。该权限策略用于将数据加工结果写入到目标Logstore。具体操作，请参见[赋予角色A读数据权限](#xwZJI)。其中关键参数配置如下：关键参数说明名称输入自定义权限策略名称。例如**tar-write**。策略内容将配置框中的原有脚本替换为如下内容。注意请根据实际情况替换内容中的`${目标Project名称}`和`${目标Logstore名称}`。`{
 "Version": "1",
 "Statement": [
 {
 "Action": [
 "log:Post*",
 "log:BatchPost*"
 ],
 "Resource": "acs:log:*:*:project/${目标Project名称}/logstore/${目标Logstore名称}",
 "Effect": "Allow"
 }
 ]
}`
3. 为角色B授予目标Logstore写权限。其中关键参数配置如下：关键参数说明授权范围选择**整个云账号**。权限在当前阿里云账号内生效。授权主体选择**role-B**。即您在上述步骤中创建的角色。自定义策略选择**tar-write**。即您在上述步骤中创建的策略。
4. 获取RAM角色标识（ARN）。在该角色B的**基本信息**中查看，例如acs:ram::1440******32:role/role-b。

##### 使用目标账号通过角色B向源账号授信

该策略使得源账号有权限通过日志服务获取临时Token来操作目标账号的资源。

1. 使用目标账号登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 在左侧导航栏中，选择**身份管理 > 角色**。
3. 在RAM角色列表中，单击目标RAM角色，例如role-B。
4. 在**信任策略**页签中，单击**编辑信任策略**。
5. 在**Service**配置项中添加源账号的ID。或将配置框中的原有脚本替换为如下内容。注意请根据实际情况替换内容中的`${源账号ID}`。`{
 "Statement": [
 {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "log.aliyuncs.com",
 "${源账号ID}@log.aliyuncs.com"
 ]
 }
 }
 ],
 "Version": "1"
}`
6. 点击保存信任策略完成授信。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970944.png)

##### 创建数据加工任务

1. 使用目标账号的RAM用户登录[日志服务控制台](https://sls.console.aliyun.com/)。请确保该用户有数据加工操作权限。具体操作，请参见[授予RAM用户数据加工操作权限](https://help.aliyun.com/zh/sls/user-guide/authorize-a-ram-user-to-manage-a-data-transformation-job#task-2005445)。
2. 进入数据加工页面。在Project列表区域，单击源Project。在**日志存储 > 日志库**页签中，单击源Logstore。在查询和分析页面，单击**数据加工**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970939.png)
3. 在页面右上角，选择数据的时间范围。请确保在**原始日志**页签中有日志数据。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970945.png)
4. 在编辑框中，输入数据加工语句。加工语句的语法请参见[数据加工语法](https://help.aliyun.com/zh/sls/user-guide/language-introduction#concept-1130584)。
5. 预览数据。单击**快速**。日志服务支持快速预览和高级预览。更多信息，请参见[预览调试概述](https://help.aliyun.com/zh/sls/user-guide/preview-mode-overview#task-2565077)。单击**预览数据**。查看预览结果。如果加工语句错误或者权限配置错误，导致数据加工失败，请根据页面提示处理。如果确认数据加工结果无误，请执行步骤下一步。
6. 创建数据加工任务。单击**保存数据加工**。在**创建数据加工任务**面板中，配置相关参数，然后单击**确定**。其中，其他参数配置请参考[数据加工快速入门](https://help.aliyun.com/zh/sls/user-guide/quick-start#task-2316153)。该场景中关键参数配置如下：关键参数说明授权方式选择**自定义角色**。角色ARN输入角色A的ARN。即您在上述步骤中创建的角色。例如acs:ram::1379******44:role/role-a。存储目标的授权方式选择**自定义角色**。角色ARN输入角色B的ARN。即您在上述步骤中创建的角色。例如acs:ram::1440******32:role/role-b。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970941.png)
7. 查看数据加工任务在左侧导航栏中，选择**任务管理 > 数据加工**。在加工任务列表中，单击目标加工任务。在**数据加工概览**页面，查看加工任务详情。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970948.png)

##### 查看目标日志库

1. 使用目标账号RAM用户登录[日志服务控制台](https://sls.console.aliyun.com/)。
2. 在Project列表区域，单击目标Project。
3. 若提示未开启日志库索引，点击页面右上角的**开启索引**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970946.png)
4. 可以选择点击自动生成索引![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970947.png)
5. 添加完所有后，等待一分钟左右，查看目标日志库，已经存在数据，说明数据完成跨账号流转![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970950.png)

#### 数据归档

日志服务提供智能分层存储功能，降低您长周期存储的成本，并同时保证日志的查询、分析、可视化、告警、投递和加工等能力不受影响。分层存储数据的存储费用按照存储空间计费，数据转换不会产生费用。

##### 开启智能存储分层

1. 登录[日志服务控制台](https://sls.console.aliyun.com/)。
2. 在Project列表区域，单击目标Project。
3. 在**日志存储 > 日志库**页签中，单击目标Logstore对应的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970949.png)图标，然后单击**修改**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970951.png)
4. 在**Logstore属性**页面，单击**修改**。
5. 开启**智能存储分层**。开启智能存储分层功能的相关参数如下图所示，图中配置表示日志一共保存365天，热存储数据保存7天后转为低频存储，低频存储数据保存30天后转为归档存储，归档存储保存328天后自动删除日志。有关热存储、低频存储、和归档存储的详细说明，请参见[存储类型](https://help.aliyun.com/zh/sls/user-guide/data-tiered-storage-overview)，其他参数说明请参见[创建Logstore](https://help.aliyun.com/zh/sls/user-guide/manage-a-logstore#section-v52-2jx-ndb)，有关计费请参见[计费中心说明](https://www.aliyun.com/price/product?spm=5176.2020520112.0.0.7c7d34c0Uuf2vr#/sls/detail)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970952.png)
6. 单击**保存**完成配置更新。

##### 冷归档到OSS

日志服务提供投递功能，支持通过控制台将数据实时投递至OSS。您可以将日志投递到冷归档类型的 OSS Bucket 中，便于您长期存储数据。启用数据投递后，日志服务将定时将采集到的数据投递至对应的云产品。下面介绍如何创建OSS投递任务。

前提条件：

- 已在日志服务Project所在的地域创建Bucket。具体操作，请参见[控制台创建存储空间](https://help.aliyun.com/zh/oss/getting-started/create-buckets-6)。注意，日志服务投递数据到OSS为同地域投递，即日志服务Project所在的地域和OSS Bucket所在地域相同。
- 建议您创建存储类型为**冷归档存储**的 Bucket，降低存储成本。注意，冷归档存储类型只支持本地冗余存储。

操作步骤：

1. 登录[日志服务控制台](https://sls.console.aliyun.com/?spm=a2c4g.11186623.0.0.41fd2b4cw6uQQc)。
2. 在Project列表区域，单击目标Project。
3. 在**日志存储 > 日志库**页签中，单击目标Logstore左侧的**>**，选择**数据处理 > 导出 > OSS（对象存储）**。
4. 将鼠标悬浮**OSS（对象存储）**上，单击**+**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970954.png)
5. 在**OSS投递功能**面板，配置如下参数，授予OSS投递任务将数据写入到OSS Bucket的权限和读取Logstore数据的权限。可以使用默认角色，单击**授权**按钮。授权完成后单击**刷新**按钮，然后单击**确定**。重要参数配置说明如下所示。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970955.png)
6. OSS投递任务创建完成后，可以在**任务管理 > 数据投递**页签中查询投递任务的运行状况，找到目标投递任务，可以进行任务配置变更和停止等操作。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970953.png)

#### 配置管控策略

您可以通过资源目录下发管控策略，限制其他账号不允许删除审计日志的 SLS Project，不允许删除日志库， 不允许删除服务日志，不允许删除日志投递任务。

1. 使用Master账号登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)。
2. 在左侧导航栏，选择**资源目录 > 管控策略**。
3. 在**策略列表**页签，单击**创建策略**。
4. 在**创建策略**页面，单击**脚本编辑**页签。
5. 输入如下管控策略内容，然后单击**继续编辑基本信息**。注意请根据实际情况替换内容中的`${日志账号ID}`，`${Project名称}`，`${日志任务ID}`，`${Bucket名称}`。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "log:DeleteProject",
 "log:DeleteLogStore"
 ],
 "Resource": [
 "acs:log:*:${日志账号ID}:project/${Project名称}",
 "acs:log:*:${日志账号ID}:project/${Project名称}/*",
 "acs:log:*:${日志账号ID}:project/${Project名称}/logstore/*"
 ]
 },
 {
 "Effect": "Deny",
 "Action": "log:DeleteJob",
 "Resource": [
 "acs:log:*:${日志账号ID}:project/${Project名称}/job/${日志任务ID}"
 ]
 },
 {
 "Effect": "Deny",
 "Action": "oss:DeleteBucket",
 "Resource": "acs:oss:oss-*:${日志账号ID}:${Bucket名称}"
 }
 ]
 }`
6. 输入管控策略**名称**和**备注**，单击**确定**。

创建成功后，您可以为资源夹或成员绑定自定义管控策略。绑定成功后，资源夹或成员将会立即受到管控策略的管控。

1. 登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)。
2. 在左侧导航栏，选择**资源目录 > 管控策略**。
3. 在**策略绑定**页签下的左侧组织结构树中，单击目标资源夹或成员。
4. 在右侧页面，单击**绑定策略**。
5. 在**绑定策略**对话框，选择上述步骤创建的管控策略。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576581571/p970956.png)
6. 单击**确定**。

#### 消费日志

日志服务支持将日志投递到SIEM，以确保阿里云上的所有法规、审计与其他相关日志能够导入到您的安全运维中心（SOC）中。推荐使用日志服务消费组构建程序实现实时消费，然后通过**HTTPS**或者**Syslog**来发送日志给SIEM。

- HTTPS投递方式请参考[通过HTTPS投递日志到SIEM](https://help.aliyun.com/zh/sls/user-guide/ship-logs-to-a-siem-system-over-https#concept-265988)。
- Syslog投递方式请参考[通过Syslog投递日志到SIEM](https://help.aliyun.com/zh/sls/user-guide/ship-logs-to-a-siem-system-over-syslog#concept-266003)。

## 故障排除

### 为什么无法开通资源目录？

可能有如下两个原因：

- 当前账号没有进行企业实名认证。关于企业实名认证，请参见[企业实名认证](https://help.aliyun.com/zh/account/verify-your-identity-enterprise-account/)。
- 当前账号已经在资源目录内，无法重复开通。

### 什么样的账号不适合作为资源目录的管理账号？

- 账号下有待处理的邀请。建议：先处理邀请后再开通资源目录。
- 账号下已经有云资源部署了业务或应用。建议：由于管理账号将承载整个资源目录的架构管理、用户权限管控以及所有资源的付款结算等高权限操作，为了确保管理账号的安全，建议您创建一个新的阿里云账号作为管理账号，避免将已有用途的阿里云账号作为管理账号。

### 为什么管控策略没有生效？

可能有如下原因：

- 管控策略中填写的镜像ID和 Golden Image 的镜像ID不匹配。
- 管控策略绑定的资源夹不正确。
- 没有使用 RAM 用户或 RAM 角色登入成员账号。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-165（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
