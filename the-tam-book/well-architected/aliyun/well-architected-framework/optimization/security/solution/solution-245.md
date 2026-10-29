<!-- source: https://help.aliyun.com/zh/well-architected/solution-245 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2928843 -->

# 通过TVM实现临时凭证的获取和使用

本方案介绍了一种通过Token Vending Machine获取并使用STS临时凭证的方案。避免直接把AccessKey固化在客户端中，引发泄露风险。同时通过会话策略（Session Policy）的动态授权，对权限进行精细化管理。

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5076581571/p968192.png)

在典型的服务端和客户端架构下，客户端如果需要访问阿里云，比如基于OSS的用户文件上传下载、使用SLS记录客户端日志等等场景，常见的方式是在客户端使用RAM用户的访问密钥（AccessKey）来完成，但是在客户端中使用长期有效的访问密钥，可能会导致访问密钥泄露，进而引起安全问题。

本文档介绍了一种在客户端获取并使用STS临时凭证的方案，通过STS临时凭证访问阿里云，无需透露长期AccessKey，减少密钥泄露的风险。同时，通过会话权限策略，可以进行精细化的权限管控，避免越权问题。

## 方案优势

### 减少密钥泄露风险

通过服务端颁发的临时凭证STS Token访问云资源，避免了将访问密钥AccessKey硬编码在客户端代码中，从而消除AccessKey泄露的风险。临时凭证（STS Token）的使用有效解决了永久凭证（AK/SK）可能带来的安全风险问题。

### 精细化权限管控

在扮演RAM角色获取临时凭证STS Token时，通过会话权限策略，可以进一步缩小权限，保证精细化的权限管控，避免越权问题。

### 支持跨平台

通过服务端颁发临时凭证STS Token，您可以在云上或者云下的任意环境中，使用STS Token访问阿里云。保证即使在阿里云外，也无需透露长期AccessKey，保证密钥安全。

## 客户场景

### 客户端使用无AK架构避免AK泄露

#### 场景描述

企业存在部署在阿里云外的客户端程序，需要访问阿里云资源，比如基于OSS的用户文件上传下载、使用SLS记录客户端日志等等，常见的方式是在客户端使用RAM用户的访问密钥（AccessKey）来完成，但是在客户端中使用长期有效的访问密钥，可能会导致访问密钥泄露，进而引起安全问题。因此需要在客户端，使用临时凭证STS Token代替长期AccessKey，避免AccessKey泄露。

#### 适用客户

- 企业存在部署在阿里云外的客户端程序，需要访问阿里云资源。
- 企业的客户端的自有用户，在阿里云上需要进行精细化的资源和权限管控。
- 出于安全考虑，不希望使用长期固定AccessKey，以避免AccessKey泄露，带来安全风险。

## 方案架构

本方案在服务端实现了STS临时凭证售卖机（TVM：Token Vending Machine），通过服务端TVM向客户端颁发STS临时凭证。首先运维管理员在ECS实例上绑定实例角色，部署在该ECS上的TVM程序可以通过阿里云官方SDK，获得代表实例角色的临时凭证STS Token（图中1、2、3），保证服务端程序无需透露长期固定AccessKey。然后运维管理员创建一个RAM角色作为业务角色，并授信给ECS实例角色，允许实例角色通过AssumeRole接口扮演业务角色，获取业务角色的STS临时凭证（图中4）。客户端在需要访问阿里云时，向服务端获取STS临时凭证，服务端收到请求并校验请求合法性后，构造会话权限策略（Session Policy）进行精细化的权限管控，然后使用实例角色身份，携带上会话权限策略AssumeRole到业务角色上，获取并返回业务角色的STS临时凭证，该STS临时凭证所具有的权限就是会话权限与业务角色权限的交集（图中5、6）。客户端拿到业务角色的STS临时凭证后，使用临时凭证直接调用API访问阿里云（图中7）。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5076581571/p968194.png)

本方案中为保证全链路（客户端与服务端）无需透出长期固定AccessKey，在服务端通过角色链式扮演的方式，获取业务角色的STS临时凭证，返回给客户端使用，具体架构如下图所示。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5076581571/p968193.png)

