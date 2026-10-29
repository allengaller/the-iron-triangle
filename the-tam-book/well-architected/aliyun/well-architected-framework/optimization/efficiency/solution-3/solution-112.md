<!-- source: https://help.aliyun.com/zh/well-architected/solution-112 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929398 -->

# 企业CMP云资源创建方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9586581571/p971611.png)

随着企业信息化的发展，开展的业务逐渐增多，使用的云产品日趋复杂，如何管理庞大的IT基础设施，成为了企业IT稳定性及高效运行保障的关键环节。本方案介绍了一种企业CMP集成阿里云[服务目录](https://help.aliyun.com/product/358913.html)、通过服务目录快速创建云资源的方式，帮助企业实现对云资源创建的统一管理，帮助企业用户实现自助化服务，持续提升企业效率以及安全合规水平。

## 方案优势

### 用户友好界面

本方案通过嵌入服务目录页面的方式提供了用户友好的云资源创建可视化界面，用户只需填写模版参数就可以快速创建云资源。

### 降低开发成本

本方案通过集成服务目录的方式间接对接了多款云产品并且无需实现参数表单可视化，极大的降低了企业开发CMP的成本。

### 基础设施代码化

基于IaC思想，将资源编排过程使用[Terraform](https://www.terraform.io/)规范化，可以安全高效地部署、更改、版本化基础设施和应用程序，管理多层次的资源，减轻运维负担。

## 客户场景

### 统一资源创建

#### 场景描述

客户没有统一的云资源创建入口。

#### 适用客户

- 有一定开发能力，并且期望自己建设CMP的企业客户。

### 降低云产品接入成本

#### 场景描述

企业CMP已经接入部分阿里云产品，但是接入云产品的成本较高。

#### 适用客户

- 已经有自建CMP，期望接入更多云产品的企业客户。

## 方案架构

本方案主要介绍了企业CMP如何集成阿里云服务目录，并通过服务目录快速创建云资源。以下的流程图描述了该方案的执行步骤，用户登录到企业CMP，企业CMP通过访问登录服务获取免密登录URL，使用iframe标签嵌入服务目录页面。用户在服务目录页面填写模板参数，点击提交后，服务目录通过postMessage方法将启动计划ID发送给企业CMP，实现跨源通信。企业CMP获取到启动计划ID后，可以调用服务目录API查询启动计划详情，打通企业内部工作流，完成审批。审批通过后，企业CMP调用服务目录API执行启动计划，创建产品实例，查询实例详情并保存到本地数据库。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9586581571/p971599.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 服务目录 | [服务目录（Service Catalog）](https://help.aliyun.com/zh/service-catalog/product-overview/what-is-service-catalog)基于阿里云IaC（基础设施即代码）能力，构建自定义的阿里云IT服务列表，并可设定约束条件符合组织治理要求，从而降低企业业务上云时选用产品的难度，提高IT服务交付效率。 | 免费，但启动产品后产生的云产品实例根据各个云产品的实际情况计费，详情参见[产品定价](https://help.aliyun.com/zh/service-catalog/product-overview/overview)。 |
| 访问控制RAM | [访问控制（RAM）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/ram/product-overview/billing-methods)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| Terraform | Terraform是一种开源工具，用于安全高效地预览、配置和管理云基础架构和资源。详情可见[Terraform概述](https://help.aliyun.com/zh/document_detail/91285.html)。 |
| 阿里云账号（Alibaba Cloud account） | 开始使用阿里云服务前，首先需要注册一个阿里云账号。阿里云账号是阿里云资源归属、资源使用计量计费的基本主体。阿里云账号为其名下所拥有的资源付费，并对其名下所有资源拥有完全控制权限。默认情况下，资源只能被阿里云账号所访问，任何其他用户访问都需要获得阿里云账号的显式授权。阿里云账号就是操作系统的root或Administrator，所以我们有时称它为根账号或主账号。 |
| RAM角色（RAM role） | RAM角色是一种虚拟用户，与实体用户（阿里云账号、RAM用户和云服务）和教科书式角色（Textbook role）不同。具体如下：实体用户：拥有确定的登录密码或访问密钥。教科书式角色：教科书式角色或传统意义上的角色是指一组权限集合，类似于RAM里的权限策略。如果一个用户被赋予了这种角色，也就意味着该用户被赋予了一组权限，可以访问被授权的资源。RAM角色：RAM角色有确定的身份，可以被赋予一组权限策略，但没有确定的登录密码或访问密钥。RAM角色需要被一个可信的实体用户扮演，扮演成功后实体用户将获得RAM角色的安全令牌，使用这个安全令牌就能以角色身份访问被授权的资源。 |

## 安全性

### SAML2.0协议

方案中使用业界标准的SAML2.0协议保障数据安全传递，相关介绍详情[SAML 2.0](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)。

### 服务目录管理员权限

需要在主账号中分配操作角色（RAM）具备服务目录的管理权限。权限点：

| 权限策略名称 | 权限策略说明 |
| --- | --- |
| AliyunServiceCatalogAdminFullAccess | 管理服务目录(ServiceCatalog)的管理员侧权限 |

### 访问控制

在本方案中，通过以下方式保证流程安全：

- 在调用阿里云令牌服务（STS）提供的[AssumeRoleWithSAML](https://help.aliyun.com/zh/ram/api-assumerolewithsaml)接口时，设置不同的Policy参数实现细粒度授权。
- 在登录时，访问阿里云令牌服务（STS）以及登录服务获取一次性免密登录URL。

## 注意事项

### 地域（Region）限制

服务目录支持部署的地域和终端用户启动产品时支持部署实例的地域存在一定限制，具体可以查看[支持的地域](https://help.aliyun.com/zh/service-catalog/product-overview/supported-regions)。

### 产品使用限制

服务目录在产品使用上面存在一定限制，具体可以查看[使用限制](https://help.aliyun.com/zh/service-catalog/product-overview/limits)。

### 支持服务及资源

想了解服务目录具体支持的云服务和对应的云资源可以查看[服务目录支持的云服务](https://help.aliyun.com/zh/service-catalog/product-overview/services-and-resources-that-work-with-service-catalog)。

## 实施步骤

### 实施准备

1. 阿里云账号确保在阿里云官网已经开通服务目录。
2. 确保企业的办公网环境可以访问阿里云控制台。
3. 确保已经建立了阿里云与企业IdP之间的互信关系，具体配置步骤可以查看[SAML角色SSO概览](https://help.aliyun.com/zh/ram/overview-of-role-based-sso)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：4小时。

### 操作步骤

#### 1. 管理员在服务目录中创建产品并授权

在服务目录控制台登录有服务目录管理权限（AliyunServiceCatalogAdminFullAccess）的RAM角色，设置符合组织要求的产品并定义约束条件，并为当前登录角色授权。具体步骤可以查看[管理员创建产品并授权](https://help.aliyun.com/zh/document_detail/403733.html)。

#### 2. 管理员在企业CMP中配置元数据

1. 企业CMP需要保存服务目录中设置的产品信息和产品版本信息。
2. 企业CMP可以根据需要配置企业内部概念与服务目录产品信息、产品版本信息的映射关系，参考下图：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9586581571/p971600.png)

#### 3. 企业CMP获取免密登录URL并嵌入服务目录页面

操作流程如下图：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9586581571/p971613.png)

1. 用户登录企业CMP。
2. 调用阿里云令牌服务（STS）的[AssumeRoleWithSAML](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerolewithsaml)接口获取临时AK、SK和SecurityToken。
3. 通过临时AK、SK以及SecurityToken获取SignInToken。STS返回的SecurityToken中可能包含特殊字符，请将特殊字符进行URL编码后再输入。请求示例：`http://signin.aliyun.com/federation?Action=GetSigninToken
 &AccessKeyId=<STS返回的临时AK>
 &AccessKeySecret=<STS返回的临时Secret>
 &SecurityToken=<STS返回的安全Token>
 &TicketType=mini`
4. 通过SignInToken生成服务目录免密登录URL。链接示例：`String signInUrl = endpoint + String.format(
 "/federation?Action=Login"
 + "&LoginUrl=%s"
 + "&Destination=%s"
 + "&SigninToken=%s",
 URLEncoder.encode("https://www.aliyun.com", "utf-8"),
 URLEncoder.encode(preUrl, "utf-8"),
 URLEncoder.encode(signInToken, "utf-8"));`其中的LoginUrl可以为如下格式：`https://servicecatalog4service.console.aliyun.com/products/launch
 ?productId=<服务目录中的产品ID>
 &controlString=<Base64编码后的控制参数>`参数productId为必选参数，表示嵌入服务目录中指定产品的启动页面。参数controlString为可选参数，表示页面的控制参数，使用Base64编码。controlString说明如下：**参数****类型****是否必选****说明****示例**provisionedProductNamestring否产品实例名称的默认值。DEMO-创建ECS+VPCportfolioIdstring否启动选项的默认值。port-bp1mtazg2a****productVersionIdstring否产品版本的默认值。pv-bp1rnchc23****stackRegionIdstring否ROS资源栈所属地域的默认值。cn-hangzhouparametersJSON否预填的模板参数。{"zone_id":"cn-hangzhou-h","vpc_cidr_block":"172.**.*.*/12","vswitch_cidr_block":"172.**.*.*/21","ecs_instance_type":"ecs.s6-c1m1.small"}styleJOSN否控制页面的展示效果。- displayModestring否displayMode = cmp，会同时实现以下效果：隐藏侧边栏；将启动产品的按钮替换为创建计划的按钮。cmp- planButtonTextJOSN否允许用户自定义按钮的文案。{"zh-cn": "提交申请",
"en":"Apply"}controlString的完整示例：`{
 "style": {
 "displayMode": "cmp",
 "planButtonText": {
 "zh-cn": "提交申请"
 }
 },
 "provisionedProductName": "DEMO-创建ECS+VPC",
 "portfolioId": "port-bp1mtazg2a****",
 "productVersionId": "pv-bp1rnchc23****",
 "stackRegionId": "cn-hangzhou",
 "parameters": {
 "zone_id": "cn-hangzhou-h",
 "vpc_cidr_block": "172.**.*.*/12",
 "vswitch_cidr_block": "172.**.*.*/21",
 "ecs_instance_type": "ecs.s6-c1m1.small"
 }
}`
5. 企业CMP根据免密登录URL，使用iframe标签嵌入服务目录页面，前端代码示例如下：`var iframe = '<iframe class="embed-responsive-item" id="iframe_showPreConsole" src="' + nonLoginUrl + '"></iframe>';
$("#serviceCatalogViewConsoleDiv").html(iframe);`页面效果如图：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9586581571/p971602.png)

#### 4. 用户在嵌入的服务目录页面中填写模板参数

用户需要在嵌入的服务目录页面中填写模板参数，确认无误后点击“提交申请”按钮，服务目录会创建启动计划并自动开启预检。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9586581571/p971604.png)

#### 5. 企业CMP获取启动计划ID，发起工作流审批

服务目录通过postMessage的方式与企业CMP进行跨域通信，企业CMP需要设置监听器，监听服务目录页面返回的消息，获取启动计划ID。

```
window.addEventListener("message", function(event) {
  var data = JSON.parse(event.data);//服务目录子页面跨域传回来的参数
  var servicecatalogPlanId = data['PlanId']; //获取启动计划ID
  //进行查询等相关操作
}, false)
```

企业CMP可以调用服务目录[GetProvisionedProductPlan](https://help.aliyun.com/zh/service-catalog/developer-reference/api-servicecatalog-2021-09-01-getprovisionedproductplan)接口定时查询预检结果，当查询到预检通过后，可以发起企业CMP内部的工作流审批。

```
GetProvisionedProductPlanRequest request = new GetProvisionedProductPlanRequest();
request.setPlanId(servicecatalogPlanId());
GetProvisionedProductPlanResponse response = client.getProvisionedProductPlan(request);
if (response.getBody().getPlanDetail().status.equals("PreviewSuccess")) {
    //预检通过
    //开启审批
}
```

#### 6. 审批通过后企业CMP调用服务目录接口执行启动计划，创建产品实例

审批通过后企业CMP通过调用服务目录[ExecuteProvisionedProductPlan](https://help.aliyun.com/zh/service-catalog/developer-reference/api-servicecatalog-2021-09-01-executeprovisionedproductplan)接口执行启动计划创建产品实例，并获取产品实例ID，代码示例如下：

```
ExecuteProvisionedProductPlanRequest request = new ExecuteProvisionedProductPlanRequest();
request.setPlanId(planId);
ExecuteProvisionedProductPlanResponse response = client.executeProvisionedProductPlan(request);
String provisionedProductId = response.getBody().getPlanDetail().provisionedProductId;
```

通过调用[GetProvisionedProduct](https://help.aliyun.com/zh/service-catalog/developer-reference/api-servicecatalog-2021-09-01-getprovisionedproduct)接口和[GetTask](https://help.aliyun.com/zh/service-catalog/developer-reference/api-servicecatalog-2021-09-01-gettask)接口查询实例相关信息，用于在企业CMP展示，代码示例如下：

```
//调用GetProvisionedProduct接口
GetProvisionedProductRequest getProvisionedProductRequest = new GetProvisionedProductRequest();
getProvisionedProductRequest.setProvisionedProductId(provisionedProductId);
GetProvisionedProductResponse getProvisionedProductResponse = client.getProvisionedProduct(getProvisionedProductRequest);

//调用GetTask接口
String lastTaskId = getProvisionedProductResponse.getBody().getProvisionedProductDetail().getLastTaskId();
GetTaskRequest getTaskRequest = new GetTaskRequest();
getTaskRequest.setTaskId(taskId);
GetTaskResponse getTaskResponse = client.getTask(getTaskRequest);
```

## 故障排除

### 嵌入的服务目录页面无法正常打开

若无法正常打开服务目录页面，可能的原因如下：

1. 元数据中服务目录产品信息和产品版本信息配置错误。
2. 当前登录角色没有对应产品的权限。

需要回到实施步骤检查第一步、第二步是否正确实施。

### 实例创建失败原因排查

实例创建失败后排查思路如下。更多信息，请参见[实例创建失败怎么办](https://help.aliyun.com/zh/service-catalog/support/what-does-an-end-user-do-if-the-system-fails-to-create-a-product-instance)。

1. 启动角色没有ROS的权限。
2. 启动角色没有资源的权限。
3. 资源创建失败。
4. 超出实例数量的限制。

## 相关内容

- [服务目录产品简介](https://help.aliyun.com/product/358913.html)
- [服务目录API参考](https://help.aliyun.com/zh/service-catalog/developer-reference/api-reference/)
- [Terraform Language](https://www.terraform.io/language)
- [Terraform：Alibaba Cloud Provider](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-112（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
