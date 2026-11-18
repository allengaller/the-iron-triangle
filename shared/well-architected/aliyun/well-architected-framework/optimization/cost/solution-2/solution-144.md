<!-- source: https://help.aliyun.com/zh/well-architected/solution-144 -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2929443 -->

# 存储资源成本优化方案

## 方案概述

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0486581571/p972498.png)

由于对云上存储资源管理粗放、不合理的使用方法、对资源计费缺乏足够了解等原因，企业在云上存储资源使用上存在浪费以及不适合自身实际的情况，用户会发现云上存储资源成本偏高、亟需优化。本文介绍了如何对对象存储服务OSS、日志服务SLS等云存储服务进行合理使用及治理，减少存储资源浪费、优化云上存储成本的方法。

## 方案优势

### 合理使用资源及成本节省

通过对存储资源用法、存储结构、资源生命周期等进行规划，引入适合企业自身的计费方式等方法，能够让企业用户更合理高效地管理存储的数据，减少云上存储资源浪费，节省相关存储资源的管理及存储成本。

## 客户场景

### 云上存储资源成本优化

#### 场景描述

由于对云上存储资源管理粗放、不合理的使用方法、对资源计费缺乏足够了解等原因，企业在云上存储资源使用上存在浪费以及不适合自身实际的情况，用户会发现云上存储资源成本偏高，甚至由于成本原因不再使用高成本的存储云产品，此时企业亟需对云上存储资源进行治理、对存储成本进行优化。

#### 适用客户

- 对云上存储成本敏感、有优化诉求的企业客户。
- 期望以更贴合自身实际、更优成本使用云上存储产品的企业客户。

## 方案架构

方案目前包括日志服务SLS、对象存储OSS的成本优化相关内容。通过规划数据存储的生命周期、优化存储结构、选用优惠资源包等方式，从成本优化角度切入，指导用户合理使用云上存储资源、帮助用户节省云上存储资源成本。

### SLS成本优化

#### 成本因素

