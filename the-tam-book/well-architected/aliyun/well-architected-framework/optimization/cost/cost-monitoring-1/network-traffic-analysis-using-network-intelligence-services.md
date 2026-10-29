<!-- source: https://help.aliyun.com/zh/well-architected/network-traffic-analysis-using-network-intelligence-services -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 3023481 -->

# 进行网络流量分析

阿里云的网络智能服务（Network Intelligence Service，简称NIS），是一个对网络进行健康分析、性能监控、诊断修复、流量分析和测量仿真的云服务，通过集成机器学习、知识图谱等AIOps方法减少网络使用复杂性，提供自助运维能力，方便网络架构师和运维工程师更高效地设计和使用网络。

NIS提供了流量分析器，可以将网络日志接入流量分析器。流量分析器将基于用户自定义的关键参数，包括流量采样间隔（控制数据采集频率）、聚合维度（如按ECS实例、地域或协议分类）以及数据存储时长（决定历史分析深度）智能生成多维度、高精度的可视化流量分析图表。这些图表不仅支持实时监测网络资源使用状况与运行健康度，还提供灵活的时间范围筛选功能，使用户能够精准查看指定周期内的核心指标，例如带宽峰值利用率、数据包传输速率、TOP N流量源/目的地排名以及公网流量分布详情。更重要的是，该分析能力深度赋能网络运维优化：最终通过流量模式分析优化带宽成本并降低费用支出。

## 优先级

高

## 不推荐做法

- 当内网VPC互访流量过大时，造成TR成本显著上升，未启用NIS进行流量分析，导致无法找到“流量刺客“，整体架构和成本优化无从下手

## 实施指南

启动流量分析器：

- 优化网络性能：面向互联网、跨地域、跨VPC等场景，为网络架构优化和容量规划提供数据支撑。
- ﻿定位网络问题：在突发流量时，快速定位到具体的流量，缩短故障排查时间。
- ﻿保障网络安全：通过分析流量细节（如五元组信息），识别非预期的网络连接和潜在的安全威胁。
- ﻿网络成本优化：快速定位TOP N流量，并提供按城市、运营商、IP、协议、VPC实例等多维度视图，为网络分账和成本优化提供数据支撑。

## 相关资源

- [流量分析器（商业版）](https://help.aliyun.com/zh/nis/user-guide/traffic-analyzer/)
- [VPC流量分析](https://help.aliyun.com/zh/nis/user-guide/view-vpc-traffic-analysis-details)

---

> 原页面：https://help.aliyun.com/zh/well-architected/network-traffic-analysis-using-network-intelligence-services（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
