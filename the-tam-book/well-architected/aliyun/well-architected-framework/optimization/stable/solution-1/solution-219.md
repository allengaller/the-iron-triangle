<!-- source: https://help.aliyun.com/zh/well-architected/solution-219 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929425 -->

# 通过MSE实现应用同城容灾

云原生网关默认采用多可用区部署，提供了地域级的、跨可用区的全局流量管理能力。在同城多活的场景下，能够确保对跨可用区的多个业务集群的请求实现高效负载均衡分配，在单个可用区内的业务集群发生故障时，可在1秒内完成故障节点的自动摘除从而实现故障转移，有效的保障服务连续性和高可用性。

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972188.png)

企业对在线的关键业务应用存在容灾需求，同城主机房发生故障，流量能切换到备机房，备机房具备实时接管能力。

本方案介绍了通过阿里云的NLB、MSE、ACK等产品组合能力，实现应用同城多活的方案。

## 方案优势

### 产品自身支持高可用

#### NLB高可用

NLB默认双可用区部署，且自身提供域名服务，自身提供域名服务，每个可用区一个VIP。支持将您拥有的常用域名通过CNAME方式解析到NLB实例的域名上，NLB的域名后面再挂上两个可用区的VIP，NLB本身支持健康检查，当单可用区的节点挂掉后，支持故障自动转移。

#### MSE云原生网关高可用

云原生网关默认双可用区部署，既使一个可用区的节点都挂了，另一个可用区的节点依旧可以正常工作。

#### MSE注册中心高可用

MSE注册中心默认三可用区部署，即使两个可用区的节点都挂了依然不会影响业务。

### 机房级故障的秒级自动转移

云原生网关对于关联服务的每个节点都建立了主动健康检查的机制，默认是2秒（也可以自己调整）。主动健康检查发现节点不健康，则会自动剔除，健康检查除了TCP的端口探测外，也支持HTTP的探测，通过健康检查机制，可以实现机房级故障的秒级自动转移。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972186.png)

### 非对等部署状态下的全局流量负载均衡

云原生网关会把两个集群的同名服务进行合并，然后在合并后的节点数量的基础上实现多种负载均衡策略，通过这种方式可以很好的实现两个机房在非对等部署状态下的负载均衡，例如：两个机房的同应用各部署了5个节点，这个时候云原生网关会把两个机房的同名服务的节点进行合并，变成10个。然后云原生网关在这10个中实现轮询等负载均衡策略，假设机房1的节点挂了4个，还剩一个。那这时分配给机房1的流量会自动的从50%降到10%，分配给机房2的流量会自动的从50%提升到90%。

### 流量的精细化管控

每个集群一套注册中心，应用启动的时候只像本可用区的注册中心注册。这样可以保证微服务调用在可用区内闭环。微服务调用可用区闭环以后，可以配合云原生网关的多种流量路由能力实现蓝绿和灰度等发布策略。

## 客户场景

### 应用同城多活

#### 场景描述

企业对在线的关键业务应用存在容灾需求，在同城多活的容灾架构下，能够实现机房级故障秒级自动转移、非对等部署状态下的全局流量负载均衡、流量的精细化管控等能力。

#### 适用客户

- 基于阿里云的ACK部署业务应用的客户。
- 使用了阿里云的SLB或NLB作为负载均衡设备的客户。

## 方案架构

