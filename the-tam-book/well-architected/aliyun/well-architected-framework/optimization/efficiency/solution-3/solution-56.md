<!-- source: https://help.aliyun.com/zh/well-architected/solution-56 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929458 -->

# 基础设施自动化流水线

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3686581571/p972769.png)

本文提供一种基础架构代码配置CI/CD的解决方案，使用Terraform作为IaC语言，并整合[Jenkins](https://www.jenkins.io/doc/)和Git实现Terraform代码的持续集成和版本控制。结合阿里云OSS和OTS产品，对Terraform的状态文件（state文件）进行远端存储和加锁，实现多人协作。同时，集成第三方开源插件Terraform-compliance，实现对Terraform代码的合规审计操作，减小创建不安全资源带来的安全风险。

## 方案优势

### 基础设施代码化

基于IaC思想，将基础设施代码使用[Terraform](https://www.terraform.io/)规范化，流水线运行使用版本化管理的Terraform代码，代码可扩展并减轻运维管理负担。

### 自动化集成及合规检测

代码提交后可自动运行流水线，流水线集成合规规则进行检测，保障Terraform合规。

## 客户场景

### 自动化管理基础设施配置变更

#### 场景描述

基础设施即代码，所有对基础设施的改动都可通过代码实现。代码每次变更都会触发pipeline的部署。这既减小了手动部署的工作，也确保在不同运行环境下基础架构保证统一。

#### 适用客户

希望使用Terraform自动化管理基础设施的企业客户。

## 方案架构

本方案主要目的是指导企业客户搭建一套管理Terraform代码变更的流水线。使用Git仓库管理Terraform代码，使用Jenkins进行CI/CD集成，使用Terraform-compliance插件进行合规审计，使用OSS + OTS作为Remote Backend实现多人协作及State文件安全。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3686581571/p972770.png)

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
| RAM用户 | RAM用户是RAM的一种实体身份类型，有确定的身份ID和身份凭证，它通常与某个确定的人或应用程序一一对应。因安全原因不推荐直接使用云账号的AK/SK。因此在账号下创建一个RAM用户，授予RAM用户最小权限，使用该RAM用户的AK/SK。 |
| State文件 | Terraform中用于描述当前资源配置的文件，详情参见[State](https://www.terraform.io/language/state)。本文使用OSS + OTS作为State文件的远端存储，详情参见[OSS Backend](https://www.terraform.io/language/settings/backends/oss)。 |

## 安全性

### Jenkins安全性

- Jenkins需要进行安全加固，安全性详情参考官方文档[Securing Jenkins](https://www.jenkins.io/doc/book/security/)。
- 当使用Jenkins并拥有大量用户及并发任务等情况时参考官方文档[Scaling Jenkins](https://www.jenkins.io/doc/book/scaling/)。

### Terraform State文件安全

使用OSS作为Backend保存Terraform State文件，使用OTS支持State文件加锁及一致性检查，详情参见[OSS Backend](https://www.terraform.io/language/settings/backends/oss)。

### Docker安全性

Docker安全性详情参见官方文档[Security](https://docs.docker.com/engine/security/)。

### AccessKey使用

资源操作的云账号下RAM用户AK至少需要拥有AliyunOSSFullAccess和AliyunOTSFullAccess权限，用于读写账号下的OSS和OTS实例，并根据实际情况添加要操作的云资源的权限。

## 注意事项

### ECS使用限制

ECS存在一些产品功能和服务性能等限制，详情参见[使用限制](https://help.aliyun.com/zh/ecs/user-guide/limitations)。

### OSS使用限制

OSS使用限制及性能指标详情参见[使用限制](https://help.aliyun.com/zh/oss/user-guide/limits)。

### OTS使用限制

OTS使用限制详情参见[使用限制](https://help.aliyun.com/zh/tablestore/limits)。

## 实施步骤

### 实施准备

- 账号下已有RAM用户并已创建AccessKey，该RAM用户至少需要拥有AliyunOSSFullAccess和AliyunOTSFullAccess，用于读写账号下的OSS和OTS实例。
- 账号已开通服务并创建一台ECS，ECS上已[安装Jenkins](https://www.jenkins.io/doc/book/installing/)及[Docker](https://docs.docker.com/engine/install/)。
- 已开通OSS及OTS服务，OSS服务用于存储Terraform的state文件，OTS服务用于对state文件加锁，保证多人协作。
- 通过[ACR](https://help.aliyun.com/zh/acr/product-overview/what-is-container-registry)能够拉取到Docker镜像。本文中使用的Docker镜像已打包存储在阿里云镜像服务ACR之中，可通过 `registry.cn-hangzhou.aliyuncs.com/terraform/terraform-docker-hub:v1` 路径拉取，该镜像的Dockerfile如下所示，用户可根据自身需要修改并重新打包使用。`FROM alpine:3.14

ENV TERRAFORM_PLUGIN_DIR=/srv/terraform-plugins
ENV TF_PLUGIN_CACHE_DIR=${TERRAFORM_PLUGIN_DIR}
ENV TERRAFORM_VERSION=1.0.2
ENV TERRAFORM_PROVIDER_ALICLOUD_VERSION=1.127.0
ENV TERRAFORM_PROVIDER_LOCAL_VERSION=2.1.0
ENV TERRAFORM_PROVIDER_EXTERNAL_VERSION=2.1.0
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

 && mkdir -p ${TERRAFORM_PLUGIN_DIR}/registry.terraform.io/hashicorp/external/${TERRAFORM_PROVIDER_EXTERNAL_VERSION}/linux_amd64 \
 && wget https://releases.hashicorp.com/terraform-provider-external/${TERRAFORM_PROVIDER_EXTERNAL_VERSION}/terraform-provider-external_${TERRAFORM_PROVIDER_EXTERNAL_VERSION}_linux_amd64.zip \
 && unzip terraform-provider-external_${TERRAFORM_PROVIDER_EXTERNAL_VERSION}_linux_amd64.zip -d ${TERRAFORM_PLUGIN_DIR}/registry.terraform.io/hashicorp/external/${TERRAFORM_PROVIDER_EXTERNAL_VERSION}/linux_amd64 \
 
 && rm -rf *.zip`
- Jenkins上已安装如下插件：
- Git：让Git和Jenkins结合
- Pipeline：Jenkins核心功能，Jenkins根据Jenkinsfile自动执行编译打包等操作
- Docker：让Jenkins与Docker结合
- Docker Pipeline：在Pipeline中使用Docker容器
- Blue Ocean：提供更加友好的Jenkins UI界面，代码更好的用户体验
- 已拥有Git仓库，并在Jenkins中添加git仓库的访问凭证。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3686581571/p972772.png)

### 操作步骤

#### 配置Terraform远端存储

1. 登录阿里云[OSS控制台](https://oss.console.aliyun.com/overview)，在对应的地域下创建Bucket。建议开启版本控制功能，便于state文件的恢复。记录下Bucket的名称和endpoint。
2. 登录阿里云[OTS控制台](https://otsnext.console.aliyun.com/)，在对应地域下创建表格存储实例，可根据自身需要选择预留模式或者按量模式。
3. 创建完成后进入OTS实例，在实例中创建数据表。**注意：**数据表中必须含有一个名为LockID，字符串类型的主键。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3686581571/p972774.png)

#### 编写Terraform代码

1. 编写Terraform backend文件，将上述记录的参数填写到backend.tf文件中。其中：access_key和secret_key为存储OSS的账号子用户AK；key为将要保存的state文件名称，对于不同state配置而言，key值必须不同，否则会出现配置覆盖的情况；tablestore_endpoint和tablestore_table为步骤3中创建的数据表实例的入口。详细参数说明可[参考文档](https://www.terraform.io/docs/language/settings/backends/oss.html)`terraform {
 backend "oss" {
 bucket = "bucket-with-terraform-state"
 prefix = "path/mystate"
 key = "terraform-state.tfstate"
 region = "cn-hangzhou"
 tablestore_endpoint = "https://xxxx.cn-hangzhou.ots.aliyuncs.com"
 tablestore_table = "statelock"
 access_key = "****************"
 secret_key = "**********************"
 endpoint = "oss-cn-hangzhou.aliyuncs.com"
 }
}`

1. 根据业务需求，编写用户自定义的Terraform代码，并上传到前序工作中的Git仓库。本文以创建RAM角色，并为角色赋权为例。其他资源配置详情参见[Alibaba Cloud Provider](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs)。`provider "alicloud" {
 access_key = "LTA****************"
 secret_key = "tQW**********************"
 region = "cn-hangzhou"
}

resource "alicloud_ram_role" "ram_role" {
 name = "tf-pipeline-test"
 description = "test terraform pipeline"
 document = <<EOF
 {
 "Statement": [
 {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
 "RAM": [
 "acs:ram::195**********:root"
 ]
 }
 }
 ],
 "Version": "1"
 }
 EOF
 force = true
}

resource "alicloud_ram_role_policy_attachment" "ram_role_attach_policies" {
 policy_name = "AliyunLogFullAccess"
 policy_type = "System"
 role_name = alicloud_ram_role.ram_role.name
}`

#### 配置合规审计规则

1. 我们选择 `terraform-compliance` 作为合规审计插件，该插件已经安装在docker镜像中，之后将使用docker直接运行pipeline，因此无需提前安装。若用户希望自定义安装，可参考[安装文档](https://terraform-compliance.com/pages/installation/)
2. terraform-compliance使用Behavior-Driven Development<BDD>编写合规规则。BDD提供了很好的自我描述能力以及很强的理解性，能够让非技术人员很轻松地编写规则和阅读测试结果。例如，我们编写如下规则：“不允许给任何RAM角色赋予AdministratorAccess”。`Feature: Test terraform-compliance

Scenario: Ensure that ram_role_policy could not be AdministratorAccess
 Given I have alicloud_ram_role_policy_attachment defined
 Then it must contain policy_name
 And its value must not be AdministratorAccess`Feature：功能，下面可以由多个ScenarioScenario：场景，下面可以由多个StepsSteps：步骤使用Given、When、Then、But、And这些关键词，真正进行合规配置的字段。详细语法可参考[BDD文档](https://terraform-compliance.com/pages/bdd-references/)

1. 规则编写完成后，可以将规则上传到Git仓库。建议Terraform代码和合规规则使用不同的Git仓库存储，分别由开发人员和审计人员管理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3686581571/p972771.png)

#### 配置Pipeline

1. 登录Jenkins页面，点击“New Item”，创建流水线项目![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3686581571/p972773.png)
2. 点击上方“Pipeline”，编写Jenkinsfile流水线脚本。用户可根据自身需要选择直接在Jenkins上填写或者在项目中使用Jenkinsfile。流水线脚本如下所示：`pipeline {
 agent {
 docker {
 image 'registry.cn-hangzhou.aliyuncs.com/terraform/terraform-docker-hub:v1'
 }
 }
 stages {
 stage('Git Checkout'){
 steps{
 git branch: 'main', credentialsId: 'xxx-github', url: 'git@github.com:xxx/Terraform2.git'
 dir('features') {
 git credentialsId: 'xxx-github', url: 'git@github.com:xxx/features.git'
 }
 }
 }
 stage('Terraform Init') {
 steps{
 sh 'terraform init -plugin-dir=/srv/terraform-plugins'
 }
 }
 stage('Terraform validate') {
 steps{
 sh 'terraform validate'
 }
 }
 stage('Terraform Plan') {
 steps{
 sh 'terraform plan -out tf.out'
 }
 }
 stage('合规审查') {
 steps{
 sh 'terraform-compliance -f features -p tf.out'
 }
 }
 stage('Terraform Apply') {
 steps{
 sh 'terraform apply --auto-approve'
 }
 }
 }
 post {
 always {
 deleteDir()
 }
 }
}`docker image使用的是阿里云容器镜像服务，镜像中已安装Terraform，aliyun Provider，terraform-compliance等插件，可直接用于运行Terraform代码。第一步：分别从Git仓库分别拉取terraform代码和合规规则，并将合规规则存放在 `./features` 文件夹中。可以使用Pipeline Syntax工具生成Git语句。第二步：初始化Terraform环境，为加快初始化速度，建议将常用的插件提前下载在指定路径，插件下载详情参见[下载地址](https://releases.hashicorp.com/)。**注意：**出于**安全**和**网络**方面的考虑，本文中使用 `-plugin-dir` 参数指定了插件安装的地址（docker镜像中插件安装在 `/srv/terraform-plugins` 文件夹下），如果所需插件在该文件夹下不存在，会报“插件未找到”的错误。若允许开发人员执行任意插件且网络畅通，可以使用缓存来加速Terraform init，具体可参考[文档](https://developer.aliyun.com/article/723935)。第三步：检查Terraform语法是否正确第四步：使用Terraform plan命令，检查state文件和当前Terraform代码的配置差异，并将更改信息写入tf.out文件。第五步：使用Terraform-compliance插件进行合规审查， `-f` 参数指定合规审查规则的路径， `-p` 参数指定plan后的.out文件路径。当上述流程全部成功后，执行Terraform代码。执行完成后，最后在ECS上将该Pipeline的工作空间删除。

#### 运行pipeline

1. 在JenkIns左侧边栏点击“Open Blue Ocean”，进入Blue Ocean页面。点击“运行”按钮，运行该pipeline。运行过程中可能出现jenkins权限不足的问题，注意为jenkins用户所在的用户组授予访问docker的权限。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3686581571/p972775.png)
2. 运行完成后，查看每一个节点的运行日志。其中“合规审查”中可以看见合规审查的结果，由于我们给RAM用户授权的并非“AdministratorAccess”，因此合规审查通过。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3686581571/p972776.png)
3. 当我们将RAM用户的权限修改为“AdministratorAccess”时，重新将Terraform代码push到Git仓库，再次执行该流水线，会发现合规审查无法通过。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3686581571/p972777.png)
4. 至此，我们完成一个简易的Terraform流水线，用户可根据自身需求，修改Terraform代码、合规规则以及流水线的步骤。

#### 发送邮件

##### Jenkins邮件配置

1. 点击左侧菜单栏“Manage Jenkins”-“Configure System”。填写“Jenkins Location”下的“System Admin e-mail address”。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3686581571/p972778.png)
2. 填写“E-mail Notification”下的参数，该参数与所使用的邮箱有关。以QQ邮箱为例，配置如下图所示：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3686581571/p972779.png)
3. 我们可以勾选“Test configuration by sending test e-mail”选项，测试能否成功发送邮件。

##### Pipeline新增邮件发送步骤

1. 在Pipeline的post中添加以下代码，表示当Pipeline执行成功后发送邮件。`post {
 success {
 echo 'successful,and send mail'
 mail body: 'current job ok', from: 'xxxx@qq.com', subject: 'account baseline success', to: 'xxx@gmail.com'
 }
 }`
2. 执行该流水线，成功后查看目标邮箱是否收到邮件。

## 故障排除

### Jenkins

Jenkins相关故障排除请参见[官网](https://www.jenkins.io/doc/)。

### Terraform

Terraform相关问题参见[官方文档](https://www.terraform.io/docs)。

## 相关内容

- [Jenkins官方文档](https://www.jenkins.io/doc/)
- [阿里云开放平台Terraform](https://open.aliyun.com/tools/terraform)
- Terraform：[Alibaba Cloud Provider](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs)
- [terraform-compliance](https://terraform-compliance.com/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-56（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
