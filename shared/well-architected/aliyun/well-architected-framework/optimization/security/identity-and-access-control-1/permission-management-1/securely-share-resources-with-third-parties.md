<!-- source: https://help.aliyun.com/zh/well-architected/securely-share-resources-with-third-parties -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2924031 -->

# 与第三方安全地共享资源

企业在日常用云的过程中，资源的共享往往不局限在企业组织内部，企业可能会有一部分数据和资源需要开放给第三方进行访问和管理，比如，企业有三方的软件供应商或者MSP服务供应商，需要访问企业的云资源，进行软件部署或者日常的运维管理。您应该遵循最小化原则，通过精细化授权和临时凭证STS Token等方式，安全的将资源共享给可信第三方。

## 优先级

中

## 不推荐做法

- 第三方需要访问或运维企业资源时，直接将固定凭据AccessKey或者用户名密码明文提供给第三方使用，增加泄露风险。
- RAM角色授信给第三方扮演时，采用默认的信任策略，没有附加ExternalId条件，容易导致混淆代理人问题的发生。

## 实施指南

1. 使用[跨账号角色扮演](https://help.aliyun.com/zh/ram/use-cases/use-a-ram-role-to-grant-permissions-across-alibaba-cloud-accounts)，实现第三方跨账号访问企业云上资源。一般来说，企业的第三方供应商会通过以下几种方式访问企业云上资源，不论哪种方式，都建议您提供RAM角色给第三方，让第三方使用跨账号角色扮演来访问企业云资源。通过控制台访问。建议第三方使用自己的阿里云账号登录控制台，通过角色扮演的方式，切换到企业云账号下的RAM角色身份，从而访问企业云资源。具体操作，请参见[通过控制台扮演RAM角色](https://help.aliyun.com/zh/ram/user-guide/assume-a-ram-role#section-j75-l2q-o53)。通过代码程序访问。建议第三方使用自己的阿里云身份凭据（比如：AccessKey），通过调用[AssumeRole - 获取扮演角色的临时身份凭证](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)接口，扮演企业云账号下的RAM角色，从而获取该RAM角色的临时凭据（STS Token），使用STS Token访问企业云资源。具体操作，请参见[通过调用API扮演RAM角色](https://help.aliyun.com/zh/ram/user-guide/assume-a-ram-role#section-br2-7rx-4nr)通过Aliyun CLI访问。建议第三方使用自己的阿里云身份凭据（比如：AccessKey），通过Aliyun CLI的跨账号角色扮演的方式，访问企业云资源。具体操作，请参见[在阿里云CLI中配置身份凭证](https://help.aliyun.com/zh/cli/configure-credentials/)中，身份凭证类型为`RamRoleArn`的配置方式。其中，需要特别注意的是，企业提供给第三方的RAM角色，其信任策略建议[使用ExternalId防止混淆代理人问题](https://help.aliyun.com/zh/ram/use-cases/use-externalid-to-prevent-the-confused-deputy-problem)。由于第三方供应商可能需要同时访问多个客户的多个阿里云账号，企业需要和第三方约定一个代表企业自身，随机且唯一的ExternalId，将ExternalId加入RAM角色信任策略中，第三方通过调用[AssumeRole](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)接口扮演角色的时候，需要提供这个ExternalId，不提供或者提供错误都会失败。如此，避免攻击者伪装成其他客户骗过第三方供应商，访问到别的企业客户的资源。
2. 参考最佳实践[定期审查公共和跨账号访问](https://help.aliyun.com/zh/well-architected/regularly-review-public-and-cross-account-access)，通过[访问分析](https://help.aliyun.com/zh/ram/access-analyzer)定期审查并识别外部访问，对于不合理的资源共享带来的外部访问，进行及时的处理，保证企业资产和数据安全。
3. 对于只能使用固定凭据AccessKey的场景，比如第三方需要访问和运维的云产品不支持RAM角色（STS Token）。请参考最佳实践[对固定凭据进行集中化管控](https://help.aliyun.com/zh/well-architected/sec02-bp05-centralized-control-of-fixed-credentials)，避免直接将AccessKey明文提供给第三方。

## 相关资源

### 相关实践

- [定期审查公共和跨账号访问](https://help.aliyun.com/zh/well-architected/regularly-review-public-and-cross-account-access)
- [对固定凭据进行集中化管控](https://help.aliyun.com/zh/well-architected/sec02-bp05-centralized-control-of-fixed-credentials)

### 相关文档

- [跨阿里云账号的资源授权](https://help.aliyun.com/zh/ram/use-cases/use-a-ram-role-to-grant-permissions-across-alibaba-cloud-accounts)

---

> 原页面：https://help.aliyun.com/zh/well-architected/securely-share-resources-with-third-parties（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
