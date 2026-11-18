<!-- source: https://help.aliyun.com/zh/well-architected/sec02-bp02-prefer-temporary-credentials -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706132 -->

# 使用临时凭据替代固定凭据

通过给RAM用户或云账号的Root身份创建AccessKey供程序调用，都属于固定凭据类型。一旦创建出来，在删除之前，就是由固定的AccessKey ID和AccessKey Secret组成了该凭据。不合理地使用固定凭据会造成很多风险，比如应用研发人员将固定AccessKey明文写入了代码中，并将其上传到了GitHub等公开仓库，造成了AccessKey泄漏，最终导致业务受损。在阿里云上，建议尽可能通过角色扮演的方式获取临时凭据STS Token，代替固定AccessKey的使用。每个STS Token生成后，在超过角色最大会话时间（小时级）后，自动失效，能够极大降低凭据泄漏的可能。

## 优先级

高

## 不推荐做法

- 针对运维、研发等职能人员在本地调试API、执行运维脚本等需求，使用RAM用户AccessKey执行CLI命令或脚本等。在这种情况下，容易将明文AccessKey写在代码、脚本或者配置文件中，且不慎提交到GitHub等公开仓库中，导致AccessKey泄漏。此种情况，建议通过SSO等方式扮演角色，获取STS Token。
- 研发、产品等职能人员使用OSS客户端（如[ossbrowser](https://help.aliyun.com/zh/oss/developer-reference/install-ossbrowser-1-0)等）管理OSS文件时，使用RAM用户AccessKey做为认证方式，此种情况下，AccessKey存储在本地，当设备遗失或者被入侵，将导致AccessKey泄漏，进而造成数据泄漏。同时，当需要使用该客户端的员工越来越多时，会导致分配更多的AccessKey，泄漏风险大大增加。此种情况，建议让员工通过SSO等方式扮演角色，获取STS Token，使用STS Token作为认证方式在OSS客户端完成登录。
- 研发人员在应用程序的代码中明文配置AccessKey，并且将代码提交到公开仓库如GitHub中。
- 研发人员将AccessKey配置在移动端App，并且将App发布到了公共的应用市场，如App Store里。
- 研发人员在移动端App中使用STS Token，却未对对应的RAM角色进行精细化授权或使用SessionPolicy进一步限制会话级的权限。客户端请求被攻击者劫持，导致STS Token泄漏，造成安全风险。
- 不同的人员共用AccessKey。此种做法会导致泄漏风险增大，并且在审计日志中，无法区分出是谁在使用该AccessKey。如果人员离职时，没有及时回收AccessKey，会进一步导致数据泄漏等安全风险，且很难通过日志定位具体是谁做了该操作。

## 实施指南

针对不同场景的使用，都应该尽可能地使用STS Token代替RAM用户AccessKey。

### 员工使用STS Token

针对运维、产品、程序研发等员工，需要使用AccessKey进行运维、管理、本地开发调试等操作，建议通过扮演RAM角色，获取STS Token，代替AccessKey的使用。详细方案，请参见《[本地开发和运维的临时凭证使用方案](https://help.aliyun.com/zh/well-architected/solution-267)》。

- 优先建议通过角色SSO的方式，获取STS Token。针对单账号场景，建议在云账号内[配置基于SAML的角色SSO](https://help.aliyun.com/zh/ram/overview-of-role-based-sso)，并按职能为员工分配RAM角色。员工可以在命令行中使用[saml2alibabacloud](https://github.com/aliyun/saml2alibabacloud)工具，完成IdP侧的认证后，即可获取到STS Token。针对多账号场景，建议使用云SSO进行[多账号的单点登录配置](https://help.aliyun.com/zh/cloudsso/user-guide/configure-sso)。配置完成后，员工即可[使用CLI登录云SSO并访问阿里云资源](https://help.aliyun.com/zh/cloudsso/user-guide/use-alibaba-cloud-cli-to-access-cloudsso-and-alibaba-cloud-resources)。
- 对于第三方供应商，需要本地开发调试的场景，如果应用部署在供应商的云环境或者供应商有自己阿里云云账号，建议您新建RAM角色，提供给供应商，由供应商的云账号进行扮演，获取STS Token。具体操作，请参见、[创建可信实体为阿里云账号的RAM角色](https://help.aliyun.com/zh/ram/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account)。其中请注意：[为不同的工作负载和环境分配不同的凭据](https://help.aliyun.com/zh/well-architected/sec02-bp01-assign-different-credentials-to-different-workloads-and-environments)。该RAM角色不要混用，只提供给供应商扮演用来本地调试。[基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)。RAM角色权限需要遵守最小可用原则。
- 对于其他场景，比如您未使用SSO或者其他不支持角色STS Token访问的场景，目前还是使用固定AccessKey，使用时请遵循以下几点，以保证AccessKey的使用安全。[对固定凭据进行集中化管控](https://help.aliyun.com/zh/well-architected/sec02-bp05-centralized-control-of-fixed-credentials)。避免人员身份直接接触凭据，降低泄漏风险。[为不同的工作负载和环境分配不同的凭据](https://help.aliyun.com/zh/well-architected/sec02-bp01-assign-different-credentials-to-different-workloads-and-environments)。该AccessKey只用于该员工本地使用，员工之间不混用、使用场景不混用。[基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)。 只赋予使用该AccessKey所需的最小权限。对该AccessKey进行安全加固，为其设置网络访问限制策略，只允许企业内部环境调用。具体操作，请参见[AccessKey网络访问限制策略](https://help.aliyun.com/zh/ram/user-guide/accesskey-network-access-restriction-policy)。

### 云上部署的应用中使用STS Token

针对不同类型的云上应用部署方式，选择相应的方案实现STS Token凭据的使用：

- 针对在ECS实例上部署的应用，参考《[通过ECS实例角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-240)》，将RAM角色跟实例进行绑定，应用程序中即可通过ECS实例RAM角色，获取STS Token。
- 针对在ACK上部署的应用，在容器服务 Kubernetes 版中，一个集群可以部署多个服务，同一个容器节点可能包含多个不同服务的Pod，在多租户场景下，若部署不受信任的服务，该服务可直接访问ECS的元数据服务（Meta Data Server），获取Worker节点关联实例RAM角色的临时令牌STS Token，会造成身份权限的泄露。参考《[通过容器服务RRSA实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-241)》，在Pod维度即可扮演对应角色实现STS Token的获取。
- 针对在函数计算中部署的Serverless应用，可以参考《[通过FC函数角色实现临时凭证的获取和使用》](https://help.aliyun.com/zh/well-architected/solution-242)。

无论哪种部署方式，在应用代码中通过阿里云官方提供的SDK，根据部署类型[设置相应的身份验证（Credentials）配置](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials#61e3df504bhpg)，都可以便捷的直接获取STS Token，无需关心具体的凭据缓存以及过期更新逻辑。

其中，对于使用多个云账号的企业，存在跨账号访问的场景，建议您参考方案《[通过角色扮演实现跨账号临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-251)》，使用STS Token代替AccessKey，避免AccessKey泄露导致的安全问题。

### 移动程序中使用STS Token

对于移动端App来说，在客户端访问阿里云API，也建议使用STS Token，避免将AccessKey放在客户端，导致被黑客逆向或者反编译，获取到明文AccessKey。

- 常见的移动端场景主要是访问OSS，比如上传文件到OSS或者从OSS中下载文件。强烈建议您参考并使用方案《[通过预签名机制在客户端实现OSS直传和下载](https://help.aliyun.com/zh/well-architected/solution-244)》。
- 其他移动端的场景，比如访问SLS日志服务上传日志、使用消息中间件等，建议您通过服务端颁发临时凭证STS Token给移动端，用来访问云资源，详细方案，请参见《[通过TVM实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-245)》。

需要注意的是，请[基于权限最小化原则进行授权](https://help.aliyun.com/zh/well-architected/sec03-bp01-authorization-based-on-the-principle-of-permission-minimization)。使用到的RAM角色权限需要遵守最小可用原则。在《[通过TVM实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-245)》的方案中，需要调用AssumeRole这个API获取STS Token，在调用时，推荐进一步通过Policy参数缩小此次会话的权限范围。比如，针对某个上传请求，可以根据用户ID、RequestId、访问路径等请求特征生成会话Policy，并进一步缩小STS Token可操作的资源范围。通过该方式，可以避免客户端请求被劫持，导致STS Token泄漏后，攻击者拥有整个RAM角色的权限。

### STS Token泄漏应急处理

虽然STS Token是临时的身份令牌，但根据其对应的角色最大会话时间，其有效期的区间为15分钟~12小时。如果STS Token发生泄露，依旧存在非常大的安全风险，您可以按以下步骤回收所有已经颁发的STS Token。

1. 使用阿里云账号登录[RAM控制台](https://ram.console.aliyun.com/)。
2. [移除RAM角色的所有权限策略](https://help.aliyun.com/zh/ram/remove-permissions-from-a-ram-role#task-188178)。
3. [删除RAM角色](https://help.aliyun.com/zh/ram/user-guide/delete-a-ram-role#task-188137)。删除RAM角色后，所有通过扮演该RAM角色获取的且未过期的STS Token都将立即失效。

如果您还需要使用该角色，在完成泄漏根因的处理后，可以重新创建同名角色并授权相同的权限策略，使用新创建的角色继续完成您的任务。

## 相关资源

### 视频教程

#### 云上应用使用临时凭据的最佳实践

### 相关实践

- 针对无法使用STS Token的场景，建议对AccessKey进行集中化管控，请参考[对固定凭据进行集中化管控](https://help.aliyun.com/zh/well-architected/sec02-bp05-centralized-control-of-fixed-credentials)

### 相关方案

- 《[通过ECS实例角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-240)》
- 《[通过容器服务RRSA实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-241)》
- 《[通过FC函数角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-242)》
- 《[通过预签名机制在客户端实现OSS直传和下载](https://help.aliyun.com/zh/well-architected/solution-244)》
- 《[通过TVM实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-245)》
- 《[通过角色扮演实现跨账号临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-251)》
- 《[本地开发和运维的临时凭证使用方案](https://help.aliyun.com/zh/well-architected/solution-267)》
- 《[通过KMS实现固定AccessKey的集中管控](https://help.aliyun.com/zh/well-architected/solution-237)》

---

> 原页面：https://help.aliyun.com/zh/well-architected/sec02-bp02-prefer-temporary-credentials（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
