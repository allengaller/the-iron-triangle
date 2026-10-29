<!-- source: https://help.aliyun.com/zh/well-architected/solution-124 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929453 -->

# 企业级ACK搭建自动化

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7586581571/p972672.png)

当企业开通ACK容器服务并创建集群时，需要同时创建如VPC，交换机，NAT网关等一系列资源实例。同时，创建ACK容器集群需要选择诸多参数并安装基础组件，增加了手动创建的复杂性。

本文档介绍了一种通过[Terraform](https://www.terraform.io/)，自动在当前账号内快速创建ACK集群的方法。

## 方案优势

### 基础设施代码化

基于IaC思想，将ACK集群创建和配置过程使用[Terraform](https://www.terraform.io/)规范化，保证创建的集群统一并且包含基础的企业级配置（包括多可用区、节点日志收集和监控等），简化了手动创建集群操作。

## 客户场景

### 云上创建ACK集群

#### 场景描述

企业因业务发展，需要在云上创建ACK集群。

#### 适用客户

- 需要在云上自动化创建ACK集群，对集群有一定高可用性、可观测性要求的企业客户。

## 方案架构

本方案使用Terraform自动化执行，创建一个VPC并在其中部署一个ACK Pro版集群。为保证高可用，该集群使用[Terway](https://help.aliyun.com/zh/ack/product-overview/terway)的网络架构，并将节点部署在不同的可用区（至少两个）。该方案会在VPC下创建NAT网关并配置SNAT规则作为网络出口，同时会为集群安装[ALB Ingress Controller](https://help.aliyun.com/zh/ack/product-overview/alb-ingress-controller)用于处理Internet请求。集群上的节点、控制平面和ingress日志均会存储在[SLS服务](https://help.aliyun.com/zh/sls/what-is-log-service)中，并安装[Prometheus监控](https://help.aliyun.com/product/122122.html)组件实现监控。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7586581571/p972676.png)

### ACK集群默认配置

除了在实施时配置的参数外，本方案创建的ACK托管版集群的其他配置如下所示。

| **配置类别** | **配置名称** | **配置值** |
| --- | --- | --- |
| 集群配置 | 集群名称 | enterprise-ack |
| 集群类型 | [ACK Pro版](https://help.aliyun.com/zh/ack/overview-of-ack-pro-clusters) |  |
| 集群付费方式 | 按量付费 |  |
| 容器运行时 | containerd 1.5.13 |  |
| 网络插件 | [Terway](https://help.aliyun.com/zh/ack/product-overview/terway) |  |
| kube-proxy代理模式 | IPVS |  |
| Secret落盘加密 | 否 |  |
| 集群本地域名 | cluster.local |  |
| 集群删除保护 | 是 |  |
| 节点池名称 | enterprise-ack-node-pool |  |
| 操作系统 | Alibaba Cloud Linux |  |
| 安全加固 | 否 |  |
| 存储插件 | [CSI](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/csi-overview-1/) |  |
| 使用Prometheus监控服务 | 是 |  |
| 日志插件 | logtail-ds，日志存储在名为k8s-log-{ClusterID}的Project下。 |  |
| 创建Ingress Dashboard | 是 |  |
| 控制平面组件日志 | 是，采集[apiserver, kcm, scheduler]的日志，保存30天。 |  |
| 安装node-problem-detector并创建[事件中心](https://help.aliyun.com/zh/sls/create-and-use-an-event-center) | 是 |  |
| 安全巡检插件 | security-inspector |  |
| 定时巡检 | 未设置 |  |
| 安全组 | 企业级安全组 |  |
| Ingress | ALB Ingress，详细见[文档](https://help.aliyun.com/zh/ack/product-overview/alb-ingress-controller) |  |
| 网络配置 | VPC名称 | enterprise-ack-vpc |
| 交换机名称 | enterprise-ack-node/pod-vswitches |  |
| NAT实例名称 | enterprise-ack-nat-gateway |  |
| NAT实例类型 | Enhanced |  |
| NAT付费模式 | 按量付费 |  |
| EIP名称 | enterprise-ack-eip |  |
| EIP付费模式 | 按量付费 |  |
| EIP流量付费 | 按使用流量计费 |  |
| EIP线路类型 | BGP（多线） |  |

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 容器服务ACK | [阿里云容器服务ACK（Alibaba Cloud Container Service for Kubernetes）](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/product-overview/what-is-ack)提供高性能的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理，让您轻松高效地在云端运行Kubernetes容器化应用。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/ack/billing-information)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 负载均衡SLB | [负载均衡SLB（Server Load Balancer）](https://help.aliyun.com/product/27537.html)是一种对流量进行按需分发的服务，通过将流量分发到不同的后端服务来扩展应用系统的服务吞吐能力，并且可以消除系统中的单点故障，提升应用系统的可用性。 | 收费，详情参见[ALB产品计费](https://help.aliyun.com/zh/slb/application-load-balancer/billing-overview)，[SLB产品计费](https://help.aliyun.com/zh/slb/classic-load-balancer/product-overview/billing-overview/) |
| 公网NAT网关 | [公网NAT网关（NAT Gateway）](https://help.aliyun.com/zh/nat-gateway/user-guide/public-network-nat-gateway)是一款针对公网访问的企业级安全网关产品，具有高性能、自动弹性、灵活计费、精细化运维等特性，可以帮助您更好地管理公网访问流量。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/nat-gateway/nat-gateway-billing) |
| 弹性公网IP | [弹性公网IP（Elastic IP Address，简称EIP）](https://help.aliyun.com/product/61789.html)是可以独立购买和持有的公网IP地址资源。当EIP和云资源绑定后，云资源可以通过EIP与公网通信。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/eip/product-overview/billing) |
| Prometheus监控 | [阿里云Prometheus监控](https://help.aliyun.com/product/122122.html)全面对接开源Prometheus生态，支持类型丰富的组件监控，提供多种开箱即用的预置监控大盘，且提供全面托管的Prometheus服务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/prometheus/product-overview/pro-edition/) |
| 日志服务SLS | [日志服务SLS](https://help.aliyun.com/zh/sls/what-is-log-service)是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/sls/billing-overview) |
| 专用网络VPC | [专有网络VPC（Virtual Private Cloud）](https://help.aliyun.com/product/27706.html)是用户基于阿里云创建的自定义私有网络, 不同的专有网络之间二层逻辑隔离，用户可以在自己创建的专有网络内创建和管理云产品实例 | 免费 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| [节点池](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/node-pool-overview/) | 节点池是集群中具有相同配置的一组节点，节点池可以包含一个或多个节点。创建集群时指定的节点数和配置将成为默认节点池，您可以向集群添加其他不同大小和类型的节点池。您可以创建和升级节点池而不会影响整个集群。 |
| [Terway](https://help.aliyun.com/zh/ack/product-overview/terway) | Terway是阿里云开源的基于专有网络VPC的容器网络接口CNI（Container Network Interface）插件，支持基于Kubernetes标准的网络策略来定义容器间的访问策略。您可以通过使用Terway网络组件实现Kubernetes集群内部的网络互通。 |

更多容器服务与原生Kubernetes名词对照，可以参考[官方链接](https://help.aliyun.com/zh/document_detail/113088.html)。

## 安全性

### 容器服务ACK服务角色

首次使用容器服务ACK时，需要为服务账号授予系统默认角色。当且仅当该角色被正确授予后，容器服务才能正常地调用相关服务（ECS，OSS、NAS、SLB等），创建集群以及保存日志等。关于容器服务默认角色的名称和对应的功能权限，请参见[容器服务默认角色说明](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/ack-default-roles)。

### 节点池Worker Ram角色

ACK集群在创建Worker时会自动生成一个名为`KubernetesWorkerRole-xxxx`的RAM角色，并将该角色绑定到节点池中的ECS实例上，更多信息请参见[实例RAM角色](https://help.aliyun.com/zh/ecs/user-guide/attach-an-instance-ram-role-to-an-ecs-instance)。

### VPC安全性

专有网络VPC具有安全可靠、灵活可控、灵活可用以及较强的可扩展性，详情参见[产品优势](https://help.aliyun.com/zh/vpc/product-overview/benefits)及[访问控制](https://help.aliyun.com/zh/vpc/access-control)。

## 注意事项

### 容器服务ACK产品限制

使用阿里云容器服务ACK产品前，需要注意相关产品使用限制。详细可以查看[官方帮助](https://help.aliyun.com/zh/ack/product-overview/limits)。

### 弹性公网IP使用限制

使用弹性公网IP（Elastic IP Address，简称EIP）前，请先了解EIP的[使用限制](https://help.aliyun.com/zh/eip/product-overview/limits)。

### NAT网关使用限制

NAT网关在产品功能和服务性能上的限制，以及如何申请更高配额，详情参见[使用限制](https://help.aliyun.com/zh/nat-gateway/user-guide/public-network-nat-gateway)。

### ALB使用限制

应用型负载均衡ALB在使用时存在限制，包括地域和可用区，详细参见[使用限制](https://help.aliyun.com/zh/slb/application-load-balancer/quotas-and-limits)。

## 实施步骤

### 实施准备

- 确保已安装并配置好Terraform环境，所需的Terraform版本需要大于等于0.13。
- 确保在「当前账号」ECS控制台下，存在一个「密钥对」。在后续的步骤中，我们将使用该密钥对。
- 确保在「当前账号」RAM控制台下，存在一个「子用户」并持有其AccessKey和SecretKey，且该子用户拥有以下权限。在后续的步骤中，我们将使用该子用户的AK和SK。**权限名称****权限描述**AliyunVPCFullAccess用于创建供ACK集群使用的VPC和交换机AliyunNATGatewayFullAccess用于创建NAT网关并配置Snat规则AliyunEIPFullAccess用于创建NAT所使用的EIPAliyunECSFullAccess用于创建密钥对以及查询指定标签下的资源AliyunCSFullAccess用于创建ACK集群和相应节点池AliyunLogFullAccess用于存储ACK集群日志
- 确保在「当前账号」下，已经开通[容器服务ACK Pro版](https://help.aliyun.com/zh/ack/overview-of-ack-pro-clusters)、[日志服务SLS](https://help.aliyun.com/product/28958.html?spm=5176.55536.J_5834642020.5.64ea6bf6516xrA)以及[Promethus监控服务](https://help.aliyun.com/product/122122.html?spm=5176.18083541.J_3817677460.5.61b04593aVu2iy)，并已授权创建相关服务角色。

**注意:**若创建ACK集群时提示`AliyunOOSLifecycleHook4CSRole`角色未找到，可参考「管理节点池」[文档](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-a-node-pool)中的「调整期望节点数」模块中的第4步-「授予CS获取云资源的权限」完成授权。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：15分钟。

### 操作步骤

#### 配置参数

本步骤配置创建ACK集群所需参数，若已配置参数可跳过该步骤。

1. 下载源代码中的代码包，解压到某个目录。目录结构可以参考附件中的解释。
2. 使用编辑器打开`terraform.tfvars`文件，修改文件内的配置信息。

| **分组名** | **中文名称** | **配置项名称** | **参考示例** | **配置项描述** |
| --- | --- | --- | --- | --- |
|  | AccessKey ID | alicloud_access_key | LTAI**************** | 在实施准备中具有对应权限的「子用户」AK和SK |
| AccessKey Secret | alicloud_secret_key | yourAccessKeySecret |  |  |
| 集群配置 | 地域 | region | cn-hangzhou | ACK集群所在的地域 |
| 时区 | timezone | Asia/Shanghai | ACK集群所使用的时区 |  |
| VPC CIDR | vpc_cidr | 192.168.0.0/16 | ACK集群所在的VPC网段 |  |
| Node VSW | node_vswitches | [{cidr = "192.168.0.0/19"zone_id = "cn-hangzhou-h"},{cidr = "192.168.64.0/19"zone_id = "cn-hangzhou-g"}] | 集群Node所使用的交换机，所填项包括交换机的**网段**和**可用区**。**注意：**为保证集群的**高可用**，强烈建议为Node创建**两个及以上**且处在**不同可用区**的交换机。 |  |
| Pod VSW | pod_vswitches | [{cidr = "192.168.32.0/19"zone_id = "cn-hangzhou-h"},{cidr = "192.168.96.0/19"zone_id = "cn-hangzhou-g"}] | 集群Pod所使用的交换机。**注意：**Pod Vswitches和Node Vswitches需要处于**相同的可用区**。 |  |
| EIP带宽 | eip_bandwidth | 10 | EIP的最大带宽 |  |
| Service CIDR | service_cidr | 172.21.0.0/20 | ACK集群Service所用的网段，注意**不可与VPC网段重合**。 |  |
| Kubernetes版本 | ack_version | 1.24.6-aliyun.1 | ACK集群的版本，仅允许最新的两个版本 |  |
| API Server访问 | load_balancer_spec | slb.s1.small | 为API Server创建的SLB实例规格 |  |
| 节点池配置 | 系统盘类型 | system_disk_category | cloud_essd | 节点系统盘类型，可选值`cloud_ssd`，`cloud_efficiency`和`cloud_essd` |
| 数据盘类型 | data_disk_category | cloud_essd | 节点数据盘类型，可选值`cloud_ssd`，`cloud_efficiency`和`cloud_essd` |  |
| 系统盘大小 | system_disk_size | 40 | 节点数据盘大小，可选值`40-500`GB |  |
| 数据盘大小 | data_disk_size | 40 | 节点数据盘大小，可选`40-32768`GB |  |
| 期望节点数量 | desired_size | 3 | 节点池期望节点数量，后续可在容器控制台上调整。 |  |
| 实例规格 | worker_instance_types | [ "ecs.c5.xlarge" ] | 节点池允许创建的实例规格，在创建节点时，将从第一个规格开始尝试，直到创建成功。最多可选**10**种实例规格。 |  |
| 密钥对 | key_pair_name | test-key-pair | 在实施准备中创建的「密钥对」名称 |  |

#### 运行Terraform代码

1. 参数配置完成后，通过命令`terraform init`下载aliyun Provider并初始化Terraform环境。
2. 使用命令`terraform plan`查看部署计划，并使用`terraform apply`命令完成部署。
3. 部署成功后，将打印ACK集群id，也可登录到容器控制台，查看对应的ACK实例。

#### 执行结果

1. 在Terraform代码执行完成后除了容器控制台的集群实例，我们也可以登录到sls控制台对应的Log Project中查看相关的日志数据。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7586581571/p972671.png)
2. 在日志服务「智能运维」- 「K8s事件中心」中可以看到对应集群的事件中心。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7586581571/p972673.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7586581571/p972674.png)
3. 在Prometheus监控实例中，也可以查看到创建的ACK集群信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7586581571/p972677.png)

## 源代码

## 代码介绍

源代码中包含ACK搭建自动化的Terraform示例实现代码，包括创建VPC、交换机、NAT、EIP、ACK Pro版集群等内容，需要结合代码与本文内容完成ACK搭建自动化。

## 代码地址

[ack-managed-cluster.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260302/gbrnya/ack-managed-cluster.zip)

## 故障排除

### 执行Terraform代码时提示xxx角色未找到？

ACK容器服务在创建集群和节点池时，依赖账号中许多RAM服务角色，其中大部分角色在进入容器控制台时已经创建。`AliyunOOSLifecycleHook4CSRole`角色并未创建，需要在创建节点池时手动进行授权。可在[文档](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-a-node-pool)中「调整期望节点数」板块，第四步「授权CS获取云资源的权限」中，点击对应的链接进行授权。

### Prometheus监控中为什么显示“未找到相关监控大盘”？

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7586581571/p972675.png)

出现原因：节点池中node内存过小，可在事件中心中查看。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7586581571/p972678.png)

解决方案：

1. 修改节点池规格信息，通过扩缩容/修改节点池中节点实例规格，变更节点配置。
2. 在完成后，等待2min左右即可查看到监控大盘。

## 方案卸载

因为相关实例开启了删除保护，无法直接使用`terraform destroy`命令进行回滚，在删除前需要在控制台上关闭对应资源实例的删除保护设置。同时，删除集群并不会删除相关日志和监控实例，需要到相关控制台上手动删除。

1. 前往「容器服务控制台」，在对应容器右侧的「操作」栏目下，点击「更多」-「修改集群删除保护状态」，关闭集群删除保护。
2. 使用`terraform destroy`命令删除创建的资源。
3. 前往「日志服务控制台」删除对应的Project，并进入K8s事件中心，删除对应的事件中心。
4. 前往「Prometheus监控控制台」卸载对应的Prometheus监控实例。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-124（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
