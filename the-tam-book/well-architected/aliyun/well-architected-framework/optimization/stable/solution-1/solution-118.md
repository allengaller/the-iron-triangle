<!-- source: https://help.aliyun.com/zh/well-architected/solution-118 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929507 -->

# 多ACK集群的统一公网出入方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0776581571/p973232.png)

多数企业在大规模上云之前会根据实际组织架构及系统需求设计Landing Zone框架，统一公网出入口已经成为Landing Zone网络架构设计的主流之一，统一公网出入口通常采用统一的账号，甚至统一的VPC来管理和部署公网资产，例如NAT网关，SLB，EIP等，以便于安全及网络团队统一进行管理和监控。

随着企业系统的架构越加复杂，微服务架构的系统已经逐渐开始成为企业系统架构的主流选择之一，阿里云ACK（Alibaba Cloud Container Service for Kubernetes）作为阿里云主要的容器服务产品之一，提供了丰富的Kubernetes集群的部署及管理模式，ACK提供了多种流量网关的接入方式，包括基于阿里云CLB的Nginx Ingress，基于ALB的ALB Ingress，以及MSE的云原生网关。

本方案统一阐述如何基于云上网络及安全相关产品来构建DMZ区，完成多个ACK集群统一网络出入，保障网络出入流量安全。

## 方案优势

### 统一管理

