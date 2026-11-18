<!-- source: https://help.aliyun.com/zh/well-architected/personnel-identity-management/ -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706128 -->

# 人员身份管理

人员身份通常代表组织中的个人，比如企业中的安全管理员、运维管理员、应用开发者。通常通过阿里云的控制台、CLI、特定场景下的客户端等方式对云上的资源进行操作。在阿里云上，针对人员身份的管理，基于安全的最小化原则，核心有两大原则：缩短暴露时长和缩小暴露面积。

- 缩短暴露时长：使用角色扮演的临时身份替代固定身份，能极大降低身份泄漏风险，同时对于人员身份来说，也能够抽象人员权限模型，如按人员职能进行角色划分，有利于规范化人员权限设置，提升管理效率。在云上，建议通过单点登录（Single Sign-on，简称 SSO），基于角色扮演的方式，实现人员身份的管理。
- 缩小暴露面积：您需要建立安全的登录机制，包括更强的密码强度、使用多因素认证 MFA（Multi Factor Authentication）、避免混用身份等。在阿里云上，建议通过单点登录（Single Sign-on，简称 SSO）方式跟组织内的IdP进行集成，实现人员身份的统一认证。

## 最佳实践

- [为每个组织成员分配独立的身份](https://help.aliyun.com/zh/well-architected/sec01-bp02-to-assign-a-separate-identity-to-each-organization-member)
- [建立安全的登录机制](https://help.aliyun.com/zh/well-architected/sec01-bp03-establish-a-secure-login-mechanism)
- [基于统一的IdP实现人员身份的统一认证](https://help.aliyun.com/zh/well-architected/sec01-bp05-unified-authentication-of-personnel-identity-based-on-unified-idp)
- [使用用户组简化人员管理](https://help.aliyun.com/zh/well-architected/simplify-people-management-sec01-bp06-using-user-groups)
- [定期审查人员身份合理性和必要性](https://help.aliyun.com/zh/well-architected/sec01-bp07-periodic-review-of-the-reasonableness-and-necessity-of-the)

---

> 原页面：https://help.aliyun.com/zh/well-architected/personnel-identity-management/（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
