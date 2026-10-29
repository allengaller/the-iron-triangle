<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_06_0041.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# OPS07-01 创建可操作的告警

- **风险等级** 高
- **关键策略** 告警需要做出响应，遵循告警可操作原则。消除无需响应的告警， 比如：磁盘IO 量瞬间飙升，CPU 使用率瞬间飙高，这类告警无需做出响应，对业务而言，意义就不大了。 遵循可操作性原则能避免很多误报。并且要定期统计和分析告警频率，识别高频告警，解决告警问题，清除明确的告警误报。
- **设计建议** 优化告警阈值：适当提高 内存／CPU／网络 IO 告警阈值。 优化日志级别：优化不合理的日志级别，把部分 ERROR 级别的日志调整为 WARNING。 屏蔽某些日志：对难以调整日志级别的应用，根据关键字屏蔽某些频繁的日志告警。 预警增强：对于某些影响业务方的操作，提供预警。 增强紧急预警：有些硬件故障会出现反应在 /var/log/messages 中，根据关键字匹配硬件类告警，以便及时处理。
- **相关云服务和工具** [应用运维管理 AOM](https://www.huaweicloud.com/intl/zh-cn/product/aom.html) [云运维中心 COC](https://support.huaweicloud.com/intl/zh-cn/coc/index.html) [云监控服务 CES](https://support.huaweicloud.com/intl/zh-cn/ces/index.html)

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_06_0041.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
