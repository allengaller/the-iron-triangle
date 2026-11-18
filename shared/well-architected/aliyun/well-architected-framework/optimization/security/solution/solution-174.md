<!-- source: https://help.aliyun.com/zh/well-architected/solution-174 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929337 -->

# 多账号自动化场景下的AK管理方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3176581571/p970834.png)

当企业使用多账号来部署云上业务，并希望设计一个账号来负责其他账号内资源自动化创建。那不同账号之间的访问凭据管理就显得特别重要，如果每个账号都提供访问密钥那管理成本高，并且容易出现密钥泄漏风险。

本方案介绍了一种利用资源目录与跨账号角色扮演的能力来实现多账号场景下应用程序访问凭据的最佳管理实践。

## 方案优势

### 集中式管理自动化程序身份

将自动化程序部署在运维账号内，能够集中式管理企业自动化程序身份，规范企业应用程序身份管理规范，进而避免出现身份泄露。

### 一种更安全的应用程序身份

通过使用ECS实例角色，而不是采用明文的AK方式，能够有效避免因误操作导致AK泄露风险。

## 客户场景

### 多账号自动化场景下应用程序身份管理

#### 场景描述

对于使用了多账号的企业，希望通过自动化的方式来管理各个账号的资源。应该如何规范各个账号职责及对应采用什么样的身份访问策略。

#### 适用客户

- 使用资源目录管理云上多个账号的企业客户。
- 使用自动化程序来管理账号内资源的客户。

## 方案架构

