<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_05_0021.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# COST03-03 公共成本分配

- **风险等级** 中
- **关键策略** 跨团队共享使用的CDN、直播带宽应按照各业务团队的实际带宽占比，将带宽费用拆分到不同的业务团队。 跨团队共享使用的CCE集群服务，应按照各团队分配和使用的CPU/内存等比例，将容器集群成本（包含CCE、ECS、EVS等服务成本）拆分到各个业务团队。 以上公共成本，以及其他共享资源&平台服务&服务支持&未及时标记产生的未分配成本，也可以按照一定的比例规则，比如平均分配、按消费比例分配、按约定比例分配等规则，拆分到各个业务部门，从而满足各团队或业务部门公平分配公共成本的需求 ![](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/zh-cn_image_0000001964545725.png)
- **相关服务和工具** 华为云成本中心的[成本单元](https://support.huaweicloud.com/intl/zh-cn/usermanual-cost/costcenter_000015_01.html)提供按比例的公共成本分拆方式。 华为云成本中心提供[共同成本分拆](https://support.huaweicloud.com/intl/zh-cn/usermanual-cost/costcenter_000002_06.html)，支持CDN、Live按照域名流量进行成本分拆。 华为云[CCE服务](https://www.huaweicloud.com/intl/zh-cn/product/cce.html)提供细化的按照Pod Level的成本分拆，并可以卷积到Workload，Service等各种标准K8S模型层级。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_05_0021.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
