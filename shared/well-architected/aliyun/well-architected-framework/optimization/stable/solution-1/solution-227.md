<!-- source: https://help.aliyun.com/zh/well-architected/solution-227 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929366 -->

# 通过Terraform实现云资源误操作快恢

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5186581571/p971257.png)

企业在运维越来越多资源之后，很容易将某些关键的实例配置做了一些误修改或删除，导致整个业务中断。当出现这种高危变更之后，如果能够通过自动化的手段快速恢复到变更前的稳定状态，那就能够有效提升业务连续性。

本方案介绍了一种通过Terraform来实现云资源被误操作的快恢方法。

## 方案优势

### 存量资源管理

兼容Terraform逆向工具，支持对账号内的存量阿里云资源一键导入，快速生成terraform代码及tfstate状态文件，能够有效降低云资源管理与配置恢复成本。

### 提供代码模板

通过自动化服务台，能够将存量资源对应的Terraform代码模板自动生成，免去了用户自已编写代码的工作量。

### 云端状态管理

基于阿里云的OSS，提供符合Terraform管理云资源过程中需要的状态数据云端存储能力，有效避免操作不当导致数据丢失的风险。

## 客户场景

### 灾备场景

#### 场景描述

通过云资源自动化 for Terraform 构建一套与线上环境同配置的云基础设施，当业务对应的资源配置被误删除或者被修改，可以将备份的那份云基础设施配置快速恢复，助力业务快速从灾难中恢复。

#### 适用客户

1. 控制台或者通过API管理云资源的客户
2. 对稳定性要求高

### 存量资源管理升级

#### 场景描述

过去企业可能是通过控制台或者API来管理云上资源，后续希望能够利用Terraform这样的工具来管理云资源；利用本方案可以将存量资源快速生成Terraform的配置。后续就可以基于这份配置及状态文件持续管理云资源。

#### 适用客户

1. 希望通过Terraform来管理云资源
2. 存在比较多的存量资源

## 方案架构

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5186581571/p971258.png)

