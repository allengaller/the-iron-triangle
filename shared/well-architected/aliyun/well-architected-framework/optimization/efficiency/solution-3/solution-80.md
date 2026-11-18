<!-- source: https://help.aliyun.com/zh/well-architected/solution-80 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929455 -->

# 同步云上配置到企业CMDB

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972698.png)

现今企业大多采用多云架构来部署云上应用，以提升应用的稳定性同时避免被单个云平台捆绑。但多云架构就意味着，没有任何一个云平台的管控体系能完整支持企业的资源管理需求。企业往往自建统一的资源管理平台或使用第三方服务商提供的多云资源管理软件。资源管理平台（CMDB）最重要的是构建完整可靠的底层数据，需要获取各个云平台的所有资源配置数据，对数据进行持续的下载、数据格式抽象统一、数据清洗、资源关系解析和长期留存等处理，用可靠的数据支持基于资源数据构建的运维管理流程和Devops程序。当使用的云平台比较多、使用云产品比较多样、云上部署规模越来越大时，这份自建数据的维护将会消耗巨大的人力和时间成本。

本方案指导企业客户在多账号的云上IT架构下，一站式的采集全量资源配置数据、资源配置历史、资源关系数据，将这些数据稳妥留存并快捷消费到自有的CMDB平台，加快企业自有CMDB的构建。

## 方案优势

### 打通云上资源跟内部CMDB数据

基于配置审计可以持续收集云上资源配置数据，将这份数据跟企业内部CMDB打通，可以解决数据不一致的问题。对于企业维护CMDB数据准确性非常有价值。

### 多账号统一收集资源

配置审计能够解决多账号内全部资源的统一收集，避免了传统需要处理每个账号内资源的繁琐任务。并且支持一键开通，操作成本极低。

## 客户场景

### 自建CMDB平台

#### 场景描述

企业为多云部署，需要自建CMDB平台（资源管理/面向应用的运维管理）或向第三方成品软件上报云上的资源配置数据。企业在内部日常运维中需依赖资源配置数据。如获取所有云上资源列表和资源配置进行资产盘查，如在进行资源变更前或发生故障后盘点资源关系以确定影响范围等。

#### 适用客户

- 研发能力较强的大型企业用户。基于OpenApi搭建了企业内部的运维平台。
- CMP云管服务提供商。为用户提供多云、混合云定制化的管理服务，隐藏各个云厂商的差异性，需统一管理调度各个云上的IT资源和应用。

## 方案架构

### 架构图

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972696.png)

### 关键流程