为服务端所在的ECS实例绑定RAM角色，该实例角色授信给ECS服务，ECS服务会去AssumeRole该实例角色，获取到实例角色的STS临时凭证，提供给服务端使用。

当客户端请求获取STS临时凭证，服务端使用实例角色的STS临时凭证，以实例角色的身份AssumeRole到业务角色上，获取业务角色的STS临时凭证并返回客户端使用，业务角色需要授信给实例角色，允许实例角色扮演。

其中，实例角色至少具有`sts:AssumeRole`的权限，业务角色的权限既客户端业务请求阿里云所需的具体权限，同时可以在AssumeRole时，通过会话权限策略进一步限制和缩小权限。比如客户端为其自有的用户提供图片、文件上传存储的功能，需要基于OSS文件夹进行用户资源和权限的隔离，如果单独为每一个客户端自有用户创建一个业务角色，会导致角色数量的巨大膨胀，带来巨大的管理成本，因此您可以使用唯一一个业务角色，该业务角色的权限收敛到OSS Bucket，如下所示。

```
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "oss:GetObject",
                "oss:PutObject"
            ],
            "Resource": "acs:oss:*:*:<oss bucket>/*"
        }
    ]
}
```

当客户端需要上传文件的时候，服务端构造收敛到OSS文件夹的会话权限策略，如下所示。

```
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "oss:GetObject",
                "oss:PutObject"
            ],
            "Resource": "acs:oss:*:*:<oss bucket>/<oss folder>/*"
        }
    ]
}
```

