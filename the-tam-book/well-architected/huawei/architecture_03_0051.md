<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0051.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# SEC07-04 静态数据的加密

加密可以防止未经授权的人访问和窃取数据。应该默认对敏感的静态数据进行加密，以确保即使数据遭到未经授权访问或意外泄露，也能保持机密性。

- **风险等级** 高
- **关键策略** 启用默认加密。对云硬盘 EVS、关系数据库 RDS、对象存储服务 OBS、弹性文件服务 SFS等云服务配置默认加密，以自动加密存储的数据。启用RDS、DWS等数据库的加密，可降低拖库、数据泄露带来的安全风险。 针对敏感数据，采取加密、掩码、匿名化等方式进行保护。这样，即使敏感数据被非法窃取，也可降低这类数据泄露的风险。 应该监控加密和解密密钥的使用，并根据数据用途、类型和分类来选择不同的加密密钥。
- **相关云服务和工具** 密码安全中心 DEW：DEW与OBS、云硬盘（EVS）、镜像服务（IMS）等服务集成，可以通过密钥管理服务（KMS）管理这些服务的密钥，并对云服务中的数据进行加密，还可以通过KMS API完成本地数据的加密。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0051.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
