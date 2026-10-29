<!-- source: https://help.aliyun.com/zh/well-architected/sec02-bp01-assign-different-credentials-to-different-workloads-and-environments -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706140 -->

# 为不同的工作负载和环境分配不同的凭据

程序访问云资源时，需要通过访问凭据（固定凭据AccessKey或临时凭据STS Token）进行身份认证。多个程序共用凭据的情况下，凭据所持有的权限需要包含所有的使用场景，导致权限扩大。另外，共用情况下，一处泄漏会导致所有使用相同凭据的场景或应用都受到影响，风险扩大，同时增加了凭据泄漏后的止血难度。对于同一个应用的不同环境，如生产环境、测试环境，往往需要访问不同的资源，同时，测试环境代码往往不够稳定和健壮，更容易有泄漏风险，如果共用同一个凭据，测试环境凭据泄漏后也极容易造成对生产环境的影响，导致业务安全风险。

建议您根据缩小暴露面积的最小化原则，为每个工作负载或应用分配独立的访问凭据，同时对于每个工作负载或应用下的环境，比如开发、测试、生产环境也分配独立的不同凭据，避免权限混用，防止泄露扩散。

## 优先级

高

## 不推荐做法

- 多个工作负载共用同一个访问凭据，比如共用同一个AccessKey或者使用同一个RAM角色的STS Token，导致权限混用，增加泄露扩散面积。
- 跨环境复用访问凭据，比如开发环境的凭据被用于生产环境，导致增加泄露风险和暴露面积。
- 人员和程序身份混用。比如一个RAM用户既提供给企业员工登录控制台使用，同时又创建有AccessKey提供给程序访问阿里云使用，导致权限混用，增加管理成本和泄露风险。

## 实施指南

建议您使用临时凭据STS Token调用阿里云OpenAPI访问云资源，降低因固定凭据泄漏导致的风险。详细，请参考[使用临时凭据替代固定凭据](https://help.aliyun.com/zh/well-architected/sec02-bp02-prefer-temporary-credentials)。

1. 创建与使用凭据。推荐您优先使用临时凭据STS Token访问阿里云，降低因固定凭据AccessKey泄漏导致的风险。您需要通过扮演某个RAM角色获取代表该角色的临时凭据。因此对于不同工作负载和环境，您需要创建和分配不同的RAM角色，具体操作，请参见[RAM角色概览](https://help.aliyun.com/zh/ram/user-guide/ram-role-overview)。针对不同的使用STS Token场景，请参考[使用临时凭据替代固定凭据](https://help.aliyun.com/zh/well-architected/sec02-bp02-prefer-temporary-credentials)，尽可能的使用STS Token代替固定凭据AccessKey的使用。如果您使用固定凭据AccessKey访问阿里云，请参考[创建RAM用户](https://help.aliyun.com/zh/ram/user-guide/create-a-ram-user)和[创建AccessKey](https://help.aliyun.com/zh/ram/create-an-accesskey-pair-1)，为不同工作负载和环境创建独立的RAM用户和AccessKey。为确保AccessKey的使用安全，请遵循集中管控、加密存储、定期轮转的原则，更多实践细节，请参考[对固定凭据进行集中化管控](https://help.aliyun.com/zh/well-architected/sec02-bp05-centralized-control-of-fixed-credentials)、[在存储和使用过程中对凭据进行加密](https://help.aliyun.com/zh/well-architected/sec02-bp04-encryption-of-credentials-during-storage-and-use)、[定期审查和轮转固定凭据](https://help.aliyun.com/zh/well-architected/sec02-bp03-periodic-review-and-rotation-of-fixed-credentials)。
2. 定期审查。您可以使用[云治理中心](https://help.aliyun.com/zh/cgc/product-overview/what-is-cloud-governance-center)治理检测的功能，通过产品化的手段，定期审查并治理身份混用等问题。同时通过订阅治理检测报告，定时获取最新的治理检测结果，方便您及时查看和处理风险事项。具体操作，请参见[订阅治理报告](https://help.aliyun.com/zh/cgc/user-guide/set-check-items#bcf88aa4211vb)。
3. 安全加固。对于程序身份进行精细化授权，确保权限最小可用。详情，请参考[基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)。对于使用固定凭据AccessKey的场景，通过[AccessKey网络访问限制策略](https://help.aliyun.com/zh/ram/user-guide/accesskey-network-access-restriction-policy)，限制使用AccessKey的API请求来源IP地址，将AccessKey调用来源控制在可信的网络环境内，提升AccessKey的安全性。

## 相关资源

### 相关实践

- [使用临时凭据替代固定凭据](https://help.aliyun.com/zh/well-architected/sec02-bp02-prefer-temporary-credentials)
- [定期审查和轮转固定凭据](https://help.aliyun.com/zh/well-architected/sec02-bp03-periodic-review-and-rotation-of-fixed-credentials)
- [基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)

---

> 原页面：https://help.aliyun.com/zh/well-architected/sec02-bp01-assign-different-credentials-to-different-workloads-and-environments（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
