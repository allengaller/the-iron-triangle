<!-- source: https://help.aliyun.com/zh/well-architected/solution-265 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929422 -->

# 通过云备份实现统一数据备份

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972047.png)云备份（Cloud Backup）作为阿里云统一灾备平台，是一种简单易用、敏捷高效、安全可靠的公共云数据管理服务，可以为阿里云ECS整机、ECS数据库、文件系统、NAS、OSS以及自建机房内的文件、数据库、虚拟机、大规模NAS等提供备份、容灾保护以及策略化归档管理。本方案介绍如何通过云备份对云上数据进行统一备份管理。

## 方案优势

### 可控

提供实时主动监控，可灵活定制全量、增量（差量）、日志、实时备份策略；短信和邮件多通道告警；备份历史任务、错误日志报告控制台多方位展示。

### 高效

高效重删压缩技术，重删比可达30:1，帮您节约所需的云存储容量。同时，针对混合云场景，源端重删能力，也节省了您上云的带宽。其次，相对自建备份显著降低成本，简化运维，提高效率。

### 安全

使用 AES-256 源端加密及存储加密，保证数据安全。通过加密、备份锁定、用户权限管理、多因素认证可最大

限度提高备份恢复的安全性。

### 可靠

使用 CRC64 校验，集群部署方式，满足12个9数据可靠性，99.9%可用性SLA。

## 客户场景

### NAS、OSS无代理自动备份

NAS , OSS 数据量大，缺乏自带定时备份机制。而使用传统方案需要在ECS上自制脚本或安装灾备软件，安装配置复杂，成本高。

### 数据备份和跨区域备份

目前脚本方式备份缺乏自动化、执行日志和统一管理，出现异常，无法快速发现；复制方式无法进行重删压缩，备份效率低下，成本高；同时恢复操作复杂，恢复粒度较大，无法保障恢复时效。

### 本地灾备上云

等保等相关合规要求，需要进行本地和异地备份、容灾，但传统备份方式无法上云或者无法根据不同数据合规要求分策略上云，只能灾备到线下的另外一个机房。以及数据量较大，带宽不足时，备份数据无法传输到云端。

### 本地非结构数据归档上云

本地非结构化数据因合规和可追溯性要求，需要长期保留几个月、几年不等，数据越来越大，成本越来越高。传统的备份方式，因数据量较大，备份一次时间全花在扫描上了，无法按期完成备份；数据在存储周期内需要避免被篡改和删除 海量数据存储后，需要快速查找、调阅到所需的文件。

## 客户案例

### 客户背景

某出版社以水利电力专业为基础、兼顾其他学科和门类，以纸质书刊为主、兼顾电子音像和数字出版。

### 客户痛点

数据分散在多套应用系统，原采用自建脚本备份，缺乏统一、自动化的备份管理能力；而传统备份方式部署复杂，周期长。因此需要对现有数据进行统一的备份管理，其中包含本地机房和阿里云端，同时需要保证数据的安全行、可靠性，并需要支持自动化执行备份、自动淘汰过期历史备份副本、异常自动告警，支持短信、邮件告警。

### 实施方案

使用云备份云上线下环境提供统一、安全、高效的数据保护。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972045.png)

### 客户收益

- 云上云下统一管控
- 云备份服务即开即用，弹性灵活
- 端到端加密，保障数据安全
- 通过重删压缩技术，可以节省大量备份成本

## 方案架构

云备份（Cloud Backup）是一种简单易用且高性价比的在线备份服务，可以为阿里云 ECS，NAS，OSS 以及自建机房内的各类数据提供安全，高效的保护。本方案主要介绍如何通过云备份对云上数据进行统一备份管理。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972046.png)

云备份支持同地域及异地备份两种模式。在进行备份时，云备份并未单独开辟一块独立于OSS之外的存储空间，而是集成并利用了OSS作为备份存储媒介，用户需要授权云备份读取OSS数据的权限，并配置备份策略指定OSS Bucket（备份库）作为备份目标。这样设计既利用了OSS的高可靠性和弹性扩展能力，也使得用户可以根据自身需求灵活管理备份存储资源。

