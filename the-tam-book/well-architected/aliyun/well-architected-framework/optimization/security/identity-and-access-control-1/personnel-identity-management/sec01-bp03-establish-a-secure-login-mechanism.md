<!-- source: https://help.aliyun.com/zh/well-architected/sec01-bp03-establish-a-secure-login-mechanism -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706134 -->

# 建立安全的登录机制

对于人员身份的登录方式，往往是通过用户名和密码的方式进行。一旦用户名和密码泄漏，攻击者极有可能通过该身份登录阿里云，造成一些不可挽回的损失。因此，对于人员身份来说，保护好用户名和密码显得尤为重要。

## 优先级

高

## 不推荐做法

- 没有为访问控制 RAM（Resource Access Management）用户和云账号Root身份实施强密码策略，包括提高密码复杂度和多因素认证MFA（Multi Factor Authentication）。
- 在不同的服务、站点，或不同的用户共用一个登录密码。
- 登录密码长时间不轮换。

## 实施指南

在阿里云上，最推荐通过SSO的方式跟组织内的IdP进行集成，实现人员身份的统一认证。更多实践细节，请参见[基于统一的IdP实现人员身份的统一认证](https://help.aliyun.com/zh/well-architected/sec01-bp05-unified-authentication-of-personnel-identity-based-on-unified-idp)。

在阿里云上，注册完一个阿里云账号后，即可通过用户名和密码的方式登录到阿里云控制台，登录成功后，即获得了Root身份。完成阿里云账号注册之后，建议立即对云账号进行安全加固：

1. 为云账号[设置强密码](https://help.aliyun.com/zh/account/how-do-i-change-my-account-password)。推荐数字、大小写字母、符号的组合，建议至少8位。
2. [启用MFA](https://help.aliyun.com/zh/account/manage-vitual-mfa)。
3. 定期更新密码，例如每90天更换一次密码，且避免跟以往密码重复。

然后您可以为每个需要访问云资源的人员创建独立的身份，并使用这些身份进行日常的云上运维管理，替代Root身份。如果您使用RAM用户代替Root身份登录控制台进行运维操作，建议采用以下方式提升登录方式的安全性：

1. 提升密码强度。如增加密码位数、混合使用数字、大小写字母、特殊字符等。针对阿里云RAM用户，管理员可以[设置RAM用户密码策略](https://help.aliyun.com/zh/ram/user-guide/configure-a-password-policy-for-ram-users)，强制RAM用户使用更复杂的密码，降低密码泄漏和被破解的风险。
2. 避免密码混用。在不同的服务、站点，或不同的用户共用一个密码，增加了密码的暴露面积，会增加密码泄漏的可能性。如果其中一个服务或用户的密码泄漏，那攻击者就可以通过尝试登录的方式，找到共用密码的其他服务。因此，确保不同服务、不同用户使用不同的密码，能够降低密码泄漏的风险。
3. 定期轮转密码。密码存在的时间越长，泄漏风险越高。通过定期重设密码，降低单个密码存在的时长，能够进一步降低密码泄漏风险。针对阿里云RAM用户户，管理员可以在[设置RAM用户密码策略](https://help.aliyun.com/zh/ram/user-guide/configure-a-password-policy-for-ram-users)中设置密码有效期，来实现密码定期轮转。
4. 使用多因素认证。多因素认证MFA（Multi Factor Authentication）是一种简单有效的安全实践，在用户名和密码之外再增加一层安全保护。针对阿里云RAM用户，管理员可以[为RAM用户绑定MFA设备](https://help.aliyun.com/zh/ram/bind-an-mfa-device-to-a-ram-user-1)，用于登录阿里云或进行敏感操作时的二次身份验证，以此保护您的账号更安全。
5. 高危操作强制使用多因素认证。您可以通过权限来限制只有开启了MFA认证的RAM用户才能执行某些高危操作。单个账号场景下，您可以[通过RAM限制只有启用了MFA的RAM用户才能访问云资源](https://help.aliyun.com/zh/ram/use-cases/allow-only-mfa-enabled-ram-users-to-access-cloud-resources)。多账号场景下，推荐使用资源目录的[管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)，在企业组织范围内，统一下发管控策略，限定组织内账号的权限边界，以删除ECS实例为例，策略内容如下所示，禁止未开启MFA认证的RAM身份删除ECS实例：`{
 "Statement": [
 {
 "Action": "ecs:DeleteInstance",
 "Effect": "Deny",
 "Resource": "*",
 "Condition": {
 "Bool": {
 "acs:MFAPresent": "false"
 }
 }
 }
 ],
 "Version": "1"
}`

## 相关资源

### 相关实践

- [避免使用Root身份](https://help.aliyun.com/zh/well-architected/sec01-bp01-avoid-using-root-identity)
- [基于统一的IdP实现人员身份的统一认证](https://help.aliyun.com/zh/well-architected/sec01-bp05-unified-authentication-of-personnel-identity-based-on-unified-idp)

### 相关文档

- [RAM实践教程](https://help.aliyun.com/zh/ram/use-cases/tutorials/)
- [资源目录自定义管控策略示例](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/examples-of-custom-access-control-policies)

---

> 原页面：https://help.aliyun.com/zh/well-architected/sec01-bp03-establish-a-secure-login-mechanism（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
