<!-- source: https://help.aliyun.com/zh/well-architected/solution-58 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929404 -->

# 基于Jenkins实现账号工厂

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7686581571/p971661.png)

当企业开通[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)，将已有阿里云账号邀请进来，或者通过新建成员账号的方式开展新的业务，那么不同账号之间的统一权限管理就会显得尤为重要，如果是在这些账号内手工创建 RAM 角色，则无法保证权限统一，后续修改维护困难，本文档则介绍了一种通过[Jenkins](https://www.jenkins.io/doc/) + [Docker](https://docs.docker.com/get-started/overview/) + [Terraform](https://www.terraform.io/) 自动化为所有成员账号创建RAM 角色、权限及VPC等统一基线的方法。

## 方案优势

### 账号统一基线

账号工厂通过同一工作流模板生产成员账号，能够确保新账号都包含流水线中定义的统一基线，根据基线内容保障新账号权限安全。

### 基础设施代码化

基于IaC思想，将资源目录中成员账号的配置过程使用[Terraform](https://www.terraform.io/)规范化，每次创建成员账号时使用同一份Terraform代码，保证所有成员账号权限统一，减轻运维管理负担。

### 灵活可扩展

Terraform及工作流代码可拓展，用户可根据需求拓展功能，提供更多的基线配置。[Jenkins](https://www.jenkins.io/doc/)为应用广泛的开源CI/CD产品，可提供API与企业内部DevOps平台集成。

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

本方案使用Terraform自动化执行，整合Jenkins + Docker搭建Terraform的执行环境，实现了Terraform的CI/CD集成。本方案中在ECS中部署Jenkins及Docker，在Docker中运行Terraform等账号基线Pipeline步骤，Terraform的State文件使用OSS + OTS作为服务远端存储（Remote Backend）并支持加锁，保证State文件安全。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7686581571/p971662.png)

以下的流程图描述了该方案的执行步骤，首先使用**企业管理主账号**下的**RAM用户**（子用户）AK信息，通过Terraform脚本登录到企业管理主账号，并在指定的资源夹下创建新的「成员账号」。之后扮演成员账号下的ResourceDirectoryAccountAccessRole角色，该角色会在成员账号加入RD时自动创建，并拥有云管理员（AdministratorAccess）权限。登录到成员账号后，会在成员账号下进行**权限配置**——创建IDP和相关RAM角色、创建一个用于执行Tarraform脚本的RAM用户并为上述角色和用户绑定权限策略。最后会在成员账号下进行**网络配置**——根据用户指定数据创建VPC和交换机。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7686581571/p971660.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 访问控制RAM | [访问控制](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)使您能够安全地集中管理对阿里云服务和资源的访问。您可以使用RAM创建和管理用户和组，并使用各种权限来运行或访问他们对云资源的访问。 | 免费。 |
| 容器镜像服务ACR | [容器镜像服务ACR](https://help.aliyun.com/zh/acr/product-overview/what-is-container-registry)提供安全地镜像托管能力，稳定的国内外镜像构建服务，便捷的镜像授权功能，方便用户进行镜像全生命周期管理。 | 企业版收费，详情见[产品计费](https://help.aliyun.com/zh/acr/product-overview/pricing/)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是阿里云提供的性能卓越、稳定可靠、弹性扩展的IaaS（Infrastructure as a Service）级别云计算服务 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 对象存储OSS | [对象存储OSS（Object Storage Service](https://help.aliyun.com/zh/oss/user-guide/what-is-oss)）是阿里云提供的海量、安全、低成本、高持久的云存储服务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/oss/billing/)。 |
| 表格存储OTS | [表格存储（Tablestore）](https://help.aliyun.com/zh/tablestore/table-store-service/product-overview/what-is-tablestore)是阿里云自研的多模型结构化数据存储，提供海量结构化数据存储以及快速的查询和分析服务。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/tablestore/table-store-service/product-overview/billing/)。 |
| Jenkins | [Jenkins](https://www.jenkins.io/doc/)是应用广泛的开源自动化CI/CD产品。 | 免费。 |
| Docker | [Docker](https://docs.docker.com/get-started/overview/)容器化技术，用于支持创建和使用容器，实现对容器的高效创建、部署及复制，并能将其从一个环境顺利迁移至另一个环境，从而有助于针对云优化应用。 | 高级版收费，详情参见[Pricing](https://www.docker.com/pricing)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| RAM用户 | RAM用户是RAM的一种实体身份类型，有确定的身份ID和身份凭证，它通常与某个确定的人或应用程序一一对应。因安全原因不推荐直接使用云账号的AK/SK。因此在账号下创建一个RAM用户，授予RAM用户最小权限，使用该RAM用户的AK/SK。 |
| 成员账号 | 在资源目录中受「企业管理主账号」邀请或被创建的其他账号，每一个成员账号均为一个独立的账号，拥有自己的云资源，企业可根据职责划分为不同的账号，由企业管理主账号统一管理。 |
| State文件 | Terraform中用于描述当前资源配置的文件，详情参见[State](https://www.terraform.io/language/state)。本文使用OSS + OTS作为State文件的远端存储，详情参见[OSS Backend](https://www.terraform.io/language/settings/backends/oss)。 |

## 安全性

### 资源目录权限

资源目录服务关联角色（AliyunServiceRoleForResourceDirectory）为资源目录集成服务提供可信访问通道，详情参见[资源目录服务关联角色](https://help.aliyun.com/zh/resource-management/security-and-compliance/ram-roles-in-a-resource-directory)。

### Jenkins安全性

- Jenkins需要进行安全加固，安全性详情参考官方文档[Securing Jenkins](https://www.jenkins.io/doc/book/security/)。
- 当使用Jenkins并拥有大量用户及并发任务等情况时参考官方文档[Scaling Jenkins](https://www.jenkins.io/doc/book/scaling/)。

### Terraform State文件安全

使用OSS作为Backend保存Terraform State文件，使用OTS支持State文件加锁及一致性检查，详情参见[OSS Backend](https://www.terraform.io/language/settings/backends/oss)。

### Docker安全性

Docker安全性详情参见官方文档[Security](https://docs.docker.com/engine/security/)。

### AccessKey使用

需要使用企业管理主账号下RAM用户的AccessKey，用于创建账号及操作阿里云资源。该RAM用户拥有 AliyunResourceDirectoryFullAccess和AliyunSTSAssumeRoleAccess两个权限。

## 注意事项

### 资源目录使用限制

资源目录及资源共享使用限制详情参见[使用限制](https://help.aliyun.com/zh/resource-management/product-overview/limits)。

### ECS使用限制

ECS存在一些产品功能和服务性能等限制，详情参见[使用限制](https://help.aliyun.com/zh/ecs/user-guide/limitations)。

### OSS使用限制

OSS使用限制及性能指标详情参见[使用限制](https://help.aliyun.com/zh/oss/user-guide/limits)。

### OTS使用限制

OTS使用限制详情参见[使用限制](https://help.aliyun.com/zh/tablestore/limits)。

## 实施步骤

### 实施准备

- 已拥有一台可连通公网的ECS（本方案使用操作系统CentOS），ECS中已[安装Jenkins](https://www.jenkins.io/doc/book/installing/)及[Docker](https://docs.docker.com/engine/install/)，并且在Jenkins中已安装Docker插件。
- 确保已在「企业管理主账号」（也可使用其他账号）OSS下创建用于存储Terraform state文件的**Bucket**，并且在OTS中创建一张**主键名为LockID，类型为String**的数据表，用于作为Terraform state文件的锁。记录下Bucket和数据表的**名称**和**endpoint**。
- 确保在「企业管理主账号」中，存在一个「RAM用户」AK，且该用户拥有 AliyunResourceDirectoryFullAccess和AliyunSTSAssumeRoleAccess两个权限；在后续的步骤中，我们将使用该RAM用户及其AK。
- 确定工作流及Terraform输入参数，输入参数分为两部分：第一部分为**全局参数**，需写入源代码中的settings.tfvars文件，每次流水线执行时均保持一致；第二部分为**执行参数**，执行流水线时动态填写，不会保存。**全局参数**encodedsaml_metadata_document：企业IDP的元文件，用于在阿里云上创建IDPsso_provider_name：创建的IDP的名称ram_roles：需要创建的ram角色列表，示例中包括只读和管理员角色user_name：用于执行TF脚本的角色名称policy_name：自定义权限策略的名称policy_document：自定义权限策略内容attach_roles：自定义权限策略绑定的角色列表attach_users：自定义权限策略绑定的用户列表reader_name：需要绑定权限策略的只读角色名称reader_policy_type：为只读角色绑定的权限策略的类型reader_policy_name：为只读角色绑定的权限策略的名称vpc_name：创建的vpc的名称vswitch_name：vpc下交换机的名称**执行参数**account_name：新创建账号的显示名称account_name_prefix：新创建账号的账号标识uid: 「企业管理主账号」uidaccess_key：「企业管理主账号」下RAM用户的AKsecret_key：「企业管理主账号」下RAM用户的SKfolder_id：新创建的成员账号所属资源夹IDvpc_cidr_block：VPC的网段switch_cidr_block：交换机的网段region：区域信息，如cn-hangzhouzone_id：可用区ID，如cn-hangzhou-b
- 完成镜像构建，并通过容器镜像服务ACR能够拉取到镜像，我们将使用ACR中的`registry.cn-hangzhou.aliyuncs.com/terraform/terraform-docker-hub:v1`镜像运行Terraform代码，用户可根据自身需求打包镜像，该镜像的Dockerfile如下所示：`FROM alpine:3.14

ENV TERRAFORM_PLUGIN_DIR=/srv/terraform-plugins
ENV TF_PLUGIN_CACHE_DIR=${TERRAFORM_PLUGIN_DIR}
ENV TERRAFORM_VERSION=1.0.2
ENV TERRAFORM_PROVIDER_ALICLOUD_VERSION=1.127.0
ENV TERRAFORM_PROVIDER_LOCAL_VERSION=2.1.0
ENV PATH="/opt/venv/bin:$PATH"

RUN apk add libxml2-dev libxslt-dev python3-dev gcc build-base wget unzip git bash \
 && python3 -m venv /opt/venv \
 && pip install terraform-compliance \
 && pip install checkov \

 && wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
 && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin/ \

 && mkdir -p ${TERRAFORM_PLUGIN_DIR}/registry.terraform.io/aliyun/alicloud/${TERRAFORM_PROVIDER_ALICLOUD_VERSION}/linux_amd64 \
 && wget https://releases.hashicorp.com/terraform-provider-alicloud/${TERRAFORM_PROVIDER_ALICLOUD_VERSION}/terraform-provider-alicloud_${TERRAFORM_PROVIDER_ALICLOUD_VERSION}_linux_amd64.zip \
 && unzip terraform-provider-alicloud_${TERRAFORM_PROVIDER_ALICLOUD_VERSION}_linux_amd64.zip -d ${TERRAFORM_PLUGIN_DIR}/registry.terraform.io/aliyun/alicloud/${TERRAFORM_PROVIDER_ALICLOUD_VERSION}/linux_amd64 \

 && mkdir -p ${TERRAFORM_PLUGIN_DIR}/registry.terraform.io/hashicorp/local/${TERRAFORM_PROVIDER_LOCAL_VERSION}/linux_amd64 \
 && wget https://releases.hashicorp.com/terraform-provider-local/${TERRAFORM_PROVIDER_LOCAL_VERSION}/terraform-provider-local_${TERRAFORM_PROVIDER_LOCAL_VERSION}_linux_amd64.zip \
 && unzip terraform-provider-local_${TERRAFORM_PROVIDER_LOCAL_VERSION}_linux_amd64.zip -d ${TERRAFORM_PLUGIN_DIR}/registry.terraform.io/hashicorp/local/${TERRAFORM_PROVIDER_LOCAL_VERSION}/linux_amd64 \
 
 && rm -rf *.zip`

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：45分钟。

### 操作步骤

#### 配置参数

1. 下载本文**源代码章节**中的账号工厂代码，目录结构参考相应说明。
2. 使用编辑器打开 `backend.tfvars`文件，修改该文件内的配置项：bucket：实施准备中在OSS中创建的**Bucket名称。**prefix：OSS中State文件存储路径，可以根据实际情况修改。region：OSS存储地区，注意和实施准备中的地域一致。tablestore_endpoint：OTS的访问入口，可在OTS实例页面上查到。根据网络情况选择入口地址。tablestore_table：实施准备中创建的OTS数据表**实例名称。**access_key：OSS/OTS在企业管理主账号时不需要填写，不在企业管理主账号时需要填写相应账号RAM用户的AccessKey，该用户需要**拥有OSS/OTS的读写权限。**secret_key：OSS/OTS在企业管理主账号时不需要填写，不在企业管理主账号时需要填写相应账号RAM用户的SecretKey。endpoint：OSS访问入口，注意和实施准备中的地域一致。
3. 用编辑器打开`settings.tfvars`文件，根据配置文件注释和前提条件中的全局参数填写。

#### 使用Jenkins完成CI/CD

1. 在Jenkins pipeline中选择`带有参数的项目`，在运行pipeline时传入实施准备中的**执行参数**。参数配置与执行参数定义保持一致。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7686581571/p971663.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7686581571/p971664.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7686581571/p971679.png)
2. Terraform代码上传到Github或者自建Git仓库中。获取访问Git仓库的访问凭证，并将访问凭证添加到Jenkins中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7686581571/p971666.png)
3. 在Jenkins中创建流水线，流水线的Jenkinsfile如下所示。根据实际情况修改Jenkinsfile中的image配置，修改**环境准备**中的**Git路径**和**凭证**。`pipeline {
 agent {
 docker {
 image 'registry.cn-hangzhou.aliyuncs.com/terraform/terraform-docker-hub:v1'
 args '-e ALICLOUD_ACCESS_KEY=$access_key -e ALICLOUD_SECRET_KEY=$secret_key -e ALICLOUD_REGION=$region'
 }
 }
 stages {
 stage('环境准备'){
 steps{
 git credentialsId: 'yf01-aliyun-code-repo', url: 'git@codeup.aliyun.com:xxxx/account-base.git'
 }
 }
 stage('创建账号') {
 steps{
 sh 'cd step/account-create && terraform init -backend-config="key=$uid-$account_name-account-create" -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins'
 sh 'cd step/account-create && terraform apply --auto-approve -var "folder_id=$folder_id" -var "account_name=$account_name" -var "account_name_prefix=$account_name_prefix"'
 }
 }
 stage('权限配置:创建IDP') {
 steps{
 sh 'cd step/auth-create-idp && terraform init -backend-config="key=$uid-$account_name-auth-create-idp" -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins'
 sh 'cd step/auth-create-idp && terraform apply --auto-approve -var-file=../../settings.tfvars -compact-warnings'
 }
 }
 stage('权限配置:创建角色') {
 steps{
 sh 'cd step/auth-create-role && terraform init -backend-config="key=$uid-$account_name-auth-create-role" -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins'
 sh 'cd step/auth-create-role && terraform apply --auto-approve -var-file=../../settings.tfvars -compact-warnings'
 }
 }
 stage('权限配置:创建TF用户') {
 steps{
 sh 'cd step/auth-create-user && terraform init -backend-config="key=$uid-$account_name-auth-create-user" -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins'
 sh 'cd step/auth-create-user && terraform apply --auto-approve -var-file=../../settings.tfvars -compact-warnings'
 }
 }
 stage('权限配置:角色授权') {
 steps{
 sh 'cd step/auth-authorize-role && terraform init -backend-config="key=$uid-$account_name-auth-authorize-role" -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins'
 sh 'cd step/auth-authorize-role && terraform apply --auto-approve -var-file=../../settings.tfvars -compact-warnings'
 }
 }
 stage('网络配置') {
 steps{
 sh 'cd step/network-create-vpc-vsw && terraform init -backend-config="key=$uid-$account_name-network-create-vpc-vsw" -backend-config=../../backend.tfvars -reconfigure -plugin-dir=/srv/terraform-plugins'
 sh 'cd step/network-create-vpc-vsw && terraform apply --auto-approve -compact-warnings -var "vpc_cidr_block=$vpc_cidr_block" -var "switch_cidr_block=$switch_cidr_block" -var "zone_id=$zone_id" -var-file=../../settings.tfvars'
 }
 }
 }
}`
4. 运行该流水线，运行完成后会在Jenkins中打印每个步骤的执行结果和日志。当在资源目录中新增成员账号、或者修改了配置项中的内容时，上传到Git仓库后重新运行流水线即可。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7686581571/p971665.png)

#### 使用API

配置完成后可以通过REST API直接操作Jenkins，便于与企业内部系统集成：

- 与Jenkins进行验证，在Jenkins 账号中新增API Token。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7686581571/p971668.png)
- 之后在请求头中，添加该API Token即可使用该账号操作Jenkins，例如：`curl -H "Authorization: Basic YWRtaW46MTE3M*********==" http://{Jenkins地址}/blue/rest/organizations/jenkins/pipelines/{pipeline名称}/`
- **获取**指定pipeline的**详细信息**`GET http://{Jenkins地址}/blue/rest/organizations/jenkins/pipelines/{pipeline名称}/`
- **运行**该pipeline，如果有输入参数，通过传如下json格式数据执行。`POST http://{Jenkins地址}/blue/rest/organizations/jenkins/pipelines/{pipeline名称}/runs/``{
 "parameters" : [{
 "name" : "******",
 "value" : "****"
 }, {
 "name" : "******",
 "value" : "****"
 }]
}`
- **获取**该pipeline的**执行结果**，执行后可获取到本次执行的**执行id**，用于获取本次执行的结果。`GET http://{Jenkins地址}/blue/rest/organizations/jenkins/pipelines/{pipeline名称}/runs/{执行id}`
- **获取**该pipeline的**执行日志**：`GET http://{Jenkins地址}/blue/rest/organizations/jenkins/pipelines/{pipeline名称}/runs/{执行id}/log`
- **获取**该pipeline**每一个node的执行结果**，可以获取到失败的node id，从该步**重新运行**。`GET http://{Jenkins地址}/blue/rest/organizations/jenkins/pipelines/{pipeline名称}/runs/{执行id}/nodes`
- 从指定的node**重新执行**pipeline`GET http://{Jenkins地址}/blue/rest/organizations/jenkins/pipelines/{pipeline名称}/runs/{执行id}/nodes/{node id}/restart/`

## 源代码

- 代码地址：[账号工厂GitHub](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/automation/account-factory)
- 代码目录结构说明：

```
├── modules             // 模块目录，本方案内无需修改
│   ├── role            // 创建角色相关的操作封装为模块便于使用，本方案内无需修改
│   │   ├── main.tf
│   │   ├── output.tf 
│   │   └── variables.tf
│   ├── idp             // 创建idp相关的操作封装为模块便于使用，本方案内无需修改
│   ├── policy          // 创建policy相关的操作封装为模块便于使用，本方案内无需修改
│   └── network         // 创建network相关的操作封装为模块便于使用，本方案内无需修改
├── step                 // 步骤目录
│   ├── account-create   // 创建账号步骤目录，本方案内无需修改
│   │   ├── main.tf      // Terraform入口执行文件
│   │   ├── backend.tf   // 用于配置state文件远端存储
│   │   ├── variables.tf // 输入变量定义
│   │   ├── outputs.tf   // 输出变量定义
│   │   └── version.tf   // 版本配置文件
│   ├── auth-authorize-role   // 角色及用户授权步骤目录，本方案内无需修改
│   ├── auth-create-idp       // 创建IDP步骤目录，本方案内无需修改
│   ├── auth-create-role      // 创建RAM角色步骤目录，本方案内无需修改
│   ├── auth-create-user      // 创建RAM用户步骤目录，本方案内无需修改
│   ├── network-create-vpc-vsw  // 创建VPC VSwitch步骤目录，本方案内无需修改
│   └── var                     // 步骤变量目录，步骤中生成、需要保存为本地文件供后续步骤使用的变量声明
│       ├── account.json.tmpl   // 保存成员账号信息的模板，创建账号的步骤中会进行值替换
│       ├── vpc.json.tmpl       // 保存VPC信息的模板，创建VPC的步骤中会进行值替换
│       └── vswitch.json.tmpl   // 保存VSwitch信息的模板，创建VSwitch的步骤中会进行值替换
├── backend.tfvars        // backend所需变量定义，本方案内需要根据实际情况修改
└── settings.tfvars       // 步骤运行所需业务固定变量定义，可以根据实际情况修改
```

## 故障排除

### Jenkins

Jenkins相关故障排除请参见[官网](https://www.jenkins.io/doc/)。

### 资源目录

资源目录常见问题详情参见[常见问题](https://help.aliyun.com/zh/resource-management/resource-directory/support/faq/)。

## 相关内容

- [Jenkins官方文档](https://www.jenkins.io/doc/)
- Terraform：[Alibaba Cloud Provider](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-58（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
