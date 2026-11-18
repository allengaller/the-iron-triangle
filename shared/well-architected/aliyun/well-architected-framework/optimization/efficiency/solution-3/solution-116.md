<!-- source: https://help.aliyun.com/zh/well-architected/solution-116 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929454 -->

# 多ACK集群连接公共ACR方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2986581571/p972679.png)

对于一家多业务组织的客户来说往往会有多个云账号，分别部署各个业务线的容器服务。但企业可能想使用一套统一的容器镜像仓库（ACR），就会面临多账号内多个ACK共享一套ACR了。如何合理规划好ACR实例上的命名空间，打通各个业务ACK集群与ACR的网络，包括如何精细化授权，都是客户需要考虑的。

本方案会介绍针对多账号多ACK场景下如何实现共享一套ACR集群，包括如何合理规划好权限、打通网络等。

## 方案优势

### 成本最优

通过一套ACR集群，而不是各个业务账号单独购买，可以有效降低实例成本。

### 统一管理

集团管理员可以对一套ACR集群进行权限管理，镜像加签与扫描等。统一管理，可以有效提升镜像这块的管理效率。

## 客户场景

### 多账号多ACK共享一套ACR

#### 场景描述

多账号企业，部署多套ACK集群，希望使用同一套ACR。

#### 适用客户

- 使用资源目录管理云上多个账号的企业客户。
- 使用多个阿里云账号的企业客户。
- 使用了ACR容器镜像服务的企业客户。

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2986581571/p972680.png)

架构说明

