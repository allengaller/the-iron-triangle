<!-- source: https://help.aliyun.com/zh/well-architected/solution-134 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929342 -->

# 基于VPC流日志实现多账号网络流量监控

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970902.png)

多账号场景下VPC、交换机、弹性网卡ENI等网络基础设施通常分布于不同账号、不同地域中，对全网流量进行统一分析及监控是用户面临的网络运维难题之一。本方案使用专有网络VPC提供的流日志功能记录VPC网络中弹性网卡ENI传入和传出的流量信息，结合日志服务SLS的多账号日志收集分析能力，为用户提供丰富的流量分析及监控能力，帮助用户在全网或特定网络范围内检查访问控制规则、监控网络流量及排查网络故障。

## 方案优势

### 多账号流日志统一记录

配置多账号采集后，用户在日志中心账号下的日志审计服务中开启VPC流日志的采集，日志审计服务会将当前中心账号以及其他成员账号下满足采集策略的VPC实例的流日志采集到日志中心账号下各个与VPC实例处于相同地域的日志并支持中心化存储。

### 自定义流量分析及监控可视化

日志服务提供一站式的告警监控、降噪、事务管理、通知分派的智能运维平台，支持自定义可视化展示查询和分析结果。日志服务提供表格、线图、柱状图等多种统计图表，用户可以根据分析需求选用合适的图表类型展示查询和分析结果，并将结果保存到仪表盘中。

### 精细化数据采集

每条流日志会捕获特定捕获窗口中的特定**五元组网络流**，如果用户选择为VPC或交换机创建流日志，则会捕获VPC和交换机中**所有弹性网卡的流量**，包括开启流日志功能后新建的弹性网卡。

## 客户场景

### 多账号VPC流量分析及监控

#### 场景描述

多账号场景下网络基础设施通常分布于不同账号中，云上网络流量通常包含南北向及东西向，VPC与公网、VPC之间、VPC与IDC之间等多种流量监控场景下，用户对流量精细化分析审计、监控面临挑战，例如在全网范围内检查访问控制规则、监控网络正常及异常流量、排查网络故障、自定义TOP内网流量视图、自定义TOP公网访问流量视图等。

#### 适用客户

多账号场景下对网络流量分析及监控有诉求的企业客户。

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970900.png)

方案架构说明如下：

