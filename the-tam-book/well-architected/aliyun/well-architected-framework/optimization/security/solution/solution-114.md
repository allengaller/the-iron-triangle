<!-- source: https://help.aliyun.com/zh/well-architected/solution-114 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929339 -->

# 基于CloudSSO实现多账号ACK集群统一身份权限管理

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970864.png)

当企业有多个业务并且每个业务单独部署了一套容器服务集群（ACK），通过开通资源目录能够把多个业务对应的阿里云账号邀请进来统一管理。不同账号内的ACK集群统一权限管理就显得非常重要。如果这些集群的权限管理都在每个账号内单独创建RAM用户或角色，则管理成本高，并且时间长了之后会出现权限混乱。

本文档介绍了当前企业有多个云账号可以使用云SSO产品来管理人员身份权限，并且基于云SSO中创建的角色与ACK中的RBAC进行映射。让企业更好地管理多ACK集群的身份权限。

## 方案优势

### 集中管理用户身份

借助SCIM协议从您的企业身份管理系统同步用户和用户组到云SSO身份目录中，降低身份管理的复杂度。

### 集中配置所有用户对账号内容器集群的访问权限

借助与资源目录（RD）的深度集成，在云SSO中您可以统一配置用户或用户组对整个RD内的任意成员账号的访问权限。根据RD的组织结构，选择不同成员账号为其分配可访问的身份（用户或用户组）以及具体的访问权限，且该权限可以随时修改和删除。

### 提供容器集群权限规范实践

遵守权限最小化原则指导企业提前规划云上账号内的权限体系。

## 客户场景

### 多账号容器集群人员身份权限统一管理

#### 场景描述

当企业有多个云账号，并且每个账号内单独部署容器集群服务。运维团队希望能够统一管理员工身份权限。

#### 适用客户

- 使用资源目录管理云上多个账号的企业客户。
- 使用多个阿里云账号的企业客户。
- 存在中心运维团队、审计团队的企业客户。
- 多个账号内都有容器集群服务的客户。

### 容器集群权限规范实践

#### 场景描述

企业希望能够有一套权限设计规范体系，用于指导云上账号内人员身份权限分配。避免出现权限过大导致的越权风险。

#### 适用客户

- 使用了容器集群服务的企业客户。
- 使用多个阿里云账号的企业客户。

## 方案架构

本方案使用了云SSO产品能力，企业运维人员可以提前规划好人员权限。在资源管理账号中运维可以实现集中人员授权。再到不同业务账号内容器服务集群中对各个角色完成精细化授权。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970865.png)

#### RAM Role容器服务场景权限建议

