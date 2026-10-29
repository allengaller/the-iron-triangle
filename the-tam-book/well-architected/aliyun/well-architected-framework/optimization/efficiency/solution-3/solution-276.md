<!-- source: https://help.aliyun.com/zh/well-architected/solution-276 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929395 -->

# 通过资源中心实现云上资源配置同步到企业CMDB

本文将指导企业用户在云上IT架构下，一站式地采集全量资源配置数据，持续获取云上资源配置变更数据，将这些数据稳妥留存并快捷消费到自有的CMDB（Configuration Management Database，配置管理数据库）平台，加快企业自有CMDB的构建和及时更新。

## 应用场景

### 适用场景

- 企业自建CMDB平台或使用第三方CMDB平台用于资源管理或面向应用的运维管理。
- 企业日常的资源管理运维中依赖资源配置数据。例如：获取所有云上资源列表和资源配置进行资产盘点、资源变更前或发生故障后盘点资源关系以确定影响范围等。

### 适用用户

- 研发能力较强的大型企业用户，基于OpenAPI搭建了企业内部的运维平台。
- CMP（Cloud Management Platform，云管理平台）云管服务提供商。为用户提供多云、混合云定制化的管理服务，隐藏各个云厂商的差异性，需统一管理调度各个云上的IT资源和应用。

## 解决方案

### 方案架构

