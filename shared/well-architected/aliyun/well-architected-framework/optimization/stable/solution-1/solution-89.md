<!-- source: https://help.aliyun.com/zh/well-architected/solution-89 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929511 -->

# 金融行业企业级云上网络解决方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973268.png)

在公有云商业模式的推出之前，传统金融机构客户构建其IT系统主要是在其线下数据中心部署大量的服务器、交换机、路由器等设备进行物理组网，以此来支持其企业的内部的应用系统以及对外提供的业务系统。近几年，随着越来越多的金融客户逐步选择上云，如何在云上搭建一套金融行业企业级安全管控的网络架构，成为了目前传统金融机构上云面临的核心问题。

本方案从金融行业企业级云上网络分区、云上容灾网络设计、云上DMZ区设计、云上访问流量安全管控设计、构建全球一张网及云上云下混合云组网等场景分别进行阐述**，**便于读者能够全面地了解阿里云网络的能力，协助客户更好地上云。

## 方案优势

### 云上网络全场景覆盖

通过云上网络、全球化网络、混合云网络三大场景能力的构建，满足金融客户对于上云网络全场景业务的覆盖，帮助客户构建全球一张企业内网，让客户上云无后顾之忧。真正实现企业上云、网络先行的价值。

### 满足安全合规强管控

通过安全组、NACL、CEN-TR路由策略及云防火墙等云上网络安全的产品能力，帮忙金融客户上云实现对于业务安全强管控、网络安全合规的云上安全能力构建，保障业务的稳定性和安全性。

### 灵活便捷、简运维

云上网络、安全产品随需开通，能够以较低的TCO成本就能完成云上网络安全的框架构建，同时利用云端统一网络安全的运维监控平台即可完成可视化管理。

## 客户场景

### 云上网络分区

#### 场景描述

企业上云，网络先行。金融客户往往有自己一套非常严格的网络安全管理规则（含网络业务分区、ip地址池资源申报/规划、网络安全访问规则等），以此来合理的规划、管理自己的网络资源。这套规则背后其实是金融客户对于其自身业务的严格安全管控理念，稳定性、合规安全是金融行业的第一大基准。

#### 适用客户

金融行业对于VPC网络基础互联、网络安全域分区、网络安全隔离和访问控制等云上组网有核心诉求的企业客户。

### 网络容灾

#### 场景描述

金融企业对于业务容灾要求非常高，在云上如何利用云网络的能力实现容灾备份是客户业务架构落地的核心能力构建。

#### 适用客户

对网络容灾设计有诉求的金融企业客户。

### 构建云上DMZ区

#### 场景描述

传统金融机构客户在安全、成本、权限、监控等诉求的迭代下，云上公网分布式出口方案逐渐从原来的分布式公网出口演进为统一公网出口。前者适合企业上云初期以及一些非敏感业务，各部门/业务团队可按需使用EIP/NATGW/LB进行各自的公网出口部署，自动度和灵活性较高，同时也带来了企业的云上安全和管理隐患问题；后者则将公网出口进行统一部署、统一管理、统一监控、统一安全策略部署，更能满足金融客户云上的整体安全管控及监管要求。

#### 适用客户

对云上DMZ区设计有诉求的金融企业客户。

### 云上访问流量网络安全管控

#### 场景描述

对于东西向和南北向的网络安全方面，公网出入口的安全审计通过DMZ VPC中的云原生或第三方防火墙实现，云网络架构可以实现将所有进出企业云上网络的公网流量通过统一的云原生或第三方安全设备进行过滤。内网东西向流量的安全防护也可以通过云原生的防火墙实现。

#### 适用客户

对云上访问流量网络安全管控设计有诉求的金融企业客户。

### 全球组网

#### 场景描述

在互联网金融这个细分行业，客户的业务也有显著的特点-全球化。从业务初生，他们就长在云上，而全球化的业务版图让他们对于云网络的全球化能力提出非常多的挑战。

#### 适用客户

对全球组网有设计诉求的金融企业客户。

### 云上云下混合云组网

#### 场景描述

金融客户在云上构建新的业务系统之前，往往具有以下现状：

- 云下已投入较多的IT资源，所以上云后，部分企业会选择将重要系统保留在企业IDC，混合云状态会长期存在。
- 金融企业往往拥有较多的线下分支机构，同时会有和总部办公室、企业IDC之间的内网互通需求，当业务逐步上云后，会涉及到线下分支既需要和线下总部互通，也需要和云上互通。

