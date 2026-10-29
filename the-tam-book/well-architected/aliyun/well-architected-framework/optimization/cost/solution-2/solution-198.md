<!-- source: https://help.aliyun.com/zh/well-architected/solution-198 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929436 -->

# 企业商务优惠管理方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972414.png)

当一家企业与阿里云平台签订框架协议之后，企业的阿里云账号就会享受到框架协议中的优惠。但是如果企业需要全新的阿里云账号用于新业务，需要把该账号向阿里云商务经理重新报备增加到框架协议中。如果完全通过手动的方式来管理账号优惠，企业无法保证所有账号都能享受相同的优惠。同时企业框架优惠一旦设置，企业内部所有员工均可以看到商务优惠信息。对于部分商务敏感型企业存在商务信息保密的问题。该方案重点阿里云上如果高效、安全地管理企业商务折扣，旨在帮助对商务信息有合规要求的企业提供系统的管理方案。

## 方案优势

### 确保实体下多账号优惠

通过配置实体优惠，企业可以在为新业务创建同企业实名的阿里云账号时，自动让新账号享受相同框架优惠。相比每次创建新账号找商务经理报备，该方案基于主体的商务优惠管理方式避免手动报备引起的折扣未配置问题，简化企业管理多账号商务折扣的流程。

### 商务折扣权限回收

通过独立的优惠查看权限配置，企业财务人员可以自主规定企业内部商务信息保密层级，为不同层级的员工设置不同的财务权限。提升云上财务管理流程的合规性。

## 客户场景

### 企业IT效益中心

#### 场景描述

企业IT团队为了从成本中心向效益中心转型，希望由企业IT团队统一为其他子公司IT业务提供云资源供给服务。为了从云资源供给、运维场景中获得IT效益收入，IT团队希望向子公司隐藏实际云资源成本，通过云平台优惠和企业内部优惠之间的差价获得IT效益。

#### 适用客户

集团型企业，每个子公司都有独立的阿里云账号进行业务管理，集团和子公司之间采用分散式的IT管理模式。

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972415.png)

云上财务管理权限有两个层级：

