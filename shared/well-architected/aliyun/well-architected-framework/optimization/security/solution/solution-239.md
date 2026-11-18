<!-- source: https://help.aliyun.com/zh/well-architected/solution-239 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929411 -->

# 云原生容器安全防护

基于阿里云云原生服务构建完整的安全体系，遵循CNCF云原生安全技术要求和最佳实践，结合阿里云多种安全控制措施，形成云原生容器安全防护的最佳实践。

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971776.png)

整体分为三部分：

- 基础设施安全：基础设施安全是构建容器集群所需的云产品的安全；
- 容器生命周期安全：容器生命筑起分为开发、分发、部署三个阶段的安全控制措施；
- 容器运行时安全：容器运行时分为工作负载层面和应用层面的运行时安全；

### 容器全生命周期定义

云原生环境下的生命周期管理是指云环境中管理、监控和弹性扩展工作负载的技术、实践和流程。生命周期管理由四个连续阶段组成：开发、版本分发（CI）、部署和运行（CD）。每个阶段都在安全的工作负载执行的基础上推进了前一个阶段的工作。

### 供应链安全定义

供应链安全可分为两部分：为创建应用程序使用的工具和服务（如开发工具）的安全，以及构成应用程序本身的组件（如库、依赖项和镜像）的安全。

供应链的实现根本在于供应链本身的完整性是可验证的，软件开发中，供应链产生的组件需要进行签名来验证来源。除此之外，上游的依赖包将不可避免地包含安全漏洞，所以组织在使用 第三方依赖 时必须谨慎。验证所使用的第三方软件包的真实性和完整性，对于确保依赖项符合预期，不带来额外的安全威胁至关重要。

供应链安全核心要解决的是第三方依赖包、制品、镜像的完整性；

安全提供的核心能力即为：

- 容器镜像的签名验签；
- 容器镜像的安全扫描；

### CNCF推荐的安全基线

利用安全基线（如 NIST Application Security Container Guide、Center for Internet Security(CIS)、NIST Security Strategies for microservices、OpenSCAP）为开发团队和组织提供创建"默认安全"的工作负载的指南。采用和实施这些基准，使团队能够对使用安全基线进行加固的工作负载进行测试。然而，这些安全基线没有考虑到实际企业的业务场景和实际需求。安全从业人员应将这些基线作为指南而不是清单来执行。

### 从攻击视角看云原生容器环境遇到的安全威胁

黑客对云原生服务和云资源的攻击路径示意：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971780.png)

在云原生容器环境内从攻击视角看黑客利用的攻击手段：（参考ATT&CKframework）

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971777.png)

本文档则介绍了针对阿里云云原生容器环境，如何构建一套满足合规，抵御入侵，解决CNCF提到的各类安全风险的容器安全防护架构。

## 方案优势

### 原生化的安全能力集成

- 在原生容器安全架构中，安全能力打散为原子化能力，嵌入到云原生产品中，形态上更加的原生化；
- 相比传统外挂式的安全控制措施而言，安全阻力更小；

### 更便捷的操作和运维

- 安全能力的开通、部署、维护、弹性等相比于第三方和传统安全组件更加可控、边界；
- 更符合云环境，安全能力融入业务流程中，更容易部署和推广；

### 更全面丰富的安全功能

- 云原生容器安全框架和体系相对完整，覆盖从开发、分发、部署、运行时等容器生命周期各阶段的安全能力；
- 覆盖ATT&CK for 容器安全的攻击链矩阵，阿里云云安全中心提供100%覆盖防护；
- 参照CNCF的安全要求，实现了全面覆盖；
- 从基础安全到容器安全 每个层面都有对应的最佳实践；

## 客户场景

### 供应链安全需求

#### 场景描述

供应链安全可分为两部分：为创建应用程序使用的工具和服务（如开发工具）的安全，以及构成应用程序本身的组件（如库、依赖项和镜像）的安全。

供应链的实现根本在于供应链本身的完整性是可验证的，软件开发中，供应链产生的组件需要进行签名来验证来源。除此之外，上游的依赖包将不可避免地包含安全漏洞，所以组织在使用 第三方依赖 时必须谨慎。验证所使用的第三方软件包的真实性和完整性，对于确保依赖项符合预期，不带来额外的安全威胁至关重要。

供应链安全核心要解决的是第三方依赖包、制品、镜像的完整性；

