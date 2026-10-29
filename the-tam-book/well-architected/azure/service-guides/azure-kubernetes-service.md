<!-- source: https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-kubernetes-service -->
<!-- captured: 2026-10-25 -->
<!-- vendor: azure -->

# Architecture best practices for Azure Kubernetes Service (AKS)

Note




Azure Kubernetes Service (AKS) is a managed Kubernetes service that you can use to deploy and manage containerized applications. Like other managed services, AKS offloads much of the operational overhead to Azure while providing high availability, scalability, and portability features to the workload.

This article assumes that, as an architect, you reviewed the [compute decision tree](/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) and chose AKS as the compute for your workload. The guidance in this article provides architectural recommendations that are mapped to the principles of the [Azure Well-Architected Framework pillars](/en-us/azure/well-architected/pillars).

**Technology scope**

This review focuses on the interrelated decisions for the following Azure resources:

- AKS

When you discuss the Well-Architected Framework pillars' best practices for AKS, it's important to distinguish between:

- *Cluster* architecture, which is a shared responsibility between the platform team and Azure.
Azure operates the control plane and managed runtime components. Your platform team configures things such as node pools, scaling, and networking. The platform team also monitors the cluster infrastructure.
- *Workload* architecture, which is owned by application teams.
Workload teams own manifests, application identities, pod security, network policies, and are responsible for workload monitoring.

This article has considerations and recommendations for each of these roles.

Note

Use separate AKS clusters for unrelated workloads which provides the strongest isolation boundary. Co-locating workloads in a shared cluster can reduce operational overhead, but it requires additional controls, such as namespaces, dedicated node pools, and network policies, to maintain adequate isolation. Evaluate the workload isolation trade-offs before choosing a shared-cluster model.

## Choose AKS Automatic or AKS Standard

AKS offers two cluster modes: AKS Automatic and AKS Standard. AKS Automatic provides a production-ready baseline with preconfigured cluster operations, built-in safeguards, hardened default configurations, and managed scaling. Many of the recommendations described in the pillars below are implemented by default in AKS Automatic. If you use AKS Standard, you must implement these recommendations yourself. For most new production workloads, choose AKS Automatic unless your workload requires specialized platform customization or a level of control beyond AKS Automatic's capabilities. Make this decision early in the design process so that you can apply reliability, security, cost, and operations guidance consistently.

Choose AKS Automatic when your goals are:

- Faster path to production with a hardened default baseline.
- Reduced cluster administration overhead.
- Preconfigured scaling and node operations.
- Built-in operational safeguards and managed lifecycle behavior.
- Consistent production posture across teams.

Choose AKS Standard when you need to own and tune platform decisions, such as:

- Your workload requires Windows node pools.
- You wish to use the long-term support option.
- Specialized networking, such as bring-your-own CNI, and platform composition patterns.
- Explicit lifecycle and management control for cluster components.
- Workload or organizational constraints that require a fully custom AKS platform model.

If uncertain, start with AKS Automatic and validate requirements against known gaps before moving to AKS Standard.

Note

The following pillars include a **design checklist** and a **list of recommendations** that indicate whether each choice applies to *cluster* architecture, *workload* architecture, or both.

## Reliability

The purpose of the Reliability pillar is to provide continued functionality by **building enough resilience and the ability to recover fast from failures**.

[Reliability design principles](/en-us/azure/well-architected/reliability/principles) provide a high-level design strategy applied for individual components, system flows, and the system as a whole.

### Workload design checklist

Start your design strategy based on the [design review checklist for Reliability](../reliability/checklist). Determine its relevance to your business requirements while keeping in mind the features of AKS and its dependencies. Extend the strategy to include more approaches as needed.

