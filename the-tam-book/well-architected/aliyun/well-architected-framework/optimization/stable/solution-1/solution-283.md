<!-- source: https://help.aliyun.com/zh/well-architected/solution-283 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929428 -->

# 基于阿里云ARMS Grafana构建线下IDC Zabbix和云上Prometheus的统一监控

## 方案概述

有许多客户在线下IDC机房和阿里云上都部署有服务器资源。部分客户之前线下IDC的统一监控是基于Zabbix实现的，在使用了阿里云后，希望可以通过阿里云的监控服务来实现云上云下的监控数据在同一个监控平台，实现统一监控。

本方案旨在给出阿里云上统一纳管线下Zabbix监控和云上Prometheus的一种解决方案。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972238.png)

本方案用阿里云的一个单独的地域模拟线下IDC环境，在其中通过terraform自动化脚本部署：

- 一台ECS作为Zabbix Server服务器提供监控服务；
- 一台ECS作为Zabbix Agent，它是Zabbix Server的监控对象和数据来源；
- 相关必要的VPC、交换机、弹性公网IP、安全组。

然后，把该Zabbix监控接入到阿里云统一监控平台--应用实时监控服务ARMS中的Grafana工作区；再把云上Prometheus监控接入到上述Grafana工作区；最后，把线下IDC Zabbix监控和云上Prometheus监控集成到同一个仪表盘文件夹。

## 方案优势

- 实现云上云下统一监控，方便客户运维；
- 实现不同监控协议的统一接入，让客户线下Zabbix配置无需改造即可快速接入阿里云监控平台；

## 客户场景

有些企业线下IDC和阿里云上都部署有服务器资源；同时，很多企业之前线下IDC的统一监控是基于Zabbix实现的，在使用了阿里云后，希望可以通过阿里云的监控服务，把云上云下监控数据集成到同一个监控平台，实现统一监控。

## 方案架构

本方案：