携带该会话权限策略AssumeRole到业务角色上，获取STS临时凭证返回给客户端使用，该STS临时凭证所具有的权限就是会话权限与业务角色权限的交集，既只具有往确定的OSS文件夹下上传文件的权限，以此针对客户端自有的不同用户进行动态的权限隔离。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5076581571/p968195.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 访问控制RAM | [访问控制RAM（Resource Access Management）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 访问密钥（AccessKey） | 访问密钥AccessKey（简称AK）是阿里云提供给用户的永久访问凭据，一组由AccessKey ID和AccessKey Secret组成的密钥对。发起的请求会携带AccessKey ID和AccessKey Secret加密请求内容生成的签名，进行身份验证及请求合法性校验。 |
| STS临时凭证 | 调用[AssumeRole - 获取扮演角色的临时身份凭证](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)接口，扮演某个RAM角色，获取该角色的STS临时凭证（STS Token），从而使用STS Token访问阿里云 |
| RAM角色（RAM Role） | RAM角色是一种虚拟用户，可以被授予一组权限策略。与RAM用户不同，RAM角色没有永久身份凭证（登录密码或访问密钥），需要被一个可信实体扮演。扮演成功后，可信实体将获得RAM角色的临时身份凭证，即安全令牌（STS Token），使用该安全令牌就能以RAM角色身份访问被授权的资源。 |
| 实例RAM角色 | 当ECS实例或部署在ECS实例上的应用需要访问其他云资源时，必须配置访问凭证，阿里云服务会通过访问凭证验证您的身份信息和访问权限。实例RAM角色允许您将一个角色关联到ECS实例，实现在实例内部自动获取并刷新临时访问凭证，无需直接暴露AccessKey，减少密钥泄露的风险。 |
| 业务RAM角色 | 由实例RAM角色扮演该角色获取STS临时凭证，使用该STS临时凭证访问云资源完成业务操作，在扮演角色时，通过设置会话权限策略，可以进一步收敛权限，实现权限隔离，防止业务角色膨胀。为方便区分，在本解决方案中，统一叫为业务RAM角色或者业务角色。 |
| 会话权限策略（Session Policy） | 在通过AssumeRole API扮演角色获取STS Token时，可以为STS Token额外添加的一个权限策略，既会话权限策略（Session Policy），进一步限制STS Token的权限。具体如下：如果指定该权限策略，则STS Token最终的权限策略取RAM角色权限策略与该权限策略的交集。如果不指定该权限策略，则STS Token最终的权限策略取RAM角色的权限策略。 |

## 安全性

### ECS元数据服务器访问模式

默认情况下，实例元数据服务器可同时通过普通模式和加固模式访问。为了进一步增强安全性，您可以设置实例元数据服务器访问模式为**仅加固模式**。采用ECS实例的元数据加固策略来获取RAM角色的初始化凭据，相较于普通模式，此方式采纳了一种更为严谨的安全逻辑：首先在ECS实例内部自动生成一个具有时效限制的token，利用此token作为凭据，向元数据服务（Metadata Server）请求获得STS（Security Token Service）临时凭证。这一系列操作构成了凭据客户端的安全初始化流程。什么是加固模式请参见[加固模式](https://help.aliyun.com/zh/ecs/user-guide/view-instance-metadata/)的介绍。

## 注意事项

### 支持STS的云服务

详情参见[支持STS的云服务](https://help.aliyun.com/zh/ram/services-that-work-with-sts)。

## 实施步骤

### 实施准备

- 本方案以客户端上传下载OSS文件为例，请确保您已经[开通OSS对象存储服务](https://help.aliyun.com/zh/oss/getting-started/getting-started-with-oss#13226d99c2mhz)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 服务端程序实现无AK架构

为保证AccessKey凭证安全，避免因为AccessKey凭证泄露导致的安全问题，固定AccessKey都不应该硬编码在您的应用程序中，建议您的服务端应用程序实现无AK架构，使用STS临时凭证代替固定AccessKey。针对不同类型的云上应用部署方式，您可以选择相应的方案实现STS临时凭证的使用：

- 针对在ECS实例上部署的应用，[通过ECS实例角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-240)，将RAM角色跟实例进行绑定，应用程序中即可通过ECS实例RAM角色，获取实例RAM角色的STS临时授权访问凭证。
- 针对在ACK上部署的应用，在容器服务Kubernetes版中，一个集群可以部署多个服务，同一个容器节点可能包含多个不同服务的Pod，在多租户场景下，若部署不受信任的服务，该服务可直接访问ECS的元数据服务（Meta Data Server），获取Worker节点关联实例RAM角色的临时令牌STS Token，会造成身份权限的泄露。[通过容器服务RRSA实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-241)，在Pod维度即可扮演对应角色实现STS临时凭证的获取。
- 针对在函数计算中部署的Serverless应用，[通过FC函数角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-242)，将RAM角色跟函数进行绑定，应用程序中即可通过函数RAM角色，获取RAM角色的STS临时授权访问凭证。

对于必须使用固定AccessKey的场景，比如需要访问不支持STS临时凭证的云服务，建议对AccessKey进行集中化管控。推荐以下解决方案：

- [通过KMS实现固定AccessKey的集中管控](https://help.aliyun.com/zh/well-architected/solution-237)，通过该方式，可以实现AccessKey的集中化管控，当业务需要使用AccessKey时，可以为其托管一个RAM用户AccessKey，并可以设置自动轮转周期，降低AccessKey泄漏风险。轮转时凭据管家会调用访问控制RAM（Resource Access Management），先创建一个新的AccessKey，然后删除旧的AccessKey。同时KMS将新的AccessKey写入凭据值，并删除旧的AccessKey对应的凭据值。当您发现RAM凭据泄露时，可以通过立即轮转凭据进行应急处理，此时推荐将轮转时长设置为30分钟实现快速轮转，降低泄漏造成的损失。

本方案中，将TVM服务端应用部署在ECS实例中为例，使用ECS实例角色扮演业务角色，获取并返回业务角色的STS Token给客户端使用。您在真实业务中使用时，建议将TVM内置在您的业务应用中，通过业务应用已有的登录态、鉴权等机制，保证请求的合法性。接下来简单介绍在创建ECS实例时，如何为ECS实例绑定RAM角色。更详细的配置方式，您可以参考[通过ECS实例角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-240)。

1. 登入应用账号，前往[实例创建页](https://ecs-buy.aliyun.com/wizard/#/)。
2. 选择**自定义购买**页签。
3. 按需选择付费类型、地域、实例规格、镜像等配置。各配置项详细说明，请参考[配置项说明](https://help.aliyun.com/zh/ecs/user-guide/create-an-instance-by-using-the-wizard)。
4. 展开**高级选型（选填）**表单，在**实例RAM角色**中，选择要绑定的RAM角色。本方案中，以名为EcsInstanceRole的实例角色为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5076581571/p968196.png)
5. 在最终创建实例前，请在页面右侧检查实例的整体配置并配置使用时长等选项，确保各项配置符合您的要求。
6. 阅读并签署**《云服务器ECS服务条款》**等服务协议（若已签署，则无需重复签署，请以页面提示为准），然后单击**确认下单**。

创建实例一般需要3~5分钟，请您耐心等待。您可前往控制台的实例列表页面查看实例的状态，当实例状态变为**运行中**时，表示实例创建完成。

#### 配置实例RAM角色权限

本方案中，将TVM部署在ECS实例中为例，您需要为ECS实例角色授予权限，允许ECS实例角色可以调用角色扮演的API，扮演到业务RAM角色上，获取业务RAM角色的STS临时凭证并返回给客户端使用，通过ECS实例角色再去扮演业务角色的角色链式扮演方式，可以在扮演时，通过设置会话权限策略（Session Policy）动态收敛权限，实现客户端程序自有用户的权限隔离。

如果您使用的是容器服务RRSA、函数角色或者固定AccessKey的方案，也需要按照如下步骤，给对应的RAM角色或RAM用户配置权限策略。

1. 登入应用账号，前往[RAM控制台](https://ram.console.aliyun.com)。
2. 左侧导航栏中，单击**权限管理** > **权限策略**。
3. 单击**创建权限策略**按钮，进入创建权限策略页面，切换为**脚本编辑**。
4. 将以下策略内容复制到策略文档输入框中，注意将内容中的`<业务RAM角色的名称>`替换为下一章节**创建业务RAM角色**中，创建的业务RAM角色（既扮演该角色获取STS临时凭证并返回给客户端）的名称。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "acs:ram:*:<账号ID>:role/<业务RAM角色的名称>"
 }
 ]
}`
5. 如果您有多个业务RAM角色需要扮演，可以在Resource中继续增加。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": [
 "acs:ram:*:<账号ID>:role/<业务RAM角色1的名称>",
 "acs:ram:*:<账号ID>:role/<业务RAM角色2的名称>"
 ]
 }
 ]
}`
6. 单击**继续编辑基本信息**，填写策略名称等基本信息，这里策略名称以EcsInstanceRolePolicy为例。
7. 单击**确定**，完成策略创建。
8. 在左侧导航栏，选择**身份管理** > **角色**。
9. 在角色页面，找到目标ECS实例RAM角色，既上一个章节中，为ECS实例绑定的RAM角色，本方案中，以名为EcsInstanceRole的实例角色为例，单击**操作**列的**新增授权**。
10. 在**新增授权**面板，为RAM角色授权。其中权限策略，选择刚刚创建出来的权限策略，这里以EcsInstanceRolePolicy为例
11. 单击**确认新增授权**，完成权限策略的绑定。

#### 创建业务RAM角色

您需要创建业务RAM角色，该角色需要具有客户端访问阿里云所需要的权限，同时需要授信给ECS实例角色，允许ECS实例角色来扮演，获取业务RAM角色的STS临时凭证。

1. 登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 在左侧导航栏，选择**身份管理 > 角色**。
3. 在**角色**页面，单击**创建角色**。
4. 在**创建角色**页面，选择可信实体类型为**阿里云账号**，然后单击**下一步**。
5. **信任的云账号**选择当前云账号，点击**完成。**

接下来，您需要修改该角色的信任策略，授信给ECS实例角色。

1. 进入该角色的详情页，选择**信任策略**页签。
2. 单击**编辑信任策略**按钮。将以下信任策略内容复制到信任策略文档输入框中，注意将内容中的`<ECS实例角色的名称>`替换为上一章节中，配置的ECS实例RAM角色的名称。`{
 "Statement": [
 {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
 "RAM": [
 "acs:ram::<账号ID>:role/<ECS实例角色的名称>"
 ]
 }
 }
 ],
 "Version": "1"
}`
3. 单击**保存信任策略**，完成信任策略的修改。

接下来，您需要为该角色分配权限，客户端程序会使用该角色的STS临时凭证访问阿里云完成业务操作。本方案中，以OSS文件上传下载的场景为例，在客户端会查询OSS文件列表，并实现文件的上传和下载。

1. 登录[RAM控制台](https://ram.console.aliyun.com/)。
2. 选择权限策略菜单，点击**创建权限策略。**
3. 通过**脚本编辑**模式，将配置框中的原有脚本替换为如下内容。注意将内容中的`<OSS Bucket的名称>`替换为您实际需要保存文件的OSS Bucket名称。该策略允许遍历该OSS Bucket的文件，并从该OSS Bucket中上传和下载文件。本方案中，以客户端为其自有的用户提供图片、文件上传存储的功能为例，需要基于OSS文件夹进行用户资源和权限的隔离，如果单独为每一个客户端自有用户创建一个业务角色，会导致角色数量的巨大膨胀，带来巨大的管理成本，因此该场景下使用唯一一个业务角色，权限只收敛到OSS Bucket级别，在客户端请求服务端获取业务角色的STS临时凭证时，服务端会根据当前请求的登录态，构造收敛到OSS文件夹的会话权限策略，然后携带该会话权限策略AssumeRole到业务角色上，获取STS临时凭证返回给客户端使用，该STS临时凭证所具有的权限就是会话权限与业务角色权限的交集，既只具有操作确定的OSS文件夹下文件的权限，以此针对客户端自有的不同用户进行动态的权限隔离。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "oss:GetObject",
 "oss:PutObject"
 ],
 "Resource": "acs:oss:*:*:<OSS Bucket的名称>/*"
 },
 {
 "Effect": "Allow",
 "Action": "oss:ListObjects",
 "Resource": "acs:oss:*:*:<OSS Bucket的名称>"
 }
 ]
}`
4. 点击**继续编辑基本信息**，输入自定义权限策略名称。点击**确定**完成创建。
5. 创建完成后，在角色页面，找到上述步骤创建的角色，将该权限策略绑定到新创建的业务角色身上。

#### 实现Token Vending Machine

本方案，以将TVM部署在ECS实例中为例，TVM程序首先会获得ECS实例角色的临时凭证STS Token，然后使用实例角色的STS Token请求AssumeRole接口扮演业务角色，获取并返回业务角色的临时凭证STS Token。以此保证：

- 全链路无需透出固定AccessKey
- 在扮演业务角色时，通过设置会话权限策略（Session Policy）动态收敛权限，实现客户端程序自有用户的权限隔离

本方案代码以Java SpringBoot为例，并未对请求合法性进行校验，您在真实业务中使用时，建议将TVM内置在您的业务应用中，通过业务应用已有的登录态、鉴权等机制，来保证请求的合法性。示例代码详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-tvm)。

##### 初始化Client

首先您需要获取ECS实例角色的临时凭证STS Token，使用该STS Token初始化STS服务的SDK Client，后续会使用该STS SDK Client请求AssumeRole接口，扮演到业务角色身上，获取业务角色的STS Token。推荐您使用阿里云的Credentials工具，获取并管理ECS实例角色的STS Token：

- 基于ECS实例RAM角色获取临时凭证时，Credentials工具会自动调用ECS的元数据服务（Meta Data Server）获取临时访问凭证。
- Credentials工具会自动维护临时凭证的生命周期，研发人员无需关心临时凭证的到期更新，Credentials工具会自动保证凭证的周期性更新。

更多Credentials工具的信息，请参考[管理访问凭据](管理访问凭据)。

如下所示，首先初始化Credentials工具的Client客户端。需要注意的是，Credentials工具的客户端应该是单例模式，不要每次请求都重新New一个，避免出现内存泄露的问题。

```
import com.aliyun.credentials.Client;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class CredentialConfig {

    // 初始化凭据客户端，Credential SDK Client 应该是单例，不要每次请求都重新 new 一个，避免内存泄露
    // 借助Credentials工具的默认凭据链，您可以用同一套代码，通过程序之外的配置来控制不同环境下的凭据获取方式
    // 当您在初始化凭据客户端不传入任何参数时，Credentials工具将会尝试按照如下顺序查找相关凭据信息（优先级由高到低）：
    // 1. 使用系统属性
    // 2. 使用环境变量
    // 3. 使用OIDC RAM角色
    // 4. 使用配置文件
    // 5. 使用ECS实例RAM角色（需要通过环境变量 ALIBABA_CLOUD_ECS_METADATA 指定 ECS 实例角色名称；通过环境变量 ALIBABA_CLOUD_ECS_IMDSV2_ENABLE=true 开启在加固模式下获取STS Token）
    // https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials#3ca299f04bw3c
    // 要使用默认凭据链，初始化 Client 时，必须使用空的构造函数，不能配置 Config 入参
    @Bean(name = "credentialClient")
    Client getCredentialClient() {
        return new Client();
    }
}
```

然后使用Credentials的Client初始化STS服务的SDK Client。需要注意的是，STS SDK Client也建议是单例模式，不要每次请求都重新New，避免出现内存泄露的问题。

```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class StsClientConfig {

    // region id 配置到了 application.properties 中，请根据实际业务需要进行修改
    @Value("${region.id}")
    String regionId;

    @Autowired
    com.aliyun.credentials.Client credentialClient;

    // 初始化阿里云 V2 版本 STS 的 SDK 客户端
    // SDK Client 应该是单例，不要每次请求都重新 New 一个，避免内存泄露
    @Bean(name = "stsClient")
    com.aliyun.sts20150401.Client getStsClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config()
            .setCredential(credentialClient)
            .setRegionId(regionId);
        return new com.aliyun.sts20150401.Client(config);
    }
}
```

##### 构造会话权限策略

在扮演业务角色时，通过设置会话权限策略（Session Policy）动态收敛权限，实现客户端程序自有用户的权限隔离。比如客户端为其自有的用户提供图片、文件上传存储的功能，需要基于OSS文件夹进行用户资源和权限的隔离，如果单独为每一个客户端自有用户创建一个业务角色，会导致角色数量的巨大膨胀，带来巨大的管理成本，因此就可以通过会话权限策略来动态收敛权限。

为方便构造Session Policy，您可以预先定义好权限模版，通过权限模版构造Session Policy。不同的云产品，您可能需要通过不同的方式来描述隔离策略，以OSS的权限策略为例，如下所示，在文件夹级别限制访问，保证客户端自有用户，只能访问用户自己对应的文件夹。

```
{
  "Effect": "Allow",
  "Action": [
    "oss:GetObject",
    "oss:PutObject",
    "oss:DeleteObject"
  ],
  "Resource": "acs:oss:*:*:{{bucket}}/{{dir}}/*"
},
{
  "Effect": "Allow",
  "Action": "oss:ListObjects",
  "Resource": "acs:oss:*:*:{{bucket}}",
  "Condition": {
    "StringLike": {
      "oss:Delimiter": "/",
      "oss:Prefix": [
        "{{dir}}/",
        "{{dir}}/*"
      ]
    }
  }
}
```

您可以针对不同的云产品，单独提供对应的权限模版，在构造Session Policy时，按需进行组合。在本代码示例中，我们提供了一个名为`PolicyGenerator`的简单Java类，由它来负责构造Session Policy。

```
String sessionPolicy = PolicyGenerator.generator()
    // 通过请求中的身份标识，限制允许操作的OSS文件夹，只允许操作同名的文件夹下面的文件
    .oss(ossBucket, identity)
    // 通过请求中的身份标识，限制允许操作的SLS Logstore，只允许操作同名的Logstore
    .sls(slsProject, identity)
    .generatePolicy();
