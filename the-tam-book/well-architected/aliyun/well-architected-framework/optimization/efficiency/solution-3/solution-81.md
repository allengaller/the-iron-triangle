<!-- source: https://help.aliyun.com/zh/well-architected/solution-81 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929279 -->

# 基于标签策略实现多账号标签合规

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6886581571/p970558.png)

本方案介绍了如何使用标签策略保障多账号场景下的标签合规，并为企业推荐一些常用合规标签。标签策略是用来帮助企业实施标签规范化的一种策略。通过标签策略，企业可以限定资源上必须绑定的合规标签，合规标签可以提升企业在标签分账、自动化运维等场景的管理效率。标签策略支持多账号模式，可以满足企业在多账号场景下对标签规范化管控的需求。

## 方案优势

### 提升不合规标签检测效率

资源创建后，可以通过标签策略监听资源变更情况，及时发现绑定了不合规标签的资源，包含以下两种情况：

- 资源绑定了标签，但是标签不规范。
- 资源未绑定指定标签。

### 提升不合规标签修复效率

基于标签自动检测的结果，如果设置的规则符合自动修复的条件，并开启了自动修复，则无需人工操作，标签策略会对不合规资源的标签进行自动修复。

## 客户场景

### 实现多账号标签合规管控

#### 场景描述

当企业在云上的资源越来越多时，企业可以通过标签对资源进行标记，实现资源分类、标签分账和自动化运维等。 但在给资源绑定标签的过程中，可能会遇到一些问题，例如创建资源后忘记绑定标签、只绑定了部分标签（如绑定了运维相关的标签，遗漏了财务相关的标签）、绑定的标签拼写错误等。这些问题会导致企业在标签分账时，出现不易划分财务归属的资源记录；企业在自动化运维时，出现不能自动化执行的资源。

#### 适用客户

- 使用标签进行分账、自动化运维的企业客户
- 对多账号资源标签合规有诉求的企业客户

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6886581571/p970551.png)

**关键流程说明**

1. 使用资源目录构建企业多账号体系。
2. 在企业管理账号中开启标签策略。
3. 新建标签策略，定义合规标签、定义不合规标签修复范围、开启不合规标签自动修复。
4. 将标签策略与资源目录中的资源夹或成员账号绑定。
5. 标签策略对绑定范围内成员账号的不合规标签进行自动检测及自动修复。

### 合规标签推荐

推荐的合规标签及说明如下：

