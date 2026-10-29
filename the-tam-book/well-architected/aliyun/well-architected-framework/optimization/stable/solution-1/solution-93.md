<!-- source: https://help.aliyun.com/zh/well-architected/solution-93 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929510 -->

# 与三方监管机构网络互联方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0876581571/p973256.png)

我们面对传统大B客户，例如金融机构、医疗、制造类企业，较多的存在多DC互联地址冲突问题。例如金融机构与三方监管机构上报数据，监管机构需指定分配访问地址，医院/药店与医保局地址规划问题，拉专线后地址冲突问题等等。该方案即针对上述场景，利用阿里云VPC 私网NAT网关来实现云上云下地址冲突互访、监管机构指定通讯IP等方案，让云上企业客户轻松应对监管挑战。

## 方案优势

### 满足与监管机构对接诉求

使用指定地址与对接机构对接，满足对接机构限定地址互访的需求。通过阿里云标准VPC NAT及转发路由器产品能力，解决了金融机构与三方监管机构通过NAT转换来满足监管机构的互联地址管理要求，支撑云上企业客户与三方监管机构的业务互联场景。

### 安全隔离

业务和对接地址管理隔离，业务系统地址无需向外部机构暴露，避免被攻击。

### 管理更简单

VPN、专线等多种私网连接方式接入统一私网入口网关，便于监控及运维管理。

## 客户场景

### 使用指定地址与监管机构对接

#### 场景描述

云上VPC与三方金融等监管机构互联场景下，**应监管机构网段要求，存在如下两个需求：**

1. 阿里云侧需支持公网私用地址。
2. 阿里云侧需完成云上VPC源地址转换成监管分配的地址。

#### 适用客户

需要使用指定地址与监管机构对接的企业客户。

### 使用指定地址与云上云下通信

#### 场景描述

企业内部网络进行多云或IDC互通，需要指定地址互访，对接多云对端只希望加白有限地址，需要使用指定地址作为源地址访问。因地址冲突通过VPC NAT交付的标准方案，同时不限于金融与三方机构互联，也可以适用于企业客户上云与IDC互联、云服务与线下IDC打通，如果有类似**网段冲突或者限制的**客户场景。

#### 适用客户

存在网段冲突、需要使用指定地址与其它云或IDC互访的企业客户。

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0876581571/p973262.png)