那如何打造一张覆盖云上云下多地域互联的内部局域网，同时**确保每个分支/总部之间两端之间最短路径互通，解决传统网络绕行问题，是金融客户上云对云供应商云网络能力构建的另外一块强诉求**。

#### 适用客户

对云上云下混合云组网设计有诉求的金融企业客户。

## 方案架构

### 企业级云上网络分区设计

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973270.png)

基于金融行业**对于VPC网络基础互联、网络安全域分区、网络安全隔离和访问控制**等云上组网核心的诉求，我们建议金融行业云上网络分区设计原则整体遵循三个维度，下面将分别进行介绍。

#### 网络分区设计

- 满足业务规模化发展需求，基于VPC为不同业务分区边界的逻辑，合理划分VPC和vSW，做到DMZ、生产、开发测试、运维管理等独立VPC部署。而app、web等不同的生产系统，则是在生产VPC下通过不同的vSW来实现隔离。
- 满足可靠稳定性，建议重要业务系统跨可用区AZ部署。
- 满足业务之间的高效调用和交互，关联业务尽可能部署同Region。

#### 分区间网络互通

- 通过采用云企业网转发路由器CEN-TR，打通阿里云上任意Region开通的业务系统VPC，实现全局一张内网。
- VPC按需加入TR，按需控制不同VPC之间or不同vSW之间的互通关系。
- 可选：统一公网出口强管控需求，可采用多路由表，配置默认路由，将对互联网的访问调流到DMZ区，

#### 云上业务互联安全设计

- 公网出入口配置云防火墙管控进出流量（可搭配云WAF）。
- 跨分区通过云企业网转发路由器CEN-TR搭配阿里云云原生防火墙或三方软件防火墙实现策略管控。
- VPC内基于不同的业务系统可基于VSW/ECS配置相应的NACL或安全组策略，实现微隔离（可搭配云防火墙，实现策略统一管理）。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973271.png)

### 云上同城/异地容灾网络设计

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973272.png)

金融企业对于业务容灾要求非常高，在云上如何利用云网络的能力实现容灾备份是客户业务架构落地的核心能力构建。

- **场景①**利用阿里云LB（7层应用型ALB/4层网络型NLB)构建应用池，解决应用单节点问题，RTO=0
- **场景②**利用将ECS分布在不同可用区，结合SLB/RDS默认已同城容灾，轻松实现整个系统同城容灾，单IDC故障，自动切换，RTO=0
- **场景③**开通灾备资源，通过DTS服务+CEN跨地域带宽实现跨region数据同步，达到两地三中心应用容灾级容灾，切换时只需依次切换RDS和修改域名服务指向即可，RTO分钟级

**业务部署模式：**目前相同的业务应用可以分别部署在阿里云两个城市的四个数据中心中（北京两个机房和上海2个机房）。生产中心和同城灾备中心处于Active模式，应用访问同一数据库实例（数据在两个同城中心各存储一份），异地灾备中心处于Standby模式。

**数据复制方式：**RDS服务实现从北京生产到北京同城灾备，再到上海异地灾备的单向串级数据复制，OSS服务实现从北京生产到北京同城灾备，再到上海异地灾备的单向串级数据复制。

**故障切换回切：**DNS将生产IP从原生产中心修改到灾备中心，实现北京到上海的故障切换和服务恢复机制，主站发生故障时，由备站继续提供服务。

### 云上DMZ区设计

传统金融机构客户在安全、成本、权限、监控等诉求的迭代下，云上公网分布式出口方案逐渐从原来的分布式公网出口演进为统一公网出口。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973274.png)

前者适合企业上云初期以及一些非敏感业务，各部门/业务团队可按需使用EIP/NATGW/LB进行各自的公网出口部署，自动度和灵活性较高，同时也带来了企业的云上安全和管理隐患问题；后者则将公网出口进行统一部署、统一管理、统一监控、统一安全策略部署，更能满足金融客户云上的整体安全管控及监管要求。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973273.png)

本方案着重介绍了传统金融机构DMZ区在云上的设计理念。本方案主要分3个设计场景，默认公网出口、第三方供应商API接口调用的特殊公网出口，以及指定域名访问出口，均部署在统一出口区域DMZ-VPC。

