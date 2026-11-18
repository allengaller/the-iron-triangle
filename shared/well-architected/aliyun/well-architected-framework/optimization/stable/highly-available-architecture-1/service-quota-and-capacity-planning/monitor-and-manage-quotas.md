<!-- source: https://help.aliyun.com/zh/well-architected/monitor-and-manage-quotas -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2968699 -->

# 监控和管理配额

随着云上业务的持续增长，服务配额（Service Quotas）的管理成为保障系统稳定运行的重要环节。阿里云上的每个服务都存在默认的资源使用上限（如ECS实例数、SLB连接数、RDS实例数等），如果这些配额未被有效监控和管理，可能会导致服务中断、自动扩缩失败、性能下降等问题。

## 优先级

中

## 不推荐做法

- 没有配置配额使用监控。
- 没有为硬性限制（如 API 调用频率）设置告警。
- 配置告警但无响应流程。
- 只监控部分服务配额，忽视其他服务。
- 忽略多地域部署下的配额一致性。
- 假设配额申请可以快速完成。

## 实施指南

1. 获取当前资源使用情况（如实例数、连接数等）
2. 获取服务配额信息：使用阿里云配额中心查阅云服务文档使用CLI或者API查询配额限制
3. 设置配额监控与告警在配额中心针对特定的配额创建监控告警（如使用率、剩余可用率、配额用量等）
4. **定期检查配额历史记录**，了解资源增长趋势
5. **发现配额不足时，提交工单申请提高配额**

## 相关资源

### 相关文档

- [Alibaba Well-Archited Framwork稳定性支柱](https://help.aliyun.com/zh/well-architected/overview-7)
- [配额告警](https://help.aliyun.com/zh/quota-center/user-guide/quota-alerts/)
- [配额模板](https://help.aliyun.com/zh/quota-center/user-guide/quota-templates/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/monitor-and-manage-quotas（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
