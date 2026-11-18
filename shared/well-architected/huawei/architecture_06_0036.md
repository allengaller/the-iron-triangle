<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_06_0036.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# OPS06-04 规范化应用日志

日志是随时间推移发生的不可变、记录时间戳的离散事件。系统需要记录关键事件和故障，以帮助诊断问题和解决故障。

- **风险等级** 高
- **关键策略** 对于一个系统来说，日志是非常重要的。它可以记录在系统中发生的一切，包括成功的操作、错误的操作、警告信息等等。因此，日志记录是可观测性设计中最基本的需求之一。通过将事件和错误信息记录到日志文件或数据库中，可以方便地进行故障排除和问题诊断。但是，仅仅记录日志并不足够，还需要对日志进行有效的管理和分析。如果日志太多，将会成为一个负担，因为它们需要占用存储空间，并且需要花费很长时间来查找有用的信息。因此，需要对日志进行过滤和归档，以便更好地管理它们。
- **设计建议** 可参考[LTS最佳实践](https://support.huaweicloud.com/intl/zh-cn/bestpractice-lts/lts_07_0020.html)

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_06_0036.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