- **默认公网出口在DMZ-VPC内部署增强型NATGW**，并申请“统一网络出口”权限开通跨VPC访问功能DMZ-VPC公网能力，实现统一公网出口。账号-1和账号-2的APP-VPC均可通过DMZ-VPC的默认NATGW的SNAT策略出局访问公网，同时并通过DNAT策略实现跨VPC的公网入口效果。
- **第三方供应商API接口调用的特殊公网出口**在VPC已有默认NATGW的情况下，由于第三方供应商API接口调用时需要双方互相针对IP地址加白名单，且出口独立性较强，不能影响其他业务或被其他业务影响，需于DMZ-VPC再部署一个特殊的NATGW，将三方目标网段路由给此NATGW，实现特殊出口。账号-2 VPC中的ECS访问常规公网时从默认NATGW出口出局，调用第三方供应商API时从特殊公网出口出局。
- **指定域名访问出口**使用LB+EIP（ECS）+ PrivateZone方式实现特殊域名出口，将需要指定出口访问的域名部署在PrivateZone中并应用于本VPC。当业务访问指定域名时，会被PrivateZone自动解析为DMZ-VPC的特殊域名出口的LB私网IP，通过代理的方式从后端服务器的公网出口出局。

同时，当前绝大部分传统金融机构还未完全上云，云上和IDC构建混合云网络的架构也是主流落地场景。**针对混合云架构的阶段**，金融客户也可以考虑将IDC的DMZ区优先部署上云，通过阿里云网络和云安全的能力在云上1：1完成DMZ上云的改造。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973275.png)

### 云上访问流量网络安全管控设计

阿里云网络在国内云厂商中率先提供的路由穿透功能，可以实现将企业网络东西向流量进行统一管控，节省了分布式部署的成本支出，同时大大降低了运维复杂度。对于有特殊合规要求的金融企业，还可以在该网络拓扑中单独构建安全VPC，并在安全VPC中的配置云原生防火墙或构建第三方防火墙实现东西向的流量过滤。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973276.png)

#### 统一互联网出口

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973277.png)

- 业务诉求：云上部署的所有VPC从统一的互联网出口访问Internet，便于集中管控，提高业务安全性。
- 功能实现：多个VPC连接至TransitRouter，业务VPC配置默认路由指向TR。TR配置默认路由指向互联网服务VPC，在互联网服务VPC部署NAT网关、VPN网关、三方IDS/IPS/审计等互联网服务网元。

#### 服务链（东西向管控）

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973279.png)

- 业务诉求：企业内网VPC之间的互访流量经过三方防火墙管控
- 功能实现：企业内网VPC和部署防火墙的VPC都连接至TransitRouter，分别应用TR上不同的路由表转发，实现东西向流量引流至安全管控VPC。

### 构建全球一张网

阿里云网络依托于阿里巴巴全球底层物理传输资源，以云企业网产品为核心，结合高速通道-物理专线、智能接入网关SAG及VPNGW等接入网络，可以帮金融客户快速的构建全球一张企业内网，以便客户迅速地打通部署在阿里云全球各地region的服务，完成业务的全球化。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973280.png)

- **全球跨地域互联：**云企业网CEN打通客户各地域IDC、分支、阿里云各地VPC，快速构建一张稳定、可靠、安全合规、高弹性的私有全球网络。
- **多种技术能力：**物理专线、智能接入网关SAG或VPN网关等多种混合云互联方式，实现一点就近接入。
- **灵活组合：**双物理专线，专线+VPN，专线+SAG方式灵活组合，快速构建一张稳定上云网络。

### 云上云下混合云组网

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973278.png)

金融客户在云上构建新的业务系统之前，往往具有以下现状：

- 云下已投入较多的IT资源，所以上云后，部分企业会选择将重要系统保留在企业IDC，混合云状态会长期存在。
- 金融企业往往拥有较多的线下分支机构，同时会有和总部办公室、企业IDC之间的内网互通需求，当业务逐步上云后，会涉及到线下分支既需要和线下总部互通，也需要和云上互通。

那如何打造一张覆盖云上云下多地域互联的内部局域网，同时**确保每个分支/总部之间两端之间最短路径互通，解决传统网络绕行问题，是金融客户上云对云供应商云网络能力构建的另外一块强诉求**。

阿里云网络按照传统金融机构线下不同组织环境的定位、规模以及与云上系统的关系，推荐如下互通方式：

