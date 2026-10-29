<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0064.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# HIVE优化

**概述**

Hive架构

![](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/zh-cn_image_0000001980833437.png)

Hive提供了Hadoop的SQL能力，主要参考标准的SQL，Hive进行了部分的修改，形成了自己的特有的SQL语法HQL（Hive SQL），更加适合于Hadoop的分布式体系，该SQL目前是Hadoop体系的事实标准。

**Hive调优**

用户输入HQL，Hive将HQL进行词法解析，语法解析，之后生成执行计划，并对执行计划进行优化，最后提交任务给YARN去执行。所以Hive的调优分为以下几个部分：

- 接入层：主要包括用户的连接性能，如网络速度、认证、连接并发数。
- HiveServer：以SQL的优化为主，执行计划是SQL优化的主要手段，通过接口查看Hive对整个SQL语句是如何进行任务的分解和编排，并结合MapReduce/Spark的执行情况针对性地进行任务的优化。
- HiveMetaStore：因为Hive的MetaStore可能是外部的独立数据库，所以它的性能也会影响到整个HiveServer的性能，主要包括HiveMetaStore访问时间，访问次数，连接并发数。
- MapReduce/Spark：以该组件进行执行时，MapReduce/Spark执行的情况直接引影响到Hive的性能，如每个任务的大小，任务与资源分配均匀度，任务拆分合理度等。
- HDFS：最底层的IO读也是性能的关键，主要考虑的指标是读取和写入的性能，还包括块大小合理设置等。

其中MapReduce/Spark/HDFS组件有自己独立的调优手册及文档，请参考对应组件的调优。本文档重点讨论上述的1，2，3部分的性能调优的内容，并结合MapReduce/Spark的进行调优说明。

**批处理业务**

批处理主要特点是耗时时间长，消耗的资源比较多，主要的调优和设计推荐如下：

- 尽量使用ORC File， 配上合适的压缩算法， 主要可选的压缩算法为Zlib和Snappy。其中Zlib压缩比高，但压缩解压时间比Snappy长，消耗资源比如Snappy多。Snappy平衡了的压缩比和压缩解压的性能。推荐使用Snappy。
- 尽量使用Map Join减少Shuffle的次数，大幅提升性能
- 不同SQL语句，完成同一个功能，生成Map Reduce的数量越少越好
- Hive系统默认是典型的配置场景，结合业务实际情况，可以做一些参数的调整，如文件块的大小，Map个数与Reduce的个数，压缩算法等。
- 合理地使用分区，分区数量不要太多，查询的SQL尽量指定具体的分区值；

**衡量指标**

衡量指标主要用于查看相应的指标来发现Hive服务或执行过程中的一些问题，尽快能定位Hive的性能问题。通常我们查看指标的顺序应该是通用指标，接入层指标，HiveMetaStore，HiveServer相关指标，其它相关组件的指标（如MapReduce/Spark/HDFS）。下面列举目前可查看到的相关指标信息：

- 通用指标

主要是指通用的服务器的相关性能指标：CPU使用率，内存占用量，磁盘IO读写速度，使用Core数量等，通过这些指标可以衡量任务在该类型机器或该机器上的执行情况，观察集群各机器的通用指标，可以看到集群的负载是否均衡。

- 接入层指标

Hive连接数，并行SQL数量，输入缓存值（或每批大小）。单HiveServer实例可以处理的最大并发数可以通过参数控制，默认是500，该参数主要受JVM内存和CPU的处理能力的限制。

- HiveMetaStore

HiveMetaStore连接数，并行SQL数量，语句执行计划。

- HiveServer

主要查看SQL语句的执行计划，进行SQL相关的调优，并结合MapReduce/Spark引擎的相关参数，主要是Job数量，Map数量，Reduce数量。

- 通用测试标准

Hive性能上业界主要是拿TPC-DS来跟同类型的产品或者自己的老版本进行对比。标准测试仅作为性能测试的一些参考。

**指标观测方法**

- 通用指标的观测

集群机器的CPU，内存，IO的使用情况可以通过Manager的主机管理界面查看到所有Host的资源使用情况。

- 接入层指标的观测

Manger的服务->Hive服务状态页面可以查看到相关的HiveServer的连接数，HQL的执行成功的统计信息。

- HiveMetaStore指标的观测

在Manager的服务->Hive服务状态页面，查看HiveMetaStore当前的请求连接数量以及关键API性能。

- HiveServer相关指标的观测

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0064.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
