<!-- source: https://help.aliyun.com/zh/well-architected/solution-50 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929430 -->

# 基于日志服务实现企业级统一监控

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972313.png)

随着企业信息化的发展，面向云的IT基础设施越来越普遍，如何解决超大软件系统监控问题，成为IT稳定性保障的关键环节。 本方案主要介绍如何使用SLS 对阿里云、企业自有IDC以及第三方云场景下，进行企业级的监控方案。

## 方案优势

### 自底向上全栈的监控能力

依托于MetricStore/Logstore存储能力，SLS提供了自底向上全栈的监控能力。客户只需要使用一套产品即可完成全栈监控，免去了维护多套监控系统的麻烦。

### 多种网络场景的监控能力

客户只需要使用一套产品即可完成多种网络场景下的监控覆盖。包括多账号场景下的统一监控、混合云场景、多云场景都可以用一套产品支持。

## 客户场景

### 统一告警事件管理

#### 场景描述

客户在云上会有多个业务部署形态，也会用到多款不同的云产品来支撑业务。而这些云产品都会有相应的告警事件触发。客户希望能够把这些告警事件统一管理。

#### 适用客户

- 多个告警事件源
- 统一事件告警

### 统一监控管理

#### 场景描述

客户在云上有多套监控系统。比如常见的：云监控、ARMS、自建的三方监控软件等。客户希望把这些监控系统的数据统一汇集到一处。

#### 适用客户

- 多套监控系统
- 统一监控管理

## 方案架构

