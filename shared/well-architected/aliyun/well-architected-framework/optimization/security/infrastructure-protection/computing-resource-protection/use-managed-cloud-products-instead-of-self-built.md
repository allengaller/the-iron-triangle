<!-- source: https://help.aliyun.com/zh/well-architected/use-managed-cloud-products-instead-of-self-built -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2925687 -->

# 使用托管云产品，而非自建

在云原生时代，企业应优先选择云厂商提供的托管产品和服务，而非自建或自行维护基础设施和中间件。托管云产品通过自动化运维、内置安全机制、弹性扩展能力和全生命周期管理，显著降低企业安全管理和运营成本，使团队能够专注于核心业务创新。

## 优先级

低

## 不推荐做法

- 自建数据库、消息队列、容器集群等，未充分利用云上提供的产品和服务，容易出现安全和稳定性隐患，增加运营成本。比如，企业在云上自建数据库，需要手动部署高可用架构、备份、灾备、性能调优。容易出现数据库版本过时导致漏洞暴露以及容量规划失误导致服务中断的情况。
- 未定期关注阿里云产品动态，无法及时了解相关产品的新功能和服务。

## 实施指南

1. 您可以从以下维度评估是否采用云上已有产品和服务，尽可能的优先使用云上已有产品和服务：功能需求：云产品能力是否满足业务所需。成本对比：云产品收费是否优于自建方案的总成本（包括硬件、人力、故障成本）。迁移可行性：如果涉及迁移工作，需要评估是否能与现有系统进行无缝或者低成本的对接，比如API兼容性、数据迁移工具。SLA要求：云产品可用性和性能是否满足业务 SLA。
2. 在消息中心中，配置通知方式和消息接收人，确保重要消息能够及时获取。详细操作，请参见[基本消息接收管理](https://help.aliyun.com/zh/account/basic-message-receiving-management)。
3. 通过以下渠道，获取阿里云产品和业务的最新动态：[官网公告](https://www.aliyun.com/notice)[产品动态](https://www.aliyun.com/product/news)[开发者社区](https://developer.aliyun.com/)

---

> 原页面：https://help.aliyun.com/zh/well-architected/use-managed-cloud-products-instead-of-self-built（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
