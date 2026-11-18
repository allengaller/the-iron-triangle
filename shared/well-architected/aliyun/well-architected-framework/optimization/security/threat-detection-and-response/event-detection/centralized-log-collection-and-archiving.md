<!-- source: https://help.aliyun.com/zh/well-architected/centralized-log-collection-and-archiving -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2925780 -->

# 进行集中化的日志收集和归档

在云原生时代，建议企业优先选择云厂商提供的托管日志服务（如阿里云SLS日志服务），而非自建或自行维护日志收集、存储和分析系统。通过集中化的日志管理，可实现日志数据的统一存储、实时分析、可视化呈现以及合规性审计，显著降低安全风险和运维复杂度。

## 优先级

中

## 不推荐做法

- 在多账号架构下，日志分散在各个账号中，安全审计时需要逐个账号排查，效率低下。
- 日志未分类存储或者长期保留，导致存储成本上升。
- 日志访问权限未分级，比如全员可读写，导致敏感日志被越权访问，同时也无法满足ISO或者等保的审计要求。

## 实施指南

1. 集中化日志收集和归档。对于云上的操作日志，您可以使用操作审计的[跟踪功能](https://help.aliyun.com/zh/actiontrail/user-guide/trail-overview)，将日志保存到指定的OSS存储空间或者SLS Logstore中，以便后期分析和长期存储。在多账号架构下，您可以参考方案《[多账号操作日志统一归集与审计](https://help.aliyun.com/zh/well-architected/solution-37)》，将企业所有账号的操作审计日志，统一归集到您的安全或审计账号中，进行统一的分析和存储。对于云上资源数据：资源快照、配置变更历史、合规快照和不合规事件，您可以使用配置审计的[投递功能](https://help.aliyun.com/zh/document_detail/310163.html)，将这些资源数据统一投递到指定的OSS存储空间或者SLS Logstore中。在多账号架构下，您可以参考方案《[多账号配置统一合规审计](https://help.aliyun.com/zh/well-architected/solution-43)》，将企业所有账号的资源数据，统一归集到您的安全或审计账号中，实现中心化的持续监测所有业务资源的合规情况。对于其他云产品的访问日志或者审计日志，比如：OSS访问日志、VPC流日志、RDS慢日志和审计日志等等，建议您使用[SLS日志审计服务](https://help.aliyun.com/zh/sls/new-log-audit-service/)，通过多日志项目中心管理日志数据，从而将云产品日志或运行时日志中心化汇总、查询、统计、分析。对于您的应用和软件日志，建议您参考并使用方案《[基于日志服务实现企业级统一日志归集](https://help.aliyun.com/zh/well-architected/solution-49)》。
2. 存储分层。您可以使用日志服务提供的[智能分层存储功能](https://help.aliyun.com/zh/sls/data-tiered-storage-overview)，按需将数据进行热存储、低频存储和归档存储。降低您长周期存储的成本，并同时保证日志的查询、分析、可视化、告警、投递和加工等能力不受影响。对于更加长期需要冷归档的数据，您可以使用日志服务的数据投递功能，[将日志投递到OSS存储空间中](https://help.aliyun.com/zh/sls/shipping-logs-to-oss-new-version/)，该OSS存储空间，您可以选择冷归档或者深度冷归档的存储类型，从而进一步降低存储成本，更多OSS存储类型，请参考[存储类型](https://help.aliyun.com/zh/oss/user-guide/overview-53/)。
3. 参考最佳实践[基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)，限制员工的日志访问权限，保证权限最小可用，避免敏感日志被越权访问。

## 相关资源

### 相关实践

- [基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)

### 相关方案

- 《[多账号操作日志统一归集与审计](https://help.aliyun.com/zh/well-architected/solution-37)》
- 《[多账号配置统一合规审计](https://help.aliyun.com/zh/well-architected/solution-43)》
- 《[基于日志服务实现企业级统一日志归集](https://help.aliyun.com/zh/well-architected/solution-49)》
- 《[多账号容器集群日志统一归集](https://help.aliyun.com/zh/well-architected/solution-120)》

---

> 原页面：https://help.aliyun.com/zh/well-architected/centralized-log-collection-and-archiving（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
