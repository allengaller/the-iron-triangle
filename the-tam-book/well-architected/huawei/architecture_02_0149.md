<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0149.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 可靠性功能

#### 集群HA

云数据库 TaurusDB服务支持主节点+只读节点的高可用架构，当主节点故障时，系统会自动切换到只读节点，只读节点提升为主节点，原来故障的主节点也会自动恢复为只读节点。

云数据库 TaurusDB服务还支持异构容灾实例(MySQL节点)，支持在极端场景，如社区未知bug、用户误操作、AZ级故障导致服务无法正常提供服务等场景，可以快速将服务切换到异构容灾实例继续提供服务。

#### 数据备份和恢复

云数据库 TaurusDB实例支持自动备份和手动备份，您可以定期对数据库进行备份，当数据库故障或数据损坏时，可以通过备份文件恢复数据库，从而保证数据可靠性。

云数据库 TaurusDB支持同区域备份与跨区域备份；跨区域备份是将备份文件存放到另一个区域存储，某一区域的实例故障后，可以在异地区域使用备份文件在异地恢复到新的云数据库 TaurusDB实例，用来恢复业务。

详见“[备份原理](https://support.huaweicloud.com/intl/zh-cn/usermanual-taurusdb/taurusdb_03_0052.html)”。

#### 自动扩缩容

云数据库 TaurusDB服务支持自动扩缩容，可自动扩缩规格和增删只读节点。

详见“[设置自动变配（自动扩缩容）](https://support.huaweicloud.com/intl/zh-cn/usermanual-taurusdb/taurusdb_03_0023.html)”。

#### 跨AZ容灾

云数据库 TaurusDB实例支持将实例的节点分别部署在多个可用区。

云数据库 TaurusDB也支持通过数据迁移服务DRS支持Region内跨AZ双主灾备，与跨Region容灾相同。

#### 跨Region容灾

云数据库 TaurusDB支持使用数据复制服务（Data Replication Service，简称DRS）创建灾备任务，当主实例所在区域发生突发性自然灾害等状况，主节点（Master）和备节点（Slave）均无法连接时，可将异地灾备实例切换为主实例，在应用端修改数据库链接地址后，即可快速恢复应用的业务访问。数据复制服务提供的实时灾备功能，可实现主实例和跨区域的灾备实例之间的单主灾备或双主灾备。

详见“[云数据库 TaurusDB到云数据库 TaurusDB单主灾备](https://support.huaweicloud.com/intl/zh-cn/realtimedr-drs/drs_03_1119.html)”和“[云数据库 TaurusDB到云数据库 TaurusDB双主灾备](https://support.huaweicloud.com/intl/zh-cn/realtimedr-drs/drs_04_0129.html)”。

#### 监控告警

配合CES服务，支持对云数据库 TaurusDB的CPU、内存、磁盘、网络等进行监控和告警。

详见“[支持的监控指标](https://support.huaweicloud.com/intl/zh-cn/usermanual-taurusdb/taurusdb_03_0085.html)”。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0149.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
