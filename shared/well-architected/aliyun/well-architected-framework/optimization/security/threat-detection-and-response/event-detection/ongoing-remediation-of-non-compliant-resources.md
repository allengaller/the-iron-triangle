<!-- source: https://help.aliyun.com/zh/well-architected/ongoing-remediation-of-non-compliant-resources -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2925784 -->

# 持续对不合规资源进行修复

在云环境中，持续检测并修复不合规资源是保障安全、合规和成本效率的核心能力。阿里云提供云治理中心、配置审计（Config）等产品，支持对资源的全生命周期治理。通过自动化扫描与修复，企业可实现：

1. 实时发现不合规资源（如未加密的 OSS 存储、未关闭公网访问的 RDS）。
2. 自动化修复（如自动关闭公网访问）。
3. 跨账号统一治理（确保多账号环境中的配置一致性）。

## 优先级

中

## 不推荐做法

- 依赖人工巡检，无法覆盖实时变更。导致新创建的不合规资源（如开放 22 端口的 ECS）未被及时发现。
- 仅记录不合规状态，未自动修复。导致安全事件响应滞后，不合规资源长期存在，增加攻击面。
- 在多账号架构下，未统一管理多账号的资源合规性。导致合规审计时无法覆盖全组织资源。

## 实施指南

1. 持续风险巡检。使用云治理中心进行持续检测。云治理中心基于云卓越架构的设计原则和最佳实践，提供了云治理成熟度的全面检测。目前覆盖了260多项检测指标，基于阿里云实时数据，自动识别云上架构中的潜在风险。具体操作，请参见[治理成熟度检测](https://help.aliyun.com/zh/cgc/user-guide/cloud-governance-maturity-detection/)。同时，建议您开启治理报告订阅，定时获取云环境最新的治理检测结果，方便您及时查看和处理风险事项。详情，请参见[订阅治理报告](https://help.aliyun.com/zh/cgc/user-guide/set-check-items#bcf88aa4211vb)。使用配置审计（Config）持续检测不合规资源。合规包是配置审计根据合规场景定制的一组规则的集合，您可以根据自身场景，使用合规包，快速创建合规规则，对云上资源进行检测。目前阿里云提供的合规包列表，请参见[合规包模板](https://help.aliyun.com/zh/document_detail/312285.html)。您也可以创建合规规则，来判断资源的某一个配置项是否合规。规则的介绍，请参见[规则的定义及运行原理](https://help.aliyun.com/zh/document_detail/128273.html)。除了阿里云提供的规则模板外，您也可以使用函数计算等方式自定义规则的检测逻辑，比如，企业使用ECS主机，通常要求ECS主机实例的系统漏洞尽快修复从而避免收到安全攻击，或者保持一致的系统、软件配置基线，比如：主机内核参数、主机时区、软件版本等等。因此，您可以通过函数计算自定义合规规则，对主机的数据平面进行检测。具体操作，请参见《[通过配置审计和函数计算实现云主机风险巡检](https://help.aliyun.com/zh/well-architected/solution-201)》。
2. 统一收集和分析资源不合规事件。您可以使用配置审计的[投递功能](https://help.aliyun.com/zh/document_detail/310163.html)，将资源的不合规事件统一投递到指定的OSS存储空间或者SLS Logstore中。在多账号架构下，您可以参考方案《[多账号配置统一合规审计](https://help.aliyun.com/zh/well-architected/solution-43)》，将企业所有账号的资源事件，统一归集到您的安全或审计账号中，实现中心化的持续监测所有业务资源的合规情况。
3. 制定修复措施。针对云治理中心治理成熟度检测结果中的部分风险项，您可以通过快速修复功能一键将其修复。具体操作，请参见[快速修复风险项](https://help.aliyun.com/zh/cgc/user-guide/quickly-fix-risk-items)。对于不支持快速修复的检测项，云治理中心提供了[辅助决策](https://help.aliyun.com/zh/cgc/user-guide/auxiliary-decision-making)功能，提供更详细、更多维度的资源数据，以此辅助您快速确定治理策略。针对配置审计合规规则评估为不合规的资源，您可以使用配置审计提供的修正能力，当规则检测到不合规资源时，可以自动执行修正，快速纠正不合规配置，确保您云上IT系统实现自主持续的合规。详情，请参考[修正设置](https://help.aliyun.com/zh/document_detail/159473.html)。

## 相关资源

### 相关实践

- [进行集中化的日志收集和归档](https://help.aliyun.com/zh/well-architected/centralized-log-collection-and-archiving)

### 相关方案

- 《[通过配置审计和函数计算实现云主机风险巡检](https://help.aliyun.com/zh/well-architected/solution-201)》
- 《[多账号配置统一合规审计](https://help.aliyun.com/zh/well-architected/solution-43)》
- 《[多账号容器集群风险审计](https://help.aliyun.com/zh/well-architected/solution-121)》

---

> 原页面：https://help.aliyun.com/zh/well-architected/ongoing-remediation-of-non-compliant-resources（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
