<!-- source: https://help.aliyun.com/zh/well-architected/solution-39 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929202 -->

# 企业多账号组织全局访问边界控制

资源目录提供管控策略功能，企业可以通过管理账号集中制定管理规则，并将这些管理规则应用于资源目录的各级资源结构（资源夹、成员）上，管控各成员内资源的访问规则，确保安全合规和成本可控。


# 方案概述

![](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/7835/1657523186239-35d284f5-6665-4c71-ad3c-0476c657c2cb.png)

当一家企业尝试使用多账号来规划、部署业务。如果对各成员的行为不加以管控，就会破坏运维规则，带来安全风险和成本浪费。资源目录提供管控策略功能，企业可以通过管理账号集中制定管理规则，并将这些管理规则应用于资源目录的各级资源结构（资源夹、成员）上，管控各成员内资源的访问规则，确保安全合规和成本可控。例如：禁止成员申请域名、禁止成员删除日志记录等。

# 方案优势

## 集中式管控

管理员能够在管控策略后台编写管控策略，并应用到不同的成员账号，不需要在多处进行管控策略配置，能够做到集中式管理。

# 客户场景

## 管控企业多账号组织全局访问边界

### 场景描述

随着客户业务的大量上云，员工（user）被密集且复杂的授予各种资源、服务的权限以运作这些业务，企业管理端很难非常细致地考量每个业务的具体授权，但希望能够从顶层做出企业的全局管控，即制定企业“大规范”以限定用户权限边界，以免超出公司的合规范围。客户可以创建基于预期的管控策略，以满足企业顶层管控需要。

### 适用客户

- 使用资源目录管理云上多个账号的企业客户
- 中心安全合规团队，制订统一的管控策略

# 客户案例

## 客户背景

某通讯企业X，是全球领先的综合通信解决方案提供商。公司在全球自建了多个私有云IDC，实现应用全球化的分布式部署，支撑公司业务全球运营，从自身出发打造“极致云公司”，数字化转型的解决方案也得到业界和权威机构的认可。但自建云模式存在投入大、站点有限、资源交付周期长的问题，考虑到公有云资源弹性、成本低廉、覆盖地域广的优势。于是在2020年5月，公司决定将部分业务向公有云转移，提升业务效率，降低成本。

## 客户痛点

