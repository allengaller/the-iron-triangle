<!-- source: https://help.aliyun.com/zh/well-architected/solution-84 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929355 -->

# 容器生命周期安全管控解决方案

## 方案概述

近年由于5G、互联网等技术的飞速发展，企业业务越来越敏捷化，基础设施的演进已经从传统的IDC走向云原生。在容器化及云原生环境下，安全架构相比基于物理机、ECS虚拟化环境已经发生了较大的变化。容器及云原生环境下系统架构变的更加的松耦合。在架构层面，安全能力随之上移，对于用户而言，在容器环境及云原生无服务器环境下，安全开始聚焦到容器层面。

基于这样的背景，本文档提供容器生命周期安全管控方案。

## 方案优势

### 原生容器安全集成能力

云原生EDR能力，覆盖主机、容器和常见的应用程序，实现更精准和高效的终端安全防护，抵挡病毒和木马等常见威胁。同时提供主机、容器和应用漏洞检测与修复、系统基线检查与加固，云平台配置检查与AK泄漏检测。集成CI/CD、私有镜像仓和公共镜像仓的威胁检测和扫描。

### 容器威胁检测能力

覆盖ATT&CK容器安全威胁图谱，实时检测容器运行时威胁，支持多达300种威胁检测模型。覆盖攻击链。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8376581571/p971097.png)

### 大数据分析能力

集成云上海量日志，依托大数据和机器学习能力，发现潜在的入侵和攻击威胁。通过对云资源的海量行为数据进行实时分析和关联查询，发现用户网络和业务系统中的异常行为，并进行威胁告警和相应处置。

## 客户场景

### 更完善地构建容器安全

#### 场景描述

企业基础设施逐步迁移到容器和云原生的环境中，容器成为基础设施，安全融入了devops，那如何设计安全方案更好地适配开发和运维，尤其是在容器这种生命周期较短的应用场景中，成为企业越来越关注的话题。阿里云认为容器安全能力应覆盖容器生命周期中三大关键阶段，即容器构建时的镜像安全、容器部署时的安全配置（基线检查）和容器运行时的入侵检测和防御。

#### 适用客户

- 云上有容器环境的客户，且有自建镜像仓、使用开源镜像的客户。

### 解决容器运行时的攻击和防护

#### 场景描述

容器环境的攻击非常隐蔽，因容器生命周期较短，安全威胁发现的MTTD和MTTR要求较高，企业应有手段对针对容器运行时的漏洞入侵、逃逸攻击、挖矿病毒、webshell、容器启动时攻击等手段进行识别和防护，避免黑客对容器环境发起攻击并进行控制。

且容器安全的风险不仅存在自身的技术栈内，运行容器的基础设施的安全水位从底层影响着容器的运行安全。

#### 适用客户

- 云上有容器环境的客户。

### 容器资产盘点和管理

#### 场景描述

企业内部有自建的容器集群和自建的容器镜像仓，安全部门缺少抓手对容器资产进行整体的盘点和风险的分析。

#### 适用客户

- 云上有容器环境的客户，且有自建镜像仓、使用开源镜像的客户。

### 容器镜像的安全管控

#### 场景描述

安全团队没有办法直接干预开发、运维、测试对于容器镜像的使用和发布，缺少工具集成到CI/CD 进行安全监管和检测。开发和运维往往随意使用开源镜像或自有镜像，初具规模的企业会有独立的镜像仓，或使用docker hub或阿里云的ACR等公共镜像仓。在代码构建完成后拉起镜像前需要进行镜像安全扫描，或构建可信镜像源，进行镜像签名验证，才能够有效确保容器镜像本身的安全，避免供应链攻击和投毒攻击。

#### 适用客户

- 云上有容器环境的客户，且有自建镜像仓、使用开源镜像的客户。

### 容器配置错误导致私钥泄露

#### 场景描述

由于在暴露风险的云配置中普遍存在不良的网络安全实践，因此云漏洞的“速度和规模”可能会增加。Accurics发现，93％的云部署包含错误配置的服务，而91％的部署至少有一个网络风险敞口（安全组易受攻击）。Accurics指出：“在过去两年中，仅这两种做法就构成了200多次泄露事件，暴露了300亿条记录。”还有其他新的做法正在造成风险敞口，包括72％的部署中存在硬编码的私钥，有一半的部署使用存储在容器配置文件中的不受保护的凭据。

#### 适用客户

- 使用容器的客户，并且有敏感数据配置。

## 方案架构

### 容器安全参考维度

容器安全的建设应该从如下两个维度考虑：

- 从Devops容器编排到CI/CD流水线集成，如下图所示。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8376581571/p971100.png)（增加CI/CD 不同环节的风险）
- 从容器自身运行时，和容器的载体，主机层面的安全进行建设。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8376581571/p971129.png)

