<!-- source: https://help.aliyun.com/zh/well-architected/sec01-bp02-to-assign-a-separate-identity-to-each-organization-member -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706145 -->

# 为每个组织成员分配独立的身份

对大部分组织来说，往往有多个组织成员，不同的组织成员（如企业中的每个员工）代表了一个独立的个体，对组织来说，建议为每个成员分配独立的云上身份，并通过权限管控确保每位成员只能访问与其工作职责相关的资源。这种方式可以显著提升安全性，并能够简化审计和合规检查。

## 优先级

高

## 不推荐做法

- 不同组织成员共享身份或账号：比如员工A和员工B，共用同一个RAM用户，使用该RAM用户访问阿里云进行日常的运维管理。这种行为带来的风险有：共享身份或账号意味着这些组织成员拥有相同的访问权限，这容易导致越权、凭据泄漏、数据泄漏等风险。共享身份或账号，难以在操作审计日志中追踪哪个用户执行了哪些操作，在出现安全事件时，无法溯源和定位责任人。该案例中，员工A和员工B因为共用同一个RAM用户，在操作审计的日志中，相关的操作都会显示由同一个RAM用户进行，导致无法区分相应的操作究竟是员工A还是员工B进行。

## 实施指南

- 为不同的成员分配不同的身份。单个账号场景下，推荐使用访问控制 RAM（Resource Access Management）为不同成员分配不同的身份。多账号场景下，推荐使用云SSO进行多账号的人员身份统一管理和分配，避免每个账号下单独管理身份的成本。
- 阿里云支持基于SAML 2.0和OIDC的SSO（Single Sign On，单点登录），也称为身份联合登录。如果企业有身份提供商（IdP），建议跟阿里云进行SSO的集成，实现人员身份的统一管理和认证，避免人员变动时未及时回收账号导致一些安全事件。单个账号场景下，可以使用访问控制 RAM（Resource Access Management）提供的单点登录功能，实现阿里云与企业IdP的集成。具体需要根据企业当前的自身情况，[选择合适的SSO方案](https://help.aliyun.com/zh/ram/scenarios-of-sso)。多账号场景下，推荐使用云SSO直接[跟企业IdP进行SSO集成](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso)，实现多个账号统一的身份管理和认证。更多实施细节，请参见[基于统一的IdP实现人员身份的统一认证](https://help.aliyun.com/zh/well-architected/sec01-bp05-unified-authentication-of-personnel-identity-based-on-unified-idp)。

## 相关资源

### 相关实践

- [基于统一的IdP实现人员身份的统一认证](https://help.aliyun.com/zh/well-architected/sec01-bp05-unified-authentication-of-personnel-identity-based-on-unified-idp)

---

> 原页面：https://help.aliyun.com/zh/well-architected/sec01-bp02-to-assign-a-separate-identity-to-each-organization-member（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
