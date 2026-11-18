<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0140.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 可靠性功能

#### 集群HA

DCS服务提供主备、Proxy集群、Cluster集群实例，通过节点冗余方式实现实例容灾，当检测到主节点故障后，快速切换到备节点并自动恢复，在异常检测和恢复期间，可能会影响业务，时间在半分钟内。

#### 数据备份和恢复

DCS支持将当前时间点的实例缓存数据备份并存储到OBS中，以便在缓存实例发生异常后能够从备份数据进行恢复。DCS实例支持定时和手动两种备份方式，定时备份频率以天为单位，最多保存7天，但至少会保留一个数据备份文件；手动备份由用户触发，通常在执行业务系统维护、升级等高危操作进行，保存期限无限制。

DCS指定备份集恢复。恢复过程中，实例会有一段时间不能处理客户端的数据操作请求，当前数据将被删除，待恢复完成后存储原有备份数据。

详见“[备份与恢复说明](https://support.huaweicloud.com/intl/zh-cn/usermanual-dcs/dcs-ug-0713010.html)”。

#### 跨AZ容灾

DCS提供的主备、Cluster集群、Proxy集群实例支持跨AZ容灾，当一个AZ异常时，另一个AZ节点不受影响，备节点会自动升级为主节点，对外提供服务。

#### 监控告警

配合CES服务，支持对DCS的CPU、内存、磁盘、网络等进行监控和告警。

详见“[支持的监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-dcs/dcs-ug-0713011.html)”。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0140.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
