<!-- source: https://help.aliyun.com/zh/well-architected/sec03-bp04-to-set-permissions-boundaries -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706133 -->

# 设置权限边界

对于云上有多个阿里云账号的组织，可以基于资源目录管控策略，限制成员账号内的 RAM 身份权限范围，自上而下统一管理资源目录各层级内资源访问的权限边界，建立企业整体访问控制原则或局部专用原则。

## 优先级

中

## 不推荐做法

- 通过资源目录搭建了企业多账号架构后，企业未建立统一的权限边界，对各成员账号的行为不加以管控，带来安全风险和成本浪费。
- 在多账号架构下，企业需要建立统一的权限边界，比如，企业安全基线要求删除资源时RAM身份必须使用MFA。从而，在每个成员账号中，为RAM身份单独配置权限策略。该做法难以保证安全基线的一致性，同时极大增加运维和管理成本。

## 实施指南

[资源目录管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)是一种基于资源结构（资源夹或成员）的访问控制策略，只定义权限边界，并不真正授予权限，您还需要在某个成员中使用访问控制（RAM）设置权限后，相应身份才具备对资源的访问权限。

当企业创建了一个资源目录，并为每个部门创建了成员后，如果对各成员的行为不加以管控，就会破坏运维规则，带来安全风险和成本浪费。资源目录提供管控策略功能，企业可以通过管理账号集中制定管理规则，并将这些管理规则应用于资源目录的各级资源结构（资源夹、成员）上，管控各成员内资源的访问规则，确保安全合规和成本可控。例如：禁止成员申请域名、禁止成员删除日志记录等。详细方案，请参见《[企业多账号组织全局访问边界控制](https://help.aliyun.com/zh/well-architected/solution-39)》。

推荐您使用云治理中心[Landing Zone 搭建](https://help.aliyun.com/zh/cgc/user-guide/build-a-landing-zone-1)功能，通过蓝图模板的形式，一站式轻松完成企业多账号环境的搭建，同时云治理中心预置了企业常用的管控策略，通过Landing Zone搭建，您也可以一键开启。

1. 搭建多账号架构，[对不同的工作负载进行合理隔离](https://help.aliyun.com/zh/well-architected/reasonable-isolation-of-different-workloads)。
2. 使用[管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)，建立统一的权限边界。在定义管控策略时，您有两种授权效果可以选择：允许（Allow）：显式指定允许的访问权限，并隐式阻止所有其它访问权限。**说明**开启管控策略后，资源目录内的资源夹和成员会默认绑定系统策略FullAliyunAccess，该策略允许对您在阿里云上的所有资源进行任何操作。如果您需要自定义允许的访问权限，在定义完管控策略并和目标绑定后，还需要将FullAliyunAccess解绑。拒绝（Deny）：显式指定不允许的访问权限，并且默认情况下允许所有其它访问权限。对于绝大多数场景，都建议您使用拒绝（Deny）的授权效果，显式指定不允许的访问权限。只有您需要对权限进行完全的强管控，并且明确知道成员账号需要使用哪些产品权限，才会使用到允许（Allow）的授权效果。此外，您可以参考[自定义管控策略示例](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/examples-of-custom-access-control-policies)，来了解如何有效地构造管控策略。

## 相关资源

### 相关实践

- [对不同的工作负载进行合理隔离](https://help.aliyun.com/zh/well-architected/reasonable-isolation-of-different-workloads)

### 相关方案

- 《[企业多账号组织全局访问边界控制](https://help.aliyun.com/zh/well-architected/solution-39)》

### 相关文档

- [自定义管控策略示例](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/examples-of-custom-access-control-policies)
- [使用管控策略实现企业可用云产品白名单](https://help.aliyun.com/zh/resource-management/resource-directory/use-cases/use-access-control-policies-to-define-services-that-can-be-accessed-by-an-enterprise)

---

> 原页面：https://help.aliyun.com/zh/well-architected/sec03-bp04-to-set-permissions-boundaries（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
