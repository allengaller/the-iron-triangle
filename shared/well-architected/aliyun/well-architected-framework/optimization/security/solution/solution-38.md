<!-- source: https://help.aliyun.com/zh/well-architected/solution-38 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929416 -->

# 基于操作日志实现业务资源事件关联分析

## 方案概述

本方案以[多账号操作日志统一归集与审计](https://help.aliyun.com/zh/well-architected/solution-37)及资源标签为基础，通过搭建日志处理服务，为操作日志新增具有业务语义的资源标签，向企业提供业务视角的审计日志查询方案。

操作审计支持将日志归集到[日志服务SLS](https://help.aliyun.com/zh/sls/what-is-log-service)，部署日志处理服务对日志消息进行监听消费，对数据清洗过滤后实时处理成用户关注的内容后再次写入SLS，支持生成用户关注的业务审计视图。日志处理过程主要为过滤掉用户不关心的操作事件、查询资源标签，从用户视角重新构建新的操作日志写入SLS，通过SLS的查询分析能力支持按标签查询用户关注的操作记录。

## 方案优势

### 提升审计效率

基于已归集的审计日志和资源标签，产出业务项目视角的审计视图，提升客户的操作日志审计效率和分析体验。

## 客户场景

### 从业务视角对操作日志进行审计

#### 场景描述

企业在内部有多个业务单元或项目，存在资源被多个账号或业务单元共享的场景，多个业务单元或项目用户会对资源有变更操作。现有操作审计日志中能看到的只是事件类型、资源、账号维度的操作记录，不具备业务属性，在进行操作审计日志统计分析的时候缺乏业务视角，无法快速统计用户操作的资源属于什么业务单元、某个项目进行了哪些变更，只能线下手动进行关联，审计操作繁琐且成本高昂。

#### 适用客户

完成操作审计配置，从业务视角对操作审计日志有统计分析诉求的企业客户。

## 客户案例

### 客户背景

某国内公司X为互联网电动汽车知名品牌，专注于针对一线城市年轻人的互联网时尚电动汽车的研发。

### 客户痛点

在一个UID下面，有多个RAM用户，这些用户对资源有变更操作，需要按项目的角度来统计哪些不同项目分别被哪些RAM User操作过，现有操作审计日志无法快速按项目统计。

### 实施方案

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971927.png)

### 客户收益

基于已归集的审计日志和资源标签，产出业务项目视角的审计视图，有效提升用户的操作日志审计效率和审计体验。

## 方案架构

**关键流程：**

- 在企业管理主账号已完成操作审计日志归集到SLS。
- 在相应账号下对关注的资源打标签，使资源具备业务属性。
- 在审计账号SLS创建新LogStore用于业务视角的日志存储，创建RAM用户及AccessKey用于供日志处理服务监听SLS消息、写入新LogStore。
- 在企业管理账号创建只读权限的RAM用户及AccessKey，用于日志处理服务读取所有账号的资源标签。
- 在ECS服务器部署启动Python日志处理服务。
- 日志处理服务对SLS日志消息进行过滤及操作事件处理、获取资源标签，将用户关注字段写入新LogStore。
- 在日志审计账号对新LogStore构建业务查询视图。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 资源标签 | [标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview)是云资源的标识，可以帮助您从不同维度对具有相同特征的云资源进行分类、搜索和聚合，让资源管理变得更加轻松。 | 免费，详情参见[计费方式](https://help.aliyun.com/zh/resource-management/product-overview/billing-methods)。 |
| 操作审计ActionTrail | [操作审计（ActionTrail）](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)帮助您监控并记录阿里云账号的活动，包括通过阿里云控制台、OpenAPI、开发者工具对云上产品和服务的访问和使用行为。您可以将这些行为事件下载或保存到日志服务或OSS存储空间，然后进行行为分析、安全分析、资源变更行为追踪和行为合规性审计等操作。 | 开通免费，详情参见[产品计费](https://help.aliyun.com/zh/actiontrail/product-overview/billing/)。 |
| 日志服务SLS | [日志服务SLS](https://help.aliyun.com/zh/sls/what-is-log-service)是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/sls/billing/)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是阿里云提供的性能卓越、稳定可靠、弹性扩展的IaaS（Infrastructure as a Service）级别云计算服务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 访问控制RAM | [访问控制](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)使您能够安全地集中管理对阿里云服务和资源的访问。您可以使用RAM创建和管理用户和组，并使用各种权限来运行或访问他们对云资源的访问。 | 免费。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| 日志审计账号 | 一般在资源目录的Core资源夹中建议存在一个日志审计账号，专门用于存储云上收集的各种日志，并且仅有审计管理员使用的角色拥有对该日志账号的管控权限，实现运维管控权限和审计监管权限的隔离，避免出现恶意运维之后又能删除审计日志逃避司法追责的情况。该账号仅承担审计日志收集、留存和分析的职能，账号下不保有其他计算和数据库资源，与业务账号独立。这个账号在初始化的时候可以通过[云治理中心](https://help.aliyun.com/zh/cgc/product-overview/what-is-cloud-governance-center)生成。 |

## 安全性

### 资源目录权限

资源目录服务关联角色（AliyunServiceRoleForResourceDirectory）为资源目录集成服务提供可信访问通道，详情参见[资源目录服务关联角色](https://help.aliyun.com/zh/resource-management/security-and-compliance/ram-roles-in-a-resource-directory)。

### 操作审计

操作审计管理权限相关，如RAM用户授权、服务关联角色、系统权限策略等详情参见[管理权限](https://help.aliyun.com/zh/actiontrail/user-guide/permission-management/)。

### AccessKey使用

- 需要使用企业管理主账号下RAM用户的AccessKey，该RAM用户需要拥有资源只读权限 ReadOnlyAccess和角色扮演AliyunSTSAssumeRoleAccess两个权限，用于日志处理服务读取资源目录账号下的资源标签。
- 需要使用日志审计账号下RAM用户的AccessKey，该RAM用户需要拥有SLS的读取及写入权限，用于监听日志消息及写入处理后的日志。

## 注意事项

### 操作审计

- 操作审计相关限制详情参见[使用限制](https://help.aliyun.com/zh/actiontrail/product-overview/limits)，地域支持详情参见支持[操作审计的地域](https://help.aliyun.com/zh/actiontrail/product-overview/supported-regions)，云产品支持情况详情参见[支持操作审计的云服务及事件](https://help.aliyun.com/zh/actiontrail/product-overview/services-that-work-with-actiontrail)。
- 企业需要为用于存储操作事件的SLS付费，根据自身需求设置新写入的日志保留天数。

### 日志处理服务可用性

方案中部署的日志处理Python服务若需要高可用，需要根据实际情况进行配置消费组信息、进行多套部署并进行异常处理加固。SLS SDK概述及异常处理等详情参见[SDK参考](https://help.aliyun.com/zh/sls/developer-reference/sdk-reference/)。

### 标签使用限制

云产品对标签支持情况详情参见[支持标签的云服务](https://help.aliyun.com/zh/resource-management/tag/product-overview/services-that-work-with-tag)。

### 资源目录使用限制

资源目录及资源共享使用限制详情参见[使用限制](https://help.aliyun.com/zh/resource-management/product-overview/limits)。

## 实施步骤

实施步骤中以ECS、SLB打标签及其操作事件为例进行部署验证。

### 实施准备

#### 已完成审计日志归集

- 按照[多账号操作日志统一归集与审计](https://help.aliyun.com/zh/well-architected/solution-37)完成审计日志配置。
- 企业管理账号需确保已开启操作审计服务。

#### 拥有运行Python环境的ECS及SLB资源

- ECS用于部署日志处理服务，具备Python3运行环境。
- 已有ECS、SLB，用于打标签并进行管控操作，进行日志写入验证。

#### 确保资源结构已创建，本方案中相应的账号UID及用途如下表

| 账号UID | 账号用途 |
| --- | --- |
| 114093xxxxxx7592 | 企业管理账号，即开通资源目录的账号 |
| 104853xxxxxx7656 | 日志审计账号（LoggingAccount），专门收集操作审计日志及资源配置数据的账号，与业务账号独立通过Landingzone部署之后会默认在Core/文件夹下面创建LoggingAccount账号 |
| 133313xxxxxx3815 | 成员账号，该账号持有ECS等资源，用于测试资源配置数据变更 |

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：45分钟。

### 操作步骤

#### 为资源添打标签

1. 登录成员账号[ECS控制台](https://ecs.console.aliyun.com/?spm=5176.8789780.J_5834642020.2.225345b5YlRO3q#/home)，为ECS打标签。如果资源已有标签可跳过此步骤。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971935.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971929.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971937.png)
2. 登录成员账号[负载均衡控制台](https://slb.console.aliyun.com/slb/overview)，为SLB打标签。如果资源已有标签可跳过此步骤。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971930.png)

#### 创建日志审计目标LogStore

1. 使用RAM用户登录管理账号[资源目录控制台](https://resourcemanager.console.aliyun.com/resource-directory/folders/)，选择日志审计账号登入。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971931.png)
2. 登入日志审计账号后进入[日志服务控制台](https://sls.console.aliyun.com/)，能够查看到已归集的审计日志记录。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971934.png)
3. 在日志服务控制台新建Project并记录名称备用，该Project用于存储处理后的日志，也可不新建使用已有Project。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971938.png)
4. 在新建的Project下新增LogStore，作为存储处理后的日志的LogStore，记录LogStore名称备用。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971932.png)

#### 新建RAM用户及AccessKey

1. 登录日志审计账号[RAM控制台](https://ram.console.aliyun.com/overview)，新建RAM用户后复制保存AccessKey备用，该AccessKey用于日志处理服务的SLS消息消费以及处理后的日志写入。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971942.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971936.png)
2. 为日志审计账号新建的RAM用户授予日志服务管控权限。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971939.png)
3. 切换到管理账号[RAM控制台](https://ram.console.aliyun.com/overview)，新建RAM用户后保存AccessKey备用，用于日志处理服务读取所有账号的ECS/SLB等资源信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971943.png)
4. 按最小授权原则，为管理账号新建的RAM用户授予只读和STS角色扮演权限，用于日志处理服务读取管理账号的资源信息、扮演资源目录角色读取成员账号的ECS/SLB等资源标签信息。日志处理服务读取成员账号的资源信息时，会使用该管理账号的RAM用户，扮演为成员账号的资源目录角色ResourceDirectoryAccountAccessRole进行资源数据读取，该角色在成员账号纳入管理账号资源目录时已经自动创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971945.png)

#### 部署日志处理服务

1. 确保要部署日志处理服务的服务器已安装Python环境，在服务器上安装阿里云相关Python SDK，本方案使用Python3。`# 安装阿里云 SDK 核心库
pip3 install aliyun-python-sdk-core

# 安装阿里云 STS SDK
pip3 install aliyun-python-sdk-sts

# 安装阿里云 日志服务SLS SDK 
pip3 install aliyun-log-python-sdk

# 安装阿里云 ECS SDK 
pip3 install aliyun-python-sdk-ecs

# 安装阿里云 SLB SDK 
pip3 install aliyun-python-sdk-slb`
2. 修改下面代码配置，填入管理账号UID、源LogStore、目标LogStore、AccessKey等配置信息，配置完成后运行Python脚本启动日志处理服务，服务会持续消费SLS源日志库，当操作事件类型为“写入”时会进行处理并写入目标LogStore。代码示例中收到ECS及SLB的操作日志时会去查询资源标签，每个标签都会向目标LogStore写入单独字段，需要查询其它资源类型的标签时引入相应sdk依赖，在query_resource_tags函数中添加类型支持即可。`# encoding: utf-8

import time
import json

from aliyun.log.consumer import *
from aliyun.log import *

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.auth.credentials import StsTokenCredential

from aliyunsdkecs.request.v20140526.ListTagResourcesRequest import ListTagResourcesRequest as EcsListTagResourcesRequest
from aliyunsdkslb.request.v20140515.ListTagResourcesRequest import ListTagResourcesRequest as SlbListTagResourcesRequest
from aliyunsdksts.request.v20150401.AssumeRoleRequest import AssumeRoleRequest

# SLS消息消费组
sls_consumer_group_name = 'g2'
sls_consumer_name = 'c2'

# SLS endpoint
sls_endpoint = 'cn-hangzhou.log.aliyuncs.com'

# SLS 源project
sls_source_project = 'testl1-trail-project'
sls_source_logstore = 'actiontrail_test212'

# SLS 目的project
sls_target_project = 'test1-trail-project'
sls_target_logstore = 'processed_test1'

# SLS AccessKey
sls_access_key = ''
sls_secret_key = ''

# 管理账号UID
admin_account_id = '1140931609457592'

# 查询资源(如ecs/slb/vpc)标签所需AK，使用管理账号RAM用户的AK，RAM用户需具备所有资源读取和STS角色扮演权限
resource_access_key = ''
resource_secret_key = ''

# 需要处理的event的serviceName，如ecs/slb/vpc/oss/cloudsso/sts，为空表示处理所有
need_process_service = []
# need_process_service = ['ecs', 'slb', 'vpc', 'oss']

# 是否只处理写事件，建议开启True
only_process_write_event = True

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

 for item in log_items['logs']:

 """
 item格式
 {'time': 1632708969, 'event': '{"acsRegion":"cn-beijing","serviceName":"Ecs","xxx":"xxx"}'}
 """
 if 'event' not in item:
 continue

 log_item_event = parse_json(item['event'])
 # 只处理写事件
 if only_process_write_event and log_item_event['eventRW'] != 'Write':
 continue

 # 只处理关心的service event
 if need_process_service and str(log_item_event['serviceName']).lower() not in need_process_service:
 continue

 print('\noriginEvent:' + str(item))

 try:
 # 构建新事件，只包含所关心的字段
 new_log_item_event = build_new_event(log_item_event)
 print('\nnewEvent:' + str(new_log_item_event))

 # 查询资源标签
 res_tags = query_resource_tags(new_log_item_event['accountId'],
 new_log_item_event['serviceName'],
 new_log_item_event['acsRegion'],
 new_log_item_event['resourceName'])
 print('\nresTags:' + str(res_tags))

 # 构建写入sls的tuple
 log_tuples = build_log_item_tuples(new_log_item_event, res_tags)
 print('\nlogTuples:' + str(log_tuples))

 # 写入sls
 put_logs(log_tuples)
 except Exception:
 import traceback
 traceback.print_exc()
 return check_point_tracker.get_check_point()

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

def build_new_event(log_item_event):
 if 'resourceType' not in log_item_event or 'resourceName' not in log_item_event:
 log_item_event['resourceType'] = ''
 log_item_event['resourceName'] = ''

 if 'principalId' not in log_item_event['userIdentity']:
 log_item_event['userIdentity']['principalId'] = ''

 new_log_item_event = {
 'eventId': log_item_event['eventId'],
 'eventName': log_item_event['eventName'],
 'eventRW': log_item_event['eventRW'],
 'eventSource': log_item_event['eventSource'],
 'eventTime': log_item_event['eventTime'],
 'eventType': log_item_event['eventType'],

 'acsRegion': log_item_event['acsRegion'],
 'serviceName': log_item_event['serviceName'],
 'resourceType': log_item_event['resourceType'],
 'resourceName': log_item_event['resourceName'],

 'accountId': log_item_event['userIdentity']['accountId'],
 'principalId': log_item_event['userIdentity']['principalId'],
 'userName': log_item_event['userIdentity']['userName'],
 'userType': log_item_event['userIdentity']['type'],
 }

 return new_log_item_event

def assume_res_dir_role(account_id):

 request = AssumeRoleRequest()
 request.set_accept_format('json')
 request.set_RoleSessionName("ResourceDirectoryAccountAccessRoleSession")
 request.set_RoleArn("acs:ram::" + str(account_id) + ":role/ResourceDirectoryAccountAccessRole")

 client = AcsClient(resource_access_key, resource_secret_key)
 response = client.do_action_with_exception(request)

 print(str(response, encoding='utf-8'))

 return parse_json(str(response, encoding='utf-8'))

def query_resource_tags(account_id, resource_type, region_id, resource_id):
 # 若需新增其它资源标签查询在此添加代码
 if 'ecs' in str(resource_type).lower():
 request = EcsListTagResourcesRequest()
 elif 'slb' in str(resource_type).lower():
 request = SlbListTagResourcesRequest()
 else:
 return []

 request.set_accept_format('json')
 request.set_ResourceType("instance")
 request.set_ResourceIds([resource_id])

 if account_id == admin_account_id:
 # 若是管理账号下资源，直接使用自己的ak
 resource_access_credentials = AccessKeyCredential(resource_access_key, resource_secret_key)
 else:
 # 成员账号，管理账号扮演资源目录角色获取STS令牌
 rd_role = assume_res_dir_role(account_id)
 resource_access_credentials = StsTokenCredential(rd_role['Credentials']['AccessKeyId'],
 rd_role['Credentials']['AccessKeySecret'],
 rd_role['Credentials']['SecurityToken'])

 client = AcsClient(region_id=region_id, credential=resource_access_credentials)

 response = client.do_action_with_exception(request)
 print(region_id + ' originTagResponse:' + str(response, encoding='utf-8'))

 response_json = parse_json(str(response, encoding='utf-8'))

 if response_json is not None and 'TagResources' in response_json and 'TagResource' in response_json['TagResources']:
 return response_json['TagResources']['TagResource']
 else:
 return []

def parse_json(content):
 try:
 return json.loads(content)
 except Exception as e:
 return None

def build_log_item_tuples(log_dict, tags):
 log_tuples = []
 for k, v in log_dict.items():
 log_tuple = (k, v)
 log_tuples.append(log_tuple)

 for tag in tags:
 log_tuple = (tag['TagKey'], tag['TagValue'])
 log_tuples.append(log_tuple)

 return log_tuples

def put_logs(log_tuples):
 print("ready to put logs for %s" % sls_target_logstore)

 log_item = LogItem()
 log_item.set_contents(log_tuples)
 log_group = [log_item]

 request = PutLogsRequest(sls_target_project, sls_target_logstore, "", "", log_group, compress=False)

 sls_log_client = LogClient(sls_endpoint, sls_access_key, sls_secret_key)
 sls_log_client.put_logs(request)

 print("put logs for %s success " % sls_target_logstore)

def main():
 client_worker = None
 try:
 option = LogHubConfig(sls_endpoint, sls_access_key, sls_secret_key, sls_source_project, sls_source_logstore,
 sls_consumer_group_name, sls_consumer_name,
 cursor_position=CursorPosition.END_CURSOR,
 heartbeat_interval=6,
 data_fetch_interval=1)

 client_worker = ConsumerWorker(SampleConsumer, consumer_option=option)
 print('********start consume********')
 client_worker.start()
 client_worker.join()
 except Exception as ex:
 print(ex)
 print('********end consume********')
 client_worker.shutdown()

if __name__ == '__main__':
 main()`

#### 目标日志库添加索引及验证

1. 登录日志审计账号[日志服务控制台](https://sls.console.aliyun.com/)，可查看目标日志库写入情况。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971944.png)
2. 建立字段索引，用于支持单字段查询分析。如果是标签字段，点击自动生成索引后可能无法自动出现在列表内，需要点击“+”号手动添加标签Key到列表中，例如company、role标签。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971946.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971948.png)
3. 按需重建索引。建立索引后只对之后的日志写入生效，如果需要按字段查询历史数据需要进行索引重建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971947.png)
4. 验证资源变更日志数据写入。对SLB、ECS进行变更类操作后等待片刻，可按资源类型及标签等字段查询处理后的日志。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971940.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971949.png)
5. 按业务标签查询，快速构建统计视图。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2576581571/p971941.png)

## 故障排除

### SLS

日志服务问题详情参见[常见问题](https://help.aliyun.com/zh/sls/frequently-asked-questions)，SDK异常处理详情参见[错误处理](https://help.aliyun.com/zh/sls/developer-reference/exception-handling)。

### 操作审计

操作审计常见问题详情参见[常见问题](https://help.aliyun.com/zh/actiontrail/support/faq/)。

### 资源目录

资源目录常见问题处理详情参见[常见问题](https://help.aliyun.com/zh/resource-management/resource-directory/support/faq/)。

## 相关内容

- [SLS SDK参考](https://help.aliyun.com/zh/sls/developer-reference/sdk-reference/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-38（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