使用[VPC NAT网关](https://help.aliyun.com/zh/nat-gateway/user-guide/what-is-a-vpc-nat-gateway)对云上VPC网段做NAT源地址映射，转换成监管提供的地址访问IDC，满足IDC正常回包给云上的要求完成通信。图示中箭头为业务访问方向，包含访问及回包路径。配置NAT网关后需要进行路由配置，方案中涉及访问节点1为VPC默认**系统路由表**，节点2为NAT所在的**子网路由表**，节点3为**VBR路由表。**

### VPC NAT网关

#### 使用建议

- VPC NAT网关要求您在创建时选择VPC，并且需要指定VPC内的交换机。为了便于路由配置，建议您使用独立交换机。
- NAT IP地址是在SNAT功能或DNAT功能中用于源或目的地址转换的IP地址。VPC NAT网关创建成功后，系统会使用VPC NAT网关所在交换机的网段作为默认NAT IP地址段，使用默认NAT IP地址段中的一个IP地址作为默认NAT IP地址。您可以在默认地址段中添加NAT IP地址，也可以新建地址段并添加NAT IP地址。

#### SNAT及DNAT

由于当前单个VPC NAT仅能实现源地址转换SNAT或目的地址转换DNAT，若客户需求同时存在SNAT和DNAT需求，故从项目交付的简易程度简易，有如下建议：

- 部署两个独立的SNAT网关和DNAT网关，同时需要利用CEN-TR的静态路由能力来实现流量的引流。
- 云上到线下DC仅做SNAT，线下到云上利用DC的路由器或者防火墙等硬件设备来实现DNAT。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云企业网 | [云企业网CEN（Cloud Enterprise Network）](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)是运行在阿里云私有全球网络上的一张高可用网络。云企业网通过转发路由器TR（Transit Router）帮助您在跨地域专有网络之间，专有网络与本地数据中心间搭建私网通信通道，为您打造一张灵活、可靠、大规模的企业级云上网络。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/cen/product-overview/billing/)。 |
| 转发路由器TR | [转发路由器TR（Transit Router）](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)提供连接网络实例、添加自定义路由表、添加路由条目、添加路由策略等丰富的网络互通和路由管理功能。本文为您介绍企业版和基础版转发路由器工作原理。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/cen/product-overview/billing/)。 |
| NAT网关 | [阿里云NAT网关（NAT Gateway，简称NAT）](https://help.aliyun.com/zh/nat-gateway/product-overview/what-is-nat-gateway)提供公网NAT和私网NAT两种功能。公网NAT网关通过自定义SNAT、DNAT规则可为云上服务器提供对外公网服务、及主动访问公网能力；私网NAT网关(也即[VPC NAT网关](https://help.aliyun.com/zh/nat-gateway/user-guide/what-is-a-vpc-nat-gateway))可使VPC内的ECS实例通过私网地址转换服务，实现VPC与VPC之间、及VPC与线下IDC互访能力。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/nat-gateway/pricing/)。 |
| 专有网络VPC | [专有网络VPC（Virtual Private Cloud）](https://help.aliyun.com/zh/vpc/what-is-vpc)是您专有的云上私有网络。您可以完全掌控自己的专有网络，例如选择IP地址范围、配置路由表和网关等，您可以在自己定义的专有网络中使用阿里云资源，如云服务器、云数据库RDS和负载均衡等。 | 本身免费，详情参见[产品计费](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |

## 安全性

### 对接安全

方案中业务系统地址和监管对接地址管理隔离，业务系统地址无需向外部机构暴露，避免被攻击。

### NAT网关安全

NAT网关的SNAT功能具有安全防护的能力，只有当VPC内的ECS实例主动访问外部才可以建立连接进行通信，而外部无法主动访问VPC内的ECS实例。SNAT功能会屏蔽VPC内ECS实例对外的端口，保护VPC内的ECS实例免受外部的入侵和攻击，详情参见[产品优势](https://help.aliyun.com/zh/nat-gateway/product-overview/what-is-nat-gateway)。

### VPC安全性

专有网络VPC具有安全可靠、灵活可控、灵活可用以及较强的可扩展性，详情参见[产品优势](https://help.aliyun.com/zh/vpc/product-overview/benefits)及[访问控制](https://help.aliyun.com/zh/vpc/access-control)。

## 注意事项

### 白名单

#### 公网私用白名单

方案中涉及到公网私用，需要联系阿里云开白名单才能够实施，白名单主要包括：

- VPC User CIDR白名单，需要提供账号UID、VPC实例ID、需要加白的网段（例如88.88.1.0/24），提工单加白。
- VBR互联地址公网私用白名单，提工单加白。

## 实施步骤

本章内容主要以方案架构中**金融机构与三方监管机构互联为背景**，云上源地址转换（SNAT）功能的落地部署介绍。以下步骤为了验证可行性，建议先让客户**在测试VPC做实施验证**。

### 实施准备

- 确保客户已经创建VPC、云企业网转发路由器TR、VPC NAT等产品，并通过高速通道-物理专线与IDC已经完成内网互联。
- 本章节主要聚焦VPC NAT、高速通道VBR和TR等产品的配置，以上产品的购买、基础配置不再本章节赘述。
- 已按照注意事项中的描述**完成白名单添加**。
- 具体产品的购买和基础配置可参考以下最佳实践：[专线接入流程](https://help.aliyun.com/zh/express-connect/user-guide/process-of-creating-a-dedicated-physical-connection/)[创建独享专线连接](https://help.aliyun.com/zh/express-connect/user-guide/classic-mode)[本地IDC通过专线访问云服务器](https://help.aliyun.com/zh/express-connect/use-cases/connect-a-data-center-to-ecs-by-using-an-express-connect-circuit)[CEN-TR转发路由器快速入门](https://help.aliyun.com/zh/cen/user-guide/upgrade-to-the-latest-cen-console-version)

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 实施步骤

#### 添加VPC附加网段

登录[VPC控制台](https://vpc.console.aliyun.com/vpc/)，在要与监管机构连通的VPC详情页面添加附加公网私用的网段，本示例输入88.88.0.0/16。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0876581571/p973263.png)

#### 创建VPC NAT网关

1. 使用已添加的附加网段，在要与监管连通的VPC中新建一个交换机，本示例交换机网段为88.88.1.0/24。
2. 新建VPC NAT网关，选择刚创建的交换机作为网关所属交换机。
3. 在VPC NAT网关中添加NAT IP，本示例填写88.88.1.1，作为要访问监管机构的目的地址。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0876581571/p973257.png)

#### 创建SNAT条目

1. 登录[NAT网关管理控制台](https://vpc.console.aliyun.com/nat)。
2. 在左侧导航栏，选择**NAT网关 > VPC NAT网关**。
3. 在顶部菜单栏，选择VPC NAT网关的地域。
4. 在**VPC NAT网关**页面，找到目标VPC NAT网关实例，然后在**操作**列单击**SNAT管理**。
5. 在**SNAT管理**页签，单击**创建SNAT条目**。具体可参考官网文档的[创建SNT条目部分](https://help.aliyun.com/zh/document_detail/270909.html)，“SNAT条目粒度”可以选择“自定义网段粒度”，具体配置监管机构提供的网段。**源地址****SNAT映射后地址****说明**SNAT规则172.16.1.0/24172.16.2.0/24NAT IP 88.88.1.1/32通过NAT-VPC完成源地址转换；NAT IP实际可自定义![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0876581571/p973264.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0876581571/p973258.png)

#### 配置VPC系统路由表

1. 参考下表路由配置，在要与监管机构连通的VPC**系统路由表**中增加**两条自定义路由条目**。具体操作可参考官网文档的[创建自定义路由](https://help.aliyun.com/zh/vpc/user-guide/create-and-manage-route-table)部分。注意：这里需要添加白名单，请参考注意事项章节中的白名单申请**路由表****网段明细****下一跳****说明**业务VPC系统路由表88.88.1.2/32NAT网关去NAT所在路由表做源地址转换88.88.1.1/32NAT网关备注：发布到TR监管机构IDC回包路由![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0876581571/p973265.png)
2. 将该IDC回包路由条目88.88.1.1/32发布到CEN-TR。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0876581571/p973261.png)

#### 配置VPC自定义路由表

1. 在与监管连通的VPC下**新建自定义路由表**。具体操作可参考[创建自定义路由表](https://help.aliyun.com/zh/vpc/network-traffic-management-using-custom-routing-tables)。
2. 将下述路由条目添加到新建的自定义路由表中。**路由表****网段明细****下一跳****说明**业务VPC自定义NAT路由表88.88.1.2/32杭州TR-att1访问VBR
3. 将自定义路由表绑定到NAT网关所在交换机，具体操作可参考[绑定交换机和自定义路由表](https://help.aliyun.com/zh/vpc/network-traffic-management-using-custom-routing-tables)。

#### 配置VBR路由

在边界路由器VBR下添加自定义路由，并将该路由发布到转发路由器TR。

注意：这里需要添加白名单，请参考注意事项章节中的白名单申请

| **路由表** | **网段明细** | **下一跳** | **说明** |
| --- | --- | --- | --- |
| VBR路由表 | 88.88.1.2/32 | 专线实例：pc-xxx备注：发布到TR | 去IDC路由 |

#### 方案验证

接下来结合路由从流量流转的角度做推演验证，实际环境验证VPC下ECS测试连通性

##### 去向流量路径

1. 云上ECS访问线下监管机构的目的地址88.88.1.2/32, VPC系统路由表中添加一条自定义路由88.88.1.2/32下一跳为NAT网关，所以经过系统路由表目的地址是88.88.1.2/32的请求会先被路由到NAT网关
2. 经过NAT转换后，源地址变为NAT IP 88.88.1.1，属于VPC NAT所在交换机网段，请求到达NAT网关交换机。
3. NAT网关交换机路由表添加目的地址为88.88.1.2/32，下一跳为TR。
4. TR会根据路由表中从CEN学习到的路由条目，将目的地址是88.88.1.2/32的请求路由指向VBR。
5. VBR根据路由表将请求转发到专线，继而到达IDC。

##### 回包流量路径

1. IDC根据本地上云路由将回包（回包目的地址是NAT转换后的地址，属于VPC的网段）请求转发到VBR。
2. VBR根据从TR同步过来的路由，TR转发路由器，将请求转发到VPC，请求到达VPC内NAT网关交换机，根据本地路由找到VPC网段内的NAT网关。**路由表****网段明细****下一跳****说明**业务VPC系统路由表Ecs Vsw:172.16.1.0/2488.88.1.1/32NATgw备注：发布到TRIDC回包路由
3. 根据NAT网关根据SNAT的映射条目，将回包报文返回给VPC ECS，往返链路全部打通。

##### 访问验证

在要访问监管机构的业务VPC中的业务VSwitch（172.16.1.0/24）下新建一台ECS，访问监管机构IP测试连通性。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0876581571/p973266.png)

## 故障排除

### 配置VPC路由表公网私用路由报错

请按照注意事项中的说明，申请添加白名单。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0876581571/p973267.png)

## 相关内容

- [使用VPC NAT网关实现VPC地址冲突时的互相访问](https://help.aliyun.com/zh/document_detail/304433.html)
- [VPC NAT网关联动VPN网关实现云上与云下私网互访](https://help.aliyun.com/zh/nat-gateway/use-a-vpc-nat-gateway-and-a-vpn-gateway-to-connect-a-data-center-and-a-vpc)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-93（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
