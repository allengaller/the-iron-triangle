<!-- source: https://help.aliyun.com/zh/well-architected/solution-266 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929421 -->

# 应用系统同城双活演练方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972011.png)

容灾演练是通过模拟实例、机房或地域级故障，判断系统服务的逃逸能力，验证系统的容灾能力以及面对灾难时的应对能力，可以帮助企业更好的验证RPO、RTO指标。为了确保业务系统能够在资源故障或可用区故障的情况下继续正常运行，客户需要在业务上线前及业务上线后定期进行容灾演练，及时发现和解决相关问题，提高系统的可用性和可靠性。

《[通过MSE实现应用同城容灾](https://help.aliyun.com/zh/well-architected/solution-219)》方案提供了一套用于演示的同城高可用的参考架构，本方案基于此架构详细介绍了如何使用云速搭 CADT 容灾管理服务来实现容灾计划和容灾集的可视化配置，以及通过非入侵方式实现容灾切换演练。

## 方案优势

### 操作简单

#### 可视化实现

从架构构建、资源配置、应用部署以及部署后的容灾演练配置，全流程可视化操作，轻松掌握当前架构高可用部署情况，简单便捷，无需编写代码，降低学习成本，提高运维效率。

#### 交付快

CADT现有客户，基于架构进行高可用设计改造，架构支持高可用情况下，容灾集配置分钟级交付。

#### 成本低

客户自服务完成容灾演练，自动化生成容灾演练报告，业务上线及架构升级后可以自服务进行容灾能力验证。

### 安全稳定

#### 安全无入侵

对基础架构层演练使用云产品原生提供的切换 API，无入侵方式进行故障注入。

#### 监控保障

提供对部署资源的统一监控能力，实现对云服务统一监控和问题定位，方便架构的运维管理。

## 客户场景

### 提高业务系统稳定性和可靠性

#### 场景描述

企业已经或者即将在阿里云上构建关键业务系统，希望以一种高效且成本可控的方法，提升整体应用层面容灾水平，确保在真实灾难发生时能够迅速恢复业务运行。

#### 适用客户

- 未上云，需要设计、部署和管理一套同城跨可用区的容灾架构的客户。
- 已上云，需要定期进行容灾演练，以验证系统的健壮性和容灾能力的客户。
- 主要适用于互联网、金融等对服务可用性较强的行业。

## 客户案例

### 客户背景

某全球化IP游戏运营商X，以IP为核心，通过自主研发和联合研发，为全球玩家提供精品IP游戏，打造极具竞争力的IP游戏生态体系。

### 客户痛点

为了保障平台稳定性，X希望对核心系统进行容灾演练，发现潜在的问题及时修复，降低出现故障的风险，目前主要存在以下痛点：

1. 需要进行演练的系统涉及到多款云产品，系统架构复杂。
2. 采用传统的演练方案需要编写对应的脚本，投入成本高、维护难度高。
3. 演练期间需要记录每个产品演练前后的状态以及状态切换的时间，采用手工统计效率低下

### 实施方案

- 通过CADT架构探查快速还原待演练系统的完整拓扑，帮助运维团队更好的管理云上的业务系统。
- 通过CADT可视化的页面，用户只需要选择对应的云产品实例，零代码快速完成演练计划的统一配置，大幅减少了人力投入。
- CADT支持导出实时的容灾演练报告，报告中记录了资源状态、演练时间、演练是否成功等关键信息，帮助用户评估演练是否符合预期。

### 客户收益

客户高效且低成本完成了容灾演练。

## 方案架构

《[通过MSE实现应用同城容灾](https://help.aliyun.com/zh/well-architected/solution-219)》方案提供了一套用于演示的同城高可用的参考架构，本方案以该架构的资源进行演练。通过这套高可用部署的架构，采用CADT容灾管理服务实现容灾计划、容灾集的可视化配置和容灾演练实验，演练完成后从演练报告、产品控制台以及应用层三个角度查看演练结果，确保服务的可用性。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972009.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云速搭CADT | [云速搭CADT](https://help.aliyun.com/zh/cadt/product-overview/what-is-cadt)是阿里云推出的一款为上云应用提供自助式云架构管理的产品，通过CADT可以快速创建云上应用架构，自动化部署资源，轻松实现对云上应用的全生命周期管理，可以显著降低云资源管理的难度和时间成本，助力客户高效便捷上云。 | 部分服务需收费，详情参见[产品计费](https://help.aliyun.com/zh/cadt/product-overview/billing) |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 容灾计划 | 当CADT应用需要进行容灾演练时，需要为其创建容灾计划，加入了容灾计划的应用才具备容灾演练能力。 |
| 容灾集 | 容灾演练基于容灾集进行，容灾集包含了同一个容灾计划中不同产品以及切换策略的自由组合，可以实现灵活的容灾演练配置。 |
| 容灾切换 | 根据容灾集中配置的资源及切换策略，进行资源切换演练。 |
| 容灾切回 | 与容灾切换相反，将资源切回到执行容灾切换之前的状态。在进行容灾切换时，系统会记录资源主备节点的配置，进行切回操作时，系统会将主备节点恢复成切换前的配置。 |

## 安全性

### 访问控制

#### 身份管理

为确保您的阿里云账号及云资源使用安全，如非必要都应避免直接使用阿里云账号（即主账号）来访问云速搭。推荐的做法是使用RAM身份（即RAM用户和RAM角色）来访问云速搭。企业内有多名员工或应用程序需要访问云速搭时，可以使用RAM服务做统一的权限管理，按需为他们分配不同的访问权限。在使用RAM管理阿里云产品的访问权限前，您需要了解云产品能与RAM的哪些功能结合使用，从而更好地设计满足业务需要的访问控制。

#### 权限管理

云速搭CADT原生支持阿里云[RAM访问控制](https://www.aliyun.com/product/ram?spm=a2c4g.11186623.0.0.20e047e2FiNTGi)和[资源管理](https://www.aliyun.com/product/entconsole?spm=a2c4g.11186623.0.0.20e047e2FiNTGi)体系，通过权限管理，您可以方便地实现对CADT及其应用和模板的权限管控。云速搭CADT支持三种系统策略，详细内容可参见[CADT系统策略介绍](https://help.aliyun.com/zh/cadt/security-and-compliance/system-policies-of-cadt)。

| **权限策略名称** | **权限策略说明** |
| --- | --- |
| AliyunCADTReadOnlyAccess | 只读管理云速搭CADT的权限 |
| AliyunCADTImportAccess | 云速搭CADT资源探查及导入资源的权限 |
| AliyunCADTFullAccess | 管理云速搭CADT的权限 |

如果系统策略无法满足您的需求，您可以通过创建自定义策略实现精细化权限管理，详细内容可参见[CADT自定义权限策略及使用方法介绍](https://help.aliyun.com/zh/cadt/security-and-compliance/create-custom-policies-for-cadt)。

## 注意事项

### 影响范围

演练时，容灾集内全部云服务器实例将强制关机，其他云产品将强制切换备用可用区，可能出现不可预知的系统异常风险、数据丢失风险以及可能触发大量告警信息。所以请确认：

- 首次演练宜选择最小范围或在非业务高峰期时段进行，减少对核心业务的影响。
- 需提前对云服务器和数据库进行数据备份，以便在紧急情况下回退。
- 做好业务中断（极端情况下4小时以上）准备工作。

### 支持的云产品

目前CADT云速搭支持部署的阿里云产品可以在CADT控制台查看列表查看，详情可参见[支持的产品](https://help.aliyun.com/zh/cadt/product-overview/supported-services)。

目前CADT容灾管理服务支持的产品见下表，详情可参见[支持的产品](https://help.aliyun.com/zh/cadt/user-guide/overview-of-disaster-recovery-management)。

| **类别** | **产品** |
| --- | --- |
| 弹性计算 | 云服务器ECS |
| 数据库 | 云数据库RDS云数据库RDS MySQL版（高可用版、集群版）云数据库RDS SQL Server版云数据库RDS PostgreSQL版 |
| 云数据库 Tair（兼容 Redis） |  |
| 云数据库MongoDB版副本集分片集群 |  |
| 云原生数据库PolarDB云原生数据库 PolarDB MySQL 版 |  |
| 云原生数据库PolarDB分布式版（PolarDB-X）PolarDB-X 2.0PolarDB-X 1.0（DRDS） |  |
| 云数据库OceanBase版 |  |
| 网络 | 网络型负载均衡NLB、应用型负载均衡 ALB |
| 中间件 | 微服务引擎MSE |
| 容器服务 | ACK 托管版、ACK专有版 |

## 实施步骤

### 实施准备

注：本方案是在《[通过MSE实现应用同城容灾](https://help.aliyun.com/zh/well-architected/solution-219)》基础上实现，所以需要先按照要求部署完前置方案所需资源，详情可参考《[通过MSE实现应用同城容灾](https://help.aliyun.com/zh/well-architected/solution-219)》中实施步骤部分。搭建完成后会存在：

1. 两个MSE注册中心
2. 两个不同可用区各有一套ACK集群
3. 一套云原生网关实例
4. 创建一台**多可用区**RDS数据库实例，详情可参见：[创建RDS实例](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases)。
5. 创建一台**多可用区**云数据库Tair（兼容Redis）实例，详情可参见：[创建Tair实例](https://help.aliyun.com/zh/redis/getting-started/step-1-create-an-apsaradb-for-redis-instance)。
6. 在两台ACK集群中部署Demo应用，应用可分别连接RDS实例与Redis实例进行查找、插入、删除操作，后期会用于验证服务可用性。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：30分钟。

### 操作步骤

#### 制定演练流程

在演练前，业务团队与运维团队需一起制定出清晰的演练步骤，不可随意更改过程或临时扩大演练范围。本方案的演练流程可参考下图：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972010.png)

#### 创建应用架构

容灾演练属于高风险操作，这里使用具有管理员权限的账号进行演示，先通过 CADT部署一个符合同城多活要求的应用架构。

1. 访问 [云速搭 CADT](https://bpstudio.console.aliyun.com/) ，登录云速搭 CADT 控制台。说明：如果提示需要开通服务，请根据提示进行开通。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972012.png)
2. 在菜单栏单击新建 > 官方解决方案 > 模版。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972013.png)
3. 在搜索中输入“基于MSE云原生网关同城多活”，找到模板，点击基于应用新建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972017.png)
4. 架构图打开后，将所需资源按需调整，可新建也可导入已有资源，本方案由于在前序方案与实施准备中已构建好所需资源，所以资源均为导入（双击架构图中某资源，右侧出现资源详情，在购买方式部分选择「导入已保有」即可）。调整完成后点击右上角保存，并设置应用名称，例如“duohuo”。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972014.png)
5. 整个架构如果确认无误的话，可以点击部署应用。进入资源验证阶段，首次使用某款云产品，需要进行开通授权操作，根据提示信息，单击授权链接进行产品授权。完成服务的开通授权操作后，点击返回，重新执行部署应用操作，当资源验证状态为校验成功时，可以点击下一步：价格清单。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972018.png)
6. 进入核算价格阶段，这里会将应用中的云资源按照免费、按量付费和包年包月进行分类显示，如果产品享受折扣这里会自动将账号对应的优惠显示出来。价格清单中的价格信息为当时的实时价格，具体产品价格信息请以页面显示为准。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972015.png)
7. 如果确认价格符合预期，可以单击下一步：确认订单。确认订单阶段会列出架构中所有的产品及其价格，需要用户确认无误后勾选接受《云速搭服务条款》，此时下一步：支付并创建才会高亮，可以单击进行实际的资源购买和部署。
8. 这时进入订单准备并进行下单，右上角会有提示，请耐心等待，不要关闭窗口。说明：这里的方案编号是这个应用的唯一标识，如果提交工单，需要提供这个方案编号。
9. 等待应用部署成功后，可以看到整个架构图中包含的网络、计算、数据库等资源已经部署完成。单击返回按钮，在应用页面可以看到，部署成功的资源在应用架构中带有绿色标识：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972020.png)

#### 购买容灾管理服务

1. 统计 duohuo 应用中支持容灾演练的资源数量。说明：截止 2024-12-12，云速搭 CADT 尚未支持所有产品。目前 CADT 容灾管理服务支持的完整产品清单请查看[支持的产品](https://help.aliyun.com/zh/cadt/user-guide/overview-of-disaster-recovery-management)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972021.png)
2. 购买对应实例数量的容灾管理服务。根据应用中支持容灾演练的资源数量为 x，需要购买可支持配置对应实例数量的容灾管理服务。（如果购买的实例数量小于应用中支持容灾演练的资源数，则无法创建容灾计划）![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972016.png)
3. 购买完成后，可以在对应的控制台页面中，查看容灾管理服务当前可支持配置的实例数量、已配置的实例数量和开通、到期时间等信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972023.png)

#### 创建容灾计划与容灾集

1. 为需要进行容灾演练的应用 duohuo 创建容灾计划。在容灾管理服务页面，单击创建容灾计划，从下拉列表选择应用“duohuo”![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972026.png)
2. 等待容灾计划创建完成，创建成功后可以在右上角看到创建成功提示。容灾计划创建时间和资源量相关，如果资源较多，例如 100-500，需要 20s 左右。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972028.png)容灾计划创建成功后进行以下检查操作：点击查看架构图，可以查看该容灾计划对应的应用架构图，避免加入错误。点击查看资源，可以查看当前应用中支持容灾演练资源的资源信息及不支持高可用的风险资源。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972019.png)查看风险资源，可以看到部署时配置的 2台单可用区的ACK集群 提示为风险资源。说明：风险资源提示不影响演练，但是建议客户对风险资源进行容灾改造。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972029.png)
3. 以业务模块维度创建容灾集![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972030.png)
4. 创建好容灾集后点击配置即可新增资源，此处为演示方便将所有资源放入同一个容灾集中![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972031.png)全部资源添加完成后，可以展开 yanlian 容灾集查看各个资源属性：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972022.png)

