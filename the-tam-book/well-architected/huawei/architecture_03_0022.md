<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0022.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# SEC02-04 一体化身份管理

在公司范围内构建统一的身份管理系统，统一管理私有云和公有云、公有云上多个账号的用户身份。

- **风险等级** 中
- **关键策略** 在公司范围内构建统一身份管理系统，集中存储用户身份信息。 统一身份管理系统与私有云、公有云平台的IAM系统进行身份联邦，统一身份管理系统中的用户身份可以同时访问私有云和公有云平台。 统一身份管理系统与公司的HR流程结合，当员工入职、调岗和离职时可以触发用户的创建、变更和删除。 针对Landing Zone搭建的云上多账号环境，利用IAM身份中心集中管理多个账号的用户身份，并集中为这些用户配置能够访问多个账号下云资源的权限，无需在每个账号的IAM系统分别创建IAM用户并配置权限，简化多账号环境下身份权限管理的工作量。 统一身份管理系统与IAM身份中心建立身份联邦，这样无需分别与每个账号的IAM系统进行身份联邦。
- **相关云服务和工具** IAM身份中心 IAM Identity Center 统一身份认证服务 IAM 应用身份管理服务 OneAccess

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0022.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