本方案基于云原生网关+MSE注册中心实现应用同城多活，通过云原生网关的主动健康检查机制可以实现秒级故障自动转移。云原生网关支持管理多套ACK集群，通过对多个集群的同名服务合并的能力，可以实现非对等部署状态下的全局流量负载均衡。通过每个集群部署一套注册中心实现微服务调用可用区闭环以后，可以配合云原生网关的多种流量路由能力实现蓝绿和灰度等发布策略。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972192.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云原生网关 | [MSE云原生网关](https://help.aliyun.com/zh/mse/product-overview/cloud-native-gateway-overview)是兼容K8s Ingress标准的下一代网关产品，将传统的流量网关和微服务网关功能合并，降低50%资源开销，支持ACK容器服务和Nacos等多种服务发现方式，支持多种认证登录方式快速构建安全防线。 | 收费，详情参见[实例及版本选型](https://help.aliyun.com/zh/mse/product-overview/select-a-gateway-instance)。 |
| MSE注册中心 | [MSE注册中心](https://help.aliyun.com/zh/mse/product-overview/overview-2)支持注册和配置中心全托管（兼容Nacos、ZooKeeper、Eureka），具备丰富完善的监控报警、控制台运维操作和引擎类型。相比开源组件，具有更高性能、SLA保障和配置能力。 | 收费，详情参见[实例及版本选型](https://help.aliyun.com/zh/mse/product-overview/billing-overview-1/)。 |

## 安全性

### 设置云原生网关安全组规则

如云原生网关和后端服务所在的节点分别处于不同的安全组内，您可以通过设置安全组规则为云原生网关授予访问后端服务的权限，关于安全组的设置请参见：[设置安全组规则](https://help.aliyun.com/zh/mse/user-guide/set-security-group-rules)。

### 设置云原生网关黑白名单规则

IP黑名单和白名单是云原生网关提供的安全防护能力之一。您可以通过配置黑、白名单来拒绝或允许特定IP的访问请求。云原生网关支持在网关全局、域名和路由级别配置IP黑名单和白名单，满足精细化的访问控制诉求，关于黑白名单的设置请参见：[设置网关IP黑名单和白名单](https://help.aliyun.com/zh/mse/user-guide/configure-ip-address-blacklists-and-whitelists-for-gateways)。

### 设置MSE注册中心白名单

通过设置Nacos实例的白名单，您可以限制一定范围内的IP地址（通过单个IP地址或指定网段）来访问该实例，提高实例的安全性。在设置白名单时，需要获取发起访问设备的公网IP地址，确保配置白名单后，设备能够正确通过公网访问Nacos实例，在提升安全性的同时不影响使用，关于NACOS公网访问白名单的设置请参见：[设置白名单](https://help.aliyun.com/zh/mse/user-guide/configure-a-public-ip-address-whitelist-1)。

### 设置MSE注册中心Client访问鉴权

MSE中的Nacos注册配置中心可以开启鉴权功能，以降低某个实例被恶意用户非法获取或修改的风险。本文介绍如何在MSE上为Nacos实例配置鉴权访问以及如何使用Nacos Client进行鉴权访问，关于Nacos Client的访问鉴权配置请参见：[Nacos Client访问鉴权](https://help.aliyun.com/zh/mse/user-guide/access-authentication-by-the-nacos-client-1?spm=a2c4g.11186623.0.0.446e34e0GCF9ls)。

## 实施步骤

### 实施准备

1. 创建两个MSE 注册中心，具体操作请参见：[创建Nacos引擎](https://help.aliyun.com/zh/mse/getting-started/create-a-nacos-engine)。
2. 在两个不同可用区各创建一套K8s集群，具体操作请参见[创建Kubernetes托管版集群](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2/)。注：如果您要实现同城多活的其中一个K8s集群是在自建的IDC或其他云平台，您可以通过ACK One的[注册集群快速入门](https://help.aliyun.com/zh/ack/quick-start-for-registered-clusters)将云下的K8s集群接入云端。
3. 创建一套云原生网关实例，具体操作请参见：[创建云原生网关](https://help.aliyun.com/zh/mse/user-guide/create-a-cloud-native-gateway-1)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：30分钟。

### 操作步骤

### 步骤一：在集群中部署DEMO应用

1. 在两套可用区的ACK集群中部署DEMO应用，在使用过程中，下文部署脚本中的nacos_address和env需要替换成您的环境内容。`apiVersion: apps/v1
kind: Deployment
metadata:
 name: duohuo-provider
 labels:
 app: duohuo-provider
spec:
 replicas: 2
 selector:
 matchLabels:
 app: duohuo-provider
 template:
 metadata:
 labels:
 app: duohuo-provider
 spec:
 containers:
 - env:
 - name: nacos_address #注册中心的endpoint
 value: 'mse-a8473b30-nacos-ans.mse.aliyuncs.com:8848' 
 - name: env #所在可用区标识，izone,jzone
 value: izone
 image: 'registry.cn-hangzhou.aliyuncs.com/jinfengdocker/mse-duohuo-provider:v1'
 imagePullPolicy: Always
 name: duohuo-provider
 ports:
 - containerPort: 8080
 protocol: TCP
 resources:
 limits:
 cpu: '2'
 memory: 1Gi
 requests:
 cpu: '0.5'
 memory: 0.1Gi
---
apiVersion: apps/v1 
kind: Deployment
metadata:
 name: duohuo-consumer
 labels:
 app: duohuo-consumer
spec:
 replicas: 2
 selector:
 matchLabels:
 app: duohuo-consumer
 template:
 metadata:
 labels:
 app: duohuo-consumer
 spec:
 containers:
 - env:
 - name: nacos_address #注册中心的endpoint
 value: 'mse-a8473b30-nacos-ans.mse.aliyuncs.com:8848' 
 - name: env #所在可用区标识，izone,jzone
 value: izone
 image: 'registry.cn-hangzhou.aliyuncs.com/jinfengdocker/mse-duohuo-consumer:v1'
 imagePullPolicy: Always
 name: duohuo-consumer
 ports:
 - containerPort: 8080
 protocol: TCP
 resources:
 limits:
 cpu: '2'
 memory: 1Gi
 requests:
 cpu: '0.5'
 memory: 0.1Gi
---
apiVersion: v1
kind: Service
metadata:
 name: duohuo-consumer-service
spec:
 ports:
 - name: http
 port: 8080
 protocol: TCP
 targetPort: 8080
 selector:
 app: duohuo-consumer
 sessionAffinity: None
 type: ClusterIP``apiVersion: apps/v1
kind: Deployment
metadata:
 name: duohuo-provider
 labels:
 app: duohuo-provider
spec:
 replicas: 2
 selector:
 matchLabels:
 app: duohuo-provider
 template:
 metadata:
 labels:
 app: duohuo-provider
 spec:
 containers:
 - env:
 - name: nacos_address #注册中心的endpoint
 value: 'mse-7a4cd080-nacos-ans.mse.aliyuncs.com:8848' 
 - name: env #所在可用区标识，izone,jzone
 value: jzone
 image: 'registry.cn-hangzhou.aliyuncs.com/jinfengdocker/mse-duohuo-provider:v1'
 imagePullPolicy: Always
 name: duohuo-provider
 ports:
 - containerPort: 8080
 protocol: TCP
 resources:
 limits:
 cpu: '2'
 memory: 1Gi
 requests:
 cpu: '0.5'
 memory: 0.1Gi
---
apiVersion: apps/v1 
kind: Deployment
metadata:
 name: duohuo-consumer
 labels:
 app: duohuo-consumer
spec:
 replicas: 2
 selector:
 matchLabels:
 app: duohuo-consumer
 template:
 metadata:
 labels:
 app: duohuo-consumer
 spec:
 containers:
 - env:
 - name: nacos_address #注册中心的endpoint
 value: 'mse-7a4cd080-nacos-ans.mse.aliyuncs.com:8848' 
 - name: env #所在可用区标识，izone,jzone
 value: jzone
 image: 'registry.cn-hangzhou.aliyuncs.com/jinfengdocker/mse-duohuo-consumer:v1'
 imagePullPolicy: Always
 name: duohuo-consumer
 ports:
 - containerPort: 8080
 protocol: TCP
 resources:
 limits:
 cpu: '2'
 memory: 1Gi
 requests:
 cpu: '0.5'
 memory: 0.1Gi
---
apiVersion: v1
kind: Service
metadata:
 name: duohuo-consumer-service
spec:
 ports:
 - name: http
 port: 8080
 protocol: TCP
 targetPort: 8080
 selector:
 app: duohuo-consumer
 sessionAffinity: None
 type: ClusterIP`
2. 部署成功后，可以在对应的ACK集群中看到两个工作负载，和一个服务。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972187.png)

### 步骤二：云原生网关创建来源

在云原生网关中创建两个来源，关联您在两个可用区的容器集群。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972189.png)

### 步骤三：云原生网关创建服务

在云原生网关中创建服务，选择对应命名空间下的服务。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972194.png)

云原生网关支持跨集群的服务统一管理，下文中所创建的服务会自动的把两套Kubernetes集群中相同命名空间下的同名服务进行合并。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972190.png)

### 步骤四：云原生网关创建路由

创建路由，设置域名和匹配规则

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972196.png)

选择目标服务后保存并上线路由

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972191.png)

### 步骤五：切流效果验证

云原生网关可根据后端集群的工作负载数及健康状态动态的调整流量，下文分别演示两个集群工作负载数量**对等部署**、**非对等部署**、**机房故障**场景下的云原生网关自动切流效果。

可以启动下方的shell脚本，循环对网关发起请求

```
#!/bin/bash
for (( i = 1; i < 1000000000; i++ )); do
      curl http://114.55.248.189/helloDuohuo  #ip需要替换成您网关的公网IP
      sleep 1
      echo
done
```

#### 两套集群工作负载数量对等部署

两套集群中工作负载的副本保持一致

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972197.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972195.png)

通过上文的shell脚本发起请求，得到以下输出

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972198.png)

输出表明，流量被负载均衡到可用区I和可用区J，两个可用区的集群各承担了50%的流量。

#### 两个集群工作负载数量非对等部署

可用区I的集群副本数量缩容为1

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972200.png)

