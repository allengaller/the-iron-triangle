<!-- source: https://help.aliyun.com/zh/well-architected/solution-19 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929514 -->

# 基于CEN-TR实现企业级云上互联

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973314.png)

随着云计算的普及，越来越多的传统企业客户也在选择把云下的业务系统搬到云上，实现更大的弹性、更强的灵活性、更高的性价比。企业级云上网络的重点是帮助企业用户更高效地搭建上云网络环境，本方案基于[云企业网CEN](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)及[转发路由器TR](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)帮客户实现云上网络架构设计及云上内部网络互通，实现合理的云上网络分区设计、简单的运维管理及灵活的弹性扩展。

## 方案优势

### 弹性可扩展的分区设计

结合企业云上网络分区最佳实践及LandingZone[企业多账号统一架构方案](https://help.aliyun.com/zh/caf/enterprise-multi-account-unified-architecture-solution)，统一描述云上网络分区与账号体系，帮助企业实现合理的分区设计、简单的运维管理及灵活的弹性扩展。

### 全球网络大规模互联

使用[云企业网CEN](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)可帮助客户构建全球化网络，打造一张灵活、可靠、大规模的企业级云上网络。[转发路由器TR](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)联合带宽包能快速连接多个地域的VPC和云下网络，实现全球资源互通。

### 高性能网络互联

[转发路由器TR](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)提供低延迟、高速率的网络传输能力。同地域资源互通最大速率可达到网络设备端口转发速率；全球资源互通，网络整体时延较公网互通时延有很大提升。主备节点自动切换，保障业务不中断。全网任意两个节点之间存在多组高质量传输链路，底层链路中断网络自动收敛，业务无感知。

### 灵活组网

[转发路由器TR](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)支持自定义路由策略，满足企业级组网需求。例如：实现不同安全域隔离、**统一隔离区DMZ（Demilitarized Zone）出口**、搭建安全服务链（Service Chaining）等复杂的组网架构。控制台提供基于地理位置和基于网络资源的可视化管理界面，您可以通过可视化管理界面快速查看同地域和跨地域组网拓扑，帮助您迅速掌握全网运行状态，提高网络运维效率。

## 客户场景

### 企业云上网络分区及互联

#### 场景描述

企业对于云上网络的规划设计、部署使用、运维管理都有自己的要求，并且还可能面临各种各样的特殊业务场景，仅仅具备云产品的初级使用能力已不能满足实际使用需求。业务系统之间需要隔离，但又有部分的数据调用需求，企业需要高效地搭建上云网络环境，并实现合理的分区设计、简单的运维管理及灵活的弹性扩展。

#### 适用客户

需要云上网络分区规划及实现云上网络互联的企业客户。

### 不同业务单元网络路由互通

#### 场景描述

集团型公司，某子公司的业务系统因业务发展需求，需要和其他子公司或集团业务系统路由互通，但又不能影响其与公司内部其他业务系统的正常通信和安全策略。

#### 适用客户

子公司与其他公司跨账号网络互通需求的企业客户。

## 方案架构

### 云上网络分区

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973319.png)

按照使用习惯和业务访问关系，可以分为业务生产区、开发测试区、互联网出口区、东西向安全区、内联运维区、外联网区等。每个分区可以由独立的VPC承载并根据实际情况调整，VPC内按照部署的业务模块选择创建不同的虚拟交换机，不同业务系统之间的互通即不同VPC之间的路由打通。可以使用云企业网CEN及转发路由器快速打通，同时可以按需进行路由表隔离、路由过滤、路由策略设置等，来满足企业用户的个性化需求。

- **业务生产区、开发测试区**：这两个区域分别用于承载客户生产环境和测试环境的资源。
- **互联网出口区**：这个区域类似于线下IDC中的**DMZ区**，用于承载互联网出口资源，如EIP，NAT网关，SLB，云防火墙等资源。
- **东西向安全区**：用来承载东西向防火墙或其他云上IDS/IPS防护设备。
- **内联运维区**：用来承载跳板机、堡垒机等企业内部人员连接云上环境入口的资源。
- **外联网区**：用来承载连接第三方IDC等外部环境的跳板机、堡垒机的入口资源。

### 账号架构及数据互通

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973315.png)

