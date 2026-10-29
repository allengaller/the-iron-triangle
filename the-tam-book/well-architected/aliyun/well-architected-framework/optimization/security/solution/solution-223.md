<!-- source: https://help.aliyun.com/zh/well-architected/solution-223 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929335 -->

# 通过SMC实现主机操作系统迁移升级

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970775.png)

操作系统因生命周期、第三方支持、开源计划演进等原因将会停止技术支持，例如 CentOS 官方将停止维护 CentOS 7/CentOS 8 等 Linux 项目，微软目前也已停止对 Windows Server 2008 R2 等操作系统提供技术支持。这些进入到停止维护周期（EOL）的操作系统版本将面临更大的安全漏洞威胁，出于安全或业务需求的考虑，企业需要将操作系统迁移升级到更高的版本。

本文档介绍了一种企业客户实现云上主机操作系统迁移升级的方案，满足多账号体系下，操作系统版本持续审计合规的需求。

## 方案优势

### 使用服务器迁移中心实现操作系统平滑迁移

服务器迁移中心（SMC）支持白屏化操作，您可以实时看到迁移进度。同时迁移前，SMC 会自动为实例创建快照，无需手动进行。使用 SMC 迁移后，系统盘原有数据依然保留，您无需担心数据丢失。

### 全局资源视图和资源搜索能力

通过资源中心，您可以查看资源目录内所有成员下不同产品、不同地域的全局资源列表。同时使用资源中心高级搜索的功能，您可以实时查询当前企业所有业务账号下的所有 ECS 实例的操作系统版本，让企业运维和安全团队，对云上实例使用的操作系统的全貌了然于心。

### 提升业务安全合规

基于配置审计，持续审计和保证主机实例镜像版本的合规情况，及时发现并处置使用过时操作系统版本的 ECS 实例，确保所有业务的 ECS 实例符合企业整体操作系统版本的要求，避免业务应用未及时升级操作系统版本，造成安全合规风险。

## 客户场景

### 企业统一运维与安全合规要求

#### 场景描述

企业内部需要统一运维 ECS 实例操作系统版本，确保所有实例都有一致的操作系统版本，并能够持续审计所有主机实例的操作系统版本，对于不合规的主机实例，能够平滑迁移升级。

#### 适用客户

- 使用 ECS 主机实例的企业客户。
- 存在中心运维团队、审计团队的企业客户。
- 有独立合规团队的企业客户。

## 方案架构

