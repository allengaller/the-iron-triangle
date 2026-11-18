<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0052.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# PERF06-01 分层看护

- **风险等级** 高
- **关键策略** 基于业务的部署架构，一般可以从最底层的硬件基础设施到最上层的应用分成5层资源，云上服务可以只需要关注虚拟网络、实例、应用三层。结合每一层资源的特征指标进行分层建模，分别设置不同梯度的性能看护指标。通常按照指标劣化程度可以设计成一般、紧急、重要三个梯度，对应每个梯度的指标配套对应的处理措施。对于敏感度或业务重要度的应用架构，可以新增一个提示级别的梯度。
- **相关云服务和工具：** 云监控服务 CES 应用运维管理 AOM 应用性能管理APM

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0052.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