- 首先，在阿里云上一个单独的地域（本例中为青岛）构建了一个Zabbix服务器和一个Zabbix Agent作为Zabbix的监控数据源，以此模拟线下IDC的Zabbix服务；此外，考虑到Zabbix服务搭建需要很多安装步骤和参数的调整，这里使用了terraform工具把所有命令行相关的配置通过脚本的形式实现了自动化部署；
- 然后，在阿里云应用实时监控服务ARMS中创建了一个Grafana工作区；
- 随后，配置线下IDC的Zabbix数据源接入到阿里云上创建的Grafana工作区；
- 为了体现云上云下统一监控，我们还配置了云上Prometheus监控接入到上述Grafana工作区；
- 最后，再把线下IDC Zabbix监控和云上Prometheus监控集成到同一个仪表盘文件夹。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972236.png)

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 云服务器ECS | [云服务器ECS（Elastic Compute Service）](https://help.aliyun.com/zh/ecs/user-guide/what-is-ecs)是一种简单高效、处理能力可弹性伸缩的计算服务。帮助您构建更稳定、安全的应用，提升运维效率，降低IT成本，使您更专注于核心业务创新。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/ecs/billing-2/)。 |
| 可观测可视化 Grafana 版 | [可观测可视化 Grafana 版](https://help.aliyun.com/zh/grafana/product-overview/what-is-grafana)作为云原生数据可视化平台，为运维SRE、研发工程师等不同角色提供一站式可视化平台，满足运维监控、经营分析、汇报展示等不同场景的数据查询、可视化、告警需求。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/grafana/product-overview/billing-4)。 |
| 应用实时监控服务ARMS | [应用实时监控服务ARMS](https://help.aliyun.com/zh/arms/product-overview/what-is-arms)作为一款[云原生](https://www.aliyun.com/getting-started/what-is/what-is-cloud-native)可观测产品平台，包含应用监控、前端监控、Prometheus监控、云拨测、Grafana服务、告警管理等一系列子产品。其覆盖浏览器、小程序、APP、分布式应用、[容器](https://www.aliyun.com/getting-started/what-is/what-is-container)等不同[可观测](https://www.aliyun.com/getting-started/what-is/what-is-observability)环境与场景，帮助企业实现全栈性能监控与端到端追踪诊断。提高监控效率，减少运维工作量。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/arms/product-overview/product-billing-new-version)。 |
| 专有网络VPC | [专有网络VPC（Virtual Private Cloud）](https://help.aliyun.com/zh/vpc/what-is-vpc)是您专有的云上私有网络。您可以完全掌控自己的专有网络，例如选择IP地址范围、配置路由表和网关等，您可以在自己定义的专有网络中使用阿里云资源，如云服务器、云数据库RDS和负载均衡等。 | 本身免费，详情参见[产品计费](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |
| 交换机vSwitch | [交换机（vSwitch）](https://help.aliyun.com/zh/vpc/create-and-manage-vswitch)是组成专有网络的基础网络模块，用来连接不同的云资源。成功创建交换机后，您可以在交换机中创建云资源、绑定自定义路由表或者绑定网络ACL。 | 免费，详情参见VPC[产品计费](https://help.aliyun.com/zh/vpc/product-overview/product-billing)。 |
| 弹性公网IP(EIP) | [弹性公网IP（Elastic IP Address，简称EIP](https://help.aliyun.com/product/61789.html)）是可以独立购买和持有的公网IP地址资源。目前，EIP仅支持绑定到专有网络类型的ECS实例、专有网络类型的私网SLB实例、专有网络类型的辅助弹性网卡、NAT网关和高可用虚拟IP上。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/eip/product-overview/billing)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| Terraform Explorer | Terraform Explorer 是一款面向 Terraform 的在线调试工具，可以帮助开发者实现 0 门槛体验 Terraform，让「自动化」更轻松。 |

## 安全性

### 应用实时服务监控ARMS访问控制

应用实时监控服务，借助访问控制RAM的RAM用户，您可以实现权限分割的目的，按需为RAM用户赋予不同权限，并避免因暴露阿里云账号密钥造成的安全风险，相关介绍参见[访问控制概述](https://help.aliyun.com/zh/arms/security-and-compliance/overview-8)和[使用RAM进行访问控制](https://help.aliyun.com/zh/arms/security-and-compliance/use-ram-for-access-control/)。

### 可观测可视化 Grafana 版访问控制

可观测可视化 Grafana 版可以借助RAM角色实现跨账号授权及资源访问的控制，相关介绍参见[访问控制](https://help.aliyun.com/zh/grafana/security-and-compliance/access-control/)。

### VPC安全性

专有网络VPC具有安全可靠、灵活可控、灵活可用以及较强的可扩展性，详情参见[产品优势](https://help.aliyun.com/zh/vpc/product-overview/benefits)及[访问控制](https://help.aliyun.com/zh/vpc/access-control)。

## 注意事项

### Terraform Provider版本

本次实施中，使用的Terraform Provider版本为1.240.0。

## 实施步骤

### 实施准备

- 确保已有相关阿里云账号，并有足够访问控制权限（详见“安全性”章节的各个访问控制说明）。

### 实施规划

本次实施中，我们用阿里云的一个单独的地域模拟线下IDC环境：

- 首先，在阿里云上一个单独的地域（本例中为青岛）构建了一个Zabbix服务器和一个Zabbix Agent作为Zabbix的监控数据源，以此模拟线下IDC的Zabbix服务；此外，考虑到Zabbix服务搭建需要很多安装步骤和参数的调整，这里使用了terraform工具把所有命令行相关的配置通过脚本的形式实现了自动化部署；
- 然后，在阿里云应用实时监控服务ARMS中创建了一个Grafana工作区；
- 随后，配置线下IDC的Zabbix数据源接入到阿里云上创建的Grafana工作区；
- 为了体现云上云下统一监控，我们还配置了云上Prometheus监控接入到上述Grafana工作区；
- 最后，再把线下IDC Zabbix监控和云上Prometheus监控集成到同一个仪表盘文件夹。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972235.png)

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：60分钟。

### 操作步骤

#### 1. 用terraform部署Zabbix Server和Agent

##### 1.1. 用阿里云Terraform Explorer创建调试任务并创建资源

确保已登录阿里云账号（并保证有足够的权限），并浏览器访问[Terraform Explorer](https://api.aliyun.com/terraform)。

点击示例模板--创建模板--创建空白模板，填写模板名称和模板描述；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972240.png)

点击下图红框打开编辑模式；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972237.png)

贴入github[链接](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-ARMS-Grafana-integrate-Zabbix-Prometheus/main.tf)代码库中的main.tf中的代码；

点击发起调试；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972239.png)

点击预览并执行；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972241.png)

整个创建资源的过程大概需要3~5分钟，执行成功后，界面如下图；

点击执行详情，把日志拉到最底部，可以看到该terraform脚本设置的三个Outputs输出，其中第一个和第三个参数之后会用到。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972242.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972243.png)

##### 1.2. 进行Zabbix管理界面初始化配置

如下步骤需要通过浏览器白屏进行操作。

用浏览器访问上一步中的zabbix_Server_URL，本例中为 http://47.104.144.42/zabbix；

点击进入页面后的Next step；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972244.png)

下个页面再次点击Next step；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972245.png)

下个页面，Password输入terraform脚本中设置的密码 zabbix，其他参数保持默认，并点击Next step；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972246.png)

注：若想自定义上述密码，可修改terraform脚本中如下参数；

```
variable "mysql_zabbix_password" {
  default = "zabbix"
}
```

下个页面，Name输入zabbix，其他参数保持默认，并点击Next step；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972247.png)