- 阿里云账号级别：在多账号架构下，通过企业账号中心可以为成员账号设置差异化财务权限。账号级别的财务权限除了账号内财务功能的读写权限之外，还可以设置跨账号的财务管理权限。比如跨账号结算权限、优惠同步。
- 用户级别：在RAM内可以为企业内不同用户设置差异化的财务权限。权限仅包含对于账号内的财务功能读写。比如对用户隐藏折扣、用户不可操作财务配置。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 企业账号中心 | 企业账号管理中心为企业用户提供集中化、一站式账号管理解决方案。企业管理员可以创建组织，账号，并对账号进行授权，设置财务相关权限和共享策略。企业管理员还可以邀请其它企业，双方成为关联企业，建立跨企业之间的组织关系，设置跨企业之间的财务相关权限和共享策略，包含常见的[组织与账号管理](https://ea.console.aliyun.com/account-manage/?spm=a2c81.c0e1020.sidebar.nav_46.3b8d1127k9ZCiq)、[账单管理](https://usercenter2.aliyun.com/finance/expense-report/overview)、[发票管理](https://usercenter2.aliyun.com/invoice/list/aliyun)、[资金管理](https://usercenter2.aliyun.com/finance/fund-flow)以及[资源共享管理](https://help.aliyun.com/zh/user-center/cost-manager)等。 | 免费，详情参见[功能介绍](https://help.aliyun.com/zh/document_detail/439725.html)。 |
| 访问控制RAM | [访问控制（RAM）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 管理员账号 | 一个企业有且只能有一个管理员账号。企业管理员账号代表企业拥有对企业管理权限。 |
| 成员账号 | 企业除管理员账号外其他账号均称为成员账号。管理员可以创建成员账号、邀请成员账号加入组织、从组织中删除、修改成员账号信息、进行成员账号授权等操作。一个账号只允许加入一个组织节点。 |
| 管理员角色 | 角色类型的一种。管理员角色关联的权限可以对被授权账号所管理的范围内账号生效。如：授权账号UID1具有管理员角色“Role001”，则账号UID1具有管理员角色"Role001"关联的权限，且生效范围为UID1所在组织目录以及下级组织目录的所有账号。 |
| 成员角色 | 角色类型的一种。成员角色关联的权限只对被授权账号本身生效。如：授权账号UID1具有成员角色“Role002”，则账号UID1具有成员角色"Role002"关联的权限。 |
| 角色授权 | 管理员对账号进行授予权限的过程。对账号授权时，只能授权账号相应权限的角色。 |
| RAM成员账号 | RAM（Resource Access Management）是阿里云提供的一项管理用户身份与权限的服务。RAM允许在一个阿里云账号（即UID）下创建并管理多个身份（RAM用户），并允许给单个身份或一组身份分配不同的权限，从而实现不同RAM用户拥有不同权限的目的。 |
| STS角色 | STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。有权限的RAM用户可以使用自己的访问密钥调用AssumeRole接口，以获取某个RAM角色的STS Token，从而使用STS Token访问阿里云资源。通过STS角色可以实现跨UID之间的授权。 |
| 官网目录价 | 或称原价，指的是基于用户选配的商品配置对应的原始价格。 |
| 折扣价格 | 或称折扣后价格、优惠后价格，指的是基于用户选配的商品配置匹配大客户合同折扣后的价格信息，具体包含应付金额、优惠金额。 |
| 自动支付 | 阿里云提供的一种自动化支付能力。走自动支付流程时，仅允许通过阿里云自有支付渠道支付（自有渠道如信控额度、账户余额），不支持支付宝、网银等第三方支付渠道。如果是国内站，会优先使用信控额度支付，然后才是账户余额。如果是国际站，会使用信控额度支付。 |

## 安全性

### 费用中心RAM策略

阿里云费用中心接入RAM访问控制，提供基于RAM的权限策略控制，详情参见[费用中心RAM策略介绍](https://help.aliyun.com/zh/user-center/ram-policies-for-billing-management)。

## 注意事项

### 企业账号中心开通说明

1. 仅支持企业认证账号开通。且您的账号不是阿里云生态合作伙伴、虚商伙伴、生态伙伴客户；
2. 如果您已使用企业财务功能，可通过企业财务升级至企业账号中心，具体升级流程可见：[企业财务云升级至企业管理相关操作说明](https://help.aliyun.com/zh/document_detail/451190.html)。
3. 如果您有多家企业需要集中管理，可通过以下3步来实现：每家企业逐一开通企业账号中心；登录账号中心，在“关联企业和组织”目录下，建立企业“运营管理”关系；在账号中心，您可切换关联的企业和组织，管理多家企业组织、账号和权限。

### 常见的已接入折扣隐藏能力的云产品

| **产品线** | **产品名称** |
| --- | --- |
| 弹性计算 | 云服务器ECS(包月)-vm云服务器（按量付费）-ecs云盘-yundisk弹性容器实例 ECI-eci_betav1 |
| 数据库 | RDS只读（包月）-rds_rordspre_public_cn关系型数据库RDS(包月)-rds云数据库 Redis 包年包月（云盘版）-kvstore_prepaid_public_cn云数据库KVStore版（包月）-prepaid_kvstore云数据库KVStore 版（按量付费）-kvstoreRDS只读实例（按量）-rords关系型数据库（按量付费）-bardsRedis日志服务-kvstore_log_public_cn |
| 网络 | 全球加速_基础带宽包（包年包月）-ga_plusbwppre_public_cn高速通道-资源占用费（预付费）-pconn_pre传统型负载均衡CLB（包年包月）-slbpre共享带宽(后付费)-cbwp弹性公网IP（后付费）-eipNAT网关（按量付费）-nat_gw应用型负载均衡(按量付费)-slb_ealb_public_cn传统型负载均衡CLB（按量付费）-slb |
| 存储 | CPFS包年包月-cpfs通用型NAS存储包-naspackage对象存储OSS资源包(包月)-ossbagCPFS（按量付费）-nas_cpfs_post |
| 安全 | DDoS高防（新BGP）-ddoscooDDoS高防（国际）-ddosDipDDoS原生防护-ddosbgp |
| 云原生 | 消息队列 Kafka（包年包月）-alikafka_pre |
| 大数据计算 | 阿里云Elasticsearch(包月)-elasticsearchpre阿里云Elasticsearch（按量付费）-elasticsearch |
| 流量及CDN | 边缘节点服务-ens边缘节点服务（按量付费）-ens_post |
| 服务 | 企业支持计划-supportplan |

## 实施步骤

### 实施准备

- 确保账号已经完成企业认证。
- 确保已经按照[开通指南](https://help.aliyun.com/zh/document_detail/441621.html)，开通了企业账号中心。
- 准备信息完整并加盖公章的[“企业授权书”](https://help.aliyun.com/zh/document_detail/441610.html)以及加盖公章的企业营业执照副本复印件。
- 完成阿里云商务优惠框架合同签订。

### 实施规划

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972411.png)

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：30分钟。

### 操作步骤

#### 多账号优惠同步

目前相同主体下的多账号优惠同步的功能属于高阶配置，需要联系商务经理找销售管理团队申请。配置完成之后，同主体下所有账号都保持相同优惠，后续新创建的同主体账号也会保持相同优惠。

#### 多账号优惠隐藏

1. 确保已经使用企业账号中心搭建了多账号财务管理框架。
2. 配置新的角色或者将折扣查询权限配置到已有角色下。以企业管理员账号进入[企业账号管理中心](https://ea.console.aliyun.com/role-permission/role-list)，创建新的角色（或给已有角色）并添加订单折扣查询权限和退订操作管理权限。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972416.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972417.png)
3. 将角色授权给成员账号UID![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972412.png)

#### 单账号优惠隐藏

1. 自定义折扣查询权限策略。进入[RAM访问控制-权限管理-权限策略](https://ram.console.aliyun.com/policies)，按照以下policy设置权限**类型****配置脚本**禁止询价{"Version": "1","Statement": [{"Effect": "Deny","Action": "bss:QueryPrice","Resource": "*"}]}允许询价{"Version": "1","Statement": [{"Effect": "Allow","Action": "bss:QueryPrice","Resource": "*"}]}
2. 给RAM用户/角色添加：自定义的财务权限策略系统策略AliyunBSSRefundAccess-费用中心退订权限

### 实现效果

#### 1. 下单链路

##### 1.1. 购买下单页面/购物车/续费

对于无折扣查询权限的RAM用户（或企业成员账号），只允许其看到原价、不允许其看到折后价和优惠金额，但不影响其下单。RAM用户（或企业成员账号）确认选配信息并下单后系统会发起自动支付流程。

**购买下单页面：**

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972419.png)

**购物车：**

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972418.png)

**续费：**

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972420.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972421.png)

**询价API：**

如果RAM用户（或企业成员账号）无折扣查询权限，调OpenAPI询价时只返回原价字段、不能查到折后价和优惠金额（或折后价和优惠金额都返回为0）。

##### 1.2. 价格计算器

RAM用户（或企业成员账号）无折扣查询权限时，只能查到原价、不能看到折后价和优惠金额，选配清单导出的excel也只能看到原价、不能看到折后价和优惠金额。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972413.png)

#### 2. 费用与成本中心

对于无折扣查询权限的RAM用户（或企业成员账号），限制其访问费用中心所有跟费用、折扣相关的页面，包括：首页、账单、成本分析、资金、发票、订单等。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972423.png)

#### 3. 退款链路

对于无退款权限的RAM用户（或企业成员账号），限制其操作云资源退订、云资源降配、包年包月转按量付费。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6286581571/p972422.png)

## 故障排除

### 不同主体的优惠是否可以同步？

不可以，只有同一个主体下的多账号可以使用实体优惠同步的能力，各主体账号需要分开申请配置。

### 不同主体账号的折扣隐藏是否可以跨主体操作？

可以。折扣隐藏属于账号权限，同实体的管理账号和集团管理账号均可以对成员账号的折扣隐藏权限进行配置。

### 多账号优惠同步是否可以仅针对部分账号？

如果同实体名下多账号存在不同团队管理的情况，不希望对所有账号进行优惠同步。可以联系商务经理不走实体优惠同步申请，手动将需要优惠同步的账号添加到框架合同中。

## 相关内容

[企业账号中心](https://help.aliyun.com/zh/document_detail/439725.html)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-198（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
