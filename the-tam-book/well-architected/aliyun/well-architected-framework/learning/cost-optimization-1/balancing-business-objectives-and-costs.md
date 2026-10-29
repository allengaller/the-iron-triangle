<!-- source: https://help.aliyun.com/zh/well-architected/balancing-business-objectives-and-costs -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2536202 -->

# 平衡业务目标与成本

企业需要选择合适的云产品及资源规格满足业务诉求，在应用负载的设计及资源选择过程中除了成本还应考虑稳定性、性能、安全合规、运营效率等方面的要求，在各项目标与成本之间进行权衡。

适合业务的应用负载设计并不意味着只追求低成本，首先需要全面了解各方面需求。单纯的低成本通常意味着在其它方面做出妥协，全面了解各方面需求后，按照业务特性对应用负载各方面要求进行权重排序，综合考虑后再做出选择。

## 成本与稳定性

如果业务对稳定性要求很高，设计出的应用负载也会带来较高的资源成本。例如对服务水平（Overall Service Level Agreement，SLA）、恢复时间（Recovery Time Objective，RTO）和恢复点（Recovery Point Objective，RPO）等指标要求严格，为了让业务应用高可用，应用服务需要更多的资源进行跨可用区或跨区域部署，跨区域进行数据复制也会增加成本。

企业可以根据业务重要性对应用负载进行分层，确定稳定性优先级，选择合适的稳定性方案。对于生产环境的在线应用通常建议选择同城双活、异地多活等高稳定性方案，重要数据选择同城冗余、跨地域备份等方式保障数据安全，测试环境可考虑降低稳定性要求以节约成本。

更多稳定性设计及注意事项参见[稳定性支柱](https://help.aliyun.com/zh/well-architected/overview-7)。

## 成本与性能

高性能要求的应用负载通常会花费更高的成本，企业需要根据业务特性对应用负载设定性能要求，选择适合的云产品、资源规格及计费方式等，在性能与成本之间进行权衡。关于成本优化与性能的一些建议如下：

- 在资源选型阶段进行性能测试，满足要求后再增加购买量。
- 引入弹性机制，关注应用负载、资源利用率、压力峰值时段等，动态调配资源供应，按需使用。
- 结合业务特性选择合适的计费方式，例如对公网带宽要求较高、流量峰值稳定的业务按带宽计费，可购买[共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/product-overview/what-is-internet-shared-bandwidth)。
- 可以根据业务场景选择使用[突发性能实例](https://help.aliyun.com/zh/ecs/user-guide/burst-performance-instance-overview)，用于应对突发性能需求并优化成本。

更多性能注意事项请参见[高效性能支柱](https://help.aliyun.com/zh/well-architected/overview-1)。

## 成本与安全合规

高安全性要求的应用负载通常会导致高成本，企业需要根据业务特性对应用负载设定安全性要求，不建议在应用负载的安全及合规上进行妥协。关于成本优化与安全合规的一些建议如下：

- 合规审计：使用[管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)、[配置审计](https://help.aliyun.com/zh/document_detail/127388.html)、[操作审计](https://help.aliyun.com/zh/actiontrail/product-overview/what-is-actiontrail)等产品便捷实现云上持续合规，产品自身目前可免费使用（以官网计费说明为准）。
- 网络安全：使用[云防火墙](https://help.aliyun.com/zh/cloud-firewall/cloudfirewall/product-overview/what-is-cloud-firewall)进行网络安全防护，支持多账号安全管控，无需在每个账号重复购买。
- 密钥安全：使用[密钥管理服务](https://help.aliyun.com/zh/kms/key-management-service/product-overview/what-is-key-management-service-1)进行密钥统一管理，支持多账号共享实例，无需在每个账号重复购买。

更多安全合规注意事项请参见[安全合规支柱](https://help.aliyun.com/zh/well-architected/overview-3)。

## 成本与卓越运营

构建可观测性系统、标准变更流程和自动化流程是卓越运营的重要组成部分，企业在建设初期通常会增加成本，但成本会随着时间推移逐渐降低；在云上做好成本管理也是提升企业运营效率的重要环节。关于成本优化与卓越运营的一些建议如下：

- 使用云原生的PaaS类监控产品，避免自己维护基础设施带来的维护成本及稳定性问题。
- 使用[Terraform](https://help.aliyun.com/zh/terraform/what-is-terraform)等基础设施自动化编排工具构建自动化流程，让基础设施代码化，降低开发和运维成本。

更多运营相关注意事项，请参见[卓越运营支柱](https://help.aliyun.com/zh/well-architected/overview)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/balancing-business-objectives-and-costs（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
