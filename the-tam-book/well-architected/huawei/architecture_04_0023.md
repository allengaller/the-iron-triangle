<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0023.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# PERF03-05 选择合适类型的存储云服务

- **风险等级** 中
- **关键策略** 在架构设计过程中，根据业务场景、数据特征等因素，选择相应的存储服务。目前可供您选择的有三种数据存储服务，分别是云硬盘、弹性文件服务（Scalable File Service, SFS）以及对象存储服务（Object Storage Service, OBS），这三种数据存储的主要区别如下： 对比维度 弹性文件服务 对象存储服务 云硬盘 概念 提供按需扩展的高性能文件存储，可为云上多个云服务器提供共享访问。弹性文件服务就类似Windows或Linux中的远程目录。 提供海量、安全、高可靠、低成本的数据存储能力，可供用户存储任意类型和大小的数据。 可以为云服务器提供高可靠、高性能、规格丰富并且可弹性扩展的块存储服务，可满足不同场景的业务需求。云硬盘就类似PC中的硬盘。 存储数据的逻辑 存放的是文件，会以文件和文件夹的层次结构来整理和呈现数据。 存放的是对象，可以直接存放文件，文件会自动产生对应的系统元数据，用户也可以自定义文件的元数据。 存放的是二进制数据，无法直接存放文件，如果需要存放文件，需要先格式化文件系统后使用。 访问方式 在ECS/BMS中通过网络协议挂载使用，支持NFS和CIFS的网络协议。需要指定网络地址进行访问，也可以将网络地址映射为本地目录后进行访问。 可以通过互联网或专线访问。需要指定桶地址进行访问，使用的是HTTP和HTTPS等传输协议。 只能在ECS/BMS中挂载使用，不能被操作系统应用直接访问，需要格式化成文件系统进行访问。 使用场景 如高性能计算、媒体处理、文件共享和内容管理和Web服务等。 ![](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/zh-cn_image_0000001943121244.png)说明： 高性能计算：主要是高带宽的需求，用于共享文件存储，比如基因测序、图片渲染这些。 如大数据分析、静态网站托管、在线视频点播、基因测序和智能视频监控等。 如高性能计算、企业核心集群应用、企业应用系统和开发测试等。 ![](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/zh-cn_image_0000001970399705.png)说明： 高性能计算：主要是高速率、高IOPS的需求，用于作为高性能存储，比如工业设计、能源勘探这些。 容量 PiB级别 EiB级别 TiB级别 时延 3~10ms 10ms 亚毫秒级 IOPS/TPS 单文件系统 10K 千万级 单盘 128K 带宽 GiB/s级别 TiB/s级别 MiB/s级别 是否支持数据共享 是 是 是 是否支持远程访问 是 是 否 是否能单独使用 是 是 否 云服务链接 [SFS官网](https://www.huaweicloud.com/intl/zh-cn/product/sfs.html) [OBS官网](https://www.huaweicloud.com/intl/zh-cn/product/obs.html) [EVS官网](https://support.huaweicloud.com/intl/zh-cn/productdesc-evs/zh-cn_topic_0044524691.html)

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_04_0023.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
