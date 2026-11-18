<!-- source: https://help.aliyun.com/zh/well-architected/sec02-bp04-encryption-of-credentials-during-storage-and-use -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706136 -->

# 在存储和使用过程中对凭据进行加密

明文存储凭据，将极大增加凭据泄露的风险，通过加密手段存储和使用凭据，有助于降低凭据泄露的可能。

## 优先级

高

## 不推荐做法

- 在未加密状态下静态存储凭证。
- 未精细化控制解密权限，比如授予了全部密钥的解密权限，导致越权访问带来的凭据泄露风险。

## 实施指南

建议您参考最佳实践[对固定凭据进行集中化管控](https://help.aliyun.com/zh/well-architected/sec02-bp05-centralized-control-of-fixed-credentials)，对凭据进行集中化的加密存储，在云上，推荐您使用密钥管理服务KMS，集中托管凭据，通过产品化的手段，保证凭据的加密存储。更多信息，请参见[凭据管理概述](https://help.aliyun.com/zh/kms/key-management-service/user-guide/secret-management-overview)。

其中，针对固定凭据AccessKey，推荐您优先使用临时凭据STS Token代替AccessKey的使用，最佳实践，请参见[使用临时凭据替代固定凭据](https://help.aliyun.com/zh/well-architected/sec02-bp02-prefer-temporary-credentials)。对于必须使用AccessKey的场景，请参考《[通过KMS实现固定AccessKey的集中管控](https://help.aliyun.com/zh/well-architected/solution-237)》，安全的存储和使用AccessKey。

同时，使用KMS，您可以控制谁可以使用您的KMS密钥并访问您的加密数据。RAM策略定义了身份（用户，组或角色）可以对哪些资源执行哪些操作。按照安全最佳实践，建议权限最小化，即只应授予身份所需的权限，且只能对需要使用的密钥进行授权，否则可能会造成数据的越权访问。不要为用户授予所有密钥的访问权限，而是确定用户访问加密数据所需的最小密钥集，然后给用户仅授予这些密钥的访问策略。例如，不要允许对所有KMS密钥使用kms:Decrypt权限。相反，只在您的账户的特定区域的特定密钥上允许该权限。通过采用最少权限原则，您可以降低无意泄露凭据的风险。

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

> 原页面：https://help.aliyun.com/zh/well-architected/sec02-bp04-encryption-of-credentials-during-storage-and-use（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
