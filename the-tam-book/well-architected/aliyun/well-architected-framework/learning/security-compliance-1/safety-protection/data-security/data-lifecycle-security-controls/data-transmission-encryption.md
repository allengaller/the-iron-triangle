<!-- source: https://help.aliyun.com/zh/well-architected/data-transmission-encryption -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2573804 -->

# 数据传输加密

## 网络传输加密

网络传输加密是指业务应用通过HTTPS协议传输数据，对HTTP网络传输协议进行安全认证，建议企业对外提供的关键业务进行网络传输加密。

通过数字证书管理服务（Certificate Management Service）来提供网络传输加密能力，数字证书管理服务（Certificate Management Service）是由阿里云联合中国及中国以外地域多家数字证书颁发机构（CA），在阿里云平台上直接提供的数字证书申请和部署服务，帮助您以较低的成本将服务从HTTP转换成HTTPS，实现网站或移动应用的身份验证和数据加密传输。

## 数据动态加密

阿里云提供了数据动态加密功能，利用密钥管理服务和用户的应用系统集成，实现数据的动态加密，确保在写入、读取数据库或存储前，数据是加密的。从而更全面的保护动态传输中的数据安全。应用执行动态数据加密需要集成阿里云密钥管理服务KMS的SDK或API，实现应用数据加密。

数据动态加密的最佳实践如下：

### 选择数据加密密钥

阿里云密钥管理服务提供了不同类型的密钥用于云产品加密和应用加密场景，需要注意的是阿里云密钥管理服务提供的默认密钥仅能用于云产品加密，不能用于应用加密。

| 密钥类别 | 密钥规格 | 加密方式 | 用途 | 限制 | 费用 |
| --- | --- | --- | --- | --- | --- |
| 默认密钥 | Aliyun_AES_256 | GCM | 仅用于云产品服务端加密 | 每个阿里云UID仅支持1个默认密钥 | 免费 |
| 软件密钥 | Aliyun_AES_256RSA_2048、RSA_3072EC_P256、EC_P256K | GCM、ECB、CBCRSAES_OAEP_SHA_256ECIES_DH_SHA_1_XOR_HMAC | 支持云产品服务端加密，支持应用客户端加密 | 参考KMS[实例说明](https://help.aliyun.com/zh/kms/key-management-service/product-overview/kms-billing) | 参考KMS[产品计费](https://help.aliyun.com/zh/kms/key-management-service/product-overview/kms-billing) |
| 硬件密钥 | Aliyun_AES_256Aliyun_AES_192Aliyun_AES_128Aliyun_SM4RSA_2048、RSA_3072、RSA_4096EC_P256、EC_P256KEC_SM2 | GCM、ECB、CBCRSAES_OAEP_SHA_256ECIES_DH_SHA_1_XOR_HMACSM2PKE | 支持云产品服务端加密，支持应用客户端加密支持金融级数据加密场景支持国密算法 | 参考KMS[实例说明](https://help.aliyun.com/zh/kms/key-management-service/product-overview/kms-billing) | 参考KMS[产品计费](https://help.aliyun.com/zh/kms/key-management-service/product-overview/kms-billing) |

- 通常情况下建议企业在应用加密场景中，选择软件密钥加密。
- 查看软件密钥类别中，对称密钥和非对称密钥的[密钥管理类型和密钥规格](https://help.aliyun.com/zh/kms/key-management-service/user-guide/key-types-and-specifications)。

### 应用与KMS的集成

应用程序可以选择通过集成API或使用封装好的KMS SDK完成应用系统与KMS的对接，并使用加密服务。

- 参考通过[应用接入点访问KMS实例](https://help.aliyun.com/zh/kms/key-management-service/create-an-aap)。
- 可选择使用RAM role进行API请求。
- 可选择使用client key（客户端密钥）对KMS和应用程序之间进行数据签名和认证。

### 为数据提供传输加密

企业在为应用系统提供数据加密时，希望在数据产生后并在写入数据库前完成数据加密。阿里云密钥管理服务提供不同的加密方式，支持对称加密和非对称加密，这两种方式在使用KMS服务时会略有不同。

选择使用KMS的对称加密方式时，则数据加密运算实际是发生在KMS的服务端，选用对称密钥用于数据加密的数据密钥。参考[使用KMS密钥在线加密和解密数据](https://help.aliyun.com/zh/kms/key-management-service/use-cases/use-a-kms-cmk-to-encrypt-and-decrypt-data-online#concept-221280)。具体流程图如下：

![使用KMS主密钥在线加密和解密数据_网络架构图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2119885561/p452634.png)

### 为数据密钥提供信封加密

选择使用KMS的非对称加密方式（信封加密）时，则数据加密运算实际发生在本地（应用环境），应用程序通过非对称加密方式和KMS之间交互本地加密运算的数据密钥（对称密钥）。参考[使用KMS密钥进行信封加密](https://help.aliyun.com/zh/kms/key-management-service/use-cases/use-envelope-encryption)。具体流程图如下：

![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0137073861/p649879.png)

---

> 原页面：https://help.aliyun.com/zh/well-architected/data-transmission-encryption（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
