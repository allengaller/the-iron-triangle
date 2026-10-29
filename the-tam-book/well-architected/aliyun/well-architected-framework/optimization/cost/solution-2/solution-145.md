<!-- source: https://help.aliyun.com/zh/well-architected/solution-145 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929442 -->

# 闲置资源治理方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972487.png)

企业用户在云上资源生命周期管理过程中通常存在创建测试资源、资源申请误操作、资源申请过多、应用下线等情况，无法完全精细化管理资源可能会造成云资源未及时释放或未及时使用，从而产生闲置资源。闲置资源会产生不必要的费用，本文指导用户快速发现多账号场景下EIP、NAT网关、云盘、ALB、ECS、ACR等闲置资源，对闲置资源进行治理，从而减少云资源浪费、节省云上成本。

## 方案优势

### 闲置资源快速发现及成本节省

本方案能够指导用户及时发现常见的闲置云资源，并对闲置资源进行治理，通过释放无用云资源或对闲置资源重新利用来减少浪费，为企业用户提升资源利用率、节省云上成本。

## 客户场景

### 通过闲置资源治理优化云上成本

#### 场景描述

云上资源生命周期管理过程中做完全精细化管理是企业用户在管云过程中面临的挑战之一，用户在创建测试资源、误申请资源、资源申请过多、应用资源下线等情况下，可能会产生未及时释放或未及时使用的闲置资源，造成资源浪费并增加费用成本。

#### 适用客户

对闲置资源进行治理及成本优化有诉求的企业客户。

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972475.png)

方案目前通过配置审计、监控、控制台、API等方式，帮助用户检测及发现未绑定的EIP、无EIP的共享带宽包、闲置NAT网关、闲置ALB、闲置云盘等闲置资源，发现后用户可根据实际情况对其进行释放或重新使用。支持的闲置资源治理说明如下：

| **闲置资源** | **闲置判断标准** | **建议发现方式** | **处理建议** |
| --- | --- | --- | --- |
| 弹性公网IP | 购买7天后，EIP未绑定资源实例，如ECS实例、CLB实例、NAT网关实例及弹性网卡实例 | 配置审计 | 绑定资源实例释放资源（按量付费） |
| 共享带宽 | 购买7天后共享带宽中未添加任何EIP | 配置审计 | 添加EIP释放资源（按量付费） |
| 应用型负载均衡ALB | 购买7天后：未配置监听或已有监听但所有监听状态为“已停止”或已有监听但对应的所有转发规则对应的服务器组中无后端服务器 | 配置审计 | 启用监听添加后端服务器释放资源（按量付费） |
| 传统型负载均衡CLB | 购买7天后：未配置监听或已有监听但所有监听状态为“已停止” | 配置审计 | 启用监听释放资源（按量付费） |
| 公网NAT网关 | 购买7天后：NAT网关未绑定EIP或绑定了EIP但未设置SNAT及DNAT条目 | 配置审计 | 绑定EIP、设置SNAT或DNAT条目释放资源（按量付费） |
| VPC NAT网关 | 购买7天后，NAT网关未设置SNAT及DNAT条目 | 配置审计 | 设置SNAT及DNAT条目释放资源（按量付费） |
| VPN网关 | 购买7天后：VPN网关未配置目的路由且未配置策略路由且未开启路由自动传播 | 配置审计 | 配置并使用VPN网关 |
| 转发路由器CEN-TR | 购买7天后，转发路由器无网络实例连接：无VPC连接且无VBR连接且无VPN连接 | 产品控制台 | 添加网络实例连接释放资源（按量付费） |
| 云盘 | 购买7天后，云盘未挂载到ECS实例，云盘为待挂载状态 | 配置审计 | 挂载到ECS实例释放资源（按量付费） |
| 文件存储NAS | 购买7天后，NAS文件系统未添加挂载点 | 配置审计 | 添加挂载点并使用资源释放资源（按量付费） |
| 容器镜像服务 | 购买7天后：容器镜像实例未创建命名空间或未创建镜像仓库 | 配置审计 | 创建命名空间及仓库，使用资源 |
| ECS预留实例券 | 购买7天后，预留实例券未匹配ECS实例 | 产品控制台 | 调整实例券使其匹配ECS创建能够匹配实例券的ECS |
| 云服务器ECS | 购买7天后，过去7天ECS实例CPU平均利用率低于3% | 云监控产品控制台 | 使用ECS部署应用释放资源（按量付费） |
| 云数据库RDS | 购买7天后，过去7天RDS实例平均连接数小于1或连接利用率小于0.1% | 云监控产品控制台 | 重新使用该实例释放资源（按量付费） |

