<!-- source: https://help.aliyun.com/zh/well-architected/solution-13 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929408 -->

# 基于资源组和标签管理单账号云资源

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971711.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971725.png)

在企业用云资源的过程中，如何规划单个云账号里面的资源归属。通过资源分类管理，能够降低企业运维管理云资源成本。

本方案会提供阿里云的两种资源标识方案：资源组和标签。结合企业自身业务场景可以选择符合企业特性的产品。

## 方案优势

### 企业进行更灵活地资源管理

通过使用标签，可以灵活进行资源管理。按不同的维度定义资源标签，基于标签维度可以适配到企业的自动化运维及分账场景。

### 企业支持资源分组管理

通过使用资源组，可以对一类资源进行归组管理。按不同分组，分配不同的权限。

## 客户场景

### 资源隔离场景

#### 场景描述

通过资源分组后，仅看到拥有权限的资源组，列出有权限的资源。

#### 适用范围

对资源组信息（名称）较敏感，解决资源可见性问题的场景。

用户可以基于现有系统按权限展示对应项目，让资源组与客户的业务建立相关性。

### 资源组监控告警场景

#### 场景描述

资源组的分组能应用到监控系统，保证用户仅看到有权限资源的监控信息。

#### 适用范围

告警配置使用资源组分组信息，配置效率高。

告警人员选择资源组人员，告警精准推送。

### 通过标签自动监控资源

#### 场景描述

对于大型企业或组织而言，可能需要维护成千上万条资源。即使对资源进行分组，也会有上千个组。人工维护耗时费力且易出错。云监控支持对资源绑定标签，并根据标签将资源分类管理，实现基于标签的自动化监控，降低您的资源监控成本。

#### 适用范围

基于标签的能力进行资源分类管理，实现基于标签的自动化监控。

### 标签分账场景

#### 场景描述

用户根据多维度进行分账。

#### 适用范围

资源管理和成本管理维度不一致；需要多种维度的分账视图。

## 方案架构

### 资源组隔离

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971713.png)

**注意事项**

- **不推荐使用默认资源组，推荐用户按照项目/部门等维度创建资源组进行使用。**
- RAM授权范围如果配置：账号级别。会导致返回全量资源组列表。
- 末接入资源组产品的资源组授权没有禁止。
- 支持资源组的云服务，详情查看[链接](https://help.aliyun.com/zh/resource-management/resource-group/product-overview/services-that-work-with-resource-group)。

### 资源组监控告警

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971714.png)

**注意事项**

- 资源组接入产品和云监控的应用分组功能有滞后性。

### 通过标签自动监控资源

云监控基于标签管理资源的限制如下：

- 目前只支持云服务器ECS（只支持实例，不支持网卡，磁盘等）、云数据库RDS和负载均衡SLB。
- 一个应用分组中每个产品最多只支持3000条资源，且资源加入分组的顺序是随机的。超出的资源不会加入分组。
- 创建应用分组约5分钟后，您可以查看分组级别的数据图表。
- 创建应用分组约5分钟后，系统自动按照报警规则上报告警。

### 标签分账场景

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971732.png)

**注意事项**