- 在资源管理账号内开启多账号配置审计服务
- 在配置审计服务中配置统一投递到OSS/MNS/SLS（三者选其一）
- 编写程序代码，监听事件

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 配置审计 | [配置审计](https://help.aliyun.com/product/127306.html)（CloudConfig）是阿里云上的配置管理和IT治理服务。将您分散在各地域的资源整合为全局资源列表，您可以便捷地搜索全局资源。同时帮助您记录云上IT资源的配置变更历史，允许您将全量资源配置和配置历史文件持续收集到指定的存储空间。同时持续自动地评估云上资源配置的合规性，实现云上IT合规治理。 | 配置审计公测期间所有阿里云有效账号均可免费使用。但具体涉及到其他服务，详情计费[参考链接](https://help.aliyun.com/zh/document_detail/133951.html) |
| 日志服务 | [日志服务](https://help.aliyun.com/product/28958.html)(SLS)是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。在该方案中配置审计会把合规扫描后发现的不合规问题以日志方式推送给日志服务，在日志服务中可以进一步消费和分发这些不合规结果信息。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/sls/billing-overview)。 |
| MNS | [消息服务](https://help.aliyun.com/product/27412.html)（MNS）是一种高效、可靠、安全、便捷、可弹性扩展的分布式消息服务。MNS能够帮助应用开发者在他们应用的分布式组件上自由的传递数据、通知消息，构建松耦合系统。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/mns/product-overview/billing-overview) |
| OSS | [对象存储服务](https://help.aliyun.com/zh/oss/user-guide/what-is-oss)（Object Storage Service，OSS）是一种海量、安全、低成本、高可靠的云存储服务，适合存放任意类型的文件。容量和处理能力弹性扩展，多种存储类型供选择，全面优化存储成本。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/oss/billing-overview) |
| 事件总线 | [事件总线](https://help.aliyun.com/product/161886.html)(EventBridge) 是阿里云提供的一款无服务器事件总线服务，支持阿里云服务、自定义应用、SaaS应用以标准化、中心化的方式接入，并能够以标准化的 CloudEvents 1.0 协议在这些应用之间路由事件，帮助您轻松构建松耦合、分布式的事件驱动架构。 | 公测期间免费 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| CMDB | 配置管理数据库。是运维体系的数据基础。它的数据准确性至关重要 |

## 安全性

### 配置审计管理员权限

需要在企业管理主账号中分配操作子用户（RAM）具备配置审计的管理权限。权限点：

| 权限策略名称 | 权限策略说明 |
| --- | --- |
| AliyunConfigFullAccess | 管理配置审计(Config)的权限 |

### 日志服务管理权限

按照Landing Zone的账号架构规范，推荐开设一个日志账号。需要在这个日志账号里面配置相应的操作子用户（RAM）具备管理日志服务权限。权限点：

| 权限策略名称 | 权限策略说明 |
| --- | --- |
| AliyunLogFullAccess | 管理日志服务(SLS)的权限 |

## 注意事项

1. 配置审计目前正在努力覆盖阿里云的云产品和事件，但目前支持的产品和事件类型有限。支持 33款阿里云产品的**资源配置数据**。请持续关注[支持的产品列表](https://help.aliyun.com/zh/document_detail/127411.html)通常情况下，资源配置信息更新会在10分钟内完成，少数情况最长会在T+2完成数据同步。
2. 方案中给出了基于增量变更的数据获取方式，企业可以需要根据自身实际情况进行拓展，这些建立和示例并不确保满足每个企业的所有需求。
3. 配置审计目前为免费产品，但不排除未来企业需要为存储在配置审计中的资源快照付费。
4. 企业目前通过配置审计将资源配置数据投递到指定存储空间不需要花费费用，但您需为账号下存储这些数据的存储空间的用量付费。

## 实施步骤

### 实施准备

#### 1. 确定资源目录中的资源配置数据账号

- 目标账号可以为企业管理账号或资源目录内任一成员账号。方案建议您将一个成员账号设置为专门收集资源配置数据的账号，该账号未来可进一步成为企业CMDB的管理账号，与其他开发和运维账号区分开。

#### 2. 确保用于存储资源配置数据的账号已开通存储产品

- 企业管理账号需确保已启用配置审计服务。
- 如果选择投递到日志服务，确保目标账号中已开通日志服务（SLS）和对象存储（OSS）。
- 如果选择投递到消息服务，确保目标账号中已开通消息服务（MNS）和对象存储（OSS）。

#### 3. 确保资源结构已创建

### 操作步骤

#### 将资源配置信息变更数据投递到日志服务（SLS）

##### step 1. 企业管理账号在配置审计中新建全局账号组

账号组相当于多账号配置管理的管理范围，您可以新建全局账号组或自定义账号组。

- 全局账号组跟企业管理账号创建的资源目录绑定，当资源目录中新增账号或账号删除和移出时，全局账号组会与资源目录联动，同步账号组织。
- 自定义账号组仅感知资源目录中账号的移出，不感知账号的新增。当您的资源目录中新增了成员账号，并且您希望该账号的资源配置也能被统一收集，您需要手动将该账号加入到自定义账号组中。

1. 登录[配置审计控制台](https://config.console.aliyun.com/)。
2. 在左侧导航栏，单击**账号组**。
3. 在**账号组**页面，单击**新建账号组**。
4. 在**新建账号组**页面，先设置账号组名称和描述，再选择**账号组类型**为**全局**。
5. 单击**提交**。在**账号组**列表中，目标账号组的状态为**创建完成**，说明新建全局账号组成功。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972699.png)
6. 点击**“概览”**，选择创建完成的**账号组**，可以查看到企业管理账号以及所有成员账号的资源视图。点击资源视图中的**对应实例**，可以查看实例的详细信息和配置时间线。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972700.png)

##### step 2. 在日志审计账号中新建日志项目（Project）和日志库（Logstore）

1. 日志审计账号登录[日志服务控制台](https://sls.console.aliyun.com/)。
2. 单击**创建Project**。
3. 在**创建Project**页面，设置Project名称和归属地域。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972701.png)
4. 单击**确定**。
5. 在**创建成功**对话框，单击**确认**。
6. 在**创建Logstore**页面，设置Logstore名称，其他参数均保持默认值。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972702.png)
7. 单击**确定**。
8. 在**创建成功**对话框，单击**确认**。最终将在步骤3创建的Project中，存在一个用于存储投递数据的Logstore。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972703.png)

##### step 3. 企业管理账号在配置审计控制台，设置SLS投递并下发合规审计规则 （配置合规审计规则）

> 本步骤使用企业管理账号在配置审计控制台设置SLS投递以及合规审计规则! 注意！这一步需要切换回企业管理账号。

1. 企业管理账号登录[配置审计控制台](https://config.console.aliyun.com/)。
2. 在左侧导航栏，选择**投递服务 > 投递到日志服务SLS**。
3. 在**投递到日志服务SLS**页面，打开**设置日志服务SLS**开关。
4. 选择**选择其他账号已有的日志项目（仅支持企业管理账号）**，设置目标成员账号的日志库ARN和扮演角色ARN。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972704.png)注意！以下选项要全部勾上![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972705.png)配置变更历史：选择了这个可以将资源增/删、改会记录。
5. 单击**确定**，完成将资源变更数据投递到日志库中。
6. 配置审计同时支持**下发资源合规审计规则**。当资源发生变更时/周期性检查，规则会作用于指定的资源类型，评估此次资源变更的结果是否合规。最终，合规评估的结果将会返回配置审计控制台。点击右侧导航栏中的**“规则”**，选中我们刚刚**创建的账号组**，点击**“新建规则”**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972706.png)
7. 可根据业务需求，选择配置审计中的已有**托管规则**，也可以函数计算服务**自定义规则**，需要开通[函数计算服务](https://help.aliyun.com/zh/functioncompute/fc-2-0/product-overview/what-is-function-compute)，如何新建自定义规则详见[链接](https://help.aliyun.com/zh/document_detail/127405.html)。当前文档我们创建**托管规则**，以**“RDS实例IP白名单不是全网段”**规则为例。选择该托管规则，按照步骤新建规则。点击“**提交**”按钮即可下发规则到该账号组下。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972707.png)
8. 【验证】此时我们模拟在**成员账号**中**创建一个RDS**，并且**将RDS的白名单设置为0.0.0.0/0**。此时在**企业管理账号**的“**配置审计**”-“**规则**”-“**CMDB账号组**”中，可以看见**不合规的资源警告**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972709.png)这一步使用日志审计账号，查看资源更改数据是否成功投递到日志库
9. 同时，**新建RDS**的操作将会投递到日志审计账号的指定日志项目的日志库下。为了验证是否成功投递，我们可以在日志审计账号**日志服务下**，点击数据投递到日志库的“**消费预览**”选项，当发生资源配置数据变更时，即可查看到变更数据：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972708.png)

至此，企业管理账号资源目录下的所有账号（包括企业管理账号，在本例中为全部账号）的资源配置信息变更数据，已经投递到日志审计账号的指定日志项目的日志库下。

至此，多账号场景下面的合规审计配置完成。接下来如果企业需要订阅审计事件，请参考以下指导手册。

下面，我们**以ECS资源的网络配置数据**为例，使用python脚本模拟将资源配置数据导入企业自有系统。

#### 获取资源配置数据

该部分分为两步:

第一步使用python脚本**初始化资源**配置，获取当前ECS实例的网络配置数据；

第二步通过python脚本监听SLS日志库，获取**增量变更数据**。

##### step 4. 初始化资源配置数据

使用到了配置审计的API，在使用前需要导入阿里云SDK核心库: [aliyun-python-sdk-core](https://help.aliyun.com/zh/document_detail/67117.html)

- ListAggregateDiscoveredResources：在多账号情况下，列出主账号下指定账号组的所有资源数据
- GetAggregateDiscoveredResource：在多账号情况下，查询指定资源的详细数据

注意：上述两个方法中都需要账号组id（aggregator_id），该参数可以通过ListAggregators查询，该参数不会发送改变，因此可以在代码中指定

```
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from aliyunsdkcore.http import protocol_type
import json

# 使用ListAggregators Api查询全部账号组，用于查询账号组id
def get_aggregators(access_key, secret_key):
    clt = AcsClient(access_key, secret_key, '')
    request = CommonRequest()
    request.set_protocol_type(protocol_type.HTTPS)
    request.set_domain('config.cn-shanghai.aliyuncs.com')
    request.set_version('2020-09-07')
    request.set_action_name('ListAggregators')
    request.set_method('GET')
    # 返回结果的最大数量
    request.add_query_param('MaxResults', 10)
    response = clt.do_action_with_exception(request)
    res = str(response, encoding='utf-8')
    json_res = json.loads(res)
    return json_res['AggregatorsResult']['Aggregators']

# 列出主账号配置审计下指定账号组下的所有ECS资源
def list_resources(access_key, secret_key, aggregator_id):
    clt = AcsClient(access_key, secret_key, '')
    request = CommonRequest()
    request.set_protocol_type(protocol_type.HTTPS)
    request.set_domain('config.cn-shanghai.aliyuncs.com')
    request.set_version('2019-01-08')
    request.set_action_name('ListAggregateDiscoveredResources')
    request.set_method('GET')
    request.add_query_param('PageSize', 50)
    request.add_query_param('PageNumber', 1)
    request.add_query_param('ResourceDeleted', 1)
    # 指定查询ECS资源，可改为其他标签，详见配置审计-API参考官方文档
    request.add_query_param('ResourceTypes', 'ACS::ECS::Instance')
    request.add_query_param('AggregatorId', aggregator_id)
    response = clt.do_action_with_exception(request)
    res = str(response, encoding='utf-8')
    json_res = json.loads(res)
    return json_res['DiscoveredResourceProfiles']['DiscoveredResourceProfileList']

# 在多账号情况下，详细查询指定ECS中的网络配置信息
def describe_resource(access_key, secret_key, region, resource_type, resource_id, aggregator_id, resource_owner_id):
    clt = AcsClient(access_key, secret_key, '')
    request = CommonRequest()
    request.set_protocol_type(protocol_type.HTTPS)
    request.set_domain('config.cn-shanghai.aliyuncs.com')
    request.set_version('2019-01-08')
    request.set_action_name('GetAggregateDiscoveredResource')
    request.set_method('GET')
    request.add_query_param('Region', region)
    request.add_query_param('ResourceType', resource_type)
    request.add_query_param('ResourceId', resource_id)
    # 账号组id
    request.add_query_param('AggregatorId', aggregator_id)
    # ECS资源所属的子账号uid
    request.add_query_param('ResourceOwnerId', resource_owner_id)
    response = clt.do_action_with_exception(request)
    res = str(response, encoding='utf-8')
    json_res = json.loads(res)
    configuration = json.loads(json_res['DiscoveredResourceDetail']['Configuration'])
    # ECS实例网络配置相关信息。
    return \
        {
            'resourceId': configuration['InstanceId'],
            'accountId': resource_owner_id,
            'InstanceNetworkType': configuration['InstanceNetworkType'],
            'InnerIpSet': configuration['InnerIpAddress']['IpAddress'],
            'Eip': configuration['EipAddress']['IpAddress'],
            'VpcIpSet': configuration['VpcAttributes']['PrivateIpAddress']['IpAddress'],
            'PublicIpSet': configuration['PublicIpAddress']['IpAddress'],
            'NetworkInterfaceSet': configuration['NetworkInterfaces']['NetworkInterface']
        }

if __name__ == "__main__":
    # 填写主账号AK, SK
    access_key = ''
    secret_key = ''
    # 填写账号组id，可以通过get_aggregators()方法查询，并选择其中一个id填入
    aggregator_id = 'ca-**********'
    for ecs_instance in list_resources(access_key, secret_key, aggregator_id):
        ecs_net_detail = describe_resource(access_key, secret_key, ecs_instance['Region'], ecs_instance['ResourceType'],
                                           ecs_instance['ResourceId'], aggregator_id, ecs_instance['AccountId'])
        print('归属账号: %s' % ecs_instance['AccountId'])
        print(ecs_net_detail)
```

代码执行完成后，会在控制台打印出当前ECS实例的网络配置信息。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972711.png)

##### step 5. 通过监听SLS投递数据持续监听并处理资源增量变更

通过step4，我们获取到了当前ECS的网络配置，现在我们通过监听SLS服务，获取ECS网络资源配置**变更的数据**。在这里我们使用到了:

- 阿里云Python SDK：[aliyun-python-sdk-core](https://help.aliyun.com/zh/document_detail/67117.html)
- SLS服务Python SDK：[aliyun-log-python-sdk](https://help.aliyun.com/zh/sls/developer-reference/overview-4)

```
# -*- coding: utf-8 -*-

import os
import time
import json
from aliyun.log.consumer import *
from aliyun.log import *

class SampleConsumer(ConsumerProcessorBase):
    shard_id = -1
    last_check_time = 0

    def initialize(self, shard):
        self.shard_id = shard

    def process(self, log_groups, check_point_tracker):
        for log_group in log_groups.LogGroups:
            items = []
            for log in log_group.Logs:
                item = dict()
                item['time'] = log.Time
                for content in log.Contents:
                    item[content.Key] = content.Value
                items.append(item)
            log_items = dict()
            log_items['topic'] = log_group.Topic
            log_items['source'] = log_group.Source
            log_items['logs'] = items
            # 您可以在此实现数据更新逻辑。
            for item in log_items['logs']:
                # 此处只过滤资源类型为ECS实例（ACS::ECS::Instance）的变更消息，您可以根据所需监听其他资源类型的资源。
                if 'resourceType' in item and item['resourceType'] and item['resourceType']=='ACS::ECS::Instance' and 'configuration' in item and item['configuration']:
                    configuration = parse_json(item['configuration'])
                    # ECS实例网络配置相关信息。
                    ecs_net_detail = {
                        'resourceId': configuration['InstanceId'],
                        'InstanceNetworkType': configuration['InstanceNetworkType'],
                        'InnerIpSet': configuration['InnerIpAddress']['IpAddress'],
                        'Eip': configuration['EipAddress']['IpAddress'],
                        'VpcIpSet': configuration['VpcAttributes']['PrivateIpAddress']['IpAddress'],
                        'PublicIpSet': configuration['PublicIpAddress']['IpAddress'],
                        'NetworkInterfaceSet': configuration['NetworkInterfaces']['NetworkInterface']
                    }
                    print(ecs_net_detail)
                    

        current_time = time.time()
        if current_time - self.last_check_time > 3:
            try:
                self.last_check_time = current_time
                check_point_tracker.save_check_point(True)
            except Exception:
                import traceback
                traceback.print_exc()
        else:
            try:
                check_point_tracker.save_check_point(False)
            except Exception:
                import traceback
                traceback.print_exc()

        # None means succesful process
        # if need to roll-back to previous checkpoint，return check_point_tracker.get_check_point()
        return None

    def shutdown(self, check_point_tracker):
        try:
            check_point_tracker.save_check_point(True)
        except Exception:
            import traceback
            traceback.print_exc()

def parse_json(content):
    """
    Json类型转换
    :param content: json字符串
    :return: Json对象
    """
    try:
        return json.loads(content)
    except Exception as e:
        return None

def main():
    # 您的sls的endpoint
    endpoint = 'cn-hangzhou.log.aliyuncs.com'
    # 您的AK/SK
    accessKeyId = ''
    accessKey = ''
    # 您在配置审计设置的日志服务的日志项目名称和日志库名称。
    project = 'config-delivery'
    logstore = 'configuration-history'
    client_worker = None
    try:
        option = LogHubConfig(endpoint, accessKeyId, accessKey, project, logstore, 'g2',
                              'c2', cursor_position=CursorPosition.END_CURSOR, heartbeat_interval=6,
                              data_fetch_interval=1)
        client_worker = ConsumerWorker(SampleConsumer, consumer_option=option)
        print('********start consume********')
        client_worker.start()
    except Exception as ex:
        print(ex)
        print('********end consume********')
        client_worker.shutdown()

if __name__ == '__main__':
    main()
```

运行上述脚本后，python脚本会持续消费SLS日志库，当ECS网络配置信息发生变更时，会将变更数据。

##### step 6. 模拟ECS实例网络配置发生修改

在这我们**模拟ECS实例网络配置修改的操作**，修改成员账号下ECS的私网ip地址，由原本的172.19.xxx.xxx变更为172.19.xxx.aaa，变更后10min内会将结果打印在控制台。可以看到，私网ip地址已经由step4控制台输出中的172.19.xxx.xxx变成了172.19.xxx.aaa。

## 故障排除

### 为什么设置的规则未被评估？

- 如果规则的触发机制为**周期执行**，则需要到固定的时间点才会评估。
- 如果规则的触发机制为**配置变更**，则您绑定规则后，被关联的资源需要发生配置变更才会触发规则。

您可以在规则详情页面，手动触发规则的**重新审计**，快速获得最新评估结果。

## 方案卸载

### 删除配置审计规则

当您不再需要某条规则时，可以对其执行删除操作。删除规则后，其配置信息不再保留。您可以在规则列表中删除新建的规则和合规包中的规则。

企业管理账号可以删除当前账号和所有账号组内成员账号中的规则。

1. 登录[配置审计控制台](https://config.console.aliyun.com/)。
2. 在左侧导航栏，单击**规则**。
3. 在**规则**页面，单击目标账号组页签。
4. 在目标账号组页签，筛选出**已停用**的规则。
5. 删除规则。单个删除单击目标规则对应**操作**列的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972712.png)，选择**删除**。在**确定删除规则？**对话框，单击**删除**。批量删除选中目标规则对应复选框，单击![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7786581571/p972710.png)。在**批量删除**对话框，单击**确定**。
6. 确认规则删除结果。在目标账号组页签，规则已被删除。

### 删除账号组

资源目录中的企业管理账号可以删除账号组。删除账号组后，企业管理账号不能再集中查看该账号组中所有成员账号的资源，企业管理账号在该账号组中新建的规则和合规包也将自动被删除，且不能恢复。该账号组中成员账号自己新建的规则和合规包将会被保留。

删除步骤：

1. 登录[配置审计控制台](https://config.console.aliyun.com/)。
2. 在左侧导航栏，单击**账号组**。
3. 在**账号组**页面，单击目标账号组对应**操作**列的**删除**。
4. 在**删除账号组**对话框，单击**确定**。

### 删除日志服务资源

1. 在Project列表中，单击目标Project对应的**删除**。
2. 在**删除Project**面板中，选择删除原因，然后单击**确定**。

## 相关内容

- 通过MNS通知机制实现不合规资源的自动修复，详情参见[链接](https://help.aliyun.com/zh/document_detail/180962.html)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-80（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
