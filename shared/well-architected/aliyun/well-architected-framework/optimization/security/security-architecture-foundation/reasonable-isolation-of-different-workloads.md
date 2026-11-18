<!-- source: https://help.aliyun.com/zh/well-architected/reasonable-isolation-of-different-workloads -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2909153 -->

# 对不同的工作负载进行合理隔离

强烈建议您在账号层面进行隔离管理，在生产、开发和测试等不同环境以及工作负载之间建立统一的防护规则与隔离边界，为安全性、计费和访问控制提供强隔离保障。通过多账号架构，可以防止安全事件跨环境传播，降低影响范围，例如，若某个工作负载被意外访问，隔离机制可限制风险扩散。同时您可以通过统一管控策略，建立企业整体访问控制原则或局部专用原则，确保安全合规和成本可控。您还可以集中化进行基础设施审计，满足合规与监管要求。

## 优先级

高

## 不推荐做法

- 将多个无关且数据敏感度不同的工作负载置于同一账号中。
- 资源夹结构混乱，导致访问控制和策略应用缺乏逻辑性。

## 实施指南

阿里云账号账户为不同敏感级别的工作负载或应用环境提供了安全隔离边界。通过该隔离边界，可有效控制资源访问权限、计费范围及安全策略。更多有关多账号的设计原则、实践模式等，请参见[阿里云构建多账号云环境白皮书](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/alibaba-cloud-building-a-multi-account-cloud-environment-white-paper)。

1. 设计规划多账号组织结构：通过[资源夹](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/manage-folders/)将账号归类分组，以实现企业的业务或应用根据其用途和需求进行逻辑划分。您可以按照业务的组织架构规划账号的组织结构。典型的架构可以选取在根资源夹下创建两个资源夹：Core、Applications。在 Core 资源夹中放置共享服务账号，用于集中横向管理类服务的部署，例如共享 VPC。在 Applications 资源夹中放置具体的应用。
2. 搭建 Landing Zone 多账号架构：[Landing Zone](https://help.aliyun.com/zh/caf/what-is-landing-zone-on-alibaba-cloud) 是阿里云的企业上云框架，可以指导企业规划和落地云上的资源结构、访问安全、网络架构和安全合规体系，为企业搭建安全、高效和可管理的云环境。您可以使用云治理中心 [Landing Zone 搭建](https://help.aliyun.com/zh/cgc/user-guide/build-a-landing-zone-1)功能，通过蓝图模板的形式，一站式轻松完成 Landing Zone 企业多账号环境的搭建。更多实施细节，请参见《[企业多账号统一架构方案](https://help.aliyun.com/zh/well-architected/solution-12)》。
3. 建立防护规则（Guardrails）：在多账号环境下实施统一的安全防护规则。您可以在云治理中心[统一配置防护规则](https://help.aliyun.com/zh/cgc/user-guide/configure-protection-rules-in-a-centralized-manner)，保证资源结构和基础配置不被修改，同时保证多账号环境的安全性。云治理中心提供了必选、推荐、可选三种类型的防护规则，其中必选规则会在您搭建 Landing Zone 时自动启用，而推荐与可选类型的防护规则，需要您手动评估并启用。建议您仔细审阅云治理中心推荐的防护规则项，优先启用与业务合规性直接相关的规则，对于可选的防护规则项，根据实际需求选择，避免过度限制业务灵活性。
4. 配置账号基线：为保证企业账号具有相同的安全合规基线，您可以使用云治理中心的[账号工厂](https://help.aliyun.com/zh/cgc/user-guide/account-factory/)功能[配置账号基线](https://help.aliyun.com/zh/cgc/user-guide/configure-the-account-baseline)，例如，密码强度等通用的安全配置。然后通过账号基线批量创建新账号，降低人工操作成本，保证基线一致性。

## 相关资源

### 相关实践

- [基于统一的IdP实现人员身份的统一认证](https://help.aliyun.com/zh/well-architected/sec01-bp05-unified-authentication-of-personnel-identity-based-on-unified-idp)

### 相关方案

- 《[企业多账号统一架构方案](https://help.aliyun.com/zh/well-architected/solution-12)》

### 相关文档

- [什么是云治理中心](https://help.aliyun.com/zh/cgc/product-overview/what-is-cloud-governance-center)
- [阿里云构建多账号云环境白皮书](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/alibaba-cloud-building-a-multi-account-cloud-environment-white-paper)
- [什么是云上Landing Zone](https://help.aliyun.com/zh/caf/what-is-landing-zone-on-alibaba-cloud)

---

> 原页面：https://help.aliyun.com/zh/well-architected/reasonable-isolation-of-different-workloads（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