安全提供的核心能力即为：

- 容器镜像的签名验签；
- 容器镜像的安全扫描；

#### 适用客户

企业级、互联网等客户，关注容器供应链安全、容器制品安全、镜像安全控制的客户。

### 容器环境的敏感信息管理需求

#### 场景描述

容器环境的敏感信息包含了AKSK、Secret、登录口令等，在容器环境中，访问ACR镜像仓、pod内配置文件硬编码的密钥需要有安全的保护措施。

主要需求是面向敏感信息的管理，包含：

- 容器secret加密；
- 容器凭据安全使用；
- 落盘加密；
- 敏感信息配置扫描；

#### 适用客户

企业级、互联网等客户；

### 容器运行时防护需求

#### 场景描述

容器运行时可细分为三大部分，分别是运行时的基础环境、容器运行时、和运行时应用安全三大部分，在这个场景下，容器会面临来自互联网的大量网络攻击，在MITRE ATT&CK攻防矩阵中，专门为容器攻防罗列了一项攻击矩阵，可见容器运行时的网络攻击的严重。

在容器运行时的安全防护需求主要集中在以下三部分：

- 容器运行时拉起的云资源、云环境的基础安全建设；
- 容器运行时runtime的安全防御、检测和响应能力；
- 容器运行应用的应用层安全；

#### 适用客户

企业级、互联网等客户；

## 客户案例

### 客户背景

某海外公司X，专为全球资本市场提供独立信用评级、指数服务、风险评估、投资研究和数据服务，在业内一向处于领先地位。

### 客户痛点（或客户诉求）

在阿里云有20多个注册账号，根据账号职能不同，对账号下资源的合规要求也不同。资源托管云上的情况下，很难构建统一的CMDB中心和日志中心。无法中心化的进行整个体系的合规测评、监督和改进。在面对等保法规时，20多个账号要作为一个信息系统应对检测，这非常繁琐且成本巨大。

### 实施方案

- 使用资源目录进行多账号统一管理。
- 使用配置审计对不同账号强制实施不同的合规基线。
- 使用配置审计对等保2.0充分预检。

可以添加客户实施方案架构图进行说明

### 客户收益

- 中心化的对多账号进行合规管控，将操作日志和配置快照归集到统一地址。
- 实施合规基线并能够持续监控云上多账号下IT系统的合规性。
- 帮助客户加速通过等保2.0三级测评。

## 方案架构

云原生容器安全整体框架如下图所示

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971781.png)

整体分为三部分：

- 基础设施安全：基础设施安全是构建容器集群所需的云产品的安全；
- 容器生命周期安全：容器生命筑起分为开发、分发、部署三个阶段的安全控制措施；
- 容器运行时安全：容器运行时分为工作负载层面和应用层面的运行时安全；

### 基础设施安全

当创建一套标准的ACK集群时，所需要的云资源架构如下图所示：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971783.png)

阿里云容器相关的基础设施资源

| 云资源 | **作用** | **ACK托管版** | **ACK专属版** | **ACKserverless** |
| --- | --- | --- | --- | --- |
| ECS（master） | •ACK集群master节点 |  | √ |  |
| ECS（worker） | •ACK集群worker节点 | √ | √ |  |
| Ingress(ALB/MSE/Nignx) | •Ingress路由网关 | √ | √ | √ |
| CLB(APIserver) | •为APIserver提供访问负载，有公网和私网两种形式 | √ | √ | √ |
| NATgateway(SNAT) | •为ACK集群及Pod集群提供出向访问 | √ | √ | √ |
| EIP | •绑定在CLB和NAT网关上 | √ | √ | √ |
| pod | •容器负载，运行业务 | √ | √ | √ |
| CEN | •当私网环境访问ACR或访问APIserver时，通过CEN转发 | √ | √ | √ |
| VPC | •创建ACK集群时会绑定的VPC，并绑定相关安全组 | √ | √ | √ |

这些基础资源之上，云原生ACK的基础设施安全架构应该遵循一下安全策略进行建设：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971779.png)

- **WAF：开启ALB ingress WAF ；**
- **边界云防火墙：防护暴露在互联网的ALB IP、CLB IP、NAT IP；**
- **VPC防火墙：防护来自CEN过来的流量；**
- **容器安全：开启防护pod容器运行时安全；**
- **主机安全：开启防护Node节点主机安全；**
- **堡垒机：提供Node节点的4A安全；**

