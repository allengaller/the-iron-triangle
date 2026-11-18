<!-- source: https://help.aliyun.com/zh/well-architected/simplify-people-management-sec01-bp06-using-user-groups -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706131 -->

# 使用用户组简化人员管理

您可以使用RAM用户组对相同职责的RAM用户进行分组统一管理，并针对用户组进行统一授权，从而减少权限策略的数量和复杂性，更加高效的管理RAM用户及其权限，更容易落实最小权限的原则。

## 优先级

中

## 不推荐做法

- 分别管理每个RAM用户的权限，并且在多个RAM用户之间复制权限。
- 用户组定义过于宽泛，导致需要授予过大权限，容易造成过度授权的风险。
- 用户组定义过于精细，造成组成员的重复和混淆，带来管理的复杂度。

## 实施指南

1. 定义用户组。您可以参考以下实践原则设计您的用户组：建议您根据用户所履行的职能来定义用户组。比如，对于管理网络的职能团队，您可以定义用于网络管理的用户组并将具有网络管理职责的用户加入到组中，进行统一管理和授权。如果两个用户组具有一些重叠的权限，建议将公共权限抽离出来作为独立的自定义权限策略，同时授予两个用户组。而不是将两个用户组合并成一个，避免用户组定义过于宽泛。具体操作，您可以参考以下方式创建用户组：如果您的用户组定义在自己的企业IdP中，建议您将企业IdP和阿里云进行SSO集成，并通过SCIM协议将IdP中的用户组同步为RAM用户组。更多信息，请参见[基于统一的IdP实现人员身份的统一认证](https://help.aliyun.com/zh/well-architected/sec01-bp05-unified-authentication-of-personnel-identity-based-on-unified-idp)。如果您直接在访问控制 RAM（Resource Access Management）中定义用户组，请参见[RAM用户组概览](https://help.aliyun.com/zh/ram/user-guide/overview-of-a-ram-user-group)。
2. 对用户组进行精细化授权：建议您遵循最小化授权的原则，参考[基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)，根据用户职能以及资源范围[为RAM用户组授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-a-ram-user-group)。

## 相关资源

### 相关实践

- [基于统一的IdP实现人员身份的统一认证](https://help.aliyun.com/zh/well-architected/sec01-bp05-unified-authentication-of-personnel-identity-based-on-unified-idp)
- [基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)

---

> 原页面：https://help.aliyun.com/zh/well-architected/simplify-people-management-sec01-bp06-using-user-groups（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
