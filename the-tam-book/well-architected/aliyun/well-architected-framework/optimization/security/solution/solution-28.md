<!-- source: https://help.aliyun.com/zh/well-architected/solution-28 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929340 -->

# 多账号主机统一运维方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3376581571/p970873.png)

本文介绍了使用[堡垒机](https://help.aliyun.com/zh/bh/bastionhost/product-overview/what-is-bastionhost)进行多账号主机统一运维方案，可以帮助多账号的企业从统一运维入口管理云主机，满足企业基础运维安全及网络安全等保合规需求，帮助企业更高效灵活的管理服务器资产、用户账号及权限。

## 方案优势

### 运维操作统一入口

管理员可以通过进行导入阿里云ECS实例和导入其他来源主机，在堡垒机中新建需要维护的主机，统一维护资产并进行相应运维操作。

### 稳定的云化架构

堡垒机采用云化架构，一方面避免了单点故障导致运维业务中断，另一方面使用的云服务都具有高稳定性、高成熟度，能更安全地保障系统资源。云化架构的堡垒机更稳定、更灵活、更安全。

### 安全可靠的运维能力

堡垒机能在Windows、Linux系统上稳定高效地运维，在Windows系统上运维不卡顿、不漏审，并且实现了多云、线下IDC、跨VPC等混合云场景下服务器资产的统一管理、集中运维。另外，堡垒机的代码经过商业化封闭包装不易被攻击，运维更稳定、更安全。

### 全球化部署

堡垒机支持在亚太、美洲、欧洲、中东等地区的全球化部署，在海外具有良好的适应性，支持纯英文版界面，支持海外多个国家手机号双因子运维认证，可保障全球范围内资产的安全运维。

### 便捷实用

堡垒机简单、易用、高效，即买即开通，可按需求灵活配置，支持一键启用，支持阿里云账户的ECS、云数据库专属集群主机的一键同步，以及RAM账户、AD账户、LDAP账户的用户一键导入。

## 客户场景

### 多账号主机高效统一管理

#### 场景描述

- 统一入口管理，解决登录分散问题：托管ECS的账号和密码（或SSH密钥）。运维员登录云盾堡垒机再登ECS，无需知道ECS密码。
- 权限细粒度化管理：实现最小权限化，最灵活、精准访问控制。重要资产或命令，可二次申请审批控制。远程办公，区分位置权限细分。

#### 适用客户

需要进行多账号主机统一运维的企业客户。

### 主机运维安全可追溯

#### 场景描述

- 多因子身份鉴别：通过短信认证、动态令牌等技术进行多重身份强认证，防止员工身份被冒用和复用。
- 非法行为阻断：危险命令及时拦截。进行中风险，随时阻断。
- 安全事件需追溯：详细记录操作日志。录播形式全量追溯操作行为。

#### 适用客户

对运维安全性及审计有诉求的企业客户。

## 方案架构

### 部署架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2376581571/p970870.png)

结合多账号架构的最佳实践，架构说明如下：

- 建议将堡垒机放到共享服务账号或运维管理账号，部署到内联运维区的VPC，业务VPC部署到业务账号。账号体系规划详情参见[企业多账号统一架构方案](https://help.aliyun.com/zh/caf/enterprise-multi-account-unified-architecture-solution)，云上网络分区详情参见[云上网络分区](https://help.aliyun.com/zh/caf/uses-cen-instances-and-transit-routers-to-establish-enterprise-grade-network-connections)。
- 通过[云企业网CEN](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)跨账号授权并打通堡垒机所在的VPC与受管控的业务VPC之间的网络。
- 用户可通过堡垒机公网或私网地址登录堡垒机，若用户网络未与云上内网连通，推荐通过[VPN网关](https://help.aliyun.com/zh/vpn/product-overview/what-is-vpn-gateway)连接到云上内网后使用堡垒机私网地址登录以提升安全性。

### 堡垒机配置流程

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3376581571/p970871.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2376581571/p970876.png)

**注意**：主机上面的用户密码需要运维人员在主机上设置，同时堡垒机用户维度授权中的用户名跟密码要保持一致。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 堡垒机 | [堡垒机](https://help.aliyun.com/zh/bh/bastionhost/product-overview/what-is-bastionhost)是阿里云提供的核心系统运维和安全审计的管控平台，可集中管理资产权限，全程管控操作行为，实时还原运维场景，保障云端运维行为身份可鉴别、权限可管控、操作可审计，解决众多资产难管理、运维职责权限不清晰以及运维事件难追溯等问题， 助力企业满足等保合规需求。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/bh/bastionhost/product-overview/pricing/)。 |
| 访问控制RAM | [访问控制RAM（Resource Access Management）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务 | 免费。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |

## 安全性

### 稳定可靠

堡垒机采用云化架构，稳定的云化架构一方面避免了单点故障导致运维业务中断，另一方面使用的云服务都具有高稳定性、高成熟度，能更安全地保障系统资源。云化架构的堡垒机更稳定、更灵活、更安全，详情参见[产品优势](https://help.aliyun.com/zh/bh/bastionhost/product-overview/benefits)。

### 运维安全

堡垒机**基础版**具备基础的运维审计能力，如双因子认证、运维授权、高危命令阻断、运维审计等功能，可满足中小企业的基础运维安全及网络安全等级保护合规需求。**高可用版**适用于对运维业务安全要求较高或业务规模较大的企业，如政企、金融、游戏、在线教育、技术开发等。高可用版除具有基础版的基础运维安全能力外，还可满足更高的业务运维安全需求，详情参见[功能特性](https://help.aliyun.com/zh/bh/bastionhost/product-overview/functions-and-features)。

建议开启堡垒机双因子认证提升安全性，详情参见[开启双因子认证](https://help.aliyun.com/zh/bh/bastionhost/user-guide/enable-two-factor-authentication)。

### 云资源授权

首次使用堡垒机服务前，需要先完成允许堡垒机访问云资源的授权，堡垒机需要访问云服务器ECS和专有网络VPC等云服务的资源，详情参见[授权堡垒机访问云资源](https://help.aliyun.com/zh/bh/bastionhost/user-guide/authorize-bastionhost-to-access-cloud-resources)。

### 操作审计及RAM接入

堡垒机已经接入日志服务、操作审计及访问控制RAM，便于操作合规审计、安全分析及访问控制，详情参见[支持的云服务](https://help.aliyun.com/zh/bh/bastionhost/product-overview/services-that-work-with-bastionhost)。

## 注意事项

### 堡垒机版本

堡垒机分为基础版及高可用版，请根据实际情况进行选择，详情参见[功能特性](https://help.aliyun.com/zh/bh/bastionhost/product-overview/functions-and-features)。

### 服务条款

使用堡垒机前请先了解相应的服务条款，详情参见[堡垒机服务条款](https://help.aliyun.com/zh/bh/bastionhost/support/bastionhost-terms-of-service)。

## 实施步骤

### 实施准备

按照Landing Zone推荐账号架构进行部署，已完成下列部署：

| 账号类型 | 部署内容 |
| --- | --- |
| 共享服务账号/运维账号 | 创建运维VPC及交换机。购买堡垒机。配置CEN，加载网络实例、与业务账号网络连通。 |
| 业务账号 | 开通并创建业务VPC。开通并创建ECS。 |

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：30分钟。

### 操作步骤

#### 启用堡垒机

登录共享服务账号，在[堡垒机控制台](https://yundun.console.aliyun.com/?p=bastion#/overview/)查看已购买的堡垒机，单击**启用，**选择网络及安全组，确认后等待初始化完成。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3376581571/p970877.png)

#### 导入主机

单击堡垒机实例**管理**按钮进入管理页面，在资产管理->主机页面可导入本账号已有ECS。因为跨账号无法在堡垒机控制台加载其他账号内的云主机，需要选择**导入其他来源主机**。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3376581571/p970878.png)

**注意**：其他来源主机对应的网络需要跟堡垒机所在的VPC网络互通。具体如何打通网络连通，请参考[云企业网](https://help.aliyun.com/product/59006.html?spm=5176.21213303.J_6028563670.9.7a153edavuNgMT)。

#### 创建堡垒机用户

管理员在堡垒机上为运维员创建登录堡垒机的账号（即新建用户）后，运维员才可以使用该账号登录堡垒机。在堡垒机实例管理页面选择**用户**菜单，创建**堡垒机用户**。堡垒机支持导入阿里云RAM用户、新建堡垒机本地用户、导入AD用户、导入LDAP认证用户，详情参见[新建用户](https://help.aliyun.com/zh/bh/bastionhost/user-guide/manage-users)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2376581571/p970885.png)

#### 创建主机账户

堡垒机需要使用对应的账户登录到需要进行运维的**目标主机**，本章节介绍如何在堡垒机页面中新增**已有的主机账户**。

**注意：**对应的账户需要事先在运维目标主机中创建出来。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2376581571/p970880.png)

1. 可通过**用户名 + 密码**的方式新增账户。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2376581571/p970891.png)
2. 可通过过**私钥**的方式新增账户。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3376581571/p970892.png)
3. 更多配置，请查看[新建主机账户](https://help.aliyun.com/zh/bh/bastionhost/user-guide/manage-a-host-account)。

#### 用户授权主机

授权主机是将堡垒机中的用户与主机资产进行关联，通过授权主机功能可以达到控制某个用户只能访问自己权限内主机的目的。授权完成后意味着指定某个自然人拥有哪些主机的哪些账户，操作步骤：

1. 在用户详情页面单击**授权主机**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2376581571/p970893.png)
2. 在已授权主机页面单击**授权主机**，选择要授权的主机后单击确定。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2376581571/p970894.png)
3. 在已授权主机列表页单击**授权账户**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2376581571/p970896.png)
4. 选择要授权主机的账户。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3376581571/p970895.png)
5. 更多配置详情参见[按用户授权主机](https://help.aliyun.com/zh/bh/bastionhost/user-guide/authorize-a-user-to-manage-hosts)。

#### 主机运维

通过堡垒机登录主机进行运维操作。操作步骤：

1. 通过命令`ssh xxxx.bastionhost.aliyuncs.com -p60022 -l yourUserName`登录堡垒机。登录链接地址可在堡垒机实例页面查看。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3376581571/p970897.png)
2. 登录成功后选择要登录的目标主机及用户。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2376581571/p970898.png)
3. 登录成功即可在目标主机进行运维操作。
4. 更多运维信息请参见[运维使用手册](https://help.aliyun.com/zh/bh/bastionhost/user-guide/o-and-m-manual-3/)。

#### 更多功能

堡垒机控制策略管理，详情参见[控制策略](https://help.aliyun.com/zh/bh/bastionhost/user-guide/policies/)。

堡垒机审批管理，详情参见[审批命令](https://help.aliyun.com/zh/bh/bastionhost/user-guide/approve-commands)。

堡垒机审计管理，详情参见[审计](https://help.aliyun.com/zh/bh/bastionhost/user-guide/o-and-m-auditing/)。

## 故障排除

### 堡垒机问题

堡垒机常见问题详情参见[售前常见问题](https://help.aliyun.com/zh/bh/faq-1)及[功能使用常见问题](https://help.aliyun.com/zh/document_detail/71375.html)。

## 相关内容

- [堡垒机用户指南](https://help.aliyun.com/zh/bh/bastionhost/user-guide/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-28（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
