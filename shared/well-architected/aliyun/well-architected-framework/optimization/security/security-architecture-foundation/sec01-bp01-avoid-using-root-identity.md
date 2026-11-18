<!-- source: https://help.aliyun.com/zh/well-architected/sec01-bp01-avoid-using-root-identity -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706137 -->

# 避免使用Root身份

在阿里云上，注册完一个阿里云账号后，即可通过用户名和密码的方式登录到阿里云控制台，登录成功后，即获得了Root身份。该身份具有该账号下所有的权限，一旦账号密码泄漏，风险极高。另外，如果多人共用该身份，每个人都保有该账号的用户名和密码，会增加泄漏的可能。同时，多人共享的情况下，在云上的操作日志中无法区分出是组织中哪个人使用了该身份进行了操作，也无法进行进一步溯源。因此，除了极个别场景，应该尽可能的使用访问控制 RAM（Resource Access Management）身份进行云上资源的访问，避免使用阿里云账号的Root身份。对于Root身份的使用，建议通过设置强密码，启用MFA等方式提升Root身份的安全性。

## 优先级

高

## 不推荐做法

- 云上的日常管理均使用阿里云云账号进行。
- 跟其他网站、App共用相同的密码。
- 企业内多人共用云账号，均使用云账号的账号密码登录控制台进行运维管控。
- 未开启MFA。
- 为Root身份启用AccessKey（也称为主账号AccessKey），Root身份的AccessKey拥有该云账号内的所有权限，一旦泄漏，风险极高。

## 实施指南

1. 完成阿里云账号注册之后，对云账号进行安全加固：为云账号[设置强密码](https://help.aliyun.com/zh/account/how-do-i-change-my-account-password)。推荐数字、大小写字母、符号的组合，建议至少8位。[启用MFA](https://help.aliyun.com/zh/account/manage-vitual-mfa)。定期更新密码，例如每90天更换一次密码，且避免跟以往密码重复。
2. 为每个需要访问云资源的人员创建独立的身份，并使用这些身份进行日常的云上运维管理，替代Root身份：如果您只有一个云账号，请使用访问控制 RAM（Resource Access Management）管理需要访问云资源的身份。如果您有多个云账号，推荐使用云SSO进行多账号的统一身份管理。
3. 不给Root用户启用AccessKey，如果已经启用了AccessKey，建议[对这些AccessKey进行治理](https://help.aliyun.com/zh/ram/avoid-using-the-accesskey-pair-of-an-alibaba-cloud-account)。
4. 使用操作审计（ActionTrail）定期审查Root等身份的使用情况。通过[操作审计高级事件查询](https://help.aliyun.com/zh/actiontrail/user-guide/query-events-related-to-an-alibaba-cloud-account-or-an-accesskey-pair)模板的**查询主账号登录控制台事件**系统模板，获取Root身份登录事件进行审计。

---

> 原页面：https://help.aliyun.com/zh/well-architected/sec01-bp01-avoid-using-root-identity（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