- 通过专有网络VPC提供的**VPC流日志**功能对VPC、交换机vSwitch、弹性网卡ENI的流量日志进行记录。流日志功能捕获的流量信息以日志方式写入日志服务中。每条日志会捕获特定捕获窗口中的特定**五元组**网络流，捕获窗口大约为10分钟，该段时间内流日志功能先聚合数据再发布日志，捕获流量字段详情参见[日志字段详情](https://help.aliyun.com/zh/sls/log-fields-27)。如果您选择为VPC或交换机创建流日志，则会捕获VPC和交换机中所有弹性网卡的流量，包括开启流日志功能后新建的弹性网卡。
- 对多账号、多地域的VPC流日志使用**SLS的日志审计服务**进行收集，将流日志统一存储到**日志账号**SLS的Logstore中。
- 为实现多账号的日志统一收集，使用**资源目录**对多账号进行统一管理，在**企业管理主账号**中将**日志账号**配置为SLS日志审计服务的**委派管理员账号**。
- 使用SLS丰富的日志查询、可视化报表及告警能力实现对流日志的分析及监控。

### 日志审计服务多账号采集

在SLS日志审计服务中配置多账号采集后，在中心账号下的日志审计服务中开启VPC流日志的采集，日志审计服务会将当前中心账号以及其他成员账号（阿里云主账号）下满足采集策略的VPC实例的流日志采集到中心账号下各个与VPC实例处于相同地域的日志服务Project （名称为**slsaudit-region-$uid-$region**）中。

日志审计服务还支持中心化存储。开启中心化存储后，日志审计服务会将存储在各个地域Logstore（vpc_log）中的VPC流日志同步到中心Project（名称为**slsaudit-center-$uid-$center_region**）下名为vpc_log的Logstore中，实现中心化查询、分析、告警、可视化、二次开发等操作。中心化存储依赖日志服务的数据加工功能。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 专有网络VPC | [专有网络VPC（Virtual Private Cloud）](https://help.aliyun.com/zh/vpc/what-is-vpc)是您专有的云上私有网络。您可以完全掌控自己的专有网络，例如选择IP地址范围、配置路由表和网关等，您可以在自己定义的专有网络中使用阿里云资源，如云服务器、云数据库RDS和负载均衡等。 | 本身免费，详情参见[产品计费](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |
| VPC流日志 | 专有网络VPC提供[流日志](https://help.aliyun.com/zh/vpc/vpc-flow-logs)功能，可以记录VPC网络中弹性网卡ENI（Elastic Network Interface）传入和传出的流量信息，帮助您检查访问控制规则、监控网络流量和排查网络故障。 | 收费，详情参见[计费说明](https://help.aliyun.com/zh/vpc/user-guide/billing-of-flow-logs)。 |
| 日志服务SLS | [日志服务SLS](https://help.aliyun.com/zh/sls/what-is-log-service)是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/sls/billing-overview)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 日志账号 | 所有资源目录成员账号的日志都归集到该账号，便于日志的统一收集与管理。 |
| 委派管理员账号 | 资源目录的管理账号可以将资源目录中的成员设置为可信服务的委派管理员账号。设置成功后，委派管理员账号将获得管理账号的授权，可以在对应可信服务中访问资源目录组织和成员信息，并在该组织范围内进行业务管理。 |
| 五元组 | 源IP地址、源端口、目的IP地址、目的端口和传输层协议这五个量组成的集合。 |

## 安全性

### 日志服务SLS安全性

阿里云日志服务具有丰富的安全防护能力，支持服务器端加密、细粒度权限管控、详细服务日志等特性，同时提供日志审计功能，针对主流云产品提供多账号下实时自动化、中心化采集云产品日志并实现审计。日志服务为您提供丰富的数据洞察能力，同时满足企业数据的安全与合规要求，详情参见[安全与合规概述](https://help.aliyun.com/zh/sls/overview)。

多账号VPC流日志使用日志审计服务进行收集，日志审计服务使用时需要用户授权，完成授权后，日志审计服务将使用服务关联角色进行云产品的日志采集。更多信息，请参见[管理服务关联角色AliyunServiceRoleForSLSAudit](https://help.aliyun.com/zh/sls/manage-the-aliyunserviceroleforslsaudit-service-linked-role)。

### VPC安全性

专有网络VPC具有安全可靠、灵活可控、灵活可用以及较强的可扩展性，详情参见[产品优势](https://help.aliyun.com/zh/vpc/product-overview/benefits)及[访问控制](https://help.aliyun.com/zh/vpc/access-control)。

## 注意事项

### SLS限制及注意事项

- SLS存在基础资源、查询分析、告警等方面的使用限制，详情参见SLS[使用限制](https://help.aliyun.com/zh/sls/limits-1/)。
- 可视化功能中存在部分报表数量等限制，详情参见可视化[限制说明](https://help.aliyun.com/zh/sls/overview-of-visualization)。
- **使用日志审计服务进行日志区域化存储或中心化存储前，请合理评估存储地域是否满足相关法律法规和安全监管的要求**，详情参见日志审计服务[使用前须知](https://help.aliyun.com/zh/sls/usage-notes)。

### VPC流日志使用须知

- VPC流日志采集的最细粒度为弹性网卡ENI的出入流量，ENI详细介绍参考[概述](https://help.aliyun.com/zh/ecs/user-guide/eni-overview)。
- SLS VPC流日志采集存在部分地域及资源限制，更多详情参见[使用前须知](https://help.aliyun.com/zh/sls/usage-notes-34/)。

## 实施步骤

日志审计服务支持跨账号采集云产品日志，本实施步骤将在多账号场景下配置VPC流日志的收集，并给出查询分析及监控告警配置示例。

### 实施准备

- 已有阿里云账号，并已使用[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)对多账号进行统一管理。在使用资源目录前，需先创建或邀请成员。具体操作，请参见[创建成员](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/create-a-member)或[邀请阿里云账号加入资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/invite-an-alibaba-cloud-account-to-join-a-resource-directory)。
- 已完成**多账号云上组网**，已有VPC网络流量。
- 已选定某个资源目录成员账号为**日志账号**，并已开通日志服务SLS。可登录[日志服务控制台](https://sls.console.aliyun.com/)，根据页面，提示完成开通。
- 已阅读注意事项章节知晓使用限制及须知等内容。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 添加日志账号为委派管理员账号

1. 使用**企业管理账号**登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)。
2. 在左侧导航栏，选择**资源目录 > 可信服务**。
3. 在**可信服务**页面，单击**日志审计服务**的**管理**。
4. 在**委派管理员账号**区域，单击**添加**。
5. 在**添加委派管理员账号**面板，选中**日志账号成员**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970899.png)
6. 单击**确定**。添加成功后，使用该委派管理员账号访问对应可信服务的多账号管理模块，即可进行资源目录组织范围内的管理操作。

#### 配置日志审计服务多账号采集

1. 使用**日志账号**登录[日志服务控制台](https://sls.console.aliyun.com/)。
2. 在**日志应用**区域的**审计与安全**页签下，单击**日志审计服务**。
3. 在左侧导航栏中，选择**多账号配置 > 全局配置**。
4. 在**资源目录管理模式**页签中，单击**修改**。
5. 在**添加账号**面板中，选择目标账号，然后单击**确认**。资源目录管理模式支持全员方式和自定义方式。更多信息，请参见[资源目录管理模式（推荐）](https://help.aliyun.com/zh/sls/configure-multi-account-collection)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970903.png)**方式****说明**全员日志审计服务自动将资源目录下的所有成员纳入到采集名单中，并采集这些成员中已开启日志采集功能的云产品的日志。新增资源目录成员后，该成员自动被纳入采集名单中。移除资源目录成员后，该成员自动被移出采集名单。自定义您可以自定义选择目标成员到采集名单中，日志审计服务会采集这些成员中已开启日志采集功能的云产品的日志。新增资源目录成员后，该成员不会自动纳入采集名单中。移除资源目录成员后，如果该成员在您的采集名单中，会被自动移出采集名单。

#### 开启流日志采集

1. 在左侧导航栏中，选择**云产品接入 > 全局配置**。
2. 在**全局配置**页面，单击**修改**。
3. 打开VPC流日志对应的采集开关。通过采集策略，可对账号、地域或实例等因素进行限制，实现精细化的日志采集目的，本示例不做修改，详情参见[采集策略](https://help.aliyun.com/zh/sls/configure-log-collection-policies)。根据实际情况调整区域化存储及中心存储的日志保存时间，本示例不做修改。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970907.png)
4. 单击**确定**。

#### 查询和分析日志

首次开启日志采集后需等待一段时间再进行日志查询。

日志审计服务提供统一的日志查询入口。开启中心化采集后进行日志查询，VPC流日志将被统一采集到中心Project下的专属Logstore中。

1. 在左侧导航栏中，选择**审计查询 > 中心化 > VPC**。
2. 输入查询和分析语句，执行查询和分析操作。查询和分析语句由查询语句和分析语句构成，格式为**查询语句|分析语句**，查询分析语句语法请参见[查询语法](https://help.aliyun.com/zh/sls/query-syntax/)、[SQL分析语法](https://help.aliyun.com/zh/sls/aggregate-function)。例如通过**account-id**字段，确定该VPC流日志所属的阿里云账号；通过**region**字段和**vpc-id**字段确定该流日志所属的VPC实例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970910.png)例如执行如下的查询和分析语句，统计不同阿里云账号在不同地域的不同VPC实例的流日志条数。`* |
SELECT
 count(*) AS "日志条数",
 region,
 "account-id",
 "vpc-id"
FROM log
GROUP BY
 "account-id",
 "region",
 "vpc-id"`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970909.png)

#### 查看内置报表

在日志审计服务中，开通VPC流日志的采集后，自动生成VPC流日志概览、VPC流日志Reject中心和VPC流日志Traffic中心三个仪表盘，帮助您更好地分析日志。

1. 在左侧导航栏中，选择**审计报表 > 中心化 > VPC**。
2. 查看仪表盘。右上角**时间选择**可以按时间进行数据筛选，报表右上角点击图标后可查看**SQL**、下载数据等操作。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970901.png)

#### 根据自定义查询语句制作报表

1. 执行下列查询SQL，查看内网流量大小TOP 10的VPC。`action: ACCEPT |
SELECT
 "vpc-id",
 sum(bytes) AS flow
FROM log
WHERE
 ip_to_domain(dstaddr) = 'intranet'
 and ip_to_domain(srcaddr) = 'intranet'
GROUP BY
 "vpc-id"
ORDER BY
 flow DESC
LIMIT
 10`
2. 按照下图图示内容选择柱状图，调整格式化及小数点位数，生成报表。可自定义选择不同时间段快速修改查询范围，更多报表详情请参见[可视化](https://help.aliyun.com/zh/sls/visualization-2/)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970913.png)
3. 可单击**添加到仪表盘**按钮，对报表进行保存，后续在仪表盘菜单进行报表查看。

#### 配置告警

配置示例：网络中不应该出现`100.64.0.0/10`到`192.168.0.0/16`的访问流量，若出现则进行短信报警。

1. 执行下列查询SQL，查询相应网段网络流量情况。`action:ACCEPT|
SELECT srcaddr,dstaddr,dstport from log
WHERE is_subnet_of('100.64.0.0/10', srcaddr) = true 
AND is_subnet_of('192.168.0.0/16', dstaddr) = true`
2. 选择另存为告警-新版告警。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970914.png)
3. 配置告警规则，修改检查频率、触发条件、添加标注、行动策略等参数后保存。本示例触发条件为有>=1条查询结果即触发，在添加标注中修改desc字段为`源IP：${srcaddr} 目的IP：${dstaddr} 目的端口：${dstport}` ，行动策略选择“SLS审计内置行动策略”。更多告警规则详情参见[告警管理](https://help.aliyun.com/zh/sls/alert-management/)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970917.png)
4. 在审计告警菜单中单击行动策略，在SLS审计内置行动策略中选择修改，可对行动策略进行编辑，按告警严重程度流转到不同行动组，并配置告警发送渠道、接收人、发送时间等。更多告警通知详情参见[通知管理](https://help.aliyun.com/zh/sls/notification-management/)，接收人管理详情参见[用户管理](https://help.aliyun.com/zh/sls/user-management/)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970918.png)
5. 本示例中若SQL查询结果中存在查询结果会触发告警条件，告警接收人将会接收到短信通知。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970919.png)

### 更多查询示例

#### 按小时查看进出专线（某网段）流量大小

```
action: ACCEPT |
SELECT
  date_format(
    from_unixtime(__time__),
    '%Y-%m-%d %H:00'
  ) AS time,
sum(bytes) AS flow
FROM  log
WHERE
  is_subnet_of('192.168.0.0/16', dstaddr) = true
  or is_subnet_of('192.168.0.0/16', srcaddr) = true
GROUP BY
  time
ORDER BY
  time ASC
```

#### 按小时查看进出专线（某网段）带宽

查询带宽时将SQL中的sum内容进行调整即可。

```
action: ACCEPT |
SELECT
  date_format(
    from_unixtime(__time__),
    '%Y-%m-%d %H:00'
  ) AS time,
sum(bytes * 8 /(
      CASE
        WHEN "end"-start = 0 THEN 1
        ELSE "end"-start
      END
    )
) AS bandwidth
FROM  log
WHERE
  is_subnet_of('192.168.0.0/16', dstaddr) = true
  OR is_subnet_of('192.168.0.0/16', srcaddr) = true
GROUP BY
  time
ORDER BY
  time ASC
```

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970920.png)

#### 进出内网流量大小TOP 10的VPC

```
action: ACCEPT |
SELECT
  "vpc-id",
  sum(bytes) AS flow
FROM  log
WHERE
  ip_to_domain(dstaddr) = 'intranet'
  and ip_to_domain(srcaddr) = 'intranet'
GROUP BY
  "vpc-id"
ORDER BY
  flow DESC
LIMIT
  10
```

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970908.png)

#### 基于源IP/目的IP的流量TOP 10

```
* |
SELECT
  srcaddr,
  dstaddr,
  sum(bytes) AS flow
FROM  log
GROUP BY
  srcaddr,
  dstaddr
ORDER BY
  flow DESC
LIMIT
  10
```

#### 基于源IP/目的IP/Action + 自定义时段精确查询

注意：SQL中指定时间进行精确查询时，页面的查询时间段需要包含SQL中指定的时间。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2476581571/p970922.png)

```
srcaddr :192.168.0.123
AND dstaddr :100.100.30.26
AND (
  action :ACCEPT
  OR action :REJECT
) |
SELECT
  action,
  srcaddr,
  srcport,
  dstaddr,
  dstport,
  direction,
  protocol,
  "vswitch-id",
  "vm-id",
  "vpc-id",
  "account-id",
  "eni-id",
  bytes,
  packets,
  start,
  "end",
  "log-status",
  version
FROM  log
WHERE
  to_unixtime(
    date_parse('2022-11-04 16:00:00', '%Y-%m-%d %H:%i:%s')
  ) <= start
  AND to_unixtime(
    date_parse('2022-11-04 16:20:00', '%Y-%m-%d %H:%i:%s')
  ) >= "end"
ORDER BY
  start
LIMIT
  1000
```

#### 被REJECT的流量TOP 10源IP

```
action:REJECT |
SELECT
  srcaddr,sum(bytes) AS flow
FROM  log
GROUP BY srcaddr
ORDER BY flow desc
LIMIT
  10
```

#### 特定端口集的公网来源访问成功的流量（高危端口检测）

```
action:ACCEPT|
SELECT * FROM log
WHERE dstport	IN (22)
AND ip_to_domain(srcaddr) != 'intranet' 
AND is_subnet_of('100.64.0.0/10', srcaddr) = false
AND direction = 'in'
```

#### 特定源网段到目的网段流量查询

```
action:ACCEPT|
SELECT srcaddr,dstaddr,dstport from log
WHERE is_subnet_of('100.64.0.0/10', srcaddr) = true 
AND is_subnet_of('192.168.0.0/16', dstaddr) = true
```

#### 访问目的地址是互联网的频次TOP 10源IP

```
action :ACCEPT |
SELECT
  srcaddr,
  count(*) AS frequency
FROM  log
WHERE
  ip_to_domain(dstaddr) != 'intranet'
  AND is_subnet_of('100.64.0.0/10', dstaddr) = false
  AND direction = 'out'
GROUP BY
  srcaddr
ORDER BY
  frequency DESC
LIMIT
  10
```

#### 指定IP段、端口范围看流量大小

```
action :ACCEPT |
SELECT
  sum(bytes)
FROM  log
WHERE
  is_subnet_of('100.64.0.0/10', srcaddr) = true
  AND is_subnet_of('192.168.0.0/16', dstaddr) = true
  AND dstport >= 1
  AND dstport <= 65535
```

## 故障排除

### 告警问题

#### 为什么设置了多个触发条件只有一个生效？

查询统计结果按照触发条件的顺序逐条匹配，当查询统计结果符合第一个触发条件后，不再匹配后面的触发条件。因此当您设置触发条件中的严重度时，需从较高级别的严重度开始配置。具体操作，请参见[设置告警严重度](https://help.aliyun.com/zh/sls/specify-severity-levels-for-alerts)。

#### 如何基于关键字设置告警？

将日志采集到日志服务后，您可以通过日志服务告警系统实现基于日志关键字的告警。具体操作，请参见[基于日志关键字设置告警](https://help.aliyun.com/zh/sls/configure-alerts-based-on-log-keywords)。

#### 为什么出现漏告警或者误告警？

- 漏告警：例如告警触发条件是错误日志数大于10就触发告警，而在Logstore查询分析页面查询时某个时间段内错误日志数实际大于10 ，却没有触发告警。
- 误告警：例如告警触发条件是QPS低于100就触发告警，而在Logstore查询分析页面查询时某个时间段内QPS实际大于100，却触发了告警。

出现漏告警或者误告警，一般是由于数据写入到Logstore到可查询存在一定的延迟，当告警监控规则中的查询时间范围设置为相对时间时，会导致告警的查询不完全准确。为了避免这两种情况，建议扩大告警监控规则中的查询时间范围或者将查询时间范围设置为整点时间。更多信息，请参见[监控时效性说明](https://help.aliyun.com/zh/sls/monitoring-timeliness)。

#### 更多告警问题

更多常见问题详情参见SLS告警[常见问题](https://help.aliyun.com/zh/sls/alert-monitoring-faq/)。

### 如何配置更多可视化报表或统计图表？

可视化相关介绍及配置详情参见[可视化](https://help.aliyun.com/zh/sls/visualization-2/)。

### 日志数据采集常见问题

数据采集常见问题详情参见[FAQ](https://help.aliyun.com/zh/sls/faq-18/)。

### 日志查询与分析常见问题

#### key (XXX) is not config as key value config,if symbol : is in your log,please wrap : with quotation mark "

- 报错原因：未对XXX字段建立索引，或者您所使用的字段中包含了特殊字符（例如空格）但未使用双引号（""）包裹。
- 解决方法：为目标字段设置索引，并开启统计功能。具体操作，请参见[配置索引](https://help.aliyun.com/zh/sls/create-indexes)。使用双引号（""）包裹目标字段。

#### sql query must follow search query,please read syntax doc

- 报错原因：仅使用了分析语句。在日志服务中，分析语句必须与查询语句一起使用，格式为**查询语句|分析语句**。
- 解决方法在分析语句前加上查询语句，例如*** | SELECT status, count(*) AS PV GROUP BY status**。更多信息，请参见[基础语法](https://help.aliyun.com/zh/sls/log-analysis-overview)。

#### 更多查询分析问题

SLS日志查询分析常见问题详情参见[FAQ](https://help.aliyun.com/zh/sls/index-and-query-faq/)。

## 相关内容

- [SLS日志审计服务概述](https://help.aliyun.com/zh/sls/overview-of-log-audit-service)
- [SLS告警功能介绍](https://help.aliyun.com/zh/sls/feature-overview/)
- [SLS可视化概述](https://help.aliyun.com/zh/sls/overview-of-visualization)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-134（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