| **标签类型** | **说明** | **标签键** |
| --- | --- | --- |
| 环境标签 | 一般用于描述资源所在的业务环境。常见组合有：开发环境、测试环境、生产环境等。 | Environment |
| 组织标签 | 一般用于描述资源的业务归属。常见组合有：公司、部门、团队、项目组等。 | CompanyDepartmentTeamProject |
| 角色标签 | 一般用于描述资源管理者角色。常见组合有：网络管理员、应用管理员、系统管理员等。 | Role |
| 成本标签 | 一般用于描述内部财务费用归属，主要用于内部结算或成本核算。常见组合有：部门、分公司、事业部等。 | BusinessUnit |
| 使用者标签 | 一般用于描述资源实际归属人，使用场景为：资源申请者和使用者不是同一人。常见组合有：人名、工号、邮箱等。 | Owner |
| **创建者标签** | 创建者标签是阿里云**自动生成并绑定**到对应资源的一种系统标签，用来标识资源的创建者。创建者标签支持阿里云主账号、RAM用户及角色，可以帮助企业分析费用和账单，有效管理企业云上成本，更多详情请参见[创建者标签概述](https://help.aliyun.com/zh/resource-management/tag/user-guide/overview-4)。 | acs:tag:createdby |

### 多账号架构

- 使用资源目录构建多账号架构，在企业管理主账号资源目录Root下构建Core及Applications资源夹，分别放置核心账号及业务账号便于管理。更多账号架构信息详情参见[企业级统一账号架构方案](https://help.aliyun.com/zh/caf/enterprise-multi-account-unified-architecture-solution)。
- 基础的合规标签策略可以绑定到高层资源夹（例如Applications资源夹），绑定后相应资源夹下所有成员账号都会生效。
- 可以在Applications资源夹下按业务线再细分资源夹，每个业务线有不同合规标签要求的可以新建不同标签策略，然后绑定到业务资源夹或指定成员账号，从而实现不同要求下的合规检测及自动修复。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录 | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 标签 | [标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview)是云资源的标识，可以帮助您从不同维度对具有相同特征的云资源进行分类、搜索和聚合，让资源管理变得更加轻松。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |

## 安全性

### 资源目录角色权限

资源目录服务关联角色（AliyunServiceRoleForResourceDirectory）为资源目录集成服务提供可信访问通道，详情参见[资源目录服务关联角色](https://help.aliyun.com/zh/resource-management/security-and-compliance/ram-roles-in-a-resource-directory)。

### 标签策略服务关联角色

标签服务通过服务关联角色（AliyunServiceRoleForTag）访问操作审计和配置审计中的操作记录和资源，进而实现资源变更的实时监听和资源配置的合规检测，从而实现标签合规的检测。更多详情参见[标签策略服务关联角色](https://help.aliyun.com/zh/document_detail/417449.html)。

## 注意事项

### 标签使用限制

- **支持的云服务**：阿里云标签服务已经支持一系列核心基础设施，例如：云服务器ECS、 云数据库RDS、对象存储OSS、专有网络VPC、负载均衡和容器服务Kubernetes版等。在此基础上，标签服务也在不断扩展对其他云服务的支持。更多信息，请参见[支持标签的云服务](https://help.aliyun.com/zh/resource-management/tag/product-overview/services-that-work-with-tag)。
- **使用限制**：标签使用限制详情参见[使用限制](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview)。

### 标签策略使用限制

- **支持的云服务**：支持标签策略的云服务详情参见[支持标签策略的云服务](https://help.aliyun.com/zh/resource-management/tag/user-guide/overview)。
- **使用限制**：标签策略使用限制详情参见[使用限制](https://help.aliyun.com/zh/resource-management/tag/user-guide/overview)。

### 资源目录使用限制

资源目录使用限制详情参见[使用限制](https://help.aliyun.com/zh/resource-management/product-overview/limits)。

## 实施步骤

### 实施准备

- **已构建多账号**：已在企业管理账号资源目录中完成多账号体系搭建。
- **确定合规标签**：企业需要确定合规标签，可参考本文章节**合规标签推荐**。本次操作步骤示例中合规标签为`company:子公司2`。
- **设置不合规标签**：已在资源目录成员账号中的资源上存在不合规标签。本方案已在成员账号创建一台ECS，并打上不合规标签`company:slave`。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6886581571/p970555.png)

### 操作步骤

根据安全最佳实践，推荐您为资源目录的管理账号创建一个RAM用户，并授予AdministratorAccess权限，充当资源目录的管理员（简称为RD管理员）。以下操作将使用RD管理员完成。关于创建RAM用户并授权的操作，请参见[创建RAM用户](https://help.aliyun.com/zh/ram/user-guide/create-a-ram-user)和[为RAM用户授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-the-ram-user)。

#### 启用标签策略

1. 使用企业管理账号登录[标签控制台](https://resourcemanager.console.aliyun.com/tags)。
2. 在左侧导航栏，选择**标签策略 > 策略库**。
3. 在**策略库**页面，单击**启用标签策略**。
4. 在**启用标签策略**对话框，单击**确定**。启用标签策略时，会自动创建一个服务关联角色（AliyunServiceRoleForTag）解决跨服务访问问题。更多信息，请参见[标签策略服务关联角色](https://help.aliyun.com/zh/document_detail/417449.html)。

#### 创建标签策略

您可以创建标签策略，通过配置策略内容，限定资源上必须绑定的标签，确保资源绑定合规的标签。

1. 在左侧导航栏，选择**标签策略 > 策略库**。
2. 在**策略库**页面的**策略列表**页签，单击**创建标签策略**。
3. 在**创建标签策略**页面，配置策略内容。输入策略名称。**可选：**输入策略描述。配置策略信息。以下两种配置方式，您可以任选其一：**快速录入**（推荐）您可以先指定标签键，然后为该标签键配置下表所示的规则，支持同时配置多个规则。单击**添加标签键**，可以继续添加标签键并配置规则。
4. 为此标签键指定允许值：支持通配符星号（*），表示允许任意标签值。
5. 强制执行：本示例不启用。强行制止不合规的标签行为，即如果标签操作不符合规范，操作将会失败。您需要指定强制执行的资源类型。支持强制执行的云服务和资源类型，请参见支持强制标签的云服务。具体示例，请参见使用标签策略实现强制标签。
6. 启用自动修复：对不合规资源的标签进行自动修复。您需要指定合规标签值和执行自动修复的资源范围。目前只支持通过标签指定资源范围。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6886581571/p970557.png)
7. 单击**创建**。

**说明** 强制标签功能目前处于邀测阶段，请先联系阿里云的服务经理，申请体验资格后才能进行试用。

#### 绑定标签策略

当您成功创建标签策略后，您还需要将标签策略绑定到目标账号，才能对目标账号中的资源进行标签规范化管控。

1. 在左侧导航栏，选择**标签策略 > 策略库**。
2. 在**策略库**页面，单击**策略列表**页签。
3. 单击目标标签策略**操作**列的**绑定**。
4. 在**绑定**对话框，选择绑定目标，本示例选择绑定子公司账号的父资源夹。然后单击**确定**。各绑定目标的生效范围如下：**说明** 标签策略不能绑定到资源目录的管理账号，即标签策略对管理账号不生效。Root资源夹：标签策略对整个资源目录中的全部成员生效。指定资源夹：标签策略仅对指定资源夹中的全部成员生效。指定成员：标签策略仅对指定成员生效。

#### 查看有效策略（可选）

标签策略绑定成功后，RD管理账号可以查看Root资源夹、资源夹和成员已绑定的有效策略，成员可以查看自己已绑定的有效策略。有效策略是根据标签策略继承关系计算得出的。更多信息，请参见[标签策略继承和有效策略计算](https://help.aliyun.com/zh/resource-management/tag/user-guide/inheritance-of-a-tag-policy-and-calculation-of-an-effective-policy)。

1. 在左侧导航栏，选择**标签策略 > 有效策略**。
2. 查看有效策略内容。默认使用可视化模式查看有效策略内容，您也可以单击**JSON格式查看**，查看JSON格式的有效策略内容。两种查看模式可以自由切换。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6886581571/p970561.png)

#### 查看检测结果

1. 登录[标签控制台](https://resourcemanager.console.aliyun.com/tags)。
2. 在左侧导航栏，选择**标签策略 > 检测结果**。
3. 在**检测结果**页面，查看不合规资源的检测结果。您可以单击**账号名称**，查看资源数量、不合规的资源数量、不合规资源占比和不合规资源列表等。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6886581571/p970562.png)
4. 在**不合规报告**区域，生成并下载不合规资源的检测报告。单击**生成新报告**。等待报告生成后，单击**下载已生成的报告**，下载Excel格式的不合规资源的检测报告。

#### 确认自动修复结果

登录子公司成员账号，在[ECS控制台](https://ecs.console.aliyun.com/server/region)查看标签修复结果，已从不合规标签`company:slave`，自动修复为合规标签`company:子公司2`。合规检测及自动修复存在一定生效延迟，生效时间详情参见[使用限制](https://help.aliyun.com/zh/resource-management/tag/user-guide/overview)。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6886581571/p970564.png)

## 故障排除

### 如何为存量资源高效地绑定标签？

对于未绑定标签或未划分资源组的存量资源，您可以采用以下方法高效地为多个资源批量绑定标签：

- 通过标签控制台为资源绑定标签。具体操作，请参见[创建并绑定标签](https://help.aliyun.com/zh/resource-management/add-a-custom-tag)。
- 通过标签编辑器为资源绑定标签。具体操作，请参见[管理标签](https://help.aliyun.com/zh/resource-management/manage-tags)。
- 通过标签API为资源绑定标签。具体操作，请参见[TagResources](https://help.aliyun.com/zh/resource-management/api-tagresources)。
- 通过运维编排服务为资源绑定标签。具体操作，请参见[使用运维编排服务批量绑定标签](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-add-tags-to-multiple-ecs-instances-at-a-time-1)。

### 如何批量修改已经绑定的标签值？修改后多久生效？

如果您想批量修改同一地域下多个资源同一标签的标签值，您可以采用以下方式：

- 通过运维编排服务修改标签值。具体操作，请参见[使用运维编排服务批量修改标签值](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-modify-a-tag-value-of-multiple-resources-1)。
- 通过标签编辑器修改标签值。具体操作，请参见[管理标签](https://help.aliyun.com/zh/resource-management/manage-tags)。
- 通过标签API修改标签值。具体操作，请参见[TagResources](https://help.aliyun.com/zh/resource-management/api-tagresources)。

## 相关内容

- [标签策略](https://help.aliyun.com/zh/resource-management/tag/user-guide/tag-policies/)
- [基于资源组和标签管理单账号云资源](https://help.aliyun.com/zh/well-architected/solution-13)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-81（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
