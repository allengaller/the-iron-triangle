<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_06_0016.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# OPS02-02 关联源代码版本和部署的应用版本，使用代码质量最佳实践

- **风险等级** 高

- **关键策略** 在代码开发阶段，需要开展代码协作设计和管理。使用现代化的代码仓管理代码，确保代码合并后，代码将保持一致，并且不会丢失任何更改。通过正确的版本控制，同时，现代化的代码仓可以方便设置代码版本，关联源代码版本和部署的应用版本，在运维阶段，一旦部署在云上的应用发生任何问题，可以方便回溯到源代码，而且方便使用上一版本的源代码回滚到上一版本的应用。 其次，在软件开发生命周期内，推动开发人员采用代码质量最佳实践，例如，使用代码审查或结对编程等最佳实践来提高代码质量，确保每行代码在合入代码仓时，都有两个以上的工程师审查过，同时，通过设置代码合入策略进行代码控制，确保代码审查规范的执行。最后，建议通过自动化代码检查策略进行代码问题检查。

- **相关云服务和工具** [华为云CodeArts Check服务](https://www.huaweicloud.com/intl/zh-cn/product/codecheck.html) [华为云CodeArts Repo服务](https://www.huaweicloud.com/intl/zh-cn/product/codehub.html)

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_06_0016.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
