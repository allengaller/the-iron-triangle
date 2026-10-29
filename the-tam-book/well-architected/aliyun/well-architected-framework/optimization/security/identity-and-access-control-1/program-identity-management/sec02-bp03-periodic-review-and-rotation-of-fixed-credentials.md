<!-- source: https://help.aliyun.com/zh/well-architected/sec02-bp03-periodic-review-and-rotation-of-fixed-credentials -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706139 -->

# 定期审查和轮转固定凭据

我们将一旦创建出来，在删除之前都是永久有效的凭据称之为固定凭据，比如给RAM用户或云账号的Root身份创建的AccessKey、数据库的用户名密码、大模型的API Key，都属于固定凭据。不合理地使用固定凭据会造成很多风险，定期审查和轮转固定凭据，可以有效降低风险。

## 优先级

高

## 不推荐做法

- 不审计固定凭证的使用情况。
- 长期使用固定凭据，不进行轮转。

## 实施指南

1. 定期审查固定凭据。建议您重点关注以下几种固定凭据的使用情况：异常调用情况，比如出现大量调用失败、存在非可信IP来源的调用。此时固定凭据有发生泄露的风险，建议您根据调用日志进一步分析定位，如有泄露风险，请尽快通过轮转等手段进行应急处理。多个工作负载或者环境共用一个固定凭据，违反了单一职责原则。请参见[为不同的工作负载和环境分配不同的凭据](https://help.aliyun.com/zh/well-architected/sec02-bp01-assign-different-credentials-to-different-workloads-and-environments)。过度授权导致固定凭据持有过大权限。请尽快进行权限收敛，删除未使用到的闲置权限，保证最小化授权。固定凭据长期没有访问记录，存在闲置情况。请根据实际情况，对闲置的凭据进行禁用、删除等处理措施。其中，针对固定凭据AccessKey，建议您采取以下措施进行风险检测：通过[云治理中心](https://help.aliyun.com/zh/cgc/product-overview/what-is-cloud-governance-center)进行配置巡检，比如：是否存在闲置的AccessKey、是否存在长时间未轮转的AccessKey等等。通过云安全中心检测GitHub开源代码中的AccessKey泄露。云安全中心支持实时检测GitHub平台公开源代码（多为企业员工私自上传并不小心公开）中是否含有AccessKey信息，在发现AccessKey泄露时向您发送通知，帮助您及时发现外泄的风险。持续检测AccessKey异常调用。通过操作审计配置异常告警。操作审计服务提供了内置告警，您可以在操作审计控制台进行启用，以便能在出现AccessKey异常调用时收到通知。具体操作，请参见[设置事件告警](https://help.aliyun.com/zh/actiontrail/user-guide/enable-and-configure-alerts)。基于历史行为检测AccessKey异常调用。操作审计服务提供的审计事件洞察（Insights事件）功能，可以基于历史行为分析调用率异常的AccessKey，及时发现异常行为。详情，请参见[Insights事件概览](https://help.aliyun.com/zh/actiontrail/user-guide/overview-of-insights-events)。如果发现您的AccessKey存在泄露风险或者已经发生泄露，请尽快进行应急处置。请参见《[AccessKey风险检测与泄露应急方案](https://help.aliyun.com/zh/well-architected/solution-271)》，获取更多风险检测和应急处理措施。
2. 定期轮转固定凭据。建议您每半年或一年轮转一次固定凭据，如果您已经落地了最佳实践[对固定凭据进行集中化管控](https://help.aliyun.com/zh/well-architected/sec02-bp05-centralized-control-of-fixed-credentials)，那么凭据的轮转对凭据使用方将是无感的，因此您甚至可以将轮转周期缩短为7-90天。通过凭据的轮转，保证在您无意泄露了凭据的情况下，能够快速缩短凭据的暴露时间。在云上，推荐您使用密钥管理服务KMS，集中托管固定凭据，通过产品化的手段，自动定期进行固定凭据的轮转。更多信息，请参见[凭据管理概述](https://help.aliyun.com/zh/kms/key-management-service/user-guide/secret-management-overview)。其中，针对固定凭据AccessKey，推荐您优先使用临时凭据STS Token代替AccessKey的使用，最佳实践，请参见[使用临时凭据替代固定凭据](https://help.aliyun.com/zh/well-architected/sec02-bp02-prefer-temporary-credentials)。对于必须使用AccessKey的场景，请参考《[通过KMS实现固定AccessKey的集中管控](https://help.aliyun.com/zh/well-architected/solution-237)》，安全的存储和使用AccessKey。

## 相关资源

### 相关实践

- [对固定凭据进行集中化管控](https://help.aliyun.com/zh/well-architected/sec02-bp05-centralized-control-of-fixed-credentials)
- [使用临时凭据替代固定凭据](https://help.aliyun.com/zh/well-architected/sec02-bp02-prefer-temporary-credentials)
- [为不同的工作负载和环境分配不同的凭据](https://help.aliyun.com/zh/well-architected/sec02-bp01-assign-different-credentials-to-different-workloads-and-environments)
- [基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)

### 相关方案

- 《[AccessKey风险检测与泄露应急方案](https://help.aliyun.com/zh/well-architected/solution-271)》
- 《[通过KMS实现固定AccessKey的集中管控](https://help.aliyun.com/zh/well-architected/solution-237)》

---

> 原页面：https://help.aliyun.com/zh/well-architected/sec02-bp03-periodic-review-and-rotation-of-fixed-credentials（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
