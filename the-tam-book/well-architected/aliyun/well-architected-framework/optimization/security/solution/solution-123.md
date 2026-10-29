<!-- source: https://help.aliyun.com/zh/well-architected/solution-123 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929216 -->

# 金融行业数据传输及存储加密方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4476581571/p969793.png)

金融行业核心系统中含有大量客户资料、市场信息及资金信息等，保密性要求高，行业合规监管及数据安全要求严格，金融企业对严格保障数据存储及传输安全需求强烈。网站数据可能产生泄露、篡改或钓鱼攻击等问题，金融企业网站中的业务数据需要实现加密传输及加密存储，有效防止敏感数据泄露。

本方案介绍了金融企业如何在阿里云上实现常见数据传输链路及存储产品的数据加密，保护金融企业云上数据的隐私性和自主性，并在云上对加密密钥和证书实现安全管理。

## 方案优势

### 数据传输及存储安全合规

通过数据传输加密及存储加密大幅提升数据安全性，防止数据泄露、篡改等，满足金融行业监管合规及企业内部合规要求。

- SSL在传输层对网络连接进行加密，能提升通信数据的安全性和完整性。HTTPS加密传输协议可激活客户端浏览器到网站服务器之间的SSL加密通道，从而实现高强度单向加密传输，防止传输数据被泄露或篡改。
- 透明数据加密TDE（Transparent Data Encryption），即对数据文件执行实时I/O加密和解密。
- 云盘加密功能，基于块存储对整个数据盘进行加密，即使数据备份泄露也无法解密，保护数据安全。
- 全加密功能是阿里云数据库的一项数据安全功能。在[RDS PostgreSQL](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/what-is-apsaradb-rds-for-postgresql)实例中开启并使用该功能，您可以对数据库表中的敏感数据列进行加密，这些列中的敏感数据将以密文进行传输、计算和存储。

### 密钥便捷管理