### 容器生命周期安全

容器的生命周期遵循CNCF的定义分为开发、分发、部署、Runtime阶段，不同阶段的安全需求和最佳实践不同。我们将分别从分发、部署、Runtime阶段介绍阿里云原生的安全能力。

#### 分发阶段安全控制措施

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971778.png)

分发阶段最重要的安全控制是针对镜像本身的，从镜像的CIA，机密性、完整性和可用性分别做防护。

**重点在于镜像的安全扫描和镜像签名。**

**其次是对ACR镜像仓库的访问控制。**

#### 部署阶段安全控制措施

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971785.png)

"部署"阶段负责安排一系列的"执行前"检查，以确保即将部署的应用程序在运行时能符合并遵守本组织的安全和合规性策略。

在部署之前，各组织应核实以下几方面是否到位、适用性以及当前状况：

- **镜像签名及完整性**
- **镜像运行策略（如没有恶意软件或严重的漏洞）**
- **容器运行策略（如无过度权限）**
- **主机安全漏洞和合规性控制**
- **工作负载、应用程序和网络安全策略**

#### Runtime安全阶段控制措施

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971782.png)

**作负载和编排这个层面包含了ACK集群和pod runtime，在整个容器运行时的安全策略中，提供更多地入侵防御能力。在这个阶段的安全控制措施如下：**

- **IAM（RAM）：RAM授权对象是ACK集群的运维操作，包含集群、节点池、集群监控等；**
- **RBAC ：这里更多的是kubernetes应用的运维操作，如工作负载、ingress、存储、namespace、secrets等；**
- **RRSA：实现Pod维度的OpenAPI权限隔离；**
- **容器防逃逸：检测runtime状态下的容器安全威胁；**
- **容器运行时入侵检测和防御：检测runtime状态下容器是否存在webshell、病毒、等入侵行为，从进程、网络及恶意文件（围绕ATT&CK for containers）；**
- **容器恶意文件的病毒查杀：检测恶意病毒；**
- **容器防火墙：做pod间网络隔离；**
- **容器文件防御：提供容器文件防篡改；**
- **ALB ingress WAF：为运行时的容器上层应用提供7层入侵防护；**
- **SNAT Firewall：为runtimes环境提供出向的互联网访问控制；**
- **ACK Secrets Management：通过KMS提供关键凭据的加密保护；**

### 容器应用安全

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971784.png)

**在应用层面，防护更加聚焦在了业务层面，和云原生及容器的安全架构没有强依赖关系，主要为以下安全控制措施：**

- **Network Access ：通过互联网防火墙实现网络隔离，谁有权限访问该应用，设定相关ACL；**
- **DDOS protection：对外业务考虑部署DDOS来解决4层、7层网络流量攻击，提高业务系统的可用性；**
- **API security：基于WAF的API安全模块实现API安全检测；**
- **Network Encryptaion：业务系统开启SSL协议加密，若通过WAF，则在WAF也要开启SSL加密认证，同时确保SSL版本大于1.2；**
- **WAF：在部署阶段已经基于ALB ingress构建了WAF；**

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云安全中心旗舰版 | 本文档提到的关键安全控制措施，是依赖云安全中心旗舰版相关功能（旗舰版不包含容器镜像漏洞扫描），如果您的云安全中心版本未升级至旗舰版，则需要完成版本升级或者购买。 |  |
| 云安全中心镜像漏洞扫描授权 | 容器镜像漏洞扫描是云安全中心的增值功能，无需依赖云安全中心的任意版本，但仅限于对容器镜像的漏洞、配置和敏感信息做扫描。在本文档中，建议购买旗舰版的同时，再购买镜像漏洞扫描授权，实现镜像漏洞的扫描。 |  |
| KMS | 本文档中涉及容器镜像签名、ACK保密字典安全、凭据安全等，需要依赖KMS3.0订阅版本。 |  |
| WAF | 本文档中的最佳实践涉及开启ingress WAF，该实践需要开启WAF3.0。 |  |
| CFW | 本文档中关于基础设施安全部分，会采用NAT防火墙、VPC防火墙以及互联网边界防火墙实现容器基础设施部分的安全管控。 |  |
| 堡垒机 | 本文档中关于基础设施安全部分，会采用堡垒机实现对于Node节点的管控。 |  |
| DDOS | 本文档中关于基础设施安全部分，会采用DDOS实现应用层稳定性的需求。 |  |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |

