<!-- source: https://help.aliyun.com/zh/well-architected/automated-management-of-quotas -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2968700 -->

# 自动化管理配额

在云上环境中，服务配额（Service Quotas）是保障系统稳定运行的重要因素。阿里云为每项服务设置了默认的资源使用上限，例如ECS实例数、RDS连接数、API调用频率等。如果这些配额未被有效监控和管理，可能会导致服务中断、自动扩缩失败、性能下降等问题。

## 优先级

中

## 不推荐做法

- 未根据工作负载需求调整配额。
- 使用过时的方法（如电子表格）手动跟踪配额。
- 只按固定周期更新配额。
- 缺乏查看配额及申请提高的标准化流程。

## 实施指南

1. **部署配额自动监控系统**使用阿里云配额中心 + CloudMonitor 设置阈值告警；
2. 为API速率创建全局配额项告警使用阿里云配额中心，监控某个产品中全部API的速率配额；
3. 自动化配额申请机制对于可自动审批的配额，设置自动提交流程；对于需人工审批的配额，设置提醒机制；
4. 定期评估配额策略检查配额使用趋势，优化配额申请策略；评估是否需要调整配额阈值或扩容策略

## 相关资源

### 相关文档

- [Alibaba Well-Archited Framwork稳定性支柱](https://help.aliyun.com/zh/well-architected/overview-7)
- [配额告警](https://help.aliyun.com/zh/quota-center/user-guide/quota-alerts/)
- [为API速率配额创建全局配额项告警](https://help.aliyun.com/zh/quota-center/use-cases/create-an-alert-for-api-rate-limits)

---

> 原页面：https://help.aliyun.com/zh/well-architected/automated-management-of-quotas（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
