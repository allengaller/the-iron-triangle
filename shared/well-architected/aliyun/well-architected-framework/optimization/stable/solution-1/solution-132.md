<!-- source: https://help.aliyun.com/zh/well-architected/solution-132 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929504 -->

# 量化交易高质量网络方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8776581571/p973220.png)

数字货币交易所API为投资客户提供K线数据获取、下单/撤单、大宗交易、做市等量化交易服务。对交易所而言，提供的接口响应速度越快、稳定性越好，对数字货币投资客户越具有吸引力，交易成交量大才能获取利润丰厚。对交易所的用户而言，获取行情、下单交易的API速度越快，获取利润的可能性越高。

数字货币交易所和投资客户双方都对网络质量有着极高的要求，本方案能够帮助交易所优化量化交易接口，提高量化交易接口的网络响应速度和稳定性，同时帮助数字货币投资客户用最快的速度接入交易所进行投资交易。

## 方案优势

### 最短路径、最低时延

- 通过双方VPC中交换机同地域同可用区部署，实现客户交易系统服务器和交易所API之间网络最短路径，以最快的网络速度获取行情信息及下单。
- 客户在其他平台或IDC就近接入阿里云，通过CEN接入交易所VPC所在Region；CEN金牌线路提供最短线路，最优的跨域时延。

### 高效的流量处理效率

- 交易所的API，使用ALB做接入网关，支持基于路径、HTTP标头、查询字符串、HTTP请求方法、Cookie和SourceIP等多种条件来识别特定业务流量，并将其转发至不同的后端服务器。更高效的处理基于不同规则的请求流量转发。
- 交易所的API，使用ALB WAF增强版，负载均衡集成了WAF的安全能力，同时流量不用绕行WAF处理，提高了流量的转发效率。

### 安全稳定的API

ALB自带DDoS防护，集成Web应用防火墙。同时提供全链路HTTPS加密，支持预制和自定义安全策略、TLS 1.3等高效安全加密协议，面向加密敏感型业务，满足Zero-Trust新一代安全技术架构需求。

## 客户场景

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8776581571/p973218.png)

交易所的API，为用户提供K线数据获取、下单/撤单、大宗交易、做市等量化交易服务。API接口的响应速度和稳定性，直接关系到量化投资客户的实际收益。因此API接口响应速度越快、稳定性越好，对数字货币投资客户越具有吸引力。交易所量化交易投资用户越多，交易所的成交量越大，交易佣金越高，交易所因此才能获得丰厚的利润。

交易所API 是一种标准的Web类型服务，分公共频道和私有频道，公共频道通过互联网提供服务、私有频道通过VPC内网IP提供服务。一般API 通过负载均衡对用户请求进行负载分摊后，转发流量至后段的API服务器进行处理。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8776581571/p973217.png)

数字货币投资客户，需要通过交易所来进行数字货币的买卖交易，因数字货币是7*24小时交易，行情变化非常快，价格波动起伏非常大。因此数字货币投资客户几乎全部采取自动化交易的形式，通过交易所的API来进行投资管理。机构客户或者投资规模比较大的客户都会选择通过私有频道的API来进行投资管理。一般情况下，投资客户希望以最快的时间获取实时行情，当出现投资机会时以最快的时间进行成单。

一些投资客户会在多个交易所，进行分散交易，以达到最佳的投资策略，获取最大的利润。由于绝大多数的交易所部署在AWS，这部分客户会选择将量化交易的策略研究系统服务器放在AWS，客户连接交易所在阿里云的交易系统会部署在阿里云上，并通过高速通道专线，连通阿里云和AWS的网络环境，实现同时在AWS和阿里云上的交易所进行量化投资管理。

### 交易所量化交易API质量优化

#### 场景描述

交易所对外服务的API接口，API需要响应速度快、流量转发效率高、安全可靠。

#### 适用客户

- 数字货币交易所。
- NFT交易平台。

### 投资客户最短路径接入交易所

#### 场景描述

投资机构接入交易所API网络环境，需要VPC在同可用区距离缩短时延、交易策略和交易系统间需要通过最快的线路。

#### 适用客户

- 私募机构。
- 量化交易投资机构。

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8776581571/p973219.png)