- (Cluster) **Build redundancy to improve resiliency**. Use availability zones for your AKS clusters as part of your resiliency strategy to increase availability when you deploy to a single region. Many Azure regions provide availability zones. The zones are close enough to have low-latency connections among them, but far enough apart to reduce the likelihood that local outages will affect more than one zone.
For critical workloads, deploy multiple clusters across different Azure regions. By geographically distributing AKS clusters, you can achieve higher resiliency and minimize the effects of regional failures. A multiregion strategy helps maximize availability and provide business continuity.
Internet-facing workloads should use [Azure Front Door](/en-us/azure/frontdoor/front-door-overview) or [Azure Traffic Manager](/en-us/azure/aks/reliability-multi-region-deployment-models) to route traffic globally across AKS clusters. For more information, see [Multiregion strategy](/en-us/azure/aks/reliability-multi-region-deployment-models#multi-region-deployment-model-implementations).
Plan the IP address space to ensure that your cluster can reliably scale and handle failover traffic in multiple-cluster topologies.
- (Cluster and workload) **Monitor reliability and overall health indicators of the cluster and workloads**. Collect logs and metrics to monitor workload health, identify performance and reliability trends, and troubleshoot problems.
Review [Best practices for monitoring Kubernetes with Azure Monitor](/en-us/azure/azure-monitor/best-practices-containers) and the Well-Architected [Health modeling for workloads](/en-us/azure/well-architected/design-guides/health-modeling) guide for help designing the reliability and health monitoring solution for your AKS solution.
Ensure that workloads are built to support horizontal scaling and report application readiness and health.
- (Cluster and workload) **Host application pods in user node pools**. By isolating system pods from application workloads, you help ensure that AKS essential services aren't affected by the resource demands or potential problems caused by a workload that runs user node pools.
Ensure that your workload runs on user node pools and choose the right size SKU. At a minimum, include two nodes for user node pools and three nodes for the system node pool.
Review [Node auto provisioning](/en-us/azure/aks/node-auto-provisioning) guide for automatically provisioning and managing the optimal VM configuration for your workloads.
- (Cluster and workload) **Define pod disruption budgets (PDBs)**. Specify the minimum number of replicas that must stay available so voluntary disruptions can't take down too many pods at once. When AKS upgrades a cluster or node pool, it moves pods off the nodes being upgraded and honors your PDBs before and during the upgrade. This keeps workloads available during planned disruptions. For more information, see Pod Disruption Budgets in [Community links](#community-links).
- (Cluster and workload) **Factor the AKS uptime service-level agreement (SLA) into your availability and recovery targets**. To define the reliability and recovery targets for your cluster and workload, follow the guidance in [Recommendations for defining reliability targets](/en-us/azure/well-architected/reliability/metrics). Then formulate a design that meets those targets. Include AKS cluster availability and, where applicable, AKS Automatic pod readiness behavior in your reliability objectives.
- (Cluster and workload) **Protect the AKS cluster service by using Azure Backup** to store recovery points in a Backup vault and perform restore during certain types of disaster scenarios. To back up and restore the containerized applications and data running in AKS clusters, follow the guidance in the AKS backup overview for configuring protection.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| (Cluster and workload) Reserve node selectors and affinity for workloads that need specific node capabilities, such as GPU-enabled or high memory nodes. Avoid using node selectors for general workload isolation. Overusing them creates node dependencies that make scheduling brittle and reduce placement flexibility. | The scheduler can place general workloads on any suitable node, so your workloads stay resilient and operationally flexible. |
| (Cluster) Choose the appropriate network plugin based on network requirements and cluster sizing. Different network plugins provide varying levels of functionality. Azure Container Networking Interface (Azure CNI) is required for specific scenarios, such as Windows-based node pools, some networking requirements, and Kubernetes network policies. Use Azure CNI Overlay as the default networking model for AKS clusters. Overlay networking simplifies IP address management, reduces subnet sizing requirements, and scales efficiently without consuming VNet IP addresses for pods. For clusters that require very large numbers of pod IPs or high pod density, consider Azure CNI with Static Block Allocation. Avoid Kubenet for new deployments. | The right network plugin can help ensure better compatibility and performance. Static block allocation enables consistent IP ranges for better security policy configuration and capacity planning. |
| (Cluster and workload) Use the [AKS uptime SLA](/en-us/azure/aks/free-standard-pricing-tiers#uptime-sla-terms-and-conditions) for production-grade clusters. | The workload can support higher availability targets because of the higher availability guarantees of the Kubernetes API server endpoint for AKS clusters. |
| (Cluster) Use [availability zones](/en-us/azure/aks/reliability-availability-zones-configure) to maximize resilience within an Azure region by distributing AKS agent nodes across physically separate datacenters. If colocality requirements exist, use a regular virtual machine scale sets-based AKS deployment into a single zone or use [proximity placement groups](/en-us/azure/aks/reduce-latency-ppg) to minimize internode latency. | By spreading node pools across multiple zones, nodes in one node pool continue to run even if another zone goes down. |
| (Cluster and workload) Define pod [resource requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in application deployment manifests. Enforce those limits by using [built-in definitions](/en-us/azure/aks/policy-reference) for AKS in [Azure Policy](/en-us/azure/aks/use-azure-policy?pivots=azure-portal) | Container CPU and memory resource limits are necessary to prevent resource exhaustion in your Kubernetes cluster. |
| (Cluster and workload) Keep the system node pool isolated from application workloads. System node pools require a virtual machine (VM) SKU of at least 4 vCPUs and 4 GB of memory. We recommend that you use 4 vCPU or more. For more information, see [System and user node pools](/en-us/azure/aks/use-system-pools#system-and-user-node-pools). | The system node pool hosts critical system pods that are essential for the control plane of your cluster. By isolating these system pods from application workloads, you help ensure that the essential services are unaffected by the resource demands or potential problems caused by a workload. |
| (Cluster and workload) Keep the substrate for your applications as flexible and resilient as possible. Reserve dedicated node pools for cases that genuinely require them, such as a specific SKU type or security requirements (for example, landing FIPS-compliant workloads on FIPS-compliant nodes). Avoid large numbers of node pools to reduce management overhead. | A flexible substrate gives the scheduler more placement options, so your workloads stay resilient and you avoid brittle node dependencies. Reserving node pinning for real hardware or security needs helps ensure each application gets the resources it requires without overprovisioning or underutilizing resources. |
| (Cluster) Use a [NAT gateway](/en-us/azure/aks/nat-gateway) for clusters that run workloads that make many concurrent outbound connections. | Azure NAT Gateway supports reliable egress traffic at scale and helps you avoid reliability problems by applying Azure Load Balancer limitations to high concurrent outbound traffic. |
| (Cluster and workload) Use Azure Backup to [protect AKS cluster and restore](/en-us/azure/backup/azure-kubernetes-service-backup-overview) to alternate regions during disaster. Azure Backup supports the backup and restore operations of containerized applications and data running for both cluster state and application data. You can [use the backups in a regional disaster scenario and recover backups](/en-us/azure/backup/azure-kubernetes-service-cluster-restore). | Azure Backup with Azure Kubernetes Service (AKS) offers a managed, scalable, secure, and cost-effective solution. Your team configures the solution to selects backup scopes, retention, and test restores without needing to build the backup infrastructure. |
| (Cluster) Use [planned maintenance](/en-us/azure/aks/planned-maintenance) to schedule and control cluster and node image upgrades in Azure Kubernetes Service (AKS). | Planned maintenance helps ensure that upgrades are applied automatically in a controlled manner, minimizing downtime and disruption to your workloads. |

## Security

The Security pillar provides **confidentiality, integrity, and availability** guarantees to the workload.

The [Security design principles](/en-us/azure/well-architected/security/principles) provide a high-level design strategy for achieving those goals by applying approaches to the technical design of AKS.

### Workload design checklist

Start your design strategy based on the [design review checklist for Security](../security/checklist) and identify vulnerabilities and controls to improve the security posture. Familiarize yourself with [AKS security concepts](/en-us/azure/aks/concepts-security) and evaluate the security hardening recommendations based on the [CIS Kubernetes benchmark](/en-us/azure/aks/cis-kubernetes). Extend the strategy to include more approaches as needed.

- (Cluster) **Integrate with Microsoft Entra ID for identity and access management**. Centralize identity management for your cluster by using Microsoft Entra ID. Any change in user account or group status automatically updates access to the AKS cluster. [Establish identity as the primary security perimeter](/en-us/azure/well-architected/security/segmentation#establish-identity-as-the-primary-security-perimeter). The developers and application owners of your Kubernetes cluster need access to different resources.
Use Kubernetes role-based access control (RBAC) with Microsoft Entra ID for [least privilege access](/en-us/azure/aks/kubernetes-rbac-entra-id). Protect configuration and secrets by minimizing the allocation of administrator privileges.
- (Cluster) **Integrate with security monitoring and security information and event management tools**. Use Microsoft Defender for Containers with [Microsoft Sentinel](/en-us/azure/sentinel/overview) to detect and quickly respond to threats across your clusters and the workloads that run on them. Enable [AKS connector for Microsoft Sentinel](/en-us/azure/sentinel/data-connectors-reference#azure-kubernetes-service-aks) to stream your AKS diagnostics logs into Microsoft Sentinel.
- (Cluster and workload) **Implement segmentation and network controls**. To prevent data exfiltration, ensure that only authorized and safe traffic is allowed, and contain the blast radius of a security breach.
Consider using a private AKS cluster to help ensure that cluster-management traffic to your API server remains on your private network. Or use the API server allow list for public clusters.
- (Workload) **Use a web application firewall (WAF) to scan incoming traffic for potential attacks**. WAF can detect and mitigate threats in real time to help block malicious traffic before it reaches your applications. It provides robust protection against common web-based attacks, such as SQL injection, cross-site scripting, and other Open Web Application Security Project vulnerabilities. Some load balancers, such as [Azure Application Gateway](/en-us/azure/web-application-firewall/ag/ag-overview) or [Azure Front Door](/en-us/azure/web-application-firewall/afds/afds-overview) have an integrated WAF.
- (Workload) **Automate mTLS between ingress and mesh services**. If your workload uses a service mesh like Istio, use [Application Gateway for Containers with Istio integration](/en-us/azure/application-gateway/for-containers/service-mesh-integration) to automate mTLS connectivity, trust, and certificate rotation between the shared ingress layer and mesh-enabled services. This reduces repetitive mTLS configuration and extends encrypted traffic paths for container platforms. Like with any integration, make sure you test functionality before deployment.
- (Workload) **Maintain a hardened workload's software supply chain**. Ensure that your continuous integration and continuous delivery pipeline is hardened with container-aware scanning. Use a [DevSecOps on AKS](/en-us/azure/architecture/guide/devsecops/devsecops-on-aks) approach.
- (Cluster and workload) **Implement extra protection for specialized secure workloads**. If your cluster needs to run a sensitive workload, you might need to deploy a private cluster. Here are some examples:
Payment Card Industry Data Security Standard (PCI DSS): [AKS regulated cluster for PCI DSS 4.0.1](/en-us/azure/aks/pci-intro)
DoD Impact Level 5 (IL5) support and requirements with AKS: [Azure Government IL5 isolation requirements](/en-us/azure/azure-government/documentation-government-impact-level-5#azure-kubernetes-service).
- (Cluster) **Govern cluster extensions as part of the cluster security boundary**. Cluster extensions install and manage services on your AKS cluster. Before enabling an extension, evaluate its in-cluster components, managed identities, RBAC permissions, network access, and lifecycle requirements. Enable only extensions that the workload requires and keep them updated.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| (Cluster) Use [managed identities](/en-us/azure/aks/managed-identity-overview) on the cluster. | You can avoid the overhead associated with managing and rotating service principals. |
| (Workload) Use [Microsoft Entra Workload ID with AKS](/en-us/azure/aks/workload-identity-overview) to access Microsoft Entra protected resources, such as Azure Key Vault and Microsoft Graph, from your workload. | Use AKS Workload IDs to protect access to Azure resources by using Microsoft Entra ID RBAC without having to manage credentials directly in your code. |
| (Cluster) Use Microsoft Entra ID to [authenticate with Azure Container Registry from AKS](/en-us/azure/aks/cluster-container-registry-integration?tabs=azure-cli). | By using Microsoft Entra ID, AKS can authenticate with Container Registry without the use of `imagePullSecrets` secrets. |
| (Cluster) Secure network traffic to your API server by using [private AKS cluster](/en-us/azure/aks/private-clusters) if the workload requirements require higher levels of segmentation. | By default, network traffic between your node pools and the API server travels the Microsoft backbone network. By using a private cluster, you can help ensure that network traffic to your API server remains on the private network only. |
| (Cluster) For public AKS clusters, use API server-authorized IP address ranges. Include sources like the public IP addresses of your deployment build agents, operations management, and node pools' egress point, such as Azure Firewall. | When you use public clusters, you can significantly reduce the attack surface of your AKS cluster by limiting the traffic that can reach the API server of your clusters. |
| (Cluster) Protect the API server by using Microsoft Entra ID RBAC. [Disable local accounts](/en-us/azure/aks/local-accounts#disable-local-accounts) to enforce all cluster access by using Microsoft Entra ID-based identities. | Securing access to the Kubernetes API server is one of the most important things that you can do to secure your cluster. Integrate Kubernetes RBAC with Microsoft Entra ID to control access to the API server. |
| (Cluster and workload) Secure network traffic between pods in a cluster with [Azure CNI Powered by Cilium](/en-us/azure/aks/azure-cni-powered-by-cilium). It combines the control plane of Azure Container Networking Interface (CNI) with the data plane of Cilium to provide high-performance networking and security. [Advanced Container Networking Services](/en-us/azure/aks/advanced-container-networking-services-overview) adds many additional useful features on top of Cilium. | Azure CNI Powered by Cilium improves service routing, enables more efficient network policy enforcement, provides better observability of cluster traffic, and supports larger clusters. |
| (Cluster) Secure clusters and pods by using [Azure Policy](/en-us/azure/aks/use-azure-policy). Use [deployment safeguards](/en-us/azure/aks/deployment-safeguards) to enforce policy best practices. | Azure Policy can help apply at-scale enforcement and safeguards on your clusters in a centralized, consistent manner. It can also control what functions pods are granted and detect whether anything is running against company policy. |
| (Cluster) Secure container access to resources. Limit access to actions that containers can perform. Provide the least number of permissions, and avoid the use of root or privileged escalation. For Linux based containers, see [Security container access to resources using built-in Linux security features](/en-us/azure/aks/secure-container-access). | By restricting permissions and avoiding the use of root or privileged escalation, you help reduce the risk of security breaches. You can help ensure that, even if a container is compromised, the potential damage is minimized. |
| (Cluster) Control cluster egress traffic by ensuring that your cluster's outbound traffic passes through a network security point such as [Azure Firewall](/en-us/azure/aks/limit-egress-traffic) or an [HTTP proxy](/en-us/azure/aks/http-proxy). | By routing outbound traffic through Azure Firewall or an HTTP proxy, you can help enforce security policies that prevent unauthorized access and data exfiltration. This approach also simplifies the administration of security policies and makes it easier to enforce consistent rules across your entire AKS cluster. |
| (Cluster) Configure [HTTP proxy support](/en-us/azure/aks/http-proxy) for existing AKS clusters in proxy-dependent environments. Enable HTTP proxy configuration for both AKS nodes and pods to integrate with existing enterprise network security architectures and compliance requirements. | Critical for financial services and other regulated industries requiring all internet traffic to flow through corporate HTTP proxies for security scanning and compliance monitoring. Enables seamless integration with existing enterprise network security infrastructure. |
| (Cluster) Implement [custom certificate authority support](/en-us/azure/aks/custom-certificate-authority) only if your workload has specific internal requirements to establish trust relationships between AKS clusters and enterprise PKI infrastructure. Configure custom CA to enable trust for private registries, proxies, and firewalls within existing organizational certificate management frameworks. | Essential for enterprises with internal certificate authority infrastructure. Enables AKS clusters to trust organizational private registries and internal services while maintaining corporate security policies and compliance requirements. |
| (Cluster) Use the open-source [Microsoft Entra Workload ID](https://github.com/Azure/azure-workload-identity) and [Secrets Store CSI Driver](/en-us/azure/aks/csi-secrets-store-driver?pivots=azure-cli-create) with Key Vault. | These features help you protect and rotate secrets, certificates, and connection strings in Key Vault by using strong encryption. They provide an access audit log and keep core secrets out of the deployment pipeline. |
| (Cluster) Use [Microsoft Defender for Containers](/en-us/azure/defender-for-cloud/defender-for-containers-introduction). | Microsoft Defender for Containers helps you monitor and maintain the security of your clusters, containers, and their applications. |

## Cost Optimization

Cost Optimization focuses on **detecting spend patterns, prioritizing investments in critical areas, and optimizing in others** to meet the organization's budget while meeting business requirements.

The [Cost Optimization design principles](/en-us/azure/well-architected/cost-optimization/principles) provide a high-level design strategy for achieving those goals and making tradeoffs as necessary in the technical design related to AKS and its environment.

### Workload design checklist

Start your design strategy based on the [design review checklist for Cost Optimization](../cost-optimization/checklist) for investments. Fine-tune the design so that the workload is aligned with the budget that's allocated for the workload. Your design should use the right Azure capabilities, monitor investments, and find opportunities to optimize over time.

- (Cluster) **Include the pricing tiers for AKS in your cost model**. To estimate costs, use the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) and test different configuration and payment plans in the calculator.
- (Cluster) **Get the best rates for your workload**. Use the appropriate VM SKU for each node pool because it directly affects the cost to run your workloads. Choosing a high-performance VM without proper utilization can lead to wasteful spending. Selecting a less powerful VM can cause performance problems and increased downtime.
If you properly plan for capacity and your workload is predictable and will exist for an extended period of time, sign up for [Azure Reservations](/en-us/azure/aks/faq#can-i-apply-azure-reservation-discounts-to-my-aks-agent-nodes-) or a [savings plan](/en-us/azure/cost-management-billing/savings-plan/savings-plan-overview#determine-your-savings-plan-commitment) to reduce your resource costs.
Choose [Azure Spot Virtual Machines](/en-us/azure/virtual-machines/spot-vms) to use unutilized Azure capacity with significant discounts. These discounts can reach up to 90% of pay-as-you-go prices. If Azure needs capacity back, the Azure infrastructure evicts the Spot nodes.
If you run AKS on-premises or at the edge, you can also use [Azure Hybrid Benefit](/en-us/windows-server/get-started/azure-hybrid-benefit) to reduce costs when you run containerized applications in those scenarios.
- (Cluster and workload) **Optimize workload components costs**. Choose the most cost-effective region for your workload. Evaluate the cost, latency, and compliance requirements to ensure that you run your workload cost-effectively and that it doesn't affect your customers or create extra networking charges. The region where you deploy your workload in Azure can significantly affect the cost. Because of many factors, the cost of resources varies for each region in Azure.
Maintain small and optimized images to help reduce costs because new nodes need to download those images. User request failures or timeouts when the application is starting up can lead to overprovisioning. Build images in a way that allows the container to start as soon as possible to help avoid failures and timeouts.
Review the Cost Optimization recommendations in [Best practices for monitoring Kubernetes with Azure Monitor](/en-us/azure/azure-monitor/containers/best-practices-containers#cost-optimization-for-kubernetes-monitoring) to determine the best monitoring strategy for your workloads. Analyze performance metrics, starting with CPU, memory, storage, and network, to identify cost optimization opportunities by cluster, nodes, and namespace.
- (Cluster and workload) **Optimize workload scaling costs**. Consider alternative vertical and horizontal scaling configurations to reduce scaling costs while still meeting all workload requirements. Use autoscalers to scale in when workloads are less active.
- (Cluster and workload) **Collect and analyze cost data**. The foundation of enabling cost optimization is the spread of a cost-saving cluster. Develop a cost-efficiency mindset that includes collaboration between finance, operations, and engineering teams to drive alignment on cost-saving goals and bring transparency to cloud costs.
- (Cluster and workload) **Make workloads more sustainable**. Making workloads more [sustainable and cloud efficient](../sustainability/overview) requires combining efforts around *cost optimization*, *reducing carbon emissions*, and *optimizing energy consumption*. Optimizing the application's cost is the initial step in making workloads more sustainable.
See [Sustainable software engineering principles in AKS](/en-us/azure/aks/concepts-sustainable-software-engineering) to learn how to build sustainable and efficient AKS workloads.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| (Cluster and workload) Align [AKS SKU selection](/en-us/azure/aks/free-standard-pricing-tiers) and managed disk size with workload requirements. | Matching your selection to your workload demands helps ensure that you don't pay for unneeded resources. |
| (Cluster) Enable [node auto-provisioning (NAP)](/en-us/azure/aks/node-auto-provisioning) to automatically select and scale the right VM instances for your [AKS node pools](/en-us/azure/aks/create-node-pools). | VM instance type directly affects the cost to run applications on AKS, so an oversized SKU leads to wasteful spending and an undersized one leads to performance problem. NAP selects the optimal VM configuration based on pending pod resource requirements, so workloads run in the most efficient and cost-effective way. |
| (Cluster) Choose VMs based on the more power efficient ARM architecture. AKS supports [creating Arm64 node pools](/en-us/azure/aks/use-arm64-vms) and a mix of Intel and Arm64 architecture nodes within a cluster. | The Arm64 architecture provides a better price-to-performance ratio because of its lower power utilization and efficient compute performance. These capabilities can bring better performance at a lower cost. |
| (Cluster) Enable the [cluster autoscaler](/en-us/azure/aks/cluster-autoscaler) to automatically reduce the number of agent nodes in response to excess resource capacity. Node auto-provisioning (NAP) can also help with scaling and manages VMs (nodes) in a cluster in response to pending pod pressure. | Automatically scaling down the number of nodes in your AKS cluster lets you run an efficient cluster when demand is low and scale up when demand increases. |
| (Workload) Use [HorizontalPodAutoscaler](/en-us/azure/aks/concepts-scale#horizontal-pod-autoscaler) to adjust the number of pods in a deployment depending on CPU utilization or other metrics. | Automatically scaling down the number of pods when demand is low and scaling out when demand increases results in a more cost-effective operation of your workload. |
| (Workload) Use [VerticalPodAutoscaler](/en-us/azure/aks/vertical-pod-autoscaler) to rightsize your pods and dynamically [set requests and limits](/en-us/azure/aks/developer-best-practices-resource-management#define-pod-resource-requests-and-limits) based on historic usage. | By setting resource requests and limits on containers for each workload, VerticalPodAutoscaler frees up CPU and memory for other pods and helps ensure effective utilization of your AKS clusters. |
| (Cluster) Configure the [AKS cost analysis add-on](/en-us/azure/aks/cost-analysis). | The cost analysis cluster extension enables you to obtain granular insight into costs that are associated with various Kubernetes resources in your clusters or namespaces. |

## Operational Excellence

Operational Excellence primarily focuses on procedures for **development practices, observability, and release management**.

The [Operational Excellence design principles](/en-us/azure/well-architected/operational-excellence/principles) provide a high-level design strategy for achieving those goals for the operational requirements of the workload.

### Workload design checklist

Start your design strategy based on the [design review checklist for Operational Excellence](../operational-excellence/checklist) for defining processes for observability, testing, and deployment. See [AKS best practices](/en-us/azure/aks/best-practices) and [Day-2 operations guide](/en-us/azure/architecture/operator-guides/aks/day-2-operations-guide) to learn about key considerations to understand and implement.

- (Cluster) **Implement an infrastructure as code (IaC) deployment approach**. Use a declarative, template-based deployment approach by using Bicep, Terraform, or similar tools. Make sure that all deployments are repeatable, traceable, and stored in a source code repo. For more information, see the [quickstarts](/en-us/azure/aks/learn/quick-kubernetes-automatic-deploy) in the AKS product documentation.
- (Cluster and workload) **Automate infrastructure and workload deployments**. Use standard software solutions to manage, integrate, and automate the deployment of your cluster and workloads. Integrate deployment pipelines with your source control system and incorporate automated tests.
Build an automated process to help ensure that your clusters are bootstrapped with the necessary cluster-wide configurations and deployments. This process is typically performed by using GitOps.
Use a repeatable and automated deployment processes for your workload within your software development lifecycle.
- (Cluster and workload) **For multi-cluster environments, use Azure Kubernetes Fleet Manager .** Fleet Manager can orchestrate cluster management operations. It can also provide resource placement across clusters when you deploy a dedicated hub cluster.
- (Cluster and workload) **Implement a monitoring strategy**. Collect logs and metrics to monitor the health of the workload, identify trends in performance and reliability, and troubleshoot problems. Review the [Best practices for monitoring Kubernetes with Azure Monitor](/en-us/azure/azure-monitor/best-practices-containers) and the Well-Architected [Recommendations for designing and creating a monitoring system](/en-us/azure/well-architected/operational-excellence/observability) to determine the best monitoring strategy for your workloads.
Enable diagnostics settings to ensure that control plane or core API server interactions are logged. Collect [AKS control plane metrics with Azure Monitor managed service for Prometheus](https://aka.ms/aks/ccp-metrics), and define alerts for signals that indicate API server, scheduler, or controller degradation. Metrics provide trend and threshold data, but retain control plane logs for event-level investigations.
The workload should be designed to emit telemetry that can be collected, which should also include liveness and readiness statuses.
Consider AI-assisted network diagnostic agents like the Container Network Insights Agent as a read-only complement to your AKS monitoring strategy when operators need to investigate intermittent pod-to-service, DNS, or packet-loss failures. These agents can use natural-language problem descriptions to correlate live cluster, flow, and host-network telemetry in a single investigation path, which reduces manual log and metric correlation during incidents. The tradeoff is added operational complexity, so use them to augment established runbooks, queries, and alerts rather than replace foundational observability practices.
- (Cluster and workload) **Implement testing in production strategies**. Testing in production uses real deployments to validate and measure an application's behavior and performance in the production environment. Use chaos engineering practices that target Kubernetes to identify application or platform reliability issues.
[Azure Chaos Studio](/en-us/azure/chaos-studio/chaos-studio-aks-guidance) can help simulate faults, such as zone failures of node pools, and trigger disaster recovery situations.
- (Cluster and workload) **Enforce workload governance**. Azure Policy helps ensure consistent compliance with organizational standards, automates policy enforcement, and provides centralized visibility and control over your cluster resources.
Review the [Azure Policy](#azure-policy) section to learn more about the available built-in policies for AKS.
- (Cluster and workload) **Use stamp-level, blue-green deployments for mission-critical workloads**. A stamp-level, blue-green deployment approach can increase confidence in releasing changes and enables zero-downtime upgrades because compatibilities with downstream dependencies like the Azure platform, resource providers, and IaC modules can be validated.
Kubernetes and ingress controllers support many advanced deployment patterns for inclusion in your release engineering process. Consider patterns like blue-green deployments or canary releases.

AKS also has [blue-green node pool upgrades(preview)](/en-us/azure/aks/blue-green-node-pool-upgrade) that enables you to upgrade your AKS node pools by adding new green nodes with the updated configuration to the existing node pool, while the original blue nodes continue running.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| (Cluster) Operationalize cluster and pod configuration standards by using [Azure policies for AKS](/en-us/azure/aks/use-azure-policy). Use [deployment safeguards](/en-us/azure/aks/deployment-safeguards) to enforce policy best practices. | Azure policies for AKS can help you apply at-scale enforcement and safeguards on your clusters in a centralized, consistent manner. Use policies to define the permissions granted to pods and ensure compliance with company policies. |
| (Cluster) Configure [Azure CNI static block allocation](/en-us/azure/aks/configure-azure-cni) for predictable pod subnet allocation and improved IP address management in AKS clusters. Implement static block allocation to provide predictable IP address assignment for Kubernetes pods within defined subnet ranges, enabling integration with existing network security policies. | Essential for development teams running multiple AKS clusters needing predictable IP address allocation to integrate with existing network security policies and firewall rules. Enhances operational excellence through predictable network addressing and simplified IP management. |
| (Cluster) Use Node Auto-Provisioning (NAP) for node scaling. Use cluster autoscaler when your workload has fixed, explicitly managed node pools. | NAP help ensure that your AKS cluster can automatically adjust the number of nodes based on resource demands, improving resource utilization and operational efficiency. |
| (Cluster) Use the [KAITO AI Toolchain Operator](/en-us/azure/aks/ai-toolchain-operator) for efficient deployment and management of AI model serving workloads. | KAITO simplifies AI model deployment and scaling on Kubernetes while providing optimized infrastructure for machine learning inference workloads. Data science teams can deploy and scale large language models or other AI models on AKS using KAITO, which automatically handles GPU resources, model serving infrastructure, and scaling policies without manual Kubernetes configuration, reducing operational complexity. |
| (Cluster) Enable [AKS Automatic](/en-us/azure/aks/intro-aks-automatic) for managed Kubernetes experience with automated cluster management. | AKS Automatic reduces operational overhead for Kubernetes cluster management by automating routine tasks while ensuring optimal configuration and security posture. Development teams can deploy applications to AKS without managing cluster configuration, updates, or optimization, allowing them to focus on application development while ensuring their Kubernetes infrastructure follows best practices automatically. |
| (Cluster) For private AKS clusters, use an [Azure Bastion tunnel to connect to the private API server](/en-us/azure/bastion/bastion-connect-to-aks-private-cluster) for management tasks. | Bastion avoids exposing the cluster endpoint to the public internet, or maintaining a jump-box VM. However, it adds service cost and becomes a dependency for operator access. |
| (Cluster) Enable [automatic upgrades](/en-us/azure/aks/auto-upgrade-cluster?tabs=azure-cli) to ensure your clusters are up to date. | Cluster autoupgrade provides a set-once-and-forget mechanism that yields tangible time and operational cost benefits. |
| (Cluster) Manage updates for multiple clusters with Azure Kubernetes Fleet Manager. Fleet Manager update run can [automate approval gates with Event Grid](/en-us/azure/kubernetes-fleet/howto-configure-events-for-gates) to provide more control over when update groups or stages are processed. | Automating update gates helps ensure consistent and controlled updates across multiple clusters, reducing the risk of downtime and configuration drift. |
| (Cluster and workload) For multi-cluster environments, use [Azure Kubernetes Fleet Manager resource placement](/en-us/azure/kubernetes-fleet/concepts-resource-placement) to distribute workloads across member clusters through policy-driven placement decisions. | Reduces manual coordination when you operate multiple AKS clusters across regions or environments and need consistent deployment governance. |
| (Cluster and workload) Use the Kubernetes Gateway API for [ingress and layer 7 traffic management](/en-us/azure/aks/concepts-network-ingress). For example, consider using the [AKS Application Routing add-on](/en-us/azure/aks/app-routing-gateway-api), which builds on the Gateway API. | The Gateway API provides a standards-based model for advanced ingress and traffic routing, without using vendor-specific configuration. The Application Routing add-on can improve traffic distribution for workloads that need traffic splitting, header-based routing, or more expressive rules without running a custom ingress controller. |

## Performance Efficiency

Performance Efficiency is about **maintaining user experience even when there's an increase in load** by managing capacity. The strategy includes scaling resources, identifying and optimizing potential bottlenecks, and optimizing for peak performance.

The [Performance Efficiency design principles](/en-us/azure/well-architected/performance-efficiency/principles) provide a high-level design strategy for achieving those capacity goals against the expected usage.

### Workload design checklist

Start your design strategy based on the [design review checklist for Performance Efficiency](../performance-efficiency/checklist) for defining a baseline based on key performance indicators for AKS.

- (Cluster and workload) **Conduct capacity planning**. Perform and iterate on a detailed capacity plan exercise that includes SKU, autoscale settings, IP addressing, and failover considerations.
After you formalize your capacity plan, frequently update the plan by continuously observing the resource utilization of the cluster.
- (Cluster) **Define a scaling strategy**. Configure scaling to ensure that resources are adjusted efficiently to meet workload demands without overuse or waste. Use AKS features like cluster autoscaling and HorizontalPodAutoscaler to dynamically meet your workload needs with less strain on operations. Optimize your workload to operate and deploy efficiently in a container.
Review the [Scaling and partitioning](/en-us/azure/well-architected/performance-efficiency/scale-partition) guide to understand the various aspects of scaling configuration.
- (Cluster and workload) **Conduct performance testing**. Perform ongoing load testing activities that exercise both the pod and cluster autoscaler. Compare results against the performance targets and the established baselines.
- (Cluster and workload) **Scale workloads and flows independently**. Separate workloads and flows into different node pools to allow independent scaling. Follow the guidance in [Optimize workload design using flows](/en-us/azure/well-architected/design-guides/optimize-workload-using-flows) to identify and prioritize your flows.
- (Cluster) **Optimize DNS resolution**. Take advantage of LocalDNS using [node auto-provisioning](/en-us/azure/aks/node-auto-provisioning-aksnodeclass#localdns-configuration). LocalDNS deploys a node level DNS proxy that resolves DNS queries, reducing query latency and provides continued name resolution even when upstream DNS services experience outages. Node auto-provisioning integration maintains optimal network performance without sacrificing operational automation capabilities.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| (Cluster) Enable [cluster autoscaler](/en-us/azure/aks/cluster-autoscaler) to automatically adjust the number of agent nodes in response to workload demands. Use the [HorizontalPodAutoscaler](/en-us/azure/aks/concepts-scale#horizontal-pod-autoscaler) to adjust the number of pods in a deployment depending on CPU utilization or other metrics. Use the [VerticalPodAutoscaler (VPA)](/en-us/azure/aks/vertical-pod-autoscaler) for pod resource optimization to match the usage pattern of your workload. | The ability to automatically scale up or scale down the number of nodes and the number of pods in your AKS cluster lets you run an efficient, cost-effective cluster. |
| (Cluster) For supported clusters with latency-sensitive or high-throughput pod traffic, evaluate [eBPF host routing](/en-us/azure/aks/container-network-performance-ebpf-host-routing) in Advanced Container Networking Services. Test network policies, node images, and host-level networking dependencies before enabling it. | eBPF host routing bypasses iptables-based host routing to reduce latency, network hops, and CPU use. Enabling it rotates nodes, applies cluster-wide, and prevents host-network iptables rules, so validate compatibility and account for the added service cost. |
| (Cluster and workload) Separate workloads into different node pools and consider [scaling user node pool](/en-us/azure/aks/scale-cluster)s. | Unlike system node pools that always require running nodes, user node pools allow you to scale up or scale down. |
| (Workload) Use AKS [advanced scheduler features](/en-us/azure/aks/operator-best-practices-advanced-scheduler) to implement advanced balancing of resources for workloads that require them. | As you manage AKS clusters, you often need to isolate teams and workloads. Advanced features that the Kubernetes scheduler provides let you control which pods can be scheduled on certain nodes. They also let you control how multipod applications can be appropriately distributed across the cluster. |
| (Workload) Use [Kubernetes Event Driven Autoscaler KEDA](/en-us/training/modules/configure-scaling-azure-kubernetes-service/) to build a meaningful autoscale ruleset based on signals that are specific to your workload. | Not all scale decisions can be derived from CPU or memory metrics. Scale considerations often come from more complex or even external data points. KEDA allows your applications to scale based on events, such as the number of messages in a queue or the length of a topic lag. |
| (Cluster) Enable [Azure Monitor High Scale mode for Container Insights](/en-us/azure/azure-monitor/containers/container-insights-high-scale#enable-high-scale-mode-for-monitoring-add-on) for large-scale Kubernetes deployments with hundreds of nodes. It reduces resource consumption while maintaining observability. | Enables monitoring and reduces agent resource overhead and improves data collection performance. This optimization is beneficial for enterprise environments running hundreds of nodes where standard monitoring approaches can impact cluster performance and increase costs. |

## Azure policy

Azure provides an extensive set of built-in policies related to AKS that apply to the Azure resource, like typical Azure policies and the Azure Policy add-on for Kubernetes, and within the cluster. Many of the Azure resource policies come in both *Audit/Deny* and *Deploy If Not Exists* variants. In addition to the built-in Azure Policy definitions, you can create custom policies for both the AKS resource and for the Azure Policy add-on for Kubernetes.

You can audit some of the recommendations in this article through Azure Policy. For example, you can check the following cluster policies:

- Clusters have readiness or liveness health probes configured for your pod spec.
- Microsoft Defender for Cloud policies.
- Authentication mode and configuration policies, like Microsoft Entra ID, RBAC, and disable local authentication.
- API server network access policies, including private cluster.
- GitOps configuration policies.
- Diagnostics settings policies.
- AKS version restrictions.
- Prevent command invoke.

You can also check the following cluster and workload policies:

- Kubernetes cluster pod security initiatives for Linux-based workloads.
- Include pod and container capability policies, such as AppArmor, sysctl, security caps, SELinux, seccomp, privileged containers, and automount cluster API credentials.
- Mount, volume drivers, and filesystem policies.
- Pod and container networking policies, such as host network, port, allowed external IPs, HTTPs, and internal load balancers.
- Namespace deployment restrictions.
- CPU and memory resource limits.

For governance, review the [Azure Policy built-in definitions for Kubernetes](/en-us/azure/governance/policy/samples/built-in-policies#kubernetes) and other policies that might affect the security of the compute layer.

## Azure Advisor recommendations

Use [Azure Advisor](/en-us/azure/advisor/advisor-overview) to review personalized recommendations for your AKS resources. Advisor analyzes resource configuration and usage telemetry and organizes applicable recommendations. Evaluate each recommendation against your workload requirements and architectural tradeoffs before implementation.

For AKS-specific cost guidance, review [AKS cost recommendations in Azure Advisor](/en-us/azure/aks/cost-advisors). Depending on the cluster configuration and historical usage, Advisor can recommend adjustments to your cluster to save you money.

## Example architecture

Foundational architecture that demonstrates the key recommendations: [AKS baseline architecture](/en-us/azure/architecture/reference-architectures/containers/aks/baseline-aks).

## Related content

Consider the following articles as resources that demonstrate the recommendations highlighted in this article.

- [Introduction to AKS Automatic](/en-us/azure/aks/intro-aks-automatic)
- [AKS baseline architecture](/en-us/azure/architecture/reference-architectures/containers/aks/baseline-aks)
- [Advanced AKS microservices architecture](/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices-advanced)
- [Introduction to AKS regulated cluster for PCI DSS 4.0.1](/en-us/azure/aks/pci-intro)
- [AKS baseline for multiregion clusters](/en-us/azure/architecture/reference-architectures/containers/aks-multi-region/aks-multi-cluster)

Build implementation expertise by using the following product documentation:

- [AKS product documentation](/en-us/azure/aks)

## Community links

- [Pod Disruption Budgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb)

## Feedback

Was this page helpful?

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

## Additional resources

- Last updated on 2026-09-14

---

> 原页面：https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-kubernetes-service（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