容器安全应覆盖三大关键阶段即容器构建时的镜像安全、容器部署时的安全配置（基线检查）和容器运行时的入侵检测和防御。阿里云容器服务也已深度集成云安全中心的防护能力。以下表格介绍了容器各生命周期对应的安全功能入口，具体产品功能可以参考[什么是云安全中心](https://help.aliyun.com/zh/security-center/what-is-security-center)。

| **容器生命周期** | **对应功能** | **功能入口（左侧导航栏）** |
| --- | --- | --- |
| 容器网络和资产可视化 | 容器网络可视化 | **总览**（容器网络拓扑页签） |
| 容器资产统一管理 | **资产中心**（容器页签） |  |
| 安全预防-镜像安全 | 镜像系统漏洞 | **安全预防 > 镜像安全扫描** |
| 镜像应用漏洞 |  |  |
| 镜像恶意样本扫描 |  |  |
| 镜像敏感信息检查 |  |  |
| 镜像基线检查 |  |  |
| 安全预防-供应链安全 | 开源供应软件漏洞扫描 | **安全预防 > 镜像安全扫描** |
| [容器签名](https://help.aliyun.com/zh/security-center/user-guide/use-the-container-signature-feature) | **安全预防 > 容器签名** |  |
| 运行时威胁检测 | [安全告警处理](https://help.aliyun.com/zh/security-center/user-guide/overview-6) | **运行时威胁检测 > 安全告警处理** |
| [运行时漏洞修复](https://help.aliyun.com/zh/security-center/user-guide/overview-4) | **运行时威胁检测 > 运行时漏洞修复** |  |
| [运行时基线检查](https://help.aliyun.com/zh/security-center/baseline-check-overview) | **运行时威胁检测 > 基线检查** |  |
| [攻击分析](https://help.aliyun.com/zh/security-center/user-guide/attack-awareness) | **运行时威胁检测 > 攻击分析** |  |
| [AK泄露检测](https://help.aliyun.com/zh/security-center/user-guide/detection-of-accesskey-pair-leaks) | **运行时威胁检测 > AK泄露检测** |  |
| [云蜜罐（公测中）](https://help.aliyun.com/zh/document_detail/196044.html) | **运行时威胁检测 > 云蜜罐** |  |

### 容器安全体系

容器安全体系如下图所示，整体分为三层。分别为产品构成、核心能力引擎、核心功能。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8376581571/p971130.png)

容器安全体系因涉及容器自身安全、镜像安全、镜像可信等维度。产品构成包括了阿里云云安全中心、KMS、和证书管理服务。KMS和证书管理服务是在创建可信镜像和镜像签名能力时，云安全中心调用的主要云安全能力之一。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云安全中心 | 云安全中心（态势感知）是一款集持续监测、深度防御、全面分析、快速响应能力于一体的云上安全管理平台。云安全中心旗舰版支持容器运行时安全、容器签名、容器主动防御、容器防火墙等功能。容器镜像安全仅单独采购增值服务即可。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/security-center/billing-overview)。 |

## 安全性

### RAM用户自定义访问权限

为提升访问安全性，云安全中心支持自定义的访问控制权限，并授予RAM用户使用云安全中心不同功能的权限，实现精细化的权限管理，具体查看[官网链接](https://help.aliyun.com/zh/security-center/create-custom-policies-and-attach-the-policies-to-ram-users)。

## 注意事项

### 接入版本：必须是旗舰版

接入限制：第三方镜像仓和自建k8s集群有接入版本限制（第三方镜像仓目前仅支持**harbor、quay**）

费用明细：详见产品费用说明。

## 实施步骤

### 实施准备

#### 配合产品及支持的环境

- 容器安全产品：阿里云云安全中心（旗舰版-容器安全）同时购买容器镜像扫描的授权。
- 加密产品：阿里云KMS、证书（支持在KMS上上传自有证书，或购买阿里云SSL证书）
- 镜像仓：官方镜像仓（ACR、docker hub），私有镜像仓（支持版本：harbor[1、2]、quay[1、2]）

### 操作步骤

#### 镜像安全扫描

##### 01 开通镜像扫描功能并购买授权

请前往云安全中心的售卖页，开通容器镜像安全扫描增值服务。

**注意：镜像安全扫描功能为云安全中心增值服务，需单独购买。仅支持高级版、企业版、旗舰版和仅采购增值服务用户购买镜像安全扫描功能。若您购买的是云安全中心旗舰版（容器安全），同样需要开通镜像安全扫描增值服务并购买授权**

开通并购买授权详见如下：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8376581571/p971104.png)

开通购买[链接](https://yundun.console.aliyun.com/?spm=5176.7946181.J_5253785160.3.5f8f42c5luSMWI&p=sas#/overview/home/cn-hangzhou?buyConfig={%22spec%22:%22level2%22})。此项功能是收费产品，具体收费情况见产品费用。

##### 02 接入镜像仓

镜像仓接入分为阿里云镜像仓 和非阿里云镜像仓。

**TIPS：非阿里云镜像仓支持（harbor、quay）。**

镜像仓接入配置详细参考[此链接](https://help.aliyun.com/zh/security-center/add-image-repositories-to-security-center)。

混合云镜像仓接入配置详细参考（混合云场景代理配置说明），参考[此链接](https://help.aliyun.com/zh/security-center/add-image-repositories-to-security-center)。

##### 03 执行镜像安全扫描配置

执行镜像安全扫描详细配置详见[此链接](https://help.aliyun.com/zh/security-center/user-guide/scan-images)。

##### 04 检查镜像扫描结果

执行完扫描后可在控制台查看相关镜像检测的结果。详见[此链接](https://help.aliyun.com/zh/security-center/user-guide/view-image-scan-results)。

#### 镜像签名配置

仅旗舰版支持该功能，其他版本用户需要升级到旗舰版才可使用该功能。

##### 前置条件

- 已创建了非对称加密算法的KMS密钥。有关创建KMS密钥的详细内容，请参见[创建密钥](https://help.aliyun.com/zh/kms/key-management-service/support/create-a-cmk-1)。

**注意** 由于非对称密钥算法才支持容器签名功能，创建KMS密钥时，**密钥类型**必须选择RSA_2048，**密钥用途**必须选择SIGN/VERIFY。关于KMS密钥算法的详细内容，请参见[KMS支持的算法规格说明](https://help.aliyun.com/zh/kms/key-management-service/support/overview-4)。

- 已创建了Kubernetes集群，并且集群已安装了kritis-validation-hook组件。创建Kubernetes集群的具体操作，请参见[创建Kubernetes专有版集群](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-an-ack-dedicated-cluster/)。有关kritis-validation-hook组件的更多信息，请参见[kritis-validation-hook组件介绍](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/introduction-to-kritis-validation-hook)。
- 首次使用容器签名，需要先完成云资产访问授权。

##### 01 创建可信镜像证明者

1. 登录云安全中心左侧导航栏，选择**安全运营 > 容器签名**。
2. 在**容器签名 > 证明者**页签中创建证明者。如果您已创建过证明者，您可在**证明者**页签中单击**创建证明者**，完成配置后并单击**确定**，完成证明者的创建。创建证明者的配置说明如下。

##### 02 创建非对称加密秘钥

开通KMS，并创建非对称秘钥，详细配置见[链接](https://help.aliyun.com/zh/kms/key-management-service/support/create-a-cmk-1)。

##### 03 创建K8S集群，并安装kritis-validation-hook组件

开通k8s集群，并安装相关组件，详细配置详见[链接](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/introduction-to-kritis-validation-hook)。

##### 04 创建镜像签名策略

可在**安全策略**页签中，单击**添加策略**，完成配置后并单击**确定**，完成策略的创建。详细配置详见[链接](https://help.aliyun.com/zh/security-center/user-guide/use-the-container-signature-feature)。

#### 容器运行时安全检测

容器运行时的威胁检测为容器Kubernetes版提供运行时刻安全监控和告警，包括在容器中或在主机层面发生的病毒和恶意程序攻击、容器内部的入侵行为、容器逃逸和高风险操作预警等主要的容器侧攻击行为。

TIPS：必须开通云安全中心旗舰版，支持容器运行时威胁检测。

支持容器风险项检测和告警。检测范围如下：

- **恶意镜像启动**对DockerHub等公开的镜像源进行实时监控，当含有后门或者挖矿行为的恶意镜像被安装到服务器时及时进行预警。
- **病毒和恶意程序**检测容器中是否存在病毒、木马、挖矿程序、恶意脚本以及Webshell。
- **容器内部入侵行为**检测是否存在黑客通过应用层漏洞成功入侵容器，以及在容器中进行后续渗透利用和横向传播的行为。
- **容器逃逸**检测是否存在黑客利用容器配置不当或者Docker、操作系统自身漏洞进行的容器逃逸攻击。
- **高风险操作预警**检测是否存在宿主机敏感目录挂载、Docker或者K8s API泄露、以及可疑的特权容器启动行为，避免攻击者轻易对这些风险点发起攻击。
- **实时检测**正在运行的容器集群安全状态，帮助您及时发现容器中的安全隐患和黑客入侵行为。支持以下检测项：K8s API Server执行异常指令Pod异常目录挂载K8s Service Account横向移动恶意镜像Pod启动

##### 01 开启运行时安全检测

升级至云安全中心旗舰版后，即可默认开启对容器环境运行时的安全检测。可检测的告警事件和检测项，详见[链接](https://help.aliyun.com/zh/security-center/user-guide/events/)。

##### 02 开启容器k8s威胁检测

打开【设置】-选择容器k8s威胁检测，并开启开关

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8376581571/p971131.png)

开启容器K8s威胁检测能力后，您无需进行其他设置，云安全中心将为您开启**容器集群异常**类型告警的检测。云安全中心支持的检测项详情，请参见[容器K8s威胁检测项](https://help.aliyun.com/zh/security-center/enable-features-on-the-container-protection-settings-tab)。

#### 容器主动防御配置

云安全中心的容器主动防御功能可在该集群内使用镜像创建资源时，对镜像进行安全风险校验，对命中容器主动防御策略的镜像执行拦截、告警或放行动作，确保集群内启动的镜像符合您的安全要求。

开通旗舰版后需要添加相关配置，详细配置见[链接](https://help.aliyun.com/zh/security-center/user-guide/use-the-feature-of-proactive-defense-for-containers)。

#### 容器防火墙配置

容器防火墙是云安全中心为容器环境提供的防火墙服务。当黑客利用漏洞或恶意镜像入侵容器集群时，容器防火墙会对异常行为进行告警或拦截。

详见配置[见链接](https://help.aliyun.com/zh/security-center/user-guide/create-a-network-object)。

TIPS：配置时注意支持的操作系统版本，参考[链接](https://help.aliyun.com/zh/security-center/user-guide/overview)。

#### 混合云容器资产接入配置

支持接入客户部署在其他云和IDC的自建第三方k8s集群，详细配置操作及注意事项详见[链接](https://help.aliyun.com/zh/security-center/connect-a-self-managed-kubernetes-cluster-to-security-center)。

## 故障排除

### 客户端排查工具

当云安全中心客户端出现异常离线、安装或卸载失败、进程CPU占有率高等问题时，您可以使用云安全中心提供的客户端问题排查功能进行排查。本文介绍如何使用客户端问题排查功能。详见操作[见链接](https://help.aliyun.com/zh/security-center/use-the-agent-troubleshooting-feature)。

### 可能因agent性能消耗过高导致的影响

部分环境下，可能担心因agent运行时消耗过多ECS资源，影响业务，因此云安全中心提供agent性能监控和限制的配置，提前做好限额阈值配置，避免因agent运行资源消耗过高导致的故障。

详细配置可参考[客户端能力配置](https://help.aliyun.com/zh/security-center/enable-features-on-the-agent-settings-tab)。

### 批量停用agent进程

可能因agent的防护策略影响业务正常运行，可考虑采用停用agent进程，判断问题是否恢复，详见操作[链接](https://help.aliyun.com/zh/security-center/uninstall-the-security-center-agent)。

### 批量卸载agent进程

若存在因agent进程影响ECS稳定性问题等严重问题，可考虑采用卸载agent的方式来判断是否是因云安全中心引起的故障。详见操作[链接](https://help.aliyun.com/zh/security-center/uninstall-the-security-center-agent)。

## 存量迁移方案

技术方案上仅需要关注使用的镜像仓是否为自建，是否在方案支持选项中，并升级云安全中心旗舰版即可实现容器安全防护。

价格上因2022年6月23日更新了容器安全的报价策略，对于存量用户的升级（原保有云安全中心旗舰版的客户在实例没有到期前，需单独报备至安全PDSA打标，保证存量未过期的客户仍享有原价格体系）需要注意变更。

## 相关内容

- [容器镜像扫描](https://help.aliyun.com/zh/security-center/user-guide/overview-8)
- [容器资产管理](https://help.aliyun.com/zh/security-center/container-assets/)
- [容器安全基线检测](https://help.aliyun.com/zh/security-center/baseline-check-overview)
- [CI/CD集成接入（支持接入jenkins、github）](https://help.aliyun.com/zh/security-center/user-guide/obtain-a-token-of-the-ci-or-cd-plug-in)
- [容器签名](https://help.aliyun.com/zh/security-center/user-guide/use-the-container-signature-feature)
- [容器运行时威胁检测](https://help.aliyun.com/zh/security-center/user-guide/use-the-feature-of-proactive-defense-for-containers)
- [容器防火墙](https://help.aliyun.com/zh/security-center/user-guide/container-firewall-feature/)
- [容器安全可视化](https://help.aliyun.com/zh/security-center/use-the-feature-of-container-network-topology)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-84（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
