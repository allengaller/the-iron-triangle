<!-- source: https://help.aliyun.com/zh/well-architected/centralized-log-analysis -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2925781 -->

# 进行集中化的日志分析

在完成日志的集中化收集和归档后，日志分析是安全防护与业务优化的核心环节。通过统一的日志分析平台，企业可实现对日志数据的实时监控、异常检测、趋势分析和自动化告警，显著提升安全事件响应效率与业务洞察力。

## 优先级

中

## 不推荐做法

- 不同团队独立收集和分析日志，日志记录策略和日志格式不统一，导致日志无法全局联动检测，遗漏关键安全事件。
- 未按业务线、环境或安全类型分类日志，导致分析效率低下，无法快速定位关键日志（如支付失败、登录异常）。
- 缺乏自动化分析，依赖人工定期检查日志，无法应对实时威胁。比如：安全事件（如横向渗透）被延迟响应、业务瓶颈（如数据库慢查询）未及时优化等等。

## 实施指南

1. 参考最佳实践[进行集中化的日志收集和归档](https://help.aliyun.com/zh/well-architected/centralized-log-collection-and-archiving)，通过集中化的日志管理，实现日志数据的统一存储、实时分析、可视化呈现以及合规性审计。
2. 配置统一日志分析平台。在云上推荐您使用SLS日志服务，日志服务提供查询和分析功能，支持秒级查询十亿到千亿级别的日志，并支持通过SQL对查询结果进行统计分析。详情，请参见[查询与分析快速指引](https://help.aliyun.com/zh/sls/quick-guide-to-query-and-analysis)。如果您建设有自己的SEIM平台，您可以[使用函数计算（FC）通过Syslog协议投递日志到SIEM平台](https://help.aliyun.com/zh/sls/use-function-compute-fc-to-post-logs-through-the-syslog-protocol)，将云上日志投递收集到自己的SEIM平台进行统一的威胁检测分析。
3. 实现可视化。您可以通过以下方式实现可视化仪表盘，展示日志分析结果。您可以直接使用SLS的可视化能力，构建基于日志分析的可视化图表，满足基础需求。具体操作，请参见[可视化概述](https://help.aliyun.com/zh/sls/overview-of-visualization)。对于企业客户来说，除了日志的分析展示外，还希望统一分析展示基础设施指标（如 CPU 使用率）、应用性能指标（如 API 响应时间）等等。建议您建设统一可观测性平台，高效全面的收集系统运行状态数据，在此基础上将系统各个维度的指标统一展示，能够快速发现当前系统存在的风险。详细方案，请参见《[多账号全栈可观测大盘方案](https://help.aliyun.com/zh/well-architected/solution-154)》。
4. 告警配置。您可以通过以下方式实现监控报警。您可以直接使用SLS的[告警](https://help.aliyun.com/zh/sls/sls-alerting/)，实现基于日志分析的监控报警，比如开发同学通过告警功能监控应用运行的错误日志。对企业开户来说，在云原生时代，企业IT基础设施的规模越来越大，越来越多的系统和服务被部署在云环境中。为了监控这些复杂的IT环境，企业通常会选择使用异构监控系统，例如Prometheus、Grafana、Zabbix等，以获取更全面的监控数据。为避免异构系统带来的告警分散问题，该问题会导致企业很难全面了解其IT系统的告警状况，使得响应告警变得更加困难，同时也增加了人工管理的复杂性和工作量。建议您参考方案《[通过ARMS告警管理实现统一告警](https://help.aliyun.com/zh/well-architected/solution-263)》，以确保告警信息能够及时到达正确的人员，以便他们能够快速采取必要的措施来应对潜在的问题。

## 相关资源

### 相关实践

- [进行集中化的日志收集和归档](https://help.aliyun.com/zh/well-architected/centralized-log-collection-and-archiving)

### 相关方案

- 《[多账号全栈可观测大盘方案](https://help.aliyun.com/zh/well-architected/solution-154)》
- 《[通过ARMS告警管理实现统一告警](https://help.aliyun.com/zh/well-architected/solution-263)》
- 《[基于操作日志实现业务资源事件关联分析](https://help.aliyun.com/zh/well-architected/solution-38)》

### 相关文档

- [进行集中化的日志收集和归档](https://help.aliyun.com/zh/well-architected/centralized-log-collection-and-archiving)

---

> 原页面：https://help.aliyun.com/zh/well-architected/centralized-log-analysis（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
