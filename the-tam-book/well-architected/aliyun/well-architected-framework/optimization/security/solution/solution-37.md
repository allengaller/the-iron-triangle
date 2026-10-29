<!-- source: https://help.aliyun.com/zh/well-architected/solution-37 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2932663 -->

# 多账号操作日志统一归集与审计

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6476581571/p978184.png)

该方案指导企业客户在多账号的云上IT架构下，正确稳妥地归集并留存操作审计日志，确保持续稳定的归集。并提供了一套基于操作日志进行安全监控和分析的方式。方案基于[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)、[操作审计](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)、[云治理中心](https://help.aliyun.com/zh/cgc/product-overview/what-is-cloud-governance-center)、[SLS](https://help.aliyun.com/zh/sls/what-is-log-service)及[OSS](https://help.aliyun.com/zh/oss/user-guide/what-is-oss)等云产品，可以指导企业客户搭建云上审计中心。

## 方案优势

### 多账号日志中心化便捷归集

使用资源目录进行多账号管理后，操作审计能够便捷的实现多账号操作日志中心化归集，并支持长期留存审计日志，应对企业外部审计及内部监管要求。

### 审计跟踪安全有保障

企业管理账号通过管控策略限制审计跟踪不能被停止和删除，审计账号不能被移出资源目录，日志存储不能被删除，确保审计数据收集及存储始终运转正常。

### 日志分析及高危操作洞察

基于审计日志能够实现持续监控告警及安全分析，及时洞察可能存在的高危操作、非法操作等潜在风险，并支持日常故障排查。

## 客户场景

### 应对企业外审要求

#### 场景描述

企业受外部审计机构要求，必须留存180天及以上的审计日志，在企业接受评估时需能够呈现该审计日志。

#### 适用客户

需支持外部审计和监管要求的企业客户。

### 企业内部运维问题

#### 场景描述

企业面对内部的运维问题，如疑似AK泄露、异常的停机宕机、计划外的资源增删、违法员工操作盘查、故障排查、资源生命周期追溯、异地登录、异常操作、高危操作等，需要依赖审计日志进行排查和分析。

#### 适用客户

对内部运维有异常识别、安全分析及故障排查有诉求的企业客户。

## 客户案例

### 客户背景

某XX集团型公司，按业务需要为不同分公司开设相应的云账号。每个云账号内都会有用户对资源的操作并且产生操作日志。

### 客户诉求

根据中国网安法和等保2.0要求，企业必须留存180天及以上的IT系统运维访问日志。日常的故障排查、自动运维、运维监控、安全洞察都必须依赖完整可靠的审计日志。现集团信息安全团队需要做统一的日志审计，客户需求如下：

- 站在集团信息安全团队，希望能够查看每个分公司内的账号操作日志。
- 将云上的审计日志拉到IDC进行二次清洗分析。

### 实施方案

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6476581571/p978183.png)

实施架构示意图见上方图片。实施说明：

- 在企业管理账号中使用资源目录进行多账号管理，一次操作审计配置，全部账号生效。
- 云上每个账号内的操作行为日志保留180天。
- 启用强制日志投递。
- 审计日志投递到OSS后，将离线日志拉取到自建IDC进行分析。

### 客户收益

- 云上每个账号内的操作日志行为均进行存档，满足等保2.0要求。
- 集团运维人员能够在统一的日志中心查看各分公司云账号的操作日志。

## 方案架构

