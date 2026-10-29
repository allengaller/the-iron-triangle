<!-- source: https://help.aliyun.com/zh/well-architected/solution-273 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929432 -->

# 云上自助成本分析方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972334.png)

当企业用云到达一定规模，云上的成本管理也会越来越复杂。原先基于云产品、地域、

随着企业云上业务的不断扩展，传统的成本管理方式已难以满足现代企业的需求。单纯依赖产品账单、地域账单等基础维度进行成本分析，已无法全面反映企业真实的资源使用情况和业务价值。为了更精准地实现成本管控，企业需要将云上成本与内部团队结构、业务数据以及实际运营需求深度结合。这种多维度的成本自助分析能力，不仅能够帮助企业更清晰地洞察资源消耗与业务产出的关系，还能为优化资源配置、提升运营效率提供有力支持。在云成本管理日益复杂的今天，构建一套灵活、精细且贴合企业自身需求的成本分析体系，已成为企业数字化转型过程中不可或缺的一环。

本文档介绍了一种通过MaxCompute+QuickBI在云上实现的自助成本分析方案。

## 方案优势

### 基于原始数据自助分析

通过直接对接云平台的原始账单数据，为企业提供了高度灵活的自助分析能力。企业可以根据自身业务特点，自由组合分析维度，例如按团队、项目、环境（开发/测试/生产）、资源类型等进行多维拆解。

### 无需研发人员搭建成本平台

本技术方案采用开箱即用的设计理念，企业无需投入研发团队即可快速上手，大幅降低了技术门槛和人力成本。

## 客户场景

### 分析云计算成本数据与业务数据趋势

#### 场景描述

云资源的费用趋势与业务数据的趋势存在一定的关联性，如果出现不符合预期的费用趋势，说明在产品使用上出现异常

#### 适用客户

- 需要精细化成本管理的企业

### 分析多云成本数据

#### 场景描述

企业需要聚合多个平台上的账单数据按照统一的财务视角进行分析

#### 适用客户

