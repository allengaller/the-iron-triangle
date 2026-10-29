<!-- source: https://help.aliyun.com/zh/well-architected/set-safety-monitoring-indicators-and-classify-them -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2925782 -->

# 设置安全监控指标并分级

在云原生环境中，安全监控指标是保障业务安全运行的核心组件。与传统的系统稳定性、性能监控指标不同，安全监控需聚焦威胁检测、异常行为识别和合规性验证。通过分级管理安全指标（如关键、重要、一般），企业可实现：

1. 优先响应高风险事件（如暴力破解、数据泄露）。
2. 降低误报率（通过分级过滤无关告警）。
3. 满足合规要求（如等保2.0的安全事件记录与处置）。

阿里云提供云监控（CloudMonitor）、SLS日志服务、云安全中心（Security Center） 等工具，支持从基础设施到应用层的全链路安全指标监控。

## 优先级

中

## 不推荐做法

- 仅监控系统性能指标，忽略安全相关指标（如登录失败次数、异常 API 调用），导致无法及时发现横向渗透攻击等安全事件。
- 安全事件未定义触发条件（如登录失败次数阈值），导致异常行为（如 SQL 注入攻击）未及时告警、安全事件响应滞后，从而扩大损失。
- 所有安全事件统一告警级别，导致高风险事件被淹没，运维团队无法快速响应紧急事件。

## 实施指南

1. 定义安全监控指标分类。关键指标（Critical）：直接影响业务可用性或数据安全的事件。比如：SSH 登录失败次数/分钟、数据库敏感操作（如 `DROP TABLE`）、云安全中心高危漏洞等。重要指标（High）：需人工干预但非紧急的威胁。比如：跨账号访问RAM角色、OSS 敏感文件公开访问、SQL 注入攻击尝试等。一般指标（Medium）：潜在风险需定期审查的事件。比如：用户权限变更（如授予RAM Admin权限）、非工作时间的登录尝试等。
2. 配置安全监控指标。对于账号内操作异常事件，比如：异常IP登录、多次登录尝试失败等，您可以使用操作审计的[事件告警](https://help.aliyun.com/zh/actiontrail/user-guide/overview-3)，其内置了常用的告警规则模板，您可以快速对相应的安全指标进行监控。详细方案，请参考《[账号异常操作监测方案](https://help.aliyun.com/zh/well-architected/solution-127)》。对于主机漏洞、AK泄露、恶意挖矿等涉及基础设施的安全事件，推荐您使用[云安全中心](https://help.aliyun.com/zh/security-center/what-is-security-center)，通过其实时检测能力，实现快速且有效地处置安全事件。如果您希望对多个安全事件的异构源进行统一的审计分析，比如上面所述的账号异常操作、云安全中心安全事件，以及数据库敏感操作、OSS访问日志等，推荐您使用SLS[日志审计服务](https://help.aliyun.com/zh/sls/new-log-audit-service/)，您可以[将操作审计日志](https://help.aliyun.com/zh/sls/log-audit-access-operation-audit-access-log)、[将云安全中心日志](https://help.aliyun.com/zh/sls/log-audit-access-cloud-security-center-access-log)、OSS访问日志、数据库审计日志等统一接入到日志审计服务中，利用其自带的查询分析、可视化报表和告警的能力，帮助您快速配置并监控安全指标。

## 相关资源

### 相关实践

- [进行集中化的日志收集和归档](https://help.aliyun.com/zh/well-architected/centralized-log-collection-and-archiving)
- [进行集中化的日志分析](https://help.aliyun.com/zh/well-architected/centralized-log-analysis)

### 相关方案

- 《[账号异常操作监测方案](https://help.aliyun.com/zh/well-architected/solution-127)》

### 相关文档

- [将OSS Bucket访问日志接入日志审计](https://help.aliyun.com/zh/sls/log-audit-access-oss-access-logs)
- [将云安全中心日志接入日志审计服务](https://help.aliyun.com/zh/sls/log-audit-access-cloud-security-center-access-log)
- [将操作审计日志接入日志审计](https://help.aliyun.com/zh/sls/log-audit-access-operation-audit-access-log)

---

> 原页面：https://help.aliyun.com/zh/well-architected/set-safety-monitoring-indicators-and-classify-them（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
