<!-- source: https://help.aliyun.com/zh/well-architected/solution-131 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929467 -->

# 容器CI/CD方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972906.png)

为确保环境权限的完全隔离，更多企业会选择多个账号构建多个集群，负责不同的业务和功能需求。在跨账号多集群的环境下，运维部署操作变得繁琐和冗余，并且手动操作难以确保环境的统一。

本文档则介绍了一种通过云效、容器服务ACK和容器镜像服务ACR，构建容器CI/CD流水线，实现镜像构建和部署的自动化。

## 方案优势

### 自动化构建

通过云效流水线实现镜像构建以及部署自动化，减小运维成本，并提高部署以及交付的效率。

### 多账号多集群

基于多账号多集群的环境，各个账号负责不同的业务和功能需求，同时在特定账号下创建对应职能的容器集群，实现集群间的完全隔离。

## 客户场景

### 多账号多集群容器部署

#### 场景描述

业务运行在多个账号下的多个集群中，需要使用CI/CD流水线实现自动化部署。

#### 适用客户

- 使用资源目录管理云上多个账号且拥有多个集群的企业客户。
- 使用云效搭建流水线的企业客户。

## 方案架构

本方案使用云效、容器镜像服务ACR和容器服务ACK搭建云效流水线，实现容器的CI/CD集成。方案中使用三个成员账号，分别为用于存放镜像仓库和项目源代码的「运维账号」，存放测试集群的「测试账号」以及存放生产集群的「生产账号」。当开发人员更新项目代码后，云效流水线首先构建镜像，并推送到镜像仓库ACR中，之后触发构建将镜像拉取到测试集群中，待测试并审核完成后，再将镜像拉取到生产集群中，完成容器CI/CD。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972907.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 云效 | [云效](https://help.aliyun.com/zh/yunxiao/product-overview/what-is-cloud-effect)是阿里云云原生时代一站式BizDevOps平台。云效流水线Flow是一款企业级、自动化的研发交付流水线， 提供灵活易用的持续集成、持续验证、 持续发布功能，帮助企业高质量、高效率的交付业务。 | 高级版收费，详情参见[云效自费](https://help.aliyun.com/zh/yunxiao/product-overview/product-billing/)。 |
| 容器镜像服务ACR | [阿里云容器镜像服务ACR](https://help.aliyun.com/zh/acr/product-overview/what-is-container-registry)（Alibaba Cloud Container Registry）是面向容器镜像、Helm Chart等符合OCI标准的云原生制品安全托管及高效分发平台。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/acr/product-overview/billing-description)。 |
| 容器服务ACK | [容器服务Kubernetes版](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/product-overview/what-is-ack)（Alibaba Cloud Container Service for Kubernetes，简称容器服务ACK）提供高性能可伸缩的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ack/billing-information)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 运维账号 | 企业运维资源会部署在这个账号内，如CI/CD流水线、镜像仓库。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |
| 测试账号 | 企业对应业务使用的测试账号，其中包括全部用于测试的资源。推荐测试账号与生产账号完全隔离，由对应的业务团队负责。 |
| 生产账号 | 企业对应业务使用的生产账号，其中包括全部用于生产的资源。推荐测试账号与生产账号完全隔离，由对应的业务团队负责。 |

## 安全性

### 云效安全性

云效产品安全性详情参见[产品安全白皮书](https://help.aliyun.com/zh/document_detail/193835.html)，角色及权限详情参考官方文档[企业角色与权限](https://help.aliyun.com/zh/yunxiao/user-guide/enterprise-roles-and-permissions/)，流水线权限控制详情参见[权限管理](https://help.aliyun.com/zh/yunxiao/user-guide/permission-management)。

### 跨账号扮演角色

测试账号和生产账号里面的ACK集群需要有assumeRole权限，扮演运维账号中特定角色。这个角色具备从ACR中拉取镜像的权限。为了避免出现权限过大，建议精细化授权。容器镜像授权请参考[官方链接](https://help.aliyun.com/zh/acr/user-guide/ram-authorization-information)。

## 注意事项

### 免密组件限制

使用ACK的免密组件涉及的镜像及集群存在限制，具体可查看[官方文档](https://help.aliyun.com/zh/acr/use-the-aliyun-acr-credential-helper-component-to-pull-images-without-using-secrets)。

### 云效企业成员管理

目前云效支持三种方式将成员邀请进入企业：通过链接邀请、添加阿里云RAM用户以及同步钉钉成员，**暂不支持使用阿里云RAM角色**进入企业，具体可参考[官方文档](https://help.aliyun.com/zh/yunxiao/user-guide/invite-members-via-link)。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972908.png)

### 云效使用自有构建

本方案中云效使用公共构建集群（云效北京构建集群），如需在云效中使用自有构建集群，请参考[官方文档](https://help.aliyun.com/zh/document_detail/202407.html)。

### 容器镜像开启公网访问入口

本方案中容器镜像服务ACR实例开启了公网访问入口，通过白名单限制允许访问容器镜像实例的IP。若不希望开启公网访问入口，请参考「多ACK集群连接公共ACR方案」。

## 实施步骤

### 实施准备

- 确保已在「运维账号」下开通云效，并且能够登录[流水线控制台](https://flow.aliyun.com/my?page=1)。
- 确保已在「测试账号」和「生产账号」下已分别创建ACK测试集群和ACK生产集群。
- 该方案使用Kubectl方式部署，代码中需提前准备好Dockerfile和用于部署的YAML文件。

#### 部署清单

| 部署账号 | 部署内容 |
| --- | --- |
| 运维账号 | 云效代码仓库，存放项目源代码云效流水线，用于编译构建镜像并部署到测试和生产集群容器镜像服务企业级实例，作为镜像仓库一个RAM角色和自定义策略，提供给测试账号和生产扮演，用于跨账号拉取镜像 |
| 测试账号 | 测试集群，用于测试环境部署 |
| 生产账号 | 生产集群，用于生产环境部署 |

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：2小时。

### 操作步骤

#### 创建云效代码管理库

首先，我们需要在**运维账号**上，创建云效代码管理库，用于存储需要部署的源代码。

1. 登录[云效代码管理控制台](https://codeup.aliyun.com/)，点击右上角的添加库，根据实际情况选择新建代码库或者导入代码库。在此处我们选择新建代码库，如何导入已有代码库，请参考[文档](https://help.aliyun.com/zh/yunxiao/user-guide/import-the-three-party-code-base-through-the-web-page)。
2. 在新建代码库对话框中，填入代码库名称、代码库路径、代码库公开性等信息后，点击**确定**后，代码库则创建完成。
3. 根据代码库中，命令行的提示，完成代码上传。至此，我们完成了云效代码管理库的创建。请记录下代码管理库中**Dockerfile**和**部署yaml文件**的相对路径，在搭建流水线的步骤中，将使用到上述两个参数。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972909.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972910.png)

#### 添加Kubernetes集群

我们需要在**运维账号**上的云效流水线控制台上，添加位于**测试账号**和**生产账号**下的Kubernetes测试集群和Kubernetes生产集群。

1. 分别登录**测试账号**和**生产账号**，进入[容器服务控制台](https://cs.console.aliyun.com/)，进入测试集群和生产集群的详情中，点击连接配置，获取连接Kubernetes集群的配置信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972911.png)
2. 登录**运维账号**，进入[云效流水线控制台](https://flow.aliyun.com/my?page=1)，在左侧菜单下方单击**设置，**进入**Kubernetes集群管理**页面。
3. 单击**新建Kubernetes集群**，因Kubernetes集群位于**生产账号**和**测试账号**，需在对话框中选择自定义集群，填入Kubernetes集群的名称和配置文件。
4. 点击保存后，完成在云效中添加Kubernetes集群的操作。重复上述步骤，直到将Kubernetes测试集群和Kubernetes生产集群都添加到云效中。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972912.png)

#### 创建并配置容器镜像仓库

完成云效代码管理的创建和配置后，我们需要在运维账号下，创建容器镜像仓库，存储流水线中打包构建完成的容器镜像。在该步骤中，我们选择阿里云容器镜像服务作为容器镜像仓库。

1. 登入**运维账号**，进入[容器镜像服务控制台](https://cr.console.aliyun.com/)，点击左上方创建企业版实例，在购买页面中根据需要选择地域、实例规格和实例名称等信息，完成后点击购买按钮后，等待实例运行状态处于**运行中**时，即创建成功。
2. 点击进入步骤1创建的容器镜像实例，点击右下方新手指引中的**访问控制**，为实例添加网络访问控制。因跨账号的情况，我们需开启实例公网访问接口，并添加公网白名单。点击公网，将访问入口开关打开，等待公网入口创建完成后，添加公网白名单。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972913.png)
3. 开启公网入口后，会默认添加一条白名单，若删除所有白名单，则公网下任何机器均可通过访问凭证访问企业版实例。因此，在此处我们推荐添加若干条白名单，实现更加精细的访问控制，包括：云效流水线IP地址：112.126.70.240、123.56.255.38、47.94.150.88云效流水线构建集群IP地址：若使用**云效流水线提供的构建集群**，则参考[云效构建集群](https://help.aliyun.com/zh/yunxiao/user-guide/build-a-cluster)文档，添加对应的构建集群IP地址。本方案中使用国内（北京）构建集群。若使用**自有构建集群**，则将自有构建集群的IP地址添加到白名单中。测试集群和生产集群Worker Node的IP地址或IP网段。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972914.png)
4. **访问凭证**我们使用Kubernetes免密组件登录，这里先跳过。点击左侧导航栏的**命名空间**，进入页面后点击左上方的**创建命名空间**，填写命名空间的名称后，根据需要选择仓库类型，点击**确定**，即可完成命名空间的创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972915.png)
5. 点击左侧导航栏的**代码源**，选择**阿里云云效**作为代码源，点击**绑定账号**。在弹窗中，需要填入云效的用户名称以及个人访客令牌。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972916.png)用户名称和个人访问令牌可通过登录[云效代码管理控制台](https://codeup.aliyun.com/)，点击右上角头像下的个人设置。在个人设置页面的左侧导航栏中，点击个人访问令牌。点击创建访问令牌，设置名称、过期时间并授予相应的权限，容器镜像服务ACR所需的最小权限见[文档](https://help.aliyun.com/zh/acr/user-guide/bind-a-source-code-hosting-platform)。创建后，即可查看到创建的访问令牌。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972917.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972918.png)用户名称的获取，先点击左侧导航栏中的**HTTPS密码**，复制**克隆账号**名称即可。将用户名称和个人访问令牌填入后，即可完成代码源的绑定。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972919.png)
6. 点击左侧导航栏的镜像仓库，进入页面后点击左上方的创建镜像仓库，填写仓库名称，根据需要填写其他相关信息。点击下一步后，需选择代码源，在云效CodeUp中选择之前创建好的代码管理库。构建设置可根据需要进行选择。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972920.png)

#### 配置Kubernetes集群访问凭证

完成容器镜像仓库的创建和配置后，云效已经能够成功将镜像上传到镜像仓库中，在该部分还需为测试和生产集群配置访问凭证，允许其Worker节点从镜像仓库中拉取镜像。我们选择使用免密组件跨账号拉取容器镜像，详情参考[从ACR免密拉取镜像](https://help.aliyun.com/zh/acr/user-guide/non-secret-pulling-container-image)。

1. 登录**运维账号**，创建拥有拉取指定私有仓库下镜像权限的RAM角色。登录[RAM控制台](https://ram.console.aliyun.com/)，点击左侧导航栏中的**角色**，点击页面中**创建角色**按钮。选择可信实体为阿里云账号，填写账号名称。
2. 创建完成后，找到该RAM角色，修改其信任策略。将**测试账号**和**生产账号**RAM中，集群Woker RAM角色(名为KubernetesWorkerRole-xxx，在集群创建时会自动创建该角色)的ARN添加到信任策略中，允许上述两个角色扮演**运维账号**中的拉取镜像角色。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972922.png)
3. 在**运维账号**中创建自定义权限策略，并将该权限授予给拉取镜像角色。点击[RAM控制台](https://ram.console.aliyun.com/)左侧**权限策略**，点击**创建权限策略**，选择**脚本编辑**，将以下权限复制到脚本编辑的Action中。创建完成后，将该权限授予步骤2所创建的角色上。`{
 "Version": "1",
 "Statement": [
 {
 "Action": [
 "cr:GetAuthorizationToken",
 "cr:ListInstanceEndpoint",
 "cr:PullRepository"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 }
 ]
}`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972921.png)
4. 分别登录**测试账号**和**生产账号**，进入RAM控制台，找到对应的Kubernetes Worker角色，为其授予AliyunSTSAssumeRoleAccess权限。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972924.png)
5. 分别登录**测试账号**和**生产账号**，进入[容器服务控制台](https://cs.console.aliyun.com/)，点击查看对应集群的详细信息。在左侧导航栏中找到**运维管理**，点击下方的**组件管理**，在搜索栏中搜索aliyun-acr-credential-helper组件，安装该组件。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972926.png)
6. 安装完成后，点击左侧导航栏中的**配置管理**，选择下方的**配置项**，切换**命名空间**为kube-system，在搜索栏搜索acr-configuration配置项，点击右侧的**YAML编辑**，设置配置项信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972923.png)
7. 修改acr-registry-info字段，添加instanceId和assumeRoleARN字段。其中instanceId为容器镜像实例Id，可在运维账号下的[容器镜像服务控制台](https://cr.console.aliyun.com/)，查看对应实例详情中的实例ID获取；assumeRoleARN为步骤2所创建的角色ARN。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972925.png)
8. 至此，我们完成了Kubernetes集群访问凭证的配置。

#### 创建云效流水线

1. 登录**运维账号**，进入[云效流水线控制台](https://flow.aliyun.com/my?page=1)，点击右上角的新建流水线。根据业务需要，可选择流水线模板并在此基础上进行修改，也可以直接使用空模板。这里我们选用【Java·测试、构建镜像，发布到Kubernetes集群/阿里云容器服务**】**模板。选择后，点击创建即可进入流水线编辑页面。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972927.png)
2. 首先需要为流水线添加代码源，我们选择云效CodeUp作为代码源，选择代码仓库和默认分支，同时根据需要可开启代码源触发。填写信息后，点击添加即完成了流水线源的配置。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972928.png)
3. 配置流水线中的【Java构建Docker镜像并推送镜像仓库】模块选择构建集群，本方案中全部使用【云效北京构建集群】完成构建，如果需要使用自有构建集群，请参考[文档](https://help.aliyun.com/zh/document_detail/202409.html)，并在容器镜像仓库的访问白名单中添加对应构建集群的IP。本方案后续构建集群均选择【云效北京构建集群】。在任务步骤中，删除【镜像构建并推送至阿里云镜像仓库个人版】，点击右上角的**添加步骤**，在**构建**中选择【镜像构建并推送至阿里云镜像仓库企业版】。添加步骤完成后，点击添加服务连接，授权云效流水线访问容器镜像服务。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972929.png)根据之前步骤中创建的容器镜像仓库，填写地域、企业实例、命名空间等基本信息。其中，标签根据需要自行设定，本方案中使用`${DATETIME}`作为标签。Dockerfile路径需填写云效代码管理库中Dockerfile的相对路径，本方案中即为Dockerfile。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972931.png)
4. 配置流水线中的【Kubernetes发布】模块。首先，我们将构建好的镜像，使用Kubectl发布到测试集群。可将任务名称更改为【测试Kubernetes集群发布】。集群连接选择之前创建好的**测试Kubernetes集群**。**YAML路径**选择云效代码库中YAML文件所处的相对路径，本方案中为manifests。由于YAML文件中存在变量`${IMAGE}`（部署所使用的镜像）和`${HOST}`（ingress所使用的host），在部署时需要在变量栏中，添加IMAGE和HOST两个变量。此处可根据自身YAML文件，自定义参数，具体参考[官方文档](https://help.aliyun.com/zh/document_detail/154944.html)。点击**变量**右侧的**添加**按钮即可。IMAGE：选择【上游任务 制品/镜像 下载地址】，名称填入IMAGE，值选择【镜像构建并推送至阿里云镜像仓库企业版.镜像公网地址】HOST：选择【自定义参数】，名称填入HOST，值根据业务需要填写，可使用测试集群的测试域名。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972930.png)
5. 测试集群测试完成后，需通过人工审核的方式发布到生产集群。点击右侧新的任务按钮，添加人工审核卡点。在任务组中选择**工具**，添加**人工卡点**任务。根据业务需求，对人工卡点任务进行配置，也可在**任务插件**处，添加邮箱或者钉钉通知。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972932.png)
6. 审核通过后，发布到生产集群。点击右侧新的任务，在任务组中选择**部署**，**Kubernetes发布**任务，集群连接选择生产Kubernetes集群，其余参数参照步骤4填写。对于生产集群，也可采用除Kubectl外其他的部署方式，比如分批部署，更多Kubernetes部署方式请参考[文档](https://help.aliyun.com/zh/yunxiao/user-guide/kubernetes-deployment/)。

#### 运行云效流水线

完成上述所有操作步骤后，点击右上方的**保存并运行**，即可运行该流水线。在测试集群上完成测试后，审批人点击**发布准入**下方的**验证通过**后，即可部署到生产集群上，完成容器的CI/CD流水线。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3586581571/p972933.png)

## 故障排除

### 云效流水线推送镜像到ACR失败？

网络不可达，请检查ACR访问白名单是否配置了云效对应的IP地址。

### 业务账号内ACK无法正常pull images?

可能有两个原因导致：

- 网络不可达，可以登录ACK 对应的worker节点，上去Ping一下ACR仓库的域名。看看能不能正常Ping通。需检查ACR访问白名单是否配置正确。
- 网络通，权限不对，需要检查一下测试账号和生产账号里面所涉及到的几个角色配置是否按照文档进行配置的。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-131（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
