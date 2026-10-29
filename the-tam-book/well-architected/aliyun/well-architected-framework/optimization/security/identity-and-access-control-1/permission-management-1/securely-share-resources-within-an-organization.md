<!-- source: https://help.aliyun.com/zh/well-architected/securely-share-resources-within-an-organization -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2924030 -->

# 在组织内安全地共享资源

随着业务和应用数量的增长，企业可能需要在多个业务和应用中共享某些资源，以此来降低成本和运维开销，并且对共享的资源进行统一的运维控制，方便企业集中配置安全策略、进行审计跟踪等。因此，企业需要使用安全的方式在组织内共享资源，最大程度的避免意外访问，减少数据泄露和丢失风险。

## 优先级

中

## 不推荐做法

- 点对点的将一个阿里云账号下的资源，直接共享给另外一个阿里云账号使用，随着共享资源和账号的增多，会带来过高的运维管理成本，并且依赖人工操作，极大的增加误操作概率。
- 没有通过管控策略等手段禁止组织外资源共享，存在组织外意外访问的风险。
- 没有定期审查组织外的共享和访问。

## 实施指南

1. 通过[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)将企业的多账号有序组织和集中管理起来，推荐您使用云治理中心[Landing Zone 搭建](https://help.aliyun.com/zh/cgc/user-guide/build-a-landing-zone-1)功能，通过蓝图模板的形式，一站式轻松完成企业多账号架构的搭建。通过多账号架构，在组织内进行安全的资源共享。
2. 将资源目录和云服务集成。我们将支持与资源目录组合使用的其他阿里云服务称为可信服务。资源目录允许可信服务访问资源目录中的成员、资源夹等信息。您可以使用管理账号或可信服务的委派管理员账号，在可信服务中基于组织进行业务管理，从而共享可信服务中的资源实例，并简化企业对云服务的统一管理。以云防火墙为例，在单账号场景下，您需要为每个企业云账号单独购买和配置云防火墙。通过资源目录构建了企业多账号架构后，您只需要在管理账号中购买一套云防火墙，就可以统一管理组织内多账号的公网IP资产，统一配置防御策略以及查看日志分析，实现集中安全管控。更多资源目录支持的可信服务，请参见[可信服务概述](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/overview-1)。
3. 通过[资源共享](https://help.aliyun.com/zh/resource-management/resource-sharing/product-overview/resource-sharing-overview)，在组织内共享资源，统一运维管理，提升共享体验。目前阿里云支持资源共享的云服务，请参见[支持资源共享的云服务](https://help.aliyun.com/zh/resource-management/resource-sharing/product-overview/services-that-work-with-resource-sharing)。为保证在组织内安全的共享资源，建议您[仅在资源目录内共享资源](https://help.aliyun.com/zh/resource-management/resource-sharing/getting-started/share-resources-with-objects-in-a-resource-directory)，避免以外共享给组织外的账号，造成数据泄露等安全事件的发生。
4. 参考最佳实践[设置权限边界](https://help.aliyun.com/zh/well-architected/sec03-bp04-to-set-permissions-boundaries)，通过[管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)对资源共享行为进行统一的管控和限制，通过权限边界，保证明确的资源或资源类型只能共享给可信的企业组织内云账号。您可以通过管控策略实现禁止组织外资源共享、仅允许共享指定资源类型等等效果。具体示例，请参见[通过管控策略限制资源共享的示例](https://help.aliyun.com/zh/resource-management/resource-sharing/user-guide/examples-of-restricting-resource-sharing-by-controlling-policies)。
5. 参考最佳实践[定期审查公共和跨账号访问](https://help.aliyun.com/zh/well-architected/regularly-review-public-and-cross-account-access)，通过[访问分析](https://help.aliyun.com/zh/ram/access-analyzer)定期审查并识别组织外的访问，对于不合理的资源共享带来的外部访问，进行及时的处理，保证企业资产和数据安全。

## 相关资源

### 相关实践

- [设置权限边界](https://help.aliyun.com/zh/well-architected/sec03-bp04-to-set-permissions-boundaries)
- [定期审查公共和跨账号访问](https://help.aliyun.com/zh/well-architected/regularly-review-public-and-cross-account-access)

### 相关文档

- [支持资源共享的云服务](https://help.aliyun.com/zh/resource-management/resource-sharing/product-overview/services-that-work-with-resource-sharing)
- [通过管控策略限制资源共享的示例](https://help.aliyun.com/zh/resource-management/resource-sharing/user-guide/examples-of-restricting-resource-sharing-by-controlling-policies)

---

> 原页面：https://help.aliyun.com/zh/well-architected/securely-share-resources-within-an-organization（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