- **交易所API入口使用ALB WAF增强版：**交易所API 使用ALB WAF增强版作为入口网关，ALB WAF增强版采用WAF 3.0服务化接入，相比之前的WAF 2.0透明化接入，服务化接入方式中WAF不参与流量转发，业务监听与转发由ALB负责，实现转发与防护的完全分离，避免了WAF转发额外带来的各种兼容性和稳定性问题，兼顾转发高效性与安全性。
- **交易所API通过转发路由实现跨VPC挂载服务器**：交易所API使用的ALB作为负载均衡网关，既可以部署在交易所账号下，也可以部署在机构客户的账号下。ALB通过转发路由器TR，进行跨VPC挂载后端Web服务器。
- **客户策略系统和交易下单系统通过跨Region金牌线路实现最短时延：**如果客户的策略决策系统和交易下单系统部署在不同地域（如东京、中国香港），所在VPC可通过CEN跨域专线连接网络。为了获得最短时延，东京的服务器或专线接入端需要部署在距离海缆最近的地方，东京A可用区。同时阿里云工程师对流量进行标记，然后通过最短路径传输直中国香港服务器，可以节省约6ms左右的时延。
- **客户交易下单系统与交易所入口API部署在同一可用区**：客户交易下单系统所在VPC可与交易所API所在VPC部署在同一地域，通过转发路由器跨账号授权后进行连接，双方系统所属的交换机处于同一可用区，可做到网络路径最短、时延最优。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 应用型负载均衡ALB | [应用型负载均衡ALB（Application Load Balancer）](https://help.aliyun.com/zh/slb/application-load-balancer/what-is-alb)是阿里云推出的专门面向HTTP、HTTPS和QUIC等应用层负载场景的负载均衡服务，具备超强弹性及大规模应用层流量处理能力。ALB具备处理复杂业务路由的能力，与云原生相关服务深度集成，是阿里云官方提供的云原生Ingress网关。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/slb/application-load-balancer/alb-billing-rules)。 |
| 云企业网CEN | [云企业网CEN（Cloud Enterprise Network）](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)是运行在阿里云私有全球网络上的一张高可用网络。云企业网通过**转发路由器TR（Transit Router）**帮助您在跨地域专有网络之间，专有网络与本地数据中心间搭建私网通信通道，为您打造一张灵活、可靠、大规模的企业级云上网络。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/cen/product-overview/billing/)。 |
| 转发路由器TR | [转发路由器TR（Transit Router）](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)是地域范围内企业级核心转发网元，可为您转发同地域或不同地域的网络实例间的流量，并支持在地域内定义灵活的互通、隔离、引流策略，帮助您打造一张灵活、可靠、大规模的企业级互联网络。转发路由器实例是云企业网实例的重要组成部分。 | 收费，CEN重要组成部分，请参见CEN计费规则。 |
| Web应用防火墙WAF | [Web应用防火墙](https://help.aliyun.com/zh/waf/web-application-firewall-3-0/product-overview/what-is-waf)（Web Application Firewall，简称WAF）为您的网站或App业务提供一站式安全防护。WAF可以有效识别Web业务流量的恶意特征，在对流量清洗和过滤后，将正常、安全的流量返回给服务器，避免网站服务器被恶意入侵导致性能异常等问题，从而保障网站的业务安全和数据安全。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/waf/web-application-firewall-3-0/product-overview/billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| WAF 3.0 | WAF 3.0支持服务化接入，通过SDK模块化的方式集成在云产品的网关中，通过内嵌在网关中的SDK提取流量并进行检测和防护。该过程中，WAF不参与流量转发，避免因额外引入一层转发而带来各种兼容性和稳定性问题。详情参见[WAF 3.0与WAF 2.0对比](https://help.aliyun.com/zh/waf/web-application-firewall-2-0/product-overview/compare-waf-3-0-with-waf-2)。 |

## 安全性

### ALB WAF增强版

WAF 3.0为ALB提供一站式安全防护，可以有效识别Web业务流量的恶意特征，详情参见[ALB WAF版优势](https://help.aliyun.com/zh/slb/application-load-balancer/enable-waf-protection-for-alb)。

### VPC安全性

专有网络VPC具有安全可靠、灵活可控、灵活可用以及较强的可扩展性，详情参见[产品优势](https://help.aliyun.com/zh/vpc/product-overview/benefits)及[访问控制](https://help.aliyun.com/zh/vpc/access-control)。

### 跨账号网络实例授权

在转发路由器实例连接其他账号的网络实例前，需要其他账号的网络实例对转发路由器实例进行授权。授权说明及操作详情参见[跨账号网络实例授权](https://help.aliyun.com/zh/cen/user-guide/grant-permissions-on-a-network-instance-that-belongs-to-another-account)。

## 注意事项

### ALB使用限制

- ALB WAF版存在升级及地域等限制，详情参见[使用限制](https://help.aliyun.com/zh/slb/application-load-balancer/enable-waf-protection-for-alb)。
- ALB只支持挂载私网服务器，不支持挂载公网服务器。

### 转发路由器使用限制

在您使用CEN转发路由器产品前，请先了解产品限制，详情参见[使用限制](https://help.aliyun.com/zh/cen/product-overview/limits)。

### 白名单

#### ALB挂载IP类型后端服务器白名单

ALB跨地域挂载的后端服务器仅支持IP类型。ALB挂载IP类型服务器功能默认不开放，如需使用，请[提交工单](https://workorder-intl.console.aliyun.com/#/ticket/createIndex)申请。

#### CEN跨地域金牌线路白名单

CEN跨Region带宽使用金牌线路最快时延，**需要提交工单或者通过商务经理联系网络架构师**，进行开通。开通金牌最快时延，一般需要至少3天时间。

## 实施步骤

### 实施准备

- 已创建相关VPC并完成云上内部组网。
- 已阅读并了解方案架构及注意事项章节，完成白名单开通。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：45分钟。

### 操作步骤

请结合方案架构内容，根据实际情况选择操作步骤。

#### 交易所为ALB实例开启WAF

下文描述交易所创建及管理WAF增强版ALB实例主要步骤，更多详情参见[开通和管理WAF增强版](https://www.alibabacloud.com/help/zh/server-load-balancer/latest/alb-waf)。

##### 新购一个WAF增强版ALB实例

1. 登录[应用型负载均衡ALB控制台](https://slb.console.aliyun.com/alb)。
2. 在顶部菜单栏，选择实例所属的地域。
3. 在**实例**页面，单击**创建应用型负载均衡**。
4. 在**应用型负载均衡（按量付费）**购买页面，完成参数的配置，然后单击**立即购买**并根据提示完成支付。本文仅列出强相关项，其余参数的配置请参见[创建应用型负载均衡](https://www.alibabacloud.com/help/zh/server-load-balancer/latest/create-an-alb-instance#task-1999195)。**功能版本（实例费）**：选择**WAF增强版**。

##### 为已创建的ALB实例开启WAF防护

您可以将已创建的基础版或标准版ALB实例升级为WAF增强版。

1. 登录[应用型负载均衡ALB控制台](https://slb.console.aliyun.com/alb)。
2. 在顶部菜单栏，选择实例所属的地域。
3. 在**实例**页面，找到目标实例，选择以下任意一种方式开启WAF防护。**方式一**：将鼠标悬停在目标实例名称后的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8776581571/p973221.png)图标，然后在气泡框中单击**Web应用安全防护**区域的**开启防护**。**方式二**：在**操作**列选择![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8776581571/p973222.png)**> 升级功能版本**。**方式三**：单击目标实例ID，在**实例详情**页签，找到**基本信息**区域中的**WAF安全防护**，然后单击**开启防护**。**方式四**：单击目标实例ID，在**实例详情**页签，单击**安全防护**页签。然后单击**开启防护**。
4. 在**应用型负载均衡（按量付费） | 变配**页面，选择**功能版本（实例费）**为**WAF增强版**，单击**立即购买**并完成支付。

##### 在ALB侧管理WAF防护

1. 登录[应用型负载均衡ALB控制台](https://slb.console.aliyun.com/alb)。
2. 在顶部菜单栏，选择实例所属的地域。
3. 管理WAF防护。**操作****步骤****查看实例是否开启WAF防护**选择以下任意一种方式查看实例是否开启WAF防护。**方式一**：在**实例**页面，找到目标实例，将鼠标悬停在实例名称后的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8776581571/p973223.png)图标，在气泡框的**Web应用安全防护**区域，查看防护状态。**方式二**：在**实例**页面，找到目标实例，单击实例ID。在**实例详情**页签，在**基本信息**区域查看**WAF安全防护**的状态。**方式三**：在**实例**页面，找到目标实例，单击实例ID。在**实例详情**页签，单击**安全防护**页签，在**Web应用安全防护**区域查看防护状态。**查看WAF安全报表**查看WAF安全报表，请确保您的ALB实例已开启WAF防护。**方式一**：在**实例**页面，找到目标实例，将鼠标悬停在实例名称后的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8776581571/p973224.png)图标，在气泡框的**Web应用安全防护**区域，单击**查看WAF安全报表**进入[WAF 3.0控制台的安全报表页面](https://yundunnext.console.aliyun.com/?p=wafnew#/waf/cn-hangzhou/report/web)查看。**方式二**：在**实例**页面，找到目标实例，单击实例ID。在**实例详情**页签，在**基本信息**区域单击**WAF安全防护**右侧的**查看WAF安全报表**进入[WAF 3.0控制台的安全报表页面](https://yundunnext.console.aliyun.com/?p=wafnew#/waf/cn-hangzhou/report/web)查看。**方式三**：在**实例**页面，找到目标实例，单击实例ID。在**实例详情**页签，单击**安全防护**页签，在**Web应用安全防护**区域查看防护状态。更多信息，请参见[安全报表](https://www.alibabacloud.com/help/zh/web-application-firewall/latest/security-report#task-2382775)。**关闭WAF防护**关闭WAF防护后，ALB实例上的业务流量将不再受WAF防护，安全报表中也不再包含相关业务流量的防护数据。**重要** ALB实例上的业务流量不受WAF防护后，WAF侧不会产生请求处理费。但您已经配置的防护规则仍会产生对应的功能费。建议您在取消业务接入前，先删除已配置的防护规则，避免产生额外计费。更多信息，请参见[计费项](https://www.alibabacloud.com/help/zh/web-application-firewall/latest/waf-3-0-billing-method#section-ok0-fal-hyn)、[防护模块概览](https://www.alibabacloud.com/help/zh/web-application-firewall/latest/protection-configuration-overview#section-vzg-9rd-qpm)。**方式一**：在**实例**页面，找到目标实例，将鼠标悬停在目标实例名称后的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8776581571/p973225.png)图标，在气泡框的**Web应用安全防护**区域，单击**关闭waf防护**；或在目标实例**操作**列选择![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8776581571/p973226.png)**> 升级功能版本**。在**应用型负载均衡（按量付费）| 变配**页面，选择**功能版本（实例费）**为**标准版**，单击**立即购买**并完成支付。**方式二**：在**实例**页面，找到目标实例，在**操作**列选择![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8776581571/p973227.png)**> 升级功能版本**。在**应用型负载均衡（按量付费）| 变配**页面，选择**功能版本（实例费）**为**标准版**，单击**立即购买**并完成支付。**方式三**：在**实例**页面，找到目标实例，单击实例ID。在**实例详情**页签，在**基本信息**区域单击**WAF安全防护**右侧的**关闭waf防护**。在**应用型负载均衡（按量付费）| 变配**页面，选择**功能版本（实例费）**为**标准版**，单击**立即购买**并完成支付。

#### 交易所ALB跨VPC挂载服务器

交易所可使用ALB跨VPC挂载后端服务器，详情参考[使用ALB挂载跨地域VPC内的服务器](https://www.alibabacloud.com/help/zh/server-load-balancer/latest/add-vpc-connected-backend-servers-to-an-alb-instance-across-regions)，根据实际情况进行操作。

#### 投资客户与交易所使用云企业网实现跨账号VPC互通

本步骤描述投资客户如何与交易所使用CEN-TR进行对接组网，投资客户下单系统所在VPC的交换机可用区需要与交易所API属于同一地域可用区，具体步骤可参考[使用云企业网实现跨地域跨账号VPC互通](https://help.aliyun.com/zh/cen/getting-started/use-enterprise-edition-transit-routers-to-connect-vpcs-across-regions-and-accounts)。

#### 投资客户CEN跨地域专线

本步骤描述投资客户创建跨地域连接并申请金牌线路主要操作步骤。

##### 使用企业版转发路由器创建跨地域连接

已完成跨地域组网的情况下请忽略本步骤**。**更多详情参见[使用转发路由器创建跨地域连接](https://www.alibabacloud.com/help/zh/cloud-enterprise-network/latest/manage-cross-region-connections-cross-region-connections#section-9yi-a1v-b5u)。

1. 登录[云企业网管理控制台](https://cen.console.aliyun.com/)。
2. 在**云企业网实例**页面，找到目标云企业网实例，单击目标实例ID。
3. 在云企业网实例详情页面，您可以通过以下两种方式，进入**连接网络实例**页面，创建跨地域连接。**说明** 如果您未在目标地域创建过转发路由器实例，请选择第一种方式创建您的跨地域连接，在您创建跨地域连接的过程中，系统自动帮您创建转发路由器实例。在**基本信息 > 带宽包管理**页签，单击**设置跨地域带宽**。在**基本信息 > 转发路由器**页签，找到目标转发路由器实例，在**操作**列单击**创建网络实例连接**。
4. 在**连接网络实例**页面，配置跨地域连接信息，然后单击**确定创建**。**配置项****说明****实例类型**选择**跨地域**。**地域**要互通的地域。**转发路由器**要互通的地域下的转发路由器实例。如果当前地域下您暂无转发路由器实例，系统默认为您自动创建。**连接名称**跨地域连接名称。名称长度为2~128个字符，以大小写字母或中文开头，可包含数字、下划线（_）或短划线（-)。**对端地域**要互通的对端地域。**转发路由器**要互通的对端地域下的转发路由器实例。如果当前地域下您暂无转发路由器实例，系统默认为您自动创建。**带宽分配方式**转发路由器实例支持以下带宽分配方式：**从带宽包分配**：从已经购买的带宽包中分配带宽。**按流量付费**：按照跨地域连接实际使用的流量计费。**说明** 首次使用**按流量付费**的带宽分配方式，您需要在控制台弹出的**提示**对话框中开通CDT服务，依据网络互通情况，分为：Cloud Data Transfer（跨境）服务Cloud Data Transfer（非跨境）服务**带宽包实例**选择已绑定的带宽包实例。如果您选择了**从带宽包分配**的带宽分配方式，请配置该项。**带宽**输入跨地域连接的带宽值。单位：Mbps。如果您选择了**从带宽包分配**的带宽分配方式，该配置项表示跨地域连接的带宽峰值。如果您选择了**按流量付费**的带宽分配方式，该配置项表示跨地域连接的限速带宽值。**高级配置**创建跨地域带宽时，系统默认帮您选中以下三种高级功能：**自动关联至转发路由器的默认路由表**开启本功能后，跨地域连接会关联至转发路由器的默认路由表，转发路由器会通过默认路由表转发跨地域间的流量。**自动传播系统路由至转发路由器的默认路由表**开启本功能后，跨地域连接会将系统路由传播至转发路由器的默认路由表中。**自动发布路由到对端地域**开启本功能后，即允许跨地域连接将本端地域转发路由器的路由自动传播至对端转发路由器的路由表中，用于网络实例跨地域互通。**说明**如果您不希望使用默认高级功能，您可以取消选中默认高级功能，后续手动关联路由表并设置路由学习关系。具体操作，请参见[关联转发](https://www.alibabacloud.com/help/zh/cloud-enterprise-network/latest/associated-forwarding#task-1964718)和[路由学习](https://www.alibabacloud.com/help/zh/cloud-enterprise-network/latest/route-learning#task-1964718)。跨地域连接只支持与转发路由器的默认路由表建立关联转发关系。

##### 通过商务经理联系阿里云工程师进行CEN金牌线路打标测试

按照注意事项章节中的白名单描述，完成金牌线路白名单开通。

## 源代码

- 创建WAF增强版ALB可参考[Terraform代码](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/terraform-modules/terraform-alicloud-landing-zone-alb/examples/create-public-alb)。
- CEN跨账号加载VPC可参考[Terraform代码](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/terraform-modules/terraform-alicloud-landing-zone-cen-vpc-attach/examples/add-vpc-attachment)。
- 路由配置可参考[CEN路由Terraform代码](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/terraform-modules/terraform-alicloud-landing-zone-cen-custom-route/examples/add-routing-entries)及[VPC路由Terraform代码](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/terraform-modules/terraform-alicloud-landing-zone-vpc-custom-route/examples/add-routing-entries)。

## 故障排除

### 应用型负载均衡ALB常见问题

应用型负载均衡问题请参见[常见问题](https://www.alibabacloud.com/help/zh/server-load-balancer/latest/alb-faq)。

### Web应用防火墙常见问题

Web应用防火墙问题请参见WAF[常见问题](https://www.alibabacloud.com/help/zh/web-application-firewall/latest/faq)。

### 云企业网CEN常见问题

云企业网问题请参见CEN[常见问题](https://www.alibabacloud.com/help/zh/cloud-enterprise-network/latest/differences-between-cen-and-express-connect)。

## 相关内容

- [ALB功能特性](https://www.alibabacloud.com/help/zh/server-load-balancer/latest/features-and-limits-of-different-editions#concept-2021067)
- [为ALB实例开启WAF防护](https://www.alibabacloud.com/help/zh/web-application-firewall/latest/cloud-product-access-alb#task-2538763)
- [WAF 3.0与WAF 2.0对比](https://www.alibabacloud.com/help/zh/web-application-firewall/latest/v3-vs-v2#task-2260089)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-132（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