本方案使用[资源中心](https://help.aliyun.com/zh/resource-management/resource-center/product-overview/resource-center-overview)统一收集跨账号、跨产品、跨地域的云上全局资源配置，并通过资源中心的相关产品能力，同步全量资源配置信息构建企业CMDB，持续获取资源配置变更事件确保CMDB内资源配置数据的实时性。

当您只有一个阿里云账号时，您可以直接使用资源中心同步单账号资源配置数据到企业CMDB。当您有多个阿里云账号时，推荐您先使用[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)搭建企业的多账号组织结构，然后在资源目录中指定一个成员作为[资源中心委派管理员账号](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/manage-the-delegated-administrator-account-of-resource-center)管理资源中心，资源中心将会收集资源目录下所有成员的云上资源配置数据。

使用资源中心的资源搜索或资源定时快照投递功能，可以方便快捷地构建云上全量资源数据。同时，设置资源配置变更事件投递后，可以实时监听并消费云上资源配置变更事件，实现对CMDB资源配置的持续更新。

当获取到资源中心的元数据后，您可以根据企业内部CMDB的资源定义进行元数据映射，按照资源的归属账号以及标签确定资源和应用的关系，按照企业自身情况实现资源分析以及可视化展示。

![图片2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3158175471/p947203.jpg)

### 方案优势

- **云上全局资源配置统一获取**。资源中心提供跨账号、跨产品、跨地域的云上全局资源统一视图及资源搜索与资源投递能力，通过资源中心可以实现云上全局资源配置统一获取。同时，支持基于资源目录的多账号管理能力，通过资源目录管理账号或资源中心委派管理员账号，统一获取资源目录下全部成员的资源配置数据。而传统模式下，您需要针对不同云产品分别对接OpenAPI获取各产品、各地域下的资源配置信息，开发及维护成本高。并且在企业多账号场景下，资源分散在多个独立账号中，更增加了获取资源配置信息的复杂度。本方案基于资源中心实现云上全局资源配置统一获取，省去您对接多款云产品OpenAPI的复杂度和开发工作量，更加高效便捷地同步云上资源至企业CMDB。
- **近实时资源同步，保障CMDB一致性。**资源中心支持资源投递功能，每日定时投递全量资源快照到对象存储（OSS）、近实时投递资源配置变更事件到日志服务（SLS）中。您通过在对象存储（OSS）或日志服务（SLS）中消费标准化的资源数据，进行云上资源备份，同时近实时感知云上资源配置变更并及时更新企业CMDB。而传统轮询OpenAPI的模式下，您需要部署监听程序或频繁调用OpenAPI检查才能获取到资源配置变更数据，成本较高且实时性较差。本方案基于资源中心的资源投递能力可持续、近实时获取云上资源配置变更事件，保障CMDB与云上资源的数据一致性。

### 安全性

资源中心通过调用各个云产品的OpenAPI全量构建资源配置信息，以及通过监听操作审计事件近实时触发增量构建，持续发现和构建目标账号下的资源配置信息。当开通资源中心时，需要您授权同意系统创建一个名为AliyunServiceRoleForResourceMetaCenter服务关联角色，资源中心将使用该角色获取账号内的云资源信息并构建资源中心。更多信息，请参见[资源中心服务关联角色](https://help.aliyun.com/zh/resource-management/security-and-compliance/service-linked-role-for-resource-center#concept-2281154)。

### 产品计费

| **云服务** | **云服务说明** | **产品计费** |
| --- | --- | --- |
| 资源目录 | [资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[计费方式](https://help.aliyun.com/zh/resource-management/product-overview/billing-methods)。 |
| 资源中心 | [资源中心](https://help.aliyun.com/zh/resource-management/resource-center/product-overview/resource-center-overview)提供跨账号、跨产品、跨地域的资源统一视图及资源搜索能力。您可以查看全局资源列表，对云上资源全貌了然于心。您可以基于地域、产品、资源类型、资源ID、资源名称或资源标签作为筛选条件进行资源搜索。 | 免费，详情参见[计费方式](https://help.aliyun.com/zh/resource-management/product-overview/billing-methods)。 |
| 对象存储 | [对象存储（OSS）](https://help.aliyun.com/zh/oss/user-guide/what-is-oss)是一种海量、安全、低成本、高可靠的云存储服务，适合存放任意类型的文件。容量和处理能力弹性扩展，多种存储类型供选择，全面优化存储成本。 | 收费，详情参见[计费概述](https://help.aliyun.com/zh/oss/billing-overview)。 |
| 日志服务 | [日志服务（SLS）](https://help.aliyun.com/zh/sls/what-is-log-service)是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[计费概述](https://help.aliyun.com/zh/sls/billing-overview)。 |

### 基本概念

| **名称** | **说明** |
| --- | --- |
| 管理账号 | 当企业拥有多个阿里云账号时，您可以使用资源目录搭建企业的多账号组织结构。开通资源目录的阿里云账号就是管理账号，对资源目录、资源夹和成员拥有完全控制权限，可以统一管理成员，统一配置成员身份权限，统一查看成员账单，统一配置审计规则并下发到各成员。 |
| 委派管理员账号 | 资源目录的管理账号可以将资源目录中的成员设置为可信服务的委派管理员账号。设置成功后，委派管理员账号将获得管理账号的授权，可以在对应可信服务中访问资源目录组织和成员信息，并在该组织范围内进行业务管理。 |
| 高级搜索 | 资源中心的高级搜索基于SQL语句查询当前账号和资源目录成员中的资源。高级搜索提供了灵活、实用且免费的资源全局检索能力。您可以使用查询模板快速查询资源，无论是查找特定类型的资源还是进行更复杂的查询，高级搜索都能满足您的要求。 |
| 资源快照 | 资源定时快照是在某个指定时间点对指定范围内所有资源配置的完整副本。本方案将资源定时快照从资源中心投递到OSS的存储空间，实现资源配置的归档存储。 |
| 资源配置变更事件 | 资源配置变更事件是在资源被创建、删除或其属性发生修改时产生的变更事件。您可以将资源配置变更事件从资源中心投递到SLS日志库。 |

### 注意事项

- 初次开通资源中心时，资源中心数据构建和更新通常需要几分钟的时间，在资源量大时可能需要更长的时间，请您耐心等待。
- 支持资源中心的云服务以及资源类型，请参见[支持资源中心的云服务及资源类型](https://help.aliyun.com/zh/resource-management/resource-center/product-overview/services-that-work-with-resource-center)。后续，会持续接入更多云服务及资源类型。若您有新的需求，可以在资源中心控制台的右上角提交反馈。
- 资源中心仅支持搜索和获取当前账号有权限访问的资源，使用RAM用户搜索资源时，该RAM用户除了具备资源中心的相应权限，还需具备所搜资源的权限。更多信息，请参见[RAM用户使用资源中心](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/permissions-for-a-ram-user-to-access-resource-center)。
- 新创建资源后，资源中心预计需要2分钟完成资源同步。如果未搜索到新创建的资源，请耐心等待并尝试重新获取。

## 实施方案

## 将当前账号的资源配置同步到企业CMDB

### 准备工作

- 开通资源中心。具体操作，请参见[开通资源中心](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/activate-resource-center)。
- 开通[对象存储（OSS）](https://oss.console.aliyun.com)和[日志服务（SLS）](https://sls.console.aliyun.com)。
- 建议您在当前阿里云账号下创建一个RAM用户，授予资源中心管理权限和云产品查看权限，担任资源中心管理员，完成下文所述的所有操作。更多信息，请参见[RAM用户使用资源中心](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/permissions-for-a-ram-user-to-access-resource-center)。

### 步骤一：规划云上资源配置的同步范围

对于当前账号，您需要提前规划需要同步的资源类型。

1. 根据[支持资源中心的云服务及资源类型](https://help.aliyun.com/zh/resource-management/resource-center/product-overview/services-that-work-with-resource-center)，结合实际业务确定需要同步的资源类型范围。
2. 在资源中心查看资源的属性列表。
3. 根据企业内部CMDB的资源定义，完成与云上资源定义之间的属性映射。

### 步骤二：初始化资源配置数据

资源中心提供以下几种方式获取资源配置数据，请根据使用场景选择合适的获取方式：

- **资源搜索**：当您仅需要获取资源的基础属性（包括资源名称、资源ID、资源类型、地域等）时，可以使用该方式获取当前账号下的资源配置数据。
- **高级搜索**：当您需要使用更加灵活的搜索条件，例如：查找关联资源、多条件组合查询时，可以使用该方式获取当前账号下的资源配置数据。
- **资源投递**：当您需要一次性获取资源的完整快照或期望定期进行资源备份时，可以使用该方式将资源快照投递到OSS中，然后通过解析资源快照获取当前账号下的资源配置数据。

## 资源搜索

### 控制台操作

请参见[搜索资源](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/search-for-resources-3)。

### SDK操作

1. 在项目中引入[资源中心SDK](https://help.aliyun.com/zh/resource-management/resource-center/developer-reference/overview-of-resource-center-sdks)。
2. 调用API查询资源。[搜索当前账号的资源](https://help.aliyun.com/zh/resource-management/resource-center/developer-reference/api-resourcecenter-2022-12-01-searchresources)：查询当前账号下有权限访问的资源列表，可通过设置一个或多个过滤条件（例如：资源类型）来精确搜索资源。该API将返回搜索范围内的资源列表，仅包含资源的基本属性，例如：资源ID、资源名称、地域等。[查询资源配置](https://help.aliyun.com/zh/resource-management/resource-center/developer-reference/api-resourcecenter-2022-12-01-getresourceconfiguration)：查询当前账号下指定资源的详细配置数据，您需要在请求参数中指定资源所属地域ID、资源类型以及资源ID。

## 高级搜索

### 控制台操作

1. 登录[资源中心控制台](https://resourcemanager.console.aliyun.com/resource-center)。
2. 在左侧导航栏，选择**资源中心** > **高级搜索**。
3. 编写SQL查询语句。您可以在页面左侧选择需要查询的资源类型及对应属性，然后在右侧编写SQL查询语句。更多信息，请参见[高级搜索概述](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/advanced-search-overview)、[SQL基本语法](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/basic-sql-syntax)。如下提供一个示例，将ECS实例和磁盘实例按照ECS实例ID来进行连表查询，并打印相关信息。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3158175471/p948830.png)`SELECT ecs.region_id, ecs.resource_type as "ECS实例类型", ecs.resource_id as "ECS实例ID", ecs.resource_name as "ECS实例名称", ecs.tags as "ECS实例标签", ecs.resource_group_id as "ECS实例资源组ID", disk.resource_id as "磁盘ID", disk.properties ->> 'DiskId' as "磁盘标识", disk.properties ->> 'InstanceId' as "关联实例ID" FROM resources ecs LEFT JOIN resources disk ON ecs.resource_id = disk.properties ->> 'InstanceId' WHERE ecs.resource_type = 'ACS::ECS::Instance' AND ecs.region_id = 'cn-hangzhou' ORDER BY ecs.resource_id, disk.resource_id;`

### SDK操作

1. 在项目中引入[资源中心SDK](https://help.aliyun.com/zh/resource-management/resource-center/developer-reference/overview-of-resource-center-sdks)。
2. 调用API查询资源。[使用SQL查询当前账号的资源](https://help.aliyun.com/zh/resource-management/resource-center/developer-reference/api-resourcecenter-2022-12-01-executesqlquery)：您可以使用上述示例提供的SQL查询语句查询资源列表。

每个用户每5秒钟最多3次请求，超过次数会被限流。另外，对查询数量、查询时间、查询函数等也存在一定限制，详情请参见[使用限制](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/advanced-search-overview#fa6bf27047tj6)。

## 资源投递

目前只支持控制台操作。

1. 创建当前账号资源投递，将资源定时快照从资源中心投递到OSS的存储空间。具体操作，请参见[投递资源定时快照](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/create-resource-delivery#79d583aa4abwz)。
2. 在OSS中查看并下载资源投递数据。具体操作，请参见[查看资源定时快照](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/view-resource-delivery-data#9378bd90cecnz)。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193073271/p817315.png)
3. 参照[资源定时快照的数据结构](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/scheduled-resource-snapshot-data-structure)，解析资源定时快照并获取资源配置数据，完成与企业CMDB资源模型的映射。

### 步骤三：获取增量变更数据

在完成资源配置数据的初始化操作后，可以通过设置资源配置变更数据投递，实时获取增量变更数据，确保企业CMDB资源数据的实时性。

1. 创建当前账号资源投递，将资源配置变更事件从资源中心投递到SLS日志库。由于SLS的限制，对于超过1MB的配置变更事件，SLS会直接丢弃。此时，您可以选择启用大文件投递功能，将其投递到OSS存储空间。具体操作，请参见[投递资源配置变更事件](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/create-resource-delivery#61b2cae6e06t2)。
2. 在SLS中查看资源配置变更事件的投递结果。具体操作，请参见[查看资源配置变更事件](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/view-resource-delivery-data#87f64720cdmcv)。资源配置变更事件的数据结构及示例，请参见[资源配置变更事件的数据结构](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/resource-configuration-change-data-structure)。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193073271/p817354.png)
3. 监听并消费SLS日志。在目标日志库中，单击**消费预览**，查看消费时获取到的SLS Log的数据结构。具体操作，请参见[消费预览](https://help.aliyun.com/zh/sls/consumption-preview)。消费SLS日志。日志服务提供多种消费的方式，请参见[普通消费概述](https://help.aliyun.com/zh/sls/overview-of-real-time-consumption)。例如：您可以通过Java SDK完成日志消费，详情请参见[通过API消费](https://help.aliyun.com/zh/sls/log-consumption-through-java-sdk)。资源变更的日志数据均存储在LogGroupData中，参考消费预览中SLS Log的结构解析LogGroupData，即可获取到数据变更的相关数据。由于变更事件投递顺序的不确定性，建议您在获取到数据变更日志中的accountId、resourceId、regionId及resourceType后，调用资源中心的[搜索当前账号的资源](https://help.aliyun.com/zh/resource-management/resource-center/developer-reference/api-resourcecenter-2022-12-01-searchresources)查询资源的最终状态，并更新到企业CMDB中。

## 将跨账号的资源配置同步到企业CMDB

### 准备工作

- 开通资源目录，并搭建企业的多账号组织结构。具体操作，请参见[开通资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/enable-a-resource-directory)、[创建资源夹](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/create-a-folder)、[创建成员](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/create-a-member)、[邀请阿里云账号加入资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/invite-an-alibaba-cloud-account-to-join-a-resource-directory)。
- 开通资源中心和跨账号搜索功能。具体操作，请参见[开通资源中心](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/activate-resource-center)、[开通跨账号资源搜索](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/enable-cross-account-resource-search)。
- 开通[对象存储（OSS）](https://oss.console.aliyun.com)和[日志服务（SLS）](https://sls.console.aliyun.com)。
- 建议您为资源中心设置一个委派管理员账号，使用该账号完成下文所述的所有操作。具体操作，请参见[管理资源中心委派管理员账号](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/manage-the-delegated-administrator-account-of-resource-center)。

### 步骤一：规划云上资源配置的同步范围

1. 确定需要同步的资源目录成员范围。
2. 确定需要同步的资源类型。根据[支持资源中心的云服务及资源类型](https://help.aliyun.com/zh/resource-management/resource-center/product-overview/services-that-work-with-resource-center)，结合实际业务确定需要获取的资源类型范围。在资源中心查看资源的属性列表。根据企业内部CMDB的资源定义，完成与云上资源定义之间的属性映射。

### 步骤二：初始化资源配置数据

资源中心提供以下几种方式获取资源配置数据，请根据使用场景选择合适的获取方式：

- **跨账号资源搜索**：当您仅需要获取资源的基础属性（包括资源名称、资源ID、资源类型、地域等）时，可以使用该方式获取多账号下的资源配置数据。
- **高级搜索**：当您需要使用更加灵活的搜索条件，例如：查找关联资源、多条件组合查询时，可以使用该方式获取多账号下的资源配置数据。
- **跨账号资源投递**：当您需要一次性获取资源的完整快照或期望定期进行资源备份时，可以使用该方式将资源快照投递到OSS中，然后通过解析资源快照获取多账号下的资源配置数据。

## 跨账号资源搜索

### 控制台操作

请参见[搜索资源](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/search-for-resources-1)。

### SDK操作

1. 在项目中引入[资源中心SDK](https://help.aliyun.com/zh/resource-management/resource-center/developer-reference/overview-of-resource-center-sdks)。
2. 调用API查询资源。[搜索多账号的资源](https://help.aliyun.com/zh/resource-management/resource-center/developer-reference/api-resourcecenter-2022-12-01-searchmultiaccountresources)：按照过滤条件搜索资源目录的管理账号和多个成员账号中的资源。调用时，需在请求参数中指定资源搜索的范围，例如：资源目录ID、资源夹ID、或者成员账号ID。[查询多账号资源配置](https://help.aliyun.com/zh/resource-management/resource-center/developer-reference/api-resourcecenter-2022-12-01-getmultiaccountresourceconfiguration)：查询资源目录的管理账号或者成员账号的资源详细配置数据。调用时，需在请求参数中指定资源所属的账号ID、资源地域ID、资源类型和资源ID。

## 高级搜索

### 控制台操作

1. 登录[资源中心控制台](https://resourcemanager.console.aliyun.com/resource-center)。
2. 在左侧导航栏，选择**资源中心** > **高级搜索**。
3. 设置查询范围为**跨账号**，然后选中需要查询的目录节点。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3158175471/p949038.png)
4. 编写SQL查询语句。您可以在页面左侧选择需要查询的资源类型及对应属性，然后在右侧编写SQL查询语句。更多信息，请参见[高级搜索概述](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/advanced-search-overview)、[SQL基本语法](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/basic-sql-syntax)。如下提供一个示例，将ECS实例和磁盘实例按照ECS实例ID来进行连表查询，并打印相关信息。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3158175471/p949175.png)`SELECT ecs.region_id, ecs.resource_type as "ECS实例类型", ecs.resource_id as "ECS实例ID", ecs.resource_name as "ECS实例名称", ecs.tags as "ECS实例标签", ecs.resource_group_id as "ECS实例资源组ID", disk.resource_id as "磁盘ID", disk.properties ->> 'DiskId' as "磁盘标识", disk.properties ->> 'InstanceId' as "关联实例ID" FROM resources ecs LEFT JOIN resources disk ON ecs.resource_id = disk.properties ->> 'InstanceId' WHERE ecs.resource_type = 'ACS::ECS::Instance' AND ecs.region_id = 'cn-hangzhou' ORDER BY ecs.resource_id, disk.resource_id;`

### SDK操作

1. 在项目中引入[资源中心SDK](https://help.aliyun.com/zh/resource-management/resource-center/developer-reference/overview-of-resource-center-sdks)。
2. 调用API查询资源。[使用SQL查询跨账号的资源](https://help.aliyun.com/zh/resource-management/resource-center/developer-reference/api-resourcecenter-2022-12-01-executemultiaccountsqlquery)：您可以使用上述示例提供的SQL查询语句查询资源列表。

每个用户每5秒钟最多3次请求，超过次数会被限流。另外，对查询数量、查询时间、查询函数等也存在一定限制，详情请参见[使用限制](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/advanced-search-overview#fa6bf27047tj6)。

## 跨账号资源投递

目前只支持控制台操作。

1. 创建跨账号资源投递，将资源定时快照从资源中心投递到OSS的存储空间。具体操作，请参见[投递资源定时快照](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/create-multi-account-resource-delivery#79d583aa4abwz)。
2. 在OSS中查看并下载资源投递数据。具体操作，请参见[查看资源定时快照](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/view-resource-delivery-data#9378bd90cecnz)。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193073271/p817315.png)
3. 参照[资源定时快照的数据结构](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/scheduled-resource-snapshot-data-structure)，解析资源定时快照并获取资源配置数据，完成与企业CMDB资源模型的映射。

### 步骤三：获取增量变更数据

在完成资源配置数据的初始化操作后，可以通过设置资源配置变更数据投递，实时获取增量变更数据，确保企业CMDB资源数据的实时性。

1. 创建跨账号资源投递，将资源配置变更事件从资源中心投递到SLS日志库。由于SLS的限制，对于超过1 MB的配置变更事件，SLS会直接丢弃。此时，您可以选择启用大文件投递功能，将其投递到OSS存储空间。具体操作，请参见[投递资源配置变更事件](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/create-multi-account-resource-delivery#61b2cae6e06t2)。
2. 在SLS中查看资源配置变更事件的投递结果。具体操作，请参见[查看资源配置变更事件](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/view-resource-delivery-data#87f64720cdmcv)。资源配置变更事件的数据结构及示例，请参见[资源配置变更事件的数据结构](https://help.aliyun.com/zh/resource-management/resource-center/user-guide/resource-configuration-change-data-structure)。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193073271/p817354.png)
3. 监听并消费SLS日志。在目标日志库中，单击**消费预览**，查看消费时获取到的SLS Log的数据结构。具体操作，请参见[消费预览](https://help.aliyun.com/zh/sls/consumption-preview)。消费SLS日志。日志服务提供多种消费的方式，请参见[普通消费概述](https://help.aliyun.com/zh/sls/overview-of-real-time-consumption)。例如：您可以通过Java SDK完成日志消费，详情请参见[通过API消费](https://help.aliyun.com/zh/sls/log-consumption-through-java-sdk)。资源变更的日志数据均存储在LogGroupData中，参考消费预览中SLS Log的结构解析LogGroupData，即可获取到数据变更的相关数据。由于变更事件投递顺序的不确定性，建议您在获取到数据变更日志中的accountId、resourceId、regionId及resourceType后，调用资源中心的[搜索多账号的资源](https://help.aliyun.com/zh/resource-management/resource-center/developer-reference/api-resourcecenter-2022-12-01-searchmultiaccountresources)查询资源的最终状态，并更新到企业CMDB中。

## 常见问题

[在资源中心搜索不到资源怎么办？](https://help.aliyun.com/zh/resource-management/resource-center/support/what-if-you-can-t-search-for-resources)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-276（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
