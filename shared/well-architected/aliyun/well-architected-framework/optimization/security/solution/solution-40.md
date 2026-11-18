<!-- source: https://help.aliyun.com/zh/well-architected/solution-40 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929356 -->

# 多账号GoldenImage方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971098.png)

当企业开通资源目录，将已有阿里云账号邀请进来，或者通过新建成员账号的方式开展新的业务，那么不同账号之间都采用企业统一构建的基础镜像，是确保云上应用安全的一个有力手段。

本文档介绍了一种企业客户实现云上基础镜像的统一构建、共享和分发的方案，确保在多账号体系下，企业相关应用账号都能够使用安全合规的基础镜像。

## 方案优势

### 集中管理基础镜像

基础镜像构建在共享服务账号或者运维账号中进行，再基于该镜像进行共享和分发，确保所有账号都使用同一份镜像。避免在每个账号中单独构建造成的镜像内容不一致、难以维护等问题。

### 基于组织共享镜像

通过资源共享的共享单元，能够将基础镜像一键共享给整个资源目录或资源夹，新加入该资源目录或资源夹的账号会自动完成基础镜像的共享，降低操作成本，提升共享体验。

### 提升业务安全

通过管控策略和服务目录强制所有账号安全高效地使用基础镜像，能够避免业务应用使用不安全的镜像，造成安全合规风险。

## 客户场景

### 企业内部统一运维

#### 场景描述

企业内部需要统一维护基础镜像，确保相应应用都有一致的操作系统版本、系统配置、应用配置等基线。

#### 适用客户

- 使用资源目录管理云上多个账号的企业客户。
- 使用多个阿里云账号的企业客户。
- 存在中心运维团队、安全团队的企业客户。

## 客户案例

### 客户背景

某电力公司是亚太区规模最大的私营电力公司之一，业务遍及中国内地、香港、东南亚及台湾。

### 客户诉求

客户有中心化的运维团队，安全团队要求所有业务应用都需要使用运维团队统一构建的基础镜像。同时，客户在阿里云上采用了多账号架构，希望能够高效分发基础镜像到所有业务账号，并且确保业务账号只能使用运维团队构建的基础镜像。

### 实施方案

- 使用资源目录进行多账号统一管理。
- 使用系统运维管理服务构建基础镜像。
- 使用云服务器镜像服务跨地域复制镜像。
- 使用资源共享跨账号分发镜像。
- 使用资源目录管控策略确保业务账号只能使用基础镜像启动云服务器。

### 客户收益

- 一键快速更新镜像，提升构建效率。
- 使用共享单元分发基础镜像到指定资源目录下的所有成员账号，新加入的账号也能自动完成基础镜像的共享，提升运维效率。
- 实施管控策略确保业务账号只能使用基础镜像，满足安全团队的要求。

## 方案架构

