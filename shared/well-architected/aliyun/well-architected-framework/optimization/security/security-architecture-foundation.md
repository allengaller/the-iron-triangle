<!-- source: https://help.aliyun.com/zh/well-architected/security-architecture-foundation/ -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2901216 -->

# 安全架构基础

建议您根据职能、合规要求或者统一的管控策略，将不同的业务或应用分配到不同的独立账号中。借助账号间的天然隔离性，使用多个账号实现企业不同业务或应用间的相互独立。例如，生产环境应用与开发/测试环境应用通过账户级隔离实现严格分离。

- 集中化账号管理：资源目录可自动化阿里云[账号的创建与管理](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/manage-member-accounts/)，并在账号创建后持续对其进行管控。同时您可以通过[资源夹](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/manage-folders/)将账号归类分组，以实现企业的业务或应用根据其用途和需求进行逻辑划分。
- 集中化访问控制：使用资源目录[管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/manage-control-policies/)，可以统一管理资源目录各层级内资源访问的权限边界，建立企业整体访问控制原则或局部专用原则，确保安全合规和成本可控。例如：禁止成员申请域名、禁止成员删除日志记录等。
- 集中化服务与资源配置：资源目录的多账号架构支持您跨账号统一配置阿里云服务。例如，您可以通过[操作审计](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)记录整个组织内所有操作日志。您也可以通过[配置审计](https://help.aliyun.com/zh/document_detail/127388.html)集中聚合合规规格的数据，实时监控业务合规性并快速响应。
- 委派管理：通过[委派管理功能](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/manage-trusted-services/)，使用可信服务的委派管理员账号，在可信服务中基于组织进行业务管理，简化企业对云服务的统一管理，同时将服务管理账号与其他账号分离，减少管理账号的直接暴露风险，提升安全性。

如此，企业可构建安全、高效且可扩展的阿里云多账户治理框架，为复杂云环境下的业务增长提供坚实基础。

## 最佳实践

- [对不同的工作负载进行合理隔离](https://help.aliyun.com/zh/well-architected/reasonable-isolation-of-different-workloads)
- [避免使用Root身份](https://help.aliyun.com/zh/well-architected/sec01-bp01-avoid-using-root-identity)

---

> 原页面：https://help.aliyun.com/zh/well-architected/security-architecture-foundation/（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
