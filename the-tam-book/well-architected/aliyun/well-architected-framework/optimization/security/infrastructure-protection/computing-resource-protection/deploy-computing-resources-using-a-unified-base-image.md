<!-- source: https://help.aliyun.com/zh/well-architected/deploy-computing-resources-using-a-unified-base-image -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2925690 -->

# 使用统一基础镜像部署计算资源

在云计算环境中，统一基础镜像是构建标准、安全和高效的工作负载的核心。尤其是在企业多个云账号规模化部署的场景下，管理并使用统一的基础镜像，可以帮助企业实现：

1. 安全性：集中安全扫描，强制使用合规镜像。
2. 一致性：全局统一基线，减少配置漂移。
3. 效率：自动化批量分发，快速覆盖。

## 优先级

高

## 不推荐做法

- 在企业多账号场景下，各个云账号独立构建镜像，导致版本混乱，安全基线不统一，存在安全隐患。
- 镜像构建完后，未经过安全扫描直接投入部署生产，导致镜像中包含一些已知漏洞被攻击者利用。
- 依赖人工复制镜像到其他企业云账号中，效率低且易出错。
- 未对镜像进行版本控制，导致回滚困难、版本冲突等一系列问题，影响业务稳定。

## 实施指南

无论对于ECS，还是容器化的部署方式，都需要关注镜像的安全，尤其是规模化的部署场景。规模化部署在企业内部海量成员账号的现实情况下存在以下痛点：企业各业务在各自成员账号下任意构建镜像，无法统一安全基线造成业务风险，并且多地域、多账号环境下镜像统一分发困难。

1. 对于ECS镜像，建议您使用黄金镜像（Golden Image）方案，在单独的共享账号内通过自动化流程进行镜像构建，在构建过程中，自动对镜像进行安全扫描和漏洞修复，保证镜像安全，同时进行统一管控，限制应用账号能够使用的镜像ID，避免应用账号使用不合规的镜像，同时基于资源共享和自动化能力，批量、快速将镜像分发给所有应用账号，提升效率。详细方案，请参见《[多账号GoldenImage方案](https://help.aliyun.com/zh/well-architected/solution-40)》。
2. 对于容器镜像，建议您使用[容器镜像服务ACR](https://help.aliyun.com/zh/acr/product-overview/what-is-container-registry)，集中管理和构建容器镜像。镜像构建：您可以[使用企业版实例构建镜像](https://help.aliyun.com/zh/acr/user-guide/build-images-on-container-registry-enterprise-edition-instances)，实现源代码到容器镜像的自动化持续集成流程。为保证镜像版本的一致性，建议您[开启镜像版本不可变](https://help.aliyun.com/zh/acr/user-guide/turn-on-immutable-image-version)，避免人为误操作引起的镜像版本覆盖问题。镜像扫描：使用[容器镜像安全扫描](https://help.aliyun.com/zh/acr/user-guide/scan-container-images)功能对镜像进行漏洞扫描和修复。镜像分发：通过容器镜像服务提供的镜像分发能力，跨地域、跨账号快速分发镜像。具体操作，请参见[同账号同步实例](https://help.aliyun.com/zh/acr/user-guide/replicate-images-between-instances-in-the-same-account)、[跨账号同步实例](https://help.aliyun.com/zh/acr/user-guide/synchronize-instances-across-accounts)。

## 相关资源

### 相关实践

- [进行集中化的漏洞管理](https://help.aliyun.com/zh/well-architected/centralized-vulnerability-management)

### 相关方案

- 《[多账号GoldenImage方案](https://help.aliyun.com/zh/well-architected/solution-40)》

---

> 原页面：https://help.aliyun.com/zh/well-architected/deploy-computing-resources-using-a-unified-base-image（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
