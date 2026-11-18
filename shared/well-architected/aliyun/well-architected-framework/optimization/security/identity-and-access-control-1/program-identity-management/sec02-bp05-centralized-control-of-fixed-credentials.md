<!-- source: https://help.aliyun.com/zh/well-architected/sec02-bp05-centralized-control-of-fixed-credentials -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706130 -->

# 对固定凭据进行集中化管控

固定凭据（如AccessKey、数据库账号密码等）应该避免直接颁发给个人，也不要明文写到代码里。通过使用凭据管家、第三方Vault等对凭据进行集中管理，避免人员直接接触凭据，降低泄漏风险。

## 优先级

高

## 不推荐做法

1. 将凭据创建出来之后，直接明文交给研发使用。当该研发离职后，后续难以追踪凭据在哪里被使用，溯源困难。
2. 将凭据明文写在代码或者配置项文件中。当代码不慎提交到公开仓库如GitHub上，导致AccessKey等凭据泄漏。即使提交到内部仓库，也常常会因为仓库权限管理不善导致AccessKey被恶意获取。
3. 给企业员工创建AccessKey并明文交给员工使用。比如给运维同学创建AccessKey，运维同学将其写入本地的脚本或者代码中用于一些自动化运维的场景，由于电脑丢失或者不慎提交到公开仓库如GitHub上，导致AccessKey泄漏。

## 实施指南

对于必须使用固定凭据（如RAM用户AccessKey）的场景，建议对凭据进行集中化管控，避免人员身份直接接触凭据。在阿里云上，推荐以下解决方案：

- 针对RAM用户AccessKey的集中化管控，[使用KMS凭据管家托管RAM凭据](https://help.aliyun.com/zh/kms/key-management-service/user-guide/manage-and-use-ram-secrets)。通过该方式，可以实现AccessKey的集中化管控，当业务需要使用AccessKey时，可以为其托管一个RAM用户AccessKey，并可以设置自动轮转周期，降低AccessKey泄漏风险。轮转时凭据管家会调用访问控制 RAM（Resource Access Management），先创建一个新的AccessKey，然后删除旧的AccessKey。同时KMS将新的AccessKey写入凭据值，并删除旧的AccessKey对应的凭据值。当您发现RAM凭据泄露时，可以通过立即轮转凭据进行应急处理，此时推荐将轮转时长设置为30分钟实现快速轮转，降低泄漏造成的损失。具体操作，请参考方案《[通过KMS实现固定AccessKey的集中管控](https://help.aliyun.com/zh/well-architected/solution-237)》。
- 针对云上数据库账号密码，通过KMS实现数据库凭据的托管。使用数据库凭据，应用程序将无需配置静态数据库账号口令。管理员在凭据管家创建数据库凭据，并且可以为凭据设置周期性自动轮转，降低凭据泄露的安全风险。也可以在凭据泄露时，通过控制台立即轮转功能快速轮转凭据，阻断入侵威胁。目前KMS支持以下数据库产品的凭据托管：[RDS凭据](https://help.aliyun.com/zh/kms/key-management-service/user-guide/manage-and-use-apsaradb-rds-secrets)[Redis/Tair凭据](https://help.aliyun.com/zh/kms/key-management-service/user-guide/apsaradb-for-redis-secrets)[PolarDB凭据](https://help.aliyun.com/zh/kms/key-management-service/user-guide/apsaradb-polardb-secrets)
- 针对ECS的账号口令或者公私钥，[使用KMS凭据管家托管ECS凭据](https://help.aliyun.com/zh/kms/key-management-service/user-guide/manage-and-use-ecs-secrets)。业务应用及阿里云服务可以向KMS动态获取账号口令，您还可以为凭据配置轮转，以减少账号口令的泄露风险。
- 针对其他的通用凭据类型，比如账号口令、访问密钥、OAuth密钥和API Token等任意的敏感数据，都可以[使用KMS凭据管家托管通用凭据](https://help.aliyun.com/zh/kms/key-management-service/user-guide/manage-and-use-generic-secrets)，解决在代码中硬编码通用凭据带来的数据泄露风险。通用凭据不支持在KMS直接配置周期性轮转，但您可以通过函数计算配置周期性轮转。具体操作，请参见[使用函数计算轮转普通凭据](https://help.aliyun.com/zh/kms/key-management-service/use-cases/use-function-compute-to-rotate-generic-secrets)。

对凭据进行集中化管控后，您就可以很方便地对凭据进行加密存储和定期轮转，进一步保证凭据的存储和使用安全。

## 相关资源

### 相关实践

- [定期审查和轮转固定凭据](https://help.aliyun.com/zh/well-architected/sec02-bp03-periodic-review-and-rotation-of-fixed-credentials)
- [在存储和使用过程中对凭据进行加密](https://help.aliyun.com/zh/well-architected/sec02-bp04-encryption-of-credentials-during-storage-and-use)

### 相关方案

- 《[通过KMS实现固定AccessKey的集中管控](https://help.aliyun.com/zh/well-architected/solution-237)》

---

> 原页面：https://help.aliyun.com/zh/well-architected/sec02-bp05-centralized-control-of-fixed-credentials（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
