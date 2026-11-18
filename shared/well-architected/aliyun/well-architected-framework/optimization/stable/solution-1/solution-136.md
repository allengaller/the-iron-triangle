<!-- source: https://help.aliyun.com/zh/well-architected/solution-136 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929502 -->

# 面向多套容器集群的网络规划方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2776581571/p973207.png)

当企业计划使用多套容器集群（ACK）时，需要提前规划好专有网络VPC、虚拟交换机、Pod网段CIDR（地址段）和Service CIDR（地址段）。借助云企业网CEN和转发路由器的能力可以实现不同账号内的VPC网络连通。进而实现不同容器集群内的Pod相互调用。

本方案会提供面向多账号多套容器集群的网络规划建议，包括容器集群内的服务暴露建议。通过这篇方案能够指导客户合理规划好集群网络。

## 方案优势

### 弹性可扩展的容器网络设计

结合Landing Zone多账号最佳实践，企业可以将不同业务部署在不同云账号内的容器集群。通过提前规划好不同账号及各个账号内的VPC网络，可以设计出一套面向企业级的可扩展容器网络架构。

### 灵活组网

[转发路由器TR](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)支持自定义路由策略，满足企业级组网需求。例如：实现不同安全域隔离、**统一隔离区DMZ（Demilitarized Zone）出口**、搭建安全服务链（Service Chaining）等复杂的组网架构。控制台提供基于地理位置和基于网络资源的可视化管理界面，您可以通过可视化管理界面快速查看同地域和跨地域组网拓扑，帮助您迅速掌握全网运行状态，提高网络运维效率。

## 客户场景

### 多账号多套集群，且集群内网需互通

#### 场景描述

客户有多个账号，并且每个账号内都会部署容器集群。需要实现跨账号的容器集群网络互通。

#### 适用客户

- 使用资源目录管理云上多个账号的企业客户。
- 使用多个容器集群来部署业务。
- 需要打通多个容器集群的内网连接。

### 混合云场景，实现容器网络与线下IDC网络互通

#### 场景描述

计划使用容器上云的客户，部分业务往云上容器进行部署，需要实现云上容器与线下服务互通。

#### 适用客户

- 使用容器上云的企业客户。
- 从IDC往云上迁移的混合云客户。

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2776581571/p973206.png)

### 网络规划

在阿里云环境下使用ACK支持的Kubernetes集群，首先需要根据业务场景、集群规模进行网络规划。您可以按下表进行规划（未包含场景，请根据实际需要自行调整）。

#### VPC网络规划

| **集群节点规模** | **目的** | **VPC规划** | **可用区** |
| --- | --- | --- | --- |
| 小于100个节点 | 一般性业务 | 单VPC | 1个 |
| 任意 | 需要多可用区 | 单VPC | 2个及以上 |
| 任意 | 对可靠性有极致要求、需要多地域 | 多VPC | 2个及以上 |

#### Terway容器网络规划（可依据自身业务适当调整，仅供参考）

建议将容器集群Node节点与Pod节点所对应的交换机分开配置，参考示例：

| **专有网络网段** | **虚拟交换机网段** | **Pod虚拟交换机网段** | **最大可分配Pod地址数** |
| --- | --- | --- | --- |
| 192.168.0.0/16 | 可用区I 192.168.0.0/19 | 192.168.32.0/19 | 8192 |
| 可用区J 192.168.64.0/19 | 192.168.96.0/19 | 8192 |  |

Service CIDR规划：172.21.0.0/20

注意：规划VPC地址的时候要避免出现IP地址重叠。

### 服务选择

集群里面需要提供4层负载服务建议使用SLB的来做Service。 具体可以查看[官网链接](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/considerations-for-configuring-a-loadbalancer-type-service-1)。

