<!-- source: https://help.aliyun.com/zh/well-architected/solution-244 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929332 -->

# 通过预签名机制在客户端实现OSS直传和下载

本方案介绍了一种通过预签名机制实现客户端直接上传或下载对象存储OSS文件的方案。避免直接把AccessKey固化在客户端中，引发泄露风险。同时通过客户端直传避免了业务服务器中转文件，提高了上传速度，节省了服务器资源。

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3076581571/p970751.png)

在典型的服务端和客户端架构下，常见的文件上传方式是服务端代理上传：客户端将文件上传到业务服务器，然后业务服务器将文件上传到OSS。在这个过程中，一份数据需要在网络上传输两次，会造成网络资源的浪费，增加服务端的资源开销。同时从OSS上传/下载文件需要使用RAM用户的访问密钥（AccessKey）来完成签名认证，但是在客户端中使用长期有效的访问密钥，可能会导致访问密钥泄露，进而引起安全问题。

本文档介绍了一种在客户端实现直接从OSS上传/下载文件的方案，避免了业务服务器中转文件，提高了上传速度，节省了服务器资源，同时，客户端基于预签名机制访问OSS，无需透露长期AccessKey，减少密钥泄露的风险。

## 方案优势

### 减少密钥泄露风险

通过服务端预签名机制，客户端可以直接从OSS上传/下载文件，同时避免了将访问密钥AccessKey硬编码在客户端代码中，从而消除AccessKey泄露的风险。

### 节省带宽和服务器资源

在典型的服务端和客户端架构下，常见的文件上传方式是服务端代理上传：客户端将文件上传到业务服务器，然后业务服务器将文件上传到OSS。在这个过程中，一份数据需要在网络上传输两次，会造成网络资源的浪费，增加服务端的资源开销。通过客户端直接从OSS上传/下载文件的方式，无需通过服务端中转，节省带宽和服务器资源。

## 客户场景

### 客户端需要上传或下载OSS文件

#### 场景描述

企业存在部署在阿里云外的客户端程序，需要上传或者下载OSS文件，比如移动端APP应用的用户头像，需要上传到OSS上，并从OSS上下载展示。常见的方式有两种。

1. 在典型的服务端和客户端架构下，客户端将文件上传到业务服务器，然后业务服务器将文件上传到OSS。但是在这个过程中，一份数据需要在网络上传输两次，会造成网络资源的浪费，增加服务端的资源开销。
2. 在客户端使用RAM用户的访问密钥（AccessKey）直接访问OSS，完成文件的上传和下载，但是在客户端中使用长期有效的访问密钥，可能会导致访问密钥泄露，进而引起安全问题，造成企业资损。

因此，需要在不透露固定AccessKey的情况下，实现客户端直接往OSS上传文件或者从OSS下载文件。

#### 适用客户

- 企业存在部署在阿里云外的客户端程序，需要上传或者下载OSS文件。
- 出于成本考虑，希望客户端直接操作OSS，而不需要通过服务端中转。
- 出于安全考虑，不希望使用长期固定AccessKey，以避免AccessKey泄露，带来安全风险。

## 方案架构

本方案通过预签名的方式在客户端实现OSS直传和下载。首先运维管理员在ECS实例上绑定实例角色，在该ECS上的服务端程序可以通过阿里云官方SDK，获得代表实例角色的临时凭证STS Token（图中1、2、3），保证服务端程序无需透露长期固定AccessKey。客户端在需要往OSS上传或者从OSS下载文件时，向服务端请求签名授权，服务端收到请求并校验请求合法性后，进行预签名并返回给客户端（图中4），客户端使用预签名的结果，直接向OSS上传文件或者从OSS下载文件（图中5）。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3076581571/p970747.png)

服务端通过预签名授权客户端上传文件到OSS的过程如下：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3076581571/p970749.png)

1. 客户端向服务端请求Post签名、Post Policy和回调等信息。
2. 服务端生成并返回Post签名、Post Policy和回调设置等信息给客户端。
3. 客户端使用Post签名、Post Policy和回调设置等信息调用PostObject通过HTML表单的方式直接上传文件到OSS。
4. 客户端上传文件到OSS结束后，OSS解析客户端的上传回调设置，发送Post回调请求给服务端。
5. 服务端对OSS回调请求进行验证，如果验证通过，返回成功响应给OSS。
6. OSS将服务端返回的消息返回给客户端。

