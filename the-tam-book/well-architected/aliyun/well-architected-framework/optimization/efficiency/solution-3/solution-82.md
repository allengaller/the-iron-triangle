<!-- source: https://help.aliyun.com/zh/well-architected/solution-82 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929400 -->

# 企业多账号场景下订阅特定资源配置变更

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0886581571/p971635.png)

当企业有多个云账号，不同账号内会有许多不同的云资源。企业内部安全合规团队如果想重点关注某些特定规则的资源变更情况。比如只关注特定全名规则的RAM角色是否发生了修改，并且希望把这份修改事件投递到企业内部的管理系统用于后续审计分析。

本文档介绍了一种通过配置审计（Config）结合事件总线（EventBridge）和函数计算为企业提供一种实现方案，文中会以特定的一个场景来演示操作步骤。客户可以参考相关配置来适配自身的业务需求。

## 方案优势

### 集中式配置

通过资源目录和配置审计集成的能力，可以完成多账号资源的集中配置。

### 灵活配置过滤规则

基于云原生产品能力，客户无需额外做过多的代码开发，即可实现对不同账号内资源的灵活过滤。相比于自定义处理配置审计投递到消息系统程序来讲，这种方式维护成本更低。

### 可扩展处理变更事件

使用函数计算处理事件总线中的变更事件，客户可以自行修改函数计算中的程序逻辑，实现可扩展。

## 客户场景

### 订阅特定资源变更事件

#### 场景描述

企业内部的安全合规要求，对特定资源变更需要重点关注，将事件投递到内部系统，并形成事件审计分析。

#### 适用客户

- 使用资源目录管理云上多个账号的企业客户。
- 对资源变更比较关注的企业客户。
- 存在中心运维团队、审计团队的企业客户。

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0886581571/p971623.png)

架构说明

