<!-- source: https://help.aliyun.com/zh/well-architected/workload-security-with-automation -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2925689 -->

# 使用自动化方式进行工作负载安全防护

在云原生环境中，工作负载（如容器、虚拟机、Serverless函数）的安全防护需从被动响应转向主动预防。通过自动化手段实现统一的基础镜像管理、漏洞修复、补丁更新、系统维护和配置审计等等，可显著降低人为操作风险、缩短安全响应时间，并满足合规性要求。

## 优先级

中

## 不推荐做法

- 手动管理基础镜像，不同团队使用不同版本的镜像，缺乏统一安全基线。
- 依赖人工扫描和修复，漏洞修复周期长，容易修复不彻底，导致横向渗透。
- 无自动化补丁策略，补丁更新依赖运维人员记忆或临时通知。
- 配置审计依赖人工检查，导致配置错误（如开放不必要的端口、弱密码）未及时发现出现安全风险。

## 实施指南

1. 统一管理基础镜像，自动化构建安全合规的基础镜像，并实现批量的分发和使用。在规模化部署的场景下，企业存在以下痛点：企业各业务在各自云账号下任意构建镜像，无法统一安全基线造成业务风险，并且多地域、多账号环境下镜像统一分发困难。阿里云建议企业使用黄金镜像（Golden Image）方案，在单独的共享账号内进行镜像构建，统一管控，限制应用账号能够使用的镜像 ID，避免应用账号使用不合规的镜像，同时基于资源共享和自动化能力，批量、快速将镜像分发给所有云账号，提升效率。详细方案，请参见《[多账号GoldenImage方案](https://help.aliyun.com/zh/well-architected/solution-40)》。
2. 使用[云安全中心](https://help.aliyun.com/zh/security-center/what-is-security-center)进行自动化的漏洞管理。通过配置自动[漏洞扫描](https://help.aliyun.com/zh/security-center/user-guide/scan-for-vulnerabilities)任务，自动化的识别和检测漏洞。使用云安全中心的[任务中心](https://help.aliyun.com/zh/security-center/use-the-playbook-feature)，制定漏洞修复计划任务，针对特定类型、等级、服务器群组进行自动化的漏洞修复。
3. 使用系统运维管理OOS的[补丁管理](https://help.aliyun.com/zh/oos/getting-started/patch-manager-overview)功能，针对系统补丁进行自动化运维，实现主机补丁集中扫描、监控和安装的运维需求。详细方案，请参见《[通过OOS实现主机操作系统补丁自动化运维](https://help.aliyun.com/zh/well-architected/solution-218)》。
4. 企业对于IT资产往往有一些合规要求，要求 ECS 主机实例保持一致的系统、软件配置基线，比如：主机内核参数、主机时区、软件版本等等。您可以使用[系统运维管理](https://help.aliyun.com/zh/oos/product-overview/introduction-to-oos)配合[ECS云助手](https://help.aliyun.com/zh/ecs/user-guide/overview-10)，实现云上主机系统与软件配置的自动化运维，满足主机系统与软件配置集中扫描、监控和修复的运维需求。详细方案，请参见《[通过OOS实现主机系统与软件配置自动化运维](https://help.aliyun.com/zh/well-architected/solution-221)》。
5. 使用[配置审计](https://help.aliyun.com/zh/document_detail/127388.html)，对云上资源进行自动化的配置扫描和修复，及时发现并修复资源配置错误，避免安全风险的发生。具体实践，请参见[持续对不合规资源进行修复](https://help.aliyun.com/zh/well-architected/ongoing-remediation-of-non-compliant-resources)。

## 相关资源

### 相关实践

- [进行集中化的漏洞管理](https://help.aliyun.com/zh/well-architected/centralized-vulnerability-management)
- [持续对不合规资源进行修复](https://help.aliyun.com/zh/well-architected/ongoing-remediation-of-non-compliant-resources)

### 相关方案

- 《[多账号GoldenImage方案](https://help.aliyun.com/zh/well-architected/solution-40)》
- 《[通过OOS实现主机操作系统补丁自动化运维](https://help.aliyun.com/zh/well-architected/solution-218)》
- 《[通过OOS实现主机系统与软件配置自动化运维](https://help.aliyun.com/zh/well-architected/solution-221)》

---

> 原页面：https://help.aliyun.com/zh/well-architected/workload-security-with-automation（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
