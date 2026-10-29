<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0026.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# SEC03-03 定期审视权限

定期检视和更新权限，以避免权限蔓延，持续清理无用的权限。

- **风险等级** 高
- **关键策略** 使用IAM用户组控制人员的访问权限，并设置权限的到期时间。 如果用户组的职责产生变化，应该及时调整用户组的权限。 当账号委托给另一个账号时，设置到期时间。 通过IAM用户的“最近一次登录时间”，判断该用户是否为长期未登录的用户，及时管理他们的身份凭证及权限。
- **相关云服务和工具** 统一身份认证服务 IAM

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0026.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