集群里面需要提供7层以及服务很多需要共用同一个入口来节省成本的推荐用ingress。具体可以查看[官网链接](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/ingress-management-2/)。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 专有网络VPC | [专有网络VPC](https://help.aliyun.com/product/27706.html)（Virtual Private Cloud）是用户基于阿里云创建的自定义私有网络, 不同的专有网络之间二层逻辑隔离，用户可以在自己创建的专有网络内创建和管理云产品实例，比如ECS、SLB、RDS等。 | 免费 |
| 云企业网CEN | [云企业网](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)可帮助您在不同地域专有网络VPC（Virtual Private Cloud）之间、VPC与本地数据中心间搭建私网通信通道，实现同地域或跨地域网络互通；同时，云企业网支持在地域内定义灵活的互通、隔离、引流策略，帮助您打造一张灵活、可靠、大规模的企业级全球互联网络。 | 免费 |
| 转发路由器TR | [转发路由器TR](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)（Transit Router）提供连接网络实例、添加自定义路由表、添加路由条目、添加路由策略等丰富的网络互通和路由管理功能。本文为您介绍企业版和基础版转发路由器工作原理。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/cen/product-overview/billing-rules)。 |
| 容器集群（ACK） | 阿里云容器服务Kubernetes版是全球首批通过Kubernetes一致性认证的服务平台，提供高性能的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理，让您轻松高效地在云端运行Kubernetes容器化应用。 | 收费，详情参见[官网链接](https://help.aliyun.com/zh/ack/billing-information)。 |
| PrivateZone | [PrivateZone](https://help.aliyun.com/zh/document_detail/64611.html)，是基于阿里云专有网络VPC（Virtual Private Cloud）环境的私有DNS服务。该服务允许您在自定义的一个或多个VPC中将私有域名映射到IP地址。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/document_detail/71338.html)。 |
| ALB | [应用型负载均衡ALB](https://help.aliyun.com/zh/slb/application-load-balancer/what-is-alb)（Application Load Balancer）是阿里云推出的专门面向HTTP、HTTPS和QUIC等应用层负载场景的负载均衡服务，具备超强弹性及大规模应用层流量处理能力，并提供最高99.995%的SLA可用性保障。ALB具备处理复杂业务路由的能力，与云原生相关服务深度集成，是阿里云官方提供的云原生Ingress网关。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/slb/application-load-balancer/billing-overview)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| Terway网络 | [Terway网络](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/network/)模式采用的是云原生的网络方案，直接基于阿里云的虚拟化网络中的弹性网卡资源来构建的容器网络。 |
| Service | 由于云原生的应用，通常需要敏捷的迭代和快速的弹性，且单一容器和其相关的网络资源的生命非常短暂，所以需要固定的访问地址，以及自动负载均衡实现快速的业务弹性。ACK采用[Service](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/network/)方式为一组容器提供固定的访问入口，并对这一组容器做负载均衡。 |
| Ingress | [Ingress](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/ingress-management-2/)是集群内Service对外暴露7层的访问接入点。您可以通过Ingress资源来配置不同的7层的转发规则。 |

## 安全性

### VPC安全性

专有网络VPC具有安全可靠、灵活可控、灵活可用以及较强的可扩展性，详情参见[产品优势](https://help.aliyun.com/zh/vpc/product-overview/benefits)及[访问控制](https://help.aliyun.com/zh/vpc/access-control)。

### 跨账号网络实例授权

在转发路由器实例连接其他账号的网络实例前，需要其他账号的网络实例对转发路由器实例进行授权。授权说明及操作详情参见[跨账号网络实例授权](https://help.aliyun.com/zh/cen/user-guide/grant-permissions-on-a-network-instance-that-belongs-to-another-account)。

## 注意事项

### 地域限制

转发路由器分为基础版和企业版。企业版转发路由器是基础版转发路由器的升级版，除包含基础版转发路由器的所有功能外，还支持定义灵活的路由策略。企业版转发路由器支持的地域和可用区可参考[产品链接](https://help.aliyun.com/zh/cen/product-overview/what-is-cen/)。

## 实施步骤

### 场景规划

本文会介绍两个场景的实施步骤：

- 场景1：跨账号同地域容器集群通过转发路由器组网，验证两个集群内Pod连通性。
- 场景2：通过PrivateZone来配置域名解析，实现ECS调用容器集群内的服务。

### 实施准备

- 请提前规划好各个账号内VPC及Vswitch的网段。具体操作，请参见[创建和管理专有网络](https://help.aliyun.com/zh/vpc/create-and-manage-a-vpc)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 场景一：跨账号同地域容器集群通过转发路由器组网，验证两个集群内Pod连通性

##### 数据规划

| 账号 | VPC名称 | VPC段 | Vswitch段 | 备注 | ServiceIP |
| --- | --- | --- | --- | --- | --- |
| 账号A | VPC1 | 10.0.0.0/16 | 10.0.0.0/24 | Node节点 | 172.16.0.0/20 |
| 10.0.16.0/20 | Pod节点 |  |  |  |  |
| 账号B | VPC2 | 192.168.0.0/16 | 192.168.0.0/24 | Node节点 | 172.16.16.0/20 |
| 192.168.16.0/20 | Pod节点 |  |  |  |  |

说明：

- 为了简化配置，Vswitch没有将连接TR的单独出来，而是跟业务公用一个。
- 为了简化配置，云企业网也是直接部署在账号A内。而没有单独开一个共享账号。

##### 架构图

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2776581571/p973204.png)

##### 配置云企业网和转发路由器

1. 登录账号A，配置云企业网。操作见[官方文档](https://help.aliyun.com/zh/cen/user-guide/cen-instances-1)。
2. 配置转发路由器，添加VPC连接，操作见[官方文档](https://help.aliyun.com/zh/cen/user-guide/connect-vpcs/)。这一步，将VPC1添加到TR里面。
3. 配置VPC跨账号网络实例授权登录账号B，完成跨账号网络实例授权。操作见[官方文档](https://help.aliyun.com/zh/cen/user-guide/grant-permissions-on-a-network-instance-that-belongs-to-another-account)。需要完成VPC2的跨账号授权。
4. 切换到账号A，继续配置转发路由器，添加VPC连接，操作见[官方文档](https://help.aliyun.com/zh/cen/user-guide/connect-vpcs/)。这一步完成将VPC2添加到TR。配置完成之后TR的截图：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2776581571/p973205.png)完成这步操作之后，登录VPC1与VPC2的网络完成打通。

##### 在VPC1与VPC2内分别创建ACK集群，验证POD网络连通性

1. 登录账号A，选择VPC1网络，创建ACK集群。具体可以参考 [开通ACK](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/getting-started/getting-started-overview)。
2. 登录账号B，选择VPC2网络，创建ACK集群。具体可以参考 [开通ACK](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/getting-started/getting-started-overview)。
3. 分别在账号A与账号B内的集群创建POD。参考指令：`apiVersion: apps/v1 
kind: Deployment
metadata:
 name: nginx-deployment-basic
 labels:
 app: nginx
spec:
 replicas: 1
 selector:
 matchLabels:
 app: nginx
 template:
 metadata:
 labels:
 app: nginx
 spec:
 containers:
 - name: nginx
 image: nginx:1.7.9 
 ports:
 - containerPort: 80
 resources:
 limits:
 cpu: "500m"`

登录到A账号内的容器POD中ping 另外一个账号B中的容器IP，可以发现能够正常PING通。

注意：如果有TCP\UDP等其他协议网络互通需求，需要配置集群安全组策略，允许对端访问。

#### 场景二：通过PrivateZone来配置域名解析，实现ECS调用容器集群内的服务

##### 数据规划

| 账号 | VPC名称 | VPC段 | Vswitch段 | 备注 | ServiceIP |
| --- | --- | --- | --- | --- | --- |
| 账号A | VPC1 | 10.0.0.0/16 | 10.0.0.0/24 | Node节点 | 172.16.0.0/24 |
| 10.0.16.0/20 | Pod节点 |  |  |  |  |
| VPC3 | 172.16.0.0/12 | 172.29.192.0/20 | 部署ECS | ECS主机：172.29.196.3 |  |

##### 架构图

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2776581571/p973208.png)

##### 把VPC3添加到转发路由器

在场景1的基础环境内，把VPC3添加到转发路由器。这样可以确保在VPC2内的主机访问到私有SLB地址。

1. 登录账号A，配置转发路由器，添加VPC连接，操作见[官方文档](https://help.aliyun.com/zh/cen/user-guide/connect-vpcs/)。这一步，将VPC3添加到TR里面。

##### 在账号A内的ACK集群上创建服务并配置域名

1. 在ACK容器集群上执行如下指令：`apiVersion: v1
kind: Service
metadata:
 name: my-service1 
 annotations:
 service.beta.kubernetes.io/alibaba-cloud-loadbalancer-address-type: intranet
 labels:
 app: nginx-svc
spec:
 selector:
 app: nginx 
 ports:
 - protocol: TCP
 name: http
 port: 80 
 targetPort: 80
 type: LoadBalancer`执行完这段指令返回的SLB地址：10.0.0.XX
2. 在账号A的PrivateZone中配置域名解析[添加Zone及PrivateZone解析记录](https://help.aliyun.com/zh/document_detail/64628.html)[关联/解关联VPC](https://help.aliyun.com/zh/document_detail/64629.html)参考截图：配置解析记录![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2776581571/p973209.png)

##### 在VPC3上的ECS主机PING测试

登录VPC3上的ECS发起PING 测试可以看到网络能够正常解析并可达。

```
[root@iZbp1h0edwd7 ~]# ping helloworld.ack.hz.lz.com
PING helloworld.ack.hz.lz.com (10.0.0.XX) 56(84) bytes of data.
64 bytes from 10.0.0.XX (10.0.0.XX): icmp_seq=1 ttl=101 time=1.27 ms
```

## 故障排除

### CEN常见问题

CEN常见问题详情参见[常见问题](https://help.aliyun.com/zh/cen/support/faq)。

### VPC常见问题

VPC常见问题详情参见[常见问题](https://help.aliyun.com/zh/vpc/support/faq)。

### ECS实例间ping不通的排查思路

ECS实例ping不通可以参见[排查思路](https://help.aliyun.com/zh/document_detail/185314.html)。

## 相关内容

- [基于CEN-TR实现企业级云上互联](https://help.aliyun.com/zh/well-architected/solution-19)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-136（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