| **阿里云账号** | **RAM Role或云SSO中访问配置** | **权限描述** | **权限定义（权限策略及K8S的RBAC）** |
| --- | --- | --- | --- |
| Master Account 企业管理账号 | SystemAdmin系统管理员 | 系统管理员权限 | AdministratorAccess |
| ResourceDirectoryAdmin资源目录管理员 | 管理资源目录 （目录管理 成员管理等） | AliyunResourceDirectoryFullAccess |  |
| Business Account 应用账号 | SystemAdmin系统管理员 | 系统管理员权限 | AdministratorAccess |
| ContainerAdmin 容器管理员 | 云原生相关的管理员权限 | 云SSO中系统策略：AliyunCSFullAccess AliyunContainerRegistryFullAccessAliyunRAMReadOnlyAccessK8S中RBAC访问权限：管理员 |  |
| ContainerOperation容器运维人员 | 云原生相关的运维权限 | 使用自定义权限策略AliyunCSFullAccess AliyunContainerRegistryFullAccessK8S中RBAC访问权限：运维人员 |  |
| ContainerDevelop 容器环境开发人员 | 云原生相关的开发人员权限 | 使用自定义权限策略{"Statement": [{"Action": ["cs:Get*","cs:List*","cs:Describe*"],"Effect": "Allow","Resource": ["acs:cs:*:*:cluster/xx" #请替换为您实际的集群ID。]}],"Version": "1"}K8S中RBAC访问权限：自定义ClusterRole（约束特定的NS） |  |
| ContainerReadOnly 容器环境只读 | 云原生相关的只读权限 | 使用自定义权限策略AliyunCSReadOnlyAccess AliyunContainerRegistryReadOnlyAccessK8S中RBAC访问权限：受限用户 |  |

##### 附：容器服务ACK在集群层面预置四种角色

| **角色** | **集群内RBAC权限** |
| --- | --- |
| 管理员 | 对所有命名空间下所有资源的读写权限。 |
| 运维人员 | 对所有命名空间下控制台可见Kubernetes资源的读写权限，对集群节点、存储卷、命名空间、配额的只读权限。 |
| 开发人员 | 对所有命名空间或所选命名空间下控制台可见Kubernetes资源的读写权限。 |
| 受限用户 | 对所有命名空间或所选命名空间下控制台可见Kubernetes资源的只读权限。 |

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云SSO | [云SSO](https://help.aliyun.com/zh/cloudsso/product-overview/what-is-cloudsso)提供基于阿里云资源目录RD（Resource Directory）的多账号统一身份管理与访问控制。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/cloudsso/product-overview/billing-methods)。 |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 访问控制RAM | [访问控制（RAM）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |
| 容器服务ACK | [阿里云容器服务Kubernetes版](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/product-overview/what-is-ack)（Alibaba Cloud Container Service for Kubernetes，简称容器服务ACK）是全球首批通过Kubernetes一致性认证的服务平台，提供高性能的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理，让您轻松高效地在云端运行Kubernetes容器化应用。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/ack/billing-information)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| RBAC | RBAC（Role-Based Access Control）是基于角色的访问控制，通过RBAC可以将权限与集群角色相关联，从而为不同角色成员配置不同的权限策略。本方案主要介绍如何配置RAM角色对应的Kubernetes集群内RBAC权限。 |
| 单点登录（SSO） | 云SSO支持基于SAML 2.0的单点登录SSO（Single Sign On）。阿里云是服务提供商（SP），而企业自有的身份管理系统则是身份提供商（IdP）。通过单点登录，企业员工可以使用IdP中的用户身份直接登录云SSO。IdP和SP的具体含义如下：身份提供商IdP（Identity Provider）可以提供身份管理服务。常见的IdP：Microsoft Active Directory Federation Service （AD FS）、Azure AD、Okta以及KeyCloak等。服务提供商SP（Service Provider）是利用IdP的身份管理功能，为用户提供具体服务的应用。SP会使用IdP提供的用户信息。一些非SAML协议的身份系统（例如：OpenID Connect），也把服务提供商称作IdP的信赖方。更多信息，请参见[单点登录概述](https://help.aliyun.com/zh/cloudsso/user-guide/overview)。 |

## 安全性

### SAML及SCIM协议

方案中使用业界标准的SAML协议及SCIM协议保障数据安全传递，相关介绍详情[SAML 2.0](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)及[SCIM](http://www.simplecloud.info/)。

### 开启MFA

为提升安全性，云SSO默认开启多因子身份认证[MFA](https://help.aliyun.com/zh/account/support/what-is-the-mfa)，建议持续开启，云SSO相应管理操作参见[MFA管理](https://help.aliyun.com/zh/cloudsso/user-guide/manage-mfa)。

### ACK集群的认证和授权

#### 使用临时Kubeconfig和Apiserver认证

ACK默认返回的集群访问凭证Kubeconfig中的证书有效期是3年，若Kubeconfig发生泄露，攻击者可以直接获得集群Apiserver的访问权限，默认的ServiceAccount Token同样是一种长期有效的静态凭据，如果泄露攻击者同样可以获得该ServiceAccount绑定的集群访问权限，直到该ServiceAccount被删除。因此请您及时吊销可能发生泄露的已下发Kubeconfig凭证。具体操作，请参见[吊销集群的KubeConfig凭证](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/revoke-a-kubeconfig-credential)。关于ACK集群的访问凭证，请参见[生成临时的KubeConfig](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster)。

#### 遵循权限最小化原则访问阿里云资源

如果某个用户需要访问ACK集群，无需为用户分配访问其他云产品资源的权限，保证用户访问云产品资源权限最小化。可以通过配置RAM和RBAC为该用户授予访问ACK集群的权限。

#### 在创建RoleBindings和ClusterRoleBindings时使用最低访问权限

和授予访问云资源的权限一样，在创建RoleBindings和ClusterRoleBindings时，同样需要遵循权限最小化原则。应该尽量避免在创建Role和ClusterRole时使用["*"]，应该明确到具体的Verbs。如果您不确定要分配哪些权限，请考虑使用类似[audit2rbac](https://github.com/liggitt/audit2rbac)之类的工具，根据Kubernetes审计日志中观察到的API调用自动生成角色和绑定。

#### 定期对集群的访问权限进行审计

对集群的访问权限可能会随着时间的推移而改变。需要集群的安全管理运维人员定期审核RAM配置和配置RAM用户RBAC权限来查看指定RAM用户是否被分配了合适的权限。或关于使用开源工具来检查绑定到特定服务帐户、用户或组的RBAC权限，并及时收敛不符合需要的过大权限配置。请参见[kubectl-who-can](https://github.com/aquasecurity/kubectl-who-can)和[rbac-lookup](https://github.com/FairwindsOps/rbac-lookup)。

## 注意事项

### ACK产品范围

容器服务ACK面向多种业务场景提供多样化的Kubernetes集群，本方案主要是介绍ACK集群场景下。客户选择其他的ACK产品如：ACK ONE可以自行查阅产品帮助文档。

## 实施步骤

### 实施准备

- 确保已在「企业管理账号」中开通了云SSO功能，并在云SSO中完成云SSO用户创建。
- 确保已在「成员账号」中已开通了ACK集群。

### 实施场景

- 场景一：集群应用运维人员
- 场景二：集群应用的开发人员
- 场景三：集群内应用的权限管理员

### 数据规划

本方案会围绕三种常见的用户权限来介绍当企业使用了云SSO与ACK产品之后，如何更好地规划用户权限。相关数据规划如下表：

| 云产品 | 参数 | 示例 |
| --- | --- | --- |
| 云SSO | 人员管理-用户 | 集群应用运维：zhangsan集群应用开发：lisi集群应用权限管理员：yaofang |
| 访问配置管理 | 集群应用运维角色：ACK-SRE集群应用开发角色：ACK-DEV集群应用权限管理：ACK-APP-ADMIN |  |
| ACK | 集群RBAC | 集群应用运维：运维人员集群应用开发：开发人员集群应用权限管理：自定义 |

### 操作流程

通过云SSO配置人员操作ACK的权限，操作流程如下图：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970863.png)

### 操作步骤

本操作步骤按照上面介绍到的这三种场景展开介绍。

#### 场景一：授权对象为集群与集群内应用的运维人员

##### 云SSO中授权

容器服务ACK在云SSO侧提供了AliyunCSFullAccess和AliyunCSReadOnlyAccess两个系统策略。

- AliyunCSFullAccess包含了容器服务ACK全部OpenAPI的读写访问权限。
- AliyunCSReadOnlyAccess包含了容器服务ACK全部OpenAPI的只读访问权限。

要登录[云SSO管理控制台](https://cloudsso.console.aliyun.com/cn-shanghai/overview)，根据需要选择绑定其中一个系统策略，创建访问配置：ACK-SRE。具体操作，请参见[创建访问配置](https://help.aliyun.com/zh/cloudsso/user-guide/create-an-access-configuration)。

配置完成效果：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970866.png)

##### RBAC中授权

完成云SSO中授权后，您还需要为云SSO中的角色授予对应集群的RBAC权限。容器服务ACK在集群层面提供了四种预置角色。

| **角色** | **集群内RBAC权限** |
| --- | --- |
| 管理员 | 对所有命名空间下所有资源的读写权限。 |
| 运维人员 | 对所有命名空间下控制台可见Kubernetes资源的读写权限，对集群节点、存储卷、命名空间、配额的只读权限。 |
| 开发人员 | 对所有命名空间或所选命名空间下控制台可见Kubernetes资源的读写权限。 |
| 受限用户 | 对所有命名空间或所选命名空间下控制台可见Kubernetes资源的只读权限。 |

此场景下，您可以在[容器服务管理控制台](https://cs.console.aliyun.com/)授权管理页面，为授权对象配置目标集群和对应命名空间的访问权限为**运维人员**。

- 选择子账号：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970867.png)
- 集群RBAC配置![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970872.png)

##### 场景验证

1. 用户：zhangsan在云SSO中登录指定的云账号。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970869.png)
2. 尝试创建一个新的命名空间，会提示没有权限。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970868.png)
3. 在命名空间：default下面可以成功创建一个配置项。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970875.png)

#### 场景二：授权对象为集群内应用的开发人员

授权对象只需要拥有ACK集群内Kubernetes资源对象的操作权限（即RBAC授权），无需云上资源的访问权限。

##### 云SSO中授权

您需要在[云SSO管理控制台](https://cloudsso.console.aliyun.com/cn-shanghai/overview)，创建访问配置：ACK-DEV，使用自定义策略。具体操作，请参见[创建访问配置](https://help.aliyun.com/zh/cloudsso/user-guide/create-an-access-configuration)。自定义策略内容如下所示：

```
{
  "Statement": [
    {
      "Action": [
        "cs:Get*",
        "cs:List*",
        "cs:Describe*"
      ],
      "Effect": "Allow",
      "Resource": [
        "acs:cs:*:*:cluster/c5cc77f5180a449a4a48cf8001831xxxx" #请替换为您实际的集群ID。
      ]
    }
  ],
  "Version": "1"
}
```

如果您需要为授权对象添加所有集群的只读权限，可以为其添加容器服务ACK提供的RAM系统策略**AliyunCSReadOnlyAccess**。

配置完成效果：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970879.png)

##### RBAC中授权

此场景下，您可以在[容器服务管理控制台](https://cs.console.aliyun.com/)授权管理页面，为授权对象配置目标集群和对应命名空间的访问权限为**开发人员**。

- 选择子账号：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970881.png)
- 集群RBAC配置![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970874.png)

##### 场景验证

1. 用户：lisi在云SSO中登录指定的云账号。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970882.png)
2. 尝试创建一个新的命名空间，会提示没有权限。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970883.png)

#### 场景三：授权对象为集群内应用的权限管理员

授权对象需要管理其他RAM用户或RAM角色的RBAC权限。默认情况下，RAM用户或RAM角色不具备对其他RAM用户或RAM角色授权RBAC的权限。当授权对象进入[容器服务管理控制台](https://cs.console.aliyun.com/)授权管理页面时，如果界面提示**当前子账号不具备授权管理权限，请联系主账号或权限管理员授权**，则说明授权对象缺少必要的RAM授权或对集群的RBAC管理员授权。

##### 云SSO中授权

您需要在[云SSO管理控制台](https://cloudsso.console.aliyun.com/cn-shanghai/overview)，创建访问配置：ACK-APP-ADMIN，使用自定义策略。具体操作，请参见[创建访问配置](https://help.aliyun.com/zh/cloudsso/user-guide/create-an-access-configuration)。自定义策略内容如下所示：

```
{
    "Statement": [{
            "Action": [
                "ram:Get*",
                "ram:List*",
                "cs:GetUserPermissions",
                "cs:GetSubUsers",
                "cs:GrantPermission",
                "cs:Get*",
                "cs:List*",
                "cs:Describe*"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "ram:AttachPolicyToUser",
                "ram:AttachPolicyToRole"
            ],
            "Effect": "Allow",
            "Resource":  [
                "acs:ram:*:*:policy/xxxxxx", # xxxxxx需要替换成您想要绑定的RAM策略名称。如果您替换成*，表示授权对象拥有所有RAM策略的授权绑定能力。
                "acs:*:*:*:user/*"
            ]
        }
    ],
    "Version": "1"
}
```

配置完成效果：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970886.png)

##### RBAC中授权

需要为授权对象配置目标集群和对应命名空间的访问权限为**管理员**或者自定义角色中的**cluster-admin**。

此场景下，您可以在[容器服务管理控制台](https://cs.console.aliyun.com/)授权管理页面，为授权对象配置目标集群和对应命名空间的访问权限为**cluster-admin**。

- 选择子账号：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970887.png)
- 集群RBAC配置![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970888.png)

##### 场景验证

1. 用户：yaofang在云SSO中登录指定的云账号。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970889.png)
2. 给其他RAM用户或角色授权![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970890.png)

## 故障排除

### 控制台提示子账号不具备授权管理权限

**问题原因：**

当前RAM用户或RAM角色缺少必要的RAM授权或对集群的RBAC管理员权限。默认情况下，RAM用户或RAM角色不具备对其他RAM用户或RAM角色授权RBAC的能力。

**解决办法：**

- RBAC管理员权限：需要确保当前登录的RAM用户或RAM角色在目标集群或命名空间上被授予预置的管理员角色或自定义中的cluster-admin角色。
- RAM授权权限：需要确保当前登录的RAM用户或RAM角色被授予必要的RAM权限，策略内容需要包括：列举其他RAM用户或RAM角色给指定RAM用户或RAM角色授予RAM权限策略查看指定RAM用户或RAM角色的K8s RBAC权限配置K8s RBAC授权能力

### 根据错误信息判断是RAM授权问题还是RBAC授权问题

#### RAM权限缺失问题

**问题现象**

API或控制台上报类似下方的错误信息：

```
RAM policy Forbidden for action cs:DescribeEvents
STSToken policy Forbidden for action cs:DescribeClusterNodes
```

**问题原因**

从这个报错信息来看，跟RAM授权有关系。权限过小，导致无法操作相关资源。

**解决方案**

1、登录[RAM控制台](https://ram.console.aliyun.com/roles)选择指定的角色检查其授权范围。添加对应的授权策略。

### 当前账号未被授予该操作所需的集群RBAC权限

**问题现象**

当您访问控制台时，出现报错“当前账号未被授予该操作所需的集群RBAC权限”，错误码：**ForbiddenQueryClusterNamespace**或者**APISERVER.403**。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4966581571/p970884.png)

**问题原因**

您使用的账号未被授予当前操作所需的集群RBAC权限。

**解决方案**

1. 使用阿里云账号或者具有管理员权限的账号登录[容器服务管理控制台](https://cs.console.aliyun.com/)，在左侧导航栏中选择**授权管理**。
2. 在**子账号**页签查找出现报错的用户名，单击用户名右侧的**管理权限**。
3. 在**授权管理**页面，选择对应集群和命名空间，添加所需权限。

## 相关内容

- [云SSO产品介绍](https://help.aliyun.com/product/252811.html)
- [ACK授权最佳实践](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/best-practices-of-authorization)
- [ACK身份认证与访问控制](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/identity-verification-and-access-control)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-114（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