## 实施步骤

### 实施准备

### 确认开通的云产品或云服务

实施以下安全控制措施前，需要确认企业客户的基础环境条件，在完成如下策略创建时，需要开通如下云产品：

| **需要开通的云产品** | **云产品版本** | **备注** |
| --- | --- | --- |
| ACR | 企业版 |  |
| ACK | pro、托管版 |  |
| 云安全中心 | 旗舰版 | 仅旗舰版支持容器安全相关的防护能力 |
| KMS | KMS3.0 | 镜像签名和Secret保护需要开通KMS，并且需要KMS具备密钥和凭据两个授权。并开通KMS共享能力，使得成员账号可以共享设置KMS |
| 云防火墙 | 企业版 | 构建ACK基础设施安全的产品 |
| 云WAF | waf3.0 | 构建ACK基础设施安全的产品 |
| 堡垒机 | 企业双擎版 | 构建ACK基础设施安全的产品 |
|  |  |  |

#### 确认账号资源部署

按照Landing Zone推荐账号架构进行部署，已完成下列部署：

| 账号类型 | 部署内容 |
| --- | --- |
| 业务账号 | 开通并创建VPC开通并创建ACR开通并创建ACK开通并创建云安全中心开通并创建WAF |
| 共享服务账号 | 配置CEN，加载网络实例、与业务账号网络连通。 |
| 安全账号 | 开通并创建云防火墙开通并创建堡垒机开通并创建KMS |

#### 部署清单

推荐部署内容及详细说明如下：

| 板块 | 部署账号 | 部署内容 |
| --- | --- | --- |
| 网络规划 | 共享服务账号 | 创建云企业网CEN，开通转发路由器TR服务通过云企业网转发路由器CEN-TR进行云上组网，配置网络互通路由构建公网统一出口构建单Region双可用区应用架构共创建DMZ VPC（1个）、EIP（3个）、VSwitch（4台）、NAT网关（1个）、ALB（1个）、ECS（2台）、安全组（1个） |
| 开发测试账号 | 构建单Region双可用区应用架构进行VPC云企业网跨账号授权共创建开发测试VPC（ 1个）、EIP（2个）、VSwitch（4台）、ALB、ECS（2台）、安全组（ 1个） |  |
| 生产账号 | VPC中配置云企业网跨账号授权创建生产VPC（ 1个）、VSwitch（4台） |  |
| 合规审计 | 企业管理账号 | 使用云治理中心完成配置审计及操作审计开通，所有成员账号资源配置及变更数据投递到日志账号中的SLS及OSS使用云治理中心启用操作审计多账号跟踪，所有成员账号操作日志投递到日志账号中的SLS及OSS启用内置合规包的自动化代码示例 |
| 日志账号 | 开通SLS及OSS服务，并进行配置及操作日志存储 |  |

### 操作步骤

#### 步骤一：配置容器安全漏洞扫描

1. **开通ACR镜像安全扫描**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971789.png)详细操作，请参考[容器镜像安全扫描](https://help.aliyun.com/zh/acr/user-guide/scan-container-images)。**推荐选择云安全扫描引擎，云安全扫描引擎支持系统漏洞的自动修复，Trivy仅支持系统漏洞和应用漏洞，对于恶意样本和基线检查都不支持扫描。**
2. **同时开通云安全中心的镜像扫描功能**云安全中心的产品分为两种形态，一种是订阅，一种是按量。其中我们要选择的镜像扫描是云安全中心的增值按量模块，计费类型为按量计费。购买如下图所示：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971786.png)**镜像安全扫描的开通不依赖任何云安全中心的版本，详细计费可参考**[计费概述](https://help.aliyun.com/zh/security-center/billing-overview)。
3. **创建定时扫描任务，对ACR镜像仓进行镜像漏洞扫描**如果使用的是阿里云ACR镜像仓企业版，则在开通ACR和云安全中心后，无需对接，即可实现漏洞扫描。在云安全中心创建镜像漏洞扫描任务。设置扫描周期。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971787.png)在配置镜像扫描任务的同时，检查基线配置策略![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971793.png)以及敏感文件扫描![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971788.png)
4. **确保ACR开启了内网专有网络连接**检查ACR镜像仓的访问控制，确保生成了内网IP，可以让云安全中心扫描到。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971790.png)否则云安全中心执行扫描任务会失败。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971795.png)
5. **执行镜像扫描，查看扫描结果**查看镜像仓内的镜像文件：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971791.png)查看云安全中心镜像扫描结果![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971792.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971797.png)返回镜像仓查看ACR侧的数据![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971794.png)点击详情![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971798.png)