依托于MetricStore/Logstore存储能力，SLS提供了从底向上全栈的监控能力。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972323.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 日志服务SLS | [日志服务SLS](https://help.aliyun.com/product/28958.html)是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/sls/billing-overview)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 容器服务ACK | [容器服务Kubernetes版](https://help.aliyun.com/product/85222.html)（Alibaba Cloud Container Service for Kubernetes，简称容器服务ACK）提供高性能可伸缩的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ack/billing-information)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 时序库（MetricStore） | 时序库（MetricStore）是日志服务中时序数据的采集、存储和查询单元。 |
| 日志库（Logstore） | 日志库（Logstore）是日志服务中日志数据的采集、存储和查询单元。 |

## 安全性

### SLS监控管理员角色

这个角色需要完成SLS相关配置。日志服务提供权限助手功能，简化日志服务相关的RAM权限策略配置。具体配置请参见[配置权限助手](https://help.aliyun.com/zh/sls/configure-the-permission-assistant-feature)。

### K8S监控配置角色

需要完成相关组件接入，包括K8S指标监控接入，事件监控，主机监控接入等。容器服务ACK提供的系统授权策略的授权粒度比较粗，如果这种粗粒度授权策略不能满足您的需要，那么您可以创建自定义授权策略。具体请参见[自定义RAM授权策略](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy)。

## 注意事项

### 日志服务基础资源的使用限制

包括Project的数量上限、Logstore数量上限、机器组数量上限等等。具体请参考[基础资源](https://help.aliyun.com/zh/sls/basic-resources)。

### 日志服务告警限制

告警监控、告警管理、通知等方面的限制。具体请参考[告警](https://help.aliyun.com/zh/sls/alerting-1)。

### 开服地域

地域是指物理的数据中心，Project创建成功后不能更换地域。在实施本方案之前需要考虑当前产品支持哪些地域

具体请参考[开服地域](https://help.aliyun.com/zh/sls/sls-supported-regions1)。

## 实施步骤

### 实施准备

1. 在阿里云官网已经开通 SLS服务
2. 确保现有的网络环境，可以连通到阿里云网络。网络联通说明: 本方案要求现有的需要采集指标或日志的设备能够联通阿里云的网络环境，目前SLS支持的Region请[查看Region列表](https://help.aliyun.com/zh/sls/endpoints)。对于IDC或者其他云厂商的场景，如果是进行POC的话可以优先使用SLS的公网地址进行 日志收集;如果是生产使用建议搭建相应的专线接入阿里云网络，以保障数据传输的可靠性。

### 操作步骤

### 汇总

| 监控层次 | 监控类型 | 接入方式 | 接入说明 |
| --- | --- | --- | --- |
| IAAS层 | k8s指标监控 | 配置即可接入（Promethues Remote Write） | 支持Pod、Deployment、SatefulSet、k8s核心组件指标监控，具体配置方法 [链接](https://help.aliyun.com/zh/sls/collect-metric-data-from-prometheus-by-using-the-remote-write-protocol) |
| k8s事件监控 | 配置即可接入（需部署k8s npd组件） | 容器的重启、Crash、OOM等监控，关键组件异常监控[链接](https://help.aliyun.com/zh/sls/create-and-use-an-event-center) |  |
| 主机监控 | logtail采集 | 支持CPU、Mem、Disk、Net、System等相关指标采集[链接](https://help.aliyun.com/zh/sls/collect-metric-data-from-hosts) |  |
| PAAS层 | MySQL | logtail采集 | 配置方案见 [链接](https://help.aliyun.com/zh/sls/collect-metric-data-from-mysql-servers) |
| MongoDB | logtail采集 | 配置方案见 [链接](https://help.aliyun.com/zh/sls/collect-metric-data-from-mongodb-databases) |  |
| Redis | logtail采集 | 配置方案见 [链接](https://help.aliyun.com/zh/sls/collect-metric-data-from-redis-servers) |  |
| ClickHouse | logtail采集 | 配置方案见 [链接](https://help.aliyun.com/zh/sls/collect-metric-data-from-clickhouse-servers) |  |
| Kafka | logtail采集 | 配置方案见 [链接](https://help.aliyun.com/zh/sls/collect-metric-data-from-kafka-servers) |  |
| Nginx | logtail采集 | 配置方案见 [链接](https://help.aliyun.com/zh/sls/collect-metric-data-from-nginx-servers) |  |
| ElasticSearch | logtail采集 | 配置方案见 [链接](https://help.aliyun.com/zh/sls/collect-metric-data-from-elasticsearch-servers) |  |
| 阿里云云产品 | 配置即可接入 | 支持常见的云产品（ecs、rds等）指标接入[链接](https://help.aliyun.com/zh/sls/import-metric-data-from-cloudmonitor-to-log-service) |  |
| 应用层 | 应用Trace | 业务代码集成（部分支持无侵入） | 支持常见语言SDK[Java Trace接入](https://help.aliyun.com/zh/sls/import-trace-data-from-java-applications-to-log-service-by-using-opentelemetry-sdk-for-java) （支持无侵入接入）[Golang Trace接入](https://help.aliyun.com/zh/sls/import-trace-data-from-golang-applications-to-log-service-by-using-opentelemetry-sdk-for-golang)[Python Trace接入](https://help.aliyun.com/zh/sls/import-trace-data-from-python-applications-to-log-service-by-using-opentelemetry-sdk-for-python)[NodeJS Trace接入](https://help.aliyun.com/zh/sls/import-trace-data-from-node-js-applications-to-log-service-by-using-opentelemetry-sdk-for-javascript)[C# Trace接入](https://help.aliyun.com/zh/sls/import-trace-data-from-csharp-applications-to-log-service-by-using-opentelemetry-sdk-for-dotnet)[Rust Trace接入](https://help.aliyun.com/zh/sls/import-trace-data-from-rust-applications-to-log-service-by-using-opentelemetry-sdk-for-rust)[Ruby Trace接入](https://help.aliyun.com/zh/sls/import-trace-data-from-ruby-applications-to-log-service-by-using-opentelemetry-sdk-for-ruby) |
| 现有Trace集成 | 配置即可接入 | OpenCensus Trace 数据接入 参考 [链接](https://help.aliyun.com/zh/sls/import-trace-data-from-opencensus-to-log-service)Zipkin Trace数据接入 参考 [链接](https://help.aliyun.com/zh/sls/import-trace-data-from-zipkin-to-log-service)SkyWalking Trace数据接入 参考 [链接](https://help.aliyun.com/zh/sls/import-trace-data-from-skywalking)Jaeger Trace数据接入 参考 [链接](https://help.aliyun.com/zh/sls/import-trace-data-from-jaeger-to-log-service) |  |
| JVM指标监控 | 配置即可接入 | 配置方式参考 [链接](https://help.aliyun.com/zh/sls/collect-metric-data-from-java-applications-or-tomcat-servers) |  |
| 自定义指标 | 开发接入/SLS数据加工/SLS ScheduleSQL | 支持使用Python、Java、Go等语言，向SLS MetricStore写入自定义的监控数据。 参考 [链接](https://help.aliyun.com/zh/sls/use-an-sdk-to-collect-metrics) |  |
| 业务层 | 业务接入层分析 | 配置即可接入 | Nginx访问日志分析 [链接](https://help.aliyun.com/zh/sls/configure-nginx-log-center)ALB访问日志分析 [链接](https://help.aliyun.com/zh/sls/enable-data-collection-1)SLB访问日志分析 [链接](https://help.aliyun.com/zh/sls/enable-the-data-collection-feature)Kubernetes Ingress日志分析 [链接](https://help.aliyun.com/zh/sls/configure-ingress-log-center) |
| 自定义指标 | 开发接入/SLS数据加工/SLS ScheduleSQL | 业务日志中的日志，通过计算转换为指标使用SLS数据加工转换日志为指标 [链接](https://developer.aliyun.com/article/782905) |  |

### 部分监控效果展示

k8s 接入Prometheus后指标查询展示：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972320.png)

k8s 接入Prometheus后使用Grafana查询：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972321.png)

k8s事件中心：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972324.png)

主机监控：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972325.png)

Redis监控：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972331.png)

云产品 - ecs指标导入：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972326.png)

SLB日志中心：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972327.png)

应用JVM监控：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972332.png)

应用Trace接入：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972328.png)

## 故障排除

### 告警常见问题

介绍在使用SLS用来做告警时，设置告警会遇到的常见问题及处理方法。具体可参考[告警常见问题](https://help.aliyun.com/zh/sls/faq-about-alerts)。

### 日志服务中的数据如何实现低成本存储

您可以通过如下方式实现数据的低成本存储。

- 通过日志服务Scheduled SQL功能对全量、细粒度的数据进行聚合存储，汇总为存储大小、精度适合的数据，长期存储。更多信息，请参见[Scheduled SQL](https://help.aliyun.com/zh/sls/how-scheduled-sql-works)。
- 通过日志服务投递功能将数据投递到[阿里云OSS](https://help.aliyun.com/zh/oss/user-guide/what-is-oss)中进行低成本存储。OSS提供标准、低频访问、归档、冷归档四种存储类型，全面覆盖从热到冷的各种数据存储场景。

### 数据采集常见问题

会介绍使用Logtail采集日志过程中遇到的各种常见故障应对策略。具体可参考[Logtail基本问题](https://help.aliyun.com/zh/sls/faq-about-logtail)。

## 方案卸载

### 卸载Logtail

- Linux系统执行以下命令卸载Logtail。`wget http://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/linux64/logtail.sh -O logtail.sh;chmod 755 logtail.sh;./logtail.sh uninstall`
- Windows系统以管理员身份运行Windows Powershell或cmd进入**logtail_installer**目录（安装包的解压目录），执行如下命令。`.\logtail_installer.exe uninstall`卸载成功后，您的Logtail的安装目录会被删除，但仍有部分配置被保留在C:\LogtailData目录中，您可以根据实际情况进行手动删除。遗留信息包括：checkpoint：存放所有Logtail插件的Checkpoint信息。只有您使用了Logtail插件后，才会出现此文件。user_config.d：存放本地采集配置的目录。其中以.json结尾的文件会被视为采集配置，格式类似于/usr/local/ilogtail/user_log_config.json。logtail_check_point：存放Logtail主体部分的Checkpoint信息。users：存放您所配置的用户标识文件。

### 删除机器组

1. 在机器组列表中，单击目标机器组后面的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972329.png)图标，选择**删除**。
2. 在弹出的对话框中，单击**确认**。

### 删除Logstore

1. 在**日志存储 > 日志库**页签中，选择目标Logstore右侧的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5086581571/p972330.png)**> 删除**。
2. 在**删除**对话框中，单击**确认**。

### 删除Project

1. 在Project列表中，单击目标Project对应的**删除**。
2. 在**删除Project**面板中，选择删除原因，然后单击**确定**。

> **警告** 删除Project后，其管理的所有日志数据及配置信息都会被永久释放，不可恢复。在删除Project前请慎重确认，避免数据丢失。

## 相关内容

[日志服务最佳实践](https://help.aliyun.com/zh/sls/best-practices-7)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-50（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
