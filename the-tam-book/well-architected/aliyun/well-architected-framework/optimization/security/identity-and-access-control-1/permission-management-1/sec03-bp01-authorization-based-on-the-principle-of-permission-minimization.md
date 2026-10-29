<!-- source: https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706142 -->

# 基于权限最小化原则进行授权

合理的权限设置能够阻止未经授权的访问，保护云上资产和数据的安全。因此，云上的权限管理的核心原则就是权限最小化，只给身份授予在特定条件下对特定资源执行特定操作所需的访问权限，确保权限最小够用。

## 优先级

高

## 不推荐做法

- 没有根据人员职能进行权限区分，直接授予管理员权限。
- 对于研发人员，进行账号范围的授权，没有根据其所负责的工作负载进行资源组级别的资源权限隔离，导致越权风险。比如，应用A和应用B，分别由研发团队a和b负责，如果进行账号级别的资源范围级别，将导致研发团队a的研发人员，有权限操作到应用B的资源，存在越权风险。
- 对于程序身份，推荐将权限收敛到特定资源的特定操作，不建议授予过于宽松的权限策略，比如，直接授予产品的FullAccess权限，避免误操作，减少程序身份泄漏后的影响面积。
- 没有定期审查并收敛权限，导致权限不断扩大蔓延。

## 实施指南

云上的权限管理是为了控制某个身份在什么条件下对哪些资源能够执行哪些操作。阿里云上的授权方式分为以下几种：

