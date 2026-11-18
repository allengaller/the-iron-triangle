<!-- source: https://help.aliyun.com/zh/well-architected/program-identity-management/ -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706129 -->

# 程序身份管理

程序身份通常代表应用程序或服务，往往是通过阿里云的OpenAPI来访问云上的资源和数据。在阿里云上，针对程序身份的管理，基于安全的最小化原则，核心有两大原则：缩短暴露时长和缩小暴露面积。

- 缩短暴露时长：尽可能使用临时凭据STS Token替代固定凭据AccessKey，即使使用固定凭据，也建议定期轮转。
- 缩小暴露面积：尽可能安全的保管凭据，同时避免在不同身份类型之间混用凭据。

## 最佳实践

- [为不同的工作负载和环境分配不同的凭据](https://help.aliyun.com/zh/well-architected/sec02-bp01-assign-different-credentials-to-different-workloads-and-environments)
- [使用临时凭据替代固定凭据](https://help.aliyun.com/zh/well-architected/sec02-bp02-prefer-temporary-credentials)
- [定期审查和轮转固定凭据](https://help.aliyun.com/zh/well-architected/sec02-bp03-periodic-review-and-rotation-of-fixed-credentials)
- [在存储和使用过程中对凭据进行加密](https://help.aliyun.com/zh/well-architected/sec02-bp04-encryption-of-credentials-during-storage-and-use)
- [对固定凭据进行集中化管控](https://help.aliyun.com/zh/well-architected/sec02-bp05-centralized-control-of-fixed-credentials)

---

> 原页面：https://help.aliyun.com/zh/well-architected/program-identity-management/（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