![](https://intranetproxy.alipay.com/skylark/lark/0/2021/png/7854/1629811740564-1190c5a9-4df0-453e-8d87-19effb5d7eaf.png)

如上图所示：

- 普通管理员有个性化的管理需求，而合规管理员需要定全局的规范。
- 不同角色需要授不同的权限。

## 实施方案

- 使用资源目录进行多账号统一管理，不同二级单位创建不同文件夹
- 在不同文件夹上面创建管控策略，限制部分二级单位在账号内的操作行为

管控策略示例如下

- 名称：DenyPublicNetworkProductsInApplicationAccount。
- 描述：除了网络管理员禁止创建具有公网访问能力的资源，包括EIP实例、域名。
- 绑定节点：Applications资源夹。
- 策略内容：

```
{
    "Version": "1",
    "Statement": [
        {
            "Action": [
                "vpc:AllocateEipAddress",
                "vpc:AllocateEipAddressPro",
                "vpc:AllocateEipSegmentAddress",
                "domain:SaveSingleTaskForCreatingOrderActivate",
                "domain:SaveSingleTaskForCreatingOrderRenew",
             	  "domain:SaveBatchTaskForCreatingOrderActivate",
                "domain:SaveBatchTaskForCreatingOrderRenew"
            ],
            "Resource": [
                "*"
            ],
            "Effect": "Deny",
            "Condition": {
                "StringNotLike": {
                    "acs:PrincipalARN": "acs:ram:*:*:role/sharedserviceaccount"
                }
            }
        }
    ]
}
```

## 客户收益

- 满足中心化运维在繁杂的授权逻辑之上轻松的制定管控限制，实现前置阻止而非后置发现
- 解决企业顶层管控难题。支持制定企业“大规范”以限定用户权限边界，以免超出公司的合规范围

# 方案架构

## 工作原理

### 基于资源目录实现从上至下的管控

架构如下：

![](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/7835/1657523204095-b689eccd-e0b9-4e20-8d86-e7a693a3dd01.png)

管控策略工作原理如下：

1. 使用管理账号开启管控策略功能。开启管控策略功能后，系统策略FullAliyunAccess将默认绑定到资源目录内的所有资源夹及成员，此策略允许所有操作，以防止管控策略的不当配置造成意料之外的访问失败。
2. 使用管理账号创建管控策略。更多信息，请参见[创建自定义管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/create-a-custom-access-control-policy)。
3. 使用管理账号将管控策略绑定到资源目录节点（资源夹、成员）。更多信息，请参见[绑定自定义管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/attach-a-custom-access-control-policy)。管控策略允许绑定到资源目录中的任何资源夹或成员。管控策略具备向下继承的特点，例如：为父资源夹设置管控策略A，为子资源夹设置管控策略B，则管控策略A和管控策略B都会在子资源夹及其下的成员中生效。**说明**请先进行局部小范围测试，确保策略的有效性与预期一致，然后再绑定到全部目标节点（资源夹、成员）。
4. 当成员中的RAM用户或RAM角色访问阿里云服务时，阿里云将会先进行管控策略检查，再进行账号内的RAM权限检查。具体如下：

- 管控策略鉴权从被访问资源所在账号开始，沿着资源目录层级逐级向上进行。
- 在任一层级进行管控策略鉴权时，命中拒绝（Deny）策略时都可以直接判定结果为拒绝（Explicit Deny），结束整个管控策略鉴权流程，并且不再进行账号内基于RAM权限策略的鉴权，直接拒绝请求。
- 在任一层级进行管控策略鉴权时，如果既未命中拒绝（Deny）策略，也未命中允许（Allow）策略，同样直接判定结果为拒绝（Explicit Deny），不再进入下一个层级鉴权，结束整个管控策略鉴权流程，并且不再进行账号内基于RAM权限策略的鉴权，直接拒绝请求。
- 在某一层级鉴权中，如果未命中拒绝（Deny）策略，而命中了允许（Allow）策略，则本层级鉴权通过，继续在父节点上进行管控策略鉴权，直至Root资源夹为止。如果Root资源夹鉴权结果也为通过，则整个管控策略鉴权通过，接下来进入账号内基于RAM权限策略的鉴权。更多信息，请参见[权限策略判定流程](https://help.aliyun.com/zh/ram/policy-evaluation-process)。
- 管控策略对服务关联角色不生效。关于服务关联角色的详情，请参见[服务关联角色](https://help.aliyun.com/zh/ram/user-guide/service-linked-roles)。
- 阿里云将会评估被访问的账号自身及其所在的每一层级上绑定的管控策略，从而确保绑定在较高层级上的管控策略可以在其下的所有账号上生效。

# 产品费用及名词

## 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)（Resource Directory）是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 管控策略 | [管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)是一种基于资源结构（资源夹或成员账号）的访问控制策略，可以统一管理资源目录各层级内资源访问的权限边界，建立企业整体访问控制原则或局部专用原则。管控策略只定义权限边界，并不真正授予权限，您还需要在某个成员账号中使用访问控制（RAM）设置权限后，相应身份才具备对资源的访问权限。 | 免费 |

## 名词解释

| 名称 | 说明 |
| --- | --- |
| 管控策略语言 | 管控策略语法和结构与RAM的基本相同。详情可以[查看链接](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/languages-of-access-control-policies) |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |

# 安全性

- 强烈建议在测试环境中验证Policy策略，可以在一个测试账号中进行验证。比如在资源管理主账号中开通了资源目录，然后在资源目录中创建一个测试账号，然后写一段Policy下发到这个测试账号上进行验证。
- 请先进行局部小范围测试，确保策略的有效性与预期一致，然后再绑定到全部目标节点（资源夹、成员）。
- 本方案是需要客户在资源管理账号中进行。建议在资源管理账号中开设RAM 子用户，并授以下的权限：

配置RAM用户的访问权限：

- **授权范围**为**整个云账号**，然后选择权限策略。
- **系统策略**：从**权限策略名称**列表，选择需要的权限。

| **权限策略名称** | **说明** |
| --- | --- |
| AliyunResourceDirectoryFullAccess | 能够管理资源目录 |

# 注意事项

## 使用限制

| **限制项** | **最大值** |
| --- | --- |
| 资源目录内最多允许创建自定义管控策略的数量 | 1500个 |
| 每个节点（资源夹、成员）最多允许绑定自定义管控策略的数量 | 10个 |
| 每个自定义策略的最大长度 | 2048个字符 |

## 支持管控策略的云服务

目前不是全部云产品都支持管控策略，需要先查看[支持管控策略的云服务](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)判断一下当前业务中是否都在这个列表中。

# 实施步骤

## 实施准备

- 确保已在「企业管理账号」开通了资源目录。
- 确保在资源目录中已经明确要对哪些组织或成员账号实施管控策略。

## 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：15分钟。

## 操作步骤

### 步骤一：开启管控策略

1. 登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)。
2. 在左侧导航栏，选择**资源目录 > 管控策略**。
3. 单击**开启管控策略**。
4. 单击**确定**。
5. 单击**刷新**，查看开启状态。

### 步骤二：创建自定义管控策略

1. 登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)。
2. 在左侧导航栏，选择**资源目录 > 管控策略**。
3. 在**策略列表**页签，单击**创建策略**。
4. 输入**策略名称**和**策略描述**。

示例：

禁止安全账号 购买域名：策略名称定为 denySecAccountBuyDomain

禁止集团官网账号 使用杭州区域的ECS服务，策略名称定为：denyPageAccountEcsRegion

1. 编辑JSON格式的策略内容。

- denySecAccountBuyDomain策略内容：

```
{
    "Version": "1",
    "Statement": [
        {
            "Action": [
                "domain:CreateOrderActivate"
            ],
            "Resource": "*",
            "Effect": "Deny"
        }
    ]
}
```

- denyPageAccountEcsRegion策略内容：

```
{
    "Version": "1",
    "Statement": [{
        "Effect": "Deny",
        "Action": [
            "ecs:*"
        ],
        "Resource": "acs:ecs:cn-hangzhou:*:*"
    }]
}
```

1. 单击**确定**。

### 步骤三：绑定自定义管控策略

1. 登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)。
2. 在左侧导航栏，选择**资源目录 > 管控策略**。
3. 在**策略绑定**页签下的左侧组织结构树中，单击目标资源夹或成员。
4. 在右侧页面，单击**绑定策略**。
5. 在**绑定策略**页面，选择需要绑定的管控策略。
6. 单击**确定**。