在云上网络分区的基础上进行账号架构设计，结合[企业多账号统一架构方案](https://help.aliyun.com/zh/caf/enterprise-multi-account-unified-architecture-solution)，将云企业网CEN、转发路由器TR、互联网VPC、内联运维VPC等归属于**共享服务账号**，由基础设施团队对该账号进行管理。业务侧的生产、开发测试VPC分别归属于生产、开发测试账号，使用TR跨账号将VPC加载到CEN中实现云上网络互联。

跨公司跨账号的路由互通场景下，可以创建数据互通VPC，采用多VPC的方式，使用TR将数据互通VPC加载到子公司CEN中，同时数据互通VPC跨账号授权给集团公司共享服务账号，使用TR将数据互通VPC加载到集团CEN中，同时实现与集团及子公司的网络路由互通。

方案中的数据互通VPC仅做示例说明，交付实施时互通VPC所属账号请根据实际情况调整。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云企业网CEN | [云企业网CEN（Cloud Enterprise Network）](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)是运行在阿里云私有全球网络上的一张高可用网络。云企业网通过转发路由器TR（Transit Router）帮助您在跨地域专有网络之间，专有网络与本地数据中心间搭建私网通信通道，为您打造一张灵活、可靠、大规模的企业级云上网络。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/cen/product-overview/billing/)。 |
| 转发路由器TR | [转发路由器TR（Transit Router）](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)是地域范围内企业级核心转发网元，可为您转发同地域或不同地域的网络实例间的流量，并支持在地域内定义灵活的互通、隔离、引流策略，帮助您打造一张灵活、可靠、大规模的企业级互联网络。转发路由器实例是云企业网实例的重要组成部分。 | 收费，CEN重要组成部分，参见CEN计费。 |
| 专有网络VPC | [专有网络VPC（Virtual Private Cloud）](https://help.aliyun.com/zh/vpc/what-is-vpc)是您专有的云上私有网络。您可以完全掌控自己的专有网络，例如选择IP地址范围、配置路由表和网关等，您可以在自己定义的专有网络中使用阿里云资源，如云服务器、云数据库RDS和负载均衡等。 | 本身免费，详情参见[产品计费](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |

## 安全性

### CEN服务关联角色

在某些场景下，为了完成云服务的某个功能，需要获取其他云服务的访问权限。通过服务关联角色，您可以更好地创建云服务正常操作所需的权限，避免误操作带来的风险。您在企业版转发路由器中创建专有网络VPC（Virtual Private Cloud）网络实例连接时，系统将会为您自动创建一个名称为AliyunServiceRoleForCEN的服务关联角色，并且为该角色添加名称为AliyunServiceRolePolicyForCEN的权限策略，该权限会允许企业版转发路由器在VPC中创建弹性网卡，作为VPC发往企业版转发路由器的流量入口。权限策略内容详情参见[AliyunServiceRoleForCEN](https://help.aliyun.com/zh/cen/security-and-compliance/aliyunserviceroleforcen)。

### VPC安全性

专有网络VPC具有安全可靠、灵活可控、灵活可用以及较强的可扩展性，详情参见[产品优势](https://help.aliyun.com/zh/vpc/product-overview/benefits)及[访问控制](https://help.aliyun.com/zh/vpc/access-control)。

### 跨账号网络实例授权

在转发路由器实例连接其他账号的网络实例前，需要其他账号的网络实例对转发路由器实例进行授权。授权说明及操作详情参见[跨账号网络实例授权](https://help.aliyun.com/zh/cen/user-guide/grant-permissions-on-a-network-instance-that-belongs-to-another-account)。

## 注意事项

### 转发路由器TR使用限制

在您使用转发路由器产品前，请先了解产品限制，详情参见[使用限制](https://help.aliyun.com/zh/cen/product-overview/limits)。转发路由器分为基础版和企业版，本方案中使用企业版，详细对比参见[转发路由器工作原理](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)。

### VPC使用限制

使用专有网络VPC（Virtual Private Cloud）前，请了解VPC的相关使用限制及提升配额方式。详情参见[限制与配额](https://help.aliyun.com/zh/vpc/understanding-vpc-quotas-in-alibaba-cloud)及[VPC支持的地域信息](https://help.aliyun.com/zh/vpc/regions-that-support-vpc-features)。

### 使用带宽包

要实现跨地域网络实例互通，您必须购买带宽包并创建跨地域连接。同地域网络实例可通过转发路由器直接互通，无需购买带宽包以及创建跨地域连接。详情参见[使用带宽包](https://help.aliyun.com/zh/cen/user-guide/work-with-a-bandwidth-plan)。

### 跨账号网络实例计费

企业版转发路由器连接专有网络VPC（Virtual Private Cloud）实例或边界路由器VBR（Virtual Border Router）实例后会收取网络实例连接费和流量处理费。在网络实例授权时，您可以选择由网络实例所属的账号付费或由企业版转发路由器实例所属的账号付费。详细说明及使用限制详情参见[跨账号网络实例授权](https://help.aliyun.com/zh/cen/user-guide/grant-permissions-on-a-network-instance-that-belongs-to-another-account)。

## 实施步骤

本章节步骤包含**账号1（集团共享服务账号）及账号2（子公司共享服务账号）**内使用CEN及TR进行跨地域网络互通**，账号2数据互通VPC**加入两个账号CEN实现双网络互通。

### 实施准备

- 已拥有2个阿里云账号并已完成企业认证。
- 整体网络规划已完成，开始创建相关产品资源。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：45分钟。

### 操作步骤

#### 云上网络搭建

##### 账号1下创建VPC

1. 构建**测试拓扑**，在[VPC控制台](https://vpc.console.aliyun.com/vpc/)上海和北京分别创建基础服务VPC。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973321.png)
2. 分别在基础服务VPC内创建一个交换机，并各自新增一台ECS，供测试连通性使用。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973316.png)

##### 账号1下创建CEN

1. 在[CEN控制台](https://cen.console.aliyun.com/cen/list)创建**CEN实例**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7676581571/p973317.png)
2. 向创建好的CEN实例中，添加所有**VPC实例**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973322.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973318.png)
3. 当添加网络实例后，系统会在网络实例对应Region自动创建**转发路由器TR**，如下面所示。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973320.png)
4. 构建上海和北京的网络互通需设置**跨地域连接**，这里设置北京-上海的跨地域连接，这里使用测试带宽。实际跨地域连通需要[使用带宽包](https://help.aliyun.com/zh/cen/user-guide/work-with-a-bandwidth-plan)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973324.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973326.png)

**说明1**：此处的配置顺序亦可以反过来，先创建对应region的转发路由器TR，然后再关联对应地域的VPC实例，

**说明2**：VPC实例接入CEN时会在对应地域TR中自动创建一个attach的连接，类型“tr-attach-xxxx”，在attach连接中包含一对主备关系的ENI（系统自动创建在不同可用区），作为VPC发送流量到TR的流量入口。

##### 账号1下网络互通验证

1. 网络互通主要看**路由表**是否正常，如果路由正常，即可相互访问。查看CEN下的路由表（此处选择北京地域的转发路由器TR），是**可用状态**，表示CEN中路由表正常。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973323.png)
2. 查看某个VPC里面的路由表，发现**动态路由**分类里面可以正常看到其他VPC的路由，状态**可用**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973325.png)
3. 也可以在路由表的系统路由中看到自己的路由。可以在这里进行**撤回操作**，撤回后CEN-TR将不再传播此路由给其他网络实例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973327.png)
4. 分别在上海VPC和北京VPC的ECS上相互ping内网地址，查看内网通信是否正常。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973332.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973329.png)

##### 账号2下网络搭建

配置流程和账号1一样，分别创建对应的VPC、CEN，并把VPC加入CEN中，保证账号2内的内网路由互通。

#### 跨账号加载VPC

账号2下创建数据互通VPC并加入CEN实现内网互通，使用跨账号授权功能，将账号2中的数据互通VPC授权给账号1并加载到账号1的CEN中，使用多VPC的方式实现与两个账号的网络都互通。

##### 跨账号授权

1. 在账号2下创建数据互通VPC，并加入CEN，注意网段不要与账号1及账号2下的网段重复。
2. 在账号2的VPC详情页面填入账号1的**UID及云企业网实例ID**，将数据互通VPC跨账号授权给账号1。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973331.png)

##### 跨账号加载VPC

1. 登录账号1，进入对应CEN，选择相应的转发路由器**创建网络实例连接**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973333.png)
2. 选择跨账号，填入账号2的**UID**，将已授权过的数据互通VPC加入CEN。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973328.png)

##### 查看验证

1. 此时可以查看在账号1和账号2的**CEN实例**中，均可以看到**数据互通VPC**（业务孵化VPC），该VPC的资产仍归属账号2，并可以和账号1的VPC进行网络互通。在账号1内查看数据互通VPC，发现他已加入账号1的CEN。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973334.png)
2. 查看到数据互通VPC的**路由信息**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973330.png)
3. 在账号2内查看数据互通VPC, 发现**已加入账号2的CEN**，可以看到对应的TR-attach。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973335.png)
4. 可以在数据互通VPC中创建ECS，测试与账号1、账号2各VPC连通性。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6676581571/p973336.png)

## 故障排除

### CEN常见问题

CEN常见问题详情参见[常见问题](https://help.aliyun.com/zh/cen/support/faq)。

### VPC常见问题

VPC常见问题详情参见[常见问题](https://help.aliyun.com/zh/vpc/support/faq)。

## 相关内容

- [企业多账号统一架构方案](https://help.aliyun.com/zh/caf/enterprise-multi-account-unified-architecture-solution)
- [企业级DMZ上云方案](https://help.aliyun.com/zh/well-architected/solution-113)
- [企业级私网互联方案](https://help.aliyun.com/zh/well-architected/solution-20)
- [云企业网用户指南](https://help.aliyun.com/zh/cen/user-guide/user-guide/)
- [阿里云云采用框架](https://help.aliyun.com/zh/caf/components-of-a-landing-zone-on-alibaba-cloud/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-19（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