- 金融企业IDC和总部上云：推荐使用高速通道-物理专线互通。针对传统金融机构，云下IT资源大多分布在两地三中心的多个数据中心机房内，通过物理分区或者逻辑分区隔离不同业务区域之间的网络。此时通过总部/IDC统一采购一组合规运营商大带宽专线，接入到阿里云专线接入点机房。从而和云上环境，构建一条稳定、低时延、高质量的内部专线通道，满足安全合规上的诉求。关于高速通道-物理专线的更多信息，请参见[高速通道-物理专线](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-physical-connection/)。
- 金融线下多分支机构：推荐采用智能接入网关SAG，通过SAG就近加密接入阿里云分布在全球的pop点，打破地域限制，覆盖各种分支形态，形成云上云下一张内网。因为阿里云提供非常多的POP接入点，所以分支机构最后一公里（采用VPN加密通道）的距离会很短，长传全部走阿里云内网传输物理专线，从而保证端到端网络质量仅次于专线，但是价格接近VPN。关于智能接入网关SAG的更多信息，请参见[智能接入网关](https://help.aliyun.com/zh/sag/product-overview/what-is-sag)。
- 特殊分支：针对不方便部署SAG（如偏远分支机构等）、企业想利旧资产等情况。则可以通过本地的VPN网关快速和云上VPN网关实现内网打通。虽然效果不如智能接入网关SAG，但是可以让偏远的分支优先解决内网互通的诉求。关于VPN网关的更多信息，请参见[VPN网关](https://help.aliyun.com/product/65234.html?spm=a2c4g.11186623.6.149.1e3d3477M7w3YN)。

#### 混合云网络互联方案不同接入场景对比

| 方案分类 | 解决方案 | 方案特点 | 典型应用场景 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 质量 | 成本 | 扩展性 | 周期 |  |  |  |
| 单链路 | VPN | 低 | 低 | 好 | 天 | 金融分支机构，移动端上云，且对网络质量要求不高的中小机构 |
| 专线 | 高 | 高 | 差 | 月 | 线下机房上云，追求高可靠 |  |
| SAG | 中 | 中 | 好 | 天 | 金融分支机构上云，同时对网络质量要求较高的中小型分支；线下机房上云，并希望快速部署 |  |
| 主备链路 | 专线 + 专线 | 高 | 高 | 差 | 月 | 线下机房上云，推荐专线 + 专线；业务弹性较大客户，推荐专线 + SAG；成本敏感客户，推荐专线 + VPN。 |
| 专线 + VPN | 中 | 中 | 好 | 月 |  |  |
| 专线 + SAG | 高 | 中 | 好 | 月 |  |  |

#### 金融机构与三方监管机构网络互联

传统金融机构，往往需要与多个三方监管机构互联已完成业务数据的互通/上报，而监管机构为了其安全管控的要求需指定分配金融机构的访问ip地址。该文档即针对如上场景，利用阿里云VPC 私网NAT来实现云上云下地址冲突、监管机构指定通讯ip等挑战，让云上金融客户轻松应对。云上VPC与三方金融监管机构互联场景下，应监管机构网段要求，**存在如下两个需求：**

1. 阿里云侧需支持公网私用地址；
2. 阿里云侧需完成云上VPC源地址转换成监管分配的地址。

**方案整体思路：**对云上VPC网段做个NAT源地址映射，转换成监管提供的地址访问IDC，这样才能满足IDC正常回包给云上，完成通信。具体方案请参见另一篇方案《与三方监管机构网络互联》。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6776581571/p973281.png)

注1：图示箭头业务访问方向

注2：访问节点1为VPC默认系统路由表，访问节点2为NAT所在的子网路由表，访问节点3为VBR路由表

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云企业网 | [云企业网CEN（Cloud Enterprise Network）](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)是运行在阿里云私有全球网络上的一张高可用网络。云企业网通过转发路由器TR（Transit Router）帮助您在跨地域专有网络之间，专有网络与本地数据中心间搭建私网通信通道，为您打造一张灵活、可靠、大规模的企业级云上网络。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/cen/product-overview/billing/)。 |
| 转发路由器TR | [转发路由器TR（Transit Router）](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)提供连接网络实例、添加自定义路由表、添加路由条目、添加路由策略等丰富的网络互通和路由管理功能。本文为您介绍企业版和基础版转发路由器工作原理。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/cen/product-overview/billing/)。 |
| 智能接入网关SAG | [智能接入网关SAG（Smart Access Gateway）](https://help.aliyun.com/zh/sag/product-overview/what-is-sag)是阿里云提供的SD-WAN解决方案。企业可通过智能接入网关实现一站式接入阿里云，获得更加智能、更加可靠和更加安全的上云体验。[云连接网CCN（Cloud Connect Network）](https://help.aliyun.com/zh/sag/user-guide/introduction-to-ccn)是由阿里云分布式接入网关组成的设备接入矩阵，是智能接入网关的另一个重要组成部分。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/sag/product-overview/billing/)。 |
| 高速通道EC | [阿里云高速通道（Express Connect）](https://help.aliyun.com/zh/express-connect/product-overview/what-is-express-connect/)可在本地数据中心IDC（Internet Data Center）和云上专有网络VPC间建立高速、稳定、安全的私网通信。[边界路由器VBR](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-virtual-border-router/)是本地CPE（Customer Premises Equipment）设备和阿里云接入点之间连接的一个路由器，作为数据在本地IDC和阿里云机房之间的转发桥梁。[专线连接](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-physical-connection/)是高速通道提供的一种快速安全连接阿里云与本地数据中心的方法。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/document_detail/48007.html)。 |
| VPN网关 | [VPN网关](https://help.aliyun.com/zh/vpn/product-overview/what-is-vpn-gateway)是一款基于互联网的网络连接服务，通过加密通道的方式实现企业本地数据中心、企业办公网络或互联网终端与阿里云专有网络VPC（Virtual Private Cloud）之间安全可靠的连接。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/pricing/)。 |
| NAT网关 | [阿里云NAT网关（NAT Gateway，简称NAT）](https://help.aliyun.com/zh/nat-gateway/product-overview/what-is-nat-gateway)提供公网NAT和私网NAT两种功能。公网NAT网关通过自定义SNAT、DNAT规则可为云上服务器提供对外公网服务、及主动访问公网能力；私网NAT网关(也即VPC NAT网关)可使VPC内的ECS实例通过私网地址转换服务，实现VPC与VPC之间、及VPC与线下IDC互访能力。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/nat-gateway/pricing/)。 |
| 专有网络VPC | [专有网络VPC（Virtual Private Cloud）](https://help.aliyun.com/zh/vpc/what-is-vpc)是您专有的云上私有网络。您可以完全掌控自己的专有网络，例如选择IP地址范围、配置路由表和网关等，您可以在自己定义的专有网络中使用阿里云资源，如云服务器、云数据库RDS和负载均衡等。 | 本身免费，详情参见[产品计费](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |
| 云防火墙 | [云防火墙](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/product-overview/what-is-cloud-firewall)是一款云平台SaaS（Software as a Service）化的防火墙，可针对您云上网络资产的互联网边界、VPC边界及主机边界实现三位一体的统一安全隔离管控，是您业务上云的第一道网络防线 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/product-overview/billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| DMZ | DMZ（全称Demilitarized Zone，中文为“非军事区”，或称Perimeter network，即“边界网络”、周边网络或“对外网络”）为一种网络架构的布置方案，常用的架设方案是在不信任的外部网络和可信任的内部网络外，创建一个面向外部网络的物理或逻辑子网，该子网能设置用于对外部网络的服务器主机。可以使用在防火墙、路由器等区隔内外网的网络设备。 |

## 安全性

### CEN服务关联角色

在某些场景下，为了完成云服务的某个功能，需要获取其他云服务的访问权限。通过服务关联角色，您可以更好地创建云服务正常操作所需的权限，避免误操作带来的风险。您在企业版转发路由器中创建专有网络VPC，网络实例连接时，系统将会为您自动创建一个名称为AliyunServiceRoleForCEN的服务关联角色，并且为该角色添加名称为AliyunServiceRolePolicyForCEN的权限策略，该权限会允许企业版转发路由器在VPC中创建弹性网卡，作为VPC发往企业版转发路由器的流量入口。权限策略内容详情参见[AliyunServiceRoleForCEN](https://help.aliyun.com/zh/cen/security-and-compliance/aliyunserviceroleforcen)。

### VPC安全性

专有网络VPC具有安全可靠、灵活可控、灵活可用以及较强的可扩展性，详情参见[产品优势](https://help.aliyun.com/zh/vpc/product-overview/benefits)及[访问控制](https://help.aliyun.com/zh/vpc/access-control)。

### SAG安全性

智能接入网关SAG支持加密认证，详情参见[产品优势](https://help.aliyun.com/zh/sag/product-overview/benefits)。

### 跨账号网络实例授权

在转发路由器实例连接其他账号的网络实例前，需要其他账号的网络实例对转发路由器实例进行授权。授权说明及操作详情参见[跨账号网络实例授权](https://help.aliyun.com/zh/cen/user-guide/grant-permissions-on-a-network-instance-that-belongs-to-another-account)。

## 注意事项

### VPC使用限制

使用专有网络VPC（Virtual Private Cloud）前，请了解VPC的相关使用限制及提升配额方式。详情参见[限制与配额](https://help.aliyun.com/zh/vpc/understanding-vpc-quotas-in-alibaba-cloud)及[VPC支持的地域信息](https://help.aliyun.com/zh/vpc/regions-that-support-vpc-features)。

### 高速通道使用限制

高速通道使用限制相关详情参见[使用限制](https://help.aliyun.com/zh/express-connect/product-overview/limits)。

### SAG使用

智能接入网关SAG使用限制详情参见[使用限制](https://help.aliyun.com/zh/sag/product-overview/limits)。智能接入网关支持直挂、旁挂模式，直挂模式下您本地分支或机构的所有流量均通过智能接入网关进行传输，旁挂模式下可以通过智能接入网关传递您的私网流量，去往公网的流量仍可通过您的出口设备进行传输，部署模式介绍参见[部署模式](https://help.aliyun.com/zh/sag/product-overview/deployment-modes)。需要**高可用**时可以将两台智能接入网关设备部署在您的网络中并开启设备的高可用功能，详情参见[高可用拓扑](https://help.aliyun.com/zh/sag/product-overview/ha-topology)。

### VPN网关使用限制

VPN网关使用限制详情参见[使用限制](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/product-overview/limits-for-ipsec-vpn)。

### 转发路由器TR使用限制

在您使用转发路由器产品前，请先了解产品限制，详情参见[使用限制](https://help.aliyun.com/zh/cen/product-overview/limits)。转发路由器分为基础版和企业版，本方案中使用企业版，详细对比参见[转发路由器工作原理](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)。

### 使用带宽包

要实现跨地域网络实例互通，您必须购买带宽包并创建跨地域连接。同地域网络实例可通过转发路由器直接互通，无需购买带宽包以及创建跨地域连接。详情参见[使用带宽包](https://help.aliyun.com/zh/cen/user-guide/work-with-a-bandwidth-plan)。

### 跨账号网络实例计费

企业版转发路由器连接专有网络VPC实例或边界路由器VBR实例后会收取网络实例连接费和流量处理费。在网络实例授权时，您可以选择由网络实例所属的账号付费或由企业版转发路由器实例所属的账号付费。详细说明及使用限制详情参见[跨账号网络实例授权](https://help.aliyun.com/zh/cen/user-guide/grant-permissions-on-a-network-instance-that-belongs-to-another-account)。

## 实施步骤

### 实施准备

- 申请阿里云账号、完成[企业实名认证](https://help.aliyun.com/zh/account/verify-your-identity-enterprise-account/)。
- 了解阿里云网络相关产品，可重点参考产品费用及名词章节。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：大于6小时。

### 操作步骤

当前金融客户在上云的过程中主要分以下三个阶段，结合三个阶段对于不同场景产品能力的依赖，调整落地路径如下：

#### 第一阶段：云上核心系统的网络架构构建

| 场景说明 | 落地实施方案 |
| --- | --- |
| 金融行业企业级云上网络分区 | 请参考《[基于CEN-TR实现企业级云上互联](https://help.aliyun.com/zh/well-architected/solution-19)》 |
| 金融企业云上容灾网络设计 |  |
| 构建全球一张网 |  |
| 云上DMZ区设计 | 请参考《[企业级DMZ上云方案](https://help.aliyun.com/zh/well-architected/solution-113)》 |

#### 第二阶段：云上云下混合云网络统一化管理

| 场景说明 | 落地实施方案 |
| --- | --- |
| 云上云下混合云组网 | 请参考《[混合云组网方案](https://help.aliyun.com/zh/well-architected/solution-23)》 |
| 金融机构与三方监管机构互联 | 请参考《[与三方监管机构网络互联方案](https://help.aliyun.com/zh/well-architected/solution-93)》 |

#### 第三阶段：云上网络安全强管控构建

| 场景说明 | 落地实施方案 |
| --- | --- |
| 云上访问流量网络安全管控设计 | 请参考《[转发路由器TR结合云防火墙部署的最佳实践](https://help.aliyun.com/zh/well-architected/solution-90)》 |

## 源代码

- 代码地址：[GitHub代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/automation/finance-industry)。
- 代码说明：代码中包含云上组网部分搭建实施内容，如CEN-TR组网、DMZ区、统一公网出口等，请查看finance/step/network-xxx文件夹。

## 相关内容

- [阿里云云采用框架CAF](https://help.aliyun.com/zh/caf/network-planning)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-89（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