通过日志服务的[计费项](https://help.aliyun.com/zh/sls/billable-items)，可以了解到日志服务的成本主要由以下几个因素决定。

- 每日导入的数据量。
- 数据存储的时间。
- 是否建立索引。

#### 智能冷热分层存储

日志服务提供冷存储功能，降低您长周期存储的成本，并同时保证日志的查询、分析、可视化、告警、投递和加工等能力不受影响。冷存储数据的存储费用按照冷存储的存储空间计费，冷热数据转换不会产生费用。

##### 功能说明

日志服务提供热存储和冷存储功能。

- 您可以在**Logstore属性**页面，开启[智能冷热分层存储](https://help.aliyun.com/zh/sls/enable-hot-and-cold-tiered-storage-for-a-logstore)功能，将热存储的数据转为冷存储。数据在Logstore热存储层中的存储时间，最少为30天。
- 您可以在开启智能冷热分层存储功能后，修改**Logstore属性**页面中的**热存储层数据保存时间**参数，将热存储的保存时间延长，实现将冷存储数据转回热存储。

相对热存储而言，冷存储数据的查询与分析性能有所降低，其余功能例如告警、投递、加工和可视化等不受影响。热存储和冷存储的主要区别如下：

| **对比项** | **热存储** | **冷存储** |
| --- | --- | --- |
| 适用场景 | 数据高频查询场景 | 数据低频查询场景 |
| 查询与分析性能 | 高，秒级返回。 | 较低，存在10秒延迟。 |
| 查询与分析费用（可能存在变化，[以官网说明](https://help.aliyun.com/zh/sls/enable-hot-and-cold-tiered-storage-for-a-logstore)为准） | SQL普通实例：无费用。SQL独享实例：收费。更多信息，请参见[开启SQL独享版](https://help.aliyun.com/zh/sls/dedicated-sql/)。 | SQL普通实例：无费用。SQL独享实例：收费。更多信息，请参见[开启SQL独享版](https://help.aliyun.com/zh/sls/dedicated-sql/)。 |
| 价格（可能存在变化，[以官网说明](https://help.aliyun.com/zh/sls/enable-hot-and-cold-tiered-storage-for-a-logstore)为准） | 0.0115元/GB/天 | 0.005元/GB/天 |

#### 使用数据加工优化存储架构

数据加工主要解决您规整数据的痛点以及帮助您进一步挖掘数据的价值，降低时间与人力成本。合理配置可以节约一定的成本。

##### 典型配置

根据[加工原理](https://help.aliyun.com/zh/sls/data-transformation-basics)和[性能指南](https://help.aliyun.com/zh/sls/performance-guide)，推荐您简化采集方案，使用一个或多个Logstore快速接入数据，然后使用数据加工进行快速分发，并根据实际需求设置不同目标Logstore的存储时间以及索引配置。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0486581571/p972500.png)

##### 优化存储结构

如果您持续采集某应用的日志，每天的写入量为100 GB，存储30天并建立全文索引，那么日志服务的成本大约是2248元/每月。

如果您更关心的是其中某一类POD的日志，例如操作日志与出错日志。假设这类日志的比例是20%，且希望存储30天。对其他的日志只需要存储7天。那么推荐您使用如下加工方案。

- 构建接入源Logstore，存储3天不建立索引。
- 构建目标Logstore1，用于存储操作日志与错误日志，存储30天并建立索引。
- 构建目标logstore2，用于存储一般性日志，存储7天并建立索引。

这种情况下您的成本约为1672元/每月，与加工之前相比大约可以节省25%的成本。

如果您的原始日志存储周期为60天，可以通过数据加工将只关心的20%的日志存储60天，其他日志存储7天即可，这样可以节约12%的成本， 并对关心的日志增加1倍存储时间。

##### 优化存储内容

如果您持续采集某应用的日志，每天的写入量为100 GB，存储30天并建立全文索引，那么日志服务的成本大约是2248元/每月。

如下为采集到的一条原始日志，大小为1021 Bytes。

```
__source__:  192.0.2.0
__topic__:  ddos_access_log
body_bytes_sent:  3866
cc_action:  none
cc_blocks:  
cc_phase:  
content_type:  text/x-flv
host:  www.example.com
http_cookie:  i1=w1;x2=q2
http_referer:  http://www.example.com
http_user_agent:  Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/192.0.2.1 Safari/537.36
http_x_forwarded_for:  192.0.2.2
https:  true
isp_line:  BGP
matched_host:  www.example.com
method:  GET
real_client_ip:  192.0.2.3
remote_addr:  192.0.2.4
remote_port:  48196
request_length:  2946
request_method:  GET
request_time_msec:  78920
request_uri:  /request/nvwlvvkhw
server_name:  www.example.com
status:  502
time:  2019-07-22T17:40:26+08:00
ua_browser:  mozilla
ua_browser_family:  
ua_browser_type:  
ua_browser_version:  9.0
ua_device_type:  
ua_os:  windows_7
ua_os_family:  
upstream_addr:  192.0.2.4:80
upstream_ip:  192.0.2.5
upstream_response_time:  0.858
upstream_status:  200
user_id:  st0s2b5
```

假设您只关心原始日志中的某些字段，则可以通过数据加工将关心的字段存储30天并建立索引，其他冗余字段仅存储3天即可。那么推荐您使用如下加工方案。

- 构建接入源Logstore，存储3天不建立索引。
- 构建目标Logstore，用于存储操作日志与错误日志，存储30天并建立索引。

假设每条日志经过加工后大小约为原来的60%，这种情况下您的成本约为1579元/每月，与加工之前相比大约可以节省30%的成本。

原始日志大小1021 Bytes，加工后日志如下所示，大小仅为618 Bytes。

```
__source__:  192.0.2.0
__topic__:  ddos_access_log
body_bytes_sent:  3866
content_type:  text/x-flv
host:  www.example.com
http_referer:  http://www.example.com
ua_browser:  mozilla
ua_browser_family:  
ua_browser_type:  
ua_browser_version:  9.0
ua_device_type:  
ua_os:  windows_7
http_x_forwarded_for:  192.0.2.2
matched_host:  www.example.com
method:  GET
real_client_ip:  192.0.2.3
request_length:  2946
request_uri:  /request/nvwlvvkhw
status:  502
upstream_addr:  192.0.2.4:80
upstream_ip:  192.0.2.5
upstream_response_time:  0.858
upstream_status:  200
user_id:  st0s2b5
```

#### 使用资源包

[SLS资源包](https://help.aliyun.com/zh/sls/overview-11)可用于抵扣日志服务所有的计费项，规格越大、包年期时长越长，价格优惠力度越大。系统每天会统计您使用的日志服务用量，在资源包额度范围内直接抵扣。当月额度被用完后，自动转为按量付费方式。

注意：

- 日志服务新版资源包的包年计划（1年期及以上版本），根据规格大小给予不同的折扣优惠，具体折扣以购买页面为准。按量付费方式的定价无变化，只有购买新版资源包（1年期及以上版本），才享受预付计划2.0的优惠策略。
- 阿里云在您购买新版资源包时一次性收取费用。例如您要购买1年期、100 CU的新版资源包，则阿里云将在您购买当天一次性收取1年的费用。

如何选择资源包规格？

- 如果您每月的日志服务费用较为稳定，则您可以通过历史月账单来选择合适的资源包规格。例如，您的日志服务历史月账单（原始金额）都稳定在1000元左右，则您可以购买1000 CU的资源包。
- 如果您每月的日志服务费用波动较大，则您可以根据未来可能产生的日志服务费用来选择合适的资源包规格。

#### 降低索引流量费用

在日志服务使用过程中，用户可以通过以下方式降低索引流量费用。

- **关闭全文索引**：配置字段索引日志服务支持全文索引和字段索引。如果是全文索引，则日志字段名（Key）和字段值（Value）都将作为text类型存储，字段名和字段值都被计入在索引流量中。如果是字段索引，则long类型和double类型的字段名不记入在索引流量中，每个字段值占用的索引流量统一为8字节。使用字段索引，可降低索引流量费用。例如：
- 对**request_uri**字段设置了索引（text类型），字段值为**/request/path-2/file-7**，则字符串**request_uri**和**/request/path-2/file-7**都会被计入在索引流量中。
- 对**status**字段设置了索引（long类型），字段值为**400**，则字符串**status**不会被计入在索引流量中，**400**的索引流量统一为8字节。
- **仅对关键字段设置索引**：如果原始日志中包含了大量字段信息，其中只有部分字段用于查询与分析，则您只需为这部分字段建立索引。
- **关闭日志聚类：**开启日志聚类功能后，索引总流量增加10%，示例如下表所示：当您不再需要使用日志聚类功能时，请及时关闭日志聚类。更多信息，请参见[日志聚类](https://help.aliyun.com/zh/sls/logreduce)。

| **原始日志大小** | **索引比例** | **日志聚类功能产生的索引量** | **索引总流量** |
| --- | --- | --- | --- |
| 100 GB | 20%（20 GB） | 100 GB×10% | 30 GB |
| 100 GB | 40%（40 GB） | 100 GB×10% | 50 GB |
| 100 GB | 100%（100 GB） | 100 GB×10% | 110 GB |

#### 配置优化及其他建议

可以从以下方面考虑进行[费用优化](https://help.aliyun.com/zh/sls/cost-optimization)：

- **减少分区个数**：分区个数一个分区最大可以处理5M/s的数据。只有readwrite的分区会收费。请调整分区个数，使其正好能处理5M/s的数据，减少分区个数请合并分区。
- **合理设置数据保存周期及产品选用**：Logstore 数据保存周期针对您对日志的查询、存储的需求不同，建议您优化Logstore 数据保存周期。如果您收集日志是为了做流计算，建议您只使用LogHub，不创建索引。如果您需要经常查询最近90天的日志数据，偶尔查询90天前的数据，建议您把Logstore 数据保存周期调整到90天，同时把数据[导入MaxCompute](https://help.aliyun.com/zh/sls/shipping-logs-to-maxcompute-new-version/)。查询90天内数据，使用日志服务，查询90天前数据，使用MaxCompute。如果您对日志有长时间存储和备份的需求，建议您把[日志导入到OSS](https://help.aliyun.com/zh/sls/shipping-logs-to-oss-new-version/)。
- **使用Logtail**：有 Batch 与断点续传功能，在保障实时性的同时以最优算法传输数据。Logtail 消耗资源是开源软件（Logstash，FluentD）的1/4，减少CPU消耗。
- **大包写入**：API写入用户尽量使用64KB~1MB大包写入，减少请求次数。

#### 潜在优化项自动检测

可以通过OpenAPI自动化查询SLS配置，发现多账号场景下潜在的成本优化项：

- LogStore开启了永久存储。
- LogStore存储天数配置超过阀值。
- LogStore热存储天数超过阀值且未开启智能冷热存储。
- LogStore开启了全文索引。
- LogStore开启了日志聚类。

### OSS成本优化

#### 存储类型转换

OSS支持标准存储、低频访问、归档存储、冷归档存储四种[存储类型](https://help.aliyun.com/zh/oss/user-guide/overview-53/)，全面覆盖从热到冷的各种数据存储场景。四种存储类型[存储费用](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.659d7952ues183#/oss/detail/ossbag)依次降低，用户可以将非热门数据转换为低频访问、归档存储或冷归档存储，将不再需要访问的数据删除，让您更高效地管理您存储的数据，节省大量人力及存储成本。用户可以根据实际情况通过CopyObject的方式或[生命周期规则](https://help.aliyun.com/zh/oss/user-guide/overview-54/)自动转换方式进行文件（Object）的[存储类型转换](https://help.aliyun.com/zh/oss/user-guide/convert-storage-classes)。

以本地冗余存储类型的指标对比示例如下表，建议根据最低存储时间及使用场景规划存储类型转换，更多对比详情参见[存储类型对比](https://help.aliyun.com/zh/oss/user-guide/overview-53/)。

注意：下表中的价格等信息可能存在变化，实际请以官网为准。

| **对比指标** | **标准存储-本地冗余** | **低频访问-本地冗余** | **归档存储类型** | **冷归档存储类型** |
| --- | --- | --- | --- | --- |
| 存储费用 | 0.12元/GB/月 | 0.08元/GB/月 | 0.033元/GB/月 | 0.015元/GB/月 |
| 最小计量单位 | 无 | 64 KB | 64 KB | 64 KB |
| 最低存储时间 | 无 | 30天 | 60天 | 180天 |
| 数据取回费用 | 无 | 按实际获取的数据量收取，单位GB。 | 按实际解冻的数据量收取，单位GB。 | 按实际解冻时选择的数据取回能力及数据大小收取，单位GB。 |
| 适用场景 | 各种社交、分享类的图片、音视频应用、大型网站、大数据分析等业务场景。例如程序下载、移动应用等。 | 较低访问频率（平均每月访问频率1到2次）的业务场景。例如热备数据、监控视频数据等。 | 数据长期保存的业务场景。例如档案数据、医疗影像、科学资料、影视素材等 | 需要超长时间存放的极冷数据。例如因合规要求需要长期留存的数据、大数据及人工智能领域长期积累的原始数据、影视行业长期留存的媒体资源、在线教育行业的归档视频等。 |

##### 通过生命周期规则自动转换Object的存储类型

OSS生命周期管理（Lifecycle）提供Object Transition机制，支持自动转换文件存储类型。关于OSS支持的四种存储类型的更多信息。

###### 基于最后一次修改时间的存储类型转换

**使用场景举例**

- 某医疗机构的医疗档案，上传至OSS后半年内需要偶尔访问，半年后基本不再访问。可以通过设置生命周期规则，将已上传180天的医疗档案转为归档存储。
- 某公司服务热线的录音文件，上传至OSS后2个月内，需要作为数据统计及核查的依据，2个月后偶尔访问，半年后基本不再访问，2年后数据不再需要存储。可以通过设置生命周期规则，设置录音文件上传60天后转为低频访问存储，180天后转为归档存储，730天后删除。
- 某存储空间内有大量文件需要全部删除，但是手动删除每次仅可以删除最多1000个文件，比较麻烦。此时可以配置一条匹配整个Bucket的生命周期规则，设置一天后删除所有文件。此Bucket内的数据会在第二天被全部删除。

**转换说明**

- 本地冗余存储（LRS）

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0486581571/p972499.png)

本地冗余类型文件转换规则如下：当Bucket同时配置了转换为低频访问、转换为归档存储、转换为冷归档存储的策略，其转换周期必须满足以下条件：转换为低频访问的周期<转换为归档的周期<转换为冷归档的周期

- 标准存储（LRS）类型可转换为低频访问（LRS）、归档存储（LRS）和冷归档存储（LRS）类型。
- 低频访问（LRS）类型可转换为归档存储（LRS）和冷归档存储（LRS）类型。
- 归档存储（LRS）类型可转换为冷归档存储（LRS）类型。
- 同城冗余存储（ZRS）

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0486581571/p972502.png)

同城冗余类型文件转换规则如下：

- 标准存储（ZRS）类型可转换为低频访问（ZRS）类型。
- 标准存储（ZRS）类型可转换为冷归档存储（LRS）类型。
- 低频访问（ZRS）类型可转换为冷归档存储（LRS）类型。

更多信息，请参见[基于最后一次修改时间的生命周期规则介绍](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time)。

###### 基于最后一次访问时间的存储类型转换

**使用场景举例**

- 多媒体场景某网站的视频、图片存储在OSS上，历史数据会逐渐从热转冷。因此，您可能需要将网站内长时间不被访问的数据保存为低频访问类型。此外，部分数据距离上传时间已久，但仍然是热门访问数据，这部分数据需要继续保存为标准存储类型。在该场景下应选用基于最后一次访问时间的生命周期规则，用于自动识别冷热数据并进行分层存储，从而降低存储成本。
- 相册或网盘场景对于长时间没有访问的冷数据，希望设置自定义转储天数，自动将冷数据转为低频访问类型，并确保数据的实时访问。
- 生命科学场景基因测序生成的大量业务数据，往往需要根据数据的最后访问时间而非最后修改时间来判断数据的冷热。按以往，客户只能手动通过日志分析或其他方式进行数据冷热的分层管理。但如果选用基于最后一次访问时间的生命周期规则，则可实现由服务端根据最后访问时间来自动识别冷热数据并实现数据分层存储。不仅如此，您还可以在同一条生命周期规则中同时结合最后访问时间与最后修改时间的策略，从而更灵活地进行数据管理。

**转换说明**

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0486581571/p972503.png)

以上规则适用于LRS类型Object之间、ZRS类型Object之间的转换。

- 基于最后一次访问时间的生命周期规则支持将Object从标准存储类型转为低频访问类型，您还可以选择当Object被访问后是否自动转回标准存储类型。
- 基于最后一次访问时间的生命周期规则支持将Object从标准存储或低频访问类型转为归档或冷归档存储类型，也可以选择将Object从归档转为冷归档存储类型。

更多信息，请参见[基于最后一次访问时间的生命周期规则介绍](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-access-time)。

##### 通过CopyObject接口手动转换Object的存储类型

用户可以通过CopyObject接口，将Object覆写为指定的存储类型。

- 本地冗余（LRS）各存储类型之间可任意转换。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0486581571/p972501.png)
- 同城冗余（ZRS）仅支持标准存储（ZRS）和低频访问（ZRS）之间互相转换。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0486581571/p972505.png)

#### 使用生命周期管理删除历史版本

OSS存储空间（Bucket）开启版本控制后，针对数据的覆盖和删除操作将会以历史版本的形式保存下来。当Bucket累积了大量的历史版本或者过期删除标记时，可以结合生命规则删除不必要的历史版本以及过期删除标记，从而减少存储成本并有效提升列举Object的性能，详情参见[使用生命周期管理文件版本](https://help.aliyun.com/zh/oss/user-guide/configure-lifecycle-rules-to-manage-object-versions)。

#### 使用资源包

对于可准确预估资源使用量的情况下，建议购买[资源包](https://help.aliyun.com/zh/oss/resource-plan/)。例如您可以准确预估接下来的3个月内，您的阿里云账号下所有Bucket的标准（LRS）存储容量约为100 GB，您可以考虑购买100 GB、购买时长为3个月的标准（LRS）资源包用于抵扣存储容量费用。在存储容量相同的情况下，相比按量付费，使用存储包可节省更多的存储成本。

##### 常用资源包

OSS常用的资源包包括存储包以及下行流量包。

- 存储包根据文件的不同存储类型，OSS对存储在Bucket中的文件收取对应的存储容量费用，您可以购买不同的存储包用于抵扣对应的存储容量费用。关于OSS支持的存储包类型及抵扣说明，请参见[存储费用](https://help.aliyun.com/zh/oss/storage-fees)。
- 下行流量包当您通过公网访问或者下载Bucket中存储的文件时，还会产生外网流出流量，您可以购买下行流量包用于抵扣外网流出流量费用。关于下行流量包的抵扣说明，请参见[流量费用](https://help.aliyun.com/zh/oss/traffic-fees)。

##### 选购建议

**建议1：根据使用场景选择资源包类型**

常用的OSS资源包购买组合为存储包+下行流量包。存储包用于抵扣OSS存储和ECS快照的存储费用。下行流量包用于抵扣外网访问OSS文件的流量费用。

| **使用场景** | **用于抵扣的资源包** |
| --- | --- |
| 使用OSS存储文本、图片、音视频等文件，且存储类型为标准存储（本地冗余） | 标准（LRS）存储包 |
| 创建并保留ECS快照 | 标准（LRS）存储包 |
| 通过外网浏览或下载OSS里的文件 | 下行流量包 |

**建议2：根据账单的计费项选择资源包类型**

如果您已有OSS账单，建议您根据[明细账单](https://usercenter2.aliyun.com/finance/expense-report/expense-detail-by-instance)里的计费项选择您要购买的资源包类型。

例如，计费项为标准存储（本地冗余）容量，那么您可以购买标准（LRS）存储包抵扣该费用。

**建议3：根据账单的用量选择资源包规格**

如果您已有OSS账单，建议根据[明细账单](https://usercenter2.aliyun.com/finance/expense-report/expense-detail-by-instance)里的用量选择您要购买的资源包规格。

例如，标准存储（本地冗余）容量每小时的用量为40 GB，那么您可以购买40 GB的标准（LRS）存储包抵扣该费用。

**建议4：购买后仍然按小时扣费的排查方法**

1. 在[明细账单](https://usercenter2.aliyun.com/finance/expense-report/expense-detail-by-instance)页面，查看计费项的类型、用量、消费时间。
2. 在[资源包列表](https://usercenter2.aliyun.com/ri/summary?commodityCode=)页面，查看生效的资源包的类型、总量、生效时间。
3. 对比计费项和资源包。

| **问题示例** | **解决方案** |
| --- | --- |
| 账单有外网流出流量（NetworkOut）计费项，但资源包列表没有下行流量包。 | 购买下行流量包 |
| 账单有标准存储（本地冗余）容量计费项，但资源包列表没有标准（LRS）存储包。 | 购买标准（LRS）存储包 |
| 账单的标准存储（本地冗余容量）计费项每小时有100 GB用量，但资源包列表的标准（LRS）存储包总量为40 GB。 | 将标准（LRS）存储包规格升级至100GB |
| 账单产生于购买资源包之前。 | 无 |

#### OSS图片高级压缩

随着拍照设备分辨率及业务显示要求的提高，图片处理功能需要支持更加灵活且压缩率更高的图片格式，例如：HEIF、AVIF。但传统的图片编解码技术在处理这类格式图片时的效率较低，无法满足业务的实时性需求。针对此类需求，OSS推出了[图片高级压缩](https://help.aliyun.com/zh/oss/user-guide/advanced-compression-of-heif-or-avif-images)功能，能够更高效地将图片转换为HEIF或AVIF高压缩率格式，从而节省存储空间、节约存储成本。

说明：转换为高压缩率格式会收取一定的转换费用，详情参见[计费说明](https://help.aliyun.com/zh/oss/user-guide/advanced-compression-of-heif-or-avif-images)。

##### 使用示例

将JPEG格式的原图转换为HEIF格式，并将其分辨率缩放为923×600。

- **原图**：`https://image-demo-oss-zhangjiakou.oss-cn-zhangjiakou.aliyuncs.com/pics/compression-demo.jpeg`
- **将JPEG格式的原图转换为HEIF格式请求URL示例**：`https://image-demo-oss-zhangjiakou.oss-cn-zhangjiakou.aliyuncs.com/pics/compression-demo.jpeg?x-oss-process=image/format,heic`
- **将JPEG格式的原图转换为HEIF格式，并将其分辨率缩放为923×600请求URL示例**：`https://image-demo-oss-zhangjiakou.oss-cn-zhangjiakou.aliyuncs.com/pics/compression-demo.jpeg?x-oss-process=image/resize,l_923,h_600/format,heic`

下表列出了JPEG原图和转换后不同分辨率HEIF图片的大小。从表中可以看出，HEIF格式图片与JPEG相比具有超高的压缩率，能够有效节约成本。

| **格式** | **分辨率** | **大小** |
| --- | --- | --- |
| JPEG（原图） | 3924×2550 | 2.09 MB |
| HEIF | 3924×2550 | 268 KB（压缩率87.5%） |
| HEIF | 923×600 | 30.7 KB（压缩率98.6%） |

#### 加速器成本优化

开启[OSS加速器](https://help.aliyun.com/zh/oss/user-guide/overview-77/)后，您可以将需要重复读取的数据缓存在加速器中。当大数据计算向OSS加速器请求数据时，加速器根据空间大小提供1.6 Gbps/TB（即200 MBps/TB）的带宽，以满足大数据计算的带宽要求。在使用OSS加速器时，可以根据业务需求调整带宽容量，降低使用成本。

##### 成本优化案例

假设用户业务场景中存在日常任务、分析任务以及仿真任务三种任务类型，每种任务需要的带宽以及任务启动时间存在差异。任务带宽以及启动时间说明如下：

| **带宽使用** | **18：00** | **19：00** | **20：00** |
| --- | --- | --- | --- |
| 固定带宽（Gb/s） | 100 | 100 | 100 |
| 弹性带宽（Gb/s） | 80 | 40 | 90 |
| 日常任务（Gb/s） | 40 | 20 | 40 |
| 分析任务（Gb/s) | 40 | 20 | 40 |
| 仿真任务（Gb/s) | 0 | 0 | 10 |

为简化费用计算过程，以下费用均以20 元/GB/小时为例。

- 采用固定带宽费用：（100+100+100）GB/小时 x 20 元/GB/小时=6000元
- （推荐）采用弹性带宽费用：（80+40+90）GB/小时 x 20 元/GB/小时=4200元

##### 成本优化建议

基于以上计费模型以及成本优化案例得知，如果您可以在需要大量带宽的时间段提升带宽，在日常使用时减少带宽，则可以实现按需使用OSS加速器时，达到优化使用成本的目的。您可以参考以下方案按需调整带宽：

**根据任务需求的评估结果进行调整**

在可以准确评估任务日常运行时间和带宽需求的情况下，仅需要在任务启动时提高带宽，在任务结束时减少带宽。

**根据实时查询的带宽用量进行调整**

在无法准确预估任务日常运行的时间和带宽需求的情况下，可以通过OSS控制台或云监控实时查询当前的带宽，然后根据监控的带宽用量调整带宽。例如，当前的带宽配置为100 GB，最近15分钟仅使用了20 GB，则考虑适当减少带宽。

**参考通用规则进行调整**

您在使用OSS加速器时，可以考虑按照梯度扩容以及快速缩容的模式进行带宽调整。

**说明** 以下示例中定义的10分钟仅供参考，请结合实际业务场景进行相应替换。

- 梯度扩容假设10分钟内当前流量超出最大带宽的90%，建议将最大带宽提高10 Gbps。
- 快速缩容假设10分钟内当前流量均低于最大带宽的50%，建议减少带宽至当前流量。

#### 潜在优化项自动检测

可以通过OpenAPI自动化查询OSS配置，发现多账号场景下潜在的成本优化项。

- Bucket无生命周期规则。
- Bucket无启用的生命周期规则。

## 产品费用及名词

### 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| 日志服务SLS | [日志服务SLS](https://help.aliyun.com/zh/sls/what-is-log-service)是云原生观测与分析平台，为Log、Metric、Trace等数据提供大规模、低成本、实时的平台化服务。日志服务一站式提供数据采集、加工、查询与分析、可视化、告警、消费与投递等功能，全面提升您在研发、运维、运营、安全等场景的数字化能力。 | 收费，详情参见[产品定价](https://help.aliyun.com/zh/sls/billing-overview)。 |
| 对象存储OSS | [阿里云对象存储OSS（Object Storage Service）](https://help.aliyun.com/zh/oss/user-guide/what-is-oss)是一款海量、安全、低成本、高可靠的云存储服务。可以将移动应用、大型网站、图片分享或热点音视频的主要存储方式数据存储到阿里云OSS。 | 收费，详情参见[产品计费](https://help.aliyun.com/zh/oss/billing/)。 |

### 名词解释

| 名称 | 说明 |
| --- | --- |
| OSS生命周期规则 | 可以基于最后一次修改时间（Last Modified Time）以及最后一次访问时间（Last Access Time）的策略创建生命周期规则，定期将存储空间（Bucket）内的多个文件（Object）转储为指定存储类型，或者将过期的Object和碎片删除，从而节省存储费用。 |
| OSS存储类型 | 对象存储OSS提供标准、低频访问、归档、冷归档四种存储类型，全面覆盖从热到冷的各种数据存储场景，详情参见[存储类型介绍](https://help.aliyun.com/zh/oss/user-guide/overview-53/)。 |

## 安全性

### OSS安全性

OSS提供企业级多层次安全防护，包括服务端加密、客户端加密、防盗链、通过Bucket Policy限制IP黑白名单访问、细粒度权限管控、STS和URL鉴权和授权机制、WORM特性、日志审计等，详情参见OSS[数据安全](https://help.aliyun.com/zh/oss/data-security-11)。

### SLS安全性

阿里云日志服务具有丰富的安全防护能力，支持服务器端加密、细粒度权限管控、详细服务日志等特性，同时提供日志审计功能，针对主流云产品提供多账号下实时自动化、中心化采集云产品日志并实现审计。日志服务为您提供丰富的数据洞察能力，同时满足企业数据的安全与合规要求，详情参见[安全与合规概述](https://help.aliyun.com/zh/sls/overview)。

### 成本优化安全性

请详细阅读本文方案架构、注意事项、操作步骤等内容，了解成本优化对数据存储、使用方法及计费方面的影响，**充分了解影响面及风险后再确定是否要执行优化**。

## 注意事项

### 日志服务SLS

#### 产品计费

请仔细阅读SLS产品计费规则，详情参见[产品计费](https://help.aliyun.com/zh/sls/billing/)。

#### 智能冷热分层存储

- 缩短数据保存时间后，日志服务将在1小时后开始删除数据。但日志服务控制台首页的**存储量（日志）**将于次日更新。例如您原本的数据保存时间为5天，现修改为1天，则日志服务将在1小时候后开始删除前4天的数据。
- 修改**热存储层数据保存时间**后，日志服务将在1小时后生效。例如您原本的数据的热存储时间为30天，现修改为40天，则日志服务将在1小时候后开始将部分冷存储数据转回热存储。
- **热存储层数据保存时间**参数值要小于**数据保存时间**参数值。

### 对象存储OSS

#### 产品计费

请子婿阅读OSS产品计费规则，详情参见[产品计费](https://help.aliyun.com/zh/oss/billing/)。

#### 存储类型转换

当Object被转换为低频访问、归档存储和冷归档存储类型后，存在最小计量空间、数据取回费用等注意事项，更多信息请参见[OSS存储类型转换注意事项](https://help.aliyun.com/zh/oss/user-guide/convert-storage-classes)。

注意1：对开通了OSS-HDFS服务的Bucket，建议不要修改OSS-HDFS的数据存储目录**.dlsdata/**下任意Object的存储类型。如果您将**.dlsdata/**下任意Object的存储类型修改为低频类型时，通过OSS-HDFS可正常访问数据。如果您将Object存储类型修改为归档或冷归档后，通过OSS-HDFS无法访问数据。如需访问，您需要对数据进行解冻操作，解冻完成后再尝试访问数据。

注意2：访问低频访问类型的Object时，会根据实际访问量额外收取数据取回费用；解冻归档存储和冷归档存储类型的Object会额外收取数据解冻费用，此费用与流出流量费用是两个独立计费项。如果Object每月平均访问频率高于1次，Object转换成低频访问、归档存储或冷归档存储类型后的使用成本可能高于标准存储类型。

#### 生命周期费用说明

通过生命周期规则转换Object存储类型或者删除Object时会涉及请求费用，不足规定存储时长删除时会额外产生不足规定时长容量费用，更多详情请参见[生命周期费用说明](https://help.aliyun.com/zh/oss/user-guide/fees-related-to-lifecycle-rules)。

当低频访问、归档、冷归档存储类型Object在不足规定时长时通过生命周期策略提前删除，还会产生不足规定时长容量费用，例如：

- 通过生命周期将Object存储类型转换为低频访问或归档，且在不足规定时长前删除Object低频访问类型最低存储时间（30天）和归档类型最低存储时间（60天）均以Object存储在OSS的Last Modified时间开始计算。例如标准类型Object在其创建10天后，通过生命周期将其转换为低频访问类型，过了20天后将其转换为归档类型，再过5天将其删除。此时会产生25天的归档存储不足规定时长容量费用。

#### 基于最后一次访问时间的生命周期规则

- 基于最后一次访问时间的生命周期规则存在匹配条件及碎片过期等限制，详情参见[使用限制](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-access-time)。
- 基于最后一次访问时间的生命周期规则存在规则数量、最后一次访问时间更新策略及费用说明等注意事项，详情参见[注意事项](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-access-time)。

#### 基于最后一次修改时间的生命周期规则

- 基于最后一次修改时间的生命周期规则存在匹配条件及碎片过期等限制，详情参见[使用限制](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time)。
- 基于最后一次修改时间的生命周期规则存在规则数量、最后一次访问时间更新策略及费用说明等注意事项，详情参见[注意事项](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time)。

#### 通过CopyObject接口手动转换Object的存储类型

- 如果将Object修改为低频访问、归档存储、冷归档存储类型，Object会涉及最小计量空间64 KB、最短存储周期、数据取回费用等。更多信息，请参见[注意事项](https://help.aliyun.com/zh/oss/user-guide/convert-storage-classes)。
- 归档存储和冷归档存储类型的Object需要解冻后才可以修改存储类型。关于解冻Object的具体操作，请参见[解冻Object](https://help.aliyun.com/zh/oss/user-guide/restore-objects-for-access)。

#### 图片高级压缩

使用OSS图片高级压缩存在一些限制及转换收费，详情参见[前提条件](https://help.aliyun.com/zh/oss/user-guide/advanced-compression-of-heif-or-avif-images)及[计费说明](https://help.aliyun.com/zh/oss/user-guide/advanced-compression-of-heif-or-avif-images)。

### 白名单

#### OSS归档存储白名单

如果您需要将Object从标准存储或低频访问类型转换为归档或冷归档存储类型，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请转换为归档或冷归档类型的权限，申请通过后您需要指定转换的目标存储类型。

**重要** 工单申请通过后，如果您基于最后一次访问时间策略将Object从标准存储或低频访问类型转为归档或冷归档类型，则Bucket中归档或冷归档类型Object的最后一次访问时间默认为该Bucket开启访问追踪的时间。

#### OSS图片高级压缩

用户需[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请使用OSS图片高级压缩功能。

## 实施步骤

### 实施准备

- 已拥有阿里云账号，了解相关资源成本费用现状。
- 已阅读方案架构及注意事项章节，了解操作影响面及可能的风险。
- 如使用OpenAPI查询优化项，需已使用[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)多账号进行管理，需已拥有[Python](https://www.python.org/)运行环境且版本大于3.6。

### 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：90分钟。

### 操作步骤

根据方案架构中的介绍，结合**企业实际情况选择进行下述优化项**进行具体操作。

#### 潜在优化项自动检测

可检出的潜在优化项请参考方案架构章节说明。

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
pip install alibabacloud_sls20201230
pip install alibabacloud_oss20190517
```

##### 下载代码并进行配置

1. 下载[多账号存储资源优化项查询示例代码](https://github.com/aliyun/alibabacloud-landing-zone/blob/master/solution/finance/storage_risk_item.py)。
2. 配置代码中的AccessKey、企业管理账号UID、要查询闲置资源的成员账号UID以及要查询的地域ID等信息。`rd_management_account_access_key_id = 'yourAccessKeyId'
rd_management_account_access_key_secret = 'yourAccessKeySecret'
rd_management_account_readonly_role_name = 'readOnly'
rd_management_account_id = 'yourRdManagementAccountId'
rd_member_account_id_list = ['yourRdMemberAccountId', 'yourRdMemberAccountId']
region_id_list = ['cn-shanghai', 'cn-xxx']
# SLS存储天数阀值，LogStore存储天数大于该值则视为风险项
sls_ttl_threshold_days = 90

# SLS热存储天数阀值，LogStore热存储天数配置大于该天数且未配置智能冷热分层存储则视为风险项
sls_hot_ttl_threshold_days = 60`

##### 运行代码

在命令行执行命令`python3 storage_risk_item.py`，查看检测出的潜在优化信息。![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0486581571/p972504.png)

#### SLS成本优化

##### 费用评估

SLS费用预估计算可参考使用[价格计算器](https://sls.console.aliyun.com/lognext/calculator)，SLS价格计算器仅覆盖主要计费项（如shard等仅占少量费用及加工等按需使用的功能不包含），因此仅作为费用评估使用，不作为最终出账参考。

##### 开启智能冷热分层存储

操作步骤详情参见[开启智能冷热分层存储功能](https://help.aliyun.com/zh/sls/enable-hot-and-cold-tiered-storage-for-a-logstore)。

##### 通过数据加工实现成本优化

详细介绍参见[通过数据加工实现成本优化](https://help.aliyun.com/zh/sls/videos/cost-optimization-by-using-data-transformation)。

##### 选购资源包

操作步骤详情参见[选购资源包](https://help.aliyun.com/zh/sls/purchase-a-resource-plan)。

##### 配置索引

SLS配置索引操作步骤请参见[配置索引](https://help.aliyun.com/zh/sls/create-indexes)。

##### 投递日志到OSS

投递操作详情参见[投递日志到OSS](https://help.aliyun.com/zh/sls/shipping-logs-to-oss-new-version/)。

##### 投递日志到MaxCompute

投递操作详情参见[投递日志到MaxCompute](https://help.aliyun.com/zh/sls/shipping-logs-to-maxcompute-new-version/)。

#### OSS成本优化

##### 基于最后一次修改时间的存储类型转换

通过OSS控制台及SDK等方式进行存储类型转换，操作步骤详情参见[基于最后一次修改时间的生命周期规则介绍](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time)。

##### 基于最后一次访问时间的存储类型转换

通过OSS控制台及SDK等方式进行存储类型转换，操作步骤详情参见[基于最后一次访问时间的生命周期规则介绍](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-access-time)。

##### 通过CopyObject接口手动转换Object的存储类型

通过OSS控制台及SDK等方式进行存储类型转换，操作步骤详情参见[通过CopyObject转换存储类型操作方式](https://help.aliyun.com/zh/oss/user-guide/convert-storage-classes)。

##### 使用生命周期管理删除历史版本

通过生命周期设置删除历史版本，操作步骤详情参见[使用生命周期管理文件版本](https://help.aliyun.com/zh/oss/user-guide/configure-lifecycle-rules-to-manage-object-versions)。

##### 使用资源包

资源包购买操作步骤详情参见[资源包购买指南](https://help.aliyun.com/zh/oss/purchase-resource-plans)。

##### 高级图片压缩

高级图片压缩操作步骤详情参见[HEIF或AVIF图片高级压缩](https://help.aliyun.com/zh/oss/user-guide/advanced-compression-of-heif-or-avif-images)。

##### 加速器成本优化

根据任务需求的评估结果或根据实时查询的带宽用量进行加速器带宽调整**，**配置OSS加速器容量的具体步骤请参见[设置加速器](https://help.aliyun.com/zh/oss/user-guide/overview-77/)。

## 故障排除

### OSS成本优化

#### 基于最后一次访问时间的生命周期规则常见问题

问题排查详情参见[常见问题](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-access-time)。

#### 基于最后一次修改时间的生命周期规则常见问题

问题排查详情参见[常见问题](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time)。

#### 资源包选购及使用常见问题

资源包问题详情参见[常见问题](https://help.aliyun.com/zh/oss/package-faq/)。

### SLS成本优化

#### 数据加工

数据加工问题详情参见[常见问题](https://help.aliyun.com/zh/sls/data-transformation-faq/)。

#### SLS计费

SLS资源包及计费相关问题详情参见产品计费[常见问题](https://help.aliyun.com/zh/sls/bill-faq-8/)。

## 相关内容

- [OSS计费案例](https://help.aliyun.com/zh/oss/billing-examples)
- [SLS费用优化](https://help.aliyun.com/zh/sls/cost-optimization)

---

> 原页面：https://help.aliyun.com/zh/well-architected/solution-144（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
