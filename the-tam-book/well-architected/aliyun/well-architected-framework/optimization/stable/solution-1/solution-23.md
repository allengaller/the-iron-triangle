<!-- source: https://help.aliyun.com/zh/well-architected/solution-23 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929512 -->

# 混合云组网方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4876581571/p973282.png)

随着云计算的普及，越来越多的传统企业客户也在选择把云下的业务系统搬到云上，实现更大的弹性、更强的灵活性、更高的性价比。上云后企业通常需要云上云下互通混合组网，云上连通云下IDC、分支机构等，本方案使用[云企业网](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)将[高速通道](https://help.aliyun.com/zh/express-connect/product-overview/what-is-express-connect/)物理专线、[智能接入网关SAG](https://help.aliyun.com/zh/sag/product-overview/what-is-sag)、[VPN网关](https://help.aliyun.com/zh/vpn/product-overview/what-is-vpn-gateway)及[VPC](https://help.aliyun.com/zh/vpc/what-is-vpc)进行连接，帮助企业构建一张灵活、可靠、大规模的企业级混合云网络，实现企业内网多地域互联。

## 方案优势

### 全球网络大规模互联

使用[云企业网CEN](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)可帮助客户构建全球化网络，打造一张灵活、可靠、大规模的企业级云上网络。[转发路由器TR](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)联合带宽包能快速连接多个地域的VPC和云下网络，实现全球资源互通。

### 高性能互通

[转发路由器TR](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)提供低延迟、高速率的网络传输能力。同地域资源互通最大速率可达到网络设备端口转发速率；全球资源互通，网络整体时延较公网互通时延有很大提升。

[高速通道](https://help.aliyun.com/zh/express-connect/product-overview/what-is-express-connect/)依靠阿里云的网络虚拟化技术，可以将不同网络环境连通，物理专线两端直接进行高速内网通信，不需要经过公网。在物理专线两端距离很远的情况下，高速通道仍可以提供低时延、低丢包率和高带宽的内网级通信质量。

### 稳定安全

阿里云[高速通道](https://help.aliyun.com/zh/express-connect/product-overview/what-is-express-connect/)产品依托阿里云优质基础设施实现，保障您网络间的通信稳定可靠。高速通道在网络虚拟化层进行网络间通信，多租户互相隔离，避免您的私密数据在传输过程中被窃取。

[智能接入网关SAG](https://help.aliyun.com/zh/sag/product-overview/what-is-sag)城域内Internet就近接入，可通过设备及链路级主备方式实现线下多机构可靠上云，混合云私网加密互连，Internet传输过程中加密认证，支持数据加密、防重放、防篡改。

### 灵活组网

[转发路由器TR](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)支持自定义路由策略，满足企业级组网需求。控制台提供基于地理位置和基于网络资源的可视化管理界面，您可以通过可视化管理界面快速查看同地域和跨地域组网拓扑，帮助您迅速掌握全网运行状态，提高网络运维效率。

## 客户场景

### 云上云下网络互通

#### 场景描述

企业用户通常会选择先把前置系统优先上云，部分业务系统仍放在云下，一方面需要过渡，另一方面利使用云下已投入的IT资源。业务搬站或系统迁移上云过程中，需要有大带宽、稳定、安全的网络通道，混合云状态会长期存在。

#### 适用客户

云下IDC、企业分支、其它特殊分支等需要与云上互联混合组网的企业客户。

## 方案架构

### 整体架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4876581571/p973283.png)

按照云下网络环境的定位、规模和与云上系统的关系，推荐不同的与云上互通方式：

- I**DC和大型企业总部**：推荐使用高速通道**专线互通，**专线在云端使用边界路由器[VBR](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-virtual-border-router/)与转发路由器TR连接，接入云企业网CEN从而和云上内网打通。高速通道可在本地数据中心IDC和云上网络间建立高速、稳定、安全的私网通信。高速通道的物理专线数据传输过程可信可控，避免网络质量不稳定问题，同时可避免数据在传输过程中被窃取。
- **企业分支和小型总部**：推荐采用**智能接入网关SAG**，SAG在云端使用[云连接网CCN](https://help.aliyun.com/zh/sag/user-guide/introduction-to-ccn)与转发路由器TR连接，接入云企业网CEN从而和云上内网打通。通过SAG就近入云，打破地域限制，覆盖各种分支形态，形成云上云下一张内网。阿里云提供非常多的POP接入点，所以分支最后一公里（走VPN加密通道）的距离会很短，长传全部走阿里云内网，端到端网络质量仅此于专线。
- **特殊分支**：针对不方便部署SAG（如海外偏远分支等）、企业想利旧资产等情况，通过IPsec连接**VPN网关，**VPN网关所在的VPC与转发路由器TR连接，接入云企业网CEN从而和云上内网打通。虽然效果不如智能接入网关SAG，但可以让偏远的分支解决内网互通诉求。

### 账号划分及网络分区

CEN、VBR、CCN、VPN所在VPC等企业共享的基础架构资源推荐放到共享服务账号，由基础设施团队统一管理。业务侧VPC放到相应业务的生产、开发测试等业务账号中，通过跨账号授权给共享服务账号后加载到CEN中，账号架构详情参见[企业多账号统一架构方案](https://help.aliyun.com/zh/caf/enterprise-multi-account-unified-architecture-solution)。

VBR、CCN、VPN所在VPC在本方案中用于企业内部互联，在推荐的网络分区中属于内联运维区，业务侧VPC在网络分区中属于业务生产区、开发测试区，云上网络分区更多介绍参见[基于CEN-TR实现企业级云上互联](https://help.aliyun.com/zh/well-architected/solution-19)。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云企业网CEN | [云企业网CEN（Cloud Enterprise Network）](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)是运行在阿里云私有全球网络上的一张高可用网络。云企业网通过转发路由器TR（Transit Router）帮助您在跨地域专有网络之间，专有网络与本地数据中心间搭建私网通信通道，为您打造一张灵活、可靠、大规模的企业级云上网络。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/cen/product-overview/billing/)。 |
| 转发路由器TR | [转发路由器TR（Transit Router）](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)是地域范围内企业级核心转发网元，可为您转发同地域或不同地域的网络实例间的流量，并支持在地域内定义灵活的互通、隔离、引流策略，帮助您打造一张灵活、可靠、大规模的企业级互联网络。转发路由器实例是云企业网实例的重要组成部分。 | 收费，CEN重要组成部分，详情参见CEN计费。 |
| 智能接入网关SAG | [智能接入网关SAG（Smart Access Gateway）](https://help.aliyun.com/zh/sag/product-overview/what-is-sag)是阿里云提供的SD-WAN解决方案。企业可通过智能接入网关实现一站式接入阿里云，获得更加智能、更加可靠和更加安全的上云体验。[云连接网CCN（Cloud Connect Network）](https://help.aliyun.com/zh/sag/user-guide/introduction-to-ccn)是由阿里云分布式接入网关组成的设备接入矩阵，是智能接入网关的另一个重要组成部分。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/sag/product-overview/billing/)。 |
| 高速通道 | [阿里云高速通道（Express Connect）](https://help.aliyun.com/zh/express-connect/product-overview/what-is-express-connect/)可在本地数据中心IDC（Internet Data Center）和云上专有网络VPC间建立高速、稳定、安全的私网通信。[边界路由器VBR](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-virtual-border-router/)是本地CPE（Customer Premises Equipment）设备和阿里云接入点之间连接的一个路由器，作为数据在本地IDC和阿里云机房之间的转发桥梁。[专线连接](https://help.aliyun.com/zh/express-connect/user-guide/what-is-a-physical-connection/)是高速通道提供的一种快速安全连接阿里云与本地数据中心的方法。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/document_detail/48007.html)。 |
| VPN网关 | [VPN网关](https://help.aliyun.com/zh/vpn/product-overview/what-is-vpn-gateway)是一款基于互联网的网络连接服务，通过加密通道的方式实现企业本地数据中心、企业办公网络或互联网终端与阿里云专有网络VPC（Virtual Private Cloud）之间安全可靠的连接。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/pricing/)。 |
| 专有网络VPC | [专有网络VPC（Virtual Private Cloud）](https://help.aliyun.com/zh/vpc/what-is-vpc)是您专有的云上私有网络。您可以完全掌控自己的专有网络，例如选择IP地址范围、配置路由表和网关等，您可以在自己定义的专有网络中使用阿里云资源，如云服务器、云数据库RDS和负载均衡等。 | 本身免费，详情参见[产品计费](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |

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

#### 网络拓扑介绍

本文以如下网络拓扑为例：

- 在北京部署云下IDC服务，广州和杭州为分支机构。
- 在云上部署VPC包括上海业务VPC1、杭州内联VPC。
- 北京IDC通过专线接入到阿里云接入点，并将对应的边界路由器VBR加载到云企业网内。
- 杭州分支机构通过VPN网关连接到杭州VPC。
- 广州分支机构通过智能接入网关上云，并将智能接入网关所属的云连接网CCN加载到云企业网内。
- 上海、杭州VPC加载到云企业网内。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4876581571/p973285.png)

#### 账号划分

账号要求及划分情况：

- 须已拥有2个阿里云账号并已完成企业认证。
- CEN、VBR、CCN、杭州内联VPC在**账号1（共享服务账号）**中，上海业务VPC在**账号2（业务账号）**中，账号1的杭州内联VPC跨账号授权给账号2，在账号2中将上海、杭州的VPC加载到云企业网内。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：大于6小时。

### 操作步骤

#### 云上网络搭建

1. 登录账号1的[VPC控制台](https://vpc.console.aliyun.com/vpc/)，创建杭州内联VPC。
2. 在[CEN控制台](https://cen.console.aliyun.com/cen/list)创建**CEN实例**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4876581571/p973286.png)
3. 在弹出页面中选择**创建网络实例连接，**将杭州内联VPC加载到CEN中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4876581571/p973284.png)
4. 登录账号2的[VPC控制台](https://vpc.console.aliyun.com/vpc/)，创建**上海业务VPC**。
5. 在VPC详情页面填入账号1的**UID及云企业网实例ID**，将业务VPC跨账号授权给账号1。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4876581571/p973287.png)
6. 登录账号1的[CEN控制台](https://cen.console.aliyun.com/cen/list)，在CEN实例详情中选择**创建转发路由器**，在上海地域完成转发路由器创建。
7. 在上海转发路由器详情页创建网络实例连接，选择**跨账号**并填入**账号2的UID**，选择上海业务VPC实例后完成连接创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4876581571/p973288.png)
8. 构建跨地域的网络互通需设置**跨地域连接**，新建广州、北京的转发路由器，并设置杭州、上海、广州、北京之间的跨地域连接，这里使用测试带宽，实际跨地域连通需要[使用带宽包](https://help.aliyun.com/zh/cen/user-guide/work-with-a-bandwidth-plan)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4876581571/p973289.png)

#### VPN接入

杭州分支机构使用IPsec连接到杭州内联VPC的VPN网关，通过杭州内联VPC接入云企业网。

##### 前提条件

- 杭州分支机构的网关设备支持IKEv1和IKEv2协议。
- 杭州分支机构的网关设备已经配置了静态公网IP。
- 杭州分支机构和VPC互通的网段没有重叠。

##### 创建VPN网关

1. 登录[VPN网关管理控制台](https://vpc.console.aliyun.com/vpn)。
2. 在**VPN网关**页面，单击**创建VPN网关**。
3. 在购买页面，根据以下信息配置VPN网关，然后单击**立即购买**并完成支付。**实例名称**：输入VPN网关的实例名称。**地域和可用区**：选择VPN网关所属的杭州地域。**网关类型**：选择要创建的VPN网关类型。本示例选择**普通型**。**VPC**：选择要连接的杭州内联VPC。**指定交换机**：是否指定VPN网关创建在VPC中的某一个交换机下。本示例选择**否**。如果您选择了**是**，您还需要指定具体的**虚拟交换机**。**带宽规格**：选择VPN网关的公网带宽峰值。单位为Mbps。**IPsec-VPN**：选择是否开启IPsec-VPN功能。本示例选择**开启**。**SSL-VPN**：选择是否开启SSL-VPN功能。本示例选择**关闭**。**计费周期**：选择购买时长。关于计费的更多信息， 请参见[计费说明](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/billing-rules-for-ipsec-vpn)。
4. 返回VPN网关页面，查看创建的VPN网关。刚创建好的VPN网关的状态是**准备中**，约1~5分钟左右会变成**正常**状态。**正常**状态表明VPN网关已经完成了初始化，可以正常使用。

##### 创建用户网关

1. 在左侧导航栏，选择**网间互联 > VPN > 用户网关**。
2. 在顶部菜单栏，选择用户网关的地域。**说明** 用户网关的地域必须和要连接的VPN网关的地域相同。
3. 在**用户网关**页面，单击**创建用户网关**。
4. 在**创建用户网关**面板，根据以下信息配置用户网关，然后单击**确定**。更多参数信息，请参见[创建用户网关](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/user-guide/customer-gateway)。**名称**：输入用户网关的名称。**IP地址**：输入VPC要连接的本地网关设备的公网IP。本示例输入211.XX.XX.68。**描述**：输入用户网关的描述信息。

##### 创建IPsec连接

1. 在左侧导航栏，选择**网间互联 > VPN > IPsec连接**。
2. 在顶部菜单栏，选择IPsec连接实例的地域。**说明** IPsec连接实例的地域必须和要连接的VPN网关的地域相同。
3. 在**IPsec连接**页面，单击**创建IPsec连接**。
4. 在**创建IPsec连接**页面，根据以下信息配置IPsec连接，然后单击**确定**。其他选项使用默认配置。更多信息，请参见[创建IPsec连接](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/user-guide/create-and-manage-ipsec-vpn-connections-in-single-tunnel-mode)。**名称**：输入IPsec连接的名称。**VPN网关**：选择已创建的VPN网关。**用户网关**：选择已创建的用户网关。**路由模式**：选择路由模式。本示例选择**目的路由模式**。**立即生效**：选择是否立即生效。本示例选择**否**。**是**：配置完成后立即进行协商。**否**：当有流量进入时进行协商。**预共享密钥**：输入共享密钥。建立IPsec连接需保证该值与本地网关设备的预共享密钥一致。如果不输入该值，系统默认生成一个16位的随机字符串。

##### 在本地网关设备中加载VPN配置

1. 在左侧导航栏，选择**网间互联 > VPN > IPsec连接**。
2. 在**IPsec连接**页面，找到目标IPsec连接实例，然后在**操作**列下选择**> 下载对端配置**。
3. 根据本地网关设备的配置要求，将下载的配置添加到本地网关设备中。具体操作，请参见[本地网关配置](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/configure-an-h3c-firewall-device)。

##### 配置VPN网关路由

1. 在左侧导航栏，选择**网间互联 > VPN > VPN网关**。
2. 在**VPN网关**页面，找到目标VPN网关实例，单击实例ID。
3. 在**目的路由表**页签，单击**添加路由条目**。
4. 在**添加路由条目**面板，根据以下信息配置目的路由，然后单击**确定**。**目标网段**：输入杭州分支机构的私网网段。本示例输入**10.1.1.0/24**。**下一跳类型**：选择**IPsec连接**。**下一跳**：选择IPsec连接实例。**发布到VPC**：选择是否将新添加的路由发布到VPC路由表。本示例选择**是**。**权重**：选择路由的权重值。本示例选择**100**。**说明** 相同目标网段的目的路由，不支持同时设置权重值为100。**100**：高优先级。**0**：低优先级。

##### 测试连通性

可以在杭州内联VPC内创建一台无公网IP的ECS，通过**ping**命令，测试与杭州分支结构一台服务器的连通性。

#### 专线接入

通过专线将北京IDC与云企业网进行连接，专线接入与CEN连通操作步骤详情参见[本地IDC通过专线访问云服务器ECS](https://help.aliyun.com/zh/express-connect/use-cases/connect-a-data-center-to-ecs-by-using-an-express-connect-circuit)。

##### 创建专线连接

可以通过高速通道控制台自主创建专线连接（独享端口方式）或通过合作伙伴共享专线方式创建专线连接。具体操作，请参见[创建独享专线连接](https://help.aliyun.com/zh/express-connect/user-guide/classic-mode)或[创建共享专线连接](https://help.aliyun.com/zh/express-connect/user-guide/overview-of-hosted-connections/)。

本文中，和专线连接的云上网关设备VBR的配置如下表所示。

| **VBR配置项** | **配置详情** |
| --- | --- |
| **VLAN ID** | 0 |
| **阿里云侧IPv4互联IP** | 10.0.0.1 |
| **客户侧IPv4互联IP** | 10.0.0.2 |
| **IPv4子网掩码** | 255.255.255.252 |

##### 在CEN加载VBR实例

1. 登录账号1[云企业网管理控制台](https://cen.console.aliyun.com/)。
2. 在**云企业网实例**页面，单击CEN实例ID。
3. 在**网络实例管理**页签，单击**加载网络实例**，加载与专线关联的VBR，然后单击**确定**。**实例类型**：选择**边界路由器（VBR）**。**地域**：选择VBR所属的北京地域。**网络实例**：选择专线关联的VBR。

##### 配置VBR路由

您需要在VBR上分别配置指向本地IDC和物理专线接口的路由。本文以在VBR上配置指向物理专线接口路由为示例。

1. 登录账号1[高速通道管理控制台](https://expressconnectnext.console.aliyun.com/)。
2. 在顶部菜单栏，选择VBR所属地域，然后在左侧导航栏，单击**边界路由器（VBR）**。
3. 在**边界路由器（VBR）**页面，单击目标边界路由器的ID。
4. 在边界路由器详情页面，单击**路由条目**页签，然后单击**添加路由条目**。
5. 在**添加路由条目**面板，根据以下信息配置路由条目，然后单击**确定**。**说明** 默认情况下，阿里云上的ECS实例无法**ping**通VBR的IP地址。如需进行ping测试，您需要添加指向物理专线接口的路由，其中使用VBR的互联IP地址段10.0.0.1/30作为本地IDC的网段。**下一跳类型**：选择**物理专线接口**。**目标网段**：输入本地IDC的网段，本示例输入10.1.3.0/24。**下一跳**：选择要自主申请的物理专线。

##### 配置健康检查

可以通过CEN的健康检查功能监测本地IDC的网络状况，详情参见[健康检查](https://help.aliyun.com/zh/cen/user-guide/configure-health-checks-1)。

##### 配置本地IDC的路由

至此，已完成阿里云上的路由配置，您还需要在专线接入设备上配置指向VPC的路由。您可以选择配置静态路由或配置BGP路由将本地IDC的数据转发至VBR。

1. 本地网关设备配置到云上VPC的路由。配置静态路由示例：`ip route 192.168.3.0 255.255.255.0 10.0.0.1`配置BGP动态路由具体操作，请参见[配置BGP](https://help.aliyun.com/zh/express-connect/user-guide/configure-and-manage-bgp)。宣告网段为需要和本地IDC通信的VPC的网段。
2. 本地网关设备**ping**云上VBR，测试连通性。执行**ping**命令，**ping 10.0.0.1**，如果能ping通，表示本地网关到云上的专线连接成功。
3. 执行如下命令，在本地IDC的服务器添加默认路由指向本地网关。`route add default gw 10.1.3.1`

##### 测试专线连通性

您可以通过ping云上VBR实例的IP地址，测试本地IDC到云上专线的通信是否正常。

1. 打开本地IDC服务器的命令行窗口。
2. 执行**ping**命令，ping云上VBR **10.0.0.1**，如果能ping通，表示本地服务器到云上的专线连接成功。**说明** ECS无法**ping**通VBR互联地址。

##### 测试ECS连通性

可以在上海VPC内创建ECS，在本地IDC通过ping云上ECS实例的IP地址，测试云上和本地IDC的通信是否正常。

**说明** 在您执行以下步骤前，请先了解您VPC中的ECS实例所应用的安全组规则，确保安全组规则允许本地IDC访问VPC中的ECS实例。具体操作，请参见[查询安全组规则](https://help.aliyun.com/zh/ecs/user-guide/view-security-group-rules)。

1. 打开本地IDC的服务器的命令行窗口执行测试：`ping 192.168.3.11`。
2. 登录阿里云ECS实例并打开命令行窗口。
3. 执行**ping**命令，ping本地IDC服务器的IP地址。如果能ping通，表示通过高速通道云下服务器到云上ECS已经连接成功：`ping 10.1.3.22`。

#### SAG接入

通过智能接入网关SAG将广州分支机构与CEN连通。单机直挂、单机旁挂静态（动态）路由、双机直挂静态（动态）路由、双机旁挂动态路由等部署方式具体操作步骤详情参见SAG操作[教程](https://help.aliyun.com/zh/sag/use-cases/)。

以下操作步骤采用单机旁挂静态路由的部署方式，**仅做示例**，详细操作步骤参见[单机旁挂静态路由上云](https://help.aliyun.com/zh/sag/use-cases/deploy-an-sag-device-in-one-arm-mode-and-enable-static-routing)。

##### 购买智能接入网关设备

在智能接入网关控制台购买智能接入网关设备后，阿里云会将智能接入网关设备寄送给您，并创建一个智能接入网关实例方便您管理设备。

**说明** 如果您要使用智能接入网关的区域非中国内地时，您需要通过第三方公司购买硬件，详情请参见[购买SAG硬件](https://help.aliyun.com/zh/sag/user-guide/purchase-an-sag-device)。

1. 登录[智能接入网关管理控制台](https://smartag.console.aliyun.com/)。
2. 在**智能接入网关**页面，单击**购买智能接入网关**。
3. 选择**创建智能接入网关（硬件版）**。
4. 根据以下信息配置智能接入网关设备信息，然后单击**立即购买**。**区域**：智能接入网关设备使用区域。本示例选择**中国内地**。**实例类型**：选择智能接入网关设备规格。本示例选择**SAG-1000**。**已有SAG硬件**：选择是否已有智能接入网关硬件设备。本示例选择**否**。**版本**：智能接入网关设备版本。本示例使用默认**标准版**。**购买数量**：智能接入网关设备购买数量。本示例选择**1**。**区域**：智能接入网关设备使用的带宽区域。该区域类型和智能接入网关设备使用区域保持一致，且无法修改。**实例名称**：智能接入网关实例名称。名称长度为2~128个字符，以大小写字母或中文开头，可包含数字、英文句点（.）、连接号（-）和下划线（_）。**带宽峰值**：选择通信网络的带宽峰值。本示例选择**50 Mbps**。**购买时长**：选择购买时长。
5. 确认订单信息，然后单击**确认购买**。
6. 在弹出的**收货地址**对话框，填写网关设备的收货地址，然后单击**立即购买**。
7. 在弹出的**支付**页面，选择支付方式，然后完成支付。

您可以在智能接入网关实例页面查看是否下单成功。系统会在下单后两个工作日内发货。如果超期，您可以[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex?spm=a2c8b.12571063.console-base-top.dwork-order-1.6c3a5675P2NEW9)查看物流状态。

##### 激活连接智能接入网关设备

收到智能接入网关设备后，请检查设备配件是否完整，详情请参见[SAG-1000设备说明](https://help.aliyun.com/zh/sag/user-guide/sag-1000-device-specifications)。

1. 登录[智能接入网关管理控制台](https://smartag.console.aliyun.com/)。
2. 在顶部菜单栏，选择目标区域。
3. 在**智能接入网关**页面，找到目标实例。
4. 单击目标实例**操作**列下的**激活**。
5. 在**激活**对话框，单击**确定**。
6. 激活设备后，您还需要将智能接入网关设备按照拓扑所示接入到本地机构中。通过网线，将智能接入网关设备的WAN（端口5）连接到三层交换机的G11端口上。
7. **可选：**如果您通过第三方公司购买的设备，需手动将设备与智能接入网关实例进行绑定。详情请参见[添加设备](https://help.aliyun.com/zh/sag/user-guide/add-a-device)。

##### 配置智能接入网关设备

连接好设备后，您可以在智能接入网关管理控制台对设备进行端口配置和路由配置。

在执行此操作前，请保持设备启动且4G信号正常，已经连接到阿里云。

1. 端口配置。在**智能接入网关**页面，单击目标实例ID链接。在智能接入网关实例详情页面，单击**设备管理**页签。在页签左侧区域，单击**WAN口管理**。在**WAN（端口5）**区域，单击**编辑**。在**WAN（端口5）配置**页面，根据以下信息配置端口，然后单击**确定**。**连接类型**：选择**静态IP**。**优先级**：采用默认值**1**。**IP地址**：WAN端口IP地址。本示例输入192.168.100.1。**掩码**：WAN端口IP地址掩码。本示例输入255.255.255.252。**网关**：网关IP地址。本示例输入192.168.100.2 。**说明** 配置网关后，智能接入网关设备会自动添加一条默认路由。
2. 配置线下路由同步方式。您需要配置线下路由同步方式将本地机构的路由同步到云上，为后续和云上资源互通做准备。在智能接入网关实例详情页面，单击**网络配置**页签。在页签左侧区域，单击**线下路由同步方式**。选择**静态路由**，然后单击**添加静态路由**，配置静态路由信息，最后单击**确定**。静态路由添加为本地机构要和云上互通的网段：172.16.0.0/12。

##### 配置交换机和出口路由器

您还需要为智能接入网关设备对端的交换机和出口路由器添加路由配置，此处以某品牌交换机和路由器为例，由于不同厂商交换机和路由器配置不同，详情请参考厂商设备手册。

1. 三层交换机的路由配置。`interface GigabitEthernet 0/11
no switchport
ip address 192.168.100.2 255.255.255.252 #配置智能接入网关对端交换机的端口IP 
ip route 192.168.3.0 255.255.255.0 192.168.100.1 #交换机去往上海VPC的路由
ip route 0.0.0.0 0.0.0.0 192.168.80.1 #交换机去往公网路由`
2. 出口路由器的路由配置。`ip route 192.168.100.0 255.255.255.252 192.168.80.2 #出口路由器去往智能接入网关的路由`

##### 配置云上网络连接

在配置好设备后，您需要配置云上网络连接，将本地机构接入阿里云。

1. 创建云连接网。登录[智能接入网关管理控制台](https://smartag.console.aliyun.com/)。在顶部菜单栏，选择**中国内地**区域。云连接网区域需和智能接入网关设备使用区域保持一致。在左侧导航栏，单击**云连接网**。在**云连接网**页面，单击**创建云连接网**。在**创建云连接网**页面，配置云连接网名称，然后单击**确定**。云连接网名称长度为2~100个字符，以大小写字母或中文开头，可包含数字、下划线（_）和连接号（-）。
2. 绑定云连接网。在左侧导航栏，单击**智能接入网关**。在**智能接入网关**页面，单击目标实例**操作**列的**网络配置**。在页签左侧区域，单击**绑定网络详情**。在**绑定网络详情**页签下，单击**添加网络**，选择绑定云连接网并选择刚刚创建的云连接网实例，然后单击**确定**。
3. 绑定云企业网。绑定后，云连接网中的智能接入网关设备便可以和云企业网实例中已加载的网络实例VPC通信。在左侧导航栏，单击**云连接网**。单击刚刚创建的云连接网实例**操作**列的**绑定云企业网**。在**绑定云企业网**页面，**选择现有CEN**并选择要绑定的云企业网实例，单击**确定**。
4. 配置安全组规则。您需要为VPC中的云服务器（ECS）实例配置安全组规则，允许本地机构的私网网段172.16.0.0/12访问ECS中的资源。详情请参见[添加安全组规则](https://help.aliyun.com/zh/ecs/user-guide/add-a-security-group-rule)。

##### 访问测试

完成上述配置后，您可以通过本地机构的客户端尝试访问已连接的VPC中部署的云资源。

## 故障排除

#### CEN常见问题

CEN常见问题详情参见[常见问题](https://help.aliyun.com/zh/cen/support/faq)。

#### SAG问题排查

智能接入网关SAG问题排查详情参见[故障排查](https://help.aliyun.com/zh/sag/support/troubleshooting/)。

#### VPN网关常见问题

IPsec连接问题排查参见[问题排查](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/support/faq-about-ipsec-vpn-connections)，VPN网关问题排查参见[VPN网关常见问题](https://help.aliyun.com/zh/vpn/sub-product-ipsec-vpn/support/faq-about-vpn-gateways)。

#### VPC常见问题

VPC常见问题详情参见[常见问题](https://help.aliyun.com/zh/vpc/support/faq)。

## 相关内容

- [阿里云云采用框架](https://help.aliyun.com/zh/caf/components-of-a-landing-zone-on-alibaba-cloud/)
- [本地IDC通过专线访问云服务器ECS](https://help.aliyun.com/zh/express-connect/use-cases/connect-a-data-center-to-ecs-by-using-an-express-connect-circuit)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-23（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
