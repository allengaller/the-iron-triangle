<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0065.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# Spark性能优化

**概述**

Spark是基于内存的分布式计算框架。在迭代计算的场景下，数据处理过程中的数据可以存储在内存中，提供了比MapReduce高10到100倍的计算能力。Spark可以使用HDFS作为底层存储，使用户能够快速地从MapReduce切换到Spark计算平台上去。Spark提供一站式数据分析能力，包括小批量流式处理、离线批处理、SQL查询、数据挖掘等，用户可以在同一个应用中无缝结合使用这些能力。

Spark的特点如下：

- 通过分布式内存计算和DAG（无回路有向图）执行引擎提升数据处理能力，比MapReduce性能高10倍到100倍。
- 提供多种语言开发接口（Scala/Java/Python），并且提供几十种高度抽象算子，可以很方便构建分布式的数据处理应用。
- 结合SQL、Streaming、MLlib、GraphX等形成数据处理栈，提供一站式数据处理能力。
- 完美契合Hadoop生态环境，Spark应用可以运行在Standalone、Mesos或者YARN上，能够接入HDFS、HBase、Hive等多种数据源，支持MapReduce程序平滑转接。

**集群服务部署规划**

**服务规模与业务容量参数配置对照表**

- Spark作为内存计算引擎，需要更多的内存和CPU。用户在规划规格时，应根据当前的业务容量和增长速度，规划合理的内存和CPU资源，特别需要关注以下几点：
- 当程序运行在yarn-client模式下时，需要关注在driver端汇聚的数据量大小，根据自己的业务场景，为driver设置合理的内存。
- 根据自己的业务目标，规划CPU资源和内存资源。规划时，需要结合当前的数据分布情况，业务复杂度，设置“executor-memory”，“executor-cores”，“Executor-num”，并在此基础上，规划需要的CPU核数和内存大小。
- 在规划内存时，要预留一定量的内存空间作为操作系统的buffer cache，一般预留20%。
- 从HDFS中读入数据时，要考虑block解压缩后的数据膨胀。
- 规划一定的磁盘作为缓存空间，包括缓存数据、日志、Shuffle数据。

**调优原则**

- 提高cpu使用率同时减少额外性能开销。

- 提高内存使用率。

- 优化业务逻辑，减少计算量和IO操作。

**典型业务的调优**

- 优化代码逻辑：在进行Spark参数调优之前，要进行相应的规划设计，优化代码逻辑。
- Spark任务跑的比较慢，cpu利用率低：检测室executor线程不能全部吃满，此时应减少每个executor的core数量，增加executor个数，同时增加partition个数。
- 任务容易出现内存溢出：部分数据分片较大，单个task处理数据过大，或者executor中并行度不足，单个task内存不足导致。此时应减少executor数量，增大数据分片。
- 数据量少，但小文件数量多：减少数据分片，在reduce算子后执行coalesce算子，以减少task数量，减少cpu负载。
- 使用spark sql查找一个大表，表列数较多，但是查找的列较少：尽量使用rcfile或parquet格式，减少文件读取成本，同时选择合适的压缩格式，减少内存负载。

**指标观测方法**

性能衡量指标包括吞吐量、资源利用率、伸缩性。

- 吞吐量：在相同资源环境下，执行相同计算任务，查看任务的完成速度
- 资源利用率：执行计算任务，查看在不同负载情况下，cpu、内存、网络的使用率。
- 伸缩性：

− 横向扩容带来的性能提升曲线：增加资源，执行相同计算任务，查看性能提升比率。

− 增加系统负担带来的性能下降曲线：在相同资源环境下，增加计算负载，查看性能下降比率

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0065.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