### 步骤四：验证

通过RAM用户或RAM角色登录这2个成员账号。集团官网账号是无法购买美东地域的ECS服务。安全账号是无法购买域名服务。

## 源代码

本章节提供一些模板Policy代码示例，大家可以结合实际的业务进行定制修改。

## 只允许使用企业指定镜像（Golden Image）创建ECS

### 业务场景

企业基于内部安全合规要求，在各操作系统的Base镜像之上添加安全合规基线配置以及预装必要的agent，如cloud-init、安全agent、监控agent等**，形成企业自定义操作系统镜像（即Golden Image），要求企业内部只能基于此专属镜像创建云服务器。**

### Control Policy模板

下文是管控策略的示例，此策略使用“Deny”禁止了两种行为。第一条语句通过限制 ecs:ImageSource 的值实现禁止使用系统镜像创建 ECS 实例，第二条语句限制只允许使用 Id 为“i-abcd”（需要替换为真实的镜像 ID）的镜像创建 ECS 实例。

```
{
  	"Statement": [
    	{
      		"Action": [
        			"ecs:RunInstances",
        			"ecs:CreateInstance"
      		],
      		"Effect": "Deny",
      		"Resource": "acs:ecs:*:*:instance/*",
      		"Condition": {
        			"StringEquals": {
          				"ecs:ImageSource": "System"
        			}
      		}
    		},
    		{
      		"Action": [
        			"ecs:RunInstances",
        			"ecs:CreateInstance"
      		],
      		"Effect": "Deny",
      		"Resource": "acs:ecs:*:*:image/*",
      		"Condition": {
        			"StringNotLike": {
          				"Resource": "acs:ecs:*:*:image/i-abcd"
        			}
      		}
    		}
  	],
  	"Version": "1"
}
```

## 只允许购买指定规格(SKU)/ 指定区域(Region)的ECS实例

### 业务场景

考虑集中管控、网络规划和成本等因素，企业客户上云时往往要求限制业务允许使用ECS的规格，并选择一到两个区域作为部署资源的主要区域（跨区域有网络延迟和流量费用）。

### Control Policy模板

