<!-- source: https://help.aliyun.com/zh/well-architected/solution-270 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929477 -->

# 存量资源快速打标签方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973081.png)

很多企业由于上云初期关注点在于业务快速上云跑通，对于云上资源的分组管理重视程度不够。往往在后期进行云上成本治理时，发现云上很多资源都没有打上资源标签。企业不得不面临着需要投入人力构建企业整体标签管理体系，同时对大量已经运行的资源进行补充或者修正标签。

本文档则介绍了三种对云上存量资源进行快速打标的方案。

## 方案优势

### 针对企业不同现状给到不同方法

不同企业的管理人员基于自身习惯，对于资源的管理方式不一样。针对不同企业现状提供了最适合的方法快速完善资源标签。

## 客户场景

### 应对企业成本治理要求

#### 场景描述

随着云上资源量增加，企业云管团队越来越需要进行成本精细化治理，同时对于当前云上混乱的资源管理现状进行体系化的梳理。

#### 适用客户

- 有成本治理诉求的企业客户
- 缺少标签管理规范的企业客户

## 方案架构

本方案有3个实现路径，根据企业情况不同进行选择

| 企业现状 | 实施路径 |
| --- | --- |
| 云上资源量较少 | 直接在资源中心进行打标 |
| 资源存在分组特征，比如名称、地域 | 通过OSS批量打标模版进行打标 |
| 不符合上述 | 资源导出到本地，本地手动打标之后通过API同步到云上 |

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973078.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源中心 | [资源中心](https://help.aliyun.com/zh/resource-management/resource-center/product-overview/resource-center-overview)为您提供跨账号、跨产品、跨地域的资源统一视图及资源搜索能力。您可以查看全局资源列表，对云上资源全貌了然于心。 | 免费 |
| OOS | [OOS阿里云系统运维管理](https://help.aliyun.com/zh/oos/product-overview/introduction-to-oos)是阿里云提供的云上自动化运维服务，能够自动化管理和执行任务。您可以通过模板来定义执行任务、执行顺序、执行输入和输出，然后通过执行模板来完成任务的自动化运行。 | 免费，详情参见[产品计费](https://help.aliyun.com/zh/oos/product-overview/billing)。 |

## 安全性

### OOS服务关联角色

服务关联角色具有操作RAM角色、权限策略和服务提供商等的权限。关于服务关联角色的更多信息，请参见[服务关联角色](https://help.aliyun.com/zh/oos/security-and-compliance/oos)。

## 实施步骤

### 实施准备

- 根据企业资源管理的目标，优先定义出云上标签体系，比如BU、Owner、Env等等。
- 通过资源中心梳理云上资源数量，并且根据资源特征选择合适的方案路径。
- 确保在企业账号，存在一个「用户」AK，且该用户拥有 AliyunTagAdministratorAccess权限；在后续的步骤中，我们将使用该用户AK。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

建议根据企业云上资源情况选择合适的实施路径。

#### 路径1：资源中心

1. 前往[资源管理](https://resourcemanager.console.aliyun.com/resource-center)，点击资源搜索，展示当前账号下所有的资源信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973082.png)
2. 选择合适的筛选条件，比如“无标签”筛选出无标签的资源![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973083.png)
3. 选择资源设置标签键值![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973084.png)

#### 路径2：OOS

1. 前往[OOS-公共任务模版](https://oos.console.aliyun.com/cn-shanghai/template/public)，模块名称搜索标签。根据企业情况选择合适的模版，比如需要给ECS资源进行批量打标![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973079.png)
2. 点击“创建执行”，进入配置页面![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973086.png)
3. 选择需要配置的标签以及实例的筛选条件，完成任务配置![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973087.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973088.png)
4. 等待任务执行完成即可![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973090.png)

#### 路径3：本地打标

1. 前往[资源管理](https://resourcemanager.console.aliyun.com/resource-center)，点击资源搜索，展示当前账号下所有的资源信息。点击右上角下载按钮![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973080.png)
2. 在本地打开CSV，在标签列中手动增加对应资源的标签。格式为key1:value1;key2:value2![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973089.png)
3. 运行python脚本进行本地csv的数据处理，并且调用OpenAPI进行资源打标`# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_tag20180828.client import Client as TagClient
from alibabacloud_credentials.client import Client as CredClient
from alibabacloud_credentials.models import Config as CredConfig
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tag20180828 import models as tag_20180828_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient
import pandas as pd
import json

class Sample:
 def __init__(self):
 pass

 @staticmethod
 def create_client() -> TagClient:
 """
 使用AK&SK初始化账号Client
 @return: Client
 @throws Exception
 """
 # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
 # 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
 type="sts"
 access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID']
 access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
 security_token=os.environ['ALIBABA_CLOUD_SECURITY_TOKEN']
 credentialConfig = CredConfig(type=type,access_key_id=access_key_id,access_key_secret=access_key_secret,security_token=security_token)

 credentialClient = CredClient(credentialConfig)

 print(credentialClient)

 tagConfig = open_api_models.Config(credential=credentialClient)
 # Endpoint 请参考 https://api.aliyun.com/product/Tag
 tagConfig.endpoint = f'tag.cn-shanghai.aliyuncs.com'
 tagClient = TagClient(tagConfig)
 return tagClient

 @staticmethod
 def convert_to_json(input_str):
 if not isinstance(input_str, str):
 return ''
 # 分割输入字符串得到键值对列表
 pairs = input_str.split(';')
 # 初始化一个空字典
 result_dict = {}
 # 遍历每一对键值
 for pair in pairs:
 # 检查是否包含冒号
 if ':' in pair:
 try:
 key, value = pair.split(':')
 except Exception as error:
 print(error)
 continue
 result_dict[key] = value
 # 将字典转换为JSON格式的字符串
 json_str = json.dumps(result_dict)
 return json_str

 @staticmethod
 def convert_to_product_code(input_str):
 # 分割字符串以获取各个部分
 parts = input_str.split("::")
 product_code_part = parts[1].lower() 
 return product_code_part

 @staticmethod
 def convert_to_resource_type(input_str):
 # 分割字符串以获取各个部分
 parts = input_str.split("::")
 resource_type_part = parts[2].lower()
 return resource_type_part

 @staticmethod
 def main(
 args: List[str],
 ) -> None:
 #创建OpenAPI服务
 region_id = 'cn-hangzhou' #每次只能同步一个地域资源
 client = Sample.create_client()
 #加载本地文件
 file_path = "./resources.csv"
 arn_template = "arn:acs:{ProductCode}:{Region}:{Account}:{ResourceType}/{ResourceId}"
 df = pd.read_csv(file_path)
 data = df[df['地域Id']==region_id]

 
 #依次对资源进行打标
 for index, row in data.iterrows():
 new_tags = Sample.convert_to_json(row['标签'])
 # 定义变量
 product_code = Sample.convert_to_product_code(row['资源类型 Code']) 
 region = row['地域Id']
 account = "xxxx" # 填入资源所在的阿里云账号uid
 resource_type = Sample.convert_to_resource_type(row['资源类型 Code']) 
 resource_id = row['资源 ID']
 # 使用format函数生成新的ARN
 changed_arn = arn_template.format(ProductCode=product_code, Region=region, Account=account, ResourceType=resource_type, ResourceId=resource_id)
 if new_tags == "":
 print(changed_arn+"标签无变化")
 continue 
 tag_resources_request = tag_20180828_models.TagResourcesRequest(
 region_id=region_id,
 # Array, 必填, 资源ARN（Aliyun Resource Name）。,
 resource_arn=[changed_arn],
 tags=new_tags
 )
 runtime = util_models.RuntimeOptions()
 try:
 resp = client.tag_resources_with_options(tag_resources_request, runtime)
 print(changed_arn+"新增标签："+new_tags)
 ConsoleClient.log(UtilClient.to_jsonstring(resp))
 except Exception as error:
 # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
 # 错误 message
 print(error.message)
 # 诊断地址
 print(error.data.get("Recommend"))
 UtilClient.assert_as_string(error.message)

if __name__ == '__main__':
 Sample.main(sys.argv[1:])`
4. 确认脚本运行结果![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973091.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2886581571/p973085.png)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-270（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