#### 步骤二：配置容器镜像签名

1. **测试在未设置镜像签名时拉取镜像创建无状态容器**可以查看镜像仓1.2.24版本镜像的状态为未加签![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971799.png)创建无状态容器，如下配置所示![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971800.png)查看运行状态![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971805.png)
2. **配置ACK使用kritis-validation-hook组件初始化**文档参考[使用kritis-validation-hook组件实现自动验证容器镜像签名](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-kritis-validation-hook-to-automatically-verify-the-signatures-of-container-images)。具体实操如下：首先安装kritis-validation-hook组件![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971801.png)其次配置RAM的授权策略，授予访问kritis-validation-hook组件所需的权限。需要确保集群拥有运行kritis-validation-hook组件所需的访问权限。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971806.png)
3. **创建用于镜像签名的KMS密钥**在本测试环境中，KMS是多账号共享的资源，提前配置好KMS的共享账号。**注意创建的KMS密钥类型选择SIGN/VERIFY**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971802.png)
4. **配置云安全中心的容器签名验签功能**开通云安全中心旗舰版，选择容器签名服务。在容器签名服务中创建证明者，选择刚刚创建的KMS密钥![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971807.png)下一步创建签名策略，将选择哪些集群和命名空间去应用这个签名。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971808.png)
5. **为ACR的仓库配置镜像加签策略**可以创建一个单独的仓库用于验证镜像签名，同时配置镜像加签策略，选择刚刚创建的证明者。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971809.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971803.png)配置ACR访问KMS的授信策略和权限，打开RAM访问控制，找到或创建一个“AliyunContainerRegistryKMSRole角色”；并按照如下操作配置好相关权限关系：[使用容器镜像加签](https://help.aliyun.com/zh/acr/user-guide/use-container-image-to-sign)。可以对比下权限最后配置的结果：**resource处需要确认region和UID信息**`{
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "kms:*",
 "Resource": "acs:kms:cn-beijing:1787697688450187:*"
 }
 ],
 "Version": "1"
}`配置好后，可以看到新创建的仓库带有“已加签”的标记![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971810.png)此时我们向镜像仓库中上传一个镜像查看镜像状态，可以看到拉取的镜像状态显示已加签。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971804.png)
6. **验证在已加签的ACK命名空间下加载未加签镜像的结果**此时我们在配置了验签的namespace下（default）拉起一个镜像查看镜像状态：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971816.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971814.png)可以在test仓库查看1.2.24镜像的状态如下：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971811.png)此时创建容器，在控制台上能够看到直接创建失败：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971812.png)
7. **验证在已加签的ACK命名空间下加载加签镜像的结果**此时创建一个加了签名的镜像仓：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971813.png)选择镜像并查看镜像在仓库的加签状态：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971817.png)此时创建拉起这个镜像，并检查状态：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971818.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971819.png)

#### 步骤三：配置ACR访问控制策略

1. **设置ACR的网络访问方式**ACR镜像仓提供公网访问和专有网络访问两种途径，通常情况下建议使用专有网络访问的方式为ECS和ACK集群提供镜像仓链接；ACR的公网访问镜像仓地址默认不开放，用户需要手动开放。如图，当选择为专有网络链接时，需要关联一个VPC网络，ACR会占用一个IP地址用于和ECS及ACK集群之间的互联。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971820.png)当配置ACR为公网访问时，需要做好白名单访问控制，此处的域名无法加入WAF、CFW进行控制，为云产品自行控制的策略。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971815.png)
2. **设置ACR镜像仓的访问凭证**此处必须使用RAM user进行设置，RAM role将无法设置访问凭证。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971822.png)

#### 步骤四：ACK Secret加密保护设置

1. **为ACK集群创建加密的key**前置条件：开通KMS登录KMS创建用于加密ACK的key
2. **开启Secret落盘加密**创建ACK集群时，可以看到一些安全选项，如高级选项中，选择加密ACK Secret;建议使用KMS托管的Key进行数据加密。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971821.png)或在创建完成集群后，开启Secret落盘加密，注意此操作会重启集群。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971824.png)
3. **开启数据盘加密**建议开启数据盘落盘加密功能，使用KMS托管的key进行数据加密；![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971823.png)

#### 步骤五：配置容器相关的基线扫描策略

容器基线相关的策略整体分为两大部分：

- 容器操作系统基线
- 容器配置合规基线

其中容器操作系统基线的模板如下:

| 序号 | 内置基线名称 |
| --- | --- |
| 1 | 阿里云标准-Kubernetes-Master安全基线检查 |
| 2 | 阿里云标准-Kubernetes-Node安全基线检查 |
| 3 | 阿里云标准-Docker主机安全基线检查 |
| 4 | 阿里云标准-Jenkins安全基线检查 |
| 5 | Kubernetes(ACK) Master 国际通用安全最佳实践基线 |
| 6 | Kubernetes(ACK) Node 国际通用安全最佳实践基线 |
| 7 | Kubernetes(K8S) 安全策略 国际通用安全最佳实践基线 |
| 8 | Kubernetes(ACK) Pod 国际通用安全最佳实践基线 |
|  |  |

配置合规类基线包含：

- **镜像合规基线扫描：**通过镜像扫描工具，扫描镜像内的配置，包括了身份安全、未授权访问、弱口令、AKSK明文等扫描内容。同时会扫描敏感文件，包含令牌、密码、数据库文件、密钥等330种类型
- **云产品配置扫描：**通过CSPM工具，扫描阿里云ACR、ACK产品的默认基础配置，如是否开启加密、是否设置白名单等操作。

1. **配置容器操作系统基线检查策略**登录云安全中心（旗舰版），点击【基线检查】，点击【策略管理】创建一个针对K8s集群的容器操作系统基线，在基线分类中过滤【linux基线】找到容器安全，如下图：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971825.png)然后选择生效的服务器，并设定检测周期即可。
2. **配置容器镜像合规扫描**前置条件：需要单独购买容器漏洞扫描功能，详细购买说明参考，[开通功能](https://help.aliyun.com/zh/security-center/user-guide/enable-container-image-scan)。登录云安全中心，点击容器镜像扫描，进入扫描设置。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971826.png)配置基线和敏感文件，并执行定期扫描即可。
3. **使用CSPM云平台配置基线检查对K8s服务进行检测**前置条件：需要单独开通CSPM付费功能，详细购买说明参考，[云安全态势管理概述](https://help.aliyun.com/zh/security-center/user-guide/cspm)。开通后登录云安全中心，找到云平台配置检查，点击检查策略设置，找到阿里云安全最佳实践，选择容器和中间件![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971827.png)配置完成后，点击立即扫描，查看云产品配置扫描结果。

#### 步骤六：通过云安全中心配置容器镜像主动防御策略

容器镜像主动防御是在容器部署阶段设置的安全防御控制措施，目的是阻断恶意镜像的拉起，虽然我们在开发、分发阶段设置了容器的安全扫描和镜像签名，用于确保镜像本身的完整性和机密性，但仍存在一定的安全暴露面使得风险镜像被拉起。

如下图所示，我们假设一种场景：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971828.png)

当我们在开发和分发阶段设置了镜像安全的控制措施（签名和扫描）；

- 在T时刻上传镜像，并对镜像进行签名；
- T时刻落到镜像仓库中执行了扫描任务，此时发现了有漏洞；
- 漏扫的任务周期是3天，则下一次扫描是在T+3；
- 此时应用程序进入部署阶段，T+2时刻拉起镜像，此时拉起的就是一个有漏洞的镜像，或者在T+2 时刻，上传的镜像刚好没有被扫描任务执行，此时的镜像就变成了未扫描镜像；
- 应用运行后，就是带有漏洞的应用，成为了业务的暴露面；

所以解决镜像被拉起前的安全风险暴露窗口，最有效的就是在镜像部署阶段，拉起镜像前，部署安全关卡，如下图：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971832.png)

在部署前，增加云安全中心主动防御功能，设置策略模板，对未经安全扫描的镜像进行阻断（拉起），对存在漏洞或其他风险的镜像进行阻断。从而严格保障发布的应用在当前时刻是安全的。

详细配置和效果如下：

1. **设置ACK的安全策略开关**应用容器主动防御功能需要使用阿里云ACK集群。需要在ACK集群设置中开启安全策略。点击ACK集权，找到策略管理，开启安全策略管理。如下图。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971829.png)
2. **通过云安全中心设置容器主动防御策略**推荐的最佳实践是将未扫描镜像、有漏洞、恶意文件、敏感文件的风险项勾选，动作设置为阻断启动。如下配置截图：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971836.png)并将该配置应用到需要保护的集群中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971830.png)
3. **验证拉起有漏洞的镜像创建一个Deployment**检查镜像仓中有漏洞的镜像版本1.2.24![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971831.png)通过ACK创建一个该镜像的deployment![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971839.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971833.png)此时查看云安全中心，会有容器主动防御的告警![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971840.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971842.png)通过主动防御提高云原生容器生命周期的安全性。

#### 步骤七：通过容器策略治理（OPA）配置Pod安全策略

云原生服务ACK中，通过安全策略来管理创建Pod的一些安全及合规策略，提供一些准入安全策略，从而预先检查传入的请求是否违规，这里是指通过ACK创建一个Pod过程中，通过镜像或yaml部署Pod的策略检查。

但当前有一些限制：

- 仅适用于Linux节点。
- 当前不支持自定义策略规则，所有规则均来自于阿里云容器服务内置的规则库。

容器安全策略是需要安装Gatekeeper插件才能使用，具体参考[gatekeeper](https://help.aliyun.com/zh/ack/product-overview/gatekeeper)。

Gatekeeper准入控制器使用开放策略（OPA）的策略，提供了更多符合K8s应用场景的安全策略规则。借助ACK集群引入的Gatekeeper组件，您可以在容器服务控制台启用或自定义安全策略，验证Pod的部署和更新是否安全可控。

具体的配置操作详见最佳实践：[启用安全策略管理](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/configure-and-enforce-ack-pod-security-policies)。

1. **安装Gatekeeper**找到ACK对应集群，点击运维管理-->组件管理，找到Gatekeeper组件，点击安装![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971834.png)安装完成后，可在安全管理中，开启策略管理，可看到如下配置界面。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971835.png)
2. **设置Gatekeeper策略**在配置好对应的组件后，点击我的策略，进行一些策略的开启和处置动作的选择，这里目前无法支持自定义策略。在内置的策略中，和容器镜像相关的所有准入策略控制，都要依赖于云安全中心的主动防御功能，具体最佳实践详见步骤六-通过云安全中心配置容器主动防御的说明。我们以禁止在指定的namespace下创建Pod策略为例：可以看到策略的具体说明如下：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971843.png)配置好后点击确认，观察验证效果。
3. **验证安全策略效果**根据上述策略，在default命名空间下部署一个Pod，预期应该是被阻止的。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971837.png)创建结果是创建失败。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971838.png)

#### 步骤八：配置ACK托管版 Runtime运行时防入侵策略

容器运行时防护在云安全中心旗舰版是默认开启的状态，运行的容器都默认在云安全中心的入侵检测和防护范围内。需要用户确认是否所有的ACK集群都被云安全中心托管，以及云安全中心的防护开关是否开启。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971847.png)

查看详细的容器入侵防御模型：[安全告警概述](https://help.aliyun.com/zh/security-center/user-guide/overview-6)。

#### 步骤九：配置ACKserverless版 运行时入侵防御策略

1. **必要前提**当前仅支持防护阿里云弹性容器实例（ECI）资产，下文中的Serverless资产均指代弹性容器实例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6376581571/p971841.png)已运行的pod无法直接安装，需要重新创建pod进行安装；（此步骤需要和客户业务沟通确认）
2. **容器serverless部署工作**使用“镜像创建”工作负载；在应用基本信息的“注解”，添加以下信息：名称：annotations值：k8s.aliyun.com/eci-aliyundun-enabled: "true"![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971845.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971844.png)在“高级配置”pod的“注解”，添加以下信息：名称：k8s.aliyun.com/eci-aliyundun-enabled值：true ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971846.png)创建完成后查看应用详情pod状态：running点击其中一个pod的详细状态，可以查看到 注解：k8s.aliyun.com/eci-aliyundun-enabled：enable 正常。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971848.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971851.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971849.png)
3. **云安全中心侧的操作**在资产中心->serverless资产，点击“同步最新资产”后，可以看到已经同步出最新的pod资产，并且云安全中心客户端的状态为“正常” 状态，此时表明客户serverless资产的云安全中心运行正常。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971852.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971853.png)针对serverless资产的“威胁告警检测”和“漏洞扫描”等功能就可以在界面进行操作；

#### 配置十：为ALB ingress开启WAF保护

当我们创建ingress的时候，ACK提供了三个选项，每个选项开启WAF的方式不同，但从WAF的形态上区分，大致分为两类，一类是云原生WAF，适用于开启在ALB或ALB ingress上，另一类的代理型WAF，适合开启在其他ingress类型上。

| 类型 | Nginxingress | **ALBingress** | **MSEingress** |
| --- | --- | --- | --- |
| 区别 | •需要您自行运维，如果您对网关定制有强烈的需求，可以选择Nginx Ingress。 | •于阿里云应用型负载均衡ALB（Application Load Balancer），属于全托管免运维的云服务。单个ALB实例支持100万QPS，提供更为强大的Ingress流量管理功能。 | •基于阿里云MSE（Microservices Engine）云原生网关，属于全托管免运维的云服务。单个MSE云原生网关实例支持100万QPS，提供更为强大的Ingress流量管理功能。 |
| 应用场景 | •网关高度定制化。•云原生应用金丝雀发布、蓝绿发布。 | •网关全托管、免运维。•互联网应用七层高性能自动弹性。•云原生应用金丝雀发布、蓝绿发布。•超大QPS、超大并发连接。 | •网关全托管、免运维。•南北向、东西向流量统一管理，微服务网关，全链路灰度。•多个容器集群、PaaS平台、ECS服务共用一个网关实例。•混合云、多数据中心、多业务域的内部互通。•认证鉴权，灵活设置，安全防护要求高。•超大流量、高并发业务。 |
| 开启WAF方式 | •可以采用cname方式将业务转发到WAF•也可以使用混合云部署模式，将WAFSDK嵌入到Nginx | •推荐采用ALB云原生接入•也可以采用cname接入 | •采用cname接入 |

两种类别的WAF区别如下：

| 类型 | 云原生WAF | **传统cnameWAF** |
| --- | --- | --- |
| 接入方式 | •原生接入•WAF不参与转发•避免SSL版本修订的问题 | •Cname接入，修改DNS解析；•WAF参与网络转发；•存在SSL版本修订的问题 |
| 多账号 | •支持 | •不存在多账号管理；•通过DMZ或域名进行统一管理； |
| 防护效果 | •一致 | •一致 |

以下实践是为ALB ingress开通WAF的最佳实践说明

1. **开通WAF3.0**前置条件：需要开通WAF3.0，仅WAF3.0支持云产品原生防护，（可以使用按量或预付费类型）在同账号，或其他RD成员账号下开通WAF即可。
2. **创建ALB ingress时开启WAF**需要为ALB ingress创建controller配置文件修改指定edition为standardwithwaf相关配置参考[使用ALB WAF增强版实例保护服务](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/enable-waf-protection)。
3. **在WAF进行防护规则的配置**第二步设置好后，即可在WAF上进行关键域名、业务的防护配置。

#### 配置十一：通过云安全中心容器防火墙实现容器网络隔离

容器防火墙的实现逻辑如下图所示：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5376581571/p971850.png)

- 容器防火墙依赖云安全中心agent Alinet进程实现访问控制隔离；
- 通过配置ACL策略实现4层网络访问控制；
- 定义镜像、标签以及应用名称作为防护对象，实现基于对象的访问控制；

## 故障排除

### 为什么无法开通资源目录？

可能有如下两个原因：

- 当前账号没有进行企业实名认证。关于企业实名认证，请参见[企业实名认证](https://help.aliyun.com/zh/account/verify-your-identity-enterprise-account/)。
- 当前账号已经在资源目录内，无法重复开通。

### 什么样的账号不适合作为资源目录的管理账号？

- 账号下有待处理的邀请。建议：先处理邀请后再开通资源目录。
- 账号下已经有云资源部署了业务或应用。建议：由于管理账号将承载整个资源目录的架构管理、用户权限管控以及所有资源的付款结算等高权限操作，为了确保管理账号的安全，建议您创建一个新的阿里云账号作为管理账号，避免将已有用途的阿里云账号作为管理账号。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-239（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