- 在运维账号部署一套企业级ACR服务，作为共享镜像服务提供给多个业务账号使用。
- 通过合理规范镜像服务上的命名空间，合理设置权限范围。
- 使用CEN-TR打通镜像服务与业务网络之间的连通性。
- 在业务账号内开启Private zone服务，完成ACR域名解析。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 转发路由器TR | [转发路由器TR（Transit Router）](https://help.aliyun.com/zh/cen/product-overview/how-transit-routers-work)是地域范围内企业级核心转发网元，可为您转发同地域或不同地域的网络实例间的流量，并支持在地域内定义灵活的互通、隔离、引流策略，帮助您打造一张灵活、可靠、大规模的企业级互联网络。转发路由器实例是云企业网实例的重要组成部分。 | 收费，CEN重要组成部分，请参见CEN计费规则。 |
| ACK容器服务 | [容器服务Kubernetes版（Alibaba Cloud Container Service for Kubernetes，简称容器服务ACK）](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/product-overview/what-is-ack)提供高性能可伸缩的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ack/billing-information)。 |
| ACR容器镜像服务 | [阿里云容器镜像服务ACR](https://help.aliyun.com/zh/acr/product-overview/what-is-container-registry)（Alibaba Cloud Container Registry）是面向容器镜像、Helm Chart等符合OCI标准的云原生制品安全托管及高效分发平台。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/acr/product-overview/billing-description)。 |
| PrivateZone | [PrivateZone](https://help.aliyun.com/zh/document_detail/64611.html)，是基于阿里云专有网络VPC（Virtual Private Cloud）环境的私有DNS服务。该服务允许您在自定义的一个或多个VPC中将私有域名映射到IP地址。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/document_detail/71338.html)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 运维账号 | 企业跟运维工具相关的服务会部署在这个账号内，如CI/CD工具、镜像仓库等。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |

## 安全性

### 跨账号扮演角色

业务账号里面的ACK集群需要有assumeRole权限，扮演运维账号中特定角色。这个角色具备操作ACR指定命名空间的权限。为了避免出现权限过大，建议精细化授权。容器镜像授权请参考[官方链接](https://help.aliyun.com/zh/acr/user-guide/ram-authorization-information)。

### 业务VPC安全性

业务账号内的VPC为了能够跟ACR连接，需要通过CEN-TR来做中转。但业务账号VPC之间并不一定需要打通网络连接。这个需要通过TR来灵活配置路由。具体可以参考云企业网[路由管理](https://help.aliyun.com/zh/cen/user-guide/manage-routes-1/)。

### 跨账号网络实例授权

在转发路由器实例连接其他账号的网络实例前，需要其他账号的网络实例对转发路由器实例进行授权。授权说明及操作详情参见[跨账号网络实例授权](https://help.aliyun.com/zh/cen/user-guide/grant-permissions-on-a-network-instance-that-belongs-to-another-account)。

## 注意事项

### 免密组件限制

使用ACK的免密组件涉及的镜像及集群是有限制的。具体可以查看[官方文档](https://www.alibabacloud.com/help/zh/container-registry/latest/use-the-aliyun-acr-credential-helper-component-to-pull-images-without-a-password)。

### 跨地域限制

本方案介绍是同地域场景，如果涉及到跨地域集群，不建议用这套方案。还是一个地域部署一套ACR集群。

## 实施步骤

### 数据规划

为了让整个操作更加通俗易懂，假设有一家企业X 。其架构图如下：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2986581571/p972683.png)

#### 账号数据

| 账号 | VPC | 功能说明 |
| --- | --- | --- |
| 运维账号，别名：A账号（以下操作均用A账号表示）账号UID：xxxxx888 | VPC1：172.16.0.0/24 | 1、部署了一套ACR服务2、配置CEN实例，配置跨账号加载 |
| cainiao账号，别名:B账号（以下操作均用B账号表示）账号UID：xxxxxx857 | VPC2：192.168.0.0/16 | 1、部署了一套ACK集群2、开通PrivateZone服务 |

#### ACR规划

| 账号 | 命名空间 | 功能 |
| --- | --- | --- |
| 运维账号，别名：A账号 | cainiao | 存放cainiao业务线的镜像 |
| alipay | 存放alipay业务线的镜像 |  |

### 实施准备

- 在运维账号（A）中完成VPC创建，完成开通ACR高级版。
- 在运维账号（A）中购买一台ECS用于当持续集成机（有Docker环境）。
- 在cainiao账号（B）中配置VPC，用于部署ACK用的。
- 在cainiao账号（B）中完成ACK购买（网络架构选择Terway），并开通PrivateZone服务。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 各场景步骤

#### 场景1：编译机（ECS）推镜像到ACR

##### 步骤一：配置访问控制

在运维账号A 的ACR访问控制页添加A账号内的VPC （编译机所在的VPC）

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2986581571/p972686.png)

创建专有网络成功后，ACR会自动在云解析PrivateZone中创建解析Zone，为您解析域名。您可以在云解析PrivateZone查看解析Zone。相关[链接](https://help.aliyun.com/zh/acr/user-guide/configure-access-over-vpcs)。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2986581571/p972682.png)

这样在当前这个VPC里面的ECS就能够正常解析到这个域名了。

##### 步骤二：配置ACR设置账号登录信息

配置命名空间

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3986581571/p972684.png)

注意！这个命名空间需要设置成私有。

配置访问密码

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2986581571/p972685.png)

因为是编译机，所以可以设置一个固定密码。

##### 步骤三：ECS推送镜像到ACR

注意！这里我们没有去做精细化权限控制，考虑到是编译机，所以没对Namespace粒度授权。

1. 登录`$ docker login --username=xx@xxxxx shareacr-registry-vpc.cn-shanghai.cr.aliyuncs.com`
2. 推镜像a. dockerfile`FROM nginx:1.8
RUN mkdir /app``$ docker build -t shareacr-registry-vpc.cn-shanghai.cr.aliyuncs.com/cainiao/a1:v0.1 -f a.dockerfile ./
$ docker push shareacr-registry-vpc.cn-shanghai.cr.aliyuncs.com/cainiao/a1:v0.1`注意，这里的地址是 -vpc，这样走的就是内网流量。

这样镜像推上去之后，在业务账号cainiao（B账号）中的ACK就可以拉取镜像了。

#### 场景2：在B账号的ACK集群上面访问运维账号里面的ACR私有镜像

##### 步骤一：打通A账号与B账号VPC互通

1. 在B账号的VPC中配置跨账号授权，其中对方账号UID请写A账号。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3986581571/p972687.png)
2. 登录A账号，完成CEN配置。需要将A\B账号对应的VPC都加进去，高级选择默认都勾上。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2986581571/p972688.png)
3. 验证A与B账号两个VPC内的ECS网络互通登录A账号的ECS（编译机），Ping B账号ACK对应的worker节点内网IP。如果正常Ping通，则说明网络打通。

##### 步骤二：配置B账号的PrivateZone

1. 配置Zone![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2986581571/p972691.png)
2. 配置PrivateZone域名解析**注意:**这里A记录，对应的IP地址需要跟A账号里面的保持一致。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3986581571/p972689.png)
3. 配置PrivateZone关联VPC![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3986581571/p972690.png)**注意:**这里面需要选择ACK所在的VPC。
4. 登录B账号中的ACK所在的某台worker节点，去ping 下这个域名：shareacr-registry-vpc.cn-shanghai.cr.aliyuncs.com 只要能够正常解析并且可达，则说明网络层正常。

##### 步骤三：配置B账号的免密访问ACR私有镜像

到此，网络层已经正常了。接下来就是需要配置权限及免密访问。

整个操作分4步：

1. A账号：配置一个RAM角色，具备拉取指定私有仓库下的私有镜像（精细化授权由这个角色决定）。
2. A账号：这个RAM角色需要允许让B用户下的ACK Worker RAM角色扮演（信任策略）。
3. B账号：B账号下的ACK集群的Worker RAM角色有扮演其他账号角色的权限（AliyunAssumeRoleAccess）。
4. B账号：设置B账号下的Worker RAM角色扮演A账号中的角色（configMap中的assumeRoleARN）。