```

通过`PolicyGenerator`，您可以按需组合不同云产品的权限模版，动态生成Session Policy。这里您需要将权限模版和它们所需要的变量绑定在一起，如上所示，我们的OSS权限策略模版需要一个OSS Bucket的名称，而我们的SLS权限策略模版，需要一个SLS Project名称，当前，它们都需要一个当前请求用户的唯一标识，既上例中的`identity`参数，通过请求用户的唯一标识，来构造用户隔离的权限策略。比如，在生成的OSS的权限策略中，对应的就是OSS Bucket文件夹的名称，以此实现通过文件夹来隔离请求用户的资源和权限。

您可以使用任意一种可以替换模板中变量的模板引擎来实现策略的生成。本示例中，使用的是Mustache。

```
String resolvedStatements = Mustache.compiler()
    .compile(statements)
    .execute(data);
String policy = "{ \"Version\": \"1\",\n  \"Statement\": [\n" + resolvedStatements + " ]\n}";
```

##### AssumeRole获取STS Token

构造好了Session Policy，您就可以携带该Session Policy，AssumeRole到业务角色上，获取STS临时凭证返回给客户端使用，该STS临时凭证所具有的权限就是Session Policy与业务角色本身权限的交集。这里您需要使用第一步**初始化Client**中，已经创建好的STS SDK Client。

```
 RuntimeOptions runtimeOptions = new RuntimeOptions()
    // 开启自动重试机制
    .setAutoretry(true)
    // 设置自动重试次数，默认3次
    .setMaxAttempts(3);
