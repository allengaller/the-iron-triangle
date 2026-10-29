<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0018.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# PERF03-02 选择合适规格的虚拟机和容器节点

- **风险等级** 中
- **关键策略** 服务器资源就类似一块块资源拼成的木桶，其最多能承载的业务需求取决于哪一块资源最先达到瓶颈。 不同应用对资源需求不同，例如： 功耗密集型业务（如高性能计算、人工智能、深度学习等场景）主要就是消耗计算维度的容量。 内存密集型业务（如大数据处理、图像/视频处理、游戏开发、数据库等场景）主要消耗内存和存储维度的容量。 存储密集型业务（如大型数据库、大数据分析、大规模文件存储、编译构建等场景）可能会比较消耗存储的带宽。 ![](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/zh-cn_image_0000001970397093.png) 根据业务的特征选择合适的虚拟机类型和规格。 具体的虚拟机类型规格请参考[官方文档](https://support.huaweicloud.com/intl/zh-cn/productdesc-ecs/zh-cn_topic_0035470096.html)。
- **相关云服务和工具** 弹性云服务器 ECS 裸金属服务器 BMS

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0018.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
