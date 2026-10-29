<!-- source: https://help.aliyun.com/zh/well-architected/infrastructure-security-implementation-best-practices -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2573784 -->

# 基础架构安全实施最佳实践

网络、账号和工作负载是企业客户在使用云时最先接触到的云资源，云提供了便利性的同时，企业仍要高度重视安全性，避免为了提供更便利的服务牺牲安全性。建议在业务上云初期，对网络规划、账号体系设计进行充分的考量和咨询，并进行有效的检测和评估。

阿里云提供了企业上云最佳实践咨询。对企业来说，将业务迁移到阿里云时，希望能够保障业务在云上安全合规，同时兼顾灵活的业务组织拓展。根据大量的客户实践总结发现，在上云前做好合理的规划可以避免对管理方式的反复重构，加速业务大规模上云。因此建议客户在上云之前先从顶层规划一个完善的企业上云框架，也称为 [Landing Zone](https://www.aliyun.com/solution/service/sllandingzone?spm=5176.21213303.1391245.1.6cd153c9aPQ9qH&scm=20140722.S_card@@%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88@@1730941.S_card0.ID_card@@%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88@@1730941-RL_landing%20zone-OR_ser-V_2-P0_0)。

## 网络架构设计最佳实践

阿里云基于大量的网络架构设计，结合不同行业业务特点和网络需求，提供网络架构设计的最佳实践。如企业级云上网络分区分域设计、云上同城/异地容灾网络设计、DMZ-VPC区域设计、VPC东西向流量隔离和管控设计、云上云下混合云组网设计等最佳实践方案。详细说明参考[网络安全保护](https://help.aliyun.com/zh/well-architected/network-security-protection)中相关内容。

## 账号体系设计最佳实践

阿里云基于Landing Zone体系，帮助企业设计资源管理及规划，账号设计和账号组织隔离方案。

### 资源规划

集团型企业对业务隔离的要求比较严格，不同业务必须按照安全要求或行业监管要求，部署在不同的云账号内，根据阿里云最佳实践，Landing Zone推荐企业使用多账号架构来管理云上资源。多账号架构帮助企业实现强隔离、降风险，应对企业多分公司关系，支持多种法律主体、多种结算模式共存，便于结构化管理，让企业的业务更便于拆分和融合。

![LZ.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4786435961/p722832.jpg)

### 账号设计

账号规划及职能说明如下：

- **企业管理账号**：用于多账号管理，在该账号中启用[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)并构建账号树，具备统一设置审计、管控策略等规则并下发到各成员账号等管理职能。该账号一般也作为财务主账号，与其它账号建立财务关联关系后对企业财务进行统一管理。
- **安全账号**：给企业的安全角色使用，用于配置相关安全产品，如Web应用防火墙（WAF）、云防火墙等。
- **日志账号**：聚合所有成员账号的日志，便于统一收集、统一管理。
- **运维账号**：部署运维相关工具，如堡垒机、统一监控平台、企业云管理平台CMP、云上资产管理平台CMDB等。
- **共享服务账号**：用于部署企业共享服务，如网络等。
- **业务账号**：业务功能账号，用于部署业务应用，如生产账号、开发测试账号。

### 账号组织结构及业务隔离

![(应用上云规划-应用上云实施-图5) 备份 4.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4786435961/p722833.jpg)

说明及建议：

- 在企业管理账号中使用[资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview)构建账号树，将其它账号作为**成员账号**纳入资源目录进行多账号统一管理。
- 基础管控类账号放置到Core资源夹下，业务账号放置到Applications资源夹下。
- 业务账号按业务组织单元进行划分，体现企业组织架构及管理方式，常见的组织单元划分如分公司、部门、产品等，可用于对不同业务单元进行隔离。
- 每个组织单元下可划分测试账号及生产账号，对生产环境及测试环境进行隔离。
- 账号下可使用不同资源组对应用资源进行隔离。
- 大数据业务集中放置到大数据账号，归属大数据资源夹。
- 外购资源夹用于放置供应商账号，根据实际情况选择是否需要，对供应商账号可以实施[管控策略](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/control-policy-overview)等基线进行操作限制。

### 工作负载架构设计最佳实践

工作负载的架构设计应从工作负载保护，工作负载网络设计、工作负载的访问控制三个层面设计。详细设计最佳实践可参考[工作负载安全保护](https://help.aliyun.com/zh/well-architected/workload-security)一节。

---

> 原页面：https://help.aliyun.com/zh/well-architected/infrastructure-security-implementation-best-practices（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