下个页面再次点击Next step；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972249.png)

完成配置，点击Finish；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972248.png)

自动进入登录页面，默认的登录账号和密码为：Admin/zabbix，填入信息点击Sign in，请留意用户名密码的大小写；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972250.png)

注：为保障安全，登录后建议及时修改默认密码。

登录后可见控制台页面如下图；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972254.png)

可选操作：设置控制台界面为中文。

点击左边菜单栏的 User settings--Language--选择 Chinese(zh_CN)，再点击 Update 完成更新。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972251.png)

##### 1.3. 在Zabbix管理页面中加入被监控主机

点击左边菜单栏【配置】中的【主机】，点击【创建主机】；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972255.png)

【主机名称】设置成 zbx-agent01

【可见的名称】设置成 zbx-agent01-172.16.0.155

【群组】选择 Linux server

【Interfaces】的【IP地址】设置成172.16.0.155

这里的IP地址172.16.0.155，请按照terraform执行详情最后的Outputs中的zabbix_Agent_Private_IP的实际显示IP进行配置；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972252.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972256.png)

完成上述配置后，先不要点击添加；

请点击【模板】进入模板配置；

在链接新模板中，输入linux，选中“Template OS Linux by Zabbix agent”；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972257.png)

此时点击添加，完成配置。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972265.png)

管理平台会返回如下页面；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972253.png)

此时，点击左边栏监测--主机，可以看到zbx-agent01的可用性一栏中，ZBX为绿色，代表已成功接入；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972258.png)

点击最新数据，也可以看到该Agent的相关监控数据，如下图；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972266.png)

#### 2. 在阿里云应用实时监控服务ARMS中创建Grafana工作区

访问阿里云[可观测可视化 Grafana 版](https://www.aliyun.com/product/aliware/grafana)产品页面，点击如下购买按钮。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972267.png)

在工作区购买页面设置以下参数，然后单击**立即购买**。

| 配置项 | 设定值 |
| --- | --- |
| **工作区名称** | Grafana云上云下统一监控 |
| **Admin 密码** | Test@12345 |
| **地域** | 上海 |
| **版本** | 开发者版 |
| **Grafana版本号** | Grafana 10.0.X |
| **用户账号数量** | 1个用户账号 |
| **购买时长** | 1个月 |
| **到期自动续费** | 不勾选 |
| **资源组** | 默认不填 |
| **标签** | 默认不填 |

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972259.png)

确认订单并完成支付。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972268.png)

随后，访问[Grafana服务的工作区管理](https://ags.console.aliyun.com/#/grafana/workspace)或者通过登录[ARMS控制台](https://arms.console.aliyun.com/?spm=a2c4g.11186623.0.0.7e684046oDQ6o7#/home)，在左侧导航栏选择**Grafana服务 > 工作区管理**进入如下页面。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972270.png)

点击上图红框，进入如下页面；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972260.png)

访问上图的【公网地址】的链接，通过用户名密码：admin/Test@12345完成登录；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972271.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972261.png)

#### 3. 配置线下IDC Zabbix数据源接入Grafana

##### 3.1. 配置Zabbix数据源

单击Grafana首页左上角的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972273.png)图标。

在grafana左侧导航栏，单击**管理--数据源**。

在**数据源**页面，单击**Add new data source**。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972276.png)

在**Add data source**页面的搜索框中搜索并单击**Zabbix**。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972262.png)

在**Settings**页面设置以下参数。