服务端通过预签名授权客户端从OSS下载文件的过程如下：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3076581571/p970755.png)

1. 客户端向服务端请求文件下载的临时签名URL。
2. 服务端生成并返回临时的签名下载URL。
3. 客户端使用临时签名的下载URL，直接从OSS下载文件。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 访问控制RAM | [访问控制RAM（Resource Access Management）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |
| 对象存储OSS | [阿里云对象存储OSS（Object Storage Service）](https://help.aliyun.com/zh/oss/product-overview/what-is-oss)是一款海量、安全、低成本、高可靠的云存储服务，可提供99.9999999999%（12个9）的数据持久性，99.995%的数据可用性。多种存储类型供选择，全面优化存储成本。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/oss/product-overview/billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 访问密钥（AccessKey） | 访问密钥AccessKey（简称AK）是阿里云提供给用户的永久访问凭据，一组由AccessKey ID和AccessKey Secret组成的密钥对。发起的请求会携带AccessKey ID和AccessKey Secret加密请求内容生成的签名，进行身份验证及请求合法性校验。 |
| STS临时凭证 | 调用[AssumeRole - 获取扮演角色的临时身份凭证](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)接口，扮演某个RAM角色，获取该角色的STS临时凭证（STS Token），从而使用STS Token访问阿里云 |
| RAM角色（RAM Role） | RAM角色是一种虚拟用户，可以被授予一组权限策略。与RAM用户不同，RAM角色没有永久身份凭证（登录密码或访问密钥），需要被一个可信实体扮演。扮演成功后，可信实体将获得RAM角色的临时身份凭证，即安全令牌（STS Token），使用该安全令牌就能以RAM角色身份访问被授权的资源。 |
| 实例RAM角色 | 当ECS实例或部署在ECS实例上的应用需要访问其他云资源时，必须配置访问凭证，阿里云服务会通过访问凭证验证您的身份信息和访问权限。实例RAM角色允许您将一个角色关联到ECS实例，实现在实例内部自动获取并刷新临时访问凭证，无需直接暴露AccessKey，减少密钥泄露的风险。 |

## 安全性

### ECS元数据服务器访问模式

默认情况下，实例元数据服务器可同时通过普通模式和加固模式访问。为了进一步增强安全性，您可以设置实例元数据服务器访问模式为**仅加固模式**。采用ECS实例的元数据加固策略来获取RAM角色的初始化凭据，相较于普通模式，此方式采纳了一种更为严谨的安全逻辑：首先在ECS实例内部自动生成一个具有时效限制的token，利用此token作为凭据，向元数据服务（Metadata Server）请求获得STS（Security Token Service）临时凭证。这一系列操作构成了凭据客户端的安全初始化流程。什么是加固模式请参见[加固模式](https://help.aliyun.com/zh/ecs/user-guide/view-instance-metadata/)的介绍。

### 对象存储OSS安全防护能力

阿里云对象存储OSS（Object Storage Service）具有丰富的安全防护能力，通过多项合规认证，支持服务器端加密、客户端加密、防盗链白名单、细粒度权限管控、日志审计、合规保留策略（WORM）等特性。详情参见[OSS安全合规](https://help.aliyun.com/zh/oss/security-and-compliance/overview-11)。

## 注意事项

### 支持STS的云服务

详情参见[支持STS的云服务](https://help.aliyun.com/zh/ram/services-that-work-with-sts)。

### 客户端OSS直传适用的场景

本方案中，客户端直接上传文件到OSS，适用于需要限制上传文件属性（文件大小、上传路径、文件类型）以及批量文件上传的场景。需要注意的是，对于基于分片上传大文件以及基于分片断点续传的场景，该客户端直传方案并不支持。

## 实施步骤

### 实施准备

- 请确保您已经[开通OSS对象存储服务](https://help.aliyun.com/zh/oss/getting-started/getting-started-with-oss#13226d99c2mhz)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 服务端程序实现无AK架构

您需要部署一个服务端程序，负责生成OSS上传/下载所需的签名Post Policy和URL，并返回给客户端使用。为保证AccessKey凭证安全，避免因为AccessKey凭证泄露导致的安全问题，固定AccessKey都不应该硬编码在您的应用程序中，建议您的服务端应用程序实现无AK架构，使用STS临时凭证代替固定AccessKey。针对不同类型的云上应用部署方式，您可以选择相应的方案实现STS临时凭证的使用：

- 针对在ECS实例上部署的应用，[通过ECS实例角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-240)，将RAM角色跟实例进行绑定，应用程序中即可通过ECS实例RAM角色，获取实例RAM角色的STS临时授权访问凭证。
- 针对在ACK上部署的应用，在容器服务Kubernetes版中，一个集群可以部署多个服务，同一个容器节点可能包含多个不同服务的Pod，在多租户场景下，若部署不受信任的服务，该服务可直接访问ECS的元数据服务（Meta Data Server），获取Worker节点关联实例RAM角色的临时令牌STS Token，会造成身份权限的泄露。[通过容器服务RRSA实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-241)，在Pod维度即可扮演对应角色实现STS临时凭证的获取。
- 针对在函数计算中部署的Serverless应用，[通过FC函数角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-242)，将RAM角色跟函数进行绑定，应用程序中即可通过函数RAM角色，获取RAM角色的STS临时授权访问凭证。

对于必须使用固定AccessKey的场景，建议对AccessKey进行集中化管控。推荐以下解决方案：

- [通过KMS实现固定AccessKey的集中管控](https://help.aliyun.com/zh/well-architected/solution-237)，通过该方式，可以实现AccessKey的集中化管控，当业务需要使用AccessKey时，可以为其托管一个RAM用户AccessKey，并可以设置自动轮转周期，降低AccessKey泄漏风险。轮转时凭据管家会调用访问控制RAM（Resource Access Management），先创建一个新的AccessKey，然后删除旧的AccessKey。同时KMS将新的AccessKey写入凭据值，并删除旧的AccessKey对应的凭据值。当您发现RAM凭据泄露时，可以通过立即轮转凭据进行应急处理，此时推荐将轮转时长设置为30分钟实现快速轮转，降低泄漏造成的损失。

本方案中，将服务端应用部署在ECS实例中为例，使用ECS实例角色的STS Token给OSS上传/下载文件所需要的Post Policy、URL等进行签名，并返回客户端使用。您在真实业务中使用时，建议将服务端逻辑内置在您的业务应用中，通过业务应用已有的登录态、鉴权等机制，保证请求的合法性。接下来简单介绍在创建ECS实例时，如何为ECS实例绑定RAM角色。更详细的配置方式，您可以参考[通过ECS实例角色实现临时凭证的获取和使用](https://help.aliyun.com/zh/well-architected/solution-240)。

1. 登入应用账号，前往[实例创建页](https://ecs-buy.aliyun.com/wizard/#/)。
2. 选择**自定义购买**页签。
3. 按需选择付费类型、地域、实例规格、镜像等配置。各配置项详细说明，请参考[配置项说明](https://help.aliyun.com/zh/ecs/user-guide/create-an-instance-by-using-the-wizard)。
4. 展开**高级选型（选填）**表单，在**实例RAM角色**中，选择要绑定的RAM角色。本方案中，以名为EcsInstanceRole的实例角色为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3076581571/p970748.png)
5. 在最终创建实例前，请在页面右侧检查实例的整体配置并配置使用时长等选项，确保各项配置符合您的要求。
6. 阅读并签署**《云服务器ECS服务条款》**等服务协议（若已签署，则无需重复签署，请以页面提示为准），然后单击**确认下单**。

创建实例一般需要3~5分钟，请您耐心等待。您可前往控制台的实例列表页面查看实例的状态，当实例状态变为**运行中**时，表示实例创建完成。

#### 配置实例RAM角色权限

在本方案中，将服务端部署在ECS实例中为例，您需要为ECS实例角色授予OSS文件上传和下载的权限。客户端在需要往OSS上传或者从OSS下载文件时，向服务端请求签名授权，服务端收到请求并校验请求合法性后，会使用ECS实例角色的身份进行预签名并返回给客户端，客户端使用预签名的结果，以ECS实例角色的身份权限，直接向OSS上传文件或者从OSS下载文件。

如果您使用的是容器服务RRSA、函数角色或者固定AccessKey的方案，也需要按照如下步骤，给对应的RAM角色或RAM用户配置权限策略。

1. 登入应用账号，前往[RAM控制台](https://ram.console.aliyun.com)。
2. 左侧导航栏中，单击**权限管理** > **权限策略**。
3. 单击**创建权限策略**按钮，进入创建权限策略页面，切换为**脚本编辑**。
4. 将以下策略内容复制到策略文档输入框中，注意将内容中的`<OSS Bucket名称>`替换为具体的保存文件的OSS Bucket名称。`{
 "Version": "1",
 "Statement": [
 {
 "Action": [
 "oss:GetObject",
 "oss:PutObject"
 ],
 "Resource": "acs:oss:*:*:<OSS Bucket名称>/*",
 "Effect": "Allow"
 }
 ]
}`
5. 单击**继续编辑基本信息**，填写策略名称等基本信息，这里策略名称以EcsInstanceRolePolicy为例。
6. 单击**确定**，完成策略创建。
7. 在左侧导航栏，选择**身份管理** > **角色**。
8. 在角色页面，找到目标ECS实例RAM角色，既上一个章节中，为ECS实例绑定的RAM角色，本方案中，以名为EcsInstanceRole的实例角色为例，单击**操作**列的**新增授权**。
9. 在**新增授权**面板，为RAM角色授权。其中权限策略，选择刚刚创建出来的权限策略，这里以EcsInstanceRolePolicy为例
10. 单击**确认新增授权**，完成权限策略的绑定。

#### 实现OSS文件直传和下载

本方案，以将服务端部署在ECS实例中为例，服务端程序首先会获得ECS实例角色的临时凭证STS Token，然后使用实例角色的STS Token为客户端上传/下载OSS文件所需的Post Policy或URL进行签名，并返回给客户端。以此保证全链路无需透出固定AccessKey。

本方案代码以Java SpringBoot为例，并未对请求合法性进行校验，您在真实业务中使用时，建议将服务端逻辑内置在您的业务应用中，通过业务应用已有的登录态、鉴权等机制，来保证请求的合法性。示例代码详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-oss-pre-signed)。

##### 初始化Client

首先您需要获取ECS实例角色的临时凭证STS Token，使用该STS Token初始化OSS服务的SDK Client，后续会使用该OSS SDK Client进行预签名。推荐您使用阿里云的Credentials工具，获取并管理ECS实例角色的STS Token：

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

然后使用Credentials的Client初始化OSS服务的SDK Client。需要注意的是，OSS SDK Client也建议是单例模式，不要每次请求都重新New，避免出现内存泄露的问题。

```
import com.aliyun.credentials.models.CredentialModel;
import com.aliyun.oss.ClientBuilderConfiguration;
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.common.auth.Credentials;
import com.aliyun.oss.common.auth.CredentialsProvider;
import com.aliyun.oss.common.auth.DefaultCredentials;
import com.aliyun.oss.common.comm.SignVersion;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.annotation.PostConstruct;

@Configuration
public class OssConfig {

    @Value("${region.id}")
    String regionId;

    @Value("${oss.bucket}")
    String bucket;

    @Value("${service.address}")
    String serviceAddress;

    // OSS文件所在的文件夹
    // 本示例，未区分调用者身份，允许调用用户上传文件到同一个固定的 OSS 文件夹下
    // 您可以根据调用者身份，使用调用者的登录信息等唯一标识作为 OSS 文件夹名称，保证不同调用者和不同文件夹绑定并且只允许上传文件到与其绑定的文件夹下，以此隔离调用用户的资源和权限
    String dir = "example/";

    String endpoint;

    String host;

    // 上传文件时，post policy 的过期时间，单位为毫秒
    long uploadExpireTime = 3600;

    // 下载文件时，签名 url 的过期时间，单位为毫秒
    long downloadExpireTime = 300;

    String postCallbackUrl;

    @Autowired
    com.aliyun.credentials.Client credentialClient;

    @PostConstruct
    public void init() {
        this.endpoint = "oss-" + regionId + ".aliyuncs.com";
        this.host = "https://" + bucket + "." + endpoint;
        this.postCallbackUrl = serviceAddress + "/upload/callback";
    }

    // 自定义 OSS Credentails Provider，通过该 Provder 初始化下方 OSS SDK Client
    // 该 Provdier 会从 Credentail SDK Client 中获取最新的 STS Token
    // Credentail SDK Client 会自动更新 STS Token，您无需关心 STS Token 到期如何更换的问题
    @Bean
    CredentialsProvider getOssCredentialsProvider() {
        return new CredentialsProvider() {
            @Override
            public void setCredentials(Credentials credentials) {
            }

            @Override
            public Credentials getCredentials() {
                // 保证线程安全，从 CredentialModel 中获取 ak/sk/security token
                CredentialModel credentialModel = credentialClient.getCredential();
                String ak = credentialModel.getAccessKeyId();
                String sk = credentialModel.getAccessKeySecret();
                String token = credentialModel.getSecurityToken();
                return new DefaultCredentials(ak, sk, token);
            }
        };
    }

    // 初始化阿里云 OSS SDK 客户端
    // OSS SDK Client 建议是单例模式，不要每次请求都重新 New 一个，避免出现内存泄露的问题
    @Bean
    OSS getOssClient(CredentialsProvider credentialsProvider) {
        // 建议使用更安全的V4签名算法，则初始化时需要加入endpoint对应的region信息，同时声明SignVersion.V4
        // OSS Java SDK 3.17.4及以上版本支持V4签名。
        ClientBuilderConfiguration configuration = new ClientBuilderConfiguration();
        configuration.setSignatureVersion(SignVersion.V4);

        return OSSClientBuilder.create()
            .endpoint(endpoint)
            .credentialsProvider(credentialsProvider)
            .clientConfiguration(configuration)
            .region(regionId)
            .build();
    }

    public String getBucket() {
        return bucket;
    }

    public String getHost() {
        return host;
    }

    public long getUploadExpireTime() {
        return uploadExpireTime;
    }

    public String getPostCallbackUrl() {
        return postCallbackUrl;
    }

    public String getDir() {
        return dir;
    }

    public long getDownloadExpireTime() {
        return downloadExpireTime;
    }
}
```

##### OSS文件直传

通过预签名机制，实现客户端直接上传文件到OSS的过程如下：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3076581571/p970750.png)

1. 客户端向服务端请求Post签名、Post Policy和回调等信息。
2. 服务端生成并返回Post签名、Post Policy和回调设置等信息给客户端。
3. 客户端使用Post签名、Post Policy和回调设置等信息调用PostObject通过HTML表单的方式直接上传文件到OSS。
4. 客户端上传文件到OSS结束后，OSS解析客户端的上传回调设置，发送Post回调请求给服务端。
5. 服务端对OSS回调请求进行验证，如果验证通过，返回成功响应给OSS。
6. OSS将服务端返回的消息返回给客户端。

需要注意的是：通过Post Policy，您可以限制客户端允许往哪个文件夹下上传文件。在Post Policy有效期内，您可以使用该Post Policy和签名持续往允许的文件夹下上传文件，客户端不需要每次上传都重新请求服务端获取Post Policy。

###### 服务端实现

客户端在需要往OSS上传文件时，向服务端请求上传所需的Post Policy和对应的签名，服务端收到请求并校验请求合法性后，需要根据当前调用者的用户身份，构造Post Policy。OSS Post Policy用于定义用户通过HTML表单上传文件到OSS时的权限限制和约束条件，有如下两部分组成：

1. expiration：用于指定Post Policy的过期时间，以ISO8601 GMT时间表示。例如指定为2023-12-03T13:00:00.000Z，表示必须在2023年12月03日13点之前发起POST请求。
2. conditions：用于指定POST请求表单域的合法值。通过多项参数限制上传操作，例如允许上传的Bucket名称、Object前缀、有效期、允许的HTTP方法、上传内容的大小限制、内容类型限制等。

详细的Post Policy介绍和conditions支持的字段，请参考[Post Policy](https://help.aliyun.com/zh/oss/developer-reference/signature-version-4-recommend)。本方案示例中，限制了上传文件的大小和允许上传到的文件夹。

```
// 构造 OSS Policy
// 更多 Policy，请参考：https://help.aliyun.com/zh/oss/developer-reference/signature-version-4-recommend#49c0713824yc9
PolicyConditions policyConds = new PolicyConditions();
// 限制上传文件的大小
policyConds.addConditionItem(PolicyConditions.COND_CONTENT_LENGTH_RANGE, 0, 1048576000);
// 限制 OSS Object 名称。这里通过 starts-with 指定前缀，限制上传文件所在的目录
// 本示例，未区分调用者身份，允许调用用户上传文件到同一个固定的 OSS 文件夹下
// 您可以根据调用者身份，使用调用者的登录信息等唯一标识作为 OSS 文件夹名称，保证不同调用者和不同文件夹绑定并且只允许上传文件到与其绑定的文件夹下，以此隔离调用用户的资源和权限
policyConds.addConditionItem(MatchMode.StartWith, PolicyConditions.COND_KEY, ossConfig.getDir());

String postPolicy = ossClient.generatePostPolicy(expiration, policyConds);
```

接着，您需要对生成的Post Policy进行签名。OSS SDK提供了签名的方法，您可以直接使用。

```
byte[] binaryData = postPolicy.getBytes("utf-8");
String encodedPolicy = BinaryUtil.toBase64String(binaryData);
String postSignature = ossClient.calculatePostSignature(postPolicy);
```

在客户端向OSS直传文件，不再经过服务端中传，为保证服务端能够感知客户端的上传行为，OSS支持在直传文件时配置Callback回调信息，客户端上传完后，OSS会根据Callback回调的配置，将上传后的文件信息回调给服务端。Callback参数是由一段经过Base64编码的JSON字符串（字段）构成，JSON字段的详细信息请参见下表。

| 字段 | 是否必选 | 描述 |
| --- | --- | --- |
| callbackUrl | 是 | 文件上传成功后，OSS向此URL发送回调请求。请求方法为POST，Body为callbackBody指定的内容。正常情况下，该URL需要响应`HTTP/1.1 200 OK`，Body必须为JSON格式，响应头Content-Length必须为合法的值，且大小不超过3 MB。支持同时配置最多5个URL，多个URL间以分号（;）分隔。OSS会依次发送请求，直到第一个回调请求成功返回。支持HTTPS地址。为了保证正确处理中文等情况，callbackUrl需做URL编码处理，例如`http://example.com/中文.php?key=value&中文名称=中文值`需要编码为`http://example.com/%E4%B8%AD%E6%96%87.php?key=value&%E4%B8%AD%E6%96%87%E5%90%8D%E7%A7%B0=%E4%B8%AD%E6%96%87%E5%80%BC`。 |
| callbackHost | 否 | 发起回调请求时Host头的值，格式为域名或IP地址。callbackHost仅在设置了callbackUrl时有效。如果没有配置callbackHost，则解析callbackUrl中的URL，并将解析的Host填充到callbackHost中。 |
| callbackBody | 是 | 发起回调时请求Body的值，例如`key=${object}&etag=${etag}&my_var=${x:my_var}`。callbackBody支持OSS系统参数、自定义变量和常量。在PutObject和CompleteMultipart中，自定义变量通过callback-var传递。在PostObject中，各个变量通过表单域传递。 |
| callbackSNI | 否 | 客户端发起回调请求时，OSS是否向通过callbackUrl指定的回源地址发送服务器名称指示SNI（Server Name Indication）。是否发送SNI取决于服务器的配置和需求。对于使用同一个IP地址来托管多个TLS/SSL证书的服务器的情况，建议选择发送SNI。callbackSNI取值如下：true：发送SNI。false（默认值）：不发送SNI。 |
| callbackBodyType | 否 | 发起回调请求的Content-Type。Content-Type支持以下两种类型：application/x-www-form-urlencoded（默认值）：将经过URL编码的值替换callbackBody中的变量。application/json：按照JSON格式替换callbackBody中的变量。 |

其中，通过callbackBody，您可以定义回调时带给服务端的文件信息参数，OSS本身提供了系统参数，包括文件（OSS对象）的完整路径、图片的尺寸、文件的大小等等，同时OSS也提供了自定义参数的能力，您可以通过callback-var参数来配置自定义参数。自定义参数是一个Key-Value对（例如：`my_var=${x:my_var}`）。在OSS发起POST回调请求的时候，会将callback-var自定义参数以及上述系统参数放在POST请求的body中，方便服务端接收回调信息。更多详情，请参阅[Callback](https://help.aliyun.com/zh/oss/developer-reference/callback)。

本示例中，也进行了Callback配置，如果您的服务端不需要感知客户端的上传行为，您可以忽略这部分代码配置。

```
// 构造 OSS Callback 配置
// 客户端上传完后，OSS 会根据 Callback 配置，将上传后的文件信息回调给服务端
// 如果您的业务场景不需要感知客户端上传结果，可以忽略此段回调配置的代码
OssPostCallback ossPostCallback = OssPostCallback.builder()
    .callbackUrl(ossConfig.getPostCallbackUrl())
    // callbackBody 支持 OSS 系统参数、自定义变量和常量
    // 更多参数配置，请参考：https://help.aliyun.com/zh/oss/developer-reference/callback#a8a8e930e31fv
    .callbackBody(
        "filename=${object}"
            + "&size=${size}"
            + "&mimeType=${mimeType}"
            + "&height=${imageInfo.height}"
            + "&width=${imageInfo.width}"
    )
    .callbackBodyType("application/x-www-form-urlencoded")
    .build();
String base64PostCallback = BinaryUtil.toBase64String(JSON.toJSONString(ossPostCallback).getBytes());
```

最后，服务端需要将Post Policy、签名、回调信息等返回给客户端，本示例中定义了一个名为`PostSignatureResp`的简单Java类，用来构造返回给客户端的响应对象，客户端通过签名等信息直接往OSS上传文件。

```
PostSignatureResp postSignatureResp = PostSignatureResp.builder()
    .accessKeyId(ossCredentialsProvider.getCredentials().getAccessKeyId())
    .securityToken(ossCredentialsProvider.getCredentials().getSecurityToken())
    .policy(encodedPolicy)
    .signature(postSignature)
    .dir(ossConfig.getDir())
    .host(ossConfig.getHost())
    .expires(String.valueOf(expireEndTime / 1000))
    .callback(base64PostCallback)
    .build();

return postSignatureResp;
```

###### 客户端实现

客户端在需要上传文件时，首先需要向服务端请求Post签名、Post Policy和回调等信息。本示例中，以Web端JavaScript为例。

```
let postSignatureResp = {};
/**
 * 以下变量请根据实际情况进行修改和填写
 */
// 这里是本地服务端的地址，请修改为真实的服务端地址
const serverAddress = 'http://127.0.0.1:7001';

function getPostSignature() {
    fetch(`${serverAddress}/upload/getPostSignature`)
        .then((response) => response.json())
        .then((data) => {
            postSignatureResp = data;
        });
}
```

然后客户端使用Post签名、Post Policy和回调设置等信息调用PostObject通过HTML表单的方式直接上传文件到OSS。

```
let fileName = '';
function upload() {
    const files = document.getElementById('file').files;
    if (files.length === 0) {
        alert('请选择文件！');
        return;
    }

    fileName = files[0].name;
    const { policy, signature, accessKeyId, host, securityToken, dir, callback } = postSignatureResp;

    const formData = new FormData();
    // 指定成功上传时，服务端返回状态码200，默认返回204。
    formData.append('success_action_status', '200');
    formData.append('policy', policy);
    formData.append('signature', signature);
    formData.append('OSSAccessKeyId', accessKeyId);
    // 如果本次访问是使用临时凭证STS Token，则需要指定该项为SecurityToken的值
    if (securityToken) {
        formData.append('x-oss-security-token', securityToken);
    }
    formData.append('key', dir + fileName);
    // 如果不需要回调通知服务端，这里可以不设置 callback 入参
    if (callback) {
        formData.append('callback', callback)
    }
    // file必须为最后一个表单参数
    formData.append('file', files[0]);

    const param = {
        method: 'POST',
        body: formData,
    };
    fetch(host, param)
        .then(async (response) => {
            const data = await response.text();
            return {
                data,
                status: response.status,
            };
        })
        .then(({data, status}) => {
            if (status == 200) {
                alert(`上传成功！${callback ? `回调服务器返回的内容是：${data}` : ''}`);
            } else if (status == 203) {
                alert(`上传成功！但是OSS访问设置的上传回调服务器失败，失败原因是：${data}`);
            } else {
                alert(`上传失败！失败原因是：${data}`);
            }
        })
        .catch(error => {
            console.log(error);
            alert('上传失败！');
        });
}
```

##### OSS文件下载

通过预签名机制，实现客户端直接从OSS下载文件的过程如下：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3076581571/p970758.png)

1. 客户端向服务端请求文件下载的临时签名 URL。
2. 服务端生成并返回临时的签名的下载 URL。
3. 客户端使用临时签名的下载 URL，直接从OSS下载文件。

###### 服务端实现

客户端在需要从OSS下载文件时，向服务端请求下载文件的临时签名URL，服务端收到请求并校验请求合法性后，生成该文件的临时签名URL，返回给客户端，客户端使用该URL可以直接下载该文件。

```
long expireEndTime = System.currentTimeMillis() + ossConfig.getDownloadExpireTime() * 1000;
Date expiration = new Date(expireEndTime);

// 本示例，未区分调用者身份，允许调用用户从同一个固定的 OSS 文件夹下下载文件
// 您可以根据调用者身份，使用调用者的登录信息等唯一标识作为 OSS 文件夹名称，保证不同调用者和不同文件夹绑定并且只允许从与其绑定的文件夹下下载文件，以此隔离调用用户的资源和权限
GeneratePresignedUrlRequest generatePresignedUrlRequest = new GeneratePresignedUrlRequest(ossConfig.getBucket(), ossConfig.getDir() + fileName, HttpMethod.GET);
// 设置过期时间。
generatePresignedUrlRequest.setExpiration(expiration);

// 生成签名URL。
URL signedUrl = ossClient.generatePresignedUrl(generatePresignedUrlRequest);

return signedUrl.toString();
```

###### 客户端实现

客户端在需要下载文件时，向服务端请求该文件的临时签名URL，通过该URL直接下载。本示例中，以Web端JavaScript为例。

```
function getSignedDownloadUrl() {
    if (!fileName) {
        alert('请选择并上传文件！');
        return;
    }
    fetch(`${serverAddress}/download/getSignedUrl?fileName=${fileName}`)
        .then((response) => response.text())
        .then((data) => {
            window.open(data);
        });
}
```

##### 代码示例

###### 代码介绍

本方案提供Java SpringBoot的代码示例，方便客户能够快速完成应用改造。

###### 代码地址

代码详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-oss-pre-signed)。

## 故障排除

### 为什么Credentials SDK报错：not found credentials？

- 请确保您已经为您的ECS绑定了RAM实例角色，您可以登录到ECS实例上，执行命令：`curl http://100.100.100.200/latest/meta-data/ram/security-credentials/${实例角色名称}`，如果正确返回临时凭证，那么您已成功绑定了RAM实例角色。
- 如果您使用的是JAVA的Credentials SDK，请确保您的SDK版本>=0.3.2。
- 如果您使用的是Credentials工具的默认凭据链，请确保您已经配置了环境变量**ALIBABA_CLOUD_ECS_METADATA**，该环境变量的值配置为RAM实例角色的名称。
- 如果您在运行在ECS中的Docker环境中使用Credentials工具请确保Docker中可以正常访问到ECS Meta Service，您可以在Docker环境中，执行命令：`url http://100.100.100.200/latest/meta-data/ram/security-credentials/${实例角色名称}`，如果正确返回临时凭证，那么您的Docker环境可以正常访问ECS Meta Service。如果您使用的是Credentials工具的默认凭据链，请确保您在Docker环境中已经配置了环境变量**ALIBABA_CLOUD_ECS_METADATA**，该环境变量的值配置为RAM实例角色的名称。需要注意的是，这里不要把环境变量配置到ECS实例上。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-244（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
