<!-- source: https://help.aliyun.com/zh/well-architected/use-bastion-machines-and-other-methods-for-workload-operation-and -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2925688 -->

# 使用堡垒机等方式进行工作负载的运维操作

在云原生架构中，直接通过公网开放 SSH 22 端口 登录服务器进行运维操作存在严重的安全隐患。堡垒机 是集中化运维管理的核心工具，通过统一入口、细粒度权限控制和全流量审计，能有效降低横向渗透攻击风险、满足合规审计要求，并提升运维效率。

## 优先级

高

## 不推荐做法

- 公网直接开放主机的SSH 22端口，攻击者可通过暴力破解或漏洞利用直接入侵。
- 多个人员共用一个密码或私钥来访问实例，导致责任难以追溯。
- 未记录运维操作记录，无法追溯异常行为。

## 实施指南

1. 使用阿里云[堡垒机](https://help.aliyun.com/zh/bh/bastionhost/product-overview/what-is-bastionhost)，进行计算资源的运维工作，避免人员身份直接接触计算资源。
2. 堡垒机支持多账号资产统一管理。如果您有多个阿里云账号，且需要一台堡垒机集中管理多个账号下的资产，可结合阿里云资源目录RD（Resource Directory）实现多账号资产的统一运维管控。详情，请参见[堡垒机多账号统一管理最佳实践](https://help.aliyun.com/zh/bh/bastionhost/use-cases/best-practices-for-unified-management-of-multiple-accounts-on-bastion-machines)。
3. 配置堡垒机身份认证。建议您将企业已有IdP的用户集成至堡垒机，以实现企业人员统一管理。详情，请参见[基于统一的IdP实现人员身份的统一认证](https://help.aliyun.com/zh/well-architected/sec01-bp05-unified-authentication-of-personnel-identity-based-on-unified-idp)，实现阿里云上有多个用户体系，比如：RAM身份、堡垒机用户、无影云桌面用户等，和企业IdP的统一SSO集成。
4. 使用堡垒机[运维审计](https://help.aliyun.com/zh/bh/bastionhost/user-guide/o-and-m-auditing/)能力，过对系统运维操作（系统登录日志、系统配置修改日志等）和资产运维会话（会话录像、字符命令等）等全方位审计，最大化保障企业运维安全。**说明**堡垒机默认仅提供180天日志存储服务，建议您将审计日志归档到SLS，进行进一步消费和更长周期的保存，比如接入到企业的SEIM系统进行统一的威胁检测和分析。详细操作，请参见[归档审计日志到日志服务](https://help.aliyun.com/zh/bh/bastionhost/user-guide/archive-audit-logs-in-log-service)。

详细方案，您可以参考《[多账号主机统一运维方案](https://help.aliyun.com/zh/well-architected/solution-28)》。

## 相关资源

### 相关实践

- [基于统一的IdP实现人员身份的统一认证](https://help.aliyun.com/zh/well-architected/sec01-bp05-unified-authentication-of-personnel-identity-based-on-unified-idp)

### 相关方案

- 《[多账号主机统一运维方案](https://help.aliyun.com/zh/well-architected/solution-28)》

### 相关文档

- [堡垒机多账号统一管理最佳实践](https://help.aliyun.com/zh/bh/bastionhost/use-cases/best-practices-for-unified-management-of-multiple-accounts-on-bastion-machines)

---

> 原页面：https://help.aliyun.com/zh/well-architected/use-bastion-machines-and-other-methods-for-workload-operation-and（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
