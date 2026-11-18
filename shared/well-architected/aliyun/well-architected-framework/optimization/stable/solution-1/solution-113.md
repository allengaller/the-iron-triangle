<!-- source: https://help.aliyun.com/zh/well-architected/solution-113 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929508 -->

# 企业级DMZ上云方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973237.png)

随着企业业务云化进程逐渐进入深水区，简单地使用云上资源出入公网已经无法满足业务的诉求，安全、成本、权限、监控等诉求的迭代，需要企业有系统性地视角来考虑如何做好公网出入口（DMZ）的规划设计。本方案统一阐述如何基于云上网络及安全相关产品来构建DMZ区，保障网络出入流量安全。

## 方案优势

### 统一管理

公网出口由企业IT部门统一管控，业务[VPC](https://help.aliyun.com/zh/vpc/what-is-vpc)通过[CEN](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)实现跨VPC出公网，各业务需要向IT部门申请后才能获取公网权限，防止业务部门私开公网资源导致业务遭受安全威胁。

### 保障安全

企业的WAN能力放到共享服务账号的DMZ VPC，在该VPC中部署[NAT网关](https://help.aliyun.com/zh/nat-gateway/product-overview/what-is-nat-gateway)、[NLB](https://help.aliyun.com/zh/slb/network-load-balancer/product-overview/what-is-nlb)、[ALB](https://help.aliyun.com/zh/slb/application-load-balancer/what-is-alb)等云产品可以联动[DDos防护](https://help.aliyun.com/zh/anti-ddos/overview)、[WAF](https://help.aliyun.com/zh/waf/web-application-firewall-3-0/product-overview/what-is-waf)、[云防火墙](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/product-overview/what-is-cloud-firewall)等安全产品保障公网出口安全，防止潜在针对云资源的攻击侵入。

### 成本优化

使用[共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/product-overview/what-is-internet-shared-bandwidth)实现出入口EIP带宽共享，优化公网成本。

### 统一监控

使用[NIS](https://help.aliyun.com/zh/nis/product-overview/what-is-network-intelligence-service)监控内网/外网访问情况，及时排查异常流量原因。

## 客户场景

### 公网统一出口

#### 场景描述

随着企业对于公网安全、成本、权限、监控等诉求的迭代，越来越需要系统性地视角来考虑如何做好公网出口的规划设计。公网出口通常统一部署在DMZ区、由企业IT部门统一管控，各业务需要向IT部门申请后才能获取公网出口权限，防止业务部门私开公网出口导致业务遭受安全威胁。

#### 适用客户

- 需要统一管控公网出口的企业客户。

### 公网统一入口

#### 场景描述

随着企业对于公网安全、成本、权限、监控等诉求的迭代，很多企业也开始规划如何做好公网入口的规划设计。公网入口在DMZ区统一管控后各业务需要向IT部门申请后才能获取公网入口权限，可以防止业务部门私开公网入口导致业务遭受安全威胁。

#### 适用客户

- 需要统一管控公网入口的企业客户。

### 实施方案

- 按照不同业务场景拆分了多个云账号对资源进行管理。
- 公网出口放到共享服务账号的DMZ VPC进行统一管控，使用[DDoS高防](https://help.aliyun.com/zh/anti-ddos/anti-ddos-pro-and-premium/product-overview/what-are-anti-ddos-pro-and-anti-ddos-premium)、[WAF](https://help.aliyun.com/zh/waf/web-application-firewall-3-0/product-overview/what-is-waf)、防火墙确保公网出入安全。
- 使用NAT网关流日志监控公网出入口流量信息，使用[网络ACL](https://help.aliyun.com/zh/vpc/network-acl-overview)进行访问行为管理，使用共享带宽包进行多业务流量共享。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973239.png)

### 客户收益

- 统一管理：公网出口统一管理，可以结合流日志及网络ACL实现可视化的监测与行为管理。
- 安全：可以选择更高级的能力组合，通过集成安全产品（如云FW）让企业更好的做风险控制。
- 成本：通过共享出入口带宽，实现多业务流量共享，降低流量费用。

## 方案架构

### 云上DMZ设计

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973238.png)

随着业务的发展及管控诉求，很多企业从传统的多VPC分布式出入口，演进到所有VPC在共享服务账号管控的统一DMZ VPC。**通常建议企业在DMZ VPC做公网统一出口，是否在DMZ VPC做公网统一入口根据企业实际情况进行选择**，ALB/NLB已分别在7/4层支持IP Target能力（创建IP类型服务器组，需要开白名单），能够便捷支持跨VPC进行后端服务器挂载。

- **DMZ VPC设计**：将企业云上公网出入口能力均放在**共享服务账号**的DMZ VPC，该VPC内可按需部署ALB、NLB、NAT网关等公网产品。
- **统一出口**：DMZ VPC与后端**业务账号**中的业务VPC通过**CEN-TR**组网进行打通，DMZ VPC中部署**公网NAT网关**作为公网统一出口，利用**SNAT**能力可为不同业务设置不同的EIP出口方便流量统计管理。
- **统一入口**：DMZ VPC与后端**业务账号**中的业务VPC通过TR或[PrivateLink](https://help.aliyun.com/zh/privatelink/what-is-a-private-network-connection)打通，通过ALB/NLB挂载后端服务器保障后端业务VPC无需暴露在公网。**公网ALB/NLB**作为统一入口，可跨VPC挂载后端服务器，配置回源路由后实现公网统一入口。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973241.png)
- **安全设计**：可联动DDoS防护、WAF、云防火墙等安全产品，保障公网出入口安全，并结合网络ACL实现安全访问策略。
- **成本优化**：启用共享带宽，并将所有EIP加入其中，节约成本。
- **权限划分**：利用将公网能力统一收口至IT部门，部署SNAT，业务VPC均通过CEN实现跨VPC访问公网。
- **监控管理**：可使用[网络智能服务NIS](https://help.aliyun.com/zh/nis/product-overview/what-is-network-intelligence-service)，监控公网出入口流量信息，并根据异动排查原因。

### 网络及安全产品选择

建议的网络及安全产品选择如下表。

| **方案** | **ALB** | **NAT网关** | **EIP** | **CEN-TR** | **共享带宽** | **DDoS防护** | **WAF** | **云防火墙** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 统一云上出口 | / | 必选 | 必选 | 必选 | 可选 | / | / | 必选 |
| 统一云上入口 | 必选 | / | 必选 | 必选 | 可选 | 必选 | 必选 | 可选 |
| 统一DMZ | 必选 | 必选 | 必选 | 必选 | 可选 | 必选 | 必选 | 必选 |

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云企业网CEN | [云企业网CEN（Cloud Enterprise Network）](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)是运行在阿里云私有全球网络上的一张高可用网络。云企业网通过**转发路由器TR（Transit Router）**帮助您在跨地域专有网络之间，专有网络与本地数据中心间搭建私网通信通道，为您打造一张灵活、可靠、大规模的企业级云上网络。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/cen/product-overview/billing/)。 |
| 转发路由器TR | [转发路由器TR（Transit Router）](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)是地域范围内企业级核心转发网元，可为您转发同地域或不同地域的网络实例间的流量，并支持在地域内定义灵活的互通、隔离、引流策略，帮助您打造一张灵活、可靠、大规模的企业级互联网络。转发路由器实例是云企业网实例的重要组成部分。 | 收费，CEN重要组成部分，请参见CEN计费规则。 |
| 弹性公网IP(EIP) | [弹性公网IP（Elastic IP Address，简称EIP](https://help.aliyun.com/product/61789.html)）是可以独立购买和持有的公网IP地址资源。目前，EIP仅支持绑定到专有网络类型的ECS实例、专有网络类型的私网SLB实例、专有网络类型的辅助弹性网卡、NAT网关和高可用虚拟IP上。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/eip/product-overview/billing)。 |
| 共享带宽 | [共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/product-overview/what-is-internet-shared-bandwidth)提供地域级带宽共享和复用功能，支持同地域下所有弹性公网IP共享带宽，能够让绑定弹性公网IP的云服务器ECS、NAT网关、负载均衡同时共享带宽，并提供包括按带宽峰值、增强型95等多种计费模式。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/internet-shared-bandwidth/product-overview/billing-overview/)。 |
| NAT网关(NATGW) | [NAT网关（NAT Gateway）](https://help.aliyun.com/zh/nat-gateway/product-overview/what-is-nat-gateway)可以提供网络地址转换服务。阿里云提供公网NAT网关和VPC NAT网关两款产品。公网NAT网关提供公网地址转换服务，VPC NAT网关提供私网地址转换服务，您可以根据业务需求灵活选择。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/nat-gateway/pricing/)。 |
| 应用型负载均衡ALB | [应用型负载均衡ALB（Application Load Balancer）](https://help.aliyun.com/zh/slb/application-load-balancer/what-is-alb)是阿里云推出的专门面向HTTP、HTTPS和QUIC等应用层负载场景的负载均衡服务，具备超强弹性及大规模应用层流量处理能力。ALB具备处理复杂业务路由的能力，与云原生相关服务深度集成，是阿里云官方提供的云原生Ingress网关。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/slb/application-load-balancer/alb-billing-rules)。 |
| 网络型负载均衡NLB | [网络型负载均衡NLB（Network Load Balancer ）](https://help.aliyun.com/zh/slb/network-load-balancer/product-overview/what-is-nlb)是阿里云面向万物互联时代推出的新一代四层负载均衡，支持超高性能和自动弹性能力，单实例可以达到1亿并发连接，帮您轻松应对高并发业务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/slb/network-load-balancer/product-overview/nlb-billable-items)。 |
| 专有网络VPC | [专有网络VPC（Virtual Private Cloud）](https://help.aliyun.com/zh/vpc/what-is-vpc)是您专有的云上私有网络。您可以完全掌控自己的专有网络，例如选择IP地址范围、配置路由表和网关等，您可以在自己定义的专有网络中使用阿里云资源，如云服务器、云数据库RDS和负载均衡等。 | 本身免费，详情参见[产品计费](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |
| 交换机vSwitch | [交换机（vSwitch）](https://help.aliyun.com/zh/vpc/create-and-manage-vswitch)是组成专有网络的基础网络模块，用来连接不同的云资源。成功创建交换机后，您可以在交换机中创建云资源、绑定自定义路由表或者绑定网络ACL。 | 免费，详情参见VPC[产品计费](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |
| DMZ | DMZ（全称Demilitarized Zone，中文为“非军事区”，或称Perimeter network，即“边界网络”、周边网络或“对外网络”）为一种网络架构的布置方案，常用的架设方案是在不信任的外部网络和可信任的内部网络外，创建一个面向外部网络的物理或逻辑子网，该子网能设置用于对外部网络的服务器主机。可以使用在防火墙、路由器等区隔内外网的网络设备。 |

## 安全性

### VPC安全性

专有网络VPC具有安全可靠、灵活可控、灵活可用以及较强的可扩展性，详情参见[产品优势](https://help.aliyun.com/zh/vpc/product-overview/benefits)及[访问控制](https://help.aliyun.com/zh/vpc/access-control)。

### 公网安全

应用《多账号网络安全统一防护方案》保障多账号网络安全，安全产品详情参考[DDoS防护](https://help.aliyun.com/zh/anti-ddos/overview)、[Web应用防火墙](https://help.aliyun.com/zh/waf/web-application-firewall-3-0/product-overview/what-is-waf)、[云防火墙](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/product-overview/what-is-cloud-firewall)。

## 注意事项

### 转发路由器使用限制

在您使用转发路由器产品前，请先了解产品限制，详情参见[使用限制](https://help.aliyun.com/zh/cen/product-overview/limits)。

### VPC使用限制

使用专有网络VPC（Virtual Private Cloud）前，请了解VPC的相关使用限制及提升配额方式。详情参见[限制与配额](https://help.aliyun.com/zh/vpc/understanding-vpc-quotas-in-alibaba-cloud)及[VPC支持的地域信息](https://help.aliyun.com/zh/vpc/regions-that-support-vpc-features)。

### NAT网关使用限制

NAT网关在产品功能和服务性能上的限制，以及如何申请更高配额，详情参见[使用限制](https://help.aliyun.com/zh/nat-gateway/limits)。

### ALB使用限制

应用型负载均衡ALB（Application Load Balancer）包含基础版和标准版，两个版本的使用限制不同，详情参见[使用限制](https://help.aliyun.com/zh/slb/application-load-balancer/quotas-and-limits)。

### 云防火墙使用限制

- 云防火墙**企业版、旗舰版支持VPC边界防火墙**，基础版（即免费版本）和高级版不支持VPC边界防火墙。云防火墙各版本的详情，请参见[产品版本与使用限制](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/product-overview/billing-of-cloud-firewall)。
- 开启VPC边界防火墙时，需要您关注的注意事项，请参见[VPC边界防火墙限制说明](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/overview-of-vpc-firewalls)。

### 白名单

#### ALB挂载IP类型后端服务器白名单

目前ALB挂载IP类型的服务器组（IP Target能力）需要开白名单，请[提交工单](https://workorder-intl.console.aliyun.com/#/ticket/createIndex)或找网络PDSA申请加白。

## 实施步骤

本实施示例在DMZ VPC中构建公网统一出入口，并使用后端业务VPC中的ECS进行部署验证。

• 统一出口：在TR组网架构下，使用NAT网关在DMZ VPC统一云上公网出口，为不同业务设置不同的EIP出口方便流量统计管理。

• 统一入口：DMZ VPC与后端业务VPC通过TR打通，通过ALB跨VPC挂载能力保障后端业务VPC无需暴露在公网。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973240.png)

### 实施准备

- 上图中涉及到的VPC已经创建，如DMZ VPC、业务VPC1、业务VPC2，本示例中VPC1用于实施验证公网统一入口，VPC2用于实施验证公网统一出口。
- 上图中两个业务VPC1与VPC2中分别部署ECS。
- VPC间已通过CEN-TR完成组网，DMZ VPC与VPC1、VPC2可互通。CEN-TR组网可参考帮助文档[使用云企业网实现跨地域跨账号VPC互通（企业版）](https://help.aliyun.com/zh/cen/getting-started/use-enterprise-edition-transit-routers-to-connect-vpcs-across-regions-and-accounts)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：

- 自动化方式：15分钟。
- 非自动化方式：90分钟。

### 操作步骤

#### 构建统一出口

##### 1、创建公网NAT网关实例

1. 登录[NAT网关管理控制台](https://vpc.console.aliyun.com/nat)。
2. 在**公网NAT网关**页面，单击**创建NAT网关**。
3. 首次使用NAT网关时，在创建公网NAT网关页面**关联角色创建**区域，单击**创建关联角色**。角色创建成功后即可创建NAT网关。关于NAT网关服务关联角色的更多信息，请参见[服务关联角色](https://help.aliyun.com/zh/nat-gateway/service-linked-role)。
4. 在创建公网NAT网关页面，配置以下购买信息，然后单击**立即购买**。**配置****说明****付费模式**默认选择为**按量付费**，即一种先使用后付费的付费模式。更多信息，请参见[公网NAT网关计费](https://help.aliyun.com/zh/nat-gateway/nat-gateway-billing)。**所属地域**选择需要创建公网NAT网关的地域。**所属专有网络**选择公网NAT网关所属的VPC(**本场景下选择DMZ VPC**)。创建后，不能修改公网NAT网关所属的VPC。**关联交换机**选择公网NAT网关实例所属的交换机。**计费类型**默认选择为**按使用量计费**，即按公网NAT网关实际使用量收费。更多信息，请参见[公网NAT网关计费](https://help.aliyun.com/zh/nat-gateway/nat-gateway-billing)。**计费周期**默认选择为**按小时**，即按使用量计费公网NAT网关的计费周期为1小时，不足1小时按1小时计算。**实例名称**设置公网NAT网关实例的名称。实例名称长度为2~128个字符，以英文大小字母或中文开头，可包含数字、下划线（_）和短划线（-）。**访问模式**选择公网NAT网关的访问模式。支持以下两种模式：o **VPC全通模式（SNAT）**：选择了VPC全通模式，在公网NAT网关创建成功后当前VPC内所有实例即可通过该公网NAT网关访问公网。选择**VPC全通模式（SNAT）**后，您需要配置弹性公网IP（Elastic IP Address，简称EIP）的相关信息。o **稍后配置**：如需稍后配置或有更多配置需求，可在购买完成后，前往控制台进行配置。选择**稍后配置**，则只购买公网NAT网关实例。**本文选择稍后配置。**
5. 在**确认订单**页面确认公网NAT网关的配置信息，选中服务协议并单击**确认订单**。

创建成功后，您可以在**公网NAT网关**页面查看网关类型为**增强型**的公网NAT网关。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973242.png)

##### 2、绑定EIP

您可以将EIP绑定到公网NAT网关上。公网NAT网关绑定EIP后，可以使用EIP配置DNAT条目和SNAT条目。

1. 登录[NAT网关管理控制台](https://vpc.console.aliyun.com/nat)。
2. 在**公网NAT网关**页面，找到前一步创建的公网NAT网关实例，然后在**操作**列选择**> 绑定弹性公网IP**。
3. 在**绑定弹性公网IP**对话框，配置以下参数，然后单击**确定**。**所在资源组**：选择EIP所在的资源组。**选择弹性公网IP**：选择要绑定到公网NAT网关的EIP。**从已有弹性公网IP中选择**：在下拉列表中选择已有的EIP实例。**新购弹性公网IP并绑定**：系统将为您创建1个按使用流量计费的EIP实例，并绑定到公网NAT网关。本文选择**新购弹性公网IP并绑定**。
4. EIP绑定完成后，您可以在**公网NAT网关**页面查看绑定的EIP。

##### 3、创建SNAT条目

公网NAT网关支持SNAT功能，为VPC中无公网IP的ECS实例提供访问互联网的代理服务。

1. 登录[NAT网关管理控制台](https://vpc.console.aliyun.com/nat)。
2. 在**公网NAT网关**页面，找到上一步创建的公网NAT网关实例，然后在**操作**列单击**设置SNAT**。
3. 在**SNAT条目列表**区域，单击**创建SNAT条目**。
4. 在**创建SNAT条目**页面，根据以下信息配置SNAT条目，然后单击**确定创建**。**SNAT条目粒度**：本文选择自定义CIDR，即通过云企业网打通的所有VPC下的ECS实例都可以通过配置的SNAT规则访问互联网，本示例对应的IP网段填写0.0.0.0/0 。**选择公网IP地址**：选择用来提供互联网访问的EIP。本文选择**使用单IP**，然后在下拉列表选择绑定到公网NAT网关的EIP。**条目名称**：SNAT条目的名称。名称长度为2~128个字符，以大小写字母或中文开头，可包含数字、下划线（_）和短划线（-）。

##### 4、配置默认路由

1. 在VPC2的系统路由表中添加自定义路由条目，目标网段**0.0.0.0/0**，下一跳为转发路由器，选择VPC2与TR的连接。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973243.png)
2. 在与**VPC2所关联的TR路由表**中添加自定义路由条目，目标网段**0.0.0.0/0，下一跳为与DMZ VPC的TR连接。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973245.png)

#### 构建统一入口

##### 1、创建ALB实例

登录[应用型负载均衡ALB控制台](https://slb.console.aliyun.com/alb)，创建实例，实例网络类型选择**公网**、VPC选择**DMZ VPC**，详情可参考[创建应用型负载均衡](https://help.aliyun.com/zh/slb/application-load-balancer/create-and-manage-alb-instances)。

##### 2、创建ALB服务器组

创建IP类型的服务器组，并为该服务器添加远端IP。

1. 登录[应用型负载均衡ALB控制台](https://slb.console.aliyun.com/alb)。
2. 在左侧导航栏，选择**应用型负载均衡ALB > 服务器组**。
3. 在**服务器组**页面，单击**创建服务器组**，完成以下配置，然后单击**创建**。**配置****说明****服务器组类型**选择服务器组类型。本文选择**IP类型**。（**请参考注意事项章节，申请白名单**）**服务器组名称**输入服务器组名称。长度为2~128个字符，必须以大小写字母或中文开头，可包含数字、半角句号（.）、下划线（_）和短划线（-）。**VPC**从VPC下拉列表中选择一个VPC。本文选择DMZ VPC。**选择后端协议**选择一种后端协议。本文选择**HTTP**。**选择调度算法**选择一种调度算法。本文使用默认值**加权轮询**。**选择资源组**选择归属的资源组。**开启会话保持**开启或关闭会话保持。本文选择默认关闭。**配置健康检查**开启或关闭健康检查。本文选择默认开启。**高级配置**本文使用默认配置。更多信息，请参见[管理服务器组](https://help.aliyun.com/zh/slb/application-load-balancer/create-and-manage-a-server-group)。
4. 在**服务器组**页面，找到目标服务器组，然后在**操作**列单击**编辑后端服务器**。
5. 在**后端服务器**页签，单击**添加IP**。
6. 在**添加后端服务器**面板，输入ECS1的私网IP地址，并打开**远端IP**，然后单击**下一步**。
7. 设置添加的IP地址的端口和权重，然后单击**确定**。本文端口输入80，权重使用默认值。

##### 3、为ALB实例配置监听

1. 登录[应用型负载均衡ALB控制台](https://slb.console.aliyun.com/alb)。
2. 在顶部菜单栏，选择ALB的所属地域。
3. 在**实例**页面，找到已经在DMZ VPC中创建好的ALB实例，在**操作**列单击**创建监听**。
4. 在**配置监听**配置向导，完成以下配置，然后单击**下一步**。**监听配置****说明****选择负载均衡协议**选择监听的协议类型。本文选择**HTTP**。**监听端口**输入用来接收请求并向后端服务器进行请求转发的监听端口，端口范围为1~65535。本文输入80。**监听名称**自定义监听的名称。**高级配置**本文使用默认配置。

1. 在**选择服务器组**配置向导，在**选择服务器组**的下拉框选择**IP类型**，并选择前一步创建的服务器组，然后单击**下一步**。
2. 在**配置审核**配置向导，确认配置信息，单击**提交**。

##### 4、为DMZ VPC的系统路由表添加路由条目

检查DMZ VPC中的系统路由表是否已经有目标网段的路由指向转发路由器DMZ VPC连接，如果没有，则执行以下步骤添加路由条目。

1. 登录[专有网络管理控制台](https://vpcnext.console.aliyun.com/vpc)。
2. 在**专有网络**页面，单击DMZ VPC的实例ID。
3. 在DMZ VPC详情页面，单击**资源管理**页签，在**路由表**下方单击数字链接。
4. 在**路由表**页面，找到**路由表类型**为**系统**的路由表并单击ID。
5. 在路由表详情页面，选择**路由条目列表 > 自定义路由条目**页签，然后单击**添加路由条目**。
6. 在**添加路由条目**面板，配置以下参数，然后单击**确定**。**参数****说明****名称**输入路由条目的名称。**目标网段**输入要转发到的目标网段。本示例输入VPC1网段地址：172.16.0.0/24**下一跳类型**选择下一跳的类型。本文选择**转发路由器**。**转发路由器**选择具体的转发路由器实例，本文选择VPC1与TR的连接。

##### 5、配置回源路由

查看ALB实例的回源路由，并分别为业务VPC1的系统路由表和VPC1关联的TR路由表添加ALB的回源路由。

1. 执行以下步骤，获取ALB实例的**回源路由**。登录[应用型负载均衡ALB控制台](https://slb.console.aliyun.com/alb)。在顶部菜单栏，选择实例的所属地域。在**实例**页面，单击在DMZ VPC中已经创建好的ALB实例ID。单击**实例详情**页签，然后在**回源路由**右侧单击**查看**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973244.png)
2. 执行以下步骤，为VPC1内的系统路由表添加ALB的回源路由。登录[专有网络管理控制台](https://vpcnext.console.aliyun.com/vpc)。在**专有网络**页面，单击VPC1的实例ID。在VPC详情页面，单击**资源管理**页签，在**路由表**下方单击数字链接。在**路由表**页面，找到**路由表类型**为**系统**的路由表，单击其ID。在路由表详情页面，选择**路由条目列表 > 自定义**页签，然后单击**添加自定义路由条目**。在**添加路由条目**面板，配置以下参数，然后单击**确定**。**参数****说明****名称**输入路由条目的名称。**目标网段**输入要转发到的目标网段。本文输入ALB实例的回源路由。如果回源路由有多条，请重复配置操作，直到所有回源路由全部配置完。本文为VPC1配置的路由条目为：100.XX.XX.0/25100.XX.XX.128/25100.XX.XX.64/26100.XX.XX.128/26100.XX.XX.192/26100.XX.XX.0/26**下一跳类型**选择下一跳的类型。本文选择**转发路由器**。**转发路由器**选择具体的转发路由器实例。本文选择VPC1关联的转发路由器。
3. 执行以下步骤，为VPC1关联的转发路由器添加ALB的回源路由。登录[云企业网管理控制台](https://cen.console.aliyun.com/)。在**云企业网实例**页面，单击已创建的云企业网实例ID。在**基本信息 > 转发路由器**页签，找到连接VPC1的转发路由器实例，并单击该目标转发路由器实例ID。单击**转发路由器路由表**页签，在页签左侧区域，单击目标路由表ID，在路由表详情页面的**路由条目**页签下，单击**创建路由条目**。在**添加路由条目**对话框，配置路由条目信息，然后单击**确定**。**配置项****说明****路由表**系统默认选择当前路由表。**所属转发路由器**系统默认选择当前转发路由器实例。**路由条目名称**路由条目名称。长度为0~128个字符，可包含大小写字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线（_）和短划线（-）。**目的地址CIDR**路由条目的目标网段。本文输入[步骤](https://help.aliyun.com/zh/slb/application-load-balancer/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region)[1](https://help.aliyun.com/zh/slb/application-load-balancer/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region)中ALB实例的回源路由。如果回源路由有多条，请重复配置操作，直到所有回源路由全部配置完。本文为VPC1关联的转发路由器配置的路由条目：100.XX.XX.0/25100.XX.XX.128/25100.XX.XX.64/26100.XX.XX.128/26100.XX.XX.192/26100.XX.XX.0/26**是否为黑洞路由**系统默认选择否。**下一跳连接**选择路由的下一跳连接。本文选择**TR与DMZ VPC连接**。**路由条目描述**路由条目的描述信息。长度为2~256个字符，可包含大小写字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线（_）和短划线（-）。

##### 6、检查后端ECS的安全组策略

跨VPC访问的报文会以回源路由网段内的IP地址作为源地址访问后端服务，请确保ECS的安全组策略可以放通此报文。更多信息，请参见[添加安全组规则](https://help.aliyun.com/zh/ecs/user-guide/add-a-security-group-rule)。

#### 出入口验证

##### 测试出口访问

1. 测试VPC2 中ECS实例是否可以访问互联网。如下图所示，执行ping命令测试网络连通性。经测试，ECS可以访问互联网。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973246.png)
2. 执行`curl myip.ipip.net`命令探测ECS的公网出口IP。经测试，VPC2 ECS公网出口IP与公网NAT网关实例中SNAT条目中的IP一致，即ECS通过公网NAT网关的SNAT功能主动访问互联网。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973248.png)

##### 测试入口访问

在业务VPC1的ECS上启动HTTP服务，测试本地是否能通过ALB访问业务VPC内的ECS。可以通过ALB实例详情页面查看ALB实例的DNS域名。本示例执行命令`wget alb-xxx.cn-xxx.alb.aliyuncs.com`,如果能接收到回复报文，表示连接成功。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973247.png)

#### 自动化搭建

除了上文的控制台搭建，用户还可以选择自动化搭建的方式，包括使用[云治理中心](https://help.aliyun.com/zh/cgc/product-overview/what-is-cloud-governance-center)及Terraform自动化的方式搭建。

##### 云治理中心搭建

云治理中心提供了网络蓝图模板，用户可以基于蓝图模板轻松搭建Landing Zone。目前搭建支持启用云企业网CEN及DMZ统一出口构建，操作详情参见[搭建Landing Zone](https://help.aliyun.com/zh/cgc/user-guide/build-a-landing-zone)。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973249.png)

##### Terraform搭建

支持使用Terraform搭建DMZ，代码及说明详情参见[GitHub代码库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/networking/build-dmz)。

### 扩展实施指引

本章节描述DMZ VPC相关扩展实施选项，包括整体组网（DMZ VPC、安全VPC、业务VPC）路由示例、云防火墙、DDoS高防、WAF接入指引。

#### 云企业网CEN组网

##### CEN-TR路由设计

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8676581571/p973250.png)

##### 云企业网基础配置

具体配置可以参考[使用云企业网实现同地域云上云下网络互通](https://help.aliyun.com/zh/cen/getting-started/connect-network-instances-in-the-same-region)。

##### 路由表配置

使用企业版转发路由器多路由表功能：

- 在不可信路由表针对没有经过防火墙的东西向流量通过私网路由引流至安全VPC。
- 在不可信路由表主动访问公网流量的流量通过默认路由指向DMZ VPC。
- 在不可信路由表同时配置ALB回源路由指向DMZ VPC。
- 在可信路由表针对经过防火墙处理后的东西向流量通过私网路由引流至对应的业务VPC。

#### 云防火墙

防火墙开启后，如果您未配置任何访问控制策略或威胁引擎未开启拦截模式，您的业务流量将只经过云防火墙，云防火墙不会对业务流量进行拦截，因此不会对业务产生任何影响。您可以在**防火墙开关**页面，为您的资产开启或关闭防火墙开关。开启防火墙无需进行复杂的网络配置，开启后即可使用。

##### 限制说明

参考上文注意事项章节中的云防火墙使用限制。

##### 操作步骤

1. 登录[云防火墙控制台](https://yundun.console.aliyun.com/?p=cfwnext)。
2. 在左侧导航栏，选择**防火墙开关 > 防火墙开关**。
3. 在**防火墙开关**页面，开启防火墙开关。

**说明** 由于仅云防火墙企业版和旗舰版支持VPC边界防火墙，如果您开通的是云防火墙基础版（即免费版本）或高级版，您在**防火墙开关**页面将无法看到**VPC边界防火墙**页签。

您可以为资产开启**互联网边界防火墙**或**VPC边界防火墙**：

- **互联网边界防火墙：**在**互联网边界防火墙**页面，定位到需要开启互联网边界防火墙保护的资产，单击**操作**列的**开启保护**。如果您需要同时对多个资产执行开启或关闭防火墙保护的操作，可以在防火墙列表中选择多个目标资产，然后单击左下角的**开启保护**或**关闭保护**。
- **VPC边界防火墙：**在**VPC边界防火墙**页面，定位到需要开启VPC边界防火墙保护的资产，单击**操作**列的**开启保护**。如果您需要同时对多个资产执行开启或关闭防火墙保护的操作，可以在防火墙列表中选择多个目标资产，然后单击左下角的**开启保护**或**关闭保护**。
- 您可通过筛选**资产类型**、**地域**、**防火墙状态**、**账号**来搜索并查看指定资产的防火墙开启状态。
- 开启或关闭防火墙后，防火墙状态更新为保护中（表示防火墙的防护已生效）或未受保护（表示防火墙的防护已关闭）。防火墙状态更新可能需要数秒时间，请耐心等待。

##### 防火墙相关操作参考

- [开启攻击防护](https://help.aliyun.com/zh/document_detail/90538.html)
- [配置访问控制策略](https://help.aliyun.com/zh/document_detail/90537.html)

#### 联合部署DDoS高防和WAF

如果您的网络遭受的攻击既有流量型攻击，又混杂精巧的Web应用层攻击时，单一使用一种网络安全防护产品无法起到全面的防护效果，我们推荐您组合使用阿里云DDoS高防和Web应用防火墙（Web Application Firewall，简称 WAF）。业务同时部署DDoS高防和WAF的背景及配置指导详情参见[联合部署DDoS高防和WAF提升防护能力](https://help.aliyun.com/zh/waf/web-application-firewall-2-0/user-guide/protect-a-website-by-using-both-anti-ddos-pro-or-anti-ddos-premium-and-waf)。

## 源代码

使用Terraform代码搭建DMZ的支持内容包括方案中的公网统一出入口的大部分场景。

- **代码地址**：[GitHub代码](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/networking/build-dmz)。
- **代码说明**：示例代码在使用CEN-TR基础组网已经完成的基础上进行搭建，执行时需要在settings.tfvars中进行参数配置，需提供已有网路配置及要创建的NAT、ALB配置，已有配置例如提供VPC ID、转发路由器TR ID等，详情参见代码库具体说明。

## 故障排除

### VPC内新建交换机下的ECS实例无法通过SNAT访问公网，而该VPC内其他交换机下的ECS实例可以通过SNAT访问公网

- NAT网关中的SNAT条目中不包含新建的交换机的网段。NAT网关不会为新建的交换机配置SNAT条目，您需要检查新建的交换机的网段是否已经包含在NAT网关已有SNAT条目中。如果未包含，则该交换机下的ECS实例无法访问公网。请您手动配置SNAT条目，具体操作，请参见[创建公网NAT网关SNAT条目实现访问公网服务](https://help.aliyun.com/zh/nat-gateway/create-a-snat-entry)。
- 新建的交换机绑定了自定义路由表，但自定义路由表中没有目标网段为0.0.0.0/0，下一跳为NAT网关的自定义路由条目。请确认自定义路由表中是否有上述路由条目，如果没有，请手动进行添加，具体操作，请参见[添加路由表中的路由条目](https://help.aliyun.com/zh/vpc/user-guide/create-and-manage-route-table)。

### VPC内存在多个NAT网关时，某个交换机下的ECS实例不能访问公网

- 如果该VPC内只使用系统路由表，且只有一条目标网段为0.0.0.0/0，下一跳指向其中一个NAT网关的自定义路由条目。当VPC内某个交换机的网段不在该NAT网关的SNAT条目中，则该交换机下的ECS实例不能访问公网。
- 如果无需使用多个NAT网关，建议您删除不需要使用的NAT网关，并为保留的NAT网关增加SNAT条目配置。
- 如果需要使用多个NAT网关，请参见[同VPC内多NAT网关部署方案](https://help.aliyun.com/zh/nat-gateway/deploy-multiple-internet-nat-gateways-in-one-vpc)。

### 新增一个VPC加载到TR后，到DMZ VPC无法ping通

请检查新增VPC、TR、及DMZ VPC路由配置，尤其注意检查DMZ VPC路由表中是否有到新增VPC的路由条目，目标网段为新增VPC的网段，下一跳为TR与DMZ VPC的连接，可参考上文章节**为DMZ VPC的系统路由表添加路由条目。**

### ALB请求响应为500、502、503、504状态码的解释及可能原因是什么？

#### 500（Internal Server Error）

后端服务内部错误，后端服务遇到意外情况，无法执行请求。

可能原因：ALB后端服务或应用出现问题，请根据后端服务和应用的日志排查问题。

#### 502（Bad Gateway）

HTTP或HTTPS监听接收到客户端连接请求后，ALB由于无法正常将请求转发至后端服务或无法从后端服务收到响应，则会收到客户端HTTP 502 Bad Gateway状态码。可能原因：

- ALB后端服务或应用直接返回502状态码，请排查后端服务或应用的日志，确定返回502状态码的原因。
- ALB与后端服务之间TCP通信异常，请排查后端服务或应用的状态是否正常、服务端口是否正常被监听、Backlog队列是否有丢包现象等。
- 健康检查异常，请排查ALB实例对应服务器组的健康检查状态，健康检查配置的状态码与后端服务返回的状态码是否一致。
- ALB后端服务没有及时完成请求处理，请排查后端服务或应用的日志，并查看对应后端服务或应用的CPU、内存等占用率。

#### 503（Service Temporarily Unavailable）

暂时无法使用服务。可能原因：

- 监听没有配置后端服务器，或者用户配置的后端服务器的权重为0。
- ALB流量超出规格，出现限速。

#### 504（Gateway Time-out）

后端服务响应超时。可能原因：

- 后端服务直接返回504状态码，请排查后端服务的负载情况。
- 后端服务负载增大，响应请求的时间大于配置的响应超时时间。例如配置的响应超时时间是60秒，如果响应时间超过60秒，则ALB返回504。您可以从访问日志查看对应时间段的延时情况。

## 相关内容

- [云防火墙最佳实践](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/use-cases/)
- [接入WAF](https://help.aliyun.com/zh/waf/web-application-firewall-2-0/user-guide/tutorial)
- [DDoS高防用户指南](https://help.aliyun.com/zh/anti-ddos/anti-ddos-pro-and-premium/user-guide/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-113（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