得到以下输出

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972201.png)

输出表明，可用区J的集群承担了90%的流量，可用区I的集群承担了10%的流量。

#### 机房故障场景下自动切流

可用区I的集群副本数量缩容为0，得到以下输出。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972203.png)

输出表明，100%的流量自动切换到了可用区J。

- 通过PTS压测，进一步观察可用区I故障后的自动切流时效性及切流过程中的流量损失

PTS新建压测场景

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972199.png)

压测的RPS配置为100后 ，点击保存去压测![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972204.png)压测执行到1分钟以后，手动的把可用区I集群中的所有工作负载删除掉，模拟集群故障，观察流量损失

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972205.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972206.png)

可以看到，MSE在I可用区的集群挂掉后，可实现秒级切流，切流过程中仅有不到1%的流量损失。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7876581571/p972202.png)

## 相关内容

- [通过云原生网关管理多个ACK集群](https://help.aliyun.com/zh/mse/user-guide/manage-services-in-multiple-ack-clusters-by-using-a-cloud-native-gateway?spm=a2c4g.11186623.0.0.52627b26xd0gfi)
- [通过云原生网关实现蓝绿部署、A/B测试和金丝雀发布](https://help.aliyun.com/zh/mse/use-cases/implement-blue-green-deployment-a-or-b-testing-and-canary-release-by-using-mse-cloud-native-gateways)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-219（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
