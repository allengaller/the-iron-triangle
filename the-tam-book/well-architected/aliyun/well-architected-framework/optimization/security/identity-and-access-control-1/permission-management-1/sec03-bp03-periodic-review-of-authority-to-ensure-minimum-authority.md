<!-- source: https://help.aliyun.com/zh/well-architected/sec03-bp03-periodic-review-of-authority-to-ensure-minimum-authority -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706144 -->

# 定期审查权限确保权限最小够用

在授权完成后，还需要定期对权限的授予进行审计，删除不需要的权限，确保每个身份的权限持续满足最小够用原则。

## 优先级

中

## 不推荐做法

- 授予过多的管理员权限，甚至默认为所有用户直接授予管理员权限。
- 没有定期审查并收敛权限，导致权限不断扩大蔓延。

## 实施指南

当业务刚开始上云或者在云上构建新应用时，通常会使用较为宽松的权限策略，方便业务测试，提高效率。比如，在应用初期的开发或者测试环境中，授予研发人员更为广泛的产品权限，方便研发人员进行产品测试和选型。随着业务和产品逐渐成熟稳定，建议您持续审查和收敛不需要的权限，避免过度授权带来的云上资产和数据的安全风险。

阿里云提供了[访问分析](https://help.aliyun.com/zh/ram/access-analyzer)的能力，帮助您快速识别过度授权，同时配合事件总线，方便您快速配置相应的通知告警机制。其中，建议您重点关注：

1. 超级管理员：指的是拥有账号内所有资源管理权限的RAM身份（RAM用户或RAM角色）。例如，被授予AdministratorAccess权限策略的RAM用户或RAM角色。建议参考[基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)，根据人员职能进行授权。对于需要进行云上运维管理的身份，阿里云提供了超级用户的权限模板，可以[通过导入策略模板](https://help.aliyun.com/zh/ram/create-a-custom-policy#section-l3j-qij-gtf)的功能，直接使用超级用户的权限模板，将超级管理员权限降级。超级用户可以负责企业的云上运维管理，可创建、查看、操作所有的云服务，不能管理身份权限、不能管理账号架构、不能使用财务关联。您也可以使用其他策略模板定义人员职能权限。
2. 特权身份：指的是拥有高危特权的RAM身份（RAM用户或RAM角色）。拥有这类特权的RAM身份往往可以为自己或其他RAM身份提升权限，使得他们获得更高的访问权限。详细的特权列表，请参见[特权列表](https://help.aliyun.com/zh/ram/identify-over-authorization#8efaf7159digb)。这类身份属于重点审计对象，请确保这些身份拥有这些特权是合理的。
3. 闲置权限：对于没有使用过的权限，结合访问分析的审计结果，针对性的进行收敛。

详细的审计和收敛步骤，请参考方案《[通过访问分析识别和收敛过度授权](https://help.aliyun.com/zh/well-architected/solution-272)》。

## 相关资源

### 相关实践

- [基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)

### 相关方案

- 《[通过访问分析识别和收敛过度授权](https://help.aliyun.com/zh/well-architected/solution-272)》

---

> 原页面：https://help.aliyun.com/zh/well-architected/sec03-bp03-periodic-review-of-authority-to-ensure-minimum-authority（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