本方案使用Terraform自动化执行，同时整合自动化服务台和OSS来搭建一套完整的Terraform的执行环境，来实现将存量账号内的资源导出成Terraform状态与代码文件。当线上环境出现误操作之后，可以将这套代码与状态文件快速恢复到线上环境中去。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 访问控制RAM | [访问控制](https://help.aliyun.com/zh/ram/product-overview/what-is-ram)使您能够安全地集中管理对阿里云服务和资源的访问。您可以使用RAM创建和管理用户和组，并使用各种权限来运行或访问他们对云资源的访问。 | 免费。 |
| 对象存储OSS | [对象存储OSS（Object Storage Service](https://help.aliyun.com/zh/oss/user-guide/what-is-oss)）是阿里云提供的海量、安全、低成本、高持久的云存储服务。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/oss/billing/)。 |
| Terraform | Terraform是一种开源工具，用于安全高效地预配和管理云基础结构。你可以使用Terraform管理阿里云资源。 | 免费。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| State文件 | Terraform中用于描述当前资源配置的文件，详情参见[State](https://www.terraform.io/language/state)。本文使用OSS作为State文件的远端存储，详情参见[OSS Backend](https://www.terraform.io/language/settings/backends/oss)。 |

## 安全性

### Terraform State文件安全

使用OSS作为Backend保存Terraform State文件，使用OTS支持State文件加锁及一致性检查，详情参见[OSS Backend](https://www.terraform.io/language/settings/backends/oss)。

### OSS数据安全

版本控制是针对存储空间（Bucket）级别的数据保护功能。开启版本控制后，针对数据的覆盖和删除操作将会以历史版本的形式保存下来。您在错误覆盖或删除对象（Object）后，能够将存储在Bucket中的Object恢复至任意时刻的历史版本。

### AccessKey使用

需要使用账号内RAM用户的AccessKey，用于创建账号及操作阿里云资源。该RAM用户拥有管理账号内资源权限。

## 注意事项

### OSS使用限制

OSS使用限制及性能指标详情参见[使用限制](https://help.aliyun.com/zh/oss/user-guide/limits)。

### 企业变更流程集成

如果企业有自建的变更流程，那需要考虑一下当线上资源发生变更之后，需要将最新的资源配置导入到Terraform配置中。

## 实施步骤

### 实施准备

1. 确保已在账号内开通OSS服务，并创建用于存储Terraform state文件的**Bucket。**
2. 确保已在账号内开通一个「子用户」AK，且该账号拥有资源管理权限。在后续的步骤中，我们将使用该子用户AK。

### 实施规划

#### 场景规划

本方案中我们介绍两种实施方式，一种是利用Terraform能力；一种是利用自动化服务台。以下是当前账号基础架构部署图(精简架构)：

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5186581571/p971247.png)

故障演示场景：

1. 演示ALB资源被误操作：假设网络管理员目前在控制台上修改ALB的规则与配置，并且这次修改是有问题的，导致ALB服务不可用。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 利用Terraform操作步骤

#### 存量资源导入

因为之前资源管理都是通过控制台进行操作，并没有被terraform管理起来。所以第一步得先将资源导入到state文件里面来。

##### 1、获取资源ID

每个被Terraform管理的资源有两种类型的资源ID，一种是阿里云自动生成的ID（如ECS的InstanceID），还有一类是Provider自动生成的ID（如2个资源关系对应，如EIP绑定到ALB上，这层绑定关系也会有ID）。

获取ID的常见办法：

- 控制台
- CLI、API查询
- Terraform的datasource，比如以下代码可以获取alb实例ID`data "alicloud_alb_load_balancers" "nameRegex" {
 name_regex = "alb-tf-prod-*"
}`

##### 2、模板声明所要导入的资源

```
provider "alicloud" {
  access_key = ""
  secret_key = ""
  alias  = "prod_account"
  region = "cn-beijing"
}

resource "alicloud_alb_load_balancer" "default" {
  provider = "alicloud.prod_account"
}
```

简单的声明之后，无需定义具体的参数即可开始资源的导入操作。在Terraform中，导入一个资源的操作通过 import 命令来完成。

```
$ terraform import alicloud_alb_load_balancer.default alb-exuexxxxx
```

第一次导入State文件内容如下。

```
{
  "version": 4,
  "terraform_version": "1.4.2",
  "serial": 1,
  "lineage": "eda603d6-62a1-fc0a-29fd-0c740a868bfa",
  "outputs": {},
  "resources": [
    {
      "mode": "managed",
      "type": "alicloud_alb_load_balancer",
      "name": "default",
      "provider": "provider[\"registry.terraform.io/hashicorp/alicloud\"].prod_account",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "access_log_config": [],
            "address_allocated_mode": "Fixed",
            "address_ip_version": "Ipv4",
            "address_type": "Internet",
            "deletion_protection_enabled": null,
            "dns_name": "alb-xxx.cn-beijing.alb.aliyuncs.com",
            "dry_run": null,
            "id": "alb-xxx",
            "load_balancer_billing_config": [
              {
                "pay_type": "PayAsYouGo"
              }
            ],
            "load_balancer_edition": "Basic",
            "load_balancer_name": "alb-tf-prod-xxxx",
            "modification_protection_config": [
              {
                "reason": "",
                "status": "NonProtection"
              }
            ],
            "resource_group_id": "rg-xxxx",
            "status": "Active",
            "tags": {
              "createdBy": "Terraform"
            },
            "timeouts": {
              "create": null,
              "delete": null,
              "update": null
            },
            "vpc_id": "vpc-xxxx",
            "zone_mappings": [
              {
                "vswitch_id": "vsw-xxx",
                "zone_id": "cn-beijing-h"
              },
              {
                "vswitch_id": "vsw-xxxx",
                "zone_id": "cn-beijing-g"
              }
            ]
          },
          "sensitive_attributes": [],
          "private": "xxxxx"
        }
      ]
    }
  ],
  "check_results": null
}
```

##### 3、补齐资源模板定义

由于模板中没有完成对所导入资源的详细定义，因此，资源导入成功后，模板内容与State存储的内容存在差异，此时如果直接运行 plan 命令，将会看到一个update。为了保持**资源模板（TF代码）与资源状态（state文件）的一致**，需要在模板中手动补齐缺失的参数定义，直到运行 plan 不会再有变更信息为止：

**注意！这份文件里面的属性值都是源自tfstate文件里面的内容:**

```
provider "alicloud" {
  alias  = "prod_account"
  region = "cn-beijing"
}
resource "alicloud_alb_load_balancer" "default" {
  provider = "alicloud.prod_account"
  resource_group_id = "rg-xxx"
  vpc_id            = "vpc-xxx"
  load_balancer_name     = "alb-tf-prod-default"
  address_type           = "Internet"
  address_allocated_mode = "Fixed"
  load_balancer_edition  = "Basic"
  load_balancer_billing_config {
  pay_type = "PayAsYouGo"
}
zone_mappings {
  vswitch_id = "vsw-xxx"
  zone_id    = "cn-beijing-h"
}
zone_mappings {
  vswitch_id = "vsw-xxx"
  zone_id    = "cn-beijing-g"
}
modification_protection_config {
  status = "ConsoleProtection"
}
tags = {
  "createdBy": "Terraform"
}
timeouts  {

}
}
```

补完之后，再执行tf plan就不会有差异了

```
No changes. Your infrastructure matches the configuration.
```

#### 定期备份存量资源配置

当资源管理员变更完资源配置之后，如果线上环境都正常，就可以手动导入到state文件里面。最好是先terraform plan一下看看有哪些规则有变化。如果没问题了再import。然后再同步更新TF代码。**这才算是一次正式的备份。**

#### 利用备份文件来恢复资源配置

假设某天管理员的一个误操作，将一个配置改错了。导致业务受影响，能不能快速将配置推上去。那就可以借助terraform的能力。只要确保状态文件是正确的。就可以恢复到指定版本。

**注意**

- 如果控制台上面的变化是有问题的，那就应该以state文件状态为主。
- TF Code里面的属性值，也得改成state文件里面的值。

如果控制台上面资源发生变更，那执行tf plan发现有一个change。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5186581571/p971261.png)

如果这个时候，执行apply的话，就会把控制台上面的修改刷成代码里面的配置。

注意：

- 如果控制台被误操作，那就可以直接将本地的state文件刷新上去，直接应用掉。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5186581571/p971260.png)

这样就算控制台上面误操作了，也可以通过这份配置快速恢复业务。

### 利用自动化服务台操作步骤

#### 存量资源批量导入

1. 登录[自动化服务台](https://iac.console.aliyun.com/exporttasks)，进入资源导出页面，点击“新建任务”按钮开始创建一个资源导出任务。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5186581571/p971248.png)在导出过程中，除了设置基本的任务属性、资源类型以及资源所在的地域和可用区之外，需要特别关注两部分的内容：设置导出时的过滤条件 资源在导出的过程中，将根据设置的资源类型和所属区域查询到对应的云资源，并在查询过程中，可以通过设置过滤条件获取到符合期望的云资源。设置导出后的资源属性变量（这点挺重要的，可以将一些变量拎出来） 资源在导出之后，所有的资源属性都将以硬编码的方式设置在模板中。在导出之后，为了满足对资源的持续管理，比如部分属性的修改，可以通过设置属性变量来将硬编码的资源属性变为可设置的属性变量保存在资源模板中，当有修改需求的时候，传入新的变量值即可。

#### 执行资源导出任务

完成任务的创建之后，点击“执行”按钮即可开始执行导出任务。任务执行完毕之后，进入任务详情页即可看到符合过滤掉条件的信息和编排模板了。

对于同一个资源导出任务，每执行一次，都将产生一个新的模板版本。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5186581571/p971249.png)

这样就能够实现state文件及TF代码模板一并导出。并且支持将这份文件导出到OSS上去。

有了这份配置文件及代码文件之后，如何恢复到生产环境，参考上面操作步骤。

## 故障排除

### 为什么有些资源实例ID查询不到？

可能有如下两个原因：

1. 检查一下当前Provider的版本，是否为最新。
2. 有些资源通过terraform data检索不出来实例ID，这种方式需要在控制台查询。

## 相关内容

- [Terraform](https://help.aliyun.com/product/95817.html?spm=a2c4g.11174283.0.i2)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-227（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