AssumeRoleRequest assumeRoleRequest = new AssumeRoleRequest()
    // 填写业务角色的arn
    .setRoleArn(roleArn)
    .setRoleSessionName(roleSessionName)
    // 填写构造好的Session Policy
    .setPolicy(sessionPolicy)
    .setDurationSeconds(durationSeconds);
try {
    // 使用已经初始化好的STS SDK Client
    AssumeRoleResponse assumeRoleResponse = stsClient.assumeRoleWithOptions(assumeRoleRequest, runtimeOptions);
    return assumeRoleResponse.getBody().getCredentials();
} catch (Exception e) {
    // 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
    e.printStackTrace();
    throw new RuntimeException(e);
}
```

##### 代码示例

###### 代码介绍

本方案提供Java SpringBoot的代码示例，方便客户能够快速完成应用改造。

###### 代码地址

代码详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-tvm)。

## 故障排除

### 为什么Credentials SDK报错：not found credentials？

- 请确保您已经为您的ECS绑定了RAM实例角色，您可以登录到ECS实例上，执行命令：`curl http://100.100.100.200/latest/meta-data/ram/security-credentials/${实例角色名称}`，如果正确返回临时凭证，那么您已成功绑定了RAM实例角色。
- 如果您使用的是JAVA的Credentials SDK，请确保您的SDK版本>=0.3.2。
- 如果您使用的是Credentials工具的默认凭据链，请确保您已经配置了环境变量**ALIBABA_CLOUD_ECS_METADATA**，该环境变量的值配置为RAM实例角色的名称。
- 如果您在运行在ECS中的Docker环境中使用Credentials工具请确保Docker中可以正常访问到ECS Meta Service，您可以在Docker环境中，执行命令：`url http://100.100.100.200/latest/meta-data/ram/security-credentials/${实例角色名称}`，如果正确返回临时凭证，那么您的Docker环境可以正常访问ECS Meta Service。如果您使用的是Credentials工具的默认凭据链，请确保您在Docker环境中已经配置了环境变量**ALIBABA_CLOUD_ECS_METADATA**，该环境变量的值配置为RAM实例角色的名称。需要注意的是，这里不要把环境变量配置到ECS实例上。

