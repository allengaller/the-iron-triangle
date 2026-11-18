<!-- source: https://help.aliyun.com/zh/well-architected/solution-49 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929222 -->

# 基于日志服务实现企业级统一日志归集

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4576581571/p969868.png)

随着企业信息化的发展，面向云的IT基础设施越来越普遍，如何在庞大的IT基础设施面前管理软件的日志，成为IT稳定性保障的关键环节。 本方案主要介绍如何使用SLS 对阿里云、专有IDC以及第三方云场景下，进行企业级的统一日志管理。

## 方案优势

### 集中日志记录

本方案提供了常见场景的日志统一投递，包括采集主机上的系统日志、跟应用程序集成采集程序业务日志、跟云产品集成采集云产品日志。通过统一日志投递，方便用户在一个可自定义、用户友好地产品控制面板做日志分析和可视化展示。

### 日志灵活查询可视化

支持查询SQL语法，支持用户定制的查询需求。另外SLS产品提供了丰富的报表制作能力，用户可以把查询结构按不同维度展示。

### 超出默认阿里云科技服务日志之外的日志记录功能

可以将您的日志记录功能扩展到默认的阿里云科技服务日志之外。非常灵活地支持了可以捕获客户在自建IDC环境上主机、网络设备日志。另外您如果有搭建一些开源软件（Logstash）也能够轻松对接。

## 客户场景

### 公有云业务日志收集分析

#### 场景描述

业务全部跑在公有云上，需要将业务的日志统一在一个地方进行管理。

#### 适用客户

- 公有云客户
- 每个账号下面的业务日志统一投递到一个日志账号

### 混合云统一日志

#### 场景描述

混合云场景，客户需要将IDC内的日志与云上日志统一在一个地方进行管理。

#### 适用客户

- 混合云客户且有专线连通
- 希望将IDC及云上的业务日志统一投递到一个日志账号

### 多云统一日志

#### 场景描述

业务跑在多云环境，客户需要将不同云环境中的业务日志统一在一个地方进行管理。

#### 适用客户

- 多云客户
- 希望将各朵云上的业务日志统一投递到一个日志账号，统一管理

## 方案架构