#### 容灾计划切换

1. 切换前进行 RDS 等资源的备份，以备容灾演练过程出现异常情况需要数据恢复时使用。云速搭 CADT 容灾管理服务使用 API 进行强制关机及强制切换模拟故障迁移场景，强制关机时未落盘的数据会丢失，强烈建议容灾演练前进行演练资源的备份。数据备份有费用产生，请详细了解相关的费用说明。可以针对不同的容灾集资源进行独立配置。建议在每次容灾演练时间窗启动时，先进行切换准备对实例创建镜像，实现数据备份。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972034.png)选择在容灾演练前为 RDS 进行备份。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972033.png)点击切换准备对 yanlian 中的资源进行备份操作。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972024.png)备份创建时间与容量相关，请耐心等待：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972035.png)当出现创建成功后，可以到 RDS 控制台中查看快照情况：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972036.png)参考上述步骤，完成其他容灾集相关演练资源的备份操作。
2. 单击容灾计划切换（切换所有在此可用区的资源），选择要进行切换的可用区，这里选择杭州可用区 I。说明：切换需要使用主账号或者具有管理员权限的子账号进行操作。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972025.png)应用切换中，可以单击刷新按钮，实时刷新查看当前容灾计划下的各个容灾集切换进度：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972027.png)可以展开容灾集资源列表，点击资源 ID 前往控制台查看、确认资源切换的状态。

