<!-- source: https://help.aliyun.com/zh/well-architected/data-encryption-at-rest -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2573803 -->

# 数据静态加密

数据静态存储在云上时，需要执行数据静态存储加密，通常情况下企业将数据存储在如ECS的云盘，OSS、云数据库、NAS等位置。需要这些云产品具备存储加密的能力，确保用户存储在这些云服务中的数据是安全的。

阿里云提供了云产品落盘存储加密服务，并统一使用密钥管理服务（KMS）进行密钥管理。阿里云的存储加密功能提供了256位密钥的存储加密强度（AES256），满足敏感数据的加密存储需求。

1. 可查看支持服务端集成静态数据加密保护的[云服务列表](https://help.aliyun.com/zh/kms/key-management-service/alibaba-cloud-services-that-can-be-integrated-with-kms)以及各个云服务执行云产品服务端加密的具体操作方式。
2. 使用阿里云提供的免费默认密钥为云产品服务端加密。【什么是[默认密钥](https://help.aliyun.com/zh/kms/key-management-service/user-guide/overview-of-key-management)】
3. 使用自定义BYOK密钥来为云产品服务端提供数据加密。参考[导入对称密钥材料](https://help.aliyun.com/zh/kms/key-management-service/user-guide/import-key-material-into-a-symmetric-key)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/data-encryption-at-rest（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