本方案主要介绍如何使用SLS 对阿里云、专有IDC以及第三方云场景下，进行企业级的日志管理。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4576581571/p969866.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 日志服务 | [日志服务SLS](https://help.aliyun.com/zh/sls/what-is-log-service)是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/sls/billing-overview)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| Logtail | Logtail是日志服务提供的日志采集Agent，用于采集阿里云ECS、自建IDC、其他云厂商等服务器上的日志。 |
| Logstash | Logstash是一个开源数据收集引擎，具有实时管道功能。 |
| Flume | Flume是一个分布式、可靠、和高可用的海量日志采集、聚合和传输的系统 |
| FluentD | fluentd是一个实时的数据收集系统，不仅可以收集日志，还可以收集定期执行的命令输出和HTTP请求内容。 |

## 安全性

### 服务器端加密

日志服务提供服务器端加密，并支持基于SSL/TLS的HTTPS加密传输，有效防止数据在云端的潜在安全风险。

- 服务器端加密。日志服务支持通过密钥管理服务KMS（Key Management Service）对数据进行加密存储，提供数据静态保护能力。KMS是阿里云提供的一款安全、易用的管理类服务。您无需花费大量成本来保护密钥的保密性、完整性和可用性。借助密钥管理服务，您可以安全、便捷的使用密钥，专注于开发加解密功能场景。您可以通过KMS控制台查看和管理KMS密钥。更多信息，请参见[密钥服务概述](https://help.aliyun.com/zh/kms/key-management-service/support/overview-4)。
- 基于SSL/TLS的HTTPS加密传输。日志服务支持通过HTTP或HTTPS的方式访问。安全传输层协议。（SSL/TLS）用于在两个通信应用程序之间提供保密性和数据完整性。

### 身份访问控制

日志服务中的访问控制，在日志管理账号中推荐的角色有两类：

- 日志管理角色。具备管理日志服务，包括创建，修改，删除Project。对应的RAM 角色配置：AliyunLogFullAccess。
- 日志查看角色。如查询特定Project下面的日志信息，相应的Policy可以如下定义：`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "log:ListConfig",
 "log:ListConsumerGroup",
 "log:ListDashboard",
 "log:ListDomains",
 "log:ListEtlJob",
 "log:ListEtlMetaName",
 "log:ListExternalStore",
 "log:ListJobs",
 "log:ListJobSchedules",
 "log:ListLogStores",
 "log:ListMachineGroup",
 "log:ListMachines",
 "log:ListProject",
 "log:ListReport",
 "log:ListSavedSearch",
 "log:ListShards",
 "log:ListShipper",
 "log:ConsumerGroupHeartBeat",
 "log:GetAppliedConfigs",
 "log:GetAppliedMachineGroups",
 "log:GetChart",
 "log:GetConfig",
 "log:GetConsumerGroupCheckPoint",
 "log:GetCursorOrData",
 "log:GetDashboard",
 "log:GetEtlJob",
 "log:GetEtlMeta",
 "log:GetExternalStore",
 "log:GetIndex",
 "log:GetJob",
 "log:GetJobSchedule",
 "log:GetLogging",
 "log:GetLogStore",
 "log:GetLogStoreContextLogs",
 "log:GetLogStoreHistogram",
 "log:GetLogStoreLogs",
 "log:GetMachineGroup",
 "log:GetProject",
 "log:GetSavedSearch",
 "log:GetShipperConfig",
 "log:GetShipperStatus",
 "log:GetShipperTasks"
 ],
 "Resource": "acs:log:*:XXXXXXXXX:project/xxx" // 特定的Project名称
 }
 ]
}`

## 注意事项

### 区域（Region）限制

本方案要求现有的需要采集指标或日志的设备能够连通阿里云的网络环境，目前SLS支持的Region 参考 [链接](https://help.aliyun.com/zh/sls/endpoints)。

对于IDC或者其他云厂商的场景，如果是进行POC的话可以优先使用SLS的公网地址进行日志收集；如果是生产使用建议搭建相应的专线接入阿里云网络，以保障数据传输的可靠性。

### 产品功能限制

SLS在产品使用上面有些限制，具体可以查看[产品限制](https://help.aliyun.com/zh/sls/limits-1/)。

## 实施步骤

### 实施准备

1. 日志账号确保在阿里云官网已经开通 SLS服务。
2. 确保现有的网络环境，可以连通到阿里云网络。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：4小时。

说明：根据实施选项不同预计时长可能存在差异。

### 操作步骤

#### 使用Logtail采集日志

##### 安装Logtail

**1、阿里云ECS**

如果是阿里云的ECS服务器，默认已经安装iLogtail了，可以直接使用。如果发现没有安装可以参考 [链接](https://help.aliyun.com/zh/sls/install-logtail-on-ecs-instances)。

**2、阿里云ACK**

阿里云ACK默认带有Logtail采集插件，如果发现没有安装， 可以通过下面步骤安装

1. 打开 [https://cs.console.aliyun.com/#/k8s/cluster/list](https://cs.console.aliyun.com/#/k8s/cluster/list)
2. 选中相应的集群进入
3. 左侧，选择应用->Helm，点击右“边“应用目录”
4. 在出现的页面里，选择”运维/可观测性“![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4576581571/p969867.png)选择 ack-sls-logtail进行安装![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4576581571/p969869.png)阿里云ACK 独享模式 参考 [链接](https://help.aliyun.com/zh/sls/use-the-log-service-console-to-collect-container-text-logs-in-daemonset-mode)。阿里云ACK Servless模式 SideCar方式 参考 [链接](https://help.aliyun.com/zh/sls/use-crds-to-collect-container-text-logs-in-sidecar-mode)。

##### 自建k8s或其他云厂商的k8s

- 参考自建k8s采集方案 [链接](https://help.aliyun.com/zh/sls/install-logtail-components-in-a-kubernetes-cluster)。

##### 其他云厂商主机

- Linux主机安装Logtail指导 [链接](https://help.aliyun.com/zh/sls/install-logtail-on-a-linux-server)。
- WIndows主机安装Logtail指导 [链接](https://help.aliyun.com/zh/sls/install-logtail-on-a-windows-server)。

##### 配置跨账号采集

这个步骤对于需要跨账号采集阿里云上ECS或者K8S日志的情况下，需要这样操作通过设置iLogtail的用户标识识，来实现跨账号采集。

- ECS上设置iLogtail用户标识的方法，操作步骤参考[通过Logtail跨阿里云账号采集日志](https://help.aliyun.com/zh/sls/use-logtail-to-collect-logs-across-accounts)。
- K8S上设置iLogtail用户标识的方法，操作步骤参考[通过Logtail跨阿里云账号采集容器日志](https://help.aliyun.com/zh/sls/use-logtail-to-collect-container-logs-across-accounts)。

##### 机器组配置

**1、非k8s的场景**

- 基于ip地址创建机器组，操作步骤参考[链接](https://help.aliyun.com/zh/sls/create-an-ip-address-based-machine-group) 。
- 基于自定义标识创建机器组， 操作步骤参考 [链接](https://help.aliyun.com/zh/sls/create-a-user-defined-identity-machine-group) 。

如果机器经常进行扩容缩容，推荐基于自定义标识创建机器组

**2、k8s场景**

无需配置机器组，机器组在k8s安装完logtail组件后，自动在k8s对应的project生成。

##### 采集配置

**极简模式采集**

适合支持单行和多行日志（比如带Java堆栈），适合任意格式 ，如果日志比较杂乱，推荐这个模式，采集到的日志将放到一个名叫content的字段里。操作步骤参考：[链接](https://help.aliyun.com/zh/sls/collect-logs-in-simple-mode)。

**正则匹配模式采集**

适合日志格式比较固定的场景，配置好相应的正则即可。操作步骤参考：[链接](https://help.aliyun.com/zh/sls/collect-logs-in-full-regex-mode)。

**Json模式采集**

适合单行日志满足Json格式的日志场景。操作步骤参考：[链接](https://help.aliyun.com/zh/sls/collect-logs-in-json-mode)。

**IIS日志采集**

适合IIS服务器打印的日志。操作步骤参考：[链接](https://help.aliyun.com/zh/sls/collect-logs-in-iis-configuration-mode)。

**Apache日志采集**

适合Apache服务打印的日志。操作步骤参考： [链接](https://help.aliyun.com/zh/sls/collect-logs-in-apache-configuration-mode)。

**Nginx日志采集**

适合Nginx服务日志。操作步骤参考：[链接](https://help.aliyun.com/zh/sls/use-the-nginx-configuration-mode-to-collect-logs)。

**K8S 标准输出采集**

适合采集Pod打印到stdout和stderr的日志， 操作步骤参考：[链接](https://help.aliyun.com/zh/sls/collect-container-stdout-and-stderr-in-daemonset-mode)。

**K8S 日志文件采集**

适合采集Pod内打印的日志文件，操作步骤参考：[链接](https://help.aliyun.com/zh/sls/use-the-log-service-console-to-collect-container-text-logs-in-daemonset-mode)。

#### 使用阿里云SLS SDk写入日志数据

##### 主流语言SDK

SLS支持主流语言的SDK，使用SDK可以很方便地往SLS写入数据。

| [Java SDK](https://help.aliyun.com/zh/sls/developer-reference/overview-of-log-service-sdk-for-java) | [Python SDK](https://help.aliyun.com/zh/sls/developer-reference/overview-4) |
| --- | --- |
| [.NET SDK](https://help.aliyun.com/zh/sls/overview-of-log-service-sdk-for-dotnet) | [.NET Core SDK](https://help.aliyun.com/zh/sls/developer-reference/overview-of-log-service-sdk-for-dotnet-core) |
| [Node.js SDK](https://help.aliyun.com/zh/sls/developer-reference/overview-of-log-service-sdk-for-node-js) | [PHP SDK](https://help.aliyun.com/zh/sls/developer-reference/overview-of-log-service-sdk-for-php) |
| [Go SDK](https://help.aliyun.com/zh/sls/developer-reference/overview-14) | [C SDK](https://help.aliyun.com/zh/sls/developer-reference/log-service-sdk-for-c) |

##### 移动端埋点SDK

- 移动端：可以使用移动端 SDK [IOS](https://help.aliyun.com/zh/sls/developer-reference/overview-of-log-service-sdk-for-ios), [Android](https://help.aliyun.com/zh/sls/developer-reference/overview-of-log-service-sdk-for-android) 接入。
- ARM 设备：ARM 平台可以使用 [Native C](https://github.com/aliyun/aliyun-log-c-sdk/tree/lite) 交叉编译。
- H5网页端，直接使用Webtracking API 方式写入日志服务 参考[链接](https://help.aliyun.com/zh/sls/use-the-web-tracking-feature-to-collect-logs)。

#### 日志查询分析

SLS除了提供日志采集和存储外，还提供强大的日志查询能力。包括关键词和SQL查询。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4576581571/p969874.png)

##### 使用关键词或SQL查询日志

**1、配置索引**

配置字段索引或全文索引，操作步骤参考 [链接](https://help.aliyun.com/zh/sls/create-indexes)。

**2、使用关键词查询**

支持使用 and、or、not、比较等方式进行关键词搜索查询，具体参考 [链接](https://help.aliyun.com/zh/sls/query-syntax/)。

示例

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4576581571/p969872.png)

**3、使用SQL查询**

SLS的SQL支持SQL 92标准语法，并且支持MySQL外表（可以将Logstore和MySQL表join），使用SQL查询的前提是对Logstore配置了字段索引。

SLS SQL查询编写方法如下。在控制台查询SQL的时候，必须先进行关键词查询，然后通过管道符号 | ，后面跟SQL查询。 关键词查询，可以在SQL运行前提前过滤日志，帮助提升SQL执行速度。

```
关键词查询 | SQL语句
```

如果不想进行关键词查询就跑SQL，可以用*作为关键词查询，表示不做过滤。

```
* | SQL语句
```

每个字段就是SQL可以查询的列。SLS SQL当前支持的函数类型如下。

| [通用聚合函数](https://help.aliyun.com/zh/sls/aggregate-function) | [安全检测函数](https://help.aliyun.com/zh/sls/security-check-functions) | [Map映射函数](https://help.aliyun.com/zh/sls/map-functions-and-operators) | [估算函数](https://help.aliyun.com/zh/sls/approximate-functions) | [数学统计函数](https://help.aliyun.com/zh/sls/mathematical-statistics-functions) | [数学计算函数](https://help.aliyun.com/zh/sls/mathematical-calculation-functions) |
| --- | --- | --- | --- | --- | --- |
| [字符串函数](https://help.aliyun.com/zh/sls/string-functions-1) | [日期和时间函数](https://help.aliyun.com/zh/sls/date-and-time-functions-1) | [URL函数](https://help.aliyun.com/zh/sls/url-functions) | [正则式函数](https://help.aliyun.com/zh/sls/regular-expression-functions-1) | [JSON函数](https://help.aliyun.com/zh/sls/json-functions) | [类型转换函数](https://help.aliyun.com/zh/sls/data-type-conversion-functions) |
| [IP地理函数](https://help.aliyun.com/zh/sls/ip-functions) | [GROUP BY语法](https://help.aliyun.com/zh/sls/group-by-clause) | [窗口函数](https://help.aliyun.com/zh/sls/window-functions) | [HAVING语法](https://help.aliyun.com/zh/sls/having-clause) | [ORDER BY语法](https://help.aliyun.com/zh/sls/order-by-clause) | [LIMIT语法](https://help.aliyun.com/zh/sls/limit-clause) |
| [CASE WHEN和IF](https://help.aliyun.com/zh/sls/conditional-expressions) | [嵌套子查询](https://help.aliyun.com/zh/sls/nested-subquery) | [数组](https://help.aliyun.com/zh/sls/array-functions-and-operators) | [二进制函数](https://help.aliyun.com/zh/sls/binary-functions) | [位运算](https://help.aliyun.com/zh/sls/bitwise-functions) | [同比和环比函数](https://help.aliyun.com/zh/sls/interval-valued-and-periodicity-valued-comparison-functions) |
| [比较运算符](https://help.aliyun.com/zh/sls/comparison-operators) | [Lambda函数](https://help.aliyun.com/zh/sls/lambda-expressions) | [逻辑函数](https://help.aliyun.com/zh/sls/logical-operators) | [列的别名](https://help.aliyun.com/zh/sls/column-aliases) | [MySQL外表关联](https://help.aliyun.com/zh/sls/join-queries-on-a-logstore-and-a-mysql-database) | [空间几何函数](https://help.aliyun.com/zh/sls/geospatial-functions) |
| [地理函数](https://help.aliyun.com/zh/sls/geo-functions) | [Join语法](https://help.aliyun.com/zh/sls/join-clause) | [unnest语法](https://help.aliyun.com/zh/sls/unnest-clause) | [insert语法](https://help.aliyun.com/zh/sls/insert-into-clause) | [电话号码函数](https://help.aliyun.com/zh/sls/mobile-number-functions) |  |

使用SQL查询示例：

##### 可视化报表

SLS提供了报表可视化能力。结合SQL查询的结果可以很方便得将结果保存在Dashboard。

目前支持的可视化组件如下：

| [表格](https://help.aliyun.com/zh/sls/display-query-results-in-a-table) | [线图](https://help.aliyun.com/zh/sls/display-query-results-on-a-line-chart) | [柱状图](https://help.aliyun.com/zh/sls/display-query-results-on-a-column-chart) | [条形图](https://help.aliyun.com/zh/sls/display-query-results-on-a-bar-chart) | [饼图](https://help.aliyun.com/zh/sls/display-query-results-on-a-pie-chart) | [变更图](https://help.aliyun.com/zh/sls/user-guide/display-query-results-on-a-lifecycle-chart) | [气泡图](https://help.aliyun.com/zh/sls/user-guide/display-query-results-on-a-bubble-chart) |
| --- | --- | --- | --- | --- | --- | --- |
| [时间轴](https://help.aliyun.com/zh/sls/display-query-results-on-a-timeline-chart) | [地图](https://help.aliyun.com/zh/sls/gaud-map) | [流图](https://help.aliyun.com/zh/sls/display-query-results-on-a-flow-chart) | [桑基图](https://help.aliyun.com/zh/sls/display-query-results-in-a-sankey-diagram) | [词云](https://help.aliyun.com/zh/sls/display-query-results-on-a-word-cloud) | [中国行政区地图](https://help.aliyun.com/zh/sls/administrative-map-of-china) |  |

示例：

在查询结果的下方，可以选择对应的可视化。

#### 日志消费和投递

SLS提供了日志实时消费和投递到其他系统的功能。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4576581571/p969873.png)

##### 使用Spark、Flink、Storm进行日志流式消费

- 开源Flink消费， 参考 [链接](https://help.aliyun.com/zh/sls/use-flink-to-consume-data)
- Spark消费，参考 [链接](https://help.aliyun.com/zh/sls/use-spark-streaming-to-consume-log-data)
- Storm消费，参考 [链接](https://help.aliyun.com/zh/sls/use-loghub-storm-to-consume-log-data)

##### 将日志投递到OSS、MaxCompute

- 投递到MaxCompute数据仓库 参考 [链接](https://help.aliyun.com/zh/sls/user-guide/create-a-data-shipping-job-of-the-new-version-to-ship-data-to-maxcompute)
- 投递到AnalyticDB 参考 [链接](https://help.aliyun.com/zh/sls/ship-logs-to-analyticdb-for-mysql)
- 投递到OSS数据湖JSON格式，参考 [链接](https://help.aliyun.com/zh/sls/user-guide/json-format-3)CSV格式，参考 [链接](https://help.aliyun.com/zh/sls/user-guide/csv-format-3)Parquet格式，参考 [链接](https://help.aliyun.com/zh/sls/user-guide/parquet-format-3)ORC格式，参考 [链接](https://help.aliyun.com/zh/sls/user-guide/orc-format)

##### 使用数据加工处理日志

SLS数据加工提供了对日志进行实时行处理的能力，可以很方便地处理日志这种非结构化的场景

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4576581571/p969882.png)

##### 复制Logstore数据

通过数据加工，支持同地域、同账号、跨地域、跨账号下的logstore数据复制。

- 同地域Logstore复制 参考 [链接](https://help.aliyun.com/zh/sls/replicate-data-from-a-logstore)
- 跨地域Logstore复制 参考 [链接](https://help.aliyun.com/zh/sls/transfer-data-across-regions)

##### Logstore数据分发

通过数据加工，可以将Logstore中的日志根据条件分发给不同的Logstore。适合收集日志的时候，收集了多种日志到一个Logstore的场景。 参考 [链接](https://help.aliyun.com/zh/sls/distribute-data-to-multiple-destination-logstores)

## 故障排除

### Logtail支持哪些平台？

Linux支持如下版本的Linux x86-64（64位）服务器

- Alibaba Cloud Linux 2.1903
- RedHat Enterprise 6、7、8
- CentOS Linux 6、7、8
- Debian GNU/Linux 8、9、10
- Ubuntu 14.04、16.04、18.04、20.04
- SUSE Linux Enterprise Server 11、12、15
- OpenSUSE 15.1、15.2、42.3
- 其他基于glibc 2.5及以上版本的Linux操作系统

WindowsMicrosoft Windows Server 2008和Microsoft Windows 7支持X86和X86_64，其他版本仅支持X86_64。

- Microsoft Windows Server 2008
- Microsoft Windows Server 2012
- Microsoft Windows Server 2016
- Microsoft Windows Server 2019
- Microsoft Windows 7
- Microsoft Windows 10
- Microsoft Windows Server Version 1909
- Microsoft Windows Server Version 2004

### 如何排查Logtail采集日志问题？

Logtail采集问题排查思路如下所示。更多信息，请参见[Logtail排查简介](https://help.aliyun.com/zh/sls/what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs)。

1. 确认Logtail心跳状态为OK。
2. 确认日志文件中的日志在实时生成。
3. 确认Logtail配置中的正则表达式与日志内容相匹配。

## 方案卸载

### 卸载Logtail

- Linux系统执行以下命令卸载Logtail。`wget http://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/linux64/logtail.sh -O logtail.sh;chmod 755 logtail.sh;./logtail.sh uninstall`
- Windows系统以管理员身份运行Windows Powershell或cmd进入**logtail_installer**目录（安装包的解压目录），执行如下命令。`.\logtail_installer.exe uninstall`

卸载成功后，您的Logtail的安装目录会被删除，但仍有部分配置被保留在C:\LogtailData目录中，您可以根据实际情况进行手动删除。遗留信息包括：

- checkpoint：存放所有Logtail插件的Checkpoint信息。只有您使用了Logtail插件后，才会出现此文件。
- user_config.d：存放本地采集配置的目录。其中以.json结尾的文件会被视为采集配置，格式类似于/usr/local/ilogtail/user_log_config.json。
- logtail_check_point：存放Logtail主体部分的Checkpoint信息。
- users：存放您所配置的用户标识文件。

### 删除机器组

1. 在机器组列表中，单击目标机器组后面的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4576581571/p969889.png)图标，选择**删除**。
2. 在弹出的对话框中，单击**确认**。

### 删除Logstore

1. 在**日志存储 > 日志库**页签中，选择目标Logstore右侧的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4576581571/p969884.png)**> 删除**。**警告** Logstore一旦删除，其存储的日志数据将会被永久删除，不可恢复，请谨慎操作。
2. 在**删除**对话框中，单击**确认**。

### 删除Project

1. 在Project列表中，单击目标Project对应的**删除**。
2. 在**删除Project**面板中，选择删除原因，然后单击**确定**。

**警告** 删除Project后，其管理的所有日志数据及配置信息都会被永久释放，不可恢复。在删除Project前请慎重确认，避免数据丢失。

## 相关内容

- [日志服务](https://help.aliyun.com/product/28958.html?spm=5176.21213303.J_6028563670.9.29533eda8mXtqW)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-49（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
