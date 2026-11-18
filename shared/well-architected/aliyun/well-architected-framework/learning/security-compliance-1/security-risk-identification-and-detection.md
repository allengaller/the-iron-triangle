<!-- source: https://help.aliyun.com/zh/well-architected/security-risk-identification-and-detection/ -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2573781 -->

# 安全风险识别和检测

安全风险识别和检测包含以下4个维度，通过梳理企业客户上云面临的整体风险，才能有针对性的对安全架构进行建议、检测和建设。

- 基础架构的风险识别和检测：云上基础架构包含了网络架构和身份体系，要评估和识别当前网络的架构设计方法，是否符合安全最小化原则和纵深防御原则；
- 云平台配置风险识别和检测：企业使用云产品创建的配置文件是否符合安全原则，需要进行识别和自动化检测，可基于云安全最佳实践和行业合规要求建立符合企业自身的“云安全基线”也被称之为“baseline”，通过标准识别和检测上云风险；
- 资产脆弱性的风险识别和检测：云上的资产可分为工作负载（ECS、Kubernetes、容器、Serverless）、基础网元（EIP、NAT、SLB等）、应用（PaaS服务、域名、镜像等），面对资产的脆弱性（包含资产基线和资产漏洞）应该进行事前的风险识别和检测，并进行维护；
- 合规风险的识别：合规包含了外部合规和内部合规。外部合规指的是面向监管的合规，内部合规指的是面向内部审计、管理的合规。

![(应用上云规划-应用上云实施-图5) 备份 10.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3266435961/p722831.jpg)

---

> 原页面：https://help.aliyun.com/zh/well-architected/security-risk-identification-and-detection/（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
