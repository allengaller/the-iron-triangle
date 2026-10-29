<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_05_0014.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# COST01-04 制定云资源管理策略和相应的权限管理机制

- **风险等级** 高
- **关键策略** 由于成本优化是跨组织多个业务部门的事项，而云资源是云上成本的主要开销，故而应该制定策略，确定您的组织应该如何管理资源。如上文所说的，可以使用账号隔离不同组织/部门的资源，甚至于在同一个组织/部门内部，开发，测试，核心业务，非核心业务，也使用不同的账号和环境。 然而即使账号/环境是分散的，云资源管理策略和权限管理机制应该是集中的。 企业的中心团队，如上文所提的云业务办公室、云卓越中心或 FinOps 团队需要为各个账号环境实施与策略一致的组和角色，控制每个组中谁可以创建、修改或停用实例和资源。同时依据企业的业务环境，创建统一的资源/成本视图，统一管理企业的账单和成本。
- **相关服务和工具** 客户可通过[统一身份认证服务IAM](https://www.huaweicloud.com/intl/zh-cn/product/iam.html)的细粒度权限管理，精细化控制账号下用户的资源访问权限，实施最小授权。 对于多账号场景，客户可通过[Organization](https://www.huaweicloud.com/intl/zh-cn/product/organizations.html)的服务控制策略（Service Control Policy），集中控制每个账号可执行的操作。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_05_0014.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