#### 演练结果及服务可用性验证

1. 容灾计划切换完成后，可以导出容灾演练报告查看本次容灾切换详情。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972037.png)演练报告中包含以下内容：容灾计划架构图容灾计划及容灾集信息切换耗时执行切换or切回前的资源清单当前资源状态信息及切换耗时明细![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972039.png)
2. 在云产品控制台查看、确认资源切换后的状态。RDS主备可用区已切换：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972041.png)Redis中MASTER节点已切换可用区：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972032.png)
3. 从应用角度验证服务可用性ACK集群中部署了一个简单的应用yanlian，分别连接了Redis和RDS，并且通过云原生网关将服务暴露出来。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972042.png)在步骤2中可以从控制台确认底层数据库均已按照预期切换了备可用区，此时通过curl指令来获取数据库中的数据：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972038.png)与演练前数据一致，并且插入删除的功能也可以正常使用，所以可以看出业务层并未因为演练而受损，仍然可以正常使用。**说明：不同的产品可能因为主备切换造成不同时间的闪断现象，时长与影响可与对应云产品沟通获取。**

#### 容灾计划切回

在故障恢复后，通过容灾计划切回功能，快速将应用中的资源切回到发生故障之前的状态。

1. 单击容灾计划切回。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1186581571/p972043.png)
2. 仔细阅读提示信息，如果出现数据丢失，可通过之前创建的备份数据进行恢复，确认无误，进行切换。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972040.png)
3. 等待全部容灾集切回成功后，立即查看容灾演练报告
4. 查看切回后的资源清单。可以看到数据库等产品主可用区已经切回到 I，备可用区切回成 J，全部资源已切回到容灾切换之前的状态。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0186581571/p972044.png)

## 故障排除

### 如何确认CADT是否支持导入某款产品的已保有实例？

在CADT控制台新建空白应用，应用中包含对应的产品，双击打开产品配置面板，如果在**购买方式**下可以看到**导入已保有**配置项，则表示CADT支持导入该产品的已保有实例，反之，则不支持。详情可参考[帮助文档](https://help.aliyun.com/zh/cadt/support/support-for-importing-existing-instances-of-a-service)。

### 部署应用时，提示属性校验（端口、监听协议等）报错，该如何处理？

进行应用部署时，提示属性校验报错，可根据提示信息修改、补充资源配置。一方面可能是资源参数配置缺失；另一方面可能是对存在关联关系的资源间缺少通信协议、端口等参数的配置。详情可参考[帮助文档](https://help.aliyun.com/zh/cadt/support/what-do-i-do-if-a-property-verification-error-is-reported-when-i-deploy-an-application)。

## 相关内容

- [通过MSE实现应用同城容灾](https://help.aliyun.com/zh/well-architected/solution-219)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-266（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
