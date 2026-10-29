<!-- source: https://help.aliyun.com/zh/well-architected/set-appropriate-alarms-for-different-levels-of-security-indicators -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2925783 -->

# 对不同等级的安全指标设置合适的告警

在安全监控中，告警通知机制的合理配置是避免“告警爆炸”（Alert Fatigue）的关键。不同等级的安全指标（如：Critical、High、Medium）需匹配不同的通知渠道、频率和响应策略。通过阿里云云监控（CloudMonitor）、SLS日志服务和事件中心（EventBridge）等产品，可实现告警的分级管理，确保关键威胁优先响应，同时降低低风险告警的干扰。

## 优先级

中

## 不推荐做法

- 所有告警使用相同通知方式，导致紧急事件被淹没。并且误报率高，导致告警疲劳。
- 未设置告警抑制规则，同一事件重复告警（如持续的 SSH 爆破尝试）。频繁通知影响团队工作效率，同时关键告警被低优先级事件掩盖。
- 告警阈值未基于历史基线动态调整。正常业务波动触发误报，或者真实威胁因阈值过高未被发现。

## 实施指南

1. 配置分级告警策略。**风险等级****适用场景****通知机制**Critical 级别直接威胁业务可用性或数据安全的事件。渠道：钉钉 + 短信 + 自动语音电话。频率：即时通知，每1小时去重一次。响应机制：自动触发 OOS 应急流程（如阻断 IP、终止实例）。High 级别需人工干预但非紧急的威胁。渠道：邮件 + 钉钉群组。频率：每 24 小时汇总一次。响应机制：生成工单并分配给安全分析师。Medium 级别潜在风险需定期审查的事件。渠道：无即时通知，仅记录日志。频率：每周生成审计报告。响应机制：由运维团队定期检查。
2. 配置告警规则。通过云监控设置分级告警。阿里云[云监控2.0](https://help.aliyun.com/zh/cms/cloudmonitor-2-0/what-is-cloud-monitor-2-0#undefined)是融合日志服务SLS、云监控CMS、应用实时监控服务ARMS等产品后全新升级的一站式可观测平台，您可以基于云监控2.0统一接入各种异构数据源，包括云服务、服务端应用和前端应用等等，并且实现统一的告警管理。具体告警规则的配置方式，请参见[告警规则](https://help.aliyun.com/zh/cms/cloudmonitor-2-0/alert-rules/)。通过SLS日志服务设置SPL查询告警。您可以编写SPL查询检测安全事件，并配置告警规则并绑定分级策略。详细操作，请参见[告警](https://help.aliyun.com/zh/sls/sls-alerting/)。

## 相关资源

### 相关实践

- [设置安全监控指标并分级](https://help.aliyun.com/zh/well-architected/set-safety-monitoring-indicators-and-classify-them)

---

> 原页面：https://help.aliyun.com/zh/well-architected/set-appropriate-alarms-for-different-levels-of-security-indicators（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