如果OSS源端发生故障，借助云备份服务，能够实现几乎即时的数据保护（分钟级RPO）和快速的业务恢复（分钟级RTO），并且在同地域恢复时不会产生额外费用。不过，实际的RTO和数据丢失量（即RPO的具体时间窗）还会受到备份频率、数据量、网络延迟等具体因素的影响，具体详见[备份及恢复速率](https://help.aliyun.com/zh/cloud-backup/support/backup-speed-and-recovery-speed)。

云备份通过同城冗余备份库（ZRS）、跨地域备份能力，以及潜在的高可用架构设计，确保了即使面临单个可用区故障，也能保持服务的高可用性和数据的可访问性，从而有效保障用户的业务连续性。

云备份还提供了用户可自定义的归档计划，其中归档执行间隔可选天、周；归档保留时间可选天、周、年、月。同时，云备份还提供了自动归档功能，专为需要长期保存但不常访问的历史数据设计，旨在帮助用户以更低的成本进行数据留存。具体详见[归档操作](https://help.aliyun.com/zh/cloud-backup/user-guide/archive-data)。

- 支持地域：华南1（深圳），华北2（北京），华东2（上海）
- 支持数据源：支持本地NAS、 HDFS系统和S3兼容存储

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云备份 Cloud Backup | [云备份（Cloud Backup）](https://help.aliyun.com/zh/cloud-backup/product-overview/what-is-hbr)作为阿里云统一灾备平台，是一种简单易用、敏捷高效、安全可靠的公共云数据管理服务，可以为阿里云ECS整机、ECS数据库、文件系统、NAS、OSS以及自建机房内的文件、数据库、虚拟机、大规模NAS等提供备份、容灾保护以及策略化归档管理。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/cloud-backup/product-overview/billing/)。 |
| 专有网络 VPC | [专有网络VPC（Virtual Private Cloud）](https://help.aliyun.com/zh/vpc/product-overview/virtual-private-cloud-overview/?spm=a2c4g.11186623.help-menu-27706.d_0_1.3db95286eC1BbI)是专有的云上私有网络，允许用户在公共云上配置和管理一个逻辑隔离的网络区域。用户能够完全掌控自己的专有网络，包括选择自己的IP地址范围、创建交换机、配置路由表和网关等。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |
| 访问控制 RAM | [访问控制RAM（Resource Access Management）](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)是阿里云提供的管理用户身份与资源访问权限的服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/ram/product-overview/billing-methods) |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 对象存储 OSS | [阿里云对象存储OSS（Object Storage Service）](https://help.aliyun.com/zh/oss/product-overview/what-is-oss?spm=a2c4g.11186623.help-menu-31815.d_0_1_0.67a21eb72ZgzPo&scm=20140722.H_31817._.OR_help-T_cn#DAS#zh-V_1)是一款海量、安全、低成本、高可靠的云存储服务，可提供99.9999999999%（12个9）的数据持久性，99.995%的数据可用性。多种存储类型供选择，全面优化存储成本。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/oss/product-overview/billing-overview/?spm=a2c4g.11186623.help-menu-31815.d_0_2.20673d885wLnCY&scm=20140722.H_59636._.OR_help-T_cn#DAS#zh-V_1)。 |
| 文件存储 NAS | [阿里云文件存储 NAS（File Storage NAS）](https://help.aliyun.com/zh/nas/product-overview/what-is-nas)是面向阿里云ECS实例、E-HPC、[容器](https://www.aliyun.com/getting-started/what-is/what-is-container)服务等计算节点的文件存储服务。它是一种可共享访问、弹性扩展、高可靠以及高性能的分布式文件系统。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/nas/product-overview/billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 备份源 | 需要备份的数据。一般这些数据都保存在服务器、虚拟机或者ECS实例等。 |
| 客户端 | 客户端安装在可以访问备份源的服务器或虚拟机上。您可以通过客户端进行备份和恢复等操作。不同的备份源系统和平台需要安装相应的客户端。客户端支持定时重试等方式确保备份稳定性，在网络短时抖动情况下依然可以完成备份。 |
| 备份库 | 用于存放您的备份数据，分为标准层和归档层。数据备份完成后，备份数据将首先存储在标准层内；如果您启用了自动归档功能，备份数据将按照设定的归档策略流转到归档层，用于长时间低成本的保存。 |
| 备份计划 | 为备份源创建一个周期性、定时定期执行的备份计划，设置的参数包括备份源、备份路径、备份起始时间、备份执行间隔、保留时间等，便于周期性地持续备份数据。 |
| 恢复任务 | 将备份库中的数据恢复至备份源或其他目的地。设置的参数包括恢复项目、恢复目的地、恢复路径等。 |
| 全量备份 | 一种备份指定数据集内所有数据的备份方式。全量备份将会读取数据集被所有数据并存储其完整副本，备份耗时较长，消耗存储空间较大 （在具有重复数据删除的备份服务中存储空间消耗可控），但因为含有完整数据集，恢复较快。 |
| 增量备份 | 一种识别并备份指定数据集内相对于上一次备份有变更操作的数据的备份方式。变更包含新增、修改、删除操作。增量备份一般来说相对全量备份耗时更少，备份效率比较高，但恢复时需要回溯备份链以寻找对应文件，恢复较慢。 |
| 恢复逻辑 | 按照用户指定的备份版本以及其中的数据（比如某个文件夹），从备份库中读取数据并经过解密，解压缩等操作恢复出原始数据并写回到用户指定的系统中。 |

## 安全性

### 服务关联角色

云备份使用服务关联角色获取云服务器ECS、专有网络VPC、对象存储OSS、文件存储NAS等资源的访问权限。通常情况下，服务关联角色是在您开启某项备份功能、创建备份计划或者为数据源关联备份策略时时，由云备份自动创建。在自动创建服务关联角色失败或云备份不支持自动创建时，您需要手动创建服务关联角色。详情请见[云备份服务关联角色](https://help.aliyun.com/zh/cloud-backup/security-and-compliance/service-association-role-provided-only-when-involved-otherwise-no-need)。

### 数据安全

1. 云备份提供备份源端加密，并支持基于SSL/TLS的HTTPS加密传输，有效防止数据在云端的潜在安全风险。
2. 云备份对备份数据在源端完成AES256加密后传输上云并加密保存。默认情况下云备份使用自行管理的密钥加密数据，您也可以使用自己账号的密钥管理服务KMS（Key Management Service）的密钥。其中，如果ECS磁盘本身已经加密，那么通过阿里云的云备份（HBR）服务进行备份的数据也会保持加密状态，详见[云备份KMS加密](https://help.aliyun.com/zh/cloud-backup/user-guide/use-kms-encryption)。
3. 云备份支持通过HTTP或HTTPS的方式访问。安全传输层协议（SSL/TLS）用于在两个通信应用程序之间提供保密性和数据完整性。

### 监控与报警

云备份已接入阿里云基础云监控系统事件服务供您免费使用，可实现对备份任务状态进行实时监控。同时支持发送备份报警通知。

## 注意事项

### 支持云备份的云产品

- NAS 文件
- OSS 文件
- ECS 整机备份
- ECS 文件系统
- ECS 自建数据库My SQL 数据库SQL Server 数据库Oracle 数据库SAP HANA 数据库

详情及使用限制请参考云备份[使用限制](https://help.aliyun.com/zh/cloud-backup/product-overview/limits-1)

## 实施步骤

- 本方案涉及资源的开通申请时，如未有特别说明，统一使用阿里云华东 1（杭州）。
- 本方案仅作为实践演示，购买的所有云产品规格均为演示需要，用户实际环境，请按照实际业务需求购买对应规格的产品服务，如 ECS、SLB 等
- 本方案为了演示方便，ECS 安全组配置以及 SLB 的访问控制配置从简，请按照实际业务需求配置正确的安全规则。
- 本方案重在演示迁移思路和做法，demo 程序以及应用配置从简，请按照实际业务需求配置。

### 实施准备

- 注册阿里云账号，并完成实名认证。您可以登录阿里云控制台，并前往[实名认证页面](https://account.console.aliyun.com/v2/#/authc/home)，查看是否已经完成实名认证。
- 阿里云账户余额大于 100 元。您可以登录阿里云控制台，并前往[账户总览](https://usercenter2.aliyun.com/home)页面查看账户余额。
- 开通以下服务：VPC：开通请前往 [VPC 控制台](https://vpc.console.aliyun.com)ECS：开通请前往 [ECS 控制台](https://ecs.console.aliyun.com)RAM：开通请前往 [RAM 控制台](https://ram.console.aliyun.com/overview)OSS：开通请前往 [OSS 控制台](https://oss.console.aliyun.com/overview)NAS：开通请前往 [NAS 控制台](https://nasnext.console.aliyun.com/overview)Cloud Backup：开通请前往 [云备份控制台](https://hbr.console.aliyun.com/)

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：40分钟。

### 操作步骤

#### 开通云备份

开通云备份只需要操作一次。

1. 登录云备份 Cloud Backup [控制台](https://hbr.console.aliyun.com/)。
2. 在服务开通页面，仔细阅读并选中云备份协议，单击开通服务。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972048.png)
3. 开通完成后，云备份控制台会提示您已经开通服务，您就可以进行备份了。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972049.png)

#### 创建备份策略

1. 在左侧导航栏选择**备份** > **策略中心**，点击**新建备份策略**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972050.png)
2. 输入策略名称 policy-hbr-test，选择备份周期按天备份，备份时间间隔选择 1 小时，备份保留时间选择 3 天，输入新建备份库名称 vault-hbr-test，单击确定。注意：**备份异地复制**：云备份默认使用同地域备份库，若需要使用备份异地复制，将会产生镜像备份库的存储费用（支持资源包抵扣和按量付费）和跨地域复制的流量费用（只支持按量付费），详见[价格详情](https://www.aliyun.com/price/detail/hbr)。**数据库加密方式**：云备份提供[KMS加密](https://help.aliyun.com/zh/cloud-backup/user-guide/use-kms-encryption)功能。通过KMS加密后的备份库，在进行备份恢复时需要目标恢复环境中必须存在并且能够访问用于加密该备份数据的KMS密钥。这意味着，如果KMS密钥被禁用或删除，备份数据将无法恢复![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972051.png)
3. 完成后，可在左侧导航**栏策略中心**查看备份策略，**存储库管理**查看备份库![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972052.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972053.png)

#### 数据备份

##### ECS 文件备份

1. 在左侧导航栏选择**备份** > **ECS 文件备份**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972056.png)
2. 如果之前未授权的话，会弹出授权提示。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972054.png)
3. 同意授权后，在 ECS 资产列表中找到需要备份的 ECS实例，点击**备份**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972055.png)
4. 创建备份计划。如无备份策略，可点击**新建策略**按照[创建备份策略](#kiVRj)步骤进行创建。选择创建好的备份策略，点击**确定**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972062.png)
5. 步骤4 返回 ECS 文件备份列表页面，进入**备份计划**，查看等待状态变为已激活。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972057.png)
6. 此后备份计划会按照设定的周期执行，也可以通过点击**更多** > **立即执行**来手动触发。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972063.png)
7. 在**备份任务**中查看任务执行状态，等待备份任务执行完成。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972064.png)

##### NAS 备份

1. 在左侧导航栏选择**备份** > **NAS 备份**
2. 如果之前未授权的话，会弹出授权提示。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972058.png)
3. 同意授权后，选择**阿里云NAS**，点击**创建备份计划**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972065.png)
4. 选择要备份的**文件系统**，点击**立即转为付费使用**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972059.png)
5. 选择需要备份的文件路径，备份文件规则，及创建好的备份策略。如无备份策略，可点击**新建策略**按照[创建备份策略](#kiVRj)步骤进行创建。点击**确定**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972066.png)NAS为单AZ架构，默认采用同地域备份方式；也可以通过选择异地备份策略，来实现NAS的跨地域备份。
6. 之后备份任务会根据设置的备份计划定时执行，也可以通过**更多** > **立即执行**，来手动触发备份计划。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972060.png)此时备份任务状态为**执行中**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972070.png)等待备份任务完成后，状态变为**完成**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972061.png)