### 为什么调用AssumeRole接口报错：NoPermission？

- 请确保当前调用身份，具有扮演到该角色的权限，您可以直接授予其`AliyunSTSAssumeRoleAccess`的系统策略。当然，这里建议您进行如下所示的精细化授权。`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "acs:ram:*:<账号ID>:role/<需要AssumeRole到的目标角色的名称>"
 }
 ]
}`
- 请确保需要AssumeRole到的目标角色，授信给当前调用身份。您可以登录RAM控制台，进入目标角色的详情页，切换到信任策略的页签，检查当前的信任策略。如果当前调用身份是阿里云账号，您可以参考如下所示进行修改。`{
 "Statement": [
 {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
 "RAM": [
 "acs:ram::<账号ID>:root"
 ]
 }
 }
 ],
 "Version": "1"
}`如果当前调用身份是阿里云账号下的RAM用户，您可以参考如下所示进行修改。`{
 "Statement": [
 {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
 "RAM": [
 "acs:ram::<账号ID>:user/<RAM用户的名称>"
 ]
 }
 }
 ],
 "Version": "1"
}`如果当前调用身份是阿里云账号的RAM角色，您可以参考如下所示进行修改。`{
 "Statement": [
 {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
 "RAM": [
 "acs:ram::<账号ID>:role/<RAM角色的名称>"
 ]
 }
 }
 ],
 "Version": "1"
}`

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-245（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