本方案用于指导当企业采用了多账号架构，希望在一个账号内执行脚本，相应的程序身份如何管理。借助资源目录与跨账号角色扮演的能力，企业可以设置一个单独跑自动化程序的账号：「运维账号」。在这个账号内跑脚本去管理其他成员账号内的资源。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3176581571/p970831.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 资源目录RD | [资源目录RD（Resource Directory）](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)是阿里云面向企业客户提供的一套多级账号和资源关系管理服务。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/resource-management/product-overview/billing/)。 |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 云效 | [云效](https://help.aliyun.com/zh/yunxiao/product-overview/what-is-cloud-effect)是阿里云云原生时代一站式BizDevOps平台。云效流水线Flow是一款企业级、自动化的研发交付流水线， 提供灵活易用的持续集成、持续验证、 持续发布功能，帮助企业高质量、高效率的交付业务。 | 高级版收费，详情参见[云效自费](https://help.aliyun.com/zh/yunxiao/product-overview/product-billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| 企业管理主账号 | 在企业拥有多个阿里云账号时，特指拥有管理其他账号资源权限的管理员账号。用于管理多账号，统一配置多账号身份权限，统一查看各云账号账单，统一配置审计规则并下发到各成员账号。 |
| ECS实例角色 | 实例RAM角色是RAM角色的一种，它让ECS实例扮演具有某些权限的角色，ECS实例可以使用该角色的临时访问凭证来访问指定的阿里云服务，例如OSS、RDS等，实现ECS实例与其他阿里云服务之间的安全通信。 |

## 安全性

### 资源目录权限

资源目录服务关联角色（AliyunServiceRoleForResourceDirectory）为资源目录集成服务提供可信访问通道，详情参见[资源目录服务关联角色](https://help.aliyun.com/zh/resource-management/security-and-compliance/ram-roles-in-a-resource-directory)。

### ECS安全性

在本方案中这台ECS配置了一个超级大的权限，能够管理多个账号的权限。所以这台ECS主机的安全性要求比较严。ECS实例安全性可以查看官方文档：《[如何提高ECS实例安全性](https://help.aliyun.com/zh/ecs/use-cases/make-ecs-instances-more-secure?spm=a2c4g.11186623.0.i15)》。

### 云效安全性

云效产品安全性详情参见[产品安全白皮书](https://help.aliyun.com/zh/document_detail/193835.html)，角色及权限详情参考官方文档[企业角色与权限](https://help.aliyun.com/zh/yunxiao/user-guide/enterprise-roles-and-permissions/)，流水线权限控制详情参见[权限管理](https://help.aliyun.com/zh/yunxiao/user-guide/permission-management)。

## 注意事项

### 方案范围

本方案主要是介绍针对多账号企业需要使用自动化场景相应AK管理的最佳实践，对于云效流水线的最佳实践不会过多涉及。

## 实施步骤

### 实施准备

- 在「运维账号」已拥有一台可连通公网的ECS（本方案使用操作系统CentOS）作为云效流水线执行主机。这台主机能够从云效Codeup中拉取到代码。
- 在「运维账号」提前开通云效流水线，能够登录[流水线控制台](https://flow.aliyun.com/my?page=1)。
- 已拥有Git仓库，能够通过http方式上传及拉取Terraform相关测试代码。不限制Git仓库类型，可使用[云效Codeup](https://help.aliyun.com/zh/document_detail/57904.html)。
- 确定用于演示的工作流及Terraform输入参数，输入参数分为两部分：第一部分为**全局参数**，需写入源代码中的settings.tfvars文件，每次流水线执行时均保持一致；第二部分为**执行参数**，执行流水线时动态填写，不会保存。全局参数vpc_name：创建的vpc的名称vpc_cidr：创建的vpc的CIDR执行参数biz_id：需要执行脚本的目标账号UID

### 实施规划

本次实施是基于企业已经按照Landing Zone的规范完成了多账号的搭建，需要在运维账号内完成对其他账号的资源自动化管理。架构示意图：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3176581571/p970833.png)

在这篇方案中主要有如下实施：

- 在运维账号C中执行一个脚本，能够在指定成员账号（A1、B1账号）进行自动化资源管理，如创建VPC、ECS等资源。

#### 部署清单

涉及部署地域为在上海（cn-shanghai）Region。部署内容及详细说明如下：

| 部署账号 | 部署内容 |
| --- | --- |
| 运维账号C | 部署一台ECS具备执行Terraform脚本环境。开通云效服务 |

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：

- 自动化方式：30分钟。
- 非自动化方式：1小时。

### 操作步骤

#### 配置权限

步骤1：在运维账号C创建一个可信实体类型为阿里云服务的角色：**ecs-role**，用于给ECS做实例角色。为这个角色授权：**调用 STS服务AssumeRole接口的权限**。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3176581571/p970847.png)

为角色：ecs-role授权

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3176581571/p970836.png)

步骤2：在**资源管理账号（MA）**创建一个可信实体类型为阿里云账号的角色：automation-assume。授信策略：

```
{
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Effect": "Allow",
      "Principal": {
        "RAM": [
          "acs:ram::xx<运维账号UID>:role/ecs-role"
        ]
      }
    }
  ],
  "Version": "1"
}
```

给角色：automation-assume授权

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3176581571/p970838.png)

#### 验证权限

步骤1：在运维账号（C）中购买一台ECS用于跑云效部署机。并且给这台ECS分配ecs-role这个角色。具体操作可以查看：[授予实例RAM角色](https://help.aliyun.com/zh/ecs/user-guide/attach-an-instance-ram-role-to-an-ecs-instance)。

步骤2：在ECS上面安装aliyun cli命令行工具、terraform命令行工具、git命令行工具。aliyun cli安装见官网[安装手册](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli)，terraform命令行安装见官网[安装手册](https://developer.hashicorp.com/terraform/downloads)，git命令行工具见官网[安装手册](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git)。

步骤3：在ECS上面执行以下脚本，获取到资源管理账号（MA）的临时AK凭据。

```
aliyun configure set --profile ecsRamRoleProfile --mode EcsRamRole --ram-role-name ecs-role --region cn-shanghai

tmp_string=`aliyun sts AssumeRole --RoleArn acs:ram::<MA Account UID>:role/automation-assume --RoleSessionName tempAutomation`
ACCESSKEYID=`echo $tmp_string|python -c 'import json,sys ; print json.load(sys.stdin)["Credentials"]["AccessKeyId"]'`
AccessKeySecret=`echo $tmp_string|python -c 'import json,sys ; print json.load(sys.stdin)["Credentials"]["AccessKeySecret"]'`
SecurityToken=`echo $tmp_string|python -c 'import json,sys ; print json.load(sys.stdin)["Credentials"]["SecurityToken"]'`

export ALICLOUD_ACCESS_KEY="$ACCESSKEYID"
export ALICLOUD_SECRET_KEY="$AccessKeySecret" 
export ALICLOUD_SECURITY_TOKEN="$SecurityToken"
```

通过上述脚本，可以将MA账号下的STS信息写入环境变量，执行TF脚本。

以上就把权限的问题解决了，下面是借助云效来看下结合企业的流水线如何实施落地。

#### 云效流水线配置

##### 添加云效主机组

1. 登录[云效流水线控制台](https://flow.aliyun.com/my?page=1)，在左侧菜单下方点击**设置，**进入**主机组管理**页面。
2. 点击**新建主机组，**在对话框中主机类型选择**阿里云ECS，**点击**新建服务授权，**授权云效获取ECS信息**。**完成授权后选择地域，勾选**运维账号C中已完成环境配置的ECS实例**，点击下一步。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3176581571/p970851.png)

##### 云效流水线配置

1. 在[云效流水线控制台](https://flow.aliyun.com/my?page=1)点击新建流水线，在流水线模板对话框中选择**空模板**，点击创建。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3176581571/p970852.png)
2. 选中空任务，将其**删除**。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3176581571/p970845.png)
3. 点击新的任务，在任务组中选择 **主机部署。**
4. 填入任务名称，**选择之前创建的主机组**，填入下方的部署脚本，部署策略选择不暂停、分批数量为1，修改流水线名称为「验证权限」，阶段名称为「代码Clone」，点击仅保存。`cd /root && rm -rf /root/many_account
git clone git@codeup.aliyun.com:651120de7f62ff9bxxxxx/code_up/many_account.git`
5. 重复上一个步骤，分别新建其他几个节点：节点：设置环境变量。对应的脚本`aliyun configure set --profile ecsRamRoleProfile --mode EcsRamRole --ram-role-name ecs-role --region cn-shanghai
tmp_string=`aliyun sts AssumeRole --RoleArn acs:ram::<MA UID>:role/automation-assume --RoleSessionName tempAutomation`
ACCESSKEYID=`echo $tmp_string|python -c 'import json,sys ; print json.load(sys.stdin)["Credentials"]["AccessKeyId"]'`
AccessKeySecret=`echo $tmp_string|python -c 'import json,sys ; print json.load(sys.stdin)["Credentials"]["AccessKeySecret"]'`
SecurityToken=`echo $tmp_string|python -c 'import json,sys ; print json.load(sys.stdin)["Credentials"]["SecurityToken"]'`
export ALICLOUD_ACCESS_KEY="$ACCESSKEYID"
export ALICLOUD_SECRET_KEY="$AccessKeySecret" 
export ALICLOUD_SECURITY_TOKEN="$SecurityToken"`节点：tf执行。对应的脚本`cd /root/many_account/
terraform init
terraform apply --auto-approve --var-file settings.tfvars -var "biz_id=$biz_id" -compact-warnings`

#### 添加流水线变量

1. 在流水线编辑页面选择**变量和缓存**，点击**新建变量**，填入流水线运行时所需参数及默认值。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3176581571/p970840.png)添加的参数包括：biz_id：目标账号的UID。可以在运行云效流水线的时候指定。

#### 运行流水线

1. 在流程配置页面点击**保存并运行，**这里可修改执行参数，点击**运行。**![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3176581571/p970853.png)
2. 点击**部署详情-部署日志**可查看日志信息。

## 源代码

提供了一套测试用的terraform代码，源代码如下：

main.tf:

```
provider "alicloud" {
  alias  = "prod_account"
  region = "cn-shanghai"
  assume_role {
    role_arn           = format("acs:ram::%s:role/ResourceDirectoryAccountAccessRole", var.biz_id)
    session_name       = "AccountLandingZoneSetup"
    session_expiration = 999
  }
}

resource "alicloud_vpc" "vpc" {
  provider = alicloud.prod_account
  vpc_name    = var.vpc_name
  cidr_block  = var.vpc_cidr
}
```

variables.tf

```
variable "vpc_cidr" {
    type    = string
    default = ""
}
variable "vpc_name" {
    type    = string
    default = ""
}
variable "biz_id" {
    type    = string
    default = ""
}
```

versions.tf

```
terraform {
  required_providers {
    alicloud = {
      source = "hashicorp/alicloud"
      version = "1.205.0"
    }
  }
  required_version = ">=0.12"
}
```

settings.tfvars

```
vpc_cidr = "10.0.0.0/12"
vpc_name = "assumerole"
biz_id = "xxx"
```

## 故障排除

### 为什么无法提交代码到云效仓库？

可能有如下两个原因：

- 没有按照官方的操作方式配置 SSH 密钥，具体可以查看[官方说明](https://help.aliyun.com/zh/yunxiao/user-guide/configure-ssh-key)。
- 本地配置问题，查看**~/.ssh/config 配置。**

## 相关内容

- [访问控制](https://help.aliyun.com/zh/ram?spm=a2c4g.11186623.0.i1)
- [资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)
- [云效](https://help.aliyun.com/product/150040.html?spm=a2c4g.200506.0.i2)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-174（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
