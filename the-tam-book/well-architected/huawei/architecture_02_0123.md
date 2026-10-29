<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0123.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# 概述

本章节介绍常用云服务的可靠性功能与故障模式，以便应用系统能充分利用云服务提供的可靠性能力，提升应用系统的可靠性，并能针对云服务的常见故障模式，进行故障恢复处理，以便最大限度减少故障，并能从故障中恢复。

| 云服务 | 简介 | 链接 |
| --- | --- | --- |
| ECS弹性云服务器 | 弹性云服务器（Elastic Cloud Server，ECS）是由CPU、内存、操作系统、云硬盘组成的基础的计算组件。弹性云服务器创建成功后，就可以像使用自己的本地PC或物理服务器一样，在云上使用弹性云服务器。 | [ECS弹性云服务器](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0124.html) |
| BMS裸金属服务器 | 裸金属服务（Bare Metal Server，BMS）是一款兼具弹性云服务器和物理机性能的计算类服务，为企业提供专属的云上物理服务器，为核心数据库、关键应用系统、高性能计算、大数据等业务提供卓越的计算性能以及数据安全。 | [BMS裸金属服务器](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0127.html) |
| CCE云容器引擎 | 云容器引擎（Cloud Container Engine，简称CCE）提供高度可扩展的、高性能的企业级Kubernetes集群，支持运行Docker容器。借助云容器引擎，可以在云上轻松部署、管理和扩展容器化应用程序。 | [CCE云容器引擎](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0130.html) |
| ELB弹性负载均衡 | ELB弹性负载均衡是将访问流量根据分配策略分发到后端多台服务器的流量分发控制服务，支持独享型负载均衡与共享型负载均衡： 独享型负载均衡：独享型负载均衡实例资源独享，实例的性能不受其它实例的影响，可根据业务需要选择不同规格的实例。 共享型负载均衡：属于集群部署，实例资源共享，实例的性能会受其它实例的影响，不支持选择实例规格。 | [ELB弹性负载均衡](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0133.html) |
| AS弹性伸缩 | 弹性伸缩（Auto Scaling，以下简称AS）是根据用户的业务需求，通过设置伸缩规则来自动增加/缩减业务资源。当业务需求增长时，AS自动增加弹性云服务器（ECS）实例或带宽资源，以保证业务能力；当业务需求下降时，AS自动缩减弹性云服务器（ECS）实例或带宽资源，以节约成本。AS支持自动调整弹性云服务器和带宽资源。 | [AS弹性伸缩](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0136.html) |
| DCS分布式缓存服务 | 分布式缓存服务（Distributed Cache Service，简称DCS）是华为云提供的一款兼容Redis的高速内存数据处理引擎，可提供即开即用、安全可靠、弹性扩容、便捷管理的在线分布式缓存能力，满足用户高并发及数据快速访问的业务诉求。 | [DCS分布式缓存服务](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0139.html) |
| DMS分布式消息服务 | DMS分布式消息服务支持以下各种消息类型： Kafka版：基于开源社区版Kafka提供的消息队列服务，向用户提供计算、存储和带宽资源独占式的Kafka专享实例。 RabbitMq版：完全兼容开源RabbitMQ，提供即开即用、消息特性丰富、灵活路由、高可用、监控和告警等特性，广泛应用于 流控、系统解耦等场景。 RocketMQ版：低延迟、弹性高可靠、高吞吐、动态扩展、便捷多样的消息中间件服务。 | [DMS分布式消息服务](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0142.html) |
| RDS云数据库 | 云数据库RDS（Relational Database Service，简称RDS）是一种基于云计算平台的稳定可靠、弹性伸缩、便捷管理的在线云数据库服务。 | [RDS云数据库](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0145.html) |
| 云数据TaurusDB云数据库 | 云数据库 云数据库 TaurusDB是华为自研的最新一代企业级高扩展高性能分布式数据库，完全兼容MySQL。基于华为最新一代DFV存储，采用计算存储分离架构，128TB的海量存储，故障秒级切换，既拥有商业数据库的高可用和性能，又具备开源低成本效益。 | [云数据库 TaurusDB云数据库](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0148.html) |
| OBS对象存储服务 | 对象存储服务（Object Storage Service，OBS）是一个基于对象的海量存储服务，提供海量、安全、高可靠、低成本的数据存储能力。 | [OBS对象存储服务](https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0151.html) |

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0123.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