说明：上述判断标准中的购买天数请根据实际情况进行调整。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 弹性公网IP | [弹性公网IP](https://help.aliyun.com/zh/eip/product-overview/what-is-eip)（Elastic IP Address，简称EIP）是可以独立购买和持有的公网IP地址资源。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/eip/product-overview/billing)。 |
| 共享带宽包 | [共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/product-overview/what-is-internet-shared-bandwidth)提供地域级带宽共享和复用功能。创建共享带宽实例后，您可以将同地域下的弹性公网IP（EIP）添加到共享带宽实例中，复用共享带宽中的带宽，节省公网带宽使用成本。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/internet-shared-bandwidth/product-overview/pricing/)。 |
| 应用型负载均衡ALB | [应用型负载均衡ALB](https://help.aliyun.com/zh/slb/application-load-balancer/what-is-alb)（Application Load Balancer）是阿里云推出的专门面向HTTP、HTTPS和QUIC等应用层负载场景的负载均衡服务，具备超强弹性及大规模应用层流量处理能力 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/slb/alb-billing/)。 |
| NAT网关 | [NAT网关](https://help.aliyun.com/zh/nat-gateway/product-overview/what-is-nat-gateway)（NAT Gateway）是一种网络地址转换服务，提供NAT代理（SNAT和DNAT）能力。阿里云NAT网关分为公网NAT网关和VPC NAT网关。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/nat-gateway/pricing/)。 |
| 云盘 | [云盘](https://help.aliyun.com/zh/ecs/user-guide/disks-2)是阿里云为云服务器ECS提供的数据块级别的块存储产品，具有低时延、高性能、持久性、高可靠等特点。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/user-guide/disks-2)。 |
| 云服务器ECS | [云服务器ECS](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)（Elastic Compute Service）是阿里云提供的性能卓越、稳定可靠、弹性扩展的IaaS（Infrastructure as a Service）级别云计算服务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| ECS预留实例券 | [预留实例券](https://help.aliyun.com/zh/ecs/user-guide/overview-6)是一种抵扣券，可以抵扣按量付费实例（不含抢占式实例）的账单，也能够预留实例资源。相比包年包月实例，预留实例券与按量付费实例这种组合模式可以兼顾灵活性和成本。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/reserved-instances)。 |
| 云数据库RDS | [阿里云关系型数据库RDS](https://help.aliyun.com/zh/rds/product-overview/what-is-apsaradb-rds-what-is-apsaradb-rds)（Relational Database Service）是一种稳定可靠、可弹性伸缩的在线数据库服务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/rds/product-overview/billing-1/)。 |
| 配置审计Config | [配置审计](https://help.aliyun.com/zh/document_detail/127388.html)（Config）是一项资源审计服务，为您提供面向资源的配置历史追踪、配置合规审计等能力。面对大量资源，帮您轻松实现基础设施的自主监管，确保持续性合规 | 公测免费，详情参见[计费说明](https://help.aliyun.com/zh/document_detail/133951.html)。 |
| 云监控 | [云监控](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/what-is-cloudmonitor)（CloudMonitor）是一项针对阿里云资源和互联网应用进行监控的服务。云监控为云上用户提供开箱即用的企业级开放型一站式监控解决方案 | 部分收费，详情参见[产品计费](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 委派管理员账号 | 资源目录的管理账号可以将资源目录中的成员设置为可信服务的[委派管理员账号](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/manage-a-delegated-administrator-account)。设置成功后，委派管理员账号将获得管理账号的授权，可以在对应可信服务中访问资源目录组织和成员信息，并在该组织范围内进行业务管理。 |

## 安全性

### 闲置资源释放风险

资源释放存在**业务风险，**发现闲置资源后若需要对闲置资源执行释放，请务必**根据企业实际情况确认资源可以执行释放**，包括但不限于与资源责任人确认、确认影响范围、确保数据已迁移等，确认无风险后再执行释放操作。

## 注意事项

- 请阅读并了解安全性章节中的资源释放风险。
- 使用在用户中心-成本管理-成本优化中使用资源智能水位分析功能会产生一定费用，该费用由云监控收取，与资源实例个数、统计天数及报表个数有关，详情参见[智能水位分析计费](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/resource-usage-report)。

## 实施步骤

### 实施准备

- 已阅读方案架构及注意事项章节，了解操作影响面及可能的风险。
- 已开通[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)、[配置审计](https://help.aliyun.com/zh/document_detail/127388.html)及[云监控](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/what-is-cloudmonitor)，已使用资源目录对多账号进行管理。
- 已[为云监控添加委派管理员账号](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/add-a-delegated-administrator-account-for-cloudmonitor)。
- 如果要使用API与企业CMP对接查询闲置资源，需已拥有[Python](https://www.python.org/)运行环境，本方案中使用Python版本为3.9.7。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：30分钟。

### 操作步骤

根据方案架构中的闲置资源发现方式，结合企业实际情况选择下述优化项进行具体操作**，**建议优先使用配置审计从资源配置角度快速发现闲置资源，ECS、RDS等负载类使用资源监控发现闲置资源，其次再使用云产品控制台。

#### 使用配置审计发现闲置资源

##### 新建账号组

使用企业管理账号或委派管理员账号登录[配置审计控制台](https://config.console.aliyun.com/aggregators?MaxResults=100)，新建**全局账号组**。详细操作步骤请参考[新建账号组](https://help.aliyun.com/zh/document_detail/211207.html)。

**注意：若已有全局账号组请跳过该步骤。**

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972476.png)

##### 启用闲置检测合规包

1. 在配置审计控制台选择“合规包”菜单，选择新建的全局账号组**，单击启用合规包，**填写合规包信息后单击下一步。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972490.png)
2. 在合规包模版中选择“**资源空闲检测最佳实践**”，支持的资源类型详情参见控制台规则列表。对规则进行批量勾选规则，单击下一步。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972477.png)
3. 根据实际情况选择是否要调整购买天数判断参数（默认7天），单击完成。

##### 查看检测结果

1. 在合规包页面单击合规包详情查看是否存在闲置资源。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972478.png)
2. 单击资源ID可查看详情。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972491.png)

#### 使用API发现闲置资源

**说明：除有API对接需求的情况外，优先推荐使用上述配置审计的方式发现闲置资源。已使用配置审计发现闲置资源可跳过本步骤**。

本步骤使用Python代码调用OpenAPI查询EIP、共享带宽、ALB、NAT网关、云盘、预留实例券等闲置资源信息。

##### 创建RAM用户、角色并授权

1. 登录企业管理账号[RAM控制台](https://ram.console.aliyun.com/users)创建RAM用户，不启用控制台访问、启用OpenAPI调用访问，生成AccessKey并**妥善保存**，详情参见[创建RAM用户](https://help.aliyun.com/zh/ram/user-guide/create-a-ram-user)。
2. 为RAM用户授予`AliyunSTSAssumeRoleAccess`权限，详情参见[为RAM用户授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-the-ram-user)。
3. 新建RAM角色`readOnly`，授予`ReadOnlyAccess`权限，详情参见[创建RAM角色](https://help.aliyun.com/zh/ram/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account)及[为RAM角色授权](https://help.aliyun.com/zh/ram/user-guide/grant-permissions-to-a-ram-role)。

##### 运行环境准备

执行下列命令完成OpenAPI相关Python包安装。

```
pip install alibabacloud_tea_util
pip install alibabacloud_tea_openapi
pip install alibabacloud_sts20150401
pip install alibabacloud_vpc20160428
pip install alibabacloud_alb20200616
pip install alibabacloud_bssopenapi20171214
pip install alibabacloud_ecs20140526
```

##### 下载代码并进行配置

1. 下载[多账号闲置资源查询示例代码](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/finance/idle_resource.py)。
2. 配置代码中的AccessKey、企业管理账号UID、要查询闲置资源的成员账号UID以及要查询的地域ID。

```
rd_management_account_access_key_id = 'yourAccessKeyId'
rd_management_account_access_key_secret = 'yourAccessKeySecret'
rd_management_account_readonly_role_name = 'readOnly'
rd_management_account_id = 'yourRdManagementAccountId'
rd_member_account_id_list = ['yourRdMemberAccountId', 'yourRdMemberAccountId']
region_id_list = ['cn-shanghai', 'cn-xxx']
```

##### 运行代码

在命令行执行命令`python3 idle_resource.py`，查看闲置资源信息及闲置原因。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972479.png)

#### 使用云产品控制台发现闲置资源

##### 转发路由器

登录[云企业网控制台](https://cen.console.aliyun.com/cen/list)，单击云企业网实例ID查看详情，单击转发路由器ID查看地域内连接详情，若无实例连接则为闲置转发路由器。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972480.png)

##### ECS预留实例券

登录[预留实例券控制台](https://usercenter2.aliyun.com/ri/use-statistics?excludeCodes%5B0%5D=ecsRi&excludeCodes%5B1%5D=scu_bag&excludeCodes%5B2%5D=polardb_cu_public_cn&commodityCode=ecsRi)，选择时间规格查看资源，[使用率](https://help.aliyun.com/zh/user-center/usage-overview)为0%则为闲置预留实例券。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972481.png)

#### 使用监控发现闲置ECS、RDS

##### 方式一：通过成本管理中的智能水位分析发现闲置资源

**多账号或大量资源场景**建议使用该方法获取闲置实例信息。

注意：

1. 使用云监控提供的资源智能水位分析会产生一定费用，费用与资源实例个数、天数及报表个数有关，详情参见[智能水位分析计费](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/resource-usage-report)。
2. 若站点中不支持下文的成本优化控制台，可直接使用云监控智能水位分析功能，操作详情参见[管理智能水位分析报表](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/manage-resource-usage-reports/)。
3. 登录成本管理-[成本优化控制台](https://usercenter2.aliyun.com/expense-manage/cost-recommend/list)，在优化分析中选择**智能水位分析**，单击**查看详情、开通服务**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972482.png)
4. 在[资源使用优化-智能水位分析](https://usercenter2.aliyun.com/expense-manage/cost-recommend/detail-monitor)页面单击**创建/查看更多报告，**单击**创建分析任务。**选择**单次**任务，选择要获取实例的资源使用监控数据时间范围，本示例选择当前时间前7天（根据实际情况调整），选择ECS及RDS产品，单击确定。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972492.png)
5. 任务运行需要一段时间，查看所有报表可看到任务状态。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972483.png)
6. 任务运行完成后单击**下载最新详细报表，**查看资源水位情况，参考方案架构中的ECS CPU利用率及RDS连接使用率发现闲置资源。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972493.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972484.png)

##### 方式二：使用基础监控判断闲置

该方式相对繁琐，若**不涉及多账号、不想使用云监控智能水位分析、仅少量资源**等情况才使用该方式。

1. 使用每个账号下的云监控控制台，ECS可以到在云监控[主机监控](https://cloudmonitornext.console.aliyun.com/hostMonitoring/all)、RDS可以在云监控[云产品监控](https://cloudmonitornext.console.aliyun.com/productListNav/acs_rds_dashboard/rds/cn-shanghai)页面查看每个实例的监控信息判断是否为闲置。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972485.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972486.png)
2. 使用每个账号下的云产品控制台，ECS可以到在[产品控制台](https://ecs.console.aliyun.com/?spm=5176.12818093.top-nav.147.5adc16d0WqxJjH#/server/region/cn-shanghai)选择地域及相应实例单击监控按钮查看CPU监控数据，RDS可以在[产品控制台](https://rdsnext.console.aliyun.com/rdsList/cn-shanghai/basic)选择地域及相应实例详情-**监控与报警**查看会话监控数据，判断是否为闲置。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972494.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972489.png)

#### 使用或释放闲置资源

##### 弹性公网IP

与相关责任人确认EIP是否继续使用，若继续使用可对其进行[资源实例绑定](https://help.aliyun.com/zh/eip/associate-an-eip-with-a-cloud-instance/)，若确认不再使用且EIP为按量付费可对其进行[释放](https://help.aliyun.com/zh/eip/release-an-eip)。

##### 共享带宽包

与相关责任人确认实例是否继续使用，若继续使用可点击**添加IP**将EIP加入共享带宽中，若确认不再使用且为按量付费类型可**删除共享带宽**。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972488.png)

##### 应用型负载均衡ALB

与相关责任人确认实例是否继续使用，若继续使用可为ALB实例配置[监听](https://help.aliyun.com/zh/document_detail/198569.html)，转发服务器组中无服务器的向其中[添加后端服务器](https://help.aliyun.com/zh/slb/application-load-balancer/create-and-manage-a-server-group)，若确认不再使用可[释放实例](https://help.aliyun.com/zh/slb/manage-alb-instances)。

##### NAT网关

与相关责任人确认实例是否继续使用，若继续使用可对NAT网关进行配置，否则按量付费实例可进行释放。

- 公网NAT网关**：**参考步骤[绑定EIP](https://help.aliyun.com/zh/nat-gateway/getting-started/use-the-snat-feature-of-an-internet-nat-gateway-to-access-the-internet)、[创建SNAT条目](https://help.aliyun.com/zh/nat-gateway/create-a-snat-entry)、[创建DNAT条目](https://help.aliyun.com/zh/nat-gateway/create-a-dnat-entry)及[删除实例](https://help.aliyun.com/zh/nat-gateway/user-guide/use-internet-nat-gateway-for-public-network-access)。
- VPC NAT网关：参考步骤[创建SNAT条目](https://help.aliyun.com/zh/document_detail/270909.html)、[创建DNAT条目](https://help.aliyun.com/zh/document_detail/270910.html)及[删除实例](https://help.aliyun.com/zh/nat-gateway/user-guide/create-and-manage-a-vpc-nat-gateway)。

##### 云盘

与相关责任人确认云盘是否继续使用，若继续使用将数据盘其[挂载到ECS实例](https://help.aliyun.com/zh/ecs/user-guide/attach-a-data-disk)，若云盘为按量付费、确认不再使用、且云盘上无有效数据再[释放云盘](https://help.aliyun.com/zh/ecs/user-guide/release-a-disk)，如需数据备份可参考[创建云盘快照](https://help.aliyun.com/zh/ecs/user-guide/create-a-snapshot)。

##### 转发路由器

与相关责任人确认转发路由器是否继续使用，若继续使用请创建[网络实例连接](https://help.aliyun.com/zh/cen/user-guide/manage-network-instance-connections/)，若不在使用请[删除转发路由器实例](https://help.aliyun.com/zh/cen/user-guide/transit-routers)。

##### ECS预留实例券

根据使用ECS的实际使用情况，将**可用区级预留实例券**进行合并或拆分，使其规格满足ECS实例抵扣条件，避免实例券闲置浪费。例如企业已使用了`ecs.g7 4 vCPU/16 GiB`的ECS实例，可以将两张闲置的`ecs.g7 2 vCPU/8 GiB`实例券进行合并，使合并后的实例券满足抵扣条件，避免实例券闲置浪费。匹配规则详情参见[预留实例券与实例的匹配](https://help.aliyun.com/zh/ecs/match-between-reserved-instances-and-pay-as-you-go-instances)，合并拆分详细信息请参见[拆分预留实例券](https://help.aliyun.com/zh/ecs/split-merge-or-modify-reserved-instances)和[合并预留实例券](https://help.aliyun.com/zh/ecs/user-guide/merge-reserved-instances)。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9486581571/p972495.png)

若不满足预留实例券拆分、合并条件，根据实际情况可考虑创建与实例券相匹配的ECS实例供需要的应用使用，避免实例券闲置情况出现。

##### ECS、RDS实例

与相关责任人确认RDS及ECS实例是否为闲置实例，若ECS实例为按量付费且确认不再继续使用可[释放实例](https://help.aliyun.com/zh/ecs/user-guide/release-an-instance)，若RDS实例不再继续使用可[释放实例](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/release-or-unsubscribe-from-an-instance)。

注意：请详细阅读相应释放实例文档中的注意事项，确认是否存在有效数据、做好数据备份。

## 源代码

- **代码说明**：使用Python代码调用OpenAPI，快速查询使用资源目录管理的多账号场景下**EIP、共享带宽、ALB、NAT网关、云盘、预留实例券等闲置资源**。
- **代码地址**：[多账号闲置资源查询](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/finance/idle_resource.py)。

## 故障排除

### 预留实例券的匹配规则是怎样的？

详情参见[预留实例券与实例的匹配](https://help.aliyun.com/zh/ecs/match-between-reserved-instances-and-pay-as-you-go-instances)。

### 预留实例券可以退款吗？

**以下情况下，您可以申请退款：**

- 购买预留实例券的五天内，可以申请无理由退款。**说明** 每个阿里云账号每年只有一次五天无理由退款的机会。例如，您同时购买了一台ECS实例和一张预留实例券，如果ECS实例无理由退款，则同年内无法再申请预留实例券无理由退款。
- 拆分、合并预留实例券或者调整预留实例券范围后，目标地域或可用区下的实例资源库存不足。

详情参见[官网说明](https://help.aliyun.com/zh/ecs/user-guide/instance-faq/)。

## 相关内容

- [配置审计快速入门](https://help.aliyun.com/zh/document_detail/127375.html)
- [资源使用优化-资源使用分析](https://help.aliyun.com/zh/user-center/analysis-on-resource-usage-for-optimization)
- [云产品监控项指标](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/support/appendix-1-metrics)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-145（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
