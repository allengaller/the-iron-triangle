<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0119.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 概述

电子商务类应用用于外部客户，需要提供较高的可用性，并能承受组件故障，其可用性目标通常要求达到99.99%，即每年故障时间可以为52.56分钟。

假定故障中断与变更中断的时长分别如下：

- 故障中断：假定每年故障中断3次，每次应急恢复决策时长为10分钟，恢复处理时长为5分钟，则每年故障中断时长为45分钟。
- 变更中断：假定应用支持金丝雀部署或蓝绿部署，并自动完成，软件更新不中断业务。

按照以上评估，每年应用系统不可用的时长是45分钟，满足可用设计目标要求。

电子商务类应用典型架构为前端无状态应用层+后端数据库，其中前端无状态应用可采用ECS或CCE；后端数据库基于不同业务类型可采用不同数据库，通常采用RDS for MySQL；同时通常还会使用DCS、Kafka等中间件及DDS文档数据库；为满足对应的可用性目标，建议采用以下方案。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0119.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
