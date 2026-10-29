<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_05_0035.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# COST07-02 释放闲置资源

- **风险等级** 中
- **关键策略** 持续监控资源的闲置情况（如ELB无流量，EVS盘无挂载，EIP没有绑定到虚机），释放资源，或者监控资源使用只是在某个固定的时间(如每天的十二点，每个周末），可以使用自动化的方式定期申请资源，使用后释放
- **相关服务和工具** 华为云优化顾问，提供成本维度的巡检，识别ECS、EIP、EVS、ELB等闲置资源。 华为云[成本中心](https://support.huaweicloud.com/intl/zh-cn/cost/index.html)，除识别ECS、EIP、EVS、ELB等闲置资源外，还基于历史消费提供节省评估。您可参考系统给出的利用率信息、预估月度节省，结合业务团队意见，采取资源优化行动。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_05_0035.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