本方案通过服务器迁移中心（SMC）和系统运维管理（OOS）实现 ECS 实例操作系统的迁移升级。企业管理账号通过资源中心可以实时查询当前企业所有业务账号下的所有 ECS 实例的操作系统版本，让企业运维和安全团队，对云上实例使用的操作系统的全貌了然于心（图中1）。通过配置审计，持续审计业务账号中所有 ECS 实例操作系统的合规情况（图中2），您还可以将审计结果通过事件总线进行通知或者通过日志服务集成到监控系统中。当需要对操作系统进行迁移升级时，企业运维团队，可以通过 SMC 对实例操作系统进行平滑迁移（图中3），对于 SMC 不支持的操作系统类型和版本，您还可以使用 OOS 的运维任务，通过更换系统盘的方式进行迁移（图中4）。迁移过程会涉及 ECS 实例的停机重启，因此，为保证业务的稳定性和可用性，您的业务应用需要支持滚动升级。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970777.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 配置审计Config | [配置审计（Cloud Config）](https://help.aliyun.com/zh/document_detail/127388.html)是一项面向资源的审计服务。在面对大量资源时，配置审计可以帮助您实现持续的基础设施的合规监管。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/document_detail/133949.html)。 |
| 资源中心 | [资源中心](https://help.aliyun.com/zh/resource-management/user-guide/overview-3)为您提供跨账号、跨产品、跨地域的资源统一视图及资源搜索能力。 | 免费 |
| 服务器迁移中心SMC | [服务器迁移中心（Server Migration Center，简称SMC）](https://help.aliyun.com/zh/smc/product-overview/what-is-smc)是阿里云提供给您的迁移平台。专注于提供能力普惠、体验一致、效率至上的迁移服务，满足您在阿里云的迁移需求。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/smc/product-overview/pricing)。 |
| 系统运维管理OOS | [系统管理与运维服务（CloudOps Orchestration Service, OOS）](https://help.aliyun.com/zh/oos/product-overview/introduction-to-oos)，是阿里云提供的云上自动化运维服务，能够自动化管理和执行任务。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/oos/product-overview/billing-1/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 日志账号 | 一般在资源目录的Core资源夹中建议存在一个日志审计账号，专门用于存储云上收集的各种日志，并且仅有审计管理员使用的角色拥有对该日志账号的管控权限，实现运维管控权限和审计监管权限的隔离，避免出现恶意运维之后又能删除审计日志逃避司法追责的情况。该账号仅承担审计日志收集、留存和分析的职能，账号下不保有其他计算和数据库资源，与业务账号独立。 |

## 安全性

### 配置审计服务关联角色

为了完成配置审计的功能，需要获取其他云服务的访问权限而提供的RAM角色，详情参见[配置审计服务关联角色](https://help.aliyun.com/zh/document_detail/162994.html)。

### 资源中心服务关联角色

资源中心通过服务关联角色（AliyunServiceRoleForResourceMetaCenter）访问其他云服务中的资源，实现全局资源视图和资源搜索。关于服务关联角色的更多信息，请参见[服务关联角色](https://help.aliyun.com/zh/resource-management/user-guide/service-linked-role-for-resource-center)。

### 服务器迁移中心服务关联角色

服务关联角色（AliyunServiceRoleForSMC）具有查询管理ECS实例的权限，允许服务器迁移中心操作您ECS和VPC中的资源，以完成服务器迁移中心相关功能。关于服务关联角色的更多信息，请参见[服务关联角色](https://help.aliyun.com/zh/smc/developer-reference/service-linked-roles-for-smc)。

### 服务器迁移中心安全性

服务器迁移中心默认采用 SSL 2048 位 RSA 密钥加密传输通道，支持通过VPN网关、高速通道物理专线等私网迁移。详情参见[产品优势](https://help.aliyun.com/zh/smc/product-overview/benefits)。

## 注意事项

### 配置审计使用限制

在配置审计中，一个账号允许新建的规则数目最大为 200 条。更多其他限制，请参见[配置审计使用限制](https://help.aliyun.com/zh/document_detail/183384.html)。

### 服务器迁移中心使用限制

服务器迁移中心迁移操作系统时，针对不同类型的操作系统，对源操作系统存在限制：

- Linux操作系统架构源操作系统目标操作系统X86CentOS 7AnolisOS 7AnolisOS 8Alibaba Cloud Linux 2Alibaba Cloud Linux 3CentOS 8AnolisOS 8Alibaba Cloud Linux 3RedHat 7（仅支持RedHat 7.9）RedHat 8Alibaba Cloud Linux 3Alibaba Cloud Linux 2Alibaba Cloud Linux 3ARM64CentOS 7AnolisOS 7AnolisOS 8Alibaba Cloud Linux 3CentOS 8AnolisOS 8Alibaba Cloud Linux 3
- Windows操作系统架构源操作系统目标操作系统X86Windows Server 2008 R2 标准版 64位中文版Windows Server 2008 R2 企业版 64位中文版Windows Server 2012 R2 数据中心版 64位中文版（仅支持升级到相同语言的版本）Windows Server 2008 R2 标准版 64位英文版Windows Server 2008 R2 企业版 64位英文版Windows Server 2012 R2 数据中心版 64位英文版（仅支持升级到相同语言的版本）Windows Server 2012 标准版 64位中文版/英文版Windows Server 2012 R2 数据中心版 64位中文版/英文版Windows Server 2016数据中心版 64位中文版/英文版（仅支持升级到相同语言的版本）

更多其他限制，请参见：

- [服务器迁移中心使用限制](https://help.aliyun.com/zh/smc/product-overview/limits)
- [Linux操作系统迁移限制](https://help.aliyun.com/zh/smc/use-cases/migrate-an-operating-system#6f04d076bdgp4)
- [Windows操作系统迁移限制](https://help.aliyun.com/zh/smc/use-cases/windows-operating-system-migration#5a6916f0847f4)

### 业务应用架构要求

在 ECS 实例操作系统迁移升级过程中，会对 ECS 实例进行停机重启的操作，为保证业务的稳定性和可用性，避免出现迁移过程中业务不可用的情况，请确保您的业务应用支持滚动发布升级。同时，在规划迁移计划时，请严格分批进行，一批迁移完成并验证确认无误后，再进行下一批实例的迁移工作。

## 实施步骤

### 实施准备

- 确保已在「企业管理主账号」中开启了资源中心和跨账号资源搜索，请参考[开通资源中心](https://help.aliyun.com/zh/resource-management/user-guide/activate-resource-center)和[开通跨账号资源搜索](https://help.aliyun.com/zh/resource-management/user-guide/enable-cross-account-resource-search)。
- 确保已在「日志账号」中开启了配置审计服务，请参考[开通配置审计服务](https://help.aliyun.com/zh/document_detail/2399579.html)。
- 确保已在「业务账号」中开通了快照服务，请参考[开通快照](https://help.aliyun.com/zh/ecs/user-guide/activate-ecs-snapshot)。
- 确保已在「业务账号」中创建了 SMC 服务关联角色，完成相关授权操作，请参考 [SMC 迁移准备工作](https://help.aliyun.com/zh/smc/user-guide/before-you-begin)。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。具体时长和您需要迁移升级的 ECS 主机实例数量有关。

### 操作步骤

#### 查询多账号下实例操作系统版本（可选）

您可以通过资源中心的高级搜索，查询当前资源目录中所有实例操作系统版本的使用情况，比如：哪些 ECS 实例使用了已经停止支持的操作系统版本，方便企业管理账号持续追踪操作系统迁移升级情况，推动操作系统安全合规的持续落实。

1. 登入企业管理主账号，进入[资源管理控制台](https://resourcemanager.console.aliyun.com/)，在左侧导航栏选择 **资源中心**> **跨账号资源搜索**。单击**开始使用**。开通跨账号资源搜索服务。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970778.png)
2. 在左侧导航栏选择 **资源中心**> **高级搜索**。更改查询范围为**跨账号**。选择您需要查询的成员账号、资源夹或者整个资源目录。这里以 Applications 资源夹为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970776.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970780.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970781.png)
3. 在临时查询填入查询语句，您可以参考并将以下代码复制到**临时查询**中，该代码用来查询所有使用了指定操作系统版本的 ECS 实例，注意将内容中的`${操作系统版本}`替换为具体的操作系统版本。更多用法，请参考资源中心[高级搜索](https://help.aliyun.com/zh/resource-management/user-guide/advanced-search)。`SELECT
 resource_id,
 resource_name,
 region_id,
 zone_id,
 account_id,
 Properties ->> 'OSName' as OSName,
 Properties ->> 'OSNameEn' as OSNameEn
FROM
 resources
WHERE
 resource_type = 'ACS::ECS::Instance' 
 AND Properties ->> 'OSName' LIKE '${操作系统版本}'`
4. 单击**运行**，即可获取查询结果。单击**保存**，将临时查询保存为查询模板，方便您后续快速地运行查询。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970779.png)

#### 持续合规审计（可选）

您可以通过配置审计，持续审计主机实例镜像版本的合规情况，及时发现并处置使用过时操作系统版本的 ECS 实例，确保所有业务的 ECS 实例符合企业整体操作系统版本的要求，避免业务应用未及时升级操作系统版本，造成安全合规风险。

1. 登入企业管理主账号，进入[资源管理控制台](https://resourcemanager.console.aliyun.com/)，在左侧导航栏选择 **资源目录**> **可信服务**。选择配置审计，单击**管理**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970783.png)
2. 在**委派管理员账号**中，单击**添加**，将日志账号委派为配置审计服务的管理员。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970786.png)
3. 登入日志账号，进入[配置审计控制台](https://config.console.aliyun.com/)，在左侧导航栏选择**账号组**。单击**创建账号组**，通过账号组，对资源目录中的成员账号进行集中合规管理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970784.png)
4. 创建账号组时，账号组类型，可以选择**全局**。全局账号组包含的成员将自动与资源目录保持一致。全局账号组会自动感知资源目录中成员的新增，并自动同步加入到该全局账号组中，确保合规管理的账号范围始终与资源目录保持一致。需要注意的是，您只能新建一个全局账号组。这里我们创建一个名为 ResourceDirectory 的全局账号组，以此为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970785.png)
5. 在左侧导航栏切换到需要合规管控的账号组中，这里以上一步创建的名为 ResourceDirectory 的账号组为例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970787.png)
6. 在左侧导航栏选择**合规审计** > **规则**，单击**新建规则**。选择名为**ECS实例使用指定版本的操作系统**的规则。单击**下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970788.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970791.png)
7. 在**参数设置**中，可以对操作系统版本进行白名单或者黑名单的配置，配置多个操作系统版本时，可以使用逗号分隔。需要注意的是，您只能在白名单和黑名单参数中二选其一进行配置。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970789.png)
8. 单击**下一步**，您可以进一步设置规则生效的范围，比如，配置该规则只对某些资源组内的资源或者具有某些标签的资源生效。以此来对合规管控的资源范围进行更加精细化的管理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970793.png)
9. 创建完成后，在规则详情页，您可以看到当前账号组下，所有不合规的资源，既操作系统版本不符合要求的所有 ECS 主机实例。该规则，默认会每 24 个小时执行一次检测，您可以在创建规则或者修改规则时，配置该规则的触发频率。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970796.png)
10. 最后，您还可以将不合规资源数据投递到其他云产品中，比如日志服务、对象存储等。方便您进一步对数据进行归档、处理、审计等操作。更多投递相关的信息，请参考[配置审计投递](https://help.aliyun.com/zh/document_detail/310163.html)。

#### 通过 SMC 实现操作系统迁移

如果您的 ECS 主机实例操作系统满足 SMC 操作系统迁移条件，可通过 SMC 平滑迁移到新的操作系统版本。SMC 支持白屏化操作，在控制台上，您可以实时查看迁移进度和迁移日志。同时，迁移前，SMC 会自动进行快照的创建，对当前主机实例进行备份，保证可回滚。最后，SMC 迁移过程中，会保留系统盘中的数据，您无需担心数据会丢失。

在使用 SMC 进行操作系统迁移前，请认真阅读上文注意事项中的**服务器迁移中心使用限制**和**业务应用架构要求**，确保您的 ECS 实例的操作系统版本等满足 SMC 的迁移要求，同时确保您的业务应用支持滚动发布升级，以此保证业务的稳定性和可用性，避免出现迁移过程中业务不可用的情况。

1. 登入相应的业务账号，进入[服务器迁移中心（SMC）控制台](https://smcnext.console.aliyun.com/)。在左侧导航栏选择**迁移源**。切换到**阿里云ECS服务器**标签页，单击**导入迁移源**，将需要进行操作系统迁移的 ECS 主机实例导入进来。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970798.png)
2. 如果进行操作系统迁移，您需要保证您的 ECS 实例上已经安装有服务器迁移中心客户端，建议您在导入迁移源时，选择自动为该 ECS 实例进行安装。您可以选择通过控制台、命令行、客户端等方式批量导入 ECS 实例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970803.png)
3. 导入完成后，在迁移源列表中，就可以看您导入的所有 ECS 实例。单击**创建迁移任务**，在**迁移任务迁移**中，选择**操作系统迁移**。建议您开启**迁移演练**，迁移演练功能可以帮助您在实际迁移前充分了解迁移任务的可行性和风险，并提供修复建议，从而减少实际迁移中可能出现的问题和损失。迁移演练过程中按量收费资源将会消耗一定的费用。具体请参考[《配置迁移演练》](https://help.aliyun.com/zh/smc/user-guide/configuration-migration-walkthrough)与[《迁移演练项说明》](https://help.aliyun.com/zh/smc/user-guide/migration-walkthrough-item-description)。单击**创建**，既可创建一个迁移任务，开始所选 ECS 实例的操作系统迁移的工作。建议您提前规划好迁移计划，严格分批进行，一批 ECS 实例迁移完成并验证确认无误后，再进行下一批实例的迁移工作。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970804.png)
4. 在左侧导航栏选择**迁移任务**。切换到**操作系统迁移**标签页，您可以在列表中查看所有的操作系统迁移任务。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970805.png)
5. 单击对应的迁移任务ID，进入迁移任务详情页。单击**查看日志**，您可以查看详细的迁移日志。单击演练报告**查看报告**，您看一查看当前迁移过程的风险，并根据修复建议进行相应的处理。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970806.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970807.png)
6. 迁移完成后，您可以在迁移目标 ECS 实例详情页的**配置信息**区域，看到操作系统已经迁移为目标系统。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970811.png)
7. 如果迁移失败，您需要查看日志修复问题后，再次重启迁移任务。常见错误及修复方案的更多信息，请参见[SMC FAQ](https://help.aliyun.com/zh/smc/support/faq)和[操作系统迁移故障（Linux）](https://help.aliyun.com/zh/smc/support/operating-system-migration-failures/)。您也可以回滚源系统云盘数据，在快照列表使用自动备份的快照进行恢复数据，登录[ECS管理控制台](https://ecs.console.aliyun.com/)，在左侧导航栏，选择**存储与快照** > **快照**。在**云盘快照**页签下，在自动备份的快照操作列，单击**回滚磁盘**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970813.png)

#### 通过 OOS 替换系统盘

对于 SMC 不支持的操作系统类型和版本，您还可以使用 OOS 的运维任务，通过更换系统盘的方式进行迁移。需要注意的是，通过替换系统盘的方式迁移操作系统，只能保留数据盘中的用户数据，系统盘内的用户数据将无法保留，因此建议您将业务应用的配置信息、应用日志等存放到数据盘中，或者确保您的业务应用的运行和运维不依赖于本地数据，比如使用[MSE Nacos配置管理](https://help.aliyun.com/zh/mse/user-guide/manage-configurations/)对应用配置进行集中管理和推送、使用[日志服务](https://help.aliyun.com/zh/sls/product-overview/what-is-log-service)统一采集应用日志等。

同时在替换系统盘前，建议您为对当前 ECS 实例的系统盘进行快照备份，保证能够在迁移失败时，快速回滚，回复数据。

##### 批量创建快照（可选）

1. 登入相应的业务账号，进入[系统运维管理 OOS 控制台](https://oos.console.aliyun.com/)。切换到系统云盘所在的地域，在左侧导航栏选择**自动化任务**>**常见运维任务**。
2. 选择**批量操作云盘**页签，单击创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970812.png)
3. 在任务类型一项中，选择**批量给云盘创建快照**。选择需要创建快照的系统盘，配置完成后，单击**创建**，既可创建一个 OOS 任务。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970817.png)
4. 在任务详情页，您可以实时查看任务执行的进度。OOS 任务执行成功后，进入 ECS 控制台，在左侧导航栏选择**存储与快照**>**快照**。切换到**云盘快照**页签，在快照列表中，就可以看到新建的云盘快照。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970819.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970821.png)

##### 替换系统盘

1. 登入相应的业务账号，进入[系统运维管理 OOS 控制台](https://oos.console.aliyun.com/)。您可以选择一个地域作为管理地域，将替换系统盘的运维任务统一创建到该管理地域，统一从管理地域运维其他地域的 ECS 实例。切换到该管理地域，在左侧导航栏选择**自动化任务**>**常见运维任务**。
2. 选择**批量操作实例**页签，单击创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970815.png)
3. 在任务类型一项中，选择**实例操作**。需要执行的操作一项中，选择**更换系统盘**。在镜像ID一项中，选择需要替换到的目标镜像。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970818.png)
4. 接下来选择需要替换系统盘的目标 ECS 实例。这里您可以通过多种方式跨地域批量选择多个 ECS 实例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970826.png)
5. 如果您有多台 ECS 实例需要迁移，建议您分批进行，一批 ECS 实例迁移完成并验证确认无误后，再进行下一批实例的迁移工作。你可以在**高级选项**一栏中，速率控制类型选择**批次控制**，然后配置批次比例，这样把一个执行明确地分成多个批次，然后一个批次运行完，再运行下一个批次，上一个批次不全部完成的情况下，下一个批次不会开始，同时配置为**每批暂停**的循环并发控制，确保能够及时对迁移结果机型验证。配置完成后，单击**创建**，既可创建一个 OOS 任务。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970820.png)
6. 在任务详情页，您可以实时查看任务执行的进度。OOS 任务执行成功后，进入 ECS 实例详情页，可以看到相应的 ECS 实例操作系统已经替换为了目标系统。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970824.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0376581571/p970828.png)
7. 如果迁移失败，您可以回滚源系统云盘数据，在快照列表使用自动备份的快照进行恢复数据，登录[ECS管理控制台](https://ecs.console.aliyun.com/)，在左侧导航栏，选择**存储与快照** > **快照**。在**云盘快照**页签下，在自动备份的快照操作列，单击**回滚磁盘**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1376581571/p970829.png)

## 故障排除

### 为什么无法使用 SMC？

可能有如下几个原因：

- 未进行 RAM 授权，请确保已经创建了 SMC 服务关联角色，完成相关授权操作。
- 账号余额不足，请确保账号余额大于等于100元（充值或代金券皆可）。
- 账号未实名认证，请确保您已完成账号实名认证。

更多原因请参考 [SMC 迁移准备工作](https://help.aliyun.com/zh/smc/user-guide/before-you-begin)。

### 为什么 SMC 操作系统迁移失败？

使用 SMC 进行操作系统迁移，常见问题请参考：

- [Linux 操作系统迁移故障](https://help.aliyun.com/zh/smc/support/operating-system-migration-failures/)
- [Windows 操作系统迁移故障](https://help.aliyun.com/zh/smc/support/windows-operating-system-migration-failure/)

### 为什么执行 OOS 运维任务失败？

使用 OOS 的常见问题，请参见 [OOS 服务支持](https://help.aliyun.com/zh/oos/support/faq)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-223（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