使用[密钥管理服务KMS](https://help.aliyun.com/zh/kms/key-management-service/support/what-is-key-management-service)，用户可随时创建新的用户主密钥（CMK），并通过访问控制（RAM）轻松管理谁可以访问该密钥。同时可以通过[操作审计（ActionTrail）](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)审核密钥的使用情况。KMS支持自带密钥（BYOK）用户可以从线下密钥管理基础设施（KMI）将密钥导入到KMS。无论在KMS内创建的密钥还是外部导入的密钥，密钥中的机密信息或者敏感数据都会被阿里云上的其他云产品用于加密保护。

### 证书全生命周期管理

阿里云联合全球多家数字证书颁发机构，在云上直接提供数字证书申请、管理、部署等的服务。数字证书管理服务同时支持SSL证书和私有证书，支持企业已有[证书上传](https://help.aliyun.com/zh/ssl-certificate/upload-an-ssl-certificate)，帮您以较低的成本将数据传输协议从HTTP转换成HTTPS，实现网站或移动应用的身份验证和数据加密传输。[数字证书管理服务](https://help.aliyun.com/zh/ssl-certificate/product-overview/what-is-certificate-management-service)和阿里云产品深度集成，支持一键将SSL证书部署到已经开通的阿里云产品中（如SLB和CDN），以低成本和方便快捷的方式轻松运维和管理不同的证书。

## 客户场景

### 数据安全监管合规

#### 场景描述

金融企业受行业监管等外部审计机构及内部合规要求，在云上的数据存储及传输必须开启加密，例如等保2.0对应到云上要求企业使用的ECS必须开启数据盘加密、OSS存储空间开启服务端加密等。

#### 适用客户

应监管合规要求对数据传输及存储加密有要求的金融企业客户。

### 数据传输及存储隐私安全

#### 场景描述

金融企业通常保存着大量敏感信息，需要严防数据泄露及篡改，因此对敏感业务数据安全要求更加严格，对数据传输及存储的安全性要求更高。金融企业可以通过对数据传输链路及存储进行加密的方式大幅提升数据安全性，保障业务稳定运行。

#### 适用客户

对数据传输及存储隐私安全有诉求的金融企业客户。

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4476581571/p969803.png)

下文从数据传输加密、数据存储加密两方面介绍方案架构。

- **数据传输加密****客户端使用HTTPS**访问部署在阿里云上的Web业务应用，另推荐公网Web访问中使用[Web应用防火墙（WAF）](https://help.aliyun.com/zh/waf/web-application-firewall-3-0/product-overview/what-is-waf)保障数据入口访问安全；**企业应用使用HTTPS**访问云服务的[OpenAPI](https://help.aliyun.com/zh/sdk/alibaba-cloud-api-overview)。部署在[ECS](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)及[ACK](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/product-overview/what-is-ack)上的业务应用使用**SSL加密通道**与云数据库[Redis](https://help.aliyun.com/zh/redis/product-overview/what-is-apsaradb-for-redis)及[RDS](https://help.aliyun.com/zh/rds/product-overview/what-is-apsaradb-rds-what-is-apsaradb-rds)进行数据传输。使用[数字证书管理服务](https://help.aliyun.com/zh/ssl-certificate/product-overview/what-is-certificate-management-service)对**SSL证书**进行管理，支持直接部署到云服务，支持导入用户已有证书实现证书统一管理。
- **数据存储加密**使用[密钥管理服务KMS](https://help.aliyun.com/zh/kms/key-management-service/support/what-is-key-management-service)进行密钥管理，支持使用在KMS生成的**用户主密钥（CMK）**及导入**自带密钥（BYOK）生成的主密钥**对云产品内用户数据进行加密。对[对象存储OSS](https://help.aliyun.com/zh/oss/user-guide/what-is-oss)存储空间可使用KMS中的密钥进行**服务端加密**，也支持进行**客户端加密**。对[云服务器ECS](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)**系统盘及数据盘**可使用KMS密钥进行加密。对[容器服务ACK](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/product-overview/what-is-ack)的**Secrets、云盘存储卷、OSS存储卷**可使用KMS密钥进行加密。对[云数据库Redis](https://help.aliyun.com/zh/redis/product-overview/what-is-apsaradb-for-redis)可使用KMS中的密钥对其中的数据进行**透明数据加密TDE**（Transparent Data Encryption）。对[云数据库RDS](https://help.aliyun.com/zh/rds/product-overview/what-is-apsaradb-rds-what-is-apsaradb-rds)可使用KMS中的密钥进行**云盘加密、透明数据加密**；另RDS PostgreSQL实例还支持[全加密](https://help.aliyun.com/zh/rds/overview)，敏感数据将以密文进行传输、计算及存储。对于安全要求**非常严格的敏感数据**，可以先在**应用中完成本地加密再存储到相关云服务**，加密密钥可以使用KMS进行管理，加解密详情参见[使用KMS信封加密在本地加密和解密数据](https://help.aliyun.com/zh/kms/key-management-service/support/use-envelope-encryption-to-encrypt-and-decrypt-local-data)。

### 多账号证书管理

[数字证书管理服务（Certificate Management Service）](https://help.aliyun.com/zh/ssl-certificate/product-overview/what-is-certificate-management-service)是由阿里云联合全球多家数字证书颁发机构，在阿里云平台上直接提供数字证书申请、管理、部署等的服务。数字证书管理服务同时支持SSL证书和私有证书，帮您以较低的成本将数据传输协议从HTTP转换成HTTPS，实现网站或移动应用的身份验证和数据加密传输。

不同类型SSL证书在适用网站类型、公信等级、认证强度、安全性和支持的证书品牌上的区别如下。对于金融企业建议使用**EV企业增强型**SSL证书保障安全。

| **证书类型** | **适用网站类型** | **公信等级** | **认证强度** | **安全性** | **支持的证书品牌** |
| --- | --- | --- | --- | --- | --- |
| DV域名型 | 个人网站 | 一般 | CA机构审核个人网站真实性、不验证企业真实性 | 一般 | DigiCert（原Symantec）、GeoTrust、GlobalSign、vTrus（国产）、WoSign（国产） |
| OV企业型 | 政府组织、企业、教育机构等 | 高 | CA机构审核组织及企业真实性 | 高 | DigiCert（原Symantec）、GeoTrust、GlobalSign、CFCA（国产）、vTurs |
| EV企业增强型 | 大型企业、金融机构等 | 最高 | 严格认证 | 最高 | DigiCert（原Symantec）、GeoTrust、CFCA（国产） |

如果客户拥有多个阿里云账号，SSL证书服务可以实现在不同阿里云账号（归属于同一个经过实名认证的个人或企业用户）之间**共享证书**。例如企业客户可以由安全管理团队统一在**安全账号**购买证书，然后分享至其它账号，分享详情参见[证书共享](https://help.aliyun.com/zh/document_detail/305605.html)。

如果企业已经通过第三方证书服务商购买并签发了SSL证书，希望将已有证书部署到阿里云产品（或者计划使用数字证书管理服务**统一管理所有证书**），可以使用数字证书管理服务的[上传证书](https://help.aliyun.com/zh/ssl-certificate/upload-an-ssl-certificate)功能。

同一企业在多账号场景下，如果多个账号实名认证不同无法直接共享证书，在安全账号购买了证书后可以先下载证书，再登录目标账号的证书管理页面上传证书。

### 密钥管理

[密钥管理服务KMS（Key Management Service）](https://help.aliyun.com/zh/kms/key-management-service/support/what-is-key-management-service)是您的一站式密钥管理和数据加密服务平台，提供简单、可靠、安全、合规的数据加密保护能力。KMS帮助您降低在密码基础设施和数据加解密产品上的采购、运维、研发开销，以便您只需关注业务本身。

KMS密钥管理可使用密钥服务（共享版）、专属基础版、专属标准版，差异详情参见[专属KMS基础版和标准版的差异](https://help.aliyun.com/zh/kms/key-management-service/support/differences-between-dedicated-kms-of-the-basic-edition-and-dedicated-kms-of-the-standard-edition)、[密钥服务](https://help.aliyun.com/zh/kms/key-management-service/support/key-service-1/)。建议金融企业新用户使用**专属KMS标准版**，标准版具备用户侧数据加密能力和加密服务密码机集群加密能力，将密钥存储在用户独享的**硬件安全密码模块（HSM）资源池**，同时支持云产品原生的数据加密，满足需使用密码资源池满足监管合规需求或安全诉求。

专属KMS支持跨账号下的VPC访问同一专属KMS实例，该方案主要用于**应用层数据的加密**，详情可参见[配置多VPC访问统一KMS专属实例](https://help.aliyun.com/zh/kms/key-management-service/support/manage-dedicated-kms-instances-of-the-basic-edition)。

对于**云产品层面的加密**（如ECS云盘加密等）需要获取账号内KMS中的密钥，目前需要在相应账号中分别部署KMS进行密钥管理。

KMS专属标准版支持自带密钥材料（BYOK）导入，详情参见[导入对称密钥材料](https://help.aliyun.com/zh/kms/key-management-service/support/import-symmetric-key-material)及[导入非对称密钥材料](https://help.aliyun.com/zh/kms/key-management-service/support/import-key-material-into-an-asymmetric-key-1)。

### ALB/CLB链路加密

#### ALB HTTPS全链路加密

随着企业的业务大量上云，云上承载业务的安全性变得越来越重要，尤其在金融行业，为了保障业务的安全性，往往会存在全链路加密的要求。这就要求负载均衡在提供服务的时候，不仅要保障前端（客户端到负载均衡）通信的安全，还要保障后端（负载均衡到业务服务器）通信的安全。ALB提供全链路HTTPS加密功能，可以实现客户端到ALB、**ALB到后端服务器之间的HTTPS加密通信**，提升**敏感业务**的安全性。详情可参见[配置全链路HTTPS访问实现加密通信](https://help.aliyun.com/zh/slb/application-load-balancer/end-to-end-data-transfer-over-https)。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4476581571/p969804.png)

#### ALB HTTPS双向认证

当金融企业在处理一些**关键业务**时，HTTPS双向认证通过对通信双方做双向认证为业务提供更高的安全性，**ALB支持实现HTTPS双向认证**，详情可参见[使用ALB部署HTTPS业务（双向认证](https://help.aliyun.com/zh/slb/application-load-balancer/configure-mutual-authentication-on-an-https-listener)）。

- HTTPS单向认证：客户端需要认证服务器端，而服务器端不需要认证客户端。客户端从服务器端下载服务器端公钥证书进行验证，然后建立安全通信通道。
- HTTPS双向认证：客户端需要从服务器端下载服务器的公钥证书进行验证，同时还需要把客户端的公钥证书上传到服务器端进行验证，双方都通过认证，才能建立安全通信通道进行数据传输。因此双向认证可以为业务提供更高的安全性。

#### CLB HTTPS双向认证

当金融企业在处理一些**关键业务**时，HTTPS双向认证通过对通信双方做双向认证为业务提供更高的安全性，**CLB支持部署HTTPS双向认证**，详情可参见[使用CLB部署HTTPS业务（双向认证）](https://help.aliyun.com/zh/slb/classic-load-balancer/use-cases/configure-mutual-authentication-on-an-https-listener-1)。

### OSS加密及防护

#### 服务端加密

当您在设置了服务器端加密的存储空间（Bucket）中上传文件（Object）时，OSS对收到的文件进行加密，再将得到的加密文件持久化保存。当您通过GetObject请求下载文件时，OSS自动将加密文件解密后返回给用户，并在响应头中返回**x-oss-server-side-encryption**，用于声明该文件进行了服务器端加密。OSS通过服务器端加密机制，提供静态数据保护。适合于对于文件存储有**高安全性或者合规性要求**的应用场景。详情可参见[服务端加密](https://help.aliyun.com/zh/oss/user-guide/server-side-encryption-8)。

OSS针对不同使用场景提供了两种服务器端加密方式，您可以根据实际使用场景选用。

| **加密方式** | **功能描述** | **使用场景** | **注意事项** | **费用说明** |
| --- | --- | --- | --- | --- |
| 使用KMS托管密钥进行加解密（SSE-KMS） | 使用KMS托管的默认CMK（Customer Master Key）或指定CMK进行加解密操作。数据无需通过网络发送到KMS服务端进行加解密。 | 因安全合规的要求，需要使用自管理、可指定的密钥。 | 用于加密Object的密钥也会被加密，并写入Object的元信息中。KMS托管密钥的服务器端加密方式仅加密Object数据，不加密Object的元数据。 | 在KMS服务侧产生少量的KMS密钥请求费用。费用详情，请参见[KMS计费标准](https://help.aliyun.com/zh/kms/key-management-service/support/billing-of-kms)。 |
| 使用OSS完全托管密钥进行加解密（SSE-OSS） | 使用OSS完全托管的密钥加密每个Object。为了提升安全性，OSS还会使用定期轮转的主密钥对加密密钥本身进行加密。 | 仅需要基础的加密能力，对密钥无自管理需求。 | 无 | 免费 |

#### 客户端加密

客户端加密是指将文件（Object）发送到对象存储OSS之前在本地进行加密，当用户希望数据上传到阿里云之前就进行加密时可使用该功能，详情参见[客户端加密](https://help.aliyun.com/zh/oss/user-guide/client-side-encryption)。

注意：

- 使用客户端加密功能时，您需要对主密钥的完整性和正确性负责。因您维护不当导致主密钥用错或丢失，从而导致加密数据无法解密所引起的一切损失和后果均由用户自行承担。
- 在对加密数据进行复制或者迁移时，您需要对加密元信息的完整性和正确性负责。因您维护不当导致加密元信息出错或丢失，从而导致加密数据无法解密所引起的一切损失和后果均由用户自行承担。

使用客户端加密时，会为每个Object生成一个随机数据加密密钥，用该随机数据加密密钥明文对Object的数据进行对称加密。主密钥用于生成随机的数据加密密钥，加密后的内容会当作Object的meta信息保存在服务端。解密时先用主密钥将加密后的随机密钥解密出来，再用解密出来的随机数据加密密钥明文解密Object的数据。主密钥只参与客户端本地计算，不会在网络上进行传输或保存在服务端，以保证主密钥的数据安全。

注意：

- 客户端加密支持分片上传超过5 GB的文件。在使用分片方式上传文件时，需要指定上传文件的总大小和分片大小， 除了最后一个分片外，每个分片的大小要一致，且分片大小目前必须是16的整数倍。
- 调用客户端加密上传文件后，加密元数据会被保护，无法通过[CopyObject](https://help.aliyun.com/zh/oss/developer-reference/copyobject)修改Object meta信息。

##### 使用KMS托管用户主密钥加密

当使用KMS托管用户主密钥用于客户端数据加密时，无需向OSS加密客户端提供任何加密密钥，只需要在上传对象时指定KMS用户主密钥ID（也就是CMK ID）。具体工作原理如下图所示。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4476581571/p969795.png)

- 加密并上传Object获取加密密钥。通过使用CMK ID，客户端首先向KMS发送一个请求，申请1个用于加密Object的数据密钥（Data Key）。作为响应，KMS会返回一个随机生成的数据明文密钥（Data Key）以及一个数据密文密钥（Encrypted Data Key）。加密数据并上传至OSS。本地客户端接收到KMS返回的数据明文密钥以及数据密文密钥后，将使用数据明文密钥进行本地加密，并且将加密后的对象以及数据密文密钥上传至OSS。
- 下载并解密Object下载Object。客户端从OSS服务端下载加密的Object以及作为对象元数据存储的数据密文密钥。解密Object。客户端将数据密文密钥以及CMK ID发送至KMS服务器。作为响应，KMS将使用指定的CMK解密，并且将数据明文密钥返回给本地加密客户端。

**说明**

- 本地加密客户端为每一个上传的对象获取一个唯一的数据加密密钥。
- 为了保证数据的安全性，建议CMK定期轮换或者更新。
- 您需要维护CMK ID与Object之间的映射关系。

##### 使用用户自主管理密钥加密

使用用户自主管理密钥时，需要您自主生成并保管加密密钥。当本地客户端加密Object时，由用户自主上传加密密钥（对称加密密钥或者非对称加密密钥）至本地加密客户端。其具体加密过程如下图所示。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4476581571/p969811.png)

- 加密并上传Object用户向本地加密客户端提供1个用户主密钥（对称密钥或者非对称密钥）。本地加密客户端在本地生成一个一次性的对称密钥，即数据密钥（Data Key）。它将用于加密单个对象（针对每个对象，客户端都会随机生成1个数据密钥）。客户端使用数据密钥加密对象，并使用用户提供的主密钥来加密数据密钥。客户端将加密的数据密钥（Encrypted Data Key）作为对象元数据的一部分上传至OSS。
- 下载并解密Object客户端从OSS下载加密的对象以及元数据。通过使用元数据中的材料，客户端将授权确定使用对应主密钥来解密数据密钥，之后使用解密后的数据密钥来解密对象。

**注意**

- OSS本地加密客户端不会将用户主密钥以及未加密的数据发送至OSS。所以，请务必妥善保管加密密钥，如果密钥丢失，将无法解密数据。
- 数据密钥由本地加密客户端随机生成。

#### 配置合规审计

[配置审计（Config）](https://help.aliyun.com/zh/document_detail/127388.html)是一项资源审计服务，为客户提供面向资源的**配置历史追踪**、**配置合规审计**等能力。面对大量资源，帮您轻松实现基础设施的自主监管，确保持续性合规。建议在配置审计中启用OSS合规管理最佳实践合规包，帮助客户实现OSS持续合规，详细合规规则参见[OSS合规管理最佳实践](https://help.aliyun.com/zh/document_detail/312327.html)。

#### 接入WAF

文件（Object）上传至存储空间（Bucket）后，OSS会自动生成文件URL，可以直接通过文件URL访问该文件。如果客户希望通过自定义域名访问这些文件，需要将自定义域名绑定至文件所在的Bucket，并添加CNAME记录，详情参见[绑定自定义域名](https://help.aliyun.com/zh/oss/user-guide/access-buckets-via-custom-domain-names)。[Web应用防火墙（WAF）](https://help.aliyun.com/zh/waf/web-application-firewall-3-0/product-overview/what-is-waf)可以有效识别Web业务流量的恶意特征，在对流量清洗和过滤后，将正常、安全的流量返回给服务器，避免网站服务器被恶意入侵导致性能异常等问题，从而保障网站的业务安全和数据安全。可以使用WAF对OSS中的文件（Object）域名进行防护，详情参见WAF [CNAME接入](https://help.aliyun.com/zh/waf/web-application-firewall-2-0/user-guide/website-access-with-cname/)。

#### 防盗链

OSS支持对存储空间（Bucket）设置防盗链，即通过对访问来源设置白名单的机制，避免OSS资源被其他人盗用。防盗链通过请求Header中的Referer地址判断访问来源。当浏览器向Web服务器发送请求的时候，请求Header中将包含Referer，用于告知Web服务器该请求的页面链接来源。OSS根据浏览器附带的Referer与用户配置的Referer规则来判断允许或拒绝此请求，如果Referer一致，则OSS将允许该请求的访问；如果Referer不一致，则OSS将拒绝该请求的访问，详情参见[防盗链](https://help.aliyun.com/zh/oss/user-guide/hotlink-protection)。

#### 其它数据安全最佳实践

OSS其它数据安全最佳实践请参见帮助文档[数据安全](https://help.aliyun.com/zh/oss/data-security-11)及[OSS安全最佳实践](https://help.aliyun.com/zh/oss/user-guide/security-best-practices/)。

### ECS云盘加密

当ECS工作负载用于处理生产数据时，通常会接触到您的业务机密、隐私信息或者关键凭证，因此需要对工作负载进行保护以防范信息泄露。数据加密适用于数据安全或法规合规等场景，帮助您加密保护存储在阿里云ECS上的数据。**被加密的云盘可以是系统盘和数据盘**，详情参见[加密概述](https://help.aliyun.com/zh/ecs/user-guide/encryption-overview)。

ECS加密采用行业标准的AES-256加密算法，利用密钥管理服务KMS（Key Management Service）加密云盘。在加密解密的过程中，实例的性能几乎没有衰减。启用加密功能的云盘性能会低于未开启加密功能的云盘，并根据上层应用的不同，性能下降的幅度也不同。

- 使用加密的系统盘（或镜像）创建ECS实例后，ECS实例操作系统内数据会被自动加密，并在读取数据时自动解密。具体操作，请参见[加密系统盘](https://help.aliyun.com/zh/ecs/user-guide/encrypt-a-system-disk)。
- 创建加密的数据盘并将其挂载到ECS实例后，以下数据会被自动加密，并在读取数据时自动解密。具体操作，请参见[加密数据盘](https://help.aliyun.com/zh/ecs/user-guide/encrypt-a-data-disk)。加密云盘中的静态数据。加密云盘和实例间传输的数据（不包括操作系统内的数据）。加密云盘从实例传递到后端存储集群的数据。从加密云盘创建的所有快照，并且该快照的加密密钥与云盘的加密密钥保持相同。从加密快照创建的所有云盘。

### 容器服务ACK

#### Secret落盘加密

在ACK Pro托管集群中，您可以使用在阿里云密钥管理服务KMS（Key Management Service）中创建的密钥加密Kubernetes Secret密钥。使用阿里云密钥管理服务（KMS）中管理的密钥对ACK Pro集群中的Kubernetes Secret密钥数据进行落盘加密，详情参见[使用阿里云KMS进行Secret的落盘加密](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2)。

#### 加密OSS存储卷

阿里云对象存储OSS（Object Storage Service）是阿里云提供的海量、安全、低成本、高持久的云存储服务，您可以在容器服务Kubernetes集群中使用阿里云OSS存储卷。可以使用KMS（Key Management Service）托管的CMK（Customer Master Key）或OSS完全托管密钥功能对阿里云容器服务ACK集群的OSS存储卷数据加密，详情参见[加密OSS存储卷](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume)。

#### 加密云盘存储卷

云盘是阿里云为云服务器ECS提供的数据块级别的块存储产品，具有低时延、高性能、持久性、高可靠等特点。可以在阿里云容器服务Kubernetes集群中使用阿里云云盘存储卷，使用阿里云密钥管理服务KMS（Key Management Service）中管理的密钥对集群中的云盘存储卷数据加密，详情参见[加密云盘存储卷](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/encrypt-cloud-disk-storage-volumes)。

### 数据库

#### 加密方式

| **对比项** | **SSL链路加密** | **透明数据加密（TDE）** | **云盘加密** | [数据库全加密](https://help.aliyun.com/zh/rds/overview) |
| --- | --- | --- | --- | --- |
| 加密方式 | 在客户端和数据库实例之间对传输的数据进行加密。 | 在数据被写入存储设备或存储服务时对数据进行加密。 | 针对云盘版实例，阿里云提供云盘加密功能，基于块存储对整个数据盘进行加密。 | 在全链路（从客户端至数据库实例，含网络、内存和存储）中对数据进行加密。 |
| 明文数据可见范围 | 数据在数据库实例中（含内存和存储）均为明文。 | 数据在参与计算前需要被解密，所以其在CPU、缓存和内存中是明文形式。 | 数据在云盘之外时是明文。 | 数据全程为密文形式，仅在**Intel SGX 安全增强型**规格实例内参与计算时被解密为明文。 |
| 安全性 | 保护数据的通信不被窃听。 | 保护存储中的数据。 | 保护云盘中数据的安全。 | 保护全链路中的数据安全。 |

#### 产品加密支持

下文中的产品加密支持情况、前提条件、注意事项等可能**存在变化**，实际选择时请以**官网说明为准**。

##### RDS MySQL

| **加密项** | **支持情况** | **前提条件** | **注意事项** |
| --- | --- | --- | --- |
| [SSL链路加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption) | 支持 | 实例版本如下：MySQL 8.0三节点企业版MySQL 8.0高可用版MySQL 5.7三节点企业版MySQL 5.7高可用版MySQL 5.6 | SSL的证书有效期为1年，即将到期时，阿里云将会通过短信、邮件、站内信（事件中心）的方式进行提醒，并会在特定时间段自动更新该证书。更新过程会造成实例闪断，您可以通过配置**计划时间配置**自定义证书更新时间。更多信息，请参见[计划内事件](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/manage-scheduled-events-2)。由于SSL加密的实现原理，启用SSL加密会显著增加CPU使用率，建议您仅在外网链路有加密需求的时候启用SSL加密。内网链路相对较安全，一般无需对链路加密。读写分离地址不支持SSL加密。关闭SSL加密后，仅支持通过非SSL方式连接。关闭SSL加密会重启实例，请谨慎操作。 |
| [透明数据加密（TDE）](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/configure-tde-for-an-apsaradb-rds-for-mysql-instance) | 支持 | 实例类型如下：RDS MySQL 8.0**高可用版本地盘**实例（内核小版本20191015及以上）RDS MySQL 5.7**高可用版本地盘**实例（内核小版本20191015及以上）RDS MySQL 5.6已开通KMS。如果您未开通KMS，可在开通TDE过程中根据引导开通KMS。 | 为保证实例的稳定性，建议您将内核小版本升级到最新。如果主实例包含只读实例，建议将所有只读实例和主实例的内核小版本都升级到最新。更多信息，请参见[升级内核小版本](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/update-the-minor-engine-version-of-an-apsaradb-rds-for-mysql-instance)。TDE开通过程中会重启实例造成闪断，请做好业务安排，谨慎操作。TDE开通后无法关闭。TDE开通后无法修改密钥。TDE开通后，用户如果要恢复数据到本地，需要先通过RDS[解密数据](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/configure-tde-for-an-apsaradb-rds-for-mysql-instance)。TDE开通后，会显著增加CPU使用率。使用已有自定义密钥时，需要注意：禁用密钥、设置密钥删除计划或者删除密钥材料都会造成密钥不可用。撤销授权关系后，重启RDS实例会导致RDS实例不可用。需要使用主账号或者具有AliyunSTSAssumeRoleAccess权限的账号。 |
| [云盘加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/configure-the-disk-encryption-feature-for-an-apsaradb-rds-for-mysql-instance) | 支持 | 仅在[创建RDS MySQL实例](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/create-an-apsaradb-rds-for-mysql-instance)时可以开启云盘加密，创建实例后无法开启。创建实例时[存储类型](https://help.aliyun.com/zh/rds/product-overview/storage-types)需要为**ESSD云盘**。创建实例时[产品系列](https://help.aliyun.com/zh/rds/overview-11)需要为**高可用版**。 | 云盘加密功能开启后无法关闭。开启云盘加密的实例不支持[跨地域备份](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/use-the-cross-region-backup-feature-of-an-apsaradb-rds-for-mysql-instance)。云盘加密不会影响您的业务，应用程序也无需修改。开启云盘加密后，实例生成的快照以及通过这些快照创建的云盘版实例将自动延续加密属性。[密钥管理服务KMS](https://help.aliyun.com/zh/kms/key-management-service/support/what-is-key-management-service)欠费会导致云盘无法解密，整个实例不可用，请确保KMS状态正常。如果您禁用或删除了KMS密钥，将会导致使用了该KMS密钥的RDS实例无法正常工作，受影响的操作包括创建快照、恢复快照和备库重建等。 |
| **数据库全加密** | 不支持 | - | - |

##### RDS PostgreSQL

| **加密项** | **支持情况** | **前提条件** | **注意事项** |
| --- | --- | --- | --- |
| [SSL链路加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/configure-ssl-encryption-for-an-apsaradb-rds-for-postgresql-instance) | 支持 | 实例为RDS PostgreSQL 10或以上的**云盘版本**。已下载[pgAdmin 4客户端](https://www.pgadmin.org/download/)。 | 开启SSL链路加密后，会造成CPU使用率上升、读写时延增长。开启SSL链路加密后，已有连接需要断开重连，加密才会生效。开启云端证书、更改云端证书保护的连接地址或关闭SSL链路加密，将会重启您的数据库实例，用时约3分钟左右，请在业务低峰期操作。 |
| **透明数据加密（TDE）** | 不支持 | - | - |
| [云盘加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance) | 支持 | 云盘加密只能在创建实例时开启，您必须参照[设置云盘加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance)进行设置，才能在创建实例时设置云盘加密。创建实例时，产品系列、存储类型和规格分类需要按照以下要求配置：产品系列：高可用版存储类型：SSD云盘或ESSD云盘规格分类：独享规格 | 云盘加密功能开启后无法关闭。开启云盘加密的实例不支持[跨地域备份](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance)。云盘加密不会影响您的业务，应用程序也无需修改。开启云盘加密后，实例生成的快照以及通过这些快照创建的云盘版实例将自动延续加密属性。[密钥管理服务KMS](https://help.aliyun.com/zh/kms/key-management-service/support/what-is-key-management-service)欠费会导致云盘无法解密，整个实例不可用，请确保KMS状态正常。如果您禁用或删除了KMS密钥，将会导致使用了该KMS密钥的RDS实例无法正常工作，受影响的操作包括创建快照、恢复快照和备库重建等。 |
| [数据库全加密](https://help.aliyun.com/zh/rds/overview) | 支持 | Intel SGX 安全增强型规格及非Intel SGX 安全增强型规格支持情况有差异，详情请查看[功能支持](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/supported-features)。 | 暂不支持明文列与密文列混合运算。全加密功能不提供用户主密钥的生成和备份服务，您需要自行生成用户主密钥。一旦您丢失密钥，将无法再访问已有的数据。因此我们建议您妥善备份用户主密钥。详情请查看[功能支持](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/supported-features)。 |

##### RDS SQL Server

| **加密项** | **支持情况** | **前提条件** | **注意事项** |
| --- | --- | --- | --- |
| [SSL链路加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/configure-ssl-encryption-for-an-apsaradb-rds-for-sql-server-instance) | 支持 | - | SSL的证书有效期为1年，请在1年内更新证书有效期，否则使用加密连接的客户端程序将无法正常连接。由于SSL加密的固有缺陷，启用SSL加密会显著增加CPU使用率，建议您仅在外网链路有加密需求的时候启用SSL加密。内网链路相对较安全，一般无需对链路加密。开启SSL加密后，将无法再关闭，请谨慎操作。读写分离地址不支持SSL加密。 |
| [透明数据加密（TDE）](https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/configure-tde-for-an-apsaradb-rds-for-sql-server-instance) | 支持 | 实例版本如下：SQL Server 2019 标准版SQL Server 企业版实例规格为通用规格或独享规格。实例不是[只读实例](https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/create-a-read-only-apsaradb-rds-for-sql-server-instance)。如果您使用自有密钥，请提前准备加密证书、私钥以及密码。 | 实例级别的TDE只能开通，无法关闭。数据库级别的TDE可以开通或关闭。如果您使用阿里云提供的服务密钥，开通TDE后，要恢复数据到本地，需要先通过RDS[关闭TDE](https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/configure-tde-for-an-apsaradb-rds-for-sql-server-instance)。关闭TDE后，还存在部分未解密的事务日志，此时下载的备份文件仍处于加密状态，无法直接用于恢复。如需下载解密后的备份文件，请在实例完成三次日志备份和一次全量备份后，再下载最新的全量备份文件。更多信息，请参见[Database Encryption in SQL Server 2008 Enterprise Edition](https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008/cc278098(v=sql.100)?redirectedfrom=MSDN)。关于如何设置日志备份和数据备份，请参见[备份SQL Server数据](https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/back-up-an-apsaradb-rds-for-sql-server-instance)。开启TDE后，会显著增加CPU使用率。 |
| [云盘加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/configure-disk-encryption-for-an-apsaradb-rds-for-sql-server-instance) | 支持 | 实例不是[共享规格实例](https://help.aliyun.com/zh/rds/product-overview/instance-families)。仅在创建实例时可以开启云盘加密，创建实例后无法开启。创建实例时[存储类型](https://help.aliyun.com/zh/rds/product-overview/storage-types)需要为SSD云盘或ESSD云盘。 | 云盘加密功能开启后无法关闭。开启云盘加密的实例不支持[跨地域备份](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/use-the-cross-region-backup-feature-for-an-apsaradb-rds-for-postgresql-instance)。云盘加密不会影响您的业务，应用程序也无需修改。开启云盘加密后，实例生成的快照以及通过这些快照创建的云盘版实例将自动延续加密属性。[密钥管理服务KMS](https://help.aliyun.com/zh/kms/key-management-service/support/what-is-key-management-service)欠费会导致云盘无法解密，整个实例不可用，请确保KMS状态正常。如果您禁用或删除了KMS密钥，将会导致使用了该KMS密钥的RDS实例无法正常工作，受影响的操作包括创建快照、恢复快照和备库重建等。 |
| **数据库全加密** | 不支持 | - | - |

##### 云数据库Redis

| **加密项** | **支持情况** | **前提条件** | **注意事项** |
| --- | --- | --- | --- |
| [SSL链路加密](https://help.aliyun.com/zh/redis/user-guide/configure-ssl-encryption) | 支持 | Redis实例为**本地盘**实例，更多信息，请参见[本地盘和云盘实例对比](https://help.aliyun.com/zh/redis/product-overview/comparison-between-tair-instances-that-cloud-native-and-classic)。Redis实例为4.0或5.0版本（[集群架构](https://help.aliyun.com/zh/redis/product-overview/cluster-master-replica-instances)）。 | SSL的证书有效期为1年，请及时更新证书有效期并重新下载配置CA证书，否则使用加密连接的客户端程序将无法正常连接。由于开通SSL加密会增加Redis服务的网络响应时间，建议仅在有加密需求时才开通SSL加密（例如通过公网连接Redis实例）。执行开通SSL加密和更新证书有效期的操作将触发重启实例动作。实例会出现秒级的连接闪断，请在业务低峰期执行该操作并确保应用具备重连机制。开通SSL后同时支持SSL和非SSL两种连接方式。 |
| [透明数据加密（TDE）](https://help.aliyun.com/zh/redis/user-guide/enable-tde) | 支持 | Redis实例为**本地盘版的**[性能增强型](https://help.aliyun.com/zh/redis/product-overview/dram-based-instances)**实例**。Redis实例的小版本为1.7.1及以上，查看及升级小版本的方法，请参见[升级小版本](https://help.aliyun.com/zh/redis/user-guide/update-the-minor-version)。 | TDE的开启粒度为实例级别，不支持Key（键）或DB（库）粒度的控制。TDE加密对象为数据落盘文件（即RDB备份文件，如dump.rdb）。TDE所使用的密钥，由[密钥管理服务KMS](https://help.aliyun.com/zh/kms/key-management-service/support/what-is-key-management-service)（Key Management Service）统一生成和管理，云数据库Redis不提供加密所需的密钥和证书。 |
| **云盘加密** | 不支持 | - | - |
| **数据库全加密** | 不支持 | - | - |

##### 云数据库MongoDB

| **加密项** | **支持情况** | **前提条件** | **注意事项** |
| --- | --- | --- | --- |
| [SSL链路加密](https://help.aliyun.com/zh/mongodb/user-guide/configure-ssl-encryption-for-an-apsaradb-for-mongodb-instance) | 支持 | MongoDB 3.4及以上版本的副本集实例。 | SSL CA证书仅支持通过云数据库MongoDB控制台下载。开通SSL加密会增加云数据库MongoDB实例的CPU使用率，建议您有加密需求（例如通过公网连接MongoDB实例）时开通SSL加密。开通SSL后支持SSL和非SSL两种连接方式。 |
| [透明数据加密（TDE）](https://help.aliyun.com/zh/mongodb/user-guide/configure-tde-for-an-apsaradb-for-mongodb-instance) | 支持 | 实例架构为副本集实例或分片集群实例。实例的存储引擎为WiredTiger。实例的数据库版本为4.0或4.2版本。如果实例数据库版本过低，您可以[升级数据库版本](https://help.aliyun.com/zh/mongodb/user-guide/upgrade-the-major-version-of-an-apsaradb-for-mongodb-instance)。 | 开通TDE功能的过程中，实例会重启一次并出现连接闪断，建议您在业务低峰期操作并确保应用有重连机制。开通TDE功能后，会增加实例的CPU使用率。加密后的集合不再支持通过物理备份恢复至自建数据库。如果您需要将加密后的集合恢复到自建数据库，您可以通过逻辑备份恢复至自建数据库，具体请参见[通过逻辑备份恢复至自建数据库](https://help.aliyun.com/zh/mongodb/user-guide/restore-data-of-an-apsaradb-for-mongodb-instance-to-a-self-managed-mongodb-database-by-using-logical-backup)。TDE功能开通后无法关闭。已开通TDE功能的实例释放后，不支持从**回收站**中恢复。当前TDE功能的开通粒度为实例，仅支持对集合进行加密。如果您需要对字段进行加密，请参见[手动字段级加密](https://docs.mongodb.com/manual/core/security-explicit-client-side-encryption/)（仅支持MongoDB 4.2版本实例）。如果业务上有特殊需求，您可以在创建集合时，指定该集合不被加密。如何设置，请参见[设置指定的集合不被加密](https://help.aliyun.com/zh/mongodb/user-guide/configure-tde-for-an-apsaradb-for-mongodb-instance)。TDE功能开通后，仅加密新创建的集合，已有的集合不会被加密。TDE功能所使用的密钥，由密钥管理服务KMS（Key Management Service）统一生成和管理，云数据库MongoDB不提供加密所需的密钥和证书。密钥管理服务KMS的更多信息，请参见[什么是密钥管理服务](https://help.aliyun.com/zh/kms/key-management-service/support/what-is-key-management-service)。 |
| **云盘加密** | 不支持 | - | - |
| **数据库全加密** | 不支持 | - | - |

#### 配置合规审计

[配置审计（Config）](https://help.aliyun.com/zh/document_detail/127388.html)是一项资源审计服务，为客户提供面向资源的**配置历史追踪**、**配置合规审计**等能力。面对大量资源，帮您轻松实现基础设施的自主监管，确保持续性合规。建议在配置审计中启用数据库合规管理最佳实践合规包，帮助客户实现数据库持续合规，详细合规规则参见[数据库合规管理最佳实践](https://help.aliyun.com/zh/document_detail/312332.html)。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 数字证书管理服务 | [数字证书管理服务（Certificate Management Service）](https://help.aliyun.com/zh/ssl-certificate/product-overview/what-is-certificate-management-service)是由阿里云联合全球多家数字证书颁发机构，在阿里云平台上直接提供数字证书申请、管理、部署等的服务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ssl-certificate/cas-billing-overview)。 |
| 密钥管理服务KMS | [密钥管理服务KMS（Key Management Service）](https://help.aliyun.com/zh/kms/key-management-service/support/what-is-key-management-service)是您的一站式密钥管理和数据加密服务平台，提供简单、可靠、安全、合规的数据加密保护能力。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/kms/key-management-service/support/billing-1-1/)。 |
| 负载均衡 | [负载均衡SLB（Server Load Balancer）](https://help.aliyun.com/zh/slb/product-overview/slb-overview)是一种对流量进行按需分发的服务，通过将流量分发到不同的后端服务器来扩展应用系统的吞吐能力，并且可以消除系统中的单点故障，提升应用系统的可用性。[应用型负载均衡ALB](https://help.aliyun.com/zh/slb/application-load-balancer/what-is-alb)、[传统型负载均衡CLB](https://help.aliyun.com/zh/slb/classic-load-balancer/product-overview/what-is-clb/)均为SLB产品家族成员。 | 收费，详情参见[ALB产品计费](https://help.aliyun.com/zh/slb/alb-billing/)、[CLB产品计费](https://help.aliyun.com/zh/document_detail/27691.html)。 |
| 对象存储OSS | [阿里云对象存储OSS（Object Storage Service）](https://help.aliyun.com/zh/oss/user-guide/what-is-oss)是一款海量、安全、低成本、高可靠的云存储服务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/oss/billing/)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是阿里云提供的性能卓越、稳定可靠、弹性扩展的IaaS（Infrastructure as a Service）级别云计算服务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)。 |
| 关系型数据库RDS | [阿里云关系型数据库RDS（Relational Database Service）](https://help.aliyun.com/zh/rds/product-overview/what-is-apsaradb-rds-what-is-apsaradb-rds)是一种稳定可靠、可弹性伸缩的在线数据库服务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/rds/product-overview/billing-1/)。 |
| 云数据库Redis | [云数据库Redis版（ApsaraDB for Redis）](https://help.aliyun.com/zh/redis/product-overview/what-is-apsaradb-for-redis)是兼容开源Redis协议标准、提供混合存储的数据库服务，基于双机热备架构及集群架构，可满足高吞吐、低延迟及弹性变配等业务需求。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/redis/product-overview/billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| SSL证书 | SSL证书采用SSL协议进行通信，是由权威机构颁发给网站的可信凭证，具有网站身份验证和加密传输双重功能。SSL证书指定了在应用程序协议（例如，HTTP、Telnet、FTP）和TCP/IP之间提供数据安全性分层的机制。它是在传输通信协议（TCP/IP）上实现的一种安全协议，采用公开密钥技术为TCP/IP连接提供数据加密、服务器认证、消息完整性以及可选的客户机认证。 |
| HTTPS | HTTPS也就是HTTP+SSL，基于SSL协议的网站加密传输协议，是HTTP的安全版。您的网站安装SSL证书后，将会通过HTTPS加密协议来传输数据，HTTPS加密传输协议可激活客户端浏览器到网站服务器之间的SSL加密通道（SSL协议），从而实现高强度双向加密传输，防止传输数据被泄露或篡改。 |
| TDE | 透明数据加密TDE（Transparent Data Encryption），即对数据文件执行实时I/O加密和解密。数据在写入磁盘之前进行加密，从磁盘读入内存时进行解密。TDE不会增加数据文件的大小，开发人员无需更改任何应用程序，即可使用TDE功能。 |
| 云盘加密 | 云盘加密功能，基于块存储对整个数据盘进行加密，即使数据备份泄露也无法解密，保护您的数据安全。 |

## 安全性

### 密钥管理服务KMS安全合规

KMS经过严格的安全设计和审核，保证您的密钥在阿里云得到最严格的保护，详情参见KMS[安全与合规能力](https://help.aliyun.com/zh/kms/key-management-service/support/benefits-1)。

- KMS仅提供基于TLS的安全访问通道，并且仅使用安全的传输加密算法套件，符合PCI DSS等安全规范。
- KMS提供了监管机构许可和认证的密码设施。根据地域分布，分别提供了经国家密码管理局检测和认证的硬件密码设备，取得了FIPS 140-2第三级认证和运行在FIPS许可的第三级模式下的密码设备。更多信息，请参见[合规](https://help.aliyun.com/zh/kms/key-management-service/support/overview-12)。
- KMS使用硬件安全模块来托管密钥，从而达到更高的安全标准，更多信息，请参见[托管密码机概述](https://help.aliyun.com/zh/kms/key-management-service/support/overview-12)。

### 数字证书管理服务安全性

阿里云证书服务采用密钥管理系统对私钥进行加密存储，以保证您证书私钥的安全。无论是您上传的证书及私钥，还是申请证书时使用系统创建CSR生成的私钥，阿里云证书服务都会采用经过权威机构认证的密钥管理系统进行加密存储，详情参见[阿里云SSL证书私钥保护原理](https://help.aliyun.com/zh/ssl-certificate/how-does-certificate-management-service-protect-private-keys)。

## 注意事项

### SSL证书到期说明

每张SSL证书都有其生命周期。从2020年09月01日起，所有CA中心签发的SSL证书有效期最长为397天。为了降低证书过期对网站业务的影响，在证书即将过期时，阿里云会向您发送续费提醒，并提供证书续费功能。本文介绍SSL证书到期的影响以及需要进行的操作详情参见[证书到期说明](https://help.aliyun.com/zh/ssl-certificate/renewal-notification-policies)。

### 密钥管理服务KMS使用限制

- KMS的使用存在限制，限制详情参见[使用限制](https://help.aliyun.com/zh/kms/key-management-service/support/limits)。
- KMS是一个区域化的服务，在不同地域的使用限制相对独立，关于KMS支持的地域，请参见[支持的地域](https://help.aliyun.com/zh/kms/key-management-service/make-api-requests-3)。
- KMS密钥管理可使用密钥服务（共享版）、专属基础版、专属标准版，差异详情参见[专属KMS基础版和标准版的差异](https://help.aliyun.com/zh/kms/key-management-service/support/differences-between-dedicated-kms-of-the-basic-edition-and-dedicated-kms-of-the-standard-edition)、[密钥服务](https://help.aliyun.com/zh/kms/key-management-service/support/key-service-1/)。
- 在选用KMS专属版时请咨询相应的安全PDSA。

### 加密方式差异

不同规格或版本的云产品实例支持的加密方式存在差异，请参考方案架构中的说明便于快速了解，最终以官网产品说明为准。

## 实施步骤

### 实施准备

- 已有阿里云账号，如果没有请进行[账号注册](https://help.aliyun.com/zh/account/ali-cloud-account-registration-process)。
- 已有域名，在阿里云购买域名详情参见[域名注册](https://help.aliyun.com/zh/dws/user-guide/quick-start-1)。

### 操作步骤

#### 管理SSL证书

如果用户没有SSL证书可以先在数字证书管理服务中购买证书实例，填写申请相关信息后进行证书申请。如果用户已经通过服务上购买并签发了SSL证书，可以在证书服务中进行证书上传，上传后可以将其部署到阿里云产品或进行统一管理。

##### 购买SSL证书

阿里云提供了多种品牌和类型的证书，用户可以根据实际需要在阿里云数字证书管理服务购买所需的SSL证书，金融企业建议购买**EV类型**的证书。

1. 登录[数字证书管理服务控制台](https://yundunnext.console.aliyun.com/?p=cas)。
2. 在左侧导航栏，单击**SSL证书**。
3. 在**SSL证书**页面，单击**购买证书**。
4. 在**立即购买**面板，参考[购买指导](https://help.aliyun.com/zh/ssl-certificate/purchase-an-ssl-certificate)完成证书购买。

##### 申请证书

使用已购买的证书实例，可以直接申请单域名、通配符域名和多域名（最多包含5个单域名）证书。不支持直接申请 **多通配符域名证书** 、 **混合域名证书** 。对于OV、**EV证书**，可以在获得多个证书实例后，使用证书合并功能来申请多通配符域名证书、混合域名证书。

阿里云数字证书管理服务会将您提交的申请信息（证书绑定的域名、联系人信息等）发送到CA中心进行审核。如果您申请的是非国产品牌的证书（例如GeoTrust、DigiCert等），您的申请信息会被发送到中国境外的CA公司。

申请的详细操作步骤参见[申请证书](https://help.aliyun.com/zh/ssl-certificate/issue-certificates/)。

##### 上传证书

如果用户已经通过第三方证书服务商购买并签发了SSL证书，希望将已有证书部署到阿里云产品（或者计划使用数字证书管理服务统一管理所有证书），那么可以使用数字证书管理服务的上传证书功能，上传操作步骤详情参见[上传证书](https://help.aliyun.com/zh/ssl-certificate/upload-an-ssl-certificate)。

##### 共享证书

多账号场景下，在数字证书管理服务购买的证书可以帮用户实现在不同阿里云账号（归属于同一个经过实名认证的个人或企业用户）之间共享证书。如果是已有第三方证书并在数字证书管理服务中上传的证书目前无法进行共享，多账号场景下可以分别登录目标账号的证书管理服务进行证书上传。共享证书的详细操作步骤参见[证书共享](https://help.aliyun.com/zh/document_detail/305605.html)。

#### 使用KMS管理密钥

下文对使用KMS管理密钥操作进行介绍，操作前请先查看注意事项章节中的**KMS相关注意事项及限制**。

##### 使用专属KMS基础版管理密钥

专属KMS基础版具备用户侧数据加密能力，将密钥单独存储在租户独享的数据库中，通过可选的凭据管家服务组件提供凭据的全生命周期管理和安全便捷的应用访问，同时支持云产品原生的数据加密。密钥管理详细操作请参考[快速入门](https://help.aliyun.com/zh/kms/key-management-service/support/quick-start-2)及[基础操作](https://help.aliyun.com/zh/kms/key-management-service/support/basic-operations/)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4476581571/p969798.png)

##### 使用专属KMS标准版管理密钥

专属KMS标准版具备用户侧数据加密能力和加密服务密码机集群加密能力，将密钥存储在您的独享密码机集群内，通过可选的凭据管家服务组件提供凭据的全生命周期管理和安全便捷的应用访问，同时支持云产品原生的数据加密。密钥管理详细操作请参考[快速入门](https://help.aliyun.com/zh/kms/key-management-service/support/connect-applications-to-the-dedicated-kms-instance-of-the-standard-edition)及[基础操作](https://help.aliyun.com/zh/kms/key-management-service/support/basic-operations-1/)。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4476581571/p969815.png)

##### 同账号多VPC访问同一专属KMS实例

同账号访问，例如账号A的多个VPC访问账号A的同一专属KMS实例。更多详细操作可参见[配置多VPC访问同一专属KMS实例](https://help.aliyun.com/zh/kms/key-management-service/support/manage-dedicated-kms-instances-of-the-basic-edition)。

1. 登录[密钥管理服务控制台](https://kms.console.aliyun.com/)。
2. 在页面左上角的地域下拉列表，选择专属KMS实例所在的地域。
3. 在左侧导航栏，单击**专属KMS**。
4. 单击目标实例**专有网络**列的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4476581571/p969817.png)图标。
5. 在**配置专有网络**对话框，选中**待选专有网络**中需要设置的专有网络，单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4476581571/p969820.png)图标，选择该VPC内的一个交换机，单击**确定**。

说明：

- 您可以单击目标实例**操作**列的**详情**，在**服务规格**中会显示当前实例支持关联的VPC数量。
- 如果选择关联的VPC数量超过了关联资源限制，您可以根据控制台上的提示，单击**前往购买**升级**专有网络数量**的规格。

##### 跨账号多VPC访问同一专属KMS实例

跨账号访问，例如账号B的多个VPC访问账号A的同一专属KMS实例。

1. 配置账号间VPC资源共享。具体操作，请参见[将资源共享给任意账号](https://help.aliyun.com/zh/resource-management/resource-sharing/getting-started/share-resources-with-an-account)。**说明** 您也可以根据业务需要仅在资源目录内共享VPC资源。具体操作，请参见[仅在资源目录内共享资源](https://help.aliyun.com/zh/resource-management/resource-sharing/getting-started/share-resources-with-objects-in-a-resource-directory)。
2. 使用账号B登录资源管理控制台，创建共享单元，向账号A共享需要访问专属KMS实例的VPC内的交换机资源。
3. 使用账号A登录资源管理控制台，接受账号B的共享邀请。
4. 使用账号A登录密钥管理服务控制台，具体操作，请参见上文同账号多VPC访问同一专属KMS实例。

#### ALB/CLB链路加密

##### ALB HTTPS全链路加密

ALB提供全链路HTTPS加密功能，可以实现客户端到ALB、**ALB到后端服务器之间的HTTPS加密通信**，提升**敏感业务**的安全性。操作步骤详情可参见[配置全链路HTTPS访问实现加密通信](https://help.aliyun.com/zh/slb/application-load-balancer/end-to-end-data-transfer-over-https)。

##### ALB HTTPS双向认证

当金融企业在处理一些**关键业务**时，HTTPS双向认证通过对通信双方做双向认证为业务提供更高的安全性，**ALB支持实现HTTPS双向认证**，操作步骤详情可参见[使用ALB部署HTTPS业务（双向认证](https://help.aliyun.com/zh/slb/application-load-balancer/configure-mutual-authentication-on-an-https-listener)）。

注意：仅支持标准版的ALB实例打开双向认证并创建CA证书，基础版的ALB实例不支持双向认证。

##### CLB HTTPS双向认证

当金融企业在处理一些**关键业务**时，HTTPS双向认证通过对通信双方做双向认证为业务提供更高的安全性，**CLB支持部署HTTPS双向认证**，操作步骤详情可参见[使用CLB部署HTTPS业务（双向认证）](https://help.aliyun.com/zh/slb/classic-load-balancer/use-cases/configure-mutual-authentication-on-an-https-listener-1)。

#### OSS加密及防护

##### 服务端加密

OSS服务端加密操作步骤详情可参见[服务端加密](https://help.aliyun.com/zh/oss/user-guide/server-side-encryption-8)。

##### 客户端加密

OSS客户端加密操作步骤详情参见[客户端加密](https://help.aliyun.com/zh/oss/user-guide/client-side-encryption)。

##### 配置合规审计

在配置审计中启用的OSS合规包模板名称为“OSS合规管理最佳实践模板”，操作步骤详情参见[启用合规包](https://help.aliyun.com/zh/document_detail/194757.html)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4476581571/p969800.png)

##### 接入WAF

通过自定义域名访问OSS中的文件，操作步骤详情参见[绑定自定义域名](https://help.aliyun.com/zh/oss/user-guide/access-buckets-via-custom-domain-names)。使用WAF对OSS中的文件域名进行防护，操作详情参见WAF [CNAME接入](https://help.aliyun.com/zh/waf/web-application-firewall-2-0/user-guide/website-access-with-cname/)。

##### 防盗链

OSS支持对存储空间（Bucket）设置防盗链，即通过对访问来源设置白名单的机制，避免OSS资源被其他人盗用，操作详情参见[防盗链](https://help.aliyun.com/zh/oss/user-guide/hotlink-protection)。

#### ECS云盘加密

ECS被加密的云盘可以是系统盘和数据盘，系统盘操作详情参见[加密系统盘](https://help.aliyun.com/zh/ecs/user-guide/encrypt-a-system-disk)，数据盘加密操作详情参见[加密数据盘](https://help.aliyun.com/zh/ecs/user-guide/encrypt-a-data-disk)。

#### 容器服务ACK加密

##### Secret落盘加密

Secret落盘加密操作详情参见[使用阿里云KMS进行Secret的落盘加密](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2)。

##### 加密OSS存储卷

对OSS存储卷加密操作详情参见[加密OSS存储卷](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume)。

##### 加密云盘存储卷

对ACK集群中的云盘存储卷数据加密操作详情参见[加密云盘存储卷](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/encrypt-cloud-disk-storage-volumes)。

#### 数据库加密

##### RDS MySQL

- SSL加密操作详情参见[设置SSL加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption)。
- 透明数据加密TDE操作详情参见[设置透明数据加密TDE](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/configure-tde-for-an-apsaradb-rds-for-mysql-instance)。
- 云盘加密操作详情参见[云盘加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/configure-the-disk-encryption-feature-for-an-apsaradb-rds-for-mysql-instance)。

##### RDS PostgreSQL

- SSL加密操作详情参见[设置SSL加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/configure-ssl-encryption-for-an-apsaradb-rds-for-postgresql-instance)。
- 云盘加密操作详情参见[云盘加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/configure-disk-encryption-for-an-apsaradb-rds-for-postgresql-instance)。
- 全加密操作详情参见[全加密数据库](https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/fully-encrypted-database)。

##### RDS SQL Server

- SSL加密操作详情参见[设置SSL加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/configure-ssl-encryption-for-an-apsaradb-rds-for-sql-server-instance)。
- 透明数据加密TDE操作详情参见[设置透明数据加密TDE](https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/configure-tde-for-an-apsaradb-rds-for-sql-server-instance)。
- 云盘加密操作详情参见[云盘加密](https://help.aliyun.com/zh/rds/apsaradb-rds-for-sql-server/configure-disk-encryption-for-an-apsaradb-rds-for-sql-server-instance)。

##### 云数据库Redis

- SSL加密操作详情参见[设置SSL加密](https://help.aliyun.com/zh/redis/user-guide/configure-ssl-encryption)。
- 透明数据加密TDE操作详情参见[设置透明数据加密TDE](https://help.aliyun.com/zh/redis/user-guide/enable-tde)。

##### 云数据库MongoDB

- SSL加密操作详情参见[设置SSL加密](https://help.aliyun.com/zh/mongodb/user-guide/configure-ssl-encryption-for-an-apsaradb-for-mongodb-instance)。
- 透明数据加密TDE操作详情参见[设置透明数据加密TDE](https://help.aliyun.com/zh/mongodb/user-guide/configure-tde-for-an-apsaradb-for-mongodb-instance)。

#### 配置合规审计

在配置审计中启用数据库合规包模板名称为“数据库合规管理最佳实践”，操作步骤详情参见[启用合规包](https://help.aliyun.com/zh/document_detail/194757.html)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4476581571/p969823.png)

## 故障排除

### 密钥管理服务

#### 密钥管理服务的端点为何无法访问？

密钥管理服务的端点无法访问，通常是因为在使用 SDK 访问密钥管理服务时，未启用 HTTPS 协议。

为了确保您的数据安全，密钥管理服务**仅支持** HTTPS 协议。因此在使用 SDK 访问密钥管理服务时，确保启用 HTTPS 协议。

#### 解密时为何出现 Forbidden.KeyNotFound 的错误？

解密时出现上述错误提示，通常是因为您解密时访问了错误的地域。

由于各个地域的密钥管理服务是完全独立的，请您确保解密时访问的地域与加密时一致。

### 数字证书管理服务

数字证书管理服务问题详情参见[常见问题](https://help.aliyun.com/zh/ssl-certificate/faq-4)。

### OSS常见问题

OSS服务问题详情参见[常见问题](https://help.aliyun.com/zh/oss/faq-overview)。

### RDS常见问题

#### RDS MySQL开启TDE后，常用数据库工具（Navicat等）还能正常使用吗？

可以正常使用。

#### RDS MySQL开启TDE后，还能正常迁移数据到其他RDS实例吗？

可以正常迁移。

#### RDS MySQL加密后查看数据为什么还是明文的？

查询数据时会解密并读取到内存，所以是明文显示。开启TDE可以防止备份泄露导致数据泄露，备份文件是加密的，无法用于恢复到本地，如果要恢复数据到本地，需要先解密数据。

#### RDS MySQL SSL证书到期后不更新会有什么影响？会影响实例运行或数据安全吗？

SSL证书到期后不更新，仅会导致使用加密连接的客户端程序无法正常连接实例，不会影响实例运行或数据安全。

#### RDS MySQL SSL在Java中使用JKS证书文件时，报错Javax.net.ssl.SSLHandshakeException: DHPublicKey does not comply to algorithm constraints，如何处理？

jdk7和jdk8若不修改jdk安全配置，会报此错误，其它类似报错，一般也都由Java安全配置导致。需要修改默认的jdk安全配置，在应用程序所在主机的**jre/lib/security/Java.security**文件中，修改如下两项配置：

```
jdk.tls.disabledAlgorithms=SSLv3, RC4, DH keySize < 224
jdk.certpath.disabledAlgorithms=MD2, RSA keySize < 1024
```

### Redis常见问题

#### 下载了加密后的RDB数据文件，如何进行解密？

目前无法解密，您可以将备份集恢复至新实例，恢复完成后，数据即完成自动解密。

#### 为什么客户端读取到的数据还是明文显示的？

加密的对象是数据落盘文件（即RDB备份文件），而查询数据时读取的是内存数据（未被加密），所以是明文显示。

#### 设置SSL加密出现“版本不支持”的错误提示怎么办？

您需要将实例的小版本升级至最新，具体操作，请参见[升级小版本](https://help.aliyun.com/zh/redis/user-guide/update-the-minor-version)。

#### 设置SSL加密中下载的CA证书有哪些文件？

下载的文件为压缩包，包含如下三个文件：

- ApsaraDB-CA-Chain.p7b：用于Windows系统中导入CA证书。
- ApsaraDB-CA-Chain.pem：用于其他系统（如Linux）或应用中导入CA证书。
- ApsaraDB-CA-Chain.jks：Java中的truststore证书存储文件，用于Java程序中导入CA证书链。

## 相关内容

- [OSS最佳实践](https://help.aliyun.com/zh/oss/use-cases/)
- [KMS最佳实践](https://help.aliyun.com/zh/kms/key-management-service/support/best-practices/)
- [ALB教程](https://help.aliyun.com/zh/document_detail/213128.html)
- [CLB教程](https://help.aliyun.com/zh/document_detail/205026.html)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-123（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
