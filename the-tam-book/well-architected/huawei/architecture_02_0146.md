<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0146.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 可靠性功能

#### 集群HA

RDS服务支持HA主备高可用架构，故障秒级自动切换。

#### 数据持久性

RDS数据持久性高达99.9999999%，保证数据安全可靠，保护业务免受故障影响。

#### 数据备份和恢复

RDS支持每天自动备份数据，备份都是以压缩包的形式自动存储在对象存储服务（Object Storage Service，简称OBS）。备份文件保留732天，支持一键式恢复。用户可以设置自动备份的周期，还可以根据自身业务特点随时发起备份，选择备份周期、修改备份策略。

支持按备份集和指定时间点的恢复。在大多数场景下，用户可以将732天内任意一个时间点的数据恢复到云数据库RDS新实例或已有实例上，数据验证无误后即可将数据迁回云数据库RDS主实例，完成数据回溯。

详见“[备份原理及方案](https://support.huaweicloud.com/intl/zh-cn/usermanual-rds-mysql/rds_08_0047.html)”。

#### 存储自动扩容

RDS支持存储空间自动扩容，在实例存储空间达到阈值时，会触发自动扩容。

详见“[存储空间自动扩容](https://support.huaweicloud.com/intl/zh-cn/usermanual-rds-mysql/rds_05_0039.html)”。

#### 跨AZ容灾

RDS支持跨AZ高可用。当用户购买实例的时候，选择主备实例类型，可以选择主可用区和备可用区不在同一个可用区（AZ）。

详见“[云数据库RDS支持跨AZ高可用吗](https://support.huaweicloud.com/intl/zh-cn/rds-mysql_faq/rds_faq_0073.html)”。

RDS for MySQL也支持通过数据迁移服务DRS支持Region内跨AZ双主灾备，与跨Region容灾相同。

#### 跨Region容灾

RDS支持使用数据复制服务（Data Replication Service，简称DRS）创建灾备任务，当主实例所在区域发生突发性自然灾害等状况，主节点（Master）和备节点（Slave）均无法连接时，可将异地灾备实例切换为主实例，在应用端修改数据库链接地址后，即可快速恢复应用的业务访问。数据复制服务提供的实时灾备功能，可实现主实例和跨区域的灾备实例之间的单主灾备双主灾备。

详见[MySQL到MySQL单主灾备](https://support.huaweicloud.com/intl/zh-cn/realtimedr-drs/drs_04_0122.html)和[MySQL到MySQL双主灾备](https://support.huaweicloud.com/intl/zh-cn/realtimedr-drs/drs_04_0127.html)。

#### 监控告警

配合CES服务，支持对RDS的CPU、内存、磁盘、网络等进行监控和告警。

详见“[支持的监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-rds-mysql/rds_06_0001.html)”。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0146.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