##### OSS 备份

1. 在左侧导航栏选择**备份** > **OSS 备份**，单击**创建备份计划**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972072.png)
2. 选择要备份的 **Bucket**，点击**立即转为付费使用**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972073.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972075.png)
3. 如无备份策略，可点击**新建策略**按照[创建备份策略](#kiVRj)步骤进行创建。选择创建好的备份策略，点击**确定**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972068.png)此时备份计划的状态为**计划中**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972076.png)
4. 点击**更多** > **立即执行**，来执行备份计划。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972067.png)此时备份任务状态为**执行中**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972077.png)等待备份任务完成后，状态变为**完成**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972078.png)

##### ECS 自建数据库备份

云备份暂不支持部署在 Windows 中的 MySQL 数据库。更多信息，请参见[兼容系统列表和使用限制](https://help.aliyun.com/zh/cloud-backup/user-guide/ecs-hosted-database-overview)。

本方案以部署在 Linux 中的 Mysql 数据库为例，实施步骤如下：

1. 在左侧导航栏，选择**备份** > **数据库备份**。左上角选择可用区 华东 1（杭州）> 点击 MySQL > 点击注册数据库实例。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972069.png)
2. 在选择数据库实例页签，系统会自动加载该地域的所有数据库资源。选择目标MySQL 数据库，点击**下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972079.png)选择 MySQL 实例后，需要在配置认证信息页面填写用于登录 MySQL 数据库的用户名和密码 → 点击**确定**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972080.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972071.png)片刻后，MySQL 数据库实例注册成功，在数据库实例页签，可以查看实例的注册信息及状态。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972081.png)
3. 注册 MySQL 实例后，可以通过预检功能提前发现不适合备份的场景，避免发生备份失败等异常问题。详细条件参考：[MySQL 5.7、8.0自建数据库全量上云](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance)点击 **预检**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972074.png)点击 **开始检查**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972082.png)确认检查全部通过![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972083.png)
4. 创建备份任务。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972084.png)
5. 选择数据库实例 -> 点击 **下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972085.png)
6. 新建备份计划：按天做全量备份，按小时做增量备份，点击 下一步。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972087.png)
7. 备份选项保持默认，点击 **下一步**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972086.png)
8. 选择备份库。本最佳实践选择新建备份库。如果已创建备份库，可以单击 选择备份库，从备份库名称列表中，选择已创建的备份库。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972088.png)
9. 点击 **确**认 后，全量备份和增量备份任务创建成功。
10. 点击 **立即执行** 执行一次全量备份。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972089.png)

