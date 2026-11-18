<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0020.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# SEC02-02 安全的登录机制

将安全的登录机制用于账号、IAM用户以及对接第三方身份提供商。

- **风险等级** 高
- **关键策略** 除了账号，确保IAM管理员（有管理员权限的IAM用户）也开启MFA机制登录，避免登录凭证泄露带来的风险。 配置IAM的登录验证策略，如会话超时策略、账号锁定策略、账号停用策略、最近登录提示等。 配置IAM的网络访问控制策略。限制用户只能从特定 IP 地址区间、网段及 VPC Endpoint 访问华为云。 多个账号或多个IAM用户间使用不同的密码。 禁止将用户的密码共享给其他人，而是为每个管理或使用华为云资源的人创建一个单独的用户。 修改新用户的默认密码。使用IAM创建新用户时，可通过邮件发送一次性登录链接给新用户，新用户使用链接进行登录时需要设置密码，另外在管理员自定义新用户的密码时可选择强制用户在激活后修改默认密码。 集中的身份管控： 使用单点登录：考虑使用单点登录解决方案，集中管理用户的身份认证信息，简化用户登录流程，提高安全性和用户体验。 多账号场景，对账号的集中管控。
- **相关云服务和工具** [IAM身份提供商](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_08_0001.html) [华为账号使用的安全最佳实践](https://support.huaweicloud.com/intl/zh-cn/bestpractice-securityInfo/securityInfo_01_0029.html) 应用身份管理服务 OneAccess：使用OneAccess与您组织的HR系统关联实现单点登录。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0020.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