下文是管控策略的示例，此策略通过限制 ecs:InstanceType 的值实现了只允许创建指定规格的 ECS 实例。限制条件 ecs:InstanceType 的值为ECS 定义的实例规格，可以通过文档 [实例规格族](https://help.aliyun.com/zh/ecs/user-guide/overview-of-instance-families)查询，或调用[DescribeInstanceTypes](https://help.aliyun.com/zh/ecs/api-describeinstancetypes)查看目标实例规格的性能数据和值。

```
{
    "Version": "1",
    "Statement": [
        {
          	"Effect": "Deny",  
          	"Action": [
                "ecs:RunInstances",
            		"ecs:CreateInstance"
            ],
          	"Resource": "*",
          	"Condition": {
                "StringNotLike": {
                    "ecs:InstanceType": [
                        "ecs.g7.large",
                        "ecs.g7.xlarge"
                    ]
                }
            }
        }
    ]
}
```

类似的，以下策略通过限制 region 的值实现了只允许在深圳区域创建 ECS 实例。

```
{
  "Version": "1",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "ecs:RunInstances",
        "ecs:CreateInstance",
        "ecs:AllocateDedicatedHosts",
        "ecs:CreateDedicatedHostCluster"
      ],
      "Resource": [
        "acs:*:*cn-qingdao:*:*",
        "acs:*:*cn-beijing:*:*",
        "acs:*:*cn-zhangjiakou:*:*",
        "acs:*:*cn-huhehaote:*:*",
        "acs:*:*cn-wulanchabu:*:*",
        "acs:*:*cn-hangzhou:*:*",
        "acs:*:*cn-shanghai:*:*",
        "acs:*:*cn-guangzhou:*:*",
        "acs:*:*cn-heyuan:*:*",
        "acs:*:*cn-chengdu:*:*",
        "acs:*:*cn-nanjing:*:*",
        "acs:*:*cn-hongkong:*:*",
        "acs:*:*ap-southeast-1:*:*",
        "acs:*:*ap-southeast-2:*:*",
        "acs:*:*ap-southeast-3:*:*",
        "acs:*:*ap-southeast-5:*:*",
        "acs:*:*ap-south-1:*:*",
        "acs:*:*ap-northeast-1:*:*",
        "acs:*:*us-west-1:*:*",
        "acs:*:*us-east-1:*:*",
        "acs:*:*eu-central-1:*:*",
        "acs:*:*eu-west-1:*:*",
        "acs:*:*me-east-1:*:*",
				"acs:*:*rus-*:*:*"
      ]
    }
  ]
}
```

## 禁止创建具有公网访问能力的网络资源

### 业务场景

企业云上环境按照是否提供面向公网的服务可以分为两类：公网型/内网型。内网型云上环境不需要公网资源，因此，基于安全和管控需求，企业希望此类环境禁止部署EIP、NAT等具有公网访问能力的网络资源。

### Control Policy模板

下文是管控策略的示例，此策略使用“Deny”禁止创建相关云产品：EIP，NAT。

**Tips：**

1）策略通过"Deny"，同时禁止了创建EIP、NAT资源的操作（Action）——类似可以禁止创建其他云资源；

2）策略的"Condition"，定义了谁可以例外（"StringNotLike"）操作：比如模板中只允许资源目录默认用来访问成员的角色ResourceDirectoryAccountAccessRole执行此操作——如果企业内部定义了管理员用户或管理角色，您也可以添加或修改PrincipalARN的值，自定义限制条件；

```
{
  "Version": "1",
  "Statement": [
    {
      "Action": [
        "vpc:AllocateEipAddress",
        "vpc:AllocateEipAddressPro",
        "vpc:AllocateEipSegmentAddress",
        "vpc:CreateNatGateway",
        "ecs:AllocatePublicIpAddress",
      ],
      "Resource": [
        "*"
      ],
      "Effect": "Deny",
      "Condition": {
        "StringNotLike": {
          "acs:PrincipalARN": "acs:ram:*:*:role/resourcedirectoryaccountaccessrole"
        }
      }
    }
  ]
}
```

# 故障排除

## 为什么无法配置Action中应用通配符* ?

原因：

- 目前因为接入度的问题，还无法确保通配符 * 能够满足。

# 方案卸载

## 解绑自定义管控策略

您可以随时解绑自定义管控策略，解绑成功后，成员对资源的操作将不受该管控策略限制。

注意：系统策略FullAliyunAccess会默认绑定在每个资源夹和成员上，且不允许解绑。

操作步骤：

1. 登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)。
2. 在左侧导航栏，选择**资源目录 > 管控策略**。
3. 在**策略绑定**页签下的左侧组织结构树中，单击目标资源夹或成员。
4. 在右侧的管控策略列表中，单击目标管控策略**操作**列的**解绑**。
5. 单击**确定**。

## 删除自定义管控策略

对于未绑定任何资源夹或成员的自定义管控策略，您可以随时删除。

注意：

- 系统管控策略不支持删除。
- 对于已绑定了资源夹或成员的自定义管控策略，需要先解绑，然后才能删除。具体操作，请参见[解绑自定义管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/detach-a-custom-access-control-policy)。

操作步骤：

1. 登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)。
2. 在左侧导航栏，选择**资源目录 > 管控策略**。
3. 在**策略列表**页签，单击目标管控策略**操作**列的**删除**。
4. 单击**确定**。

## 关闭管控策略功能

如果您不想限制资源目录内资源夹和成员的权限，则可以关闭管控策略功能。

注意：

- 关闭管控策略功能后，您绑定到资源夹和成员上的管控策略会全部自动解绑。但管控策略本身不会被删除，只能不能再绑定到任何目标对象上。

操作步骤：

1. 登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)。
2. 在左侧导航栏，选择**资源目录 > 管控策略**。
3. 在**管控策略**页面上方的文字描述区域，单击**关闭管控策略**。
4. 单击**确定**。
5. 单击**刷新**，查看关闭状态。当状态显示**管控策略已关闭**时，表示管控策略功能已关闭。

# 相关内容

- [资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)
- [自定义管控策略示例](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/examples-of-custom-access-control-policies)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-39（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
