<!-- source: https://help.aliyun.com/zh/well-architected/solution-60 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929468 -->

# 基于ArgoWorkflow实现账号工厂

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2786581571/p972959.png)

当企业开通[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)，将已有阿里云账号邀请进来，或者通过新建成员账号的方式开展新的业务，那么不同账号之间的统一权限管理就会显得尤为重要，如果是在这些账号内手工创建 RAM 角色，则无法保证权限统一，后续修改维护困难，本文档则介绍了一种通过[Argo Workflows](https://argoproj.github.io/argo-workflows/) + [ACK](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/product-overview/what-is-ack) + [Terraform](https://www.terraform.io/) 自动化为所有成员账号创建RAM 角色、权限及VPC等统一基线的方法。

## 方案优势

### 账号统一基线

账号工厂通过同一工作流模板生产成员账号，能够确保新账号都包含流水线中定义的统一基线，根据基线内容保障新账号权限安全。

### 基础设施代码化

基于IaC思想，将资源目录中成员账号的配置过程使用[Terraform](https://www.terraform.io/)规范化，每次创建成员账号时使用同一份Terraform代码，保证所有成员账号权限统一，减轻运维管理负担。

### 灵活可扩展

Terraform及工作流代码可拓展，用户可根据需求拓展功能，提供更多的基线配置。[Argo Workflows](https://argoproj.github.io/argo-workflows/)为CNCF项目，与K8s天然集成、生态丰富，API可与企业DevOps平台集成。

### AK便捷安全管理

可与[KMS](https://help.aliyun.com/zh/kms/key-management-service/support/what-is-key-management-service)凭据管家集成，统一管理外部及阿里云AccessKey，提升安全性及便捷性。

## 客户场景

### 上云阶段批量生产成员账号

#### 场景描述

企业上云阶段构建多账号体系，多成员账号权限配置繁琐、效率低下，无法保证账号权限、资源配置等基线统一，后续修改维护困难。

#### 适用客户

上云阶段需要批量生成统一基线账号的企业客户。

### 业务扩展新建成员账号

#### 场景描述

企业业务扩展需开设新账号，企业手动创建账号时无法快速创建拥有统一身份权限、资源配置基线的成员账号。

#### 适用客户

企业业务扩展阶段需要生成统一基线账号的企业客户。

## 方案架构

本方案使用Terraform自动化执行，整合Git仓库 + ArgoWorkflows搭建Terraform的执行环境，实现了Terraform的CI/CD集成。方案中以ACK集群为基础搭建Argo Workflows，Terraform的state文件使用Azure Storage Account Container作为服务远端存储（Backend）并支持加锁，保证state文件的安全。另整合KMS凭据管家（也可选择k8s保密字典）对访问控制密钥（AccessKey）进行托管，对Azure及阿里云密钥进行集中管理，提升密钥管理的安全性和便捷性。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972935.png)

以下的流程图描述了该方案的执行步骤，首先使用**企业管理账号**下的**RAM用户**（子用户）AK信息，通过Terraform脚本登录到企业管理账号，并在指定的资源夹下创建新的「成员账号」。之后扮演成员账号下的ResourceDirectoryAccountAccessRole角色，该角色会在成员账号加入RD时自动创建，并拥有云管理员（AdministratorAccess）权限。登录到成员账号后，会在成员账号下进行**权限配置**——创建IDP和相关RAM角色、创建一个用于执行Tarraform脚本的RAM用户并为上述角色和用户绑定权限策略。最后会在成员账号下进行**网络配置**——根据用户指定数据创建VPC和交换机。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972934.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 访问控制RAM | [访问控制](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)使您能够安全地集中管理对阿里云服务和资源的访问。您可以使用RAM创建和管理用户和组，并使用各种权限来运行或访问他们对云资源的访问。 | 免费。 |
| 容器服务ACK | [阿里云容器服务Kubernetes版](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/product-overview/what-is-ack)是全球首批通过Kubernetes一致性认证的服务平台，提供高性能的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理，让您轻松高效地在云端运行Kubernetes容器化应用。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ack/billing-information)。 |
| 容器镜像服务ACR | [容器镜像服务ACR](https://help.aliyun.com/zh/acr/product-overview/what-is-container-registry)提供安全地镜像托管能力，稳定的国内外镜像构建服务，便捷的镜像授权功能，方便用户进行镜像全生命周期管理。 | 企业版收费，详情见[产品计费](https://help.aliyun.com/zh/acr/product-overview/pricing/)。 |
| 阿里云文件存储NAS | [阿里云文件存储](https://help.aliyun.com/zh/nas/product-overview/what-is-nas)是面向ECS实例、E-HPC和容器服务等计算节点的文件存储服务。它是一种可共享访问、弹性扩展、高可靠以及高性能的分布式文件系统。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/nas/product-overview/billing/)。 |
| 密钥管理服务KMS | [密钥管理服务](https://help.aliyun.com/zh/kms/key-management-service/support/what-is-key-management-service)是阿里云一站式密钥管理和数据加密服务平台，提供简单、可靠、安全、合规的数据加密保护能力。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/kms/key-management-service/support/billing-1-1/)。 |
| Argo Workflows | [Argo Workflows](https://argoproj.github.io/argo-workflows/)是基于 Kubernetes 的开源任务编排服务，它自定义了一个名为 Workflow 的 CR (Custom Resource)，提供了丰富的执行控制逻辑。 | CNCF开源项目，免费。 |
| Azure存储容器 | [Azure存储容器](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction#blob-storage-resources)对一组 blob 进行组织，类似于文件系统中的目录。 一个存储账户可以包含无限数量的容器，一个容器可以存储无限数量的 Blob | 收费，详情参见[价目表](https://azure.microsoft.com/zh-cn/pricing/details/storage/blobs/#pricing)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| RAM用户 | RAM用户是RAM的一种实体身份类型，有确定的身份ID和身份凭证，它通常与某个确定的人或应用程序一一对应。因安全原因不推荐直接使用云账号的AK/SK。因此在账号下创建一个RAM用户，授予RAM用户最小权限，使用该RAM用户的AK/SK。 |
| 成员账号 | 在资源目录中受「企业管理账号」邀请或被创建的其他账号，每一个成员账号均为一个独立的账号，拥有自己的云资源，企业可根据职责划分为不同的账号，由企业管理账号统一管理。 |
| State文件 | Terraform中用于描述当前资源配置的文件，本文使用Azure存储容器作为远端存储，可参考[文档](https://www.terraform.io/docs/language/settings/backends/azurerm.html)。 |

## 安全性

### 资源目录权限

资源目录服务关联角色（AliyunServiceRoleForResourceDirectory）为资源目录集成服务提供可信访问通道，详情参见[资源目录服务关联角色](https://help.aliyun.com/zh/resource-management/security-and-compliance/ram-roles-in-a-resource-directory)。

### ACK安全性

阿里云容器服务Kubernetes版的安全体系维度有运行时安全、可信软件供应链和基础架构安全三个维度，包括安全巡检、策略管理、运行时监控和告警、镜像扫描、镜像签名、云原生应用交付链、默认安全、身份管理、细粒度访问控制等，详情参见[安全体系概述](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/security-system-overview)。容器服务ACK的授权体系包含RAM授权和RBAC授权两部分，详情参见[授权概述](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/authorization-overview/)。

### KMS安全性

KMS经过严格的安全设计和审核，保证密钥在阿里云得到最严格的保护，详情参见[安全与合规能力](https://help.aliyun.com/zh/kms/key-management-service/support/benefits-1)。

### Terraform State文件安全

使用Azure存储容器作为Backend保存Terraform State文件，存储容器支持State加锁及一致性检查，详情参见[Azurerm Backends](https://www.terraform.io/language/settings/backends/azurerm)。

### Argo Workflows安全性

Argo Server可运行在不同的权限认证模式下，详情参见[Auth Mode](https://argoproj.github.io/argo-workflows/argo-server/#auth-mode)。使用API及工作流界面时可启用[Access Token](https://argoproj.github.io/argo-workflows/access-token/)提升工作流管控安全性，整体安全性概述可参见官网[Security](https://argoproj.github.io/argo-workflows/security/)。

### AccessKey使用

方案需要使用企业管理主账号下RAM用户的AccessKey，用于创建账号及操作阿里云资源。需要使用Azure侧的订阅ID、租户ID、应用ID及Secret，用于操作Azure存储容器。

## 注意事项

### 资源目录使用限制

资源目录及资源共享使用限制详情参见[使用限制](https://help.aliyun.com/zh/resource-management/product-overview/limits)。

### ACK使用限制

ACK使用过程中有配额及底层云产品限制等，详情参见[使用限制](https://help.aliyun.com/zh/ack/product-overview/limits)。

### KMS使用限制

KMS存在配额及地域等限制，详情参见[使用限制](https://help.aliyun.com/zh/kms/key-management-service/support/limits)。

## 实施步骤

### 实施准备

- 已完成[创建Kubernetes托管版集群](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2/)，使用docker作为执行容器、开通NAS、公网SLB，且ACK集群已初始化完成。
- 已拥有Azure账号，能够通过[Azure Portal](https://portal.azure.com/?quickstart=true#home)及命令行操作Azure资源。
- 已拥有Git仓库，用于上传及拉取Terraform工作流相关代码。
- 已经开通阿里云KMS服务，可参考[开通链接](https://common-buy.aliyun.com/?spm=a2c4g.11186623.0.0.52ad7be6QjC5fP&commodityCode=kms#/open)。
- 确保在「企业管理账号」中，存在一个「RAM用户」AK，且该账号拥有 AliyunResourceDirectoryFullAccess和AliyunSTSAssumeRoleAccess两个权限；在后续的步骤中，我们将使用该RAM用户及其AK。根据后续实施步骤中选择不同的AK管理方案，AK将会托管到KMS或保密字典中，不在工作流中存储或显式传入。
- 确定工作流及Terraform输入参数，输入参数分为两部分：第一部分为**全局参数**，写入settings.tfvars文件，每次流水线执行时均保持一致；第二部分为**执行参数**，执行流水线时动态填写，不会保存。**全局参数**encodedsaml_metadata_document：企业IDP的元文件，用于在阿里云上创建IDPsso_provider_name：创建的IDP的名称ram_roles：需要创建的ram角色列表，示例中包括只读和管理员角色user_name：用于执行TF脚本的角色名称policy_name：自定义权限策略的名称policy_document：自定义权限策略内容attach_roles：自定义权限策略绑定的角色列表attach_users：自定义权限策略绑定的用户列表reader_name：需要绑定权限策略的只读角色名称reader_policy_type：为只读角色绑定的权限策略的类型reader_policy_name：为只读角色绑定的权限策略的名称vpc_name：创建的vpc的名称vswitch_name：vpc下交换机的名称**执行参数**account_name：新创建账号的显示名称account_name_prefix：新创建账号的账号标识uid: 「企业管理账号」uidfolder_id：新创建的成员账号所属资源夹IDvpc_cidr_block：VPC的网段switch_cidr_block：交换机的网段region：区域，如cn-hangzhouzone_id：可用区ID，如cn-hangzhou-balicloud_secret_name：KMS中的阿里云凭据名称，采用KMS凭据管家管理密钥时需要，这里仅做说明、后续步骤生成该配置后作为参数传入工作流azure_secret_name：KMS中的Azure凭据名称，采用KMS凭据管家管理密钥时需要，这里仅做说明、后续步骤生成该配置后作为参数传入工作流kms_aap_client_key_pwd：KMS应用接入点ClientKey口令，采用KMS凭据管家管理密钥时需要，这里仅做说明、后续步骤生成该配置后作为参数传入工作流
- 完成镜像构建，并通过容器镜像服务（ACR）能够拉取到镜像，我们将使用ACR中的`acr-hangzhou-1-registry.cn-hangzhou.cr.aliyuncs.com/terraform/terraform:v9`镜像运行Terraform代码，用户也可根据自身需求打包镜像，该镜像的Dockerfile如下所示：`FROM mcr.microsoft.com/azure-cli:latest

ENV TERRAFORM_PLUGIN_DIR=/srv/terraform-plugins
ENV TF_PLUGIN_CACHE_DIR=${TERRAFORM_PLUGIN_DIR}
ENV TERRAFORM_VERSION=1.0.2
ENV TERRAFORM_PROVIDER_ALICLOUD_VERSION=1.145.0
ENV TERRAFORM_PROVIDER_AZUREM_VERSION=2.81.0
ENV TERRAFORM_PROVIDER_LOCAL_VERSION=2.1.0
ENV PATH="/opt/venv/bin:$PATH"

RUN apk add libxml2-dev libxslt-dev python3-dev gcc build-base wget unzip git bash \
 && python3 -m venv /opt/venv \
 && pip install terraform-compliance \
 && pip install checkov \
 && python3 -m pip install --upgrade pip \
 && pip install aliyun-secret-manager-client==0.0.5 \
 && pip install alibabacloud-resourcemanager20200331==2.0.3 \
 && pip install alibabacloud_bssopenapi20171214==2.0.3 \
 
 && wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
 && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin/ \

 && mkdir -p ${TERRAFORM_PLUGIN_DIR}/registry.terraform.io/aliyun/alicloud/${TERRAFORM_PROVIDER_ALICLOUD_VERSION}/linux_amd64 \
 && wget https://releases.hashicorp.com/terraform-provider-alicloud/${TERRAFORM_PROVIDER_ALICLOUD_VERSION}/terraform-provider-alicloud_${TERRAFORM_PROVIDER_ALICLOUD_VERSION}_linux_amd64.zip \
 && unzip terraform-provider-alicloud_${TERRAFORM_PROVIDER_ALICLOUD_VERSION}_linux_amd64.zip -d ${TERRAFORM_PLUGIN_DIR}/registry.terraform.io/aliyun/alicloud/${TERRAFORM_PROVIDER_ALICLOUD_VERSION}/linux_amd64 \

 && mkdir -p ${TERRAFORM_PLUGIN_DIR}/registry.terraform.io/hashicorp/azurerm/${TERRAFORM_PROVIDER_AZUREM_VERSION}/linux_amd64 \
 && wget https://releases.hashicorp.com/terraform-provider-azurerm/${TERRAFORM_PROVIDER_AZUREM_VERSION}/terraform-provider-azurerm_${TERRAFORM_PROVIDER_AZUREM_VERSION}_linux_amd64.zip \
 && unzip terraform-provider-azurerm_${TERRAFORM_PROVIDER_AZUREM_VERSION}_linux_amd64.zip -d ${TERRAFORM_PLUGIN_DIR}/registry.terraform.io/hashicorp/azurerm/${TERRAFORM_PROVIDER_AZUREM_VERSION}/linux_amd64 \
 

 && mkdir -p ${TERRAFORM_PLUGIN_DIR}/registry.terraform.io/hashicorp/local/${TERRAFORM_PROVIDER_LOCAL_VERSION}/linux_amd64 \
 && wget https://releases.hashicorp.com/terraform-provider-local/${TERRAFORM_PROVIDER_LOCAL_VERSION}/terraform-provider-local_${TERRAFORM_PROVIDER_LOCAL_VERSION}_linux_amd64.zip \
 && unzip terraform-provider-local_${TERRAFORM_PROVIDER_LOCAL_VERSION}_linux_amd64.zip -d ${TERRAFORM_PLUGIN_DIR}/registry.terraform.io/hashicorp/local/${TERRAFORM_PROVIDER_LOCAL_VERSION}/linux_amd64 \
 
 && rm -rf *.zip`

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：90分钟。

### 操作步骤

#### 配置Azure存储容器

1. 在Azure Portal命令行分别执行下述命令，创建资源组、存储账户、存储容器，记录创建信息，用于Terraform Backend存储。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972960.png)`#!/bin/bash

RESOURCE_GROUP_NAME=tfstate
STORAGE_ACCOUNT_NAME=tfstate$RANDOM
CONTAINER_NAME=tfstate

# Create resource group
az group create --name $RESOURCE_GROUP_NAME --location eastus

# Create storage account tfstate9104
az storage account create --resource-group $RESOURCE_GROUP_NAME --name $STORAGE_ACCOUNT_NAME --sku Standard_LRS --encryption-services blob

# Create blob container
az storage container create --name $CONTAINER_NAME --account-name $STORAGE_ACCOUNT_NAME`
2. 在存储账户页面能够查看刚创建的账户及容器信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972936.png)
3. 在命令行执行“az account show”，记录account ID。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2786581571/p972937.png)
4. 在命令行执行“az ad sp create-for-rbac --name terraform-sp”，创建service principal，用于Terraform运行时授权使用，记录appId、password、tenant。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972962.png)
5. 上述记录的信息需要记录下来，作为工作流的环境变量传入用于支持Terraform运行。字段和变量对应关系如下：`# ENV variable
ARM_SUBSCRIPTION_ID="xxx" # account ID, argo variable: arm_subscription_id
ARM_TENANT_ID="xxx" # tenant, argo variable: arm_tenant_id
ARM_CLIENT_ID="xxx" # appId, argo variable: arm_client_id
ARM_CLIENT_SECRET="xxx" # password, argo variable: arm_client_secret`

#### 配置参数

1. 从本文**源代码章节**下载账号工厂代码，目录结构可以参考章节中相应说明。
2. 用编辑器打开代码**，拷贝**账号工厂代码`extension/backend`目录中的`azurerm-backend.tfvars`文件内容，**替换掉**账号工厂代码最外层的`backend.tfvars`**文件内容**。
3. 替换完成后修改该文件内的配置项并保存：resource_group_name：**已创建的Azure资源组名称**storage_account_name：**已创建的Azure存储账户名称**container_name：**已创建的Azure存储容器名称**
4. **拷贝**账号工厂代码`extension/backend`目录中的`azurerm-backend.tf`**文件内容**，替换掉账号工厂代码`step`目录的**所有子目录下的backend.tf文件内容并保存。**
5. 用编辑器打开`settings.tfvars`文件，根据配置文件注释和实施准备中的全局参数填写。
6. 将代码上传到Git仓库，也可以等后续所有配置都完成后再上传。

#### 安装K8S命令行

1. 在本地或平时操作的机器部署kubectl，不同操作系统的操作步骤参考[链接](https://kubernetes.io/docs/tasks/tools/)。
2. 查看ACK集群连接信息，将凭证信息保存到$HOME/.kube/config 文件下。可使用命令kubectl cluster-info验证集群信息获取。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972938.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972939.png)

#### 部署Argo Workflows

1. 执行下述命令，在ACK集群中部署工作流。Argo Workflow官方文档可参考[链接](https://argoproj.github.io/argo-workflows/quick-start/)。`kubectl create ns argo
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/master/manifests/quick-start-postgres.yaml`
2. 本地Argo Workflows CLI安装，参考[链接](https://github.com/argoproj/argo-workflows/releases/tag/v3.2.0)，可尝试用CLI提交工作流并查看工作流运行信息。`argo submit -n argo --watch https://raw.githubusercontent.com/argoproj/argo-workflows/master/examples/hello-world.yaml
argo list -n argo
argo get -n argo @latest
argo logs -n argo @latest`
3. 在本地创建port-forward，用于在本地即可访问已部署在ACK集群的Argo Workflow。`kubectl -n argo port-forward deployment/argo-server 2746:2746`
4. 访问 [https://localhost:2746](https://localhost:2746) 查看Workflow页面。若访问页面提示权限问题可运行`argo server --auth-mode server`命令后重试。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2786581571/p972963.png)
5. 若需要通过公网访问可执行如下命令（需要ACK集群中有公网SLB），等待EXTERNAL-IP出现后即可通过该公网地址访问页面https://118.31.xx.xx:2746/。`kubectl patch svc argo-server -n argo -p '{"spec": {"type": "LoadBalancer"}}'
kubectl get svc argo-server -n argo`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972940.png)

#### 配置ACK集群

本文中使用ACK部署Argo Workflows来运行工作流，必须先创建ACK集群然后再搭建Argo Workflow，推荐使用ACK托管版，相关详情可参考[链接](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/getting-started/getting-started-overview)。

##### 配置NAS

1. 进入在[ACK控制台](https://cs.console.aliyun.com/#/k8s/cluster/list)集群详情页，创建存储卷并挂载到集群，用于工作流执行时步骤间共享文件数据。选择NAS，名称：pv-nas-1，子目录：/nas。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972964.png)
2. 进入在[ACK控制台](https://cs.console.aliyun.com/#/k8s/cluster/list)集群详情页创建存储声明，用于工作流执行时步骤间共享文件数据。注意页面上方选择命名空间，需要与工作流页面的NAMESPACE保持一致，声明类型选择NAS，名称：pvc-nas-1，选择已有存储卷，即上一步创建的存储卷。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2786581571/p972941.png)

##### 配置Git仓库访问信息

添加Git仓库访问信息到保密字典，用于工作流运行时拉取代码。

1. 在集群详情保密字典页面创建保密字典，注意页面上方选择命名空间，需要与工作流页面的NAMESPACE保持一致，名称为git-terraform-creds，添加键名称username、password、ssh-private-key并填入相应值后保存。这里**可以只选择填写username、password或ssh-private-key其中一项，**代码中默认使用用户名密码拉取，**要使用SSH私钥拉取可以在工作流代码中按注释说明调整下配置即可（方案中暂不支持Azure DevOps Git仓库私钥拉取，参考后续步骤说明）**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972942.png)

##### 配置镜像免密拉取

授权ACK能够免密拉取ACR镜像，如果ACR中Terraform运行镜像配置为公共镜像则可跳过该项配置步骤。

1. 在集群详情页面选择配置项，按下图所示选择命名空间kube-system，填入ACR实例ID、地域、service-account、watch-namespace信息，本文配置的是和ACK在同一账号下的ACR实例ID，其它场景可参考[链接](https://help.aliyun.com/zh/acr/use-the-aliyun-acr-credential-helper-component-to-pull-images-without-using-secrets)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972965.png)
2. 配置拉取权限策略。按下图所示在集群信息-集群资源Tab页进入RAM角色配置页面。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972943.png)
3. 点击下图权限策略名称链接，进入权限配置详情。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972966.png)
4. 点击修改策略内容，将下述配置代码添加到策略内容中后保存。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972944.png)`{
 "Action": [
 "cr:Get*",
 "cr:List*",
 "cr:PullRepository"
 ],
 "Resource": "*",
 "Effect": "Allow"
}`

#### 管理访问控制密钥

这一章节提供了“KMS凭据管家”和“ACK保密字典+KMS落盘加密”两种访问控制密钥（AK，AccessKey）管理方案，用于对工作流中使用的密钥信息进行集中管理，提升安全性和便捷性，以下**两种方案选用一种即可**。注意KMS对API调用和用户上传密钥的托管会收取一定费用，计费说明参考[链接](https://help.aliyun.com/zh/kms/key-management-service/support/billing-of-kms)。

##### 使用KMS凭据管家

KMS凭据管家能够集中管理外部及阿里云密钥信息，支持阿里云AK自动轮转，凭据管家介绍可参考[链接](https://help.aliyun.com/zh/kms/key-management-service/support/overview-6)。工作流变量配置中需要使用凭据管家的三项信息，分别为阿里云凭据名称、Azure 凭据名称、应用接入点ClientKey口令，这三项信息会在下面的操作步骤中产生。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2786581571/p972967.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2786581571/p972945.png)

**操作步骤**：

1. 通过RAM服务角色授予凭据管家管理RAM用户AccessKey的权限。具体操作，请参见[授予凭据管家管理RAM用户AccessKey的权限](https://help.aliyun.com/zh/kms/key-management-service/support/authorize-secrets-manager-to-manage-accesskey-pairs-of-ram-users)。
2. 登录[KMS凭据控制台](https://kms.console.aliyun.com/cn-hangzhou/secret/list)，左上角选择地域，在凭据页面创建新的凭据。这里先对阿里云密钥进行配置，选择使用RAM凭据，选择前置条件中已创建AK的RAM用户，在下一步可以选择使用自动轮转AK的功能，无需管理员手动定时更换凭据。注意设置凭据值这里请输入这个RAM用户对应的一个**合法的AK值**，KMS是用这个AK值去做轮转判断的，官方文档可参考[链接](https://help.aliyun.com/zh/kms/key-management-service/support/manage-dynamic-ram-secrets)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972968.png)
3. 使用应用接入点AAP（Application Access Point），用于控制工作流如何使用凭据。选择应用管理，创建应用接入点，填写名称、描述，认证方式使用ClientKey。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2786581571/p972946.png)
4. 进入下一步，点击+号创建权限策略，选择已准备好的RAM用户的Secret，根据实际情况在可选规则中点击+号创建网络控制规则。完成相应选择后完成接入点创建，在弹出的对话框中选择创建ClientKey。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972947.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972969.png)
5. 输入ClientKey加密口令，点击确定后可下载ClientKey，记录口令和下载的ClientKey备用，在工作流代码中需要使用。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972970.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972948.png)
6. 更新Terraform代码包中的配置，按实际情况在`extension/secretsmanager.properties`文件中填入KMS凭据所在地域，并将下载的ClientKey内容更新到`extension/kms_client_key_kaap.json`中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972949.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2786581571/p972971.png)
7. 上述已经完成了阿里云的凭据配置，这一步创建Azure凭据。在凭据管理页面创建凭据时选择其它凭据，用于存储Azure的保密信息，名称可以自定义后作为参数传入工作流。**凭据值的键使用固定值**，分别创建arm_subscription_id、arm_tenant_id、arm_client_id、arm_client_secret，填入相应信息后完成创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2786581571/p972950.png)
8. 在**应用接入点详情-权限策略**列表中点击编辑，将创建的Azure凭据纳入应用接入点的访问范围后保存，通过该应用接入点可以获取阿里云以及Azure的密钥信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972973.png)

##### 使用ACK保密字典+KMS落盘加密

保密字典是k8s集群管理保密信息的通用标准方案，在ACK集群详情界面可进行配置。另可以使用KMS密钥对保密字典进行数据落盘加密提升安全性，使用KMS密钥进行数据落盘加密时需要创建KMS主密钥及相应系统角色权限。操作步骤：

1. 登录[ACK管理控制台](https://cs.console.aliyun.com/)，进入集群详情页面。
2. 在配置管理-保密字典页面，点击创建按钮进行密钥信息添加。这里我们添加两个保密字典项，分别用于存放阿里云和Azure密钥信息，这里填写的名称会在工作流代码中使用。注意根据实际情况在页面上方选择命名空间，需要与工作流页面的NAMESPACE保持一致。阿里云保密字典名称terraform-ak-alicloud，键的名称分别为access_key、secret_key，填入值信息后点击确定完成创建。Azure保密字典名称terraform-ak-azure，键的名称分别为arm_subscription_id、arm_tenant_id、arm_client_id、arm_client_secret，填入值信息后点击确定完成创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972951.png)
3. 可以使用KMS密钥进行保密字典数据落盘加密，配置过程参考官方[链接](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2)。

#### 运行Argo Workflows

##### 准备工作流代码

根据实施准备中的配置及实际情况修改下面的工作流yaml代码中的**工作流参数、Git仓库地址、镜像配置**，保存备用。注意下面有两个版本的工作流代码，**根据上述密钥管理的方式选择一个版本即可**。

- KMS凭据管家版本：`# KMS凭据管家版本
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
 namespace: argo
 generateName: terraform-workflow-
 annotations:
 workflows.argoproj.io/version: ">= 3.1.0"
spec:
 entrypoint: terraform-workflow
 arguments:
 parameters:
 # 阿里云凭据名称
 - name: alicloud_secret_name
 value: "acs/ram/user/xxx"

 # Azure凭据名称
 - name: azure_secret_name
 value: "terraform-ak-azure"

 # 应用接入点ClientKey口令
 - name: kms_aap_client_key_pwd
 value: "xxx"

 - name: region
 value: "cn-hangzhou"

 - name: uid
 value: "15462275xxx"

 - name: account_name
 value: "xxx"

 - name: account_name_prefix
 value: "xxx"

 - name: folder_id
 value: "xxx"

 - name: vpc_cidr_block
 value: "172.16.0.0/12"

 - name: switch_cidr_block
 value: "172.16.0.0/21"

 - name: zone_id
 value: "cn-hangzhou-b"

 templates:
 - name: terraform-workflow
 steps:

 # 环境准备
 - - name: env-prepare
 template: git-clone-init
 arguments:
 parameters:
 - name: cmd
 value: 'pwd && ls -al'

 # 创建账号
 - - name: account-create
 template: execute-func
 arguments:
 parameters:
 - name: cmd
 value: '
 cd extension 
 && python kms_secret.py {{workflow.parameters.alicloud_secret_name}} {{workflow.parameters.azure_secret_name}} env_temp
 && source env_temp && rm -rf env_temp && cd ..
 && cd step/account-create 
 && terraform init -backend-config="key={{workflow.parameters.uid}}-{{workflow.parameters.account_name}}-account-create"
 -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins
 && terraform apply --auto-approve -var "folder_id={{workflow.parameters.folder_id}}"
 -var "account_name={{workflow.parameters.account_name}}" -var "account_name_prefix={{workflow.parameters.account_name_prefix}}"
 '

 # 权限配置:创建IDP
 - - name: auth-create-idp
 template: execute-func
 arguments:
 parameters:
 - name: cmd
 value: '
 cd extension 
 && python kms_secret.py {{workflow.parameters.alicloud_secret_name}} {{workflow.parameters.azure_secret_name}} env_temp
 && source env_temp && rm -rf env_temp && cd ..
 && cd step/auth-create-idp
 && terraform init -backend-config="key={{workflow.parameters.uid}}-{{workflow.parameters.account_name}}-auth-create-idp"
 -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins
 && terraform apply --auto-approve -var-file=../../settings.tfvars -compact-warnings
 '

 # 权限配置:创建角色
 - - name: auth-create-role
 template: execute-func
 arguments:
 parameters:
 - name: cmd
 value: '
 cd extension 
 && python kms_secret.py {{workflow.parameters.alicloud_secret_name}} {{workflow.parameters.azure_secret_name}} env_temp
 && source env_temp && rm -rf env_temp && cd ..
 && cd step/auth-create-role
 && terraform init -backend-config="key={{workflow.parameters.uid}}-{{workflow.parameters.account_name}}-auth-create-role"
 -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins
 && terraform apply --auto-approve -var-file=../../settings.tfvars -compact-warnings
 '

 # 权限配置:创建TF用户
 - - name: auth-create-user
 template: execute-func
 arguments:
 parameters:
 - name: cmd
 value: '
 cd extension 
 && python kms_secret.py {{workflow.parameters.alicloud_secret_name}} {{workflow.parameters.azure_secret_name}} env_temp
 && source env_temp && rm -rf env_temp && cd ..
 && cd step/auth-create-user
 && terraform init -backend-config="key={{workflow.parameters.uid}}-{{workflow.parameters.account_name}}-auth-create-user"
 -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins
 && terraform apply --auto-approve -var-file=../../settings.tfvars -compact-warnings
 '

 # 权限配置:角色授权
 - - name: auth-authorize-role
 template: execute-func
 arguments:
 parameters:
 - name: cmd
 value: '
 cd extension 
 && python kms_secret.py {{workflow.parameters.alicloud_secret_name}} {{workflow.parameters.azure_secret_name}} env_temp
 && source env_temp && rm -rf env_temp && cd ..
 && cd step/auth-authorize-role
 && terraform init -backend-config="key={{workflow.parameters.uid}}-{{workflow.parameters.account_name}}-auth-authorize-role"
 -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins
 && terraform apply --auto-approve -var-file=../../settings.tfvars -compact-warnings
 '

 # 网络配置
 - - name: network-configure
 template: execute-func
 arguments:
 parameters:
 - name: cmd
 value: '
 cd extension 
 && python kms_secret.py {{workflow.parameters.alicloud_secret_name}} {{workflow.parameters.azure_secret_name}} env_temp
 && source env_temp && rm -rf env_temp && cd ..
 && cd step/network-create-vpc-vsw
 && terraform init -backend-config="key={{workflow.parameters.uid}}-{{workflow.parameters.account_name}}-network-create-vpc-vsw"
 -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins
 && terraform apply --auto-approve -compact-warnings -var "vpc_cidr_block={{workflow.parameters.vpc_cidr_block}}"
 -var "switch_cidr_block={{workflow.parameters.switch_cidr_block}}" -var "zone_id={{workflow.parameters.zone_id}}"
 -var-file=../../settings.tfvars
 '

 - name: execute-func
 inputs:
 parameters:
 - name: cmd
 container:
 image: acr-hangzhou-1-registry.cn-hangzhou.cr.aliyuncs.com/terraform/terraform:v9
 volumeMounts:
 - name: pvc-nas-1
 mountPath: "/nas" # NAS挂载路径
 command: ["/bin/sh", "-c"]
 args: ["{{inputs.parameters.cmd}}"]
 workingDir: /nas/tf-dir-{{workflow.name}}
 env:
 - name: ALICLOUD_REGION
 value: "{{workflow.parameters.region}}"
 - name: KMS_AAP_CLIENT_KEY_PWD
 value: "{{workflow.parameters.kms_aap_client_key_pwd}}"
 volumes:
 - name: pvc-nas-1
 persistentVolumeClaim:
 claimName: pvc-nas-1 # NAS PVC

 - name: git-clone-init
 inputs:
 parameters:
 - name: cmd
 artifacts:
 - name: terraform-source
 path: /nas/tf-dir-{{workflow.name}}
 git:
 repo: https://codeup.aliyun.com/xxxx/account-base.git # when authenticating via basic auth
# repo: git@codeup.aliyun.com:xxxx/account-base.git # when authenticating via sshPrivateKeySecret
 revision: "azure-backend-update"
 usernameSecret: # when authenticating via basic auth
 name: git-terraform-creds
 key: username
 passwordSecret: # when authenticating via basic auth
 name: git-terraform-creds
 key: password
# sshPrivateKeySecret: # when authenticating via sshPrivateKeySecret
# name: git-terraform-creds
# key: ssh-private-key
# insecureIgnoreHostKey: true # when authenticating via sshPrivateKeySecret
 depth: 1
 container:
 image: acr-hangzhou-1-registry.cn-hangzhou.cr.aliyuncs.com/terraform/terraform:v9
 volumeMounts:
 - name: pvc-nas-1
 mountPath: "/nas"
 command: ["/bin/sh", "-c"]
 args: ["{{inputs.parameters.cmd}}"]
 workingDir: /nas/tf-dir-{{workflow.name}}
 volumes:
 - name: pvc-nas-1
 persistentVolumeClaim:
 claimName: pvc-nas-1`
- ACK保密字典版本：`# ACK保密字典版本
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
 namespace: argo
 generateName: terraform-workflow-
 annotations:
 workflows.argoproj.io/version: ">= 3.1.0"
spec:
 entrypoint: terraform-workflow
 arguments:
 parameters:
 - name: region
 value: "cn-hangzhou"

 - name: uid
 value: "15462275xxx"

 - name: account_name
 value: "xxx"

 - name: account_name_prefix
 value: "xxx"

 - name: folder_id
 value: "fd-xxx"

 - name: vpc_cidr_block
 value: "172.16.0.0/12"

 - name: switch_cidr_block
 value: "172.16.0.0/21"

 - name: zone_id
 value: "cn-hangzhou-b"

 templates:
 - name: terraform-workflow
 steps:
 # 环境准备
 - - name: env-prepare
 template: git-clone-init
 arguments:
 parameters:
 - name: cmd
 value: 'pwd && ls -al'

 # 创建账号
 - - name: account-create
 template: execute-func
 arguments:
 parameters:
 - name: cmd
 value: '
 cd step/account-create 
 && terraform init -backend-config="key={{workflow.parameters.uid}}-{{workflow.parameters.account_name}}-account-create"
 -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins
 && terraform apply --auto-approve -var "folder_id={{workflow.parameters.folder_id}}" 
 -var "account_name={{workflow.parameters.account_name}}" -var "account_name_prefix={{workflow.parameters.account_name_prefix}}"
 '

 # 权限配置:创建IDP
 - - name: auth-create-idp
 template: execute-func
 arguments:
 parameters:
 - name: cmd
 value: '
 cd step/auth-create-idp
 && terraform init -backend-config="key={{workflow.parameters.uid}}-{{workflow.parameters.account_name}}-auth-create-idp"
 -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins
 && terraform apply --auto-approve -var-file=../../settings.tfvars -compact-warnings
 '

 # 权限配置:创建角色
 - - name: auth-create-role
 template: execute-func
 arguments:
 parameters:
 - name: cmd
 value: '
 cd step/auth-create-role
 && terraform init -backend-config="key={{workflow.parameters.uid}}-{{workflow.parameters.account_name}}-auth-create-role"
 -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins
 && terraform apply --auto-approve -var-file=../../settings.tfvars -compact-warnings
 '

 # 权限配置:创建TF用户
 - - name: auth-create-user
 template: execute-func
 arguments:
 parameters:
 - name: cmd
 value: '
 cd step/auth-create-user
 && terraform init -backend-config="key={{workflow.parameters.uid}}-{{workflow.parameters.account_name}}-auth-create-user"
 -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins
 && terraform apply --auto-approve -var-file=../../settings.tfvars -compact-warnings
 '

 # 权限配置:角色授权
 - - name: auth-authorize-role
 template: execute-func
 arguments:
 parameters:
 - name: cmd
 value: '
 cd step/auth-authorize-role
 && terraform init -backend-config="key={{workflow.parameters.uid}}-{{workflow.parameters.account_name}}-auth-authorize-role"
 -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins
 && terraform apply --auto-approve -var-file=../../settings.tfvars -compact-warnings
 '

 # 网络配置
 - - name: network-create-vpc-vsw
 template: execute-func
 arguments:
 parameters:
 - name: cmd
 value: '
 cd step/network-create-vpc-vsw
 && terraform init -backend-config="key={{workflow.parameters.uid}}-{{workflow.parameters.account_name}}-network-create-vpc-vsw"
 -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins
 && terraform apply --auto-approve -compact-warnings -var "vpc_cidr_block={{workflow.parameters.vpc_cidr_block}}"
 -var "switch_cidr_block={{workflow.parameters.switch_cidr_block}}" -var "zone_id={{workflow.parameters.zone_id}}"
 -var-file=../../settings.tfvars
 '

 - name: execute-func
 inputs:
 parameters:
 - name: cmd
 container:
 image: acr-hangzhou-1-registry.cn-hangzhou.cr.aliyuncs.com/terraform/terraform:v9
 volumeMounts:
 - name: pvc-nas-1
 mountPath: "/nas" # NAS挂载路径

 command: ["/bin/sh", "-c"]
 args: ["{{inputs.parameters.cmd}}"]
 workingDir: /nas/tf-dir-{{workflow.name}}
 env:
 - name: ALICLOUD_REGION
 value: "{{workflow.parameters.region}}"
 
 - name: ALICLOUD_ACCESS_KEY
 valueFrom:
 secretKeyRef:
 name: terraform-ak-alicloud
 key: access_key
 
 - name: ALICLOUD_SECRET_KEY
 valueFrom:
 secretKeyRef:
 name: terraform-ak-alicloud
 key: secret_key
 

 - name: ARM_SUBSCRIPTION_ID
 valueFrom:
 secretKeyRef:
 name: terraform-ak-azure
 key: arm_subscription_id
 
 - name: ARM_TENANT_ID
 valueFrom:
 secretKeyRef:
 name: terraform-ak-azure
 key: arm_tenant_id
 
 - name: ARM_CLIENT_ID
 valueFrom:
 secretKeyRef:
 name: terraform-ak-azure
 key: arm_client_id
 
 - name: ARM_CLIENT_SECRET
 valueFrom:
 secretKeyRef:
 name: terraform-ak-azure
 key: arm_client_secret
 volumes:
 - name: pvc-nas-1
 persistentVolumeClaim:
 claimName: pvc-nas-1 # NAS PVC

 - name: git-clone-init
 inputs:
 parameters:
 - name: cmd
 artifacts:
 - name: terraform-source
 path: /nas/tf-dir-{{workflow.name}}
 git:
 repo: https://codeup.aliyun.com/xxx/account-base.git # when authenticating via basic auth
# repo: git@codeup.aliyun.com:xxx/account-base.git # when authenticating via sshPrivateKeySecret
 revision: "azure-backend-update"
 usernameSecret: # when authenticating via basic auth
 name: git-terraform-creds
 key: username
 passwordSecret: # when authenticating via basic auth
 name: git-terraform-creds
 key: password
# sshPrivateKeySecret: # when authenticating via sshPrivateKeySecret
# name: git-terraform-creds
# key: ssh-private-key
# insecureIgnoreHostKey: true # when authenticating via sshPrivateKeySecret
 depth: 1
 container:
 image: acr-hangzhou-1-registry.cn-hangzhou.cr.aliyuncs.com/terraform/terraform:v9
 volumeMounts:
 - name: pvc-nas-1
 mountPath: "/nas"
 command: ["/bin/sh", "-c"]
 args: ["{{inputs.parameters.cmd}}"]
 workingDir: /nas/tf-dir-{{workflow.name}}
 volumes:
 - name: pvc-nas-1
 persistentVolumeClaim:
 claimName: pvc-nas-1`

##### Azure Git仓库适配

如果使用Azure DevOps Git仓库存放Terraform等相关代码，由于Git服务器实现方式不同，使用上述代码中ArgoWorkflows的“git”组件可能会在拉取代码时报错造成无法拉取，需要对工作流代码进行简单调整。调整后的代码使用保密字典中的用户名和密码拉取代码，方案中暂不支持使用私钥拉取。调整步骤：

1. 替换“环境准备”这一步骤中的代码，根据实际情况修改Git仓库地址git_repo_url的value。`# 环境准备
 - - name: env-prepare
 template: git-clone-init
 arguments:
 parameters:
 - name: git_repo_url
 value: "dev.azure.com/xxx/helloDevOps/_git/helloDevOps"
 - name: cmd
 value: 'pwd && ls -al'`
2. 将名称为“git-clone-init”的template替换为以下代码，根据实际情况修改镜像。`- name: git-clone-init
 inputs:
 parameters:
 - name: cmd
 - name: git_repo_url
 container:
 image: acr-hangzhou-1-registry.cn-hangzhou.cr.aliyuncs.com/terraform/terraform:v9
 volumeMounts:
 - name: pvc-nas-1
 mountPath: "/nas" # NAS挂载路径
 command: ["/bin/sh", "-c"]
 args: ["git clone https://$GIT_USERNAME:$GIT_PASSWORD@{{inputs.parameters.git_repo_url}} /nas/tf-dir-{{workflow.name}} && {{inputs.parameters.cmd}}"]
 workingDir: /nas/tf-dir-{{workflow.name}}
 env:
 - name: GIT_USERNAME
 valueFrom:
 secretKeyRef:
 name: git-terraform-creds
 key: username
 - name: GIT_PASSWORD
 valueFrom:
 secretKeyRef:
 name: git-terraform-creds
 key: password
 volumes:
 - name: pvc-nas-1
 persistentVolumeClaim:
 claimName: pvc-nas-1 # NAS PVC`

##### 页面运行

1. 访问workflow界面[https://localhost:2746](https://localhost:2746)，打开创建工作流页面。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972952.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972953.png)
2. 将原有示例代码全选、粘贴上述已修改配置的yaml代码，然后点击Create即可运行工作流。如果yaml格式错误在下方会有提示。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972972.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2786581571/p972954.png)
3. 也可以先创建工作流模板，修改参数后创建工作流。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972956.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972955.png)
4. 点击工作流进入详情可查看日志。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972974.png)
5. 在Azure存储账户中可看到state文件已经更新。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972957.png)

##### 使用API

- 根据工作流模板创建工作流：`POST https://118.31.xx.xx:2746/api/v1/workflows/argo/submit``# POST request body
{
 "resourceKind": "WorkflowTemplate",
 "resourceName": "terraform-workflow-nxbpp", # Template Name
 "submitOptions": {
 "labels": "workflows.argoproj.io/workflow-template=terraform-workflow-nxbpp",
 "parameters": [
 "region=cn-hangzhou",
 "uid=11409316xxxxxxxxx",
 "account_name=accountxxxx",
 "account_name_prefix=accountxxxx",
 "folder_id=fd-xxxxxx",
 "vpc_cidr_block=172.16.0.0/12",
 "switch_cidr_block=172.16.0.0/21",
 "zone_id=cn-hangzhou-b"
 ]
 }
}

# Response
{
 "metadata": {
 "name": "terraform-workflow-nxbpp-26xwc", # Workflow instance name
 "generateName": "terraform-workflow-nxbpp-",
 "namespace": "argo",
 "uid": "ee843f87-2f7a-4989-9808-68e64180e2ea",
 "resourceVersion": "393837",
 "generation": 1,
 "creationTimestamp": "2021-10-25T12:37:30Z",
 "labels": {
 "workflows.argoproj.io/creator": "system-serviceaccount-argo-argo-server",
 "workflows.argoproj.io/workflow-template": "terraform-workflow-nxbpp"
 }
 "xxx":"xxx"
 }
 "xxx":"xxx"
}`
- 查询工作流实例信息：`GET https://118.31.xx.xx:2746/api/v1/workflows/argo/terraform-workflow-sqgjc-pgrcq`
- 重新提交工作流实例：`PUT https://118.31.xx.xx:2746/api/v1/workflows/argo/terraform-workflow-sqgjc-pgrcq/resubmit`
- 全量API说明：https://118.31.xx.xx:2746/apidocs![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972975.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972958.png)

##### 权限认证

为提升安全性，包括页面及API都需要开启权限认证。

1. 执行下述代码，进行角色绑定并获取访问Token。`kubectl create sa sa-argo-server-admin -n argo
kubectl create rolebinding rb-argo-server-admin -n argo --role=argo-server-role --serviceaccount=argo:sa-argo-server-admin

SECRET=$(kubectl get sa sa-argo-server-admin -n argo -o=jsonpath='{.secrets[0].name}')
ARGO_TOKEN="Bearer $(kubectl get secret $SECRET -n argo -o=jsonpath='{.data.token}' | base64 --decode)"
echo $ARGO_TOKEN`
2. 重新部署argo-server，启用Token认证。将下述代码保存为argo-server.yaml，执行命令`kubectl apply -f argo-server.yaml`。`apiVersion: apps/v1
kind: Deployment
metadata:
 namespace: argo
 name: argo-server
spec:
 selector:
 matchLabels:
 app: argo-server
 template:
 metadata:
 labels:
 app: argo-server
 spec:
 containers:
 - args:
 - server
 - --namespaced
 - --auth-mode
 - client
 image: quay.io/argoproj/argocli:latest
 name: argo-server
 ports:
 - containerPort: 2746
 name: web
 readinessProbe:
 httpGet:
 path: /
 port: 2746
 scheme: HTTPS
 initialDelaySeconds: 10
 periodSeconds: 20
 securityContext:
 capabilities:
 drop:
 - ALL
 volumeMounts:
 - mountPath: /tmp
 name: tmp
 nodeSelector:
 kubernetes.io/os: linux
 securityContext:
 runAsNonRoot: true
 serviceAccountName: argo-server
 volumes:
 - emptyDir: {}
 name: tmp`
3. 再次访问公网地址`https://118.31.xx.xx:2746/workflows`会提示需要权限认证。将之前生成的Token粘贴到Token对话框中然后登录。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2786581571/p972976.png)
4. 使用API会提示需要Token，将Token添加到请求Header中，添加方式见代码示例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3786581571/p972961.png)`curl https://118.31.xx.xx:2746/api/v1/workflows/argo -k -H "Authorization: $ARGO_TOKEN"`

## 源代码

- 代码地址：[账号工厂GitHub](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/automation/account-factory)
- 代码目录结构说明：

```
├── extension           // 扩展目录，选用kms时需要根据实际情况调整目录下相关配置
├── modules             // 模块目录，本方案内无需修改
│   ├── role            // 创建角色相关的操作封装为模块便于使用，本方案内无需修改
│   │   ├── main.tf
│   │   ├── output.tf 
│   │   └── variables.tf
│   ├── idp             // 创建idp相关的操作封装为模块便于使用，本方案内无需修改
│   ├── policy          // 创建policy相关的操作封装为模块便于使用，本方案内无需修改
│   └── network         // 创建network相关的操作封装为模块便于使用，本方案内无需修改
├── step                 // 步骤目录
│   ├── account-create   // 创建账号步骤目录，本方案内无需修改
│   │   ├── main.tf      // Terraform入口执行文件
│   │   ├── backend.tf   // 用于配置state文件远端存储
│   │   ├── variables.tf // 输入变量定义
│   │   ├── outputs.tf   // 输出变量定义
│   │   └── version.tf   // 版本配置文件
│   ├── auth-authorize-role   // 角色及用户授权步骤目录，本方案内无需修改
│   ├── auth-create-idp       // 创建IDP步骤目录，本方案内无需修改
│   ├── auth-create-role      // 创建RAM角色步骤目录，本方案内无需修改
│   ├── auth-create-user      // 创建RAM用户步骤目录，本方案内无需修改
│   ├── network-create-vpc-vsw  // 创建VPC VSwitch步骤目录，本方案内无需修改
│   └── var                     // 步骤变量目录，步骤中生成、需要保存为本地文件供后续步骤使用的变量声明
│       ├── account.json.tmpl   // 保存成员账号信息的模板，创建账号的步骤中会进行值替换
│       ├── vpc.json.tmpl       // 保存VPC信息的模板，创建VPC的步骤中会进行值替换
│       └── vswitch.json.tmpl   // 保存VSwitch信息的模板，创建VSwitch的步骤中会进行值替换
├── backend.tfvars        // backend所需变量定义，本方案内需要根据实际情况修改
└── settings.tfvars       // 步骤运行所需业务固定变量定义，可以根据实际情况修改
```

## 故障排除

### Argo Workflows FAQ

详情参见[FAQ](https://argoproj.github.io/argo-workflows/faq/)。

### ACK集群异常

- [容器镜像仓库构建服务失败问题排查](https://help.aliyun.com/zh/acr/support/troubleshoot-issues-for-failure-to-create-images-in-container-registry)
- [容器镜像源代码仓库常见问题](https://help.aliyun.com/zh/acr/support/faq-about-source-code-repositories)
- [容器服务故障排查与常见问题](https://help.aliyun.com/zh/ack/support/troubleshooting-and-faq)

### 容器服务ACK应用故障排查

- Pod停留在Pending状态表示该Pod不能被调度到任何一个节点上，通常是因为集群中缺乏需要的资源导致。您可以通过**kubrctl describe pod**命令查看事件和排查。具体操作，请参见[Pod状态为Pending](https://help.aliyun.com/zh/ack/troubleshoot-application-issues-in-ack)。
- Pod停留在Waiting状态说明此Pod已经被调度到某个节点，但是却不能运行。通常是私有镜像、公网镜像拉取不成功或镜像地址不存在等问题导致。具体操作，请参见[Pod状态为Wating](https://help.aliyun.com/zh/ack/troubleshoot-application-issues-in-ack)。
- Pod不断被拉起但状态为Crashing或者Unhealthy通常表示Pod已经完成调度并启动，但是启动失败，通常是由配置、权限等问题造成。您可以查看容器的日志，以诊断容器中应用程序出现的问题。具体操作，请参见[Pod状态为Crash或者Unhealthy](https://help.aliyun.com/zh/ack/troubleshoot-application-issues-in-ack)。
- Pod状态为Running但是没有正常工作通常是由部署使用的YAML文件中存在的部分字段拼写错误造成的，您可以通过校验部署来进行故障排查。具体操作，请参见[Pod状态为Running但是没正常工作](https://help.aliyun.com/zh/ack/troubleshoot-application-issues-in-ack)。
- Service无法正常工作在排除网络插件自身的问题外，最可能的是**label**配置有问题，您可以通过查看**endpoints**进行故障排查。具体操作，请参见[检查Service](https://help.aliyun.com/zh/ack/troubleshoot-application-issues-in-ack)。

### 排查故障的经典步骤与常见原因

- ECS实例之间的互通是否有异常？具体操作，请参见[ECS实例间ping不通的排查思路](https://help.aliyun.com/zh/document_detail/185314.html)。
- 安全组是否配置有误？具体操作，请参见[安全组FAQ](https://help.aliyun.com/zh/ecs/user-guide/security-faq/)。关于如何配置ECS安全组，请参见[安全组应用指导和案例](https://help.aliyun.com/zh/ecs/user-guide/security-groups-for-different-use-cases)。
- 使用的RAM用户（即子账户）是否被正确授权？具体操作，请参见[为RAM用户授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-the-ram-user)。
- 采用**docker run**的方式执行命令，确认运行环境是否正常？
- 当集群异常时，是否可以使用kubectl命令登录集群？执行**kubectl get event**命令是否有异常？具体操作，请参见[通过kubectl工具连接集群](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster)。
- 在K8s里通过一个Pod去访问目标的Pod是否正常？具体操作，请参见[Pod访问其他节点上的Pod异常](https://help.aliyun.com/zh/document_detail/142373.html)。
- 通过Service方式访问应用是否正常？具体操作，请参见[通过使用已有SLB的服务公开应用](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-an-existing-slb-instance-to-expose-an-application)。
- 通过Ingress方式访问应用是否正常？具体操作，请参见[通过ALB Ingress访问服务](https://help.aliyun.com/zh/ack/serverless-kubernetes/user-guide/access-services-by-using-an-alb-ingress-2)。
- API Server、Scheduler或Controller日志是否有异常？
- Docker Daemon日志是否有异常？如果报错信息提示**docker daemon is not running**，您只需要在cmd.exe中执行，开启守护进程即可。

### 如何通过查看日志排查故障？

您可以通过以下命令查询日志信息，排查分析故障：

- 查看事件：**kubectl describe ******
- Docker引擎日志：**journalctl -u docker -f**
- Kubelet日志：**journalctl -u kubelet -f**
- API Server日志：**docker logs <api server container id>说明** 该命令用于查看专有集群的API Server日志，如果是托管集群，具体操作，请参见[收集托管集群控制平面组件日志](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/collect-control-plane-component-logs-of-ack-managed-cluster)。
- Scheduler日志：**docker logs <scheduler container id>**
- Worker proxy日志：**docker logs <worker proxy container id>**
- Master proxy日志：**docker logs <master proxy container id>**
- Controller日志：**docker logs <controller container id>**，**<controller container id>**涉及的组件包括kube-controller、alicloud-monitor-controller、alicloud-disk-controller和 cloud-controller。

## 相关内容

- [ACK常见问题](https://help.aliyun.com/zh/ack/faq-2)
- Terraform：[Alibaba Cloud Provider](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs)
- [Argo Workflows官网](https://argoproj.github.io/argo-workflows/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-60（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
