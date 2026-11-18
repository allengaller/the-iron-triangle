<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0019.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES01-03 云服务器反亲和

应用内相同业务的ECS需要分散到多台物理服务器，避免运行到同一台物理服务器上，当发生这种情况时，可能会由于一台物理服务器故障而导致业务中断。

- **风险等级** 高

- **关键策略** 针对多个承载相同业务的ECS，需要配置主机组反亲和，从而可以将相同业务的ECS调度到不同物理服务器上，以避免由于单台物理服务器故障而导致所有业务不可用的场景。 若ECS通过AS进行弹性伸缩时，则需要AS配置云服务器组反亲和，以避免AS自动创建的ECS运行在同一个物理服务器上。 若CCE集群节点或节点池采用弹性云服务器ECS时，建议配置云服务器组反亲和，以避免CCE集群中的ECS节点运行在同一个物理服务器上。
- **相关云服务和工具** 弹性云服务器 ECS：云服务器组 弹性伸缩服务 AS 云容器引擎 CCE

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0019.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