- 使用多个云服务商的企业

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| Maxcompute | [MaxCompute](https://help.aliyun.com/zh/maxcompute/user-guide/what-is-maxcompute)是适用于数据分析场景的企业级SaaS（Software as a Service）模式云数据仓库，以Serverless架构提供快速、全托管的在线数据仓库服务，消除了传统数据平台在资源扩展性和弹性方面的限制，最小化用户运维投入，使您可以经济并高效地分析处理海量数据。 | 免费，详情参见[产品定价](https://help.aliyun.com/zh/maxcompute/overview-31)。 |
| 智能商业分析 Quick BI | [Quick BI](https://help.aliyun.com/zh/quick-bi/product-overview/introduction-to-quick-bi-1)——阿里云旗下产品，大数据的高效分析与展现平台。通过对数据源的连接，和数据集的创建，可对数据进行即时分析与查询。并通过电子表格或仪表板功能，以拖拽的方式进行数据的可视化呈现。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/quick-bi/product-overview/billing-methods-of-quick-bi)。 |

## 注意事项

### 账单数据延时

- 开通订阅成功之后，表结构在Maxcompute空间中立即可见，但是数据要等第2天才会推送；
- 可以订阅历史周期的数据，数据推送第2天推送；
- 订阅成功之后，数据每天下午18点前完成前一天的数据推送；

## 实施步骤

### 实施准备

- 已开通高级版及以上的quickBI

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：90分钟。

### 操作步骤

#### 账单数据投递到Maxcompute

1. 前往成本管理--成本分析--更多分析工具![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972346.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972333.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972347.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972335.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972349.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972336.png)
2. 找到订阅的表，地址：[https://maxcompute.console.aliyun.com/cn-shanghai/sql-express](https://maxcompute.console.aliyun.com/cn-shanghai/sql-express)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7486581571/p972337.png)
3. 查看表的列信息![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972350.png)
4. 跑分析sql，地址：[https://da-cn-shanghai.data.aliyun.com/query](https://da-cn-shanghai.data.aliyun.com/query)先在我的文件下创建一个一个文件：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7486581571/p972338.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7486581571/p972339.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972351.png)比如查询按财务单元纬度查看应付费用的sql：`select SUM(require_amount),resource_user_id,finance_unit_name FROM cost_mgt_1261829428813528.split_item_detail_for_billing_period
where ds='202405'
group BY resource_user_id,finance_unit_name`![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972340.png)

#### 使用QuickBI构建数据大盘

1. 在QuickBI中新建数据源![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972341.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7486581571/p972342.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972353.png)数据库地址：连接MaxCompute项目的URL，外网或经典网络，推荐采用经典网络连接（如网络不通，需关闭白名单限制），提升连接速度，并避免在外网访问中可能产生的额外费用。请根据Project所在地域选择对应的Endpoint（地域请登录MaxCompute控制台点击左上角查看），所有VPC Endpoint地址参考：[https://help.aliyun.com/zh/maxcompute/user-guide/endpoints#section-oit-45y-23z](https://help.aliyun.com/zh/maxcompute/endpoints)其他链接方式参考：各地域及网络下的Endpoint及Tunnel Endpoint对照表，请参见[各地域Endpoint对照表（公网连接方式）](https://help.aliyun.com/zh/maxcompute/endpoints)、[各地域Endpoint对照表（阿里云VPC网络连接方式）](https://help.aliyun.com/zh/maxcompute/endpoints)和[各地域Endpoint对照表（阿里云产品互联方式）](https://help.aliyun.com/zh/maxcompute/endpoints)。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7486581571/p972343.png)
2. 去quickBI的模版市场中选择需要的看板，并应用到自己的工作空间中![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972344.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972345.png)
3. 为模版替换数据集替换数据集，要选择自己的数据集进行替换，要先建立自己的数据集，阿里云的账单模版主要用到了两个数据，我们将基于这俩数据做数据集：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972348.png)做第一个数据集 分账账单按天汇总 的数据集：点击新建数据集：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972354.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972352.png)打开 批量配置，先对所有字段重新命名为中文，把描述字段的中文copy到字段原名字段：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7486581571/p972355.png)把金额相关的字段全部处理成 度量字段：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7486581571/p972362.png)更改度量字段类型为数字：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7486581571/p972356.png)更改出账日期字段的类型为日期![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972366.png)加工资源ID字段：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972367.png)字段表达式：`case 
when ([split_item_code] is null or [split_item_code]='' or [split_item_code]='-' or [split_item_code]='\N' ) 
then [instance_id]
else [split_item_code] end`加工 资源名称 字段：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972357.png)字段表达式：`case 
when ([split_item_name] is null or [split_item_name]='' or [split_item_name]='-' or [split_item_name]='\N' ) 
then [instance_nick]
else [split_item_name] end`加工 消费可开票(元) 度量字段：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7486581571/p972369.png)字段表达式：`[应付金额]-[代金券抵扣金额]`加工 折后金额 字段：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972358.png)`[官网价]-[优惠金额]`过滤条件：ds 不为空的数据要全部拿出来（这里必须设置这个过滤条件，要不然会加载不出来数据）![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7486581571/p972368.png)保存数据集：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972370.png)应用数据集：分账分析模版替换数据集![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972371.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972359.png)注：如若遇到不匹配的，根据含义选择对应即可；替换完成后，查看分账报表；![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972372.png)如果针对某些图标格式不满意，可以直接点击编辑按钮，可以直接编辑，比如更改图表样式：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972360.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972373.png)更改仪表板名称，更改之后记得发布![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7486581571/p972361.png)做第二个数据集 计费项纬度的月汇总数据把 billing_item_detail_monthly 表拖到数据集中并把所有字段原名处理成中文：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7486581571/p972374.png)新增计算字段：消费可开票(元)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972375.png)字段表达式：`sum([应付金额(元)]-[代金券抵扣(元)]-[储值卡支付金额(元)]-
(case when ([信用额度退款抵扣(元)] is null) then 0 else [信用额度退款抵扣(元)] end)
)`新建计算字段：折后金额(元)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972363.png)字段表达式：`sum([目录总价(元)]-[优惠金额(元)])`新建计算字段：出账月![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972376.png)字段表达式：`BI_TODATE((BI_REPLACE([month], ' ', '-01')), 'yyyy-MM-dd')`注意：一定要确保替换的空白部分是 tab，鼠标选中是这个样子：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972377.png)否则这个字段是加工不出来的。处理日期的显示格式：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972378.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972379.png)新增计算字段：优惠折扣率![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972364.png)字段表达式：`case when (BI_SUM([目录总价(元)])>0) 
then 
sum([目录总价(元)]-[优惠金额(元)])/BI_SUM([目录总价(元)])
 else 0 end`过滤条件：ds 不为空的数据要全部拿出来（这里必须设置这个过滤条件，要不然会加载不出来数据）![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972380.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972365.png)替换消费分析模版的数据集：![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972381.png)匹配新做的数据集![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6486581571/p972382.png)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-273（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