在企业管理账号中使用资源目录进行多账号管理，并进行操作审计配置，能够统一收集所有账号操作日志。操作审计支持投递日志到SLS及OSS进行存储，SLS及OSS支持日志留存时间配置，满足外部审计及内部监管合规要求。操作审计支持查看事件查询及事件告警，便捷查看用户操作时间线及监控云上异常和高危操作。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6476581571/p978182.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 操作审计ActionTrail | [操作审计（ActionTrail）](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)帮助您监控并记录阿里云账号的活动，包括通过阿里云控制台、OpenAPI、开发者工具对云上产品和服务的访问和使用行为。您可以将这些行为事件下载或保存到日志服务或OSS存储空间，然后进行行为分析、安全分析、资源变更行为追踪和行为合规性审计等操作。 | 开通免费，详情参见[产品计费](https://help.aliyun.com/zh/actiontrail/product-overview/billing/)。 |
| 云治理中心 | [云治理中心](https://help.aliyun.com/zh/cgc/product-overview/what-is-cloud-governance-center)是企业在阿里云上进行多账号集中IT治理的平台。通过步骤式向导和自动化流程帮助企业快速搭建Landing Zone，建立安全合规的多账号环境，并对企业在云上的多账号环境进行持续治理。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/cgc/product-overview/billing/)。 |
| 日志服务SLS | [日志服务SLS](https://help.aliyun.com/zh/sls/what-is-log-service)是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/sls/billing/)。 |
| 对象存储服务OSS | [对象存储OSS（Object Storage Service）](https://help.aliyun.com/zh/oss/user-guide/what-is-oss)是阿里云提供的海量、安全、低成本、高持久的云存储服务。OSS适合存放任意类型的文件，容量和处理能力弹性扩展，多种存储类型供选择，全面优化存储成本 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/oss/billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 日志审计账号 | 一般在资源目录的Core资源夹中建议存在一个日志审计账号，专门用于存储云上收集的各种日志，并且仅有审计管理员使用的角色拥有对该日志账号的管控权限，实现运维管控权限和审计监管权限的隔离，避免出现恶意运维之后又能删除审计日志逃避司法追责的情况。该账号仅承担审计日志收集、留存和分析的职能，账号下不保有其他计算和数据库资源，与业务账号独立。这个账号在初始化的时候可以通过[云治理中心](https://help.aliyun.com/zh/cgc/product-overview/what-is-cloud-governance-center)生成。 |

## 安全性

### 配置审计服务关联角色

为了完成配置审计的某个功能，需要获取其他云服务的访问权限而提供的RAM角色，详情参见[配置审计服务关联角色](https://help.aliyun.com/zh/document_detail/162994.html)。当您使用配置审计的自动修正功能修正不合规资源时，需要获取不合规资源的访问权限，详情参见[自动修正功能的服务关联角色](https://help.aliyun.com/zh/document_detail/193207.html)。

### OSS安全性

OSS数据安全详情参见[数据安全](https://help.aliyun.com/zh/oss/data-security-11)。

### SLS安全性

SLS安全与合规详情参见[安全与合规](https://help.aliyun.com/zh/sls/security-and-compliance)。

## 注意事项

### 主要注意事项

1. 操作审计目前正在努力覆盖阿里云的所有云产品和事件，但目前支持的产品和事件类型有限。支持多款阿里云产品的**管控事件**，管控事件一般是**运维团队**对云上IT基础设施进行管控变更时产生，如ECS实例的新增和删除等，请持续关注[支持的产品列表](https://actiontrail.console.aliyun.com/resources)。暂不支持**数据事件**。仅有部分产品有数据事件，如函数计算中触发函数调用的事件、OSS中在Bucket上传和下载文件的事件。数据事件一般是**业务团队**开发的业务应用在业务运行过程中产生，事件量巨大且重复率高。业务研发团队负责业务应用开发和运行维护，可以仅关注数据事件。运维团队负责基础设施搭建和运维，应重点关注管控事件，同时如果要监督业务应用的运行也可以关注数据事件。操作审计尚未支持的云产品的操作事件将无法被统一收集。
2. 阿里云操作审计仅会默认记录和留存90天的操作事件，企业只有按照该方案创建跟踪才能确保留存更长期的日志。
3. 方案中提到的[历史事件投递任务](https://help.aliyun.com/zh/actiontrail/user-guide/create-a-historical-event-delivery-task)目前仍处于白名单申请使用阶段，请联系您的服务经理或提交工单申请。
4. 方案中给出了部分基于操作事件的监控和分析建议，企业需要根据自身实际情况进行拓展，这些建立和示例并不确保满足每个企业的所有审计监控需求。
5. 企业需要为用于存储操作事件的SLS和OSS产品付费。企业可以视自己对日志保留天数来做组合搭建。其中SLS推荐保存日志180天，OSS可以永久保存。
6. 登录资源目录建议用RAM用户，否则无法在资源目录控制台登入进其他成员账号。
7. 操作审计默认提供90天在线查询，是免费的但功能有限，比如只能单地域查询，而且查询条件有限（主要是成本考虑）。

### 存储成本设计

客户如果对存储费用比较敏感，认为一份操作事件没有必要既投递到SLS同时又投递到OSS。那建议只投递到SLS里面，然后使用SLS的冷热分层存储方案。冷热分层存储有一个限制：日志的TTL必须在60天以上，否则无法开启，详情参见[智能冷热分层存储](https://help.aliyun.com/zh/sls/enable-hot-and-cold-tiered-storage-for-a-logstore)。

### 配置审计使用限制

配置审计使用限制详情参见[使用限制](https://help.aliyun.com/zh/document_detail/183384.html)。

### OSS使用限制

对象存储OSS的一些使用限制及性能指标详情参见[使用限制](https://help.aliyun.com/zh/oss/user-guide/limits)。

### SLS使用限制

SLS相关使用限制详情参见[使用限制](https://help.aliyun.com/zh/sls/limits-1/)。

## 实施步骤

### 实施准备

#### 确定资源目录中的日志审计账号

一般在资源目录的Core OU中建议存在一个**日志账号**，专门用于存储云上收集的各种日志，并且仅有审计管理员使用的角色拥有对该日志账号的管控权限，实现运维管控权限和审计监管权限的隔离，避免出现恶意运维之后又能删除审计日志逃避司法追责的情况。该账号仅承担审计日志收集、留存和分析的职能，账号下不保有其他计算和数据库资源，与业务账号独立。

注意：日志账号的财务模型推荐采用财务托管，由主账号或指定财务结算账号统一管理。

#### 确保日志审计账号已开通存储产品

- 确保日志审计账号中开通日志服务（SLS）和对象存储（OSS）。
- 如果企业需要永久保存操作日志需要开通OSS存储。

#### 确保资源结构已创建

本方案中相应的账号UID及用途如下：

| 账号UID | 账号用途 |
| --- | --- |
| 195121xxxx354857 | 企业管理主账号，即开通资源目录的账号。 |
| 173042xxxx627905 | 日志账号，这个账号用于审计日志收集、留存、分析的职能，与业务账号独立。 |

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：15分钟。

### 操作步骤

#### 配置审计日志投递

1. 使用企业管理账号登录[云治理中心控制台](https://governance.console.aliyun.com/)。
2. 在左侧导航栏，选择**Landing Zone > Landing Zone搭建**。
3. 选择蓝图，然后单击**搭建**。本文以标准蓝图为例。
4. 在**配置蓝图**页面的**已添加搭建项**区域，单击**操作审计统一日志投递**。如果已添加搭建项中没有目标搭建项，您可以单击**添加搭建项**，添加目标搭建项。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6476581571/p978185.png)
5. 在**账号选择**下拉列表中，选择日志投递的目标账号。默认将审计日志投递到Landing Zone搭建中创建的日志账号。
6. 打开目标投递方式的开关，然后配置投递参数。**投递方式****投递参数**投递到日志服务SLS**地域**：SLS日志空间所属的地域。**日志空间名称**：需全局唯一，建议您使用企业名作为前缀。例如：landingzone-actiontrail-xxxx。投递到对象存储OSS**地域**：OSS存储空间所属的地域。**存储空间名称**：需全局唯一，建议您使用企业名作为前缀。例如：landingzone-actiontrail-xxxx。
7. 创建完成后，在指定的**日志账号**里面能够看到创建的SLS对应的Project及OSS对应的bucket，同时在当前企业管理主账号的[操作审计控制台](https://actiontrail.console.aliyun.com/)的跟踪列表中能够看到已**开启多账号跟踪**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6476581571/p978186.png)

#### 构建分析看板

基于SLS分析操作事件，并构建分析看板。

**注意**：以下操作是在日志账号下进行的操作。

1. 登录[日志服务控制台](https://sls.console.aliyun.com/)。
2. 在**全部的Project**页签单击选择之前创建的Project，单击创建跟踪时自动生成的Logstore。
3. 然后单击**15分钟（相对）**，设置查询的时间范围。
4. 在搜索框中输入查询代码，然后单击**查询/分析**，查询事件。示例为查询指定云服务和指定事件。例如：将<TargetServiceName>和<TargetEventName>分别指定为OSS和GetBucketLocation，查询获取OSS存储空间位置的事件。`and event.serviceName: <TargetServiceName> and event.eventName: <TargetEventName>`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6476581571/p978187.png)
5. 单击**统计图表**页签，然后单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6476581571/p978188.png)图标，生成数据看板。显示OSS GetBucketLocation接口的调用频率趋势图。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6476581571/p978189.png)

更多分析示例如下：

- 示例1：查询某个角色的使用时间线，包括角色被谁扮演和扮演者在扮演期间的操作事件。`• 先查询谁扮演了角色， [角色名称] 替换成您想要分析的角色。
* and event.eventName: AssumeRole and [角色名称] | SELECT "event.userIdentity.accountId" as accountId, "event.userIdentity.type" as type, "event.userIdentity.principalId" as principalId, "event.userIdentity.username" as username, "event.resourcename" as stsAk
• 再查询一次角色扮演后，查询该扮演者都做了哪些操作, [stsAk]替换成上面查询到的stsAk。
* and event.userIdentity.accessKeyId : [stsAk] | SELECT "event.serviceName" as serviceName, "event.eventName" as eventName`
- 示例2：查询某个RAM用户的使用时间线，包括以RAM用户身份的操作事件、扮演其他角色的事件和扮演其他角色后的操作事件。`• 查询最近有访问的RAM用户。
* and event.userIdentity.type : ram-user | SELECT DISTINCT "event.userIdentity.username" as username
• 查询指定RAM用户的调用事件， [RAM用户名称]替换成您想要分析的RAM用户名称。
* and event.userIdentity.type : ram-user and event.userIdentity.username: [RAM用户名称] | SELECT "event.serviceName" as serviceName, "event.eventName" as eventName
• 查询指定RAM用户的角色扮演记录， [RAM用户名称]替换成您想要分析的RAM用户名称。
* and event.userIdentity.type : ram-user and event.userIdentity.username: [RAM用户名称] and AssumeRole | SELECT "event.resourceName" as stsAk
• 查询指定RAM用户角色扮演后，做了哪些操作，[stsAk]替换成上面查询到的stsAk。
* and event.userIdentity.accessKeyId : [stsAk] | SELECT "event.serviceName" as serviceName, "event.eventName" as eventName`
- 示例3：查询某个AK的使用时间线。`• 查询所有在调用的AK。
* and event.userIdentity.accessKeyId : * | SELECT DISTINCT "event.userIdentity.accessKeyId" as ak where "event.userIdentity.accessKeyId" not like 'STS%' and "event.userIdentity.accessKeyId" != '-'
• 查询指定AK的操作事件。
* and event.userIdentity.accessKeyId : [AK] | SELECT "event.serviceName" as serviceName, "event.eventName" as eventName`
- 示例4：查询有访问操作的IP，以及IP的操作事件统计。`• 统计所有访问的IP。
* not event.sourceIpAddress:Internal | SELECT DISTINCT "event.sourceIpAddress" as ip
• 分析访问IP的城市和调用量。
* not event.sourceIpAddress:Internal | SELECT count(1) as pv, city, ip FROM (SELECT "event.sourceIpAddress" AS ip, ip_to_city("event.sourceIpAddress") as city FROM log) GROUP BY city, ip ORDER BY pv DESC`
- 示例5：查询指定云服务的多个事件。例如：将<TargetServiceName>和<TargetEventName>分别指定为ECS、RunInstances和CreateInstance，获取创建ECS实例的操作事件。`* and event.serviceName: <TargetServiceName> and (event.eventName: <TargetEventName1> or event.eventName: <TargetEventName2> )`

## 故障排除

### 事件该投递到SLS还是OSS？

- 对象存储OSS主要用于归档事件，如果您需要对事件进行超过90天的长时间存储，而且暂时不需要查询或分析事件，建议您将事件投递到OSS。
- 日志服务SLS主要用于查询或分析事件，如果您需要对事件进行查询或分析，或者需要使用操作审计的事件高级搜索、事件告警和智能分析Insight事件等功能，建议您将事件投递到SLS。SLS收费略高于OSS，但是可以实现更多需求，因此更推荐您将事件投递到SLS。
- 关于选择存储服务的更多信息，请参见[将操作事件持续投递到指定服务](https://help.aliyun.com/zh/actiontrail/use-cases/deliver-events-to-specified-alibaba-cloud-services)。

### 如何在SLS设置SQL语句查询操作审计的事件

操作审计（ActionTrail）帮助您监控阿里云账号的活动并记录最近90天的事件。当您需要分析更长时间的事件时，可以通过操作审计创建跟踪，将事件投递到日志服务SLS，使用SQL语句对事件进行查询和分析，详情参见[如何在SLS设置SQL语句查询操作审计的事件](https://help.aliyun.com/zh/actiontrail/support/how-can-i-use-sql-statements-to-query-actiontrail-events-delivered-to-log-service)。

## 相关内容

- [云上持续审计合规最佳实践](https://bp.aliyun.com/detail/114)
- [SLS冷热分层存储](https://help.aliyun.com/zh/sls/enable-hot-and-cold-tiered-storage-for-a-logstore)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-37（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