#### 备份恢复

以OSS为例

1. 打开**恢复任务**页签，并点击**创建恢复任务**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972091.png)
2. 选择备份库、待恢复的 Bucket，选择可用恢复的备份内容，单击下一步，选择。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972092.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972093.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972090.png)
3. 在恢复任务中查看任务状态，并等待任务完成。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972094.png)

#### 备份恢复及测试

以ECS文件为列

1. 查看原文件 MD5 值![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972095.png)
2. 按照 [ECS 文件备份](#G8mSR)步骤进行备份![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972096.png)
3. 修改 ECS 文件内容并记录新的 MD5 值![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972097.png)
4. 在备份计划里找到备份的 ECS，单击左侧的+号，选择最近的还原点。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972099.png)
5. 新建恢复任务。说明：如果要恢复到其它 ECS，可以选择从其他 ECS 恢复。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972098.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7976581571/p972100.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972102.png)
6. 在恢复任务中查看任务状态，并等待任务完成。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972103.png)
7. 再次查看 ECS 实例中测试文件的 MD5 值是否与修改前一致。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6976581571/p972101.png)

## 故障排除

### 为什么无法开通云备份？

可能有如下两个原因：

- 当前账号没有进行企业实名认证。关于企业实名认证，请参见[企业实名认证](https://help.aliyun.com/zh/account/verify-your-identity-enterprise-account/)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-265（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
