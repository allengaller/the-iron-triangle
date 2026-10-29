<!-- source: https://help.aliyun.com/zh/well-architected/key-management -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2573802 -->

# 密钥管理

数据库账号口令、服务器账号口令、SSH Key、访问密钥等凭据的泄露，是当今数据安全面临的主要威胁之一。密钥的保护是数据安全保护措施中最基础的一项，为使用阿里云密钥、通用密钥提供保护措施能够保护数据不被泄露，保障企业数据安全。

在云环境中，密钥类别可分为通用密钥（数据库账号口令、服务器账号口令、SSH Key），和云账户密钥（RAM AccessKey/SecretKey）。

密钥的有效保护措施分为密钥加密、密钥托管（动态获取密钥，称之为凭据）、凭据轮转，以及访问控制和审计。

不安全使用密钥的场景包括：

- 将密钥明文写在代码中；
- 直接使用AccessKey/SecretKey调用；
- AccessKey/SecretKey没有区分应用或使用环境；
- AccessKey/SecretKey没有定期轮转。

在云上，针对密钥管理，有以下最佳实践：

## 开通KMS并配置密钥和凭据的托管

阿里云提供[密钥管理服务（KMS）](https://help.aliyun.com/zh/kms/key-management-service/product-overview/what-is-key-management-service-1)来保护用户的密钥，并提供[凭据管理](https://help.aliyun.com/zh/kms/key-management-service/user-guide/secret-management-overview)加密存储、定期轮转、安全分发、中心化管理等能力，使应用程序规避明文配置凭据风险，支持轮转进而有效降低凭据泄漏事件危害。

下图为使用凭据托管的标准场景和流程：

![(应用上云规划-应用上云实施-图5) 备份 8.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5576435961/p722839.jpg)

- 管理员在目标数据库配置MyApp访问数据库所需的用户名和密码。
- 管理员在KMS创建一个凭据对象MyDbCreds，用来加密存储上述用户名和密码。
- 当MyApp需要访问数据库时，需要向KMS请求凭据MyDbCreds。
- KMS读取到存储的凭据密文，解密后将明文通过HTTPS返回给MyApp。
- MyApp读取并解析KMS返回的凭据明文，获取到用户名和密码，使用该账号可以访问目标数据库。

开通KMS并配置密钥和凭据托管的最佳实践：

- 开通并[启用KMS](https://help.aliyun.com/zh/kms/key-management-service/user-guide/manage-kms-instances)。
- 开通KMS后，针对[密钥保护的标准步骤](https://help.aliyun.com/zh/kms/key-management-service/user-guide/manage-and-use-generic-secrets)是先创建通用凭据，输入凭据的值（也就是密钥的明文），选择加密凭据的[主密钥](https://help.aliyun.com/zh/kms/key-management-service/user-guide/key-types-and-specifications#task-2292624)（主密钥是由KMS生成或客户自行导入的外部密钥，用于在KMS内完成数据加密运算），起到密钥加密存储的作用。其次通过集成KMS的SDK或API完成应用程序的调用。
- 开启RAM密钥（AccessKey/SecretKey）的安全保护，在凭据管理中[托管RAM凭据](https://help.aliyun.com/zh/kms/key-management-service/user-guide/manage-and-use-ram-secrets)，无需在应用程序中配置AccessKey，应用程序安装RAM凭据插件的方式即可安全的调用托管的密钥，如下图所示。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5576435961/p722841.png)

## 使用凭据轮转提高密钥安全等级

通常情况下建议定期对保存在KMS中的密钥进行轮转，从而达到更高级别的安全要求，增强敏感信息的安全性。在KMS服务中，企业根据保存的密钥类型（通用凭据还是RAM凭据）选择轮转方案。

- 阿里云支持[使用函数计算轮转通用凭据](https://help.aliyun.com/zh/kms/key-management-service/use-cases/use-function-compute-to-rotate-generic-secrets)。
- RAM凭据、ECS、RDS凭据支持[自动轮转](https://help.aliyun.com/zh/kms/key-management-service/user-guide/manage-and-use-ram-secrets)。

## 为密钥访问设定访问控制策略

通常情况下，为防止非授权访问应限定访问密钥的方式、身份及策略。在云端应该限制授权范围和授权主体以及应用程序访问。

- 使用RAM实现对KMS资源的[访问控制](https://help.aliyun.com/zh/kms/key-management-service/security-and-compliance/use-ram-to-manage-access-to-kms-resources/)。
- 使用KMS应用接入点实现对应用程序访问和接入[KMS实例](https://help.aliyun.com/zh/kms/key-management-service/create-an-aap)。
- 通过创建应用接入点，精细化配置哪些凭据可以授权给哪些应用程序，以及访问的网络、和身份认证，提供更精细化的授权策略，KMS应用访问控制流程如下图所示。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4576435961/p722842.png)

## 为密钥的使用开启安全审计

为KMS的使用开通安全审计，有助于事后安全溯源和合规审计。使用操作审计[查询密钥管理服务的操作事件](https://help.aliyun.com/zh/kms/key-management-service/security-and-compliance/use-actiontrail-to-query-kms-event-logs-1)，可查看支持审计的[操作和事件说明](https://help.aliyun.com/zh/kms/key-management-service/security-and-compliance/key-management-service-support-audited-event-description)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/key-management（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