公网出口由企业IT部门统一管控，业务[VPC](https://help.aliyun.com/zh/vpc/what-is-vpc)通过[CEN](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)实现跨VPC出公网，各业务需要向IT部门申请后才能获取公网权限，防止业务部门私开公网资源导致业务遭受安全威胁。

### 保障安全

企业的WAN能力放到共享服务账号的DMZ VPC，在该VPC中部署[NAT网关](https://help.aliyun.com/zh/nat-gateway/product-overview/what-is-nat-gateway)、[NLB](https://help.aliyun.com/zh/slb/network-load-balancer/product-overview/what-is-nlb)、[ALB](https://help.aliyun.com/zh/slb/application-load-balancer/what-is-alb)等云产品可以联动[DDos防护](https://help.aliyun.com/zh/anti-ddos/overview)、[WAF](https://help.aliyun.com/zh/waf/web-application-firewall-3-0/product-overview/what-is-waf)、[云防火墙](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/product-overview/what-is-cloud-firewall)等安全产品保障公网出口安全，防止潜在针对云资源的攻击侵入。

### 成本优化

使用[共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/product-overview/what-is-internet-shared-bandwidth)实现出入口EIP带宽共享，优化公网成本。

### 统一监控

使用[NIS](https://help.aliyun.com/zh/nis/product-overview/what-is-network-intelligence-service)监控内网/外网访问情况，及时排查异常流量原因。

### 中心化管理公网 ALB

ACK集群的ALB Ingress统一采用私网模式，在统一公网出入口账号部署公网ALB进行流量转发，所有系统必须通过网络或安全团队审核才可开通公网ALB访问，提升内部系统安全性，提高安全或网络团队的管控能力。

## 客户场景

### 应对企业安全要求

#### 场景描述

企业网络团队或安全团队希望统一对所有系统的公网访问及公网入口进行管控，必须通过安全或网络团队才可创建响应资源。

#### 适用客户

- 使用资源目录管理云上多个账号的企业客户。
- 使用多个阿里云账号的企业客户。
- 存在中心运维（安全或网络）团队的企业客户。
- 使用统一公网出入口方案的企业客户。
- 使用容器服务搭建企业系统的客户。

### 公网统一出口

#### 场景描述

随着企业对于公网安全、成本、权限、监控等诉求的迭代，越来越需要系统性地视角来考虑如何做好公网出口的规划设计。公网出口通常统一部署在DMZ区、由企业IT部门统一管控，各业务需要向IT部门申请后才能获取公网出口权限，防止业务部门私开公网出口导致业务遭受安全威胁。

#### 适用客户

- 需要统一管控公网出口的企业客户。
- 使用容器服务搭建企业系统的客户。

### 公网统一入口

#### 场景描述

随着企业对于公网安全、成本、权限、监控等诉求的迭代，很多企业也开始规划如何做好公网入口的规划设计。公网入口在DMZ区统一管控后各业务需要向IT部门申请后才能获取公网入口权限，可以防止业务部门私开公网入口导致业务遭受安全威胁。

#### 适用客户

- 需要统一管控公网入口的企业客户。
- 使用容器服务搭建企业系统的客户。

## 方案架构

### 云上DMZ设计

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0776581571/p973234.png)

随着业务的发展及管控诉求，很多企业从传统的多VPC分布式出入口，演进到所有VPC在共享服务账号管控的统一DMZ VPC。**通常建议企业在DMZ VPC做公网统一出口，是否在DMZ VPC做公网统一入口根据企业实际情况进行选择**，ALB/NLB已分别在7/4层支持IP Target能力（创建IP类型服务器组，需要开白名单），能够便捷支持跨VPC进行后端服务器挂载。

- **DMZ VPC设计**：将企业云上公网出入口能力均放在**共享服务账号**的DMZ VPC，该VPC内可按需部署ALB、NLB、NAT网关等公网产品。
- **统一出口**：DMZ VPC与后端**业务账号**中的业务VPC通过**CEN-TR**组网进行打通，DMZ VPC中部署**公网NAT网关**作为公网统一出口，利用**SNAT**能力可为不同业务设置不同的EIP出口方便流量统计管理。
- **统一入口**：DMZ VPC与后端**业务账号**中的业务VPC通过TR或[PrivateLink](https://help.aliyun.com/zh/privatelink/what-is-a-private-network-connection)打通，通过ALB/NLB挂载后端服务器保障后端业务VPC无需暴露在公网。**公网ALB/NLB**作为统一入口，可跨VPC挂载后端服务器，配置回源路由后实现公网统一入口。

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
| 负载均衡ALB | [应用型负载均衡ALB（Application Load Balancer）](https://help.aliyun.com/zh/slb/application-load-balancer/what-is-alb)是阿里云推出的专门面向HTTP、HTTPS和QUIC等应用层负载场景的负载均衡服务，具备超强弹性及大规模应用层流量处理能力。ALB具备处理复杂业务路由的能力，与云原生相关服务深度集成，是阿里云官方提供的云原生Ingress网关。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| NAT网关 | [NAT网关（NAT Gateway）](https://help.aliyun.com/zh/nat-gateway/user-guide/public-network-nat-gateway)可以提供网络地址转换服务。阿里云提供公网NAT网关和VPC NAT网关两款产品。公网NAT网关提供公网地址转换服务，VPC NAT网关提供私网地址转换服务，您可以根据业务需求灵活选择。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/nat-gateway/nat-gateway-billing)。 |
| 转发路由器TR | [转发路由器TR（Transit Router）](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)是地域范围内企业级核心转发网元，可为您转发同地域或不同地域的网络实例间的流量，并支持在地域内定义灵活的互通、隔离、引流策略，帮助您打造一张灵活、可靠、大规模的企业级互联网络。转发路由器实例是云企业网实例的重要组成部分。 | 收费，CEN重要组成部分，请参见CEN计费规则。 |
| 弹性公网IP(EIP) | [弹性公网IP（Elastic IP Address，简称EIP](https://help.aliyun.com/product/61789.html)）是可以独立购买和持有的公网IP地址资源。目前，EIP仅支持绑定到专有网络类型的ECS实例、专有网络类型的私网SLB实例、专有网络类型的辅助弹性网卡、NAT网关和高可用虚拟IP上。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/eip/product-overview/billing)。 |
| 网络型负载均衡NLB | [网络型负载均衡NLB（Network Load Balancer ）](https://help.aliyun.com/zh/slb/network-load-balancer/product-overview/what-is-nlb)是阿里云面向万物互联时代推出的新一代四层负载均衡，支持超高性能和自动弹性能力，单实例可以达到1亿并发连接，帮您轻松应对高并发业务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/slb/network-load-balancer/product-overview/nlb-billable-items)。 |
| 专有网络VPC | [专有网络VPC（Virtual Private Cloud）](https://help.aliyun.com/zh/vpc/what-is-vpc)是您专有的云上私有网络。您可以完全掌控自己的专有网络，例如选择IP地址范围、配置路由表和网关等，您可以在自己定义的专有网络中使用阿里云资源，如云服务器、云数据库RDS和负载均衡等。 | 本身免费，详情参见[产品计费](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |
| 交换机vSwitch | [交换机（vSwitch）](https://help.aliyun.com/zh/vpc/create-and-manage-vswitch)是组成专有网络的基础网络模块，用来连接不同的云资源。成功创建交换机后，您可以在交换机中创建云资源、绑定自定义路由表或者绑定网络ACL。 | 免费，详情参见VPC[产品计费](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |
| ACK容器服务 | [容器服务Kubernetes版（Alibaba Cloud Container Service for Kubernetes，简称容器服务ACK）](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/product-overview/what-is-ack)提供高性能可伸缩的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ack/billing-information)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |
| DMZ | DMZ（全称Demilitarized Zone，中文为“非军事区”，或称Perimeter network，即“边界网络”、周边网络或“对外网络”）为一种网络架构的布置方案，常用的架设方案是在不信任的外部网络和可信任的内部网络外，创建一个面向外部网络的物理或逻辑子网，该子网能设置用于对外部网络的服务器主机。可以使用在防火墙、路由器等区隔内外网的网络设备。 |

## 安全性

### RBAC授权

RBAC（Role-Based Access Control）是基于角色的访问控制，通过RBAC可以将权限与集群角色相关联，从而为不同角色成员配置不同的权限策略。详细请参考[配置RAM用户或RAM角色RBAC权限](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles)。

### VPC安全性

专有网络VPC具有安全可靠、灵活可控、灵活可用以及较强的可扩展性，详情参见[产品优势](https://help.aliyun.com/zh/vpc/product-overview/benefits)及[访问控制](https://help.aliyun.com/zh/vpc/access-control)。

### 跨账号网络实例授权

在转发路由器实例连接其他账号的网络实例前，需要其他账号的网络实例对转发路由器实例进行授权。授权说明及操作详情参见[跨账号网络实例授权](https://help.aliyun.com/zh/cen/user-guide/grant-permissions-on-a-network-instance-that-belongs-to-another-account)。

### 公网安全

应用《多账号网络安全统一防护方案》保障多账号网络安全，安全产品详情参考[DDoS防护](https://help.aliyun.com/zh/anti-ddos/overview)、[Web应用防火墙](https://help.aliyun.com/zh/waf/web-application-firewall-3-0/product-overview/what-is-waf)、[云防火墙](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/product-overview/what-is-cloud-firewall)。

## 注意事项

### 转发路由器使用限制

在您使用转发路由器产品前，请先了解产品限制，详情参见[使用限制](https://help.aliyun.com/zh/cen/product-overview/limits)。

### NAT网关使用限制

NAT网关在产品功能和服务性能上的限制，以及如何申请更高配额，详情参见[使用限制](https://help.aliyun.com/zh/nat-gateway/limits)。

### ALB使用限制及白名单

- 应用型负载均衡ALB（Application Load Balancer）包含基础版和标准版，两个版本的使用限制不同，详情参见[使用限制](https://help.aliyun.com/zh/slb/application-load-balancer/quotas-and-limits)。
- 目前ALB挂载IP类型的服务器组（IP Target能力）需要开白名单，请找网络PDSA申请加白。

### 云防火墙使用限制

- 云防火墙**企业版、旗舰版支持VPC边界防火墙**，基础版（即免费版本）和高级版不支持VPC边界防火墙。云防火墙各版本的详情，请参见[产品版本与使用限制](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/product-overview/billing-of-cloud-firewall)。
- 开启VPC边界防火墙时，需要您关注的注意事项，请参见[VPC边界防火墙限制说明](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/overview-of-vpc-firewalls)。

## 实施步骤

### 实施架构图

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0776581571/p973231.png)

### 数据规划

| 配置项 | 地域 | 配置值 | 可用区 [2] | 描述 |
| --- | --- | --- | --- | --- |
| 账号 UID |  | 111111 |  | 统一公网出入口管理账号 |
| DMZ-VPC | 香港 | 172.16.0.0/16 |  | 统一公网出入口VPC |
| DMZ-vSwitch1 | 172.16.1.0/24 | 可用区B | 部署ALB及SNAT网关； |  |
| DMZ-vSwitch2 | 172.16.2.0/24 | 可用区C | 部署ALB及SNAT网关 |  |
| DMZ-vSwitch3 | 172.16.3.0/24 | 可用区B | 连接CEN-TR |  |
| DMZ-vSwitch4 | 172.16.4.0/24 | 可用区C | 连接CEN-TR |  |
| 账号 UID |  | 222222 |  | 业务系统账号 |
| Biz-VPC | 香港 | 192.168.0.0/16 |  | 业务系统VPC |
| Biz-vSwitch5 | 192.168.5.0/24 | 可用区B | 部署ACK集群私网ALB Ingress |  |
| Biz-vSwitch6 | 192.168.6.0/24 | 可用区C | 部署ACK集群私网ALB Ingress |  |
| Biz-vSwitch7 | 192.168.7.0/24 | 可用区B | 部署ACK集群ECS工作节点 |  |
| Biz-vSwitch8 | 192.168.8.0/24 | 可用区C | 部署ACK集群ECS工作节点 |  |
| Biz-vSwitch9 | 192.168.9.0/24 | 可用区B | 连接CEN-TR |  |
| Biz-vSwitch10 | 192.168.10.0/24 | 可用区C | 连接CEN-TR |  |
| Biz-vSwitch11 |  | 192.168.11.0/24 | 可用区B | 部署ACK集群POD节点 |
| Biz-vSwitch12 |  | 192.168.12.0/24 | 可用区C | 部署ACK集群POD节点 |

说明：

1. 在业务账号内部署ACK集群，建议将ALB/ECS/POD/CEN-TR所在交换机分开。
2. 因为合规及跨地域网络资源成本及利用率考虑，本文档统一公网出入口及业务系统VPC均为香港地域。如果需要跨地域方案，请事前咨询相关合规及安全团队评估风险。
3. 创建ALB，CEN网络实例连接，及NAT网关时，请确认当前所在地域相关服务支持的可用区，vSwitch交换机需要创建在服务支持的可用区以便后续服务的部署。详细请参考以下文档。[企业版转发路由器支持的地域和可用区](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)[ALB支持的地域与可用区](https://help.aliyun.com/zh/slb/application-load-balancer/supported-regions-and-zones)请前往阿里云工作台确认NAT网关支持可用区，目前香港地域支持可用区B和C

### 前置准备

- 已为阿里云账号UID（111111）申请ALB白名单，可以为ALB创建IP类型的服务器组。
- 已创建如上表中提到的VPC及交换机，本文档以账号UID 111111 香港地域VPC作为统一公网出入口VPC，以账号UID 222222香港地域VPC作为业务系统部署VPC。[1]

### 操作步骤

#### 1.1 通过CEN创建跨账号VPC连接

##### 1.1.1 创建CEN转发路由器

1. 登录账号UID 111111，进入CEN控制台。
2. 点击「创建云企业网实例」，输入云企业网名称，本文使用「DMZ-CEN」，点击「确认」。
3. 点击CEN实例ID（cen-xxxxxxxxxxx），在转发路由器标签页选择「创建转发路由器」，本文使用以下配置，并点击「确认创建」，创建过程通常会在1到2分钟内完成。地域：中国（香港）勾选同意转发路由器协议并点击「开通转发路由器服务」，转发路由器服务会创建一个关联服务角色，以便CEN之后访问相关网络资源，如VPC，CCN等，点击「确定开通」。名称：CEN-TR-HK

##### 1.1.2 为DMZ-VPC创建CEN转发路由器网络实例连接

1. 点击创建的转发路由器实例ID（tr-xxxxxxxxxxx）。
2. 在「地域内连接管理」页签选择「创建网络实例连接」
3. 本文使用以下配置，点击「确定创建」，创建过程通常会在1到2分钟内完成。实例类型：专有网络（VPC）地域：中国（香港）资源归属UID：同账号付费方式：按量付费连接名称：（例）DMZ-VPC-Attach网络实例：选择DMZ-VPC交换机：香港可用区B，选择DMZ-vSwitch3，香港可用区C选择DMZ-vSwitch4高级配置：默认勾选三个自助选项（自动关联至转发路由器的默认路由表，自动传播系统路由至转发路由器的默认路由表，自动为VPC的所有路由表配置指向转发路由器的路由），连接至CEN的VPC网络会自动联通。

##### 1.1.3 授权CEN跨账号加载VPC

1. 登入阿里云账号UID 222222，打开专有网络VPC页面。
2. 点击预先创建的Biz-VPC VPC ID（vpc-xxxxxxxxxxx）。
3. 切换到「云企业网跨账号授权」页签，点击「云企业网跨账号授权」键。
4. 填写信息并点击「确定」以授权账号UID 111111内的CEN可跨账号加载该业务VPC。对方账号UID：111111（此为示例UID，请填写实际的UID）对方云企业网实例ID：cen-xxxxxxxxxxx（参考步骤1.1.1.3）资费承担方式：CEN用户承担资费（CEN相关费用由CEN所在账号统一承担，如需业务账号承担请选择VPC用户承担资费）

##### 1.1.4 为业务VPC创建CEN转发路由器网络实例连接

1. 登入阿里云账号UID 111111，进入CEN控制台。
2. 点击DMZ-CEN实例ID cen-xxxxxxxxxx。
3. 在转发路由器页签，点击转发路由器ID tr-xxxxxxxxxx。
4. 在「地域内连接管理」页签选择「创建网络实例连接」
5. 本文使用以下配置，点击「确定创建」，创建过程通常会在1到2分钟内完成。实例类型：专有网络（VPC）地域：中国（香港）资源归属UID：跨账号UID：222222付费方式：按量付费连接名称：（例）Biz-VPC-Attach网络实例：选择阿里云账号UID 111111内的Biz-VPC交换机：香港可用区B，选择DMZ-vSwitch9，香港可用区C选择DMZ-vSwitch10高级配置：默认勾选三个自助选项（自动关联至转发路由器的默认路由表，自动传播系统路由至转发路由器的默认路由表，自动为VPC的所有路由表配置指向转发路由器的路由），连接至CEN的VPC网络会自动联通。

#### 1.2 公网出口部署

##### 1.2.1 创建公网NAT网关实例

1. 登录账号UID 111111，进入专有网络VPC控制台。
2. 在「NAT网关」「公网NAT网关」页面点击「创建NAT网关」键。
3. 首次使用NAT网关时，在创建公网NAT网关页面「关联角色创建」区域，单击「创建关联角色」。角色创建成功后即可创建NAT网关。关于NAT网关服务关联角色的更多信息，请参见[服务关联角色](https://help.aliyun.com/zh/nat-gateway/service-linked-role)。
4. 在创建公网NAT网关页面，配置以下购买信息，然后单击「立即购买」。**配置****说明****付费模式**默认选择为「按量付费」，即一种先使用后付费的付费模式。更多信息，请参见[公网NAT网关计费](https://help.aliyun.com/zh/nat-gateway/nat-gateway-billing)。**所属地域**选择需要创建公网NAT网关的地域，本文选择「中国香港」。**所属专有网络**选择公网NAT网关所属的VPC。创建后，不能修改公网NAT网关所属的VPC。本文选择DMZ-VPC。**关联交换机**选择公网NAT网关实例所属的交换机，本文选择DMZ-vSwitch2。**计费类型**默认选择为「按使用量计费」，即按公网NAT网关实际使用量收费。更多信息，请参见[公网NAT网关计费](https://help.aliyun.com/zh/nat-gateway/nat-gateway-billing)。**计费周期**默认选择为「按小时」，即按使用量计费公网NAT网关的计费周期为1小时，不足1小时按1小时计算。**实例名称**设置公网NAT网关实例的名称，本文使用DMZ-NAT。实例名称长度为2~128个字符，以英文大小字母或中文开头，可包含数字、下划线（_）和短划线（-）。**访问模式**选择公网NAT网关的访问模式。支持以下两种模式：VPC全通模式（SNAT）：选择了VPC全通模式，在公网NAT网关创建成功后当前VPC内所有实例即可通过该公网NAT网关访问公网。选择VPC全通模式（SNAT）后，您需要配置弹性公网IP（Elastic IP Address，简称EIP）的相关信息。稍后配置：如需稍后配置或有更多配置需求，可在购买完成后，前往控制台进行配置。选择稍后配置，则只购买公网NAT网关实例。本文选择「稍后配置」。
5. 在确认订单页面确认公网NAT网关的配置信息，选中服务协议并单击「确认订单」。当出现「恭喜，购买成功！」的提示后，说明您创建成功，通常需要1-2分钟创建NAT网关。创建成功后，您可以在「公网NAT网关」页面查看网关类型为「增强型」的公网NAT网关。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0776581571/p973233.png)

##### 1.2.2 为NAT网关创建EIP并绑定

您需要将EIP绑定到公网NAT网关上。公网NAT网关绑定EIP后，可以使用EIP配置DNAT条目和SNAT条目。

1. 登入阿里云账号UID 111111控制台。
2. 打开专有网络页面，在「公网访问」分类下选择「弹性公网IP」。
3. 点击「创建弹性公网」。
4. 在购买页面填写信息，并点击「立即购买」，以下信息供参考。**配置****说明****付费模式**默认选择为「按量付费」，即一种先使用后付费的付费模式。更多信息，请参见[公网EIP计费](https://help.aliyun.com/zh/eip/billing-overview)。**地域和可用区域**选择需要创建公网EIP的地域，本文选择「中国香港」。**线路类型**选择「BGP（多线）」。创建后，不能修改公网EIP类型。线路类型分别请参考[申请EIP文档](https://help.aliyun.com/zh/eip/apply-for-new-eips)。**网络类型**公网。**安全防护**默认，默认提供不超过5Gbps的基础DDoS防护能力。**流量**默认选择为「按使用流量计费」，即根据每小时出向公网的实际流量计费。不同的计费模式请参考[EIP计费方式文档](https://help.aliyun.com/zh/eip/pay-as-you-go/)。**带宽峰值**设置公网EIP的峰值带宽，本文选择200Mbps。如果该峰值带宽无法满足您的业务需求，请创建工单联系我们的售后人员。**名称**本文使用DMZ-NAT-EIP，可根据实际运维习惯命名。
5. 在「NAT网关」分类下选择「公网NAT网关」，找到之前1.2.1创建的DMZ-NAT，在「弹性公网IP」栏点击「立即绑定」。
6. 选择EIP所在资源组（默认为默认资源组），选择「从已有弹性公网IP中选择」，选择步骤4创建的EIP，点击「确定」键。刷新页面后可见到EIP已绑定NAT网关。

##### 1.2.3 创建SNAT路由条目

公网NAT网关支持SNAT功能，为VPC中无公网IP的ECS/POD实例提供访问互联网的代理服务。

1. 登录[NAT网关管理控制台](https://vpc.console.aliyun.com/nat)。
2. 在**公网NAT网关**页面，找到上一步创建的公网NAT网关实例，然后在**操作**列单击**设置SNAT**。
3. 在**SNAT条目列表**区域，单击**创建SNAT条目**。
4. 在**创建SNAT条目**页面，根据以下信息配置SNAT条目，然后单击**确定创建**。**SNAT条目粒度**：统一公网出口方案需选择「自定义网段粒度」，指定网段下的ECS可以通过配置的公网IP访问互联网，如选择其他配置方式，Biz-VPC无法通过NAT网关访问互联网。自定义网段：填写Biz-VPC（192.168.0.0/16）及DMZ-VPC（172.16.0.0/16）的网段。**选择公网IP地址**：选择用来提供互联网访问的EIP。本文选择「**使用单IP」**，然后在下拉列表选择绑定到公网NAT网关的EIP。
5. 打开专有网络页面，点击DMZ-VPC ID，「资源管理」页签内点击「路由表」数字1。
6. 点击路由表ID（vtb-xxxxxxxxxx），在「路由条目列表」下的「自定义路由条目」内点击「添加路由条目」键，此文档我们使用以下配置。名称：DMZ-SNAT-Route，可根据实际运维习惯调整。目标网段：0.0.0.0/0。下一跳类型：NAT网关。NAT网关：选择1.2.1创建的NAT网关。
7. 创建成功后在「CEN中状态」点击「发布」，发布成功后，CEN路由表会自动生成一跳路由，以下供参考。目标网段：0.0.0.0/0。下一跳：tr-attach-xxxxxxxxxx，DMZ-VPC-Attach。类型：连接实例。路由类型：自动学习。路由状态：可用。

##### 1.2.4 为业务VPC创建SNAT路由条目

之前的步骤为DMZ-VPC创建了SNAT路由条目，此章节我们为业务VPC（Biz-VPC）创建SNAT条目，业务VPC内资源访问互联网时的流量会经过CEN，到达DMZ-VPC，之后经过NAT网关访问互联网资源。

1. 登入阿里云账号UID 222222，打开专有网络VPC页面。
2. 点击预先创建的Biz-VPC VPC ID（vpc-xxxxxxxxxxx）。
3. 打开「资源管理」页签，在「专有网络资源」部分下点击「路由表」数字1。
4. 点击路由表ID（vtb-xxxxxxxxxx），在「路由条目列表」下选择「自定义路由条目」，点击「添加路由条目」键。
5. 输入以下内容将此VPC内访问互联网的流量引流至CEN。名称：本文使用DMZ-VPC-Route，可根据实际运维习惯更改。目标网段：0.0.0.0/0下一跳类型：转发路由器转发路由器：选择Biz-VPC连接至CEN-TR时的ID，可参考1.1.4获取连接ID（例tr-attach-xxxxxxxxxx）。

##### 1.2.5 （可选）测试统一公网出口路由

您可以在Biz-VPC内创建一部无公网IP的ECS，通过VNC或堡垒机远程到该ECS。在该ECS上尝试访问公网系统，观测是否经过DMZ-VPC NAT网关访问公网。本文档使用Linux服务器，尝试拿取访问互联网时的公网IP。

参考指令：

```
curl https://ip.me/
```

输出结果可见到公网访问的IP是NAT网关的公网IP，即业务Biz-VPC内的服务器访问公网时，流量都会经过NAT网关，NAT网关的公网IP可在[NAT网关页面](https://vpc.console.aliyun.com/nat/cn-hongkong/nats)查看。

#### 1.3 创建ACK集群并部署服务

##### 1.3.1 创建ACK集群

登录阿里云UID 222222 容器服务管理控制台。

在控制台左侧导航栏中，单击集群。

在集群列表页面中，单击页面右上角的创建集群。

在ACK托管版页签下，配置以下相关的集群参数，未说明参数保留默认设置即可。

| 项目 | 内容 | 备注 |
| --- | --- | --- |
| 集群名称 | 输入集群名称，例如ack-demo |  |
| 地域 | 香港 |  |
| 付费类型 | 安量付费 | 测试完毕后如无需保留测试环境请及时删除集群避免产生额外费用。 |
| Kubernetes版本 | 1.24.3-aliyun.1 |  |
| 容器运行时 | congtainerd 1.5.10 |  |
| 专有网络 | 选择香港地域创建的Biz-VPC |  |
| 网络插件 | Terway |  |
| IPvlan及NetowkrPolicy支持 | 开启 |  |
| 虚拟交换机 | 选择创建的Biz-vSwitch-7/8 | 请选择上面数据规划表中规划好的交换机 |
| Pod虚拟交换机 | 选择创建的Biz-vSwitch-11/12 |  |
| Service DIDR | 10.0.0.0/24 | 建议不与已经创建的VPC重叠 |
| 配置SNAT | 否 |  |
| API Server访问 | 标准型slb.s2.small使用EIP暴露API Server：否 |  |
| 自动创建企业安全组 | 是 |  |
| 集群删除保护 | 是 | 如需删除集群，请手动关闭该保护 |
| 实例规格 | 选择g7a.xlarge |  |
| 数量 | 2 |  |
| 系统盘 | ESSD PL1，120 GB | 推荐开启加密选项。说明：若提示创建请完成RAM授权，创建AliyunCSManagedSecurityRole角色可供ACK调用KMS服务 |
| 操作系统 | Alibaba Cloud Linux 3.2104 |  |
| 安全加固 | CIS加固 |  |
| 登录方式 | 设置密钥 | 可根据实际运维习惯调整 |
| 密钥对 | 选择刚刚创建的密钥 |  |
| Ingress | ALB Ingress |  |
| 其余配置项 | 选择默认配置 |  |

##### 1.3.2 创建AlbConfig

说明：客户可以通过堡垒机远程访问ACK Kubernetes集群，通过以下YAML部署以下无状态工作负载，服务及路由，也可以通过阿里云ACK工作台「使用YAML创建资源」功能白屏创建相关负载，服务及路由。

创建并拷贝以下内容到alb-test.yaml文件中，用于创建AlbConfig。

```
# 创建AlbConfig
# vSwtichId选择vSwitch-5，vSwitch-6（见上面数据规划表）
apiVersion: alibabacloud.com/v1
kind: AlbConfig
metadata:
  name: alb-demo
spec:
  config:
    name: alb-test
    addressType: Intranet
    zoneMappings:
    - vSwitchId: vsw-123456789****
    - vSwitchId: vsw-123456789****
```

**注意**！在生产环境中部署需要考虑一下ALB规格。建议合理评估业务峰值与流量。

连接Kubernetes集群，执行创建以上yaml文件，及执行以下命令。

```
kubectl apply -f alb-test.yaml
```

预期的输出。

```
AlbConfig.alibabacloud.com/alb-demo created
```

##### 1.3.3 创建IngressClass

说明：客户可以通过堡垒机远程访问ACK Kubernetes集群，通过以下YAML部署以下无状态工作负载，服务及路由，也可以通过阿里云ACK工作台「使用YAML创建资源」功能白屏创建相关负载，服务及路由。

创建并拷贝以下内容到alb.yaml文件中，用于创建IngressClass。

```
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: alb
spec:
  controller: ingress.k8s.alibabacloud/alb
  parameters:
    apiGroup: alibabacloud.com
    kind: AlbConfig
    name: alb-demo
```

连接Kubernetes集群，执行创建以上yaml文件，及执行以下命令。

```
kubectl apply -f alb.yaml
```

预期的输出。

```
ingressclass.networking.k8s.io/alb created
```

##### 1.3.4 部署服务

说明：客户可以通过堡垒机远程访问ACK Kubernetes集群，通过以下YAML部署以下无状态工作负载，服务及路由，也可以通过阿里云ACK工作台「使用YAML创建资源」功能白屏创建相关负载，服务及路由。

创建并拷贝以下内容到cafe-service.yaml文件中，用于部署两个名称分别为coffee和tea的Deployment，以及两个名称分别为coffee和tea的Service。

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: coffee
spec:
  replicas: 2
  selector:
    matchLabels:
      app: coffee
  template:
    metadata:
      labels:
        app: coffee
    spec:
      containers:
      - name: coffee
        image: registry.cn-hangzhou.aliyuncs.com/acs-sample/nginxdemos:latest
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: coffee-svc
spec:
  ports:
  - port: 80
    targetPort: 80
    protocol: TCP
  selector:
    app: coffee
  type: NodePort
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tea
spec:
  replicas: 1
  selector:
    matchLabels:
      app: tea
  template:
    metadata:
      labels:
        app: tea
    spec:
      containers:
      - name: tea
        image: registry.cn-hangzhou.aliyuncs.com/acs-sample/nginxdemos:latest
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: tea-svc
spec:
  ports:
  - port: 80
    targetPort: 80
    protocol: TCP
  selector:
    app: tea
  type: NodePort
```

执行以下命令，部署两个Deployment和两个Service。

```
kubectl apply -f cafe-service.yaml
```

预期的输出。

```
deployment "coffee" created
service "coffee-svc" created
deployment "tea" created
service "tea-svc" created
```

执行以下命令，查看服务状态。

```
kubectl get svc,deploy
```

预期的输出。

```
NAME             TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
coffee-svc   NodePort    172.16.231.169   <none>        80:31124/TCP   6s
tea-svc      NodePort    172.16.38.182    <none>        80:32174/TCP   5s
NAME            DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deploy/coffee   2         2         2            2           1m
deploy/tea      1         1         1            1           1m
```

##### 1.3.5 配置Ingress

说明：客户可以通过堡垒机远程访问ACK Kubernetes集群，通过以下YAML部署以下无状态工作负载，服务及路由，也可以通过阿里云ACK工作台「使用YAML创建资源」功能白屏创建相关负载，服务及路由。

创建并拷贝以下内容到cafe-ingress.yaml文件中，用于部署两个名称分别为coffee和tea的Deployment，以及两个名称分别为coffee和tea的Service。

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: cafe-ingress
spec:
  ingressClassName: alb
  rules:
  - http:
      paths:
      - path: /tea
        pathType: ImplementationSpecific
        backend:
          service:
            name: tea-svc
            port:
              number: 80
      # 配置Context Path
      - path: /coffee
        pathType: ImplementationSpecific
        backend:
          service:
            name: coffee-svc
            port:
              number: 80
```

执行以下命令，配置coffee和tea服务对外暴露的域名和path路径。

```
kubectl apply -f cafe-ingress.yaml
```

预期的输出。

```
ingress "cafe-ingress" created
```

#### 1.4 入口设计

通过1.3步骤操作，ACK集群的Ingress与Serivce资源已部署就绪，接下来需要配置DMZ中的公网ALB，将流量转发到集群私网ALB上。

##### 1.4.1 创建ALB服务器组

创建IP类型的服务器组，并为该服务器添加远端IP。

1. 登录[应用型负载均衡ALB控制台](https://slb.console.aliyun.com/alb)。
2. 在左侧导航栏，选择**应用型负载均衡ALB > 服务器组**。
3. 在**服务器组**页面，单击**创建服务器组**，完成以下配置，然后单击**创建**。**配置****说明****服务器组类型**选择服务器组类型。本文选择**IP类型**。说明：IP类型后端服务器组需要创建工单申请白名单。**服务器组名称**输入服务器组名称。长度为2~128个字符，必须以大小写字母或中文开头，可包含数字、半角句号（.）、下划线（_）和短划线（-）。**VPC**从VPC下拉列表中选择一个VPC。本文选择DMZ-VPC。**选择后端协议**选择一种后端协议。本文选择**HTTP**。**选择调度算法**选择一种调度算法。本文使用默认值**加权轮询**。**选择资源组**选择归属的资源组。**开启会话保持**开启或关闭会话保持。本文选择默认关闭。**配置健康检查****开启或关闭健康检查，本文选择默认开启，修改健康检查路径为/tea或/coffee，因为此文档未在ACK集群内创建路径为根目录的Ingress路由。****注意：**请根据实际业务系统返回请求配置健康检查，若目标实例（本文为Intranet ALB）无法通过ALB服务器组健康检查，默认会返回502 Bad Gateway，即使后端服务正常。**高级配置**本文使用默认配置。更多信息，请参见[管理服务器组](https://help.aliyun.com/zh/slb/application-load-balancer/create-and-manage-a-server-group)。
4. 在**服务器组**页面，找到目标服务器组，然后在**操作**列单击**编辑后端服务器**。
5. 在**后端服务器**页签，单击**添加IP**。
6. 在**添加后端服务器**面板，输入上一章节内的ALB私网IP地址，并开启「远端IP」，然后单击**下一步**。
7. 设置添加的IP地址的端口和权重，然后单击**确定**。本文端口输入80，权重使用默认值。

##### 1.4.2 创建ALB实例配置监听

1. 登录[应用型负载均衡ALB控制台](https://slb.console.aliyun.com/alb)。
2. 在顶部菜单栏，选择ALB的所属地域。本文选择**中国香港**。
3. 在**实例**页面，点击**创建应用型负载均衡。**
4. 使用如下配置，并点击「立即购买」。**配置****说明****地域**中国香港**实例网络类型**公网**VPC**从VPC下拉列表中选择一个VPC，本文选择DMZ-VPC。**可用区**香港 可用区B选择DMZ-vSwitch1香港 可用区C选择DMZ-vSwitch2选择**自动分配公网IP****IP模式**本文选择固定IP**协议版本**IPv4**功能版本**标准版说明：标准版支持自定义TLS安全策略，重定向等高级功能，建议选用标准版ALB**加入共享带宽**不选择**公网计费方式**按流量计费**实例名称**dmz-alb，客户可根据运维需求调整实例名称

##### 1.4.3 为ALB实例配置监听

1. 登录[应用型负载均衡ALB控制台](https://slb.console.aliyun.com/alb)。
2. 在顶部菜单栏，选择ALB的所属地域。本文选择**中国香港**。
3. 在**实例**页面，**找到已经在**DMZ-VPC**中创建好的ALB实例**，在**操作**列单击**创建监听**。
4. 在**配置监听**配置向导，完成以下配置，然后单击**下一步**。**监听配置****说明****选择负载均衡协议**选择监听的协议类型。本文选择**HTTP**。**监听端口**输入用来接收请求并向后端服务器进行请求转发的监听端口，端口范围为1~65535。本文输入80。**监听名称**自定义监听的名称。**高级配置**本文使用默认配置。
5. 在**选择服务器组**配置向导，在**选择服务器组**的下拉框选择**IP类型**，并选择前一步创建的服务器组，然后单击**下一步**。
6. 在**配置审核**配置向导，确认配置信息，单击**提交**。

##### 1.4.4 配置回源路由

查看ALB实例的回源路由，并分别为Biz-VPC的系统路由表和DMZ-VPC关联的CEN-TR转发路由器添加ALB的回源路由。

1. 执行以下步骤，获取ALB实例的回源路由。登录[应用型负载均衡ALB控制台](https://slb.console.aliyun.com/alb)。在顶部菜单栏，选择实例的所属地域。本文选择**中国香港**。在**实例**页面，单击在DMZ-VPC中已经创建好的ALB实例ID。单击**实例详情**页签，然后在**回源路由**右侧单击**查看**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0776581571/p973235.png)
2. 执行以下步骤，为Biz-VPC内的系统路由表添加ALB的回源路由。登录UID 222222，打开[专有网络管理控制台](https://vpcnext.console.aliyun.com/vpc)。在**专有网络**页面，单击Biz-VPC的实例ID。在VPC详情页面，单击**资源管理**页签，在**路由表**下方单击数字链接。在**路由表**页面，找到**路由表类型**为**系统**的路由表，单击其ID。在路由表详情页面，选择**路由条目列表 > 自定义**页签，然后单击**添加自定义路由条目**。在**添加路由条目**面板，配置以下参数，然后单击**确定**。**参数****说明****名称**输入路由条目的名称。**目标网段**输入要转发到的目标网段。本文输入[步骤](https://help.aliyun.com/zh/slb/application-load-balancer/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region)[1](https://help.aliyun.com/zh/slb/application-load-balancer/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region)中ALB实例的回源路由。如果回源路由有多条，请重复配置操作，直到所有回源路由全部配置完。本文为Biz-VPC配置的路由条目为：100.122.189.128/26100.122.189.192/26100.122.189.64/26100.122.190.0/26100.122.188.128/26100.122.188.192/26100.122.188.64/26100.122.189.0/26**下一跳类型**选择下一跳的类型。本文选择**转发路由器**。**转发路由器**选择具体的转发路由器实例。本文选择Biz-VPC关联的转发路由器连接ID tr-attach-xxxxxxxxxx。
3. 执行以下步骤，为DMZ-VPC关联的转发路由器添加ALB的回源路由。登录UID 111111，打开[云企业网管理控制台](https://cen.console.aliyun.com/)。在**云企业网实例**页面，单击已创建的云企业网实例ID。在**基本信息 > 转发路由器**页签，找到连接DMZ-VPC的转发路由器实例，并单击该目标转发路由器实例ID。单击**转发路由器路由表**页签，在页签左侧区域，单击目标路由表ID，在路由表详情页面的**路由条目**页签下，单击**创建路由条目**。在**添加路由条目**对话框，配置路由条目信息，然后单击**确定**。**配置项****说明****路由表**系统默认选择当前路由表。**所属转发路由器**系统默认选择当前转发路由器实例。**路由条目名称**路由条目名称。长度为0~128个字符，可包含大小写字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线（_）和短划线（-）。**目的地址CIDR**路由条目的目标网段。本文输入[步骤](https://help.aliyun.com/zh/slb/application-load-balancer/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region)[1](https://help.aliyun.com/zh/slb/application-load-balancer/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region)中ALB实例的回源路由。如果回源路由有多条，请重复配置操作，直到所有回源路由全部配置完。本文为DMZ-VPC关联的转发路由器配置的路由条目：100.122.189.128/26100.122.189.192/26100.122.189.64/26100.122.190.0/26100.122.188.128/26100.122.188.192/26100.122.188.64/26100.122.189.0/26**是否为黑洞路由**保持系统默认选择否。**下一跳连接**选择路由的下一跳连接。本文选择DMZ-VPC连接。**路由条目描述**路由条目的描述信息。长度为2~256个字符，可包含大小写字母、数字、中文、半角逗号（,）、半角句号（.）、半角分号（;）、正斜线（/）、at（@）、下划线（_）和短划线（-）。

##### 1.4.5（可选）检查后端ECS的安全组策略

跨VPC访问的报文会以回源路由网段内的IP地址作为源地址访问后端服务，请确保ECS的安全组策略可以放通此报文。更多信息，请参见[添加安全组规则](https://help.aliyun.com/zh/ecs/user-guide/add-a-security-group-rule)。

说明：步骤1.3.1中我们默认使用ACK自动创建企业版安全组进行部署，如需要精细化的ACK工作节点安全组控制，客户可以选择已创建的安全组或更改自动创建的企业安全组配置。

##### 1.4.6 验证

搭建完毕环境之后可通过浏览器访问前端公网ALB域名（或IP）验证方案是否部署成功，正常会显示以下页面，该文档我们访问以下两个路径确认服务生效，您可根据实际业务系统调整监听端口或路径。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0776581571/p973236.png)

## 故障排除

### 创建云企业网并跨账号授权连接后网络不通

请参考以下文档：

- [云企业网跨账号授权连接后网络不通](https://help.aliyun.com/zh/cen/why-do-vpcs-within-different-alibaba-cloud-accounts-fail-to-access-each-other-after-the-required-authorization-is-completed)

### 公网入口ALB无法访问后段ACK ALB Ingres

- ALB 回源路由配置遗漏
- CEN加载网络实例未勾选自动学习网络实例路由，导致不同网络实例之间不通

## 相关内容

- [使用ALB挂载IDC服务器](https://help.aliyun.com/zh/slb/application-load-balancer/specify-an-on-premises-server-as-a-backend-server-of-alb)
- [通过公网NAT网关实现云上统一公网出入口IP](https://help.aliyun.com/zh/document_detail/189646.html)
- 阿里云云防火墙 - [防护云企业网TR连接的VPC之间的所有流量](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/use-cases/protect-traffic-between-vpcs-connected-by-using-a-cen-transit-router)
- 阿里云ACK - [通过ALB Ingress访问服务](https://help.aliyun.com/zh/ack/serverless-kubernetes/user-guide/access-services-by-using-an-alb-ingress-2)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-118（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
