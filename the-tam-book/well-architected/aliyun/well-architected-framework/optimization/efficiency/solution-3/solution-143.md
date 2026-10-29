<!-- source: https://help.aliyun.com/zh/well-architected/solution-143 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929409 -->

# 面向分销场景多账号统一管控方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4986581571/p971728.png)

伙伴在给客户进行项目交付是需要生态伙伴平台APS在流程上的支撑，在生态伙伴平台报备之后才能有效统计服务佣金。但是由于目前生态伙伴平台对于账号存在一些限制，在Landing Zone交付过程中经常会遇到一些问题，比如客户账号搭建了多账号架构之后在生态伙伴平台APS中无法进行项目报备，基于财务托管搭建多账号架构之后无法收到佣金等。

因为在分销场景中涉及到生态伙伴平台的规则：

1. 分销账号无法创建成员账号
2. 伙伴的佣金与分销账号中的消费账单强关联

所以标准的Landing Zone解决方案在资源和财务模块设计上需要进行特殊设计，才能高效完成项目交付。

本文档介绍了一套符合阿里云分销伙伴规则的Landing Zone搭建方案，主要解决资源规划、财务管理搭建过程中的常见问题。

## 方案优势

### 基于分销账号搭建RD子账号

帮助规避生态伙伴平台APS引入的账号生成限制，集中管理APS分销账号，快速搭建符合生态规则的Landing Zone框架。

### 财务关系符合伙伴佣金机制

在新的Landing Zone框架下，规范账号之间的财务关系，确保伙伴能够获得在生态伙伴平台APS中的标准服务佣金。

## 客户场景

### 分销场景下搭建Landing Zone

#### 场景描述

在分销账号中为客户搭建Landing Zone框架经常会遇到一些问题，比如客户账号搭建了多账号架构之后在生态伙伴平台APS中无法进行项目报备、基于财务托管搭建多账号架构之后无法收到佣金等。

#### 适用客户

- 需要进行分销场景交付Landing Zone的伙伴

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4986581571/p971729.png)

### 统一账号来源

在分销场景下，资源目录中所有账号都通过生态伙伴平台APS报备生成的分销账号，通过资源目录RD里面的成员邀请加入到资源目录RD中进行统一管理。由于APS系统限制客户报备上限为5个（突破限制方式参考“注意事项”内容），建议在业务维度进行租户隔离。如需在业务内部进一步隔离，建议通过资源组/VPC方式进行操作。

### 规范财务配置

在分销场景下，所有账号的财务关系保留账号初始化之初的“自主结算”方式，不建议使用Landing Zone的财务管理模块进行配置，财务管理模块会影响分销绩效。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 企业财务 | [企业财务](https://help.aliyun.com/zh/user-center/corporate-finance-overview-1)将多个账号关联到一起，以企业全视角统筹规划云上费用，对关联账号的资金、发票、账单集中化管理，完成费用代付、统一结算、统一发票、统一账单、统一分账、费用分析等业务，并通过用量共享、优惠共享等方式优化企业费用。 | 免费，详情参见[功能介绍](https://help.aliyun.com/zh/user-center/corporate-finance-overview-1)。 |
| 生态伙伴平台APS | [阿里云生态伙伴平台（APS）](https://help.aliyun.com/zh/document_detail/210679.html)是阿里云为生态合作伙伴提供的外部业务平台，旨在支撑阿里云生态伙伴的销售流程作业、阿里云与生态合作伙伴合作的信息沟通和协作以及生态伙伴生命周期管理与服务。合作伙伴可通过该平台进行客户拓展，客户管理，业务销售管理以及项目管理等操作。 |  |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 分销账号 | 生态伙伴通过阿里云生态伙伴平台（APS）关联之后，以客户实体进行企业认证的阿里云账号。 |

## 安全性

### RAM权限

本方案是需要客户在资源管理账号中进行。建议在资源管理账号中开设RAM子用户，并授以下权限：

配置RAM用户的访问权限：

- **授权范围**为**整个云账号**，然后选择权限策略。
- **系统策略**：从**权限策略名称**列表，选择需要的权限。权限策略名称说明AliyunResourceDirectoryFullAccess能够管理资源目录AliyunGovernanceFullAccess能够管理云治理中心

## 注意事项

### 使用限制

#### RD管理多实体账号白名单

目前RD只能管理相同实体的账号，如果需要同时管理一个以上实体的认证账号，请联系SA申请添加RD白名单。

#### 生态伙伴中心同实体账号数限制

目前APS限制伙伴账号uid申请报备相同客户数量存在上限，相同实体最多只能报备5次。如果申请账号数量大于5次，需要在APS系统报备流程中等待APS团队审批。

### 财务限制

由于目前生态伙伴平台存在限制，当前方案中无法对所有账号的财务进行统一管理，无法统一结算、付费、开票和成本分析，需要每个成员账号自行操作财务行为。

## 实施步骤

### 实施准备

#### 设计整体上云框架图

通过与客户的深度沟通，了解客户对于IT方案的预期。基于云治理理念设计符合客户预期的Landing Zone架构图，梳理当前企业需要多少个云账号。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：1小时。

### 操作步骤

1. 报备客户登录APS平台，参考[APS平台登录方式](https://help.aliyun.com/zh/document_detail/210680.html)。点击右上角“报备客户”按钮，进入报备页面。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4986581571/p971740.png)填写客户名称，完成客户报备，若客户已经报备，建议走项目报备流程，详见APS平台引导。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4986581571/p971730.png)报备完成之后，在客户列表中点击“邀请注册”邀请客户注册阿里云账号。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4986581571/p971731.png)客户通过邮件中的注册链接完成分销账号的创建。可以根据方案所需的客户账号数量，不断重复步骤1，确保账号数满足要求。确定1个企业管理账号。
2. 搭建资源管理模块企业管理账号登录[资源目录控制台](https://resourcemanager.console.aliyun.com/resource-directory/)。根据Landing Zone架构图，点击“创建资源夹”创建企业的组织架构。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4986581571/p971733.png)在左侧目录中点击“邀请成员”，填写步骤1中生成的客户账号uid信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4986581571/p971741.png)每个被邀请客户账号登录[资源目录控制台](https://resourcemanager.console.aliyun.com/resource-directory/)，接受管理账号邀请。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4986581571/p971735.png)重新登录企业管理账号，进入资源目录控制台，在“资源组织”页中点击每个用户的“移动”按钮，可以把账号与资源夹根据架构图进行一一映射。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4986581571/p971737.png)
3. 设置财务关系设置财务关系，无须对财务关系进行特殊设置，APS生成账号被邀请之后，默认的财务关系是“自主结算”。

## 故障排除

### 为什么无法开通资源目录？

可能有如下两个原因：

- 当前账号没有进行企业实名认证。关于企业实名认证，请参见[企业实名认证](https://help.aliyun.com/zh/account/verify-your-identity-enterprise-account/)。
- 当前账号已经在资源目录内，无法重复开通。

### 为什么成员账号无法接受资源目录邀请？

检查被邀请账号是否与资源目录管理账号的认证主体是否一致。如果确认是不同的认证主体，需要联系SA在资源目录中添加多实体账号白名单。

### 什么样的账号不适合作为资源目录的管理账号？

- 账号下有待处理的邀请。建议：先处理邀请后再开通资源目录。
- 账号下已经有云资源部署了业务或应用。建议：由于管理账号将承载整个资源目录的架构管理、用户权限管控以及所有资源的付款结算等高权限操作，为了确保管理账号的安全，建议您创建一个新的阿里云账号作为管理账号，避免将已有用途的阿里云账号作为管理账号。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-143（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
