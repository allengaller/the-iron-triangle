<!-- source: https://help.aliyun.com/zh/well-architected/best-practices-for-risk-detection-of-default-configurations-on-cloud -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2573787 -->

# 云平台及产品默认配置风险检测最佳实践

## 梳理企业常用云产品和使用方式

企业应统计阿里云账号下开通的云产品资源，并做好分类。同时调研其使用方式，从安全层面关注的使用方式的影响主要是该云服务是公网访问还是私网访问，是共享资源还是独享资源，以及该云服务应用和存储的数据类别及重要程度等。以便在后续的安全风险评估中，根据云产品实际应用场景来确定给出的风险建议。

建议企业按照以下分类方式对云资源进行分类：

| 资源类别 | 示例 | 使用方式 | 是否涉及重要数据 |
| --- | --- | --- | --- |
| 网络 | SLB、EIP、VPC、CEN…… | 私网访问和公网访问 | 否 |
| 数据库及存储 | RDS、OSS | 私网访问和公网访问 | 是 |
| 计算 | ECS、ACK | 私网访问 | 是 |
| 安全 | WAF、云防火墙CFW | 公网访问 | 否 |

## 选择安全评估标准

针对云平台和云服务的安全评估标准分为两个层面，第一个层面是基准，第二个层面是策略。策略是达成一系列基准的检测方法，每个云平台的安全评估策略略有不同，但可以遵循同一个基准执行相关的检测策略。这也是大多数企业多云客户的选择方式。

推荐企业参考的基准模板如下：

- ISO 27001
- 阿里云安全最佳实践

通常情况下，企业需要结合推荐的基准模板结合自身业务进行梳理和融合，如金融行业可在基准模板上再叠加PCI DSS、等级保护、GDPR等基准，融合成为适合企业在云环境的统一标准安全评估基准。

## 使用工具自动化检测扫描配置风险

在确定企业的安全评估基准后，需要通过一系列的策略来检测企业是否使用或开启相关的安全控制措施，以满足安全基准要求。并根据检测结果给出云平台整体的安全评估风险和建议。

- 使用云安全中心的[云安全态势管理概述](https://help.aliyun.com/zh/security-center/user-guide/cspm)功能对当前云账号下的默认配置及安全控制项进行检测。
- 通过查看云平台配置检查列表中的[检测策略](https://help.aliyun.com/zh/security-center/user-guide/cspm)，包含了阿里云身份权限管理检测策略、云产品配置最佳实践、合规检测策略等。

## 设定云资源安全评分

推荐企业采用定量的[安全评分](https://help.aliyun.com/zh/security-center/user-guide/asset-security-overview#section-moa-2is-or3)系统对云资源的整体安全风险进行可量化的评估，安全评分可以间接的反映结合安全评估基准，企业的安全控制措施的完备性。同时在多账号的客户架构中，安全评分也可用于更好地管理业务团队安全的使用云资源。

企业使用云安全中心的云平台配置检查功能完成自动化扫描后，会根据企业订阅的资产通过率进行打分，企业可根据评分情况及通过率查看每个策略详情，关联的资产、账号等。详细细节参考云安全中心的[安全评分](https://help.aliyun.com/zh/security-center/user-guide/asset-security-overview#section-moa-2is-or3)功能。

## 跟踪风险和定期评估

企业应定期对云服务环境进行风险评估，因为云资源的生命周期相比传统IDC要短，每次资源变更都有可能产生新的安全风险，需要企业结合上述最佳实践方式，设定定期评估的方案计划，以及通过[安全评分](https://help.aliyun.com/zh/security-center/user-guide/asset-security-overview#section-moa-2is-or3)来跟踪云服务的安全风险水平。

---

> 原页面：https://help.aliyun.com/zh/well-architected/best-practices-for-risk-detection-of-default-configurations-on-cloud（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
