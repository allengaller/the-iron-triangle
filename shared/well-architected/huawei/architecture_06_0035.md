<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_06_0035.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# OPS06-03 制定和实施可观测性指标

- **风险等级** 高
- **关键策略** 指标是对时间周期内的测量数据的数值表示。可观测性指标是围绕发现率、定级准确率、定界时长、覆盖率、有效率、 一致率打造可观测能力，将可观测设计规范统一发布，统一设计要求与运维管理要求。
- **设计建议** 整体技术方案会变成标准并进行发布，各个业务系统架构师在设计时遵循这套标准，这样可以保证能力能够从设计态开始，包括运行态、高可用架构等场景中得到应用。 ![](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/zh-cn_image_0000001940304892.png) 可观测指标可以通过监控工具来实现，并允许在发生异常时发送警报。有很多监控工具可以使用，例如Prometheus、Grafana、Zabbix等，以及华为云提供的云监控服务CES。这些工具可以定期收集指标，提供可视化的指标报告，并且可以发送警报，以帮助组织及时发现问题。 可参考[CES的最佳实践](https://support.huaweicloud.com/intl/zh-cn/bestpractice-ces/ces_14_0002.html)。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_06_0035.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