| 参数 | 说明 | 示例值 |
| --- | --- | --- |
| **Name** | 自定义数据源名称。 | Zabbix-IDC |
| **URL** | Zabbix服务地址。 | `[zabbix_Server_URL]/api_jsonrpc.php`本例中为：`http://47.104.144.42/zabbix/api_jsonrpc.php` |
| **Username** | Zabbix服务账号。 | 默认：Admin |
| **Password** | Zabbix服务密码。 | 默认：zabbix |

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972263.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972278.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972280.png)

其他参数保持默认不动，点击Save&test；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972264.png)

点击后得到test结果如下；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972282.png)

##### 3.2. 使用Zabbix数据源创建Grafana仪表盘

在上一步的相同页面中（或者从**管理--数据源--Zabbix-IDC**重新进入该页面），回到页面最上方，点击Dashboards；

然后点击“Zabbix Template Linux Server”右侧的Import；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972269.png)

得到如下结果；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972283.png)

单击Grafana首页左上角的![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972272.png)图标；

在grafana左侧导航栏，单击**仪表盘**。

在页面中，单击“Zabbix Template Linux Server”进入该仪表盘；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972285.png)

得到如下页面；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972286.png)

已经可以看到zbx-agent01的监控数据，如上图；

Group如果选择Zabbix servers，也可以看到Zabbix服务器的监控数据，如下图。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972287.png)

至此，线下IDC的Zabbix数据源已成功接入到阿里云上Grafana统一监控大盘。

#### 4. 配置云上Prometheus数据源接入Grafana

##### 4.1. 新建Prometheus实例并配置主机监控

访问[应用实时监控服务ARMS](https://arms.console.aliyun.com/)，选择上海区域；

在Prometheus监控--实例列表--接入数据--基础设施中选择主机监控；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972274.png)

选择想要监控ECS主机所属的VPC，在本例中，我上海VPC1中有两台ECS，因此我选择该VPC。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972288.png)

其他配置保持默认，点击确定开始配置；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972275.png)

完成配置后，点击接入管理；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972289.png)

可得如下界面，可以看到该VPC下两台ECS，已经安装了相应的探针和服务组件；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972290.png)

##### 4.2. 将Prometheus监控集成到Grafana

访问[应用实时监控服务ARMS](https://arms.console.aliyun.com/)，通过Grafana服务--工作区管理，进入之前创建的Grafana工作区，如下图；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972291.png)

选择刚刚创建的Prometheus监控服务，并点击对应的【集成】，如下图；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972292.png)

点击确认；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972277.png)

完成后效果如下图；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972294.png)

此时我们点击Grafana公网地址可再次访问Grafana统一监控页，如上图红框；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972295.png)

此时，在Grafana仪表盘中，已经可以看到云上ECS相关监控；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972296.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972279.png)

#### 5. 将线下IDC Zabbix监控和云上Prometheus监控集成到同一仪表盘文件夹

在Grafana管理页面的仪表盘中，点击“Env-VPC-上海VPC1-cn-shanghai”--Settings；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972297.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972298.png)

将文件夹名改为“云上云下统一监控”，并点击Save；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972281.png)

在仪表盘页面，单击“Zabbix Template Linux Server”进入仪表盘，并点击下图红框的仪表盘设置；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972299.png)

点击Folder，下拉框中选择“云上云下统一监控”，然后点击左上角“Save dashboard”;

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972300.png)

点击Save；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972293.png)

点击Save as；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972301.png)

点击Save；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972302.png)

至此，在“云上云下统一监控”下，可以同时看到线下IDC Zabbix和云上Prometheus的Dashboard。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972305.png)

## 源代码

### 代码介绍

该代码通过terraform自动化脚本部署:

- 一台ECS作为Zabbix Server服务器提供监控服务;
- 一台ECS作为Zabbix Agent,它是Zabbix Server的监控对象和数据来源;
- 相关必要的VPC、交换机、安全组。

### 代码地址

代码地址详见如下[链接](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/solution-ARMS-Grafana-integrate-Zabbix-Prometheus/main.tf)。

## 方案卸载

在Terraform Explorer页面中点击“销毁资源”，如下图；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972303.png)

等待几分钟，出现预览结果“成功”，点击“执行”，进行资源销毁；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8086581571/p972304.png)

等待出现执行结果“成功”，如下图，即可；此时，之前通过Terraform创建的资源会全部释放掉；

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7086581571/p972306.png)

其他通过控制台白屏创建的资源和配置，也按需删除或释放即可。

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-283（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
