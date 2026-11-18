<!-- source: https://help.aliyun.com/zh/well-architected/regularly-review-public-and-cross-account-access -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2924028 -->

# 定期审查公共和跨账号访问

企业在日常用云的过程中，为保证业务的灵活性，通常会出现外部访问授权的情形，比如供应商需要访问企业账号内的云资源上。不合理的外部访问，会给企业资产和数据带来巨大的安全风险，比如OSS Bucket非预期的公开访问，导致企业数据泄露。因此，您需要定期审查，及时发现外部访问（公共或跨账号访问），从而判断该访问的合理性并收敛非必要的外部访问权限。

## 优先级

低

## 不推荐做法

- 开启OSS Bucket公共读写或者公共读，增加企业数据泄露风险。
- RAM角色临时授信给了外部账号扮演使用，比如企业的外部软件供应商，需要扮演企业账号的RAM角色来访问账号内的云资源完成软件的部署。在使用结束后，没有及时清理，长时间暴露给外部账号。
- 没有定期审查公共和跨账号访问，无法及时发现并收敛不合理的外部访问，导致安全风险。

## 实施指南

通常来说，一般有以下几种方式进行公共和跨账号访问：

1. 开放公共访问。比如OSS存储空间（Bucket）开启了公共读写或者公共读。
2. 通过基于资源的授权，允许匿名或者跨账号访问。比如[Bucket Policy](https://help.aliyun.com/zh/oss/user-guide/oss-bucket-policy/)。
3. 允许其他账号扮演您的RAM角色实现跨账号访问。详情，请参见[跨阿里云账号的资源授权](https://help.aliyun.com/zh/ram/use-cases/use-a-ram-role-to-grant-permissions-across-alibaba-cloud-accounts)。

阿里云提供了[访问分析](https://help.aliyun.com/zh/ram/access-analyzer)的能力，帮助您快速识别外部访问，同时配合事件总线，方便您快速配置相应的通知告警机制。详细的审计和收敛步骤，请参考《[通过访问分析识别和收敛外部访问](https://help.aliyun.com/zh/well-architected/solution-262)》。

1. 使用[访问分析](https://help.aliyun.com/zh/ram/access-analyzer)，定期对公共和跨账号访问进行审查。在创建访问分析的外部访问分析器时，您有以下两种分析范围可以选择，这里的分析范围就是分析器的信任区。分析器会监测信任区内支持分析的资源，并且认为信任区内身份对资源的访问是可信的。资源目录：本账号所属资源目录内的所有账号的身份均被认为是可信的，资源目录外其他账号内身份被认为是非可信的。当前账号：本账号内身份被认为是可信的，其他账号内身份被认为是非可信的。如果您的企业使用了多个阿里云账号，推荐您使用云治理中心[Landing Zone 搭建](https://help.aliyun.com/zh/cgc/user-guide/build-a-landing-zone-1)功能，一站式完成资源目录中企业多账号架构的搭建。如此，在访问分析时，通过对资源目录访问进行分析，实现以企业视角对多账号组织架构进行审查，及时发现组织外的跨账号访问。
2. 配置监控和报警。您可以将访问分析的分析结果，通过[事件总线EventBridge](https://help.aliyun.com/zh/eventbridge/product-overview/what-is-eventbridge)以邮箱等渠道，通知到您的运维团队。以便让您能够第一时间发现非预期的外部访问，降低企业安全风险。
3. 重点关注并处理OSS存储桶（Bucket）的公开访问，避免企业敏感数据泄露。发现OSS存储桶开放了公开访问后，请及时评估合理性，对于非预期的公开，您可以通过[阻止公共访问](https://help.aliyun.com/zh/oss/user-guide/block-public-access)快速进行处理。如果您的OSS存储桶存放的图片、视频、文档等静态资源需要对外公开，建议您使用CDN进行分发，CDN支持回源到私有的OSS存储桶，您无需直接公开OSS存储桶，可以降低流量费用，提升资源加载速度。如果您使用资源目录搭建了多账号架构，您可以使用[管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)，来阻止将OSS存储桶设置为公共访问。具体的策略内容，参考如下；`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "oss:PutObject",
 "oss:PutObjectAcl"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "oss:x-oss-object-acl": [
 "public-read",
 "public-read-write"
 ]
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": "oss:PutBucket",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "oss:x-oss-acl": [
 "public-read",
 "public-read-write"
 ]
 }
 }
 }
 ]
}`

## 相关资源

### 相关实践

- [基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)

### 相关方案

- 《[通过访问分析识别和收敛外部访问](https://help.aliyun.com/zh/well-architected/solution-262)》

### 相关文档

- [自定义管控策略示例](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/examples-of-custom-access-control-policies)
- [使用管控策略实现企业可用云产品白名单](https://help.aliyun.com/zh/resource-management/resource-directory/use-cases/use-access-control-policies-to-define-services-that-can-be-accessed-by-an-enterprise)
- [降低因账号密码泄露带来的未授权访问风险](https://help.aliyun.com/zh/oss/user-guide/reduce-the-risks-of-unauthorized-access-caused-by-accesskey-pair-leaks)

---

> 原页面：https://help.aliyun.com/zh/well-architected/regularly-review-public-and-cross-account-access（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