1. 基于身份的授权：主要是指针对RAM用户、用户组或角色进行授权。
2. 基于资源的授权：部分云产品支持为某个特定资源绑定权限。如OSS的[Bucket Policy](https://help.aliyun.com/zh/oss/user-guide/oss-bucket-policy/)，支持向其他账号的RAM用户授予访问权限，以及向匿名用户授予带特定IP条件限制的访问权限。
3. 管控策略（Control Policy）：管控策略是一种针对启用了资源目录（Resource Directory，简称 RD）的多账号组织，基于资源结构（资源夹或成员）的访问控制策略，可以统一管理资源目录各层级内资源访问的权限边界，建立企业整体访问控制原则或局部专用原则。管控策略只定义权限边界，并不真正授予权限。
4. 会话策略（Session Policy）：在角色扮演的过程中，可以指定一个会话策略，定义本次扮演中可以获得权限，进一步缩小角色权限的范围。同样，会话策略只限定权限，并不真正授予权限。

无论基于何种授权方式，都需要遵循权限最小化的原则。

1. 进行精细化授权。针对不同身份类型，您可以参考以下最佳实践。人员身份的权限管理。基于人员职能进行授权。对于组织来说，不同职责的人需要访问云上不同类型的资源。安全管理员往往需要访问安全产品，但数据库管理员往往只需要访问数据库相关的产品。但对于同一职责，尤其是一些基础职能，如财务、数据库管理员、安全管理员、审计员等，所需要访问和管理的资源范围往往是一致的。因此，建议针对人员职能划分，进行权限的抽象。阿里云针对常见的职能身份，提供了策略模板，您可以[通过导入策略模板](https://help.aliyun.com/zh/ram/create-a-custom-policy#section-l3j-qij-gtf)并在此基础上进行修改调整，来快速创建符合企业身份职能的自定义权限策略，从而简化授权过程，降低管理成本。按资源范围授权。对于大型组织来说，应该按照人员尤其是研发人员所管理的业务应用对应的资源范围进行授权，保证业务应用A的研发不会意外访问和操作到业务应用B的资源，如此避免越权访问和误操作，同时，能够简化授权逻辑，提高权限策略复用率，进而在权限最小化和管理效率中取得平衡。首先，您可以[使用资源组对阿里云账号内的资源进行分组管理](https://help.aliyun.com/zh/resource-management/resource-group/getting-started/to-group-resources-using-resource-groups)，将不同业务应用的资源划分到不同的资源组，然后在授权时应用范围选择相应的资源组，具体授权操作，请参见[资源分组和授权](https://help.aliyun.com/zh/resource-management/resource-group/use-cases/use-ram-to-create-and-authorize-resource-groups)。如此，将资源组作为资源隔离和权限管理的容器。更多资源分组实践，请参考[资源分组最佳实践](https://help.aliyun.com/zh/resource-management/resource-group/use-cases/resource-grouping-best-practices)。程序身份的权限管理。精细化授权。一般来说，应用程序所需要访问的阿里云资源，对应进行的操作是可以预期的，应该尽可能的通过自定义权限策略来定义该程序身份所需要的最小权限。比如一个用户社区需要展示用户头像，支持头像上传，那么该程序仅需要特定OSS Bucket的GetObject和PutObject权限即可。您可以通过[可视化编辑模式](https://help.aliyun.com/zh/ram/create-a-custom-policy#section-v5a-gji-s5k)和[导入策略](https://help.aliyun.com/zh/ram/create-a-custom-policy#section-l3j-qij-gtf)的方式创建自定义权限策略，简化创建策略的过程。此外，您还可以充分利用权限策略中的[条件（Condition）](https://help.aliyun.com/zh/ram/policy-elements#section-jix-u0j-2ms)元素，进一步约束和收敛权限。比如，您可以通过条件（Condition）元素限制只能[通过指定的IP地址访问阿里云](https://help.aliyun.com/zh/ram/access-alibaba-cloud-resources-by-using-a-specific-ip-address-or-cidr-block)、[在指定的时间段访问阿里云](https://help.aliyun.com/zh/ram/access-alibaba-cloud-in-a-specified-period-of-time)等等，这对于人员身份同样适用。使用会话策略（Session Policy）。在某些场景下，为了避免RAM角色的膨胀并且提高权限策略复用率，您需要通过会话策略动态收敛权限。比如，企业的客户端应用，有自己的用户体系，支持用户上传文件到OSS，需要通过权限限制每个用户只能上传文件到自己的文件夹中，实现资源和权限的隔离。如果为每个用户都分配一个阿里云的RAM角色，势必会带来角色数量的膨胀，超过Quota限制并且增加管理成本。此时，企业可以创建一个RAM角色供应用上传文件使用，角色的权限可以适当放大，比如限制到OSS Bucket级别：`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "oss:PutObject"
 ],
 "Resource": [
 "acs:oss:*:*:examplebucket/*"
 ]
 }
 ]
}`在应用调用[AssumeRole - 获取扮演角色的临时身份凭证](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)这个API扮演角色获取STS Token上传文件时，进一步通过Policy参数缩小此次会话的权限范围。比如，用户ID为123的用户需要上传自己的文件到examplebucket中，那么文件所在的文件夹路径为`oss://examplebucket/user/123/`。那么在Policy中可以进一步限制此次生成的STS Token的权限：`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "oss:PutObject",
 "Resource": [
 "acs:oss:*:*:examplebucket/user/123/*"
 ]
 }
 ]
}`此时，生成的STS Token所具有的权限就是会话权限与角色权限的交集，既只具有往确定的OSS文件夹下上传文件的权限，以此针对企业应用程序自有的不同用户进行动态的权限隔离。
2. 定期审查权限策略，并移除不必要的权限。阿里云提供了[访问分析](https://help.aliyun.com/zh/ram/access-analyzer)的能力，帮助您快速识别外部访问和过度授权，同时配合事件总线，方便您快速配置相应的通知告警机制。更多内容，请参见[定期审查权限确保权限最小够用](https://help.aliyun.com/zh/well-architected/sec03-bp03-periodic-review-of-authority-to-ensure-minimum-authority)。
3. 设置权限边界。对于云上有多个阿里云账号的组织，可以基于[资源目录管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)，限制成员账号内的RAM身份权限范围，禁用一些高危操作降低身份泄漏风险。如禁止成员删除域名或修改域名解析记录、禁止成员删除日志记录等。更多内容，请参见[设置权限边界](https://help.aliyun.com/zh/well-architected/sec03-bp04-to-set-permissions-boundaries)。
4. 建立临时权限申请机制。企业在践行权限最小化的过程中，势必会遇到需要临时提权的情况。比如，为防止误删除资源，企业没有授予业务团队删除资源的权限，当业务团队确实需要删除资源时，需要提交申请流程临时提权进行操作，如此，减少误操作同时在权限最小化和管理效率中取得平衡。

## 相关资源

### 相关实践

- [定期审查权限确保权限最小够用](https://help.aliyun.com/zh/well-architected/sec03-bp03-periodic-review-of-authority-to-ensure-minimum-authority)
- [设置权限边界](https://help.aliyun.com/zh/well-architected/sec03-bp04-to-set-permissions-boundaries)

### 相关文档

- [资源分组最佳实践](https://help.aliyun.com/zh/resource-management/resource-group/use-cases/resource-grouping-best-practices)
- [自定义管控策略示例](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/examples-of-custom-access-control-policies)

---

> 原页面：https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