- 通过资源目录将企业多个云账号统一纳管，建立账号树。
- 通过Config委派管理员的方式，开通多账号的配置审计。
- 在单个成员账号中配置事件总线，选择事件投递目标为“日志账号”，事件模式选择特定的过滤规则。
- 在“日志账号”内配置事件总线，将对应的事件投递到函数计算；函数计算解析相应的事件对象，并保存入库。
- 在本方案中提供函数计算里面的代码为Python3.X。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 配置审计Config | [配置审计](https://help.aliyun.com/product/127306.html)（CloudConfig）是阿里云上的配置管理和IT治理服务。将您分散在各地域的资源整合为全局资源列表，您可以便捷地搜索全局资源。同时帮助您记录云上IT资源的配置变更历史，允许您将全量资源配置和配置历史文件持续收集到指定的存储空间。同时持续自动地评估云上资源配置的合规性，实现云上IT合规治理。 | 配置审计公测期间所有阿里云有效账号均可免费使用。但具体涉及到其他服务，详情计费[参考链接](https://help.aliyun.com/zh/document_detail/133951.html) |
| 事件总线EventBridge | 事件总线EventBridge是阿里云提供的一款无服务器事件总线服务，能够以标准化的CloudEvents 1.0协议在应用之间路由事件，帮助您轻松构建松耦合、分布式的事件驱动架构。 | 公测期间产品免费。 |
| 函数计算 | 阿里云函数计算是事件驱动的全托管计算服务。通过函数计算，您无需管理服务器等基础设施，只需编写代码并上传。函数计算会为您准备好计算资源，以弹性、可靠的方式运行您的代码，并提供日志查询、性能监控、报警等功能。 | 收费，详情参见[计费概述](https://help.aliyun.com/zh/functioncompute/billing-overview-of-fc)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| CloudEvents 1.0 | 用标准方式描述事件数据的开源规范，旨在简化事件声明以及跨服务、跨平台的消息投递。 |
| 事件模式 | 对事件进行过滤的模块。事件模式支持对CloudEvents包含data在内的所有字段进行过滤。 |
| 事件目标 | 事件的处理终端，负责消费事件。 |

## 安全性

### 跨账号路由事件

同组织或关联组织下不同的阿里云账号通常需要进行事件互通，事件总线EventBridge提供跨账号路由事件的能力，您可以将多个账号的事件路由到一个账号中统一处理。授权说明及操作详情参见[跨账号路由事件](https://help.aliyun.com/zh/eventbridge/use-cases/route-events-across-alibaba-cloud-accounts)。

### 成员账号配置事件总线权限

事件总线EventBridge的权限管理是通过阿里云的访问控制RAM（Resource Access Management）产品实现的。使用RAM可以让您避免与其他用户共享云账号密钥，即AccessKey（包含AccessKey ID和AccessKey Secret），按需为用户分配最小权限。此方案中授权配置如下：

| 权限策略名称 | 说明 |
| --- | --- |
| AliyunEventBridgeFullAccess | 事件总线EventBridge的管理权限，等同于阿里云账号的权限，被授予该权限的RAM用户可执行发布事件和控制台所有操作。 |

### 日志账号操作权限

日志账号里面需要配置事件总线、函数计算。参照按需为用户分配最小权限。此方案中授权配置如下：

| 权限策略名称 | 说明 |
| --- | --- |
| AliyunEventBridgeFullAccess | 事件总线EventBridge的管理权限，等同于阿里云账号的权限，被授予该权限的RAM用户可执行发布事件和控制台所有操作。 |
| AliyunFcDefaultRole | 用于FC服务角色的授权策略。 |

### 代码中的敏感数据

本方案中用到了RDS数据库，对于数据库连接所需要用到的账号、密码等敏感数据建议不要硬编码在代码中。而是推荐放在函数计算的环境变量里面。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0886581571/p971624.png)

## 注意事项

### 支持配置审计的云服务

阿里云配置审计服务已支持一系列核心基础设施，例如：云服务器ECS、 云数据库RDS、对象存储OSS、专有网络VPC、负载均衡和容器服务Kubernetes版等。在此基础上，配置审计也在不断扩展对其他云服务的支持。更多信息，请参见[支持配置审计的云服务](https://help.aliyun.com/zh/document_detail/127411.html)。

### 变更事件时延

用户修改特定的云资源，到事件触发到函数计算进行处理。这个过程时延大概在5~8分钟。

## 实施步骤

### 实施准备

- 确保已在「企业管理账号」中开通资源目录，并且将其他账号邀请到资源目录中。具体操作，请参见[Landing Zone搭建概述](https://help.aliyun.com/zh/cgc/user-guide/build-a-landing-zone-1)。
- 确保已在「企业管理账号」中开启多账号的配置审计功能。具体操作，请参见[云治理中心-统一配置防护规则](https://help.aliyun.com/zh/cgc/user-guide/configure-protection-rules-in-a-centralized-manner)。
- 确保在各个成员账号中开通事件总线。具体操作，请参见[开通事件总线](https://help.aliyun.com/product/161886.html)。
- 确保在「日志账号」中开通事件总线及函数计算、开通日志服务、配置相应的VPC网络及安全组用于配置数据库及函数计算资源。创建相应的数据库，相应的数据表及授权。具体操作，请参见[开通事件总线](https://help.aliyun.com/product/161886.html)。

### 实施场景

某客户多账号架构如下：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0886581571/p971625.png)

在业务账号B里面有如下几个Ram角色：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0886581571/p971626.png)

客户只关注以sg前缀的Ram角色对应的变更（包括修改、创建、删除），其他角色的变更不需要订阅。相关角色修改触发的变更事件在数据库中记录，如下图所示：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0886581571/p971627.png)

### 数据规划

本文以订阅特定规则RAM角色变更事件，为您介绍通过配置审计结合事件总线，函数计算实现过滤特定规则的变更事件。相关数据规划如下表：

| 云服务 | 参数 | 示例 |
| --- | --- | --- |
| 配置审计 | 账号组 | configgroup |
| 事件总线 | 规则名称 | eb-filter-ram-role |
| 函数计算 | 服务 | eb_event_action |
| 服务的系统模板权限 | AliyunFCDefaultRolePolicy |  |
| 函数 | eb_event_trigger |  |
| 触发器 | ConfigurationItemChangeTrigger |  |

注意：由于配置审计部署在华东2（上海），为了减少网络损耗，建议事件总线及函数计算选择华东2（上海）。

### 操作流程

通过配置审计将账号内资源变更事件投递到事件总线，触发函数计算完成对事件内容处理过滤，并完成数据入库完整的操作流程如下图所示：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0886581571/p971628.png)

### 操作步骤

本操作步骤中提到的账号均以上面「某客户多账号架构」为指引。

1. 登录日志账号A,新建一个RAM角色支持事件总线跨账号路由。角色名称：b-account-eb-role具体操作，请参见 [跨云账号路由事件](https://help.aliyun.com/zh/eventbridge/use-cases/route-events-across-alibaba-cloud-accounts)。
2. 登录业务账号B,配置事件总线：登录[事件总线控制台](https://eventbridge.console.aliyun.com/cn-hangzhou/event-buses)。在左侧导航栏，单击事件总线。在顶部菜单栏，选择地域，例如：华东2（上海）。选择 default 进入这个默认事件配置页。在 事件规则 页面，单击 创建规则。在**创建规则**页面，完成以下操作。在**配置基本信息**配置向导，在**名称**文本框输入规则名称（eb-filter-ram-role），在**描述**文本框输入规则的描述，然后单击**下一步**。在**配置事件模式**配置向导，**事件源类型**选择**阿里云官方事件源**，**事件源**选择**acs.ram 访问控制**，**事件类型**选择ram:Config:ConfigurationItemChangeNotification**访问控制配置变更通知**，在**事件模式内容**代码框输入事件模式如下，然后点下一步。`{
 "source": [
 "acs.ram"
 ],
 "data": {
 "resourceName": [
 {
 "prefix": "sg-"
 }
 ]
 },
 "type": [
 "ram:Config:ConfigurationItemChangeNotification"
 ]
}`在**配置事件目标**配置向导，配置以下参数，然后单击**创建**。**服务类型**：单击**事件总线**。**目标账户类型**：默认选择**其他阿里云账号**。**账号ID**：输入接收账号的ID。在本场景中配置「日志账号UID」。**总线名称**：输入default。**角色名称**：输入 「b-account-eb-role」。**事件**：默认选择**完整事件**，不做转换，直接投递原生CloudEvents 1.0协议中的完整结构。
3. 登录日志账号A，配置函数计算：新建服务。登录[函数计算控制台](https://fc.console.aliyun.com/)。在左侧导航栏，单击**服务及函数**。在顶部菜单栏，选择地域，例如：华东2（上海）。在**服务列表**页面，单击**创建服务**。在**创建服务**面板，**名称**输入**eb_event_action**。单击**确定**。新建函数。在服务**eb_event_action**的左侧导航栏，单击**函数管理**。单击**创建函数**。在**创建函数**页面，**名称**输入**eb_event_trigger，运行环境**选择**Python 3**，配置**函数触发器**选择**EventBridge触发器->访问控制，其中触发器名称**ConfigurationItemChangeTrigger，事件类型选择「选中全部事件类型」，其他参数保持默认值。单击**创建**。配置函数的环境变量。在函数**eb_event_trigger**的**函数代码**页签，单击**函数配置**页签。在**环境变量**区域，单击**编辑**。单击**添加变量**，输入该环境变量的变量名称和变量值。**变量MYSQL_ENDPOING,值为RDS内网地址。****变量MYSQL_PORT，值为RDS数据库端口。****变量MYSQL_USER，值为数据库用户名称。****变量MYSQL_PASSWORD，值为数据库用户密码。****变量MYSQL_DBNAME，值为数据库名称。**单击**保存**。配置函数实例生命周期回调方法在**函数管理**页面，单击目标函数**操作**列的**配置**。在编辑函数配置页面的**实例生命周期回调**区域，设置回调程序与超时时间，然后单击**保存**。本示例中的配置如下截图：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0886581571/p971630.png)函数代码在函数**eb_event_trigger**的**触发器管理**页签，单击**函数代码**页签。单击文件**index.py**。拷贝并粘贴如下代码至文件**index.py**。`import pymysql
import json,logging
import os
connection = None
logger = logging.getLogger()
def initialize(context):
 global connection
 try:
 connection = pymysql.connect(
 host=os.environ['MYSQL_ENDPOING'], # 替换为您的HOST名称。
 port=int(os.environ['MYSQL_PORT']), # 替换为您的端口号。
 user=os.environ['MYSQL_USER'], # 替换为您的用户名。
 passwd=os.environ['MYSQL_PASSWORD'], # 替换为您的用户名对应的密码。
 db=os.environ['MYSQL_DBNAME'], # 替换为您的数据库名称。
 connect_timeout=5)
 logger.info('eb job connect mysql success!!!')
 except Exception as e:
 logger.error(
 "ERROR: Unexpected error: Could not connect to MySql instance.")
 raise Exception(str(e))

def pre_stop(context):
 if connection != None:
 connection.close()

def save_transactional(sql, params):
 try:
 cursor=connection.cursor()
 cursor.execute(sql , params)
 connection.commit()
 except Exception as e:
 logger.error(e)

def handler(event, context):
 eb = json.loads(event).get("data")
 eb_action,eb_time,resource_name,req_id = eb.get("resourceEventType"),eb.get("captureTime"),eb.get("resourceName"),eb.get("requestId")
 account_id, region, config_diff, resourse_type = eb.get("accountId"),eb.get("regionId"),eb.get("configurationDiff"),eb.get("resourceType")
 logger.info(eb_action+eb_time+resource_name+req_id+account_id+region+config_diff+resourse_type)
 change_sql = "insert into event_list(req_id,type,time,resource,account,region,configdiff,resourcetype) values(%s,%s,%s,%s,%s,%s,%s,%s)"
 params = (req_id,eb_action,eb_time,resource_name,account_id, region, config_diff, resourse_type)
 save_transactional(change_sql, params)
 return 'success'`**说明**：本段代码是以处理RAM Role资源变更为例，为您介绍对于此类资源变更如何保存到数据库。对于其他资源类型的变更可以在这个方案基础上稍作修改。以上代码示例中提到的表「event_list」结构如下：`CREATE TABLE `event_list` (
 `req_id` varchar(255) NOT NULL,
 `type` varchar(255) DEFAULT NULL,
 `time` varchar(255) DEFAULT NULL,
 `resource` varchar(255) DEFAULT NULL,
 `account` varchar(255) DEFAULT NULL,
 `region` varchar(255) DEFAULT NULL,
 `configdiff` text,
 `resourcetype` varchar(255) DEFAULT NULL,
 PRIMARY KEY (`req_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;`
4. 登录业务账号B，对Ram角色进行变更。增加一个新的Role角色。名称：sg-100。修改一个现有的Role角色，名称：sg-001。删除一个现有的Role角色，名称:sg-001。
5. 登录日志账号A，查看事件追踪通过事件总线控制台查看事件追踪![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0886581571/p971631.png)通过函数计算控制台查看调用日志 ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0886581571/p971632.png)

## 源代码

### 代码介绍

源代码中包含在成员账号中对事件总线的配置，包括事件目标、事件模式配置等。在日志账号中完成函数计算配置。在执行代码之前需要参考以下实施准备，代码配置项会依赖到。

### 实施准备

- 确保已在「企业管理账号」中开通资源目录，并且将其他账号邀请到资源目录中。具体操作，请参见[使用资源目录快速搭建企业的多账号资源结构](https://help.aliyun.com/zh/resource-management/resource-directory/getting-started/use-a-resource-directory-to-quickly-establish-a-structure-for-the-accounts-and-resources-of-an-enterprise)。
- 确保已在「企业管理账号」中开启多账号的配置审计功能。具体操作，请参见[云治理中心-统一配置防护规则](https://help.aliyun.com/zh/cgc/user-guide/configure-protection-rules-in-a-centralized-manner)。
- 确保在各个成员账号中开通事件总线。具体操作，请参见[开通事件总线](https://help.aliyun.com/product/161886.html)。
- 确保在「日志账号」中开通事件总线及函数计算、开通日志服务、配置OSS对象并将函数计算中用到的代码（见下面文档index.py）打包（index.py.zip）上传到OSS。配置相应的VPC网络及安全组用于配置数据库及函数计算资源。创建相应的数据库，相应的数据表及授权。具体操作，请参见[开通事件总线](https://help.aliyun.com/product/161886.html) 和 [开通函数计算](https://help.aliyun.com/product/50980.html)。

### 代码地址

github代码地址：[https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/compliance/3.4-sub-resource-changes/python_script](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/compliance/3.4-sub-resource-changes/python_script)

## 故障排除

### 为什么业务账号内的资源变更了但事件追踪查不到？

从业务账号内资源变更到配置审计，再投递到事件总线，这个过程大概会有5~8分钟的时延。可以稍微等几分钟再去查询事件追踪。

### 函数计算中的程序无法访问后端数据库？

- 确认当前函数计算是否有配置网络选项，需要确保函数计算所在的网络环境跟RDS在同一个VPC内。

## 相关内容

- [事件总线EventBridge](https://help.aliyun.com/zh/eventbridge/product-overview/what-is-eventbridge)
- [函数计算](https://help.aliyun.com/zh/functioncompute/what-is-function-compute)
- [配置审计](https://help.aliyun.com/product/127306.html)
- [云治理中心](https://help.aliyun.com/product/252812.html)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-82（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
