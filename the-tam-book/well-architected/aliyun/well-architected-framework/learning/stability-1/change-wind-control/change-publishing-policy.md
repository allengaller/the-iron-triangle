<!-- source: https://help.aliyun.com/zh/well-architected/change-publishing-policy -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2573875 -->

# 变更发布策略

通过合理的流量分配及部署策略，可将生产流量逐步切至已发布新版本的应用上实现灰度及快速回滚，以最大限度避免非预期的变更部署问题导致的影响。业界广泛采用的发布策略包括：

- 蓝绿发布：通过对服务新版本进行冗余部署实现。一般会将新版本的实例规格和数量与旧版本保持一致。当新版本服务验证通过后，将业务流量全部切至新版本。旧版本作为热备。如新版本上线后出现问题，可将流量全部切回至旧版本完成回滚，缩短故障恢复时间。
- A/B测试：通过用户请求的元信息将流量路由到新版本，是一种基于请求内容匹配的灰度发布策略。常见的做法包括基于HTTP Header和Cookie，将特定请求或用户灰度至新版本，降低故障影响范围。
- 金丝雀发布：通过调整流量权重比例，逐步将流量从老版本切换至新版本。同时对老版本服务进行缩容，对新版本进行扩容，相比蓝绿发布资源利用率较高。

阿里云[MSE云原生网关](https://help.aliyun.com/zh/mse/use-cases/implement-blue-green-deployment-a-or-b-testing-and-canary-release-by-using-mse-cloud-native-gateways)以托管的方式来做流量入口，提供丰富的流量治理能力，支持多种服务发现方式，如容器服务、MSE Nacos、MSE Zookeeper、EDAS注册中心、SAE注册中心、固定地址和DNS域名，并以统一的模型支持服务版本以及灰度发布能力。支持以上三种发布策略及应用无损上下线等功能。

---

> 原页面：https://help.aliyun.com/zh/well-architected/change-publishing-policy（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
