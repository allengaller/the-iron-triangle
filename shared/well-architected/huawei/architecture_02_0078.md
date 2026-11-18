<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0078.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES11-04 灾难演练

通过容灾演练，可以验证灾备系统是否可用，且数据丢失时间以及恢复时间符合数据的RPO与RTO指标要求。

灾难演练着重测试服务跨AZ或跨Region故障转移能力，验证系统的容灾能力以及面对灾难时的应对能力，涉及到多个团队间配合，通常作为专项开展。容灾演练可以帮助企业更好地验证RPO、RTO指标，及时发现和解决相关问题，提高系统的可用性和可靠性。

- **风险等级** 高
- **关键策略** 模拟AZ故障或Region故障场景，并基于容灾切换手册进行恢复演练 演练结束后，检查RPO/RTO指标是否符合预期；当不符合预期时，调整系统容灾方案，重新进行灾难演练
- **相关云服务和工具** MAS多活高可用服务灾难演练：支持同城跨AZ灾备/双活、两地三中心及异地多活等场景下的业务高可用容灾管理、工作流编排及演练切换功能。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0078.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
