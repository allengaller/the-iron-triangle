<!-- source: https://help.aliyun.com/zh/well-architected/manage-service-quotas-across-multiple-accounts-and-regions -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2968696 -->

# 跨多个账户和区域管理服务配额

随着企业对高可用性、灾备恢复能力的需求日益增长，越来越多的应用部署在多个账户与多个地域中。在阿里云平台上，每个服务在不同地域和账户中都存在默认的**服务配额**（Service Quotas）和资源限制。如果这些配额未在所有环境中保持一致性，可能会导致**故障转移失败**或**服务中断**。

## 优先级

高

## 不推荐做法

- 手动单独设置不同账号、不同区域的资源配额。
- 未定期评估所有地域和账户的配额使用情况。
- 未利用配额模板统一管理多地域配额。
- 忽略故障转移场景下的配额需求。

## 实施指南

### 1. 统一配额管理

1. **审查当前账户和地域的配额使用情况**，识别是否存在服务配额偏差；
2. **使用阿里云配额中心或 CloudMonitor 查看配额使用率**，是否接近 80% 或 90%；
3. 对于多账号场景，需要通过资源目录将多账号统一纳管；
4. 在资源管理账号内开启配额模板；
5. 在配额模板中批量为成员账号申请配额；

## 相关资源

### 相关文档

- [Alibaba Well-Archited Framwork稳定性支柱](https://help.aliyun.com/zh/well-architected/overview-7)
- [配额模板](https://help.aliyun.com/zh/quota-center/user-guide/quota-templates/)
- [云服务使用限制索引](https://help.aliyun.com/zh/quota-center/product-overview/limits-of-alibaba-cloud-services)

---

> 原页面：https://help.aliyun.com/zh/well-architected/manage-service-quotas-across-multiple-accounts-and-regions（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
