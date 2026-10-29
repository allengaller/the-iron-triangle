<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0017.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# PERF03-01 选择合适类型的计算云服务

- **风险等级** 中
- **关键策略** 根据应用的特征选择合适的计算云服务。选择计算云服务主要考虑以下两个因素： 应用本身的部署形态 上云时，业务的迁移方式（例如：业务是简单的迁移上云，还是本身要做改造） 如果业务本身在IDC部署模式是虚拟机部署，应用系统比较老旧，业务本身也没有改造的计划，建议按照原来IDC的部署模式，采用ECS或者BMS的形式进行应用部署，以满足应用和业务本身的性能诉求。 如果借助上云的机会业务侧也会做容器化和微服务的改造，上云时选择容器化（CCE/CCI）进行部署。 如果本身业务已经是微服务化的形式，建议上云时考虑容器服务（CCE/CCI）进行部署。
- **相关服务和工具** 弹性云服务器 ECS 裸金属服务器 BMS 云容器引擎 CCE 云容器实例 CCI

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0017.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