接下来详细介绍一下每一步的操作过程

第一步：配置一个RAM角色，并授权

1. 在A账号创建RAM角色：受信实体为**阿里云账号**类型的RAM角色。
2. 自定义RAM角色权限策略内容，确保该RAM角色拥有拉取A用户私有镜像的权限。创建自定义策略名称：acr-policy`{
 "Version": "1",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "cr:*",
 "Resource": "*"
 },
 {
 "Action": [
 "cr:GetAuthorizationToken",
 "cr:ListInstanceEndpoint",
 "cr:PullRepository"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`
3. 将这个策略与角色相关联![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2986581571/p972693.png)

第二步：修改这个RAM角色对应的信任策略。

1. 查看B账号ACK集群的worker RAM角色的ARN信息![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3986581571/p972692.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2986581571/p972694.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3986581571/p972695.png)
2. 修改A账号下的角色acr-role对应的信任策略对应的信任策略：`{
 "Statement": [
 {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
 "RAM": [
 
 "acs:ram::{B账号UID}:role/{B账号ACK对应的Worker RAM角色的ARN}"
 ]
 }
 }
 ],
 "Version": "1"
}`

第三步：修改B账号worker RAM角色添加AssumeRole权限

1. 选择这个角色，添加AssumeRole权限。

第四步：配置B账号下的Worker RAM角色扮演A账号中的角色

1. 升级aliyun-acr-credential-helper组件。登录[容器服务管理控制台](https://cs.console.aliyun.com/)。在控制台左侧导航栏中，单击**集群**。在**集群列表**页面，单击目标集群操作列下的**更多 > 系统组件管理**。在**安全**区域，找到**aliyun-acr-credential-helper**，单击**升级**。
2. 配置acr-configuration配置项。需要修改的配置：`acr-registry-info: |
 - instanceId: "{ACR实例ID}"
 domains: "shareacr-registry-vpc.cn-shanghai.cr.aliyuncs.com"
 assumeRoleARN: "{A账号角色的ARN}"`**注意:**这里面的domains需要填的是VPC内网地址。assumeRoleARN写的是A账号对应角色的ARN（即第一步创建的Role对应的ARN）。

完成以上4步操作之后，可以在ACK中创建一个Deployment资源，试一下是不是正常能够pull到镜像。

创建YAML格式：

```
apiVersion: apps/v1 # for versions before 1.8.0 use apps/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment-basic
  labels:
    app: nginx
spec:
  replicas: 2
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
        image: shareacr-registry-vpc.cn-shanghai.cr.aliyuncs.com/cainiao/a1:v0.1
        ports:
        - containerPort: 80
```

#### 延展

##### B账号的ACK只能拉特定命名空间下的私有镜像

常见的场景比如cainiao账号不能拉取alipay下面的镜像。

修改A账号里面的acr-policy策略:

```
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cr:ListInstance*",
                "cr:GetInstance*",
                "cr:ListSignature*"
            ],
            "Resource": "*"
        },
        {
            "Action": [
                "cr:GetAuthorizationToken",
                "cr:ListInstanceEndpoint",
                "cr:PullRepository"
            ],
            "Resource": "acs:cr:*:{uid}:repository/*/cainiao/*",
            "Effect": "Allow"
        }
    ]
}
```

再到B账号的ACK中去尝试拉另外一个namespace的镜像(shareacr-registry-vpc.cn-shanghai.cr.aliyuncs.com/alipay/a1:v0.1)

会报错：server message: insufficient_scope: authorization failed。

这样的话，可以在A账号里面针对不同成员账号（cainiao\alipay）配置不同的角色，进而能够达到精细化授权。

## 故障排除

### 业务账号内ACK无法正常pull images?

可能有两个原因导致：

- 网络不可达，可以登录ACK 对应的worker节点，上去Ping一下ACR仓库的域名。看看能不能正常Ping通。
- 网络通，权限不对，需要检查一下A、B两个账号里面所涉及到的几个角色配置是否按照文档进行配置的。

## 相关内容

- [cen 跨账号vpc互通文档](https://www.alibabacloud.com/help/zh/cloud-enterprise-network/latest/use-enterprise-edition-transit-routers-to-connect-vpcs-across-regions-and-accounts)
- [构建仓库与镜像帮助文档](https://www.alibabacloud.com/help/zh/container-registry/latest/image-build-use-container-registry-enterprise-edition-instances-to-build-images)
- [使用免密组件拉取容器镜像](https://www.alibabacloud.com/help/zh/container-registry/latest/use-the-aliyun-acr-credential-helper-component-to-pull-images-without-a-password)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-116（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