本方案基于多账号体系实现企业 Golden Image 的构建和分发。镜像构建在共享服务账号内进行，您可以将已有的云下镜像导入到阿里云（图中1），当需要构建新的镜像时，您可以触发系统运维管理服务的自动化任务来进行（图中2），构建过程中，还可以接入镜像漏洞扫描（图中3）和人工审批流程（图中4），进一步保证镜像的安全合规。构建完成后，复制到企业业务所在的所有地域（图中5），然后配置服务目录产品组合（图中6），保证镜像的受控使用。通过资源共享的共享单元，将镜像和服务目录产品组合共享给企业内相应的业务成员账号（图中7）。业务成员账号可以通过服务目录的产品组合一键创建使用 Golden Image 的云服务器 ECS。最后通过下发管控策略（图中8），确保业务成员账号只能使用 Golden Image 创建 ECS。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971102.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 资源共享 | [资源共享（Resource Sharing）](https://help.aliyun.com/zh/resource-management/user-guide/resource-sharing-overview)是指多账号间通过共享的方式将一个账号下的指定资源共享给一个或多个目标账号使用。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 服务目录 | [服务目录（Service Catalog）](https://help.aliyun.com/zh/service-catalog/product-overview/what-is-service-catalog)基于阿里云IaC（基础设施即代码）能力，构建自定义的阿里云IT服务列表，并可设定约束条件符合组织治理要求，从而降低企业业务上云时选用产品的难度，提高IT服务交付效率。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/service-catalog/product-overview/pricing/)。 |
| 系统运维管理OOS | [系统管理与运维服务（CloudOps Orchestration Service, OOS）](https://help.aliyun.com/zh/oos/product-overview/introduction-to-oos)，是阿里云提供的云上自动化运维服务，能够自动化管理和执行任务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/oos/product-overview/billing-1/)。 |
| 云安全中心 | [云安全中心（Security Center）](https://help.aliyun.com/zh/security-center/what-is-security-center)是一款集持续监测、深度防御、全面分析、快速响应能力于一体的云上安全管理平台。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/security-center/billing/)。 |
| 对象存储OSS | [阿里云对象存储OSS（Object Storage Service）](https://help.aliyun.com/zh/oss/product-overview/what-is-oss)是一款海量、安全、低成本、高可靠的云存储服务 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/oss/product-overview/billing)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 共享服务账号 | 企业共享服务会部署在这个账号内，如网络的部署。推荐这个账号的费用由统一的某个团队来承担，比如基础设施团队。 |
| 共享单元 | 共享单元是资源共享的实例。共享单元包括：资源所有者、资源使用者和共享的资源。 |
| 服务目录产品 | 产品代表您希望在阿里云上部署的 IT 资源。底层是基于Terraform构成的云资源模板。根据Terraform的定义，可以是单个云资源，也可以是多个云资源的组合。 |
| 服务目录产品组合 | 产品组合由一个或多个产品构成，是管理产品的方式。管理员可以在产品组合上设置产品的约束和权限，以便终端用户启动产品并管理产品的实例。 |
| 镜像管理地域 | 构建镜像等管理操作所在的地域，其他地域通过镜像复制的方式进行分发。 |

## 安全性

通过使用管控策略（Control Policy），限制 Application 目录下的业务成员账号，均只能使用特定 ImageId 的 Golden Image 创建 ECS，确保操作系统基线安全。但有部分例外情况，请参考注意事项章节中管控策略限制一节。

镜像构建过程中，您可以接入镜像漏洞扫描（图中3）和人工审批流程（图中4），进一步保证镜像的安全合规。详情请参考自动化方案章节。

在共享镜像的过程中，云产品不会校验被共享者是否属于当前资源目录，请使用资源共享在资源目录的范围内进行资源分发，不要使用手动输入云账号 ID，避免错误输入导致镜像内容被他人获取。同时，构建 Golden Image 时，请确认自定义镜像已清除敏感数据和文件。

## 注意事项

### 共享镜像限制

对于云服务器镜像的跨账号共享，有以下限制：

- 每份自定义镜像最多可以共享给50个用户。
- 支持中国站、国际站和日本站账号之间共享镜像，但是基于镜像市场镜像创建的自定义镜像除外。

更多其他限制，请参见[共享或取消共享镜像](https://help.aliyun.com/zh/ecs/user-guide/share-a-custom-image/)。

### 管控策略工作原理

因管控策略的工作原理和特性，在实际使用过程中，会出现以下现象：

- 无法限制成员账号的 Root 身份。在成员账号中，管控策略能够限制成员账号的 RAM 用户和 RAM 角色，如果开启了成员账号的 Root 权限并使用 Root 身份创建 ECS，则不受管控策略限制。
- 管控策略对服务关联角色不生效。当云产品使用服务关联角色进行资源操作时，不受管控策略限制。

其他特性请参见[管控策略工作原理](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)。

### 云安全中心漏洞扫描限制

在自动化方案章节中，镜像构建时，会使用云安全中心手动进行漏洞扫描，云安全中心只有部分高级版本支持手动漏洞扫描，请您购买或升级到以下任意版本：高级版、企业版、旗舰版。

更多支持的漏洞类型和扫描限制，请参见[漏洞管理介绍](https://help.aliyun.com/zh/security-center/user-guide/overview-4)。

## 自动化模板

### 模板介绍

本方案提供了基于 Terraform 的自动化模版，模版代码结构如下所示。

```
├── golden-image-pipeline					// 通过 Terraform 部署 Golden Image 自动化 Pipeline。详细参考自动化 Pipeline 章节
└── golden-image-distribution			// 分发 Golden Image 的 Terraform 代码实现。共分为如下两个步骤
    ├── step1-copy-golden-image		// 复制镜像到其他地域
    └── step2-share-golden-image	// 通过资源共享的共享单元，共享镜像给其他账号、资源夹或者整个资源目录
```

### 模板地址

模板地址详情参见[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-golden-image)。

## 实施步骤

### 实施准备

- 确保已在「企业管理主账号」中开启了管控策略功能，请参考资源目录[开启管控策略功能](https://help.aliyun.com/zh/resource-management/user-guide/enable-the-control-policy-feature)。
- 确保已在「企业管理主账号」中开启了资源目录组织共享，请参考资源目录[启用资源目录组织共享](https://help.aliyun.com/zh/resource-management/user-guide/enable-resource-sharing)。
- 如果您需要将本地镜像导入到阿里云上：为保证自定义镜像的可用性和提高镜像的导入效率，请您在导入镜像前，仔细阅读[导入镜像必读](https://help.aliyun.com/zh/ecs/user-guide/instructions-for-importing-images/)。确保已在「共享服务账号」中开通了对象存储服务OSS。确保已在「共享服务账号」中[授予ECS对OSS资源的访问权限](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22ECS%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunECSImageImportDefaultRole%22%2C%22TemplateId%22%3A%22ECSImportRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunECSImageExportDefaultRole%22%2C%22TemplateId%22%3A%22ECSExportRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fecs.console.aliyun.com%2F%22%7D)。
- 在「共享服务账号」中选择一个地域作为 Golden Image 的管理地域，确保构建镜像的操作在管理地域进行，其他地域通过镜像复制的方式进行分发。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 导入本地镜像（可选）

1. 登入共享服务账号，进入 [OSS 控制台](https://oss.console.aliyun.com/overview)，在左侧导航栏选择 **Bucket 列表**。单击**创建 Bucket**，创建镜像文件的存储空间，请保证 Bucket 存储空间的地域和您的镜像管理地域相同。如果您已有合适的 Bucket 存储空间，也可以直接使用。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971101.png)
2. 上传镜像文件到 OSS Bucket 中。需要注意的是，超过 5GB 大小的文件，无法通过控制台进行上传，您需要通过命令行工具 [ossutil](https://help.aliyun.com/zh/oss/developer-reference/overview-59/)、[OSS SDK](https://help.aliyun.com/zh/oss/overview-21) 或 [OSS API](https://help.aliyun.com/zh/oss/developer-reference/description) 等方式，通过[分片上传](https://help.aliyun.com/zh/oss/user-guide/multipart-upload-12)的方式进行镜像上传。以命令行工具 ossutil 为例，如下所示，您可以通过 [cp](https://help.aliyun.com/zh/oss/developer-reference/upload-objects-6) 命令进行镜像上传。`./ossutil64 cp your-local-image.raw oss://yourbucketname`
3. 获取镜像文件 URL，进入 [OSS 控制台](https://oss.console.aliyun.com/overview)，在左侧导航栏选择 **Bucket 列表**。从 Bucket 列表中，选择存储镜像文件的 Bucket，单击该 Bucket，进入文件列表。选择第 2 步导入的镜像文件，单击**详情**。在详情中，复制镜像文件 URL。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971103.png)
4. 授予ECS对OSS资源的访问权限 [AliyunECSImageImportDefaultRole](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22ECS%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunECSImageImportDefaultRole%22%2C%22TemplateId%22%3A%22ECSImportRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunECSImageExportDefaultRole%22%2C%22TemplateId%22%3A%22ECSExportRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fecs.console.aliyun.com%2F%22%7D)。
5. 进入 [ECS 控制台](https://ecs.console.aliyun.com/home)，切换到镜像管理地域，在左侧导航栏选择 **实例与镜像**> **镜像**。单击**导入镜像**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971105.png)
6. 完成导入前准备，单击**下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971106.png)
7. 填写待导入的镜像的基本信息。其中**镜像文件 URL**，请填写在第 3 步获取的镜像文件URL。填写完成后，单击**确定导入**，完成镜像的导入。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971107.png)

#### 构建镜像

建议您使用系统运维管理 OOS 提供的自动化运维任务进行镜像的构建。具体步骤如下所示，该操作步骤中，并不包含方案架构图中的镜像漏洞扫描和镜像审批流程，如果您需要实现这些高级功能，请您参考**自动化方案**章节。

1. 登入共享服务账号，进入[系统运维管理 OOS 控制台](https://oos.console.aliyun.com/)，切换到镜像管理地域，在左侧导航栏选择**自动化任务**> **常用运维任务**>**创建或更新镜像**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971132.png)
2. 单击**创建**，开始配置创建或更新镜像的任务。您可以选择从已有 ECS 实例创建镜像或者更新一个已有镜像。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971109.png)
3. 填写任务配置。以更新镜像为例：新镜像名称：更新镜像会新创建一个镜像，这里需要填写新创建出来的镜像名称。新镜像名称不能和已有镜像的名称重复。选择镜像：选择需要更新的已有源镜像。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971108.png)
4. 配置中转实例：更新镜像时，会使用已有源镜像，创建一台临时中转的 ECS，然后从这台 ECS 上创建出新镜像，创建完镜像后，这台中转 ECS 会被删除。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971133.png)
5. 发送远程命令：该命令会在中转 ECS 实例中运行。您可以通过远程命令给镜像安装补丁、软件等。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971110.png)
6. 镜像分发：您可以在构建阶段直接进行新镜像的分发。建议您只进行镜像的跨地域复制，跨账号共享镜像请参考**分发镜像** > **共享镜像**章节。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971134.png)

#### 分发镜像

镜像的分发分为如下两步：

1. 跨地域复制镜像：将镜像批量复制到其它需要业务成员账号需要的地域
2. 跨账号共享镜像：通过资源共享将镜像共享给需要的业务成员账号

##### 跨地域复制镜像

1. 登入共享服务账号，进入 [ECS 控制台](https://ecs.console.aliyun.com/home)，切换到镜像管理地域，在左侧导航栏选择 **实例与镜像**> **镜像**。找到已经构建好的镜像或者导入新的镜像。本文以下图 golden_image_2021_06_07 这个镜像为例：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971111.png)
2. 单击**复制镜像**，将该镜像批量复制到其它需要业务成员账号需要的地域，这里以 cn-qingdao 和 cn-beijing 为例：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971135.png)
3. 收集所有需要共享的 Golden Image 的镜像ID，供后续配置管控策略使用。

##### 跨账号共享镜像

1. 登入共享服务账号，进入[资源管理控制台](https://resourcemanager.console.aliyun.com/)，在左侧导航栏选择 **资源共享**> **我的共享**。单击**创建共享单元**，开始共享单元的创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971112.png)
2. 按步骤配置共享单元。在第一步中填写共享单元名称（这里名称以 **golden_image** 为例）选择您需要共享的镜像资源。这里以 golden_image_2021_06_07 镜像为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971113.png)
3. 在第三步关联资源使用者中，您可以按照组织单元进行共享设置。使用者范围中选择**仅允许资源目录内共享**，资源使用者类型中，您可以选择将镜像共享给整个资源目录、单个成员账号或者资源夹。这里以 Applications 资源夹为例，填入资源夹 ID，单击**添加**。配置完成后，继续确认并提交，完成共享单元的创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971136.png)
4. 切换地域，重复上述操作，将其它地域的镜像依次共享给成员账号。

#### 查询多账号下镜像使用情况（可选）

您可以通过资源中心的高级搜索，查询当前资源目录中镜像的使用情况，比如：哪些 ECS 实例没有使用 Golden Image，方便企业管理账号持续追踪镜像的更新升级情况，推动镜像安全基线的继续落实。

1. 登入资源目录管理账号，进入[资源管理控制台](https://resourcemanager.console.aliyun.com/)，在左侧导航栏选择 **资源中心**> **跨账号资源搜索**。单击**开始使用**。开通跨账号资源搜索服务。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971114.png)
2. 在左侧导航栏选择 **资源中心**> **高级搜索**。更改查询范围为**跨账号**。选择您需要查询的成员账号、资源夹或者整个资源目录。这里以 Applications 资源夹为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971137.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971115.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971116.png)
3. 在临时查询填入查询语句，您可以参考并将以下代码复制到**临时查询**中，该代码用来查询所有没有使用目标镜像的 ECS 实例，注意将内容中的`${镜像ID}`替换为 Golden Image 的镜像ID。更多用法，请参考资源中心[高级搜索](https://help.aliyun.com/zh/resource-management/user-guide/advanced-search)。`SELECT
 resource_id,
 resource_name,
 region_id,
 zone_id,
 account_id,
 resource_group_id
FROM
 resources
WHERE
 resource_type = 'ACS::ECS::Instance'
 AND properties ->> 'ImageId' != '${镜像ID}';`
4. 如果有多个 Golden Image 需要查询，可以在查询条件中继续增加。`SELECT
 resource_id,
 resource_name,
 region_id,
 zone_id,
 account_id,
 resource_group_id
FROM
 resources
WHERE
 resource_type = 'ACS::ECS::Instance'
 AND properties ->> 'ImageId' not in ('${镜像1ID}', '${镜像2ID}');`
5. 单击**运行**，即可获取查询结果。单击**保存**，将临时查询保存为查询模版，方便您后续快速地运行查询。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971138.png)

#### 配置管控策略

1. 登入资源目录管理账号，打开[资源目录控制台](https://resourcemanager.console.aliyun.com/resource-directory)，进入**管控策略**页面，单击**创建策略**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971117.png)
2. 填入**策略名称**，并将以下代码复制到**策略JSON**中，注意将内容中的`${镜像ID}`替换为 Golden Image 的镜像ID：`{
 "Statement": [
 {
 "Action": [
 "ecs:RunInstances",
 "ecs:CreateInstance"
 ],
 "Effect": "Deny",
 "Resource": "acs:ecs:*:*:instance/*",
 "Condition": {
 "StringEquals": {
 "ecs:ImageSource": [
 "System",
 "Marketplace"
 ]
 }
 }
 },
 {
 "Action": [
 "ecs:RunInstances",
 "ecs:CreateInstance"
 ],
 "Effect": "Deny",
 "Resource": "acs:ecs:*:*:image/*",
 "Condition": {
 "StringNotLike": {
 "Resource": [
 "acs:ecs:*:*:image/${镜像ID}"
 ]
 }
 }
 }
 ],
 "Version": "1"
}`
3. 如果有多个 Golden Image 需要共享，可以在`Resource`中继续增加：`{
 "Statement": [
 {
 "Action": [
 "ecs:RunInstances",
 "ecs:CreateInstance"
 ],
 "Effect": "Deny",
 "Resource": "acs:ecs:*:*:instance/*",
 "Condition": {
 "StringEquals": {
 "ecs:ImageSource": [
 "System",
 "Marketplace"
 ]
 }
 }
 },
 {
 "Action": [
 "ecs:RunInstances",
 "ecs:CreateInstance"
 ],
 "Effect": "Deny",
 "Resource": "acs:ecs:*:*:image/*",
 "Condition": {
 "StringNotLike": {
 "Resource": [
 "acs:ecs:*:*:image/${镜像1的ID}",
 "acs:ecs:*:*:image/${镜像2的ID}",
 "acs:ecs:*:*:image/${镜像3的ID}"
 ]
 }
 }
 }
 ],
 "Version": "1"
}`
4. 单击**确定**，完成策略创建。
5. 单击**策略绑定**选项卡，在左侧选择需要绑定的资源夹（本示例中以“Applications”资源夹为例）后，单击**绑定策略**按钮，打开绑定策略对话框，选择刚才创建的 Golden Image 管控策略后，单击**确定**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971139.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971118.png)
6. 在弹出的确认绑定策略对话框中，单击**确认并继续**，完成绑定。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971119.png)

##### 验证管控策略

以 RAM 用户的身份登录成员账号，验证是否可以基于其他非指定镜像创建实例。如果管控策略没有问题，选择非 Golden Image 的镜像创建 ECS 实例时会出现创建失败，没有权限的提示。

注意：RD 管控策略对生效的资源账号以及云账号中的 RAM 用户和 RAM 角色均生效。

##### 云市场镜像注意事项

对于云市场的镜像，在管控策略中，无法通过具体的镜像 ID 进行限制，建议您基于云市场镜像构建新的自定义镜像作为 Golden Image，并对该镜像配置上述的管控策略。如果您需要直接使用云市场的镜像，并且希望能够进行强制的管控，建议您参考**基于服务目录高效可控地使用镜像**章节，通过服务目录对镜像使用进行管控。

#### 基于服务目录高效可控地使用镜像（可选）

服务目录（Service Catalog）基于阿里云IaC（基础设施即代码）能力，构建自定义的阿里云IT服务列表，并可设定约束条件符合组织治理要求，从而降低企业业务上云时选用产品的难度，提高IT服务交付效率。

您可以在共享服务账号中，创建服务目录产品，该产品用来创建 ECS 实例，然后创建包含该产品的产品组合，通过产品组合的模版约束，您可以限制使用该产品创建 ECS 实例时，只能选择相应的 Golden Image，然后您可以将产品组合共享给其他成员账号，成员账号可以使用该产品组合高效合规地创建出使用 Golden Image 的 ECS 实例，保证镜像高效可控地使用。以下是该流程的架构图。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971140.png)

##### 创建并分发产品组合

1. 登入资源目录管理账号，进入[资源目录控制台](https://resourcemanager.console.aliyun.com/resource-directory)，在左侧导航栏选择**资源目录**> **可信服务**。在可信服务列表中，找到服务目录产品，单击**管理**。在委派管理员一栏中，单击**添加**，选择共享服务账号，将共享服务账号指定为服务目录的委派管理员。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971120.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971141.png)
2. 登入共享服务账号，进入[服务目录控制台](https://servicecatalog.console.aliyun.com/)，在左侧导航栏选择**管理员**> **产品组合管理**。单击**创建产品组合**。在创建页面，填写名称（这里名称以 **golden_image** 为例）等基本信息，完成创建。这里您可以选择服务目录支持的任意地域，该地域并不影响终端用户启动产品部署资源的地域，您依然可以将资源部署到其支持的任意地域。
3. 进入产品组合详情页，单击**创建产品**。该产品用来创建云服务器 ECS，这里版本内容以**入门示例 > 云服务器 ECS** 为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971121.png)
4. 在产品组合详情页，切换到**约束**标签页，单击**创建约束**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971122.png)
5. 在创建约束页面，创建启动约束。选择启动使用的 RAM 角色，该 RAM 角色需要授信给服务目录，详情请参考[创建服务关联角色](https://help.aliyun.com/zh/ram/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service)。产品启动时，会扮演该 RAM 角色，完成产品中定义的资源实例的部署，请确保该 RAM 角色具有资源编排 ROS 管理权限以及需要部署的相应资源的管理权限。具体操作，请参考[创建启动约束](https://help.aliyun.com/zh/service-catalog/user-guide/create-a-launch-constraint)。这里以名为 **service-catalog-launch-role** 的 RAM 角色为例。该 RAM 角色被授予了**AliyunROSFullAccess** 和 **AliyunECSFullAccess** 系统权限策略。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971142.png)
6. 继续上述过程，约束条件选择**模版约束**。在约束设置中，单击**添加新规则**，在弹窗中，**参数**一项，选择 **image_id**，**参数值**一项，填入正则表达式`^镜像ID$`，注意将内容中的`镜像ID`替换为 Golden Image 的镜像ID。如果有多个 Golden Image 需要约束，那么可以在参数值正则表达式中使用`|`分隔：`^镜像1ID|镜像2ID$`。具体操作，请参考[创建模板约束](https://help.aliyun.com/zh/service-catalog/user-guide/create-a-template-constraint)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971124.png)
7. 参考**实施步骤** > **操作步骤** > **分发镜像** > **跨账号共享镜像**章节，通过共享单元将上述创建的产品组合共享给目标账号或资源夹。这里以**跨账号共享镜像**章节中创建的共享单元为例。进入**资源共享** > **我的共享**，找到该共享单元，进入共享单元详情，单击编辑**共享单元**。在编辑页面资源一栏，新增在步骤 1 中已经创建的服务目录产品组合。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971123.png)
8. 使用服务目录管理员身份（详情请参考[为管理员授权](https://help.aliyun.com/zh/service-catalog/user-guide/grant-permissions-to-the-administrator)），登入被共享的其他成员账号，进入[服务目录控制台](https://servicecatalog.console.aliyun.com/)，在左侧导航栏选择**管理员**> **产品组合管理**。选择**其他账号共享**标签页，找到在步骤 7 中共享的产品组合。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971143.png)
9. 进入该产品组合详情页，选择**授权**标签页，单击**添加授权关系**，选择允许使用该产品组合中产品的终端用户，终端用户可以为 RAM 用户或者 RAM 角色。请赋予该 RAM 用户或者 RAM 角色**AliyunServiceCatalogEndUserFullAccess** 的系统策略。单击**授权**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971125.png)
10. 进入 [RAM 访问控制控制台](https://ram.console.aliyun.com/)，创建和该产品组合启动约束中同名的 RAM 角色（本例中名称为 **service-catalog-launch-role**），该 RAM 角色需要授信给服务目录，详情请参考[创建服务关联角色](https://help.aliyun.com/zh/ram/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service)。同时您可以参考步骤 5 为该 RAM 角色授予相应资源的管理权限。

##### 配置管控策略

您可以通过资源目录下发管控策略，限制应用账号使用 RAM 身份登录后，无法直接创建 ECS 实例，只能通过服务目录来创建，进一步确保 Golden Image 的使用，同时提升资源的交付效率。操作方式请参考**安全可控地使用镜像** > **配置管控策略**章节，其中策略内容如下，注意将内容中的`${启动约束 RAM 角色名称}`替换为服务目录产品组合的启动约束中配置的 RAM 角色名称。在本例中，该 RAM 角色名称为 **service-catalog-launch-role**。

```
{
  "Version": "1",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "ecs:RunInstances",
        "ecs:CreateInstance"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotLike": {
          "acs:PrincipalARN": [
            "acs:ram:*:*:role/${启动约束 RAM 角色名称}"
          ]
        }
      }
    }
  ]
}
```

##### 使用产品组合部署 Golden Image

1. 使用服务目录终端用户身份（详情请参考[为终端用户授权](https://help.aliyun.com/zh/service-catalog/user-guide/grant-permissions-to-an-end-user)），登入被共享的其他成员账号，进入[服务目录控制台](https://servicecatalog.console.aliyun.com/)，在左侧导航栏选择**产品**。在产品列表中，可以看到产品组合中包含的所有产品。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971144.png)
2. 单击**启动产品**，填写参数并预览启动。由于在模版约束中，约束了 **image_id** 参数的选择范围，终端用户只能通过该产品，创建出使用 Golden Image 的 ECS 实例。

## 自动化 Pipeline

### 实施准备

- 共享服务账号
- 选择一个地域作为 Golden Image 的管理地域，确保构建镜像的操作在管理地域进行，其他地域通过镜像复制的方式进行分发。
- 云安全中心已经购买或升级到以下任意版本：高级版、企业版、旗舰版。
- 创建用于审批镜像构建流程的 RAM 用户，并确保该 RAM 用户至少拥有以下权限。您也可以直接授予该用户 **AliyunOOSFullAccess** 的系统权限。

### 操作步骤

#### 部署 Pipeline 环境

本方案提供了基于 Terraform 的自动化 Pipeline 的模版，您可以从[代码仓库](https://github.com/aliyun/alibabacloud-landing-zone/tree/master/solution/solution-golden-image/golden-image-pipeline)中下载模版，并使用共享服务账号的身份部署该 Terraform 模版，其模板参数如下。请确保您将该模版部署到了您选定的镜像管理地域。

| **参数名称** | **参数值示例** | **描述** |
| --- | --- | --- |
| imageFamily | GoldenImage | 配置新构建的 Golden Image 的镜像族系，用来聚合一组同一用途的 Golden Image。您可以在触发镜像构建的流程时修改该参数。 |
| imageOSAndVersion | CentOS-7.9 | Golden Image 的OS详情。建议格式为 OSName-OSVersion。您可以在触发镜像构建的流程时修改该参数。 |
| imageVersion | 1 | Golden Image 的版本号。每次更新 Golden Image 时，需要同时升级版本号。您可以在触发镜像构建的流程时修改该参数。 |
| cidrVpccidrVSwitch | 有效的 IPV4 网段，10.0.0.0/16 | 该自动化方案会自动创建 VPC、交换机和安全组，供镜像构建过程中创建中转的 ECS 实例使用。您可以在触发镜像构建的流程时选择其他已有的交换机和安全组。 |
| zoneId | cn-hangzhou-k | 新建的交换机所在的可用区。 |
| instanceType | ecs.c6.large | 镜像构建过程中创建的 ECS 实例的实例规格。您可以在触发镜像构建的流程时修改该参数。 |
| internetMaxBandwidthOut | 10 | 镜像构建过程中创建的 ECS 实例的公网带宽。为 0 时表示不分配公网地址。您可以在触发镜像构建的流程时修改该参数。 |
| approverRamUserName | approver | 允许审批镜像构建流程的 RAM 用户。该 RAM 用户至少需要具有下方所示的读写权限，您也可以直接授予其 AliyunOOSFullAccess 权限。该 RAM 用户可以批准/拒绝 Golden Image。您可以在触发镜像构建的流程时修改该参数。 |
| webHookUrl | 有效的 WebHook 链接 | 在镜像构建流程中开启镜像漏洞扫描或者需要人工审批时，会通过该 WebHook 发送消息通知。您可以在触发镜像构建的流程时修改该参数。 |

审批镜像构建流程的 RAM 用户 至少需要具有如下的读写权限：

```
{
  "Version": "1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "oos:GetExecutionTemplate",
        "oos:ListTaskExecutions",
        "oos:ListExecutions",
        "oos:NotifyExecution"
      ],
      "Resource": "*"
    }
  ]
}
```

#### 构建镜像

1. 登入共享服务账号，进入[系统运维管理 OOS 控制台](https://oos.console.aliyun.com/)，切换到镜像管理地域，在左侧导航栏选择**自动化任务**> **自定义任务模版**。
2. 在任务模版列表中，选择 **GoldenImageAutomation**，单击**创建执行**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971126.png)
3. 进入创建任务页面，开始配置参数。基础信息中，版本选择一栏，选择当前最新的模版版本基础信息中，执行模式一栏，保持当前默认选择：自动执行设置参数中，除了**源镜像ID**和**镜像版本**，其他参数都已经设置了默认值。您需要为一下参数指定适当的值。**参数****描述**源镜像ID（sourceImageId）您可以选择公共镜像、共享镜像、自定义镜像或者镜像市场作为源镜像。后续您可以通过云助手命令安装补丁或软件。请确保源镜像位于您的镜像管理地域中。镜像族系（imageFamily）配置新构建的 Golden Image 的镜像族系，用来聚合一组同一用途的 Golden Image。长度为2~128个英文或中文字符。必须以大小写字母或中文开头，不能以aliyun和acs:开头，不能包含http://或者https://。可以包含数字、半角冒号（:）、下划线（_）或者短划线（-）。镜像OS信息（imageOSAndVersion）Golden Image 的OS详情。建议格式为 OSName-OSVersion镜像版本（imageVersion）Golden Image 的版本号。每次更新 Golden Image 时，需要同时升级版本号。可用区（zoneId）实例类型（instanceType）安全组ID（securityGroupId）交换机ID（vSwitchId）公网带宽（internetMaxBandwidthOut）系统盘云盘种类（systemDiskCategory）实例的RAM角色（ramRoleName）用来配置中转 ECS 实例。该中转实例用于创建新镜像和漏洞扫描。在ECS实例中执行的云助手命令（commandContent）该自定义脚本会通过云助手在中转 ECS 实例执行，您可以通过该脚本给镜像安装补丁或软件等。审批人（approverUser）允许审批镜像构建流程的 RAM 用户。该 RAM 用户需要具有相应的读写权限，请参考**部署自动化环境章节**。您也可以直接授予其 AliyunOOSFullAccess 权限。该 RAM 用户可以批准/拒绝 Golden Image。WebHook地址（webHookUrl）在镜像构建流程中开启镜像漏洞扫描或者需要人工审批时，会通过该 WebHook 发送消息通知。需要@的指定用户（atMobiles）只支持钉钉机器人的 WebHook 通知。当群助手向钉钉群中发送审批通知时，要被@的群成员注册钉钉所用手机号。
4. 单击**下一步：确认**。确认无误后，单击**创建**。开始镜像构建的流程任务。

至此，您已成功触发 Golden Image 的构建任务，每次构建 Golden Image 时，请确保同一用途的 Golden Image，配置相同的**镜像族系（imageFamily）**和**镜像OS信息（imageOSAndVersion）**。

以下是整个镜像构建过程的架构图。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971127.png)

您可以通过多种方式触发构建镜像的流程。该过程可能需要大约 30 分钟左右。您可以手动触发或者在您的 CI-CD 中通过 API 触发。该自动化流程的工作原理如下。

1. 该流程使用源镜像创建中转 ECS 实例。通过云助手在中转实例中运行您的自定义脚本，安装补丁、软件等。然后停止该中转实例并基于该实例创建镜像。
2. 使用新构建的 Golden Image 创建漏洞扫描用的中转 ECS 实例。在该实例中安装云安全客户端，然后通过云安全中心对该 ECS 实例进行漏洞扫描并导出漏洞报告。
3. 漏洞扫描完成后，会将漏洞报告以及审批信息通过 WebHook 进行消息通知。以钉钉机器人为例，您会收到如下的一条消息通知。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4276581571/p971128.png)
4. 审批人接到通知后，可以批准/拒绝 Golden Image 构建流程。批准后，会为 Golden Image 打上标签，通过标签标记为有效的 Golden Image。

## 故障排除

### 为什么管控策略没有生效？

可能有如下原因：

- 管控策略中填写的镜像ID和 Golden Image 的镜像ID不匹配。
- 管控策略绑定的资源夹不正确。
- 没有使用 RAM 用户或 RAM 角色登入成员账号。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-40（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