- 要注意标签接入度，是否满足企业当前使用的资源列表。
- 支持标签的云服务，详情参见[链接](https://help.aliyun.com/zh/resource-management/tag/product-overview/services-that-work-with-tag)。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源标签 | 标签是云资源的标识，可以帮助您从不同维度对具有相同特征的云资源进行分类、搜索和聚合，让资源管理变得更加轻松。 | 标签为免费产品，默认为开通状态，暂不支持关闭。标签提供的资源管理功能免费，参见[官网链接](https://help.aliyun.com/zh/resource-management/product-overview/billing-methods)。 |
| 资源组 | 资源组（Resource Group）是在阿里云账号下进行资源分组管理的一种机制。资源组帮助您解决单个云账号内多项目或多应用的资源分组，以及用户授权管理的复杂性问题。 | 资源组为免费产品，默认为开通状态，暂不支持关闭。资源组提供的资源管理功能免费，参见[官网链接](https://help.aliyun.com/zh/resource-management/product-overview/billing-methods)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 资源元数据中心服务 | 资源元数据是指资源的属性信息，常用的有资源名称、资源IP地址和资源标签等。资源元数据中心服务RMC（Resource Meta Center）提供了资源元数据信息的搜索功能，支持跨资源组、跨云服务和跨资源类型的资源搜索。 |
| 标签键值对 | 标签由一个键值对（Key:Value）组成，包含标签键（Key）、标签值（Value）。 |
| 自定义标签 | 自定义标签是由用户自己定义的标签。更多信息，请参见[创建并绑定自定义标签](https://help.aliyun.com/zh/resource-management/add-a-custom-tag)。 |
| 预置标签 | 预置标签是您预先创建并作用于所有地域的一种标签，非常适合在标签规划阶段使用。您可以在标签规划阶段创建预置标签，然后在标签实施阶段绑定具体的云资源。在预置标签中系统还预置了常见的标签类型，方便您快速规划标签体系。更多信息，请参见[创建预置标签](https://help.aliyun.com/zh/resource-management/tag/user-guide/create-a-tag)。 |
| 系统标签 | 系统标签是由系统自动生成的一种标签，只能查看，不能编辑。系统标签通常以一种相对标准化的形式呈现数据关系。在一些特定场景下，您可以借助系统标签来辅助处理业务。例如：集群关联的ECS会自动绑定集群ID的系统标签来标识归属。更多信息，请参见[查看系统标签及其绑定的资源](https://help.aliyun.com/zh/resource-management/tag/user-guide/view-system-tags-and-the-resources-to-which-a-system-tag-is-added)。 |

## 安全性

客户如果要给资源绑定标签，可以分配的权限系统策略：AliyunTagAdministratorAccess。

## 注意事项

### 资源组使用限制

| **限制项** | **最大值** | **提升配额方式** |
| --- | --- | --- |
| 资源组数量 | 30个 | [配额申请](https://quotas.console.aliyun.com/products/entconsole/quotas) |
| 资源组标识字符数 | 50个 | 无 |
| 资源组名称字符数 | 50个 | 无 |

支持资源组的云产品限制。请查看[列表](https://help.aliyun.com/zh/resource-management/resource-group/product-overview/services-that-work-with-resource-group)

### 标签使用限制

| **限制项** | **规格** |
| --- | --- |
| 单个资源最多允许绑定的标签数 | 20个 |
| 不同地域中的标签信息是否互通 | 否。例如：在华东1（杭州）地域创建的标签在华东2（上海）地域不可见。 |
| 标签键限制 | 标签键最多支持128个字符，不能以**aliyun**或**acs:**开头，也不能包含**http://**或**https://**。 |
| 标签值限制 | 标签值最多支持128个字符，不能以**aliyun**或**acs:**开头，也不能包含**http://**或**https://**。 |
| 资源绑定限制 | 同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。例如：某资源先绑定了**city:shanghai**，后续如果绑定**city:newyork**，则**city:shanghai**自动被解绑。 |

支持标签的云产品限制，详情参见[列表](https://help.aliyun.com/zh/resource-management/tag/product-overview/services-that-work-with-tag)。

## 实施步骤

### 实施准备

- 如果当前账号是主账号，那直接就可以操作。
- 如果当前是RAM子用户，那需要有对资源组及标签管理的权限。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：90分钟。

### 场景一：资源组隔离

#### 管理资源组

1. 登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源组**。
3. 单击**创建资源组**。
4. 填写**资源组标识**和**资源组名称**。
5. 单击**确定**。

#### 添加RAM身份并授权

**注意：**

- 访问控制授权后，权限对云账号下所有资源生效。资源组内授权后，权限仅对当前资源组内所有资源生效。

操作步骤

1. 登录[资源管理控制台](https://resourcemanager.console.aliyun.com/)。
2. 在左侧导航栏，单击**资源组**。
3. 在**操作**列表下，单击**权限管理**。
4. 单击**新增授权**。
5. 选择**被授权主体**。
6. 选择需要授予的权限策略。
7. 单击**确定**，完成授权。

完成授权后，被授权的主体将获得当前资源组内资源的相应权限。

### 场景二：资源组监控告警场景

#### 前提条件

**需要在RAM中给云监控授权SLR。**

操作指引：RAM访问控制 -> 身份管理 -> 角色->创建角色（阿里云服务）-> 选择“云监控”

#### 操作步骤

云监控中通过资源组创建应用分组步骤：

1. 登录[云监控控制台](https://cloudmonitor.console.aliyun.com/)。
2. 在左侧导航栏，单击**应用分组**。
3. 在**应用分组**页签，单击右上角的**创建组**。
4. 在**创建应用分组**面板，选择**创建方式**为**资源组创建**，并设置相关参数。**参数****说明****基本信息**设置资源组和报警联系人组。取值：**资源组创建**：从资源管理控制台选择资源组。**联系人组**：用于接收报警通知的联系人组。您可以选择已有报警联系人组，也可以快速创建。**初始化安装监控插件**您开启**初始化安装监控插件**后，云监控自动对应用分组中的主机安装云监控插件，以便采集主机的监控数据。**事件监控**您选中**订阅事件通知**后，当应用分组内相关资源产生严重和警告级别事件时，云监控自动给您发送报警通知。
5. 单击**添加**。
6. 在**应用分组**页签的搜索区域，从下拉列表中选择**资源组**，查看创建的应用分组。

### 场景三：通过标签自动监控资源

#### 前提条件

需要在RAM中给云监控授权slr。

操作步骤：RAM访问控制 -> 身份管理 -> 角色->创建角色（阿里云服务）-> 选择“云监控”

#### 操作步骤

##### 方式一：资源绑定固定标签

阿里云的不同产品上创建资源时，如果确认该资源需要通过云监控控制台进行管理，则需要在该资源上绑定标签：**cloudmonitor-group**。针对该标签，云监控都会自动创建一个应用分组。在分组中，您可以查看资源监控图表，并对资源进行管理。

操作步骤：

1. 在阿里云产品上创建资源时，绑定标签：cloudmonitor-group。
2. 云监控根据标签在云监控控制台上**自动创建一个应用分组**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971715.png)

**说明** 对于自动创建的应用分组，**联系人组**默认是**云账号报警联系人**，监控模板默认是**常用基础模板**。您可以根据实际业务需求手动修改。

##### 方式二：在云监控控制台上指定标签

如果您在阿里云的不同产品上创建资源且绑定了非cloudmonitor-group的标签时，可以在云监控控制台上通过**手动创建应用分组**来指定标签，对该标签下的资源进行定制化管理。

1. 登录[云监控控制台](http://cloudmonitor.console.aliyun.com/)。
2. 创建应用分组指定标签。**说明** 创建应用分组完成后，请您稍等2分钟再查看生成的应用分组。在左侧导航栏选择**应用分组**。在**应用分组**页面，单击**创建组**。在**创建应用分组**页面，配置**创建方式**、**基本信息**、**监控报警**、**区域**、**匹配规则**和**事件监控**。创建应用分组时，参数配置说明如下：**创建方式**选择**智能标签同步创建**，系统自动生成**应用分组名称**。**联系人组**默认是**云账号报警联系人**，您可以根据实际业务需求自定义。监控报警模板默认是**常用基础模板**，您可以根据实际业务需求自定义。您可以根据实际业务需求配置**资源标签键**和**资源标签值**。启用**初始化安装监控插件**，系统会对本应用分组的服务器批量安装监控插件，默认处于启用状态。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971734.png)单击**添加**。通过**资源标签**过滤出指定的标签值。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971716.png)

### 场景四：标签分账场景

模拟案例场景描述：

有一家企业有一个账号UID，有4个部门，需要清楚知道这4个部门分别对应的账单。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971736.png)

#### (一) 规划标签体系

本案例中会涉及到以下标签：

- department: 标识不同的部门，如业务部/市场部/运维部。

#### (二) 建立标签关系

1. 通过控制台打标签我们这个案例中只考虑一种云资源：ECS。其他云资源参考相应的帮助文档。可能的标签值对如下：department: biz / martket / dev / ops。登录ECS控制台打标签![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971717.png)在ECS的控制台中可以找到添加标签入口，完成标签的定义与关联指定的云资源。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971718.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971738.png)
2. 通过api打标签参考TagResources，UntagResources 这两个api的使用。

#### (三) 配置分账场景

**3.1 分账账单控制台**

1. 开通费用中心 -> 费用分析 功能，这个功能可在T+1后根据标签进行分账。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971719.png)可以通过各种条件进行过滤筛选来做费用分析。比如按产品、产品明细、财务单元、标签等。
2. 进入分账账单，查看费用明细。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971720.png)

**注意：账单明细数据延迟两天更新。**

**3.2 通过API导出分账账单**

有些企业有内部系统想做费用分析，可以集成费用信息的OpenAPI来完成分账和对账处理。

**3.3 通过财务单元导出分账账单**

通过财务单元与标签映射的方式进行分账，资源按照标签分组管理后，通过创建对应的财务单元，将标签对应到财务单元实现按财务单元汇总账单。

典型的场景：比如某个公司多个项目在使用云资源，财务希望按照项目进行出账，以解决财务成本分摊的问题。

那就可以给不同的项目定义不同的财务单元。

**3.3.1 创建财务单元**

1. 企业财务 -> 财务单元 -> 新增财务单元![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971721.png)可以将4个部门的财务单元创建出来![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971722.png)

**3.3.2 关联资源到财务单元**

1. 查看末分配，按照标签进行资源筛选。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971723.png)
2. 单击market，按照标签设置自动分配资源规则。**注意：**自动分配资源规则，只对末分配的资源，可以按照配置的规则，自动分配到当前财务单元。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971724.png)注意：资源自动分配到财务单元，一般是在次日生效。

**3.3.3 按财务单元查看账单**

1. 费用账单 -> 费用账单，可根据财务单元进行账单查看![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971726.png)

#### (四) 持续优化改进

**4.1 通过Config进行标签配置审计**

1. 登录配置审计控制台。[链接](https://config.console.aliyun.com/rules/-)
2. 在规则 -> 新建规则 -> 选择内置的一条规则模板（满足多标签值的一种枚举）![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971739.png)
3. 选择要监控的资源类型。本案例中请选择ECS。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4886581571/p971727.png)
4. 输入对应的键值对，单元确定配置完之后，就可以发现有多少资源不符合标签规范了。

## 故障排除

### 如何为存量资源高效地绑定标签？

对于未绑定标签或未划分资源组的存量资源，您可以采用以下方法高效地为多个资源批量绑定标签：

- 通过标签控制台为资源绑定标签。具体操作，请参见[创建并绑定标签](https://help.aliyun.com/zh/resource-management/add-a-custom-tag)。
- 通过标签编辑器为资源绑定标签。具体操作，请参见[管理标签](https://help.aliyun.com/zh/resource-management/manage-tags)。
- 通过标签API为资源绑定标签。具体操作，请参见[TagResources](https://help.aliyun.com/zh/resource-management/api-tagresources)。
- 通过运维编排服务为资源绑定标签。具体操作，请参见[使用运维编排服务批量绑定标签](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-add-tags-to-multiple-ecs-instances-at-a-time-1)。

### 如何查看分账账单？

您可以在[用户中心](https://usercenter2.aliyun.com/home)查看分账账单。更多信息，请参见：

- [分账账单查看方式](https://help.aliyun.com/zh/resource-management/tag/use-cases/methods-to-view-split-bills)
- [查看和导出实例型云服务的分账账单](https://help.aliyun.com/zh/resource-management/tag/use-cases/view-and-export-the-split-bills-of-instance-based-services)
- [查看和导出分拆型云服务的分账账单](https://help.aliyun.com/zh/resource-management/tag/use-cases/view-and-export-the-split-bills-of-shared-services)
- [查看和导出集群型云服务的分账账单](https://help.aliyun.com/zh/resource-management/tag/use-cases/view-and-export-the-split-bills-of-cluster-based-services)

### 如何为不支持标签的云服务分账？

对于不支持标签的云服务，您可以考虑采用以下方式进行分账：

- 对于支持资源组的云服务，您可以采用资源组进行分账。具体操作，请参见[资源组分账](https://help.aliyun.com/zh/resource-management/resource-group/use-cases/view-billing-statements-by-resource-group)。
- 对于费用归属一致的云服务，您可以在[财务单元](https://usercenter2.aliyun.com/finance/finance-unit/list)设置分配资源规则，在分账账单中根据财务单元分账。
- 对于其他情况，您可以在[费用账单](https://usercenter2.aliyun.com/finance/expense-report/expense-detail-by-instance)的**账单明细**中导出账单到本地电脑，在Excel中手工按账号、产品等维度进行简单的分账。

### 如何批量修改已经绑定的标签值？修改后多久生效？

如果您想批量修改同一地域下多个资源同一标签的标签值，您可以采用以下方式：

- 通过运维编排服务修改标签值。具体操作，请参见[使用运维编排服务批量修改标签值](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-modify-a-tag-value-of-multiple-resources-1)。
- 通过标签编辑器修改标签值。具体操作，请参见[管理标签](https://help.aliyun.com/zh/resource-management/manage-tags)。
- 通过标签API修改标签值。具体操作，请参见[TagResources](https://help.aliyun.com/zh/resource-management/api-tagresources)。

标签修改后将立即生效。

### 财务单元的自动分配规则是否对存量资源生效？

是。当您在财务单元创建了按标签自动分配财务单元的规则后，所有绑定了该标签的资源都会自动分配到对应的财务单元，即不区分存量资源或新创建的资源。

## 相关内容

- [云监控配置](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/create-an-application-group)
- [资源管理](https://help.aliyun.com/zh/resource-management/product-overview/what-is-resource-management)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-13（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
