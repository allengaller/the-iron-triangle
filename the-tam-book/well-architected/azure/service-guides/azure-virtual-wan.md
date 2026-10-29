<!-- source: https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-virtual-wan -->
<!-- captured: 2026-10-25 -->
<!-- vendor: azure -->

# Architecture best practices for Azure Virtual WAN

Note




Azure Virtual WAN is a networking service that provides unified connectivity, security, and routing. It connects branches and users globally through virtual private network (VPN) connections and Azure ExpressRoute connections, supports encrypted private links, and integrates with Azure Firewall for centralized protection. Virtual WAN uses a hub-and-spoke architecture built for scale and performance in global transit networks.

The guidance in this article provides architectural recommendations that are mapped to the principles of the [Well-Architected Framework pillars](/en-us/azure/well-architected/pillars).

**Technology scope**

This review focuses on the interrelated decisions for the following Azure resources:

- Azure Virtual WAN
- Azure VPN Gateway

## Reliability

The purpose of the Reliability pillar is to provide continued functionality by **building enough resilience and the ability to recover fast from failures**.

The [Reliability design principles](/en-us/azure/well-architected/resiliency/principles) provide a high-level design strategy applied for individual components, system flows, and the system as a whole.

### Workload design checklist

Start your design strategy based on the [design review checklist for Reliability](../reliability/checklist). Determine its relevance to your business requirements while keeping in mind the nature of your application and the criticality of its components. Extend the strategy to include more approaches as needed.

- **Review service limits and known problems:** Review [Virtual WAN limits](/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-virtual-wan-limits) and [known problems](/en-us/azure/virtual-wan/whats-new#knownissues) before you plan your architecture. Virtual WAN enforces limits on connected resources per hub and per subscription. Known problems include available workarounds.
Choose the Virtual WAN [Standard SKU](/en-us/azure/virtual-wan/virtual-wan-about#basicstandard) for production deployments to get zone redundancy and advanced routing capabilities.
- **Anticipate potential failures through failure mode analysis (FMA):** FMA helps you anticipate failure scenarios and develop mitigation strategies.
Failure
Mitigation
Regional outage that affects a single-region Virtual WAN hub
Deploy multiple hubs across regions to maintain connectivity when one region becomes unavailable.
ExpressRoute connection failure
Deploy redundant circuits or backup VPN connections to maintain hybrid connectivity during outages.
Branch site VPN connection failure
Provision site-to-site VPN with redundant internet service provider (ISP) links to protect against provider-level connectivity problems.
- **Understand service-level agreement (SLA) and composite reliability targets:** Virtual WAN hub routing infrastructure has a 99.95% SLA. During downtime, you can't establish or maintain connections. See SLA terms for service credits.
End-to-end connectivity requires a composite SLA calculation. Hubs, gateways, and firewalls each have independent SLAs. Calculate the combined SLA for critical connectivity paths.
The SLA excludes customer responsibilities, like on-premises equipment failures, internet connectivity problems outside Azure control, and configuration errors.
- **Plan multiregion redundancy for hub deployment:** Distribute virtual hubs across multiple Azure regions to achieve region-level redundancy.
When you select regions, prioritize the following factors:
Proximity to users and workloads
Paired regions for disaster recovery
Cross-region connectivity requirements
Regulatory and data residency constraints
Establish routing to support automatic or manual region failover. Plan for asymmetric routing patterns during failures and document expected outage behavior. Regulatory and data residency requirements might constrain multiregion deployment strategies.
- **Plan for layered redundancy:** Virtual WAN supports three redundancy layers. Each layer addresses distinct failure scenarios.
Layer
Protects against
Zone-level
Datacenter failures within a region
Connection-level
Single-path failures
Route-level
Preferred path failures through traffic engineering and failover control
Balance redundancy decisions against availability needs, implementation complexity, and cost. Evaluate each failure domain's effect on workload operations. Choose symmetric or asymmetric routing patterns that match operational capabilities.
- **Plan for reliable hub and gateway scaling:** Size infrastructure for expected growth rather than current traffic. Hub routers automatically scale but require up to 25 minutes. Gateways require manual sizing and scheduled maintenance for changes. Overprovision capacity to maintain reliability during demand spikes.
- **Design resilience for point-to-site VPN:** Use the global VPN profile for automatic hub selection and failover. Size point-to-site address pools to handle at least double the expected concurrent users to prevent exhaustion during gateway redistribution.
- **Set up VPN backup for failover:** Deploy a VPN gateway alongside an ExpressRoute gateway. Set the Border Gateway Protocol (BGP) preference to favor ExpressRoute over VPN for automatic failover.
- **Validate failover behavior:** Test routing and network virtual appliance (NVA) behavior during failover scenarios. Document expected traffic flows and client impact for each failover pattern.
- **Incorporate business continuity testing:** Test your failover configuration to avoid surprises during actual outages.
Simulate the following scenarios during testing:
Region failures to verify multiregion failover behavior
ExpressRoute circuit failures to confirm VPN backup activation
Parallel path scenarios to identify asymmetric routing patterns
BGP route advertisement during failover events
- **Turn on monitoring and alerting for service health:** Set up monitoring for hub routers, gateways, and routing infrastructure to detect problems before users report outages. Create alerts for performance degradation for early response.
Turn on diagnostic logs across all Virtual WAN components to support troubleshooting through event correlation. Azure Resource Health distinguishes Azure service problems from customer-side connectivity problems.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| Choose the [Virtual WAN Standard SKU](/en-us/azure/virtual-wan/virtual-wan-about#basicstandard) for production deployments to get critical reliability capabilities. The Standard SKU provides zone redundancy, supports advanced routing scenarios, and provides hub-to-hub and branch-to-branch connectivity patterns. | Provides zone-redundant gateway deployment across availability zones for datacenter-level fault tolerance. Supports global transit architecture for multiregion connectivity patterns. |
| Select [NVAs](/en-us/azure/virtual-wan/about-nva-hub) that have native Virtual WAN hub integration. Native integration provides better reliability and support and avoids complex custom routing configurations. | Eliminates user-defined route maintenance overhead. Provides combined Microsoft and partner support for integrated solutions. |
| Deploy virtual hubs in at least two [Azure regions](/en-us/azure/virtual-wan/virtual-wan-global-transit-network-architecture) to establish redundancy. Choose regions close to users and workloads. Consider Azure paired regions for enhanced disaster recovery capabilities. | Maintains network operations during complete region failures. Preserves branch and virtual network connectivity through alternate region hubs. Supports workload distribution for load balancing. |
| Set up VPN gateways by using a [zone-redundant SKU](/en-us/azure/reliability/reliability-virtual-network-gateway) to provide automatic distribution across availability zones. Verify that the target region supports availability zones and confirm successful zone distribution through gateway properties. | Maintains VPN tunnel availability during availability zone failures. Eliminates single datacenter dependency through automatic instance distribution. |
| Set up [site-to-site VPN tunnels](/en-us/azure/vpn-gateway/about-active-active-gateways) in active-active configuration. Create a separate tunnel to each VPN gateway instance by using identical settings. Use BGP peering on both tunnels for dynamic routing and immediate failover without convergence delay. | Eliminates convergence delays during failover events. Provides instant traffic routing through alternative tunnels when the primary fails. Improves throughput compared to active-passive deployments. |
| Advertise routes from on-premises to Azure across all [ExpressRoute circuits](/en-us/azure/expressroute/designing-for-high-availability-with-expressroute) for active-active route advertisement. Use BGP autonomous system (AS) path prepending for traffic engineering when needed. Monitor the route advertisement status on all connections. | Maximizes ExpressRoute redundancy and bandwidth through automatic failover. Provides traffic distribution control via AS path prepending. Optimizes network utilization through active-active forwarding. |
| Set [virtual hub routing infrastructure units](/en-us/azure/virtual-wan/hub-settings) to exceed baseline requirements to accommodate anticipated growth. Set units based on expected traffic and growth projections. Monitor routing capacity utilization metrics to identify scaling needs and prevent performance degradation as traffic increases. | Avoids routing performance bottlenecks when traffic exceeds baseline capacity. Prevents the 25-minute scaling delay from affecting active connections. Supports workload expansion without service disruption. |
| Set VPN and ExpressRoute [gateway scale units](/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-gateway-settings) for expected aggregate throughput with extra capacity for future growth. Size gateway scale units based on throughput requirements and growth projections. Gateways don't automatically scale, and scale unit changes require maintenance windows. | Prevents capacity bottlenecks and connectivity degradation from gateway exhaustion. Avoids packet loss when traffic exceeds capacity. Reduces operational overhead by minimizing gateway resize tasks. |
| Create a [global VPN profile](/en-us/azure/virtual-wan/global-hub-profile) across all hubs to provide automatic hub selection for point-to-site connections. The global profile directs VPN clients to the nearest available hub and provides resilience when the primary hub becomes unavailable. | Ensures remote user connectivity during hub outages through automatic failover. Connects users to the nearest hub for optimal latency. Maintains productivity during regional failures. |
| Size the [point-to-site address pool](/en-us/azure/vpn-gateway/vpn-gateway-vpn-faq) with capacity to support double the expected user count. Size the address pool to prevent exhaustion during gateway instance redistribution. Monitor address pool utilization for ongoing capacity planning. | Prevents address exhaustion during gateway maintenance or failures. Provides single VPN profile deployment to all users. Supports business continuity for remote workforce. |
| Use [site-to-site VPN as backup connectivity](/en-us/azure/expressroute/use-s2s-vpn-as-backup-for-expressroute-privatepeering) for ExpressRoute circuits by deploying a VPN gateway alongside the ExpressRoute gateway in the virtual hub. Set the BGP preference to favor ExpressRoute over VPN. | Maintains connectivity when ExpressRoute fails. Preserves application availability for on-premises dependent services. |
| Turn on [diagnostic settings](/en-us/azure/virtual-wan/monitor-virtual-wan) for all Virtual WAN resources, like virtual hubs, gateways, and firewalls. Send the logs to a Log Analytics workspace for visibility. | Supports proactive problem detection and rapid incident response. Identifies connectivity problems before users report outages. Notifies operations teams instantly when failures occur. |
| Create alerts for [Virtual WAN metrics and Resource Health](/en-us/azure/virtual-wan/monitor-virtual-wan-reference) events. Create alerts for gateway connectivity failures and BGP peer session status changes. Set alerts for routing infrastructure capacity thresholds and turn on Resource Health alerts. | Accelerates troubleshooting through centralized log correlation. Provides historical data for pattern identification. Supports automated remediation workflows for common problems. |
| Review the [Virtual WAN disaster recovery guidance](/en-us/azure/virtual-wan/disaster-recovery-design) to learn about failure scenarios and mitigation strategies. | Systematic FMA identifies reliability risks early in design. Supports proactive mitigation through redundancy and failover mechanisms before production deployment. |

## Security

The purpose of the Security pillar is to provide **confidentiality, integrity, and availability** guarantees to the workload.

The [Security design principles](/en-us/azure/well-architected/security/security-principles) provide a high-level design strategy for achieving those goals by applying approaches to the technical design of Virtual WAN.

### Workload design checklist

Start your design strategy based on the [design review checklist for Security](../security/checklist) and identify vulnerabilities and controls to improve the security posture. Extend the strategy to include more approaches as needed.

- **Establish a security baseline:** Apply the [Azure security baseline for Virtual WAN](/en-us/security/benchmark/azure/baselines/virtual-wan-security-baseline) as your foundational security baseline. The baseline covers Virtual WAN-specific controls for hub security, gateway configuration, routing security, and connection encryption.
This standardized approach addresses Virtual WAN service endpoints, like virtual hubs, VPN gateways, ExpressRoute gateways, and Azure Firewall integration. It provides compliance mapping for network infrastructure requirements.
- **Implement network segmentation through routing controls:** Control network segmentation in Virtual WAN through routing tables. Create custom route tables to isolate routing domains and prevent unauthorized traffic between zones. Apply route maps when standard route table isolation doesn't meet connection requirements.
Deploy a secured virtual hub to inspect traffic centrally. Use Azure Firewall for threat intelligence and Azure service integration, or deploy partner NVAs for deep packet inspection and advanced threat prevention.
- **Establish private connectivity and protect public endpoints:** Deploy private endpoints in spoke networks to access Azure platform as a service (PaaS) solutions without internet exposure. On-premises users reach these services through ExpressRoute or VPN connections. Routing through secured hubs provides inspection but adds latency and cost.
Protect public-facing spoke workloads by using Azure DDoS Protection at the virtual network or IP address level. Hub public IP addresses don't support DDoS Protection.
- **Implement identity and access management:** Select your point-to-site VPN authentication method based on requirements.
Microsoft Entra ID authentication provides Microsoft Entra Conditional Access policies, multifactor authentication (MFA), device compliance checks, and risk-based authentication.
Certificate-based authentication requires public key infrastructure (PKI) and certificate life cycle management.
Remote Authentication Dial-In User Service (RADIUS) authentication integrates with existing RADIUS infrastructure.
Control Virtual WAN configuration access by using role-based access control (RBAC):
Apply RBAC assignments to control who can modify Virtual WAN configuration.
Use built-in Network Contributor and Reader roles for most scenarios.
Create custom roles for more granular permission boundaries when built-in roles are too permissive.
- **Control and filter network traffic by using defense in depth:** Deploy security controls at multiple network layers. Use the Virtual WAN Standard SKU to deploy Azure Firewall or partner security solutions in the hub for centralized application-aware filtering and threat protection. Deploy network security groups (NSGs) in spoke networks for subnet-level filtering based on IP addresses, ports, and protocols.
Each layer addresses different security requirements. Hub security controls enforce organization-wide policies and detect threats across all connected networks. Spoke NSGs provide workload-specific controls that teams define based on application requirements.
- **Ensure encrypted connectivity:** Select strong encryption algorithms like AES-256-GCM or AES-256-CBC to protect data confidentiality. Use strong integrity algorithms like SHA-256 or SHA-384 to prevent tampering. To prevent tunnel establishment failures, align Internet Protocol Security (IPsec) and Internet Key Exchange (IKE) encryption policies for site-to-site VPN between Azure and on-premises VPN devices.
- **Manage encryption for ExpressRoute and point-to-site VPN:** Evaluate ExpressRoute encryption requirements separately from VPN requirements because each connection type requires different configurations. Manage point-to-site VPN encryption based on client requirements and security policies.
- **Harden architecture by following Zero Trust principles:** Assume breach and limit the blast radius. Implement deny-by-default network access controls with explicit permit rules for required traffic only.
Turn off unused features to reduce attack surface:
Avoid legacy or weak VPN cipher suites like DES, 3DES, and MD5.
Remove unnecessary point-to-site authentication modes.
Eliminate unneeded public IP address assignments.
Turn on diagnostic logging, metric alerts, and Microsoft Sentinel threat detection to monitor for breaches.
- **Implement security monitoring and threat detection:** Turn on diagnostic logging for Virtual WAN components, like hubs, gateways, and Azure Firewall, for security event visibility. Use a Log Analytics workspace to provide centralized log collection, long-term retention, and query-based analysis.
Create Azure Monitor alerts for reactive notification of specific metric thresholds or log patterns. Deploy Microsoft Sentinel to add proactive threat detection through machine learning and correlation with broader organizational signals.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| Create [custom route tables](/en-us/azure/virtual-wan/scenario-isolate-vnets-custom) that match your defined security zones. Set [route table associations](/en-us/azure/virtual-wan/how-to-virtual-hub-routing) on spoke virtual network connections. Set route table propagations to control which route tables receive routes from connections. Set the route table association to **None** to completely isolate a connection and prevent any route sharing. | Prevents unauthorized traffic between segmented zones through route control. Reduces blast radius by limiting communication with compromised resources. Provides granular connectivity control. |
| Create [private endpoints](/en-us/azure/virtual-wan/howto-private-link) in spoke virtual networks for PaaS services that require private connectivity, like Azure Storage, Azure SQL Database, Azure Cosmos DB, and other [supported services](/en-us/azure/private-link/private-endpoint-overview#private-link-resource). Integrate private endpoints with spoke virtual network subnets. Route private endpoint traffic through a secured virtual hub when inspection is required. | Eliminates data exfiltration risks from PaaS services. Reduces attack surface by removing public endpoints. Provides secure PaaS access from on-premises networks. |
| Turn on [DDoS Protection](/en-us/azure/ddos-protection/manage-ddos-protection) at the virtual network level, or turn on DDoS IP Protection for individual public IP addresses. Apply protection to public IP addresses on workload resources. Virtual WAN hub public IP addresses don't support DDoS Protection, so implement it at the spoke level. | Detects and mitigates volumetric attacks that attempt to overwhelm network bandwidth. Absorbs attack traffic before it reaches workloads. Automatically scales mitigation capacity during attacks. |
| Register the [Azure VPN application](/en-us/azure/vpn-gateway/openvpn-azure-ad-tenant) in your Microsoft Entra ID tenant and use Microsoft Entra ID authentication for the VPN gateway. Deploy Azure VPN Client to user devices with a profile that authenticates through Microsoft Entra ID. | Prevents unauthorized VPN access through MFA. Supports risk-based authentication that adapts to user risk, sign-in risk, and device posture. |
| Create [Conditional Access policies](/en-us/azure/vpn-gateway/openvpn-azure-ad-mfa) that target the Azure VPN application to enforce MFA, device compliance, and location restrictions. | Enforces adaptive access controls for VPN connections. Requires MFA for high-risk sign-ins. Restricts access to compliant devices and trusted locations. |
| Assign the [Network Contributor role](/en-us/azure/virtual-wan/roles-permissions) for full management permissions, and assign the Reader role for view-only access. Create custom RBAC roles when built-in roles exceed required permissions. | Prevents unauthorized configuration changes through permission limits. Reduces the impact of compromised accounts through least privilege. Supports separation of duties through role-based job functions. |
| Select the Virtual WAN Standard SKU to deploy security solutions. Deploy [Azure Firewall](/en-us/azure/firewall/overview) or a partner security solution in the virtual hub for centralized filtering. Use [routing intent](/en-us/azure/virtual-wan/how-to-routing-policies) to automatically route traffic through the security solution. Use internet traffic routing intent for outbound traffic inspection. | Delivers traffic filtering through centralized hub security and distributed spoke controls. Supports workload-specific controls via spoke NSGs. Provides flexibility for implementing controls at the appropriate architectural layer. |
| Implement [NSGs](/en-us/azure/virtual-network/network-security-groups-overview) on subnets in spoke virtual networks for subnet-level filtering. Deploy a hub security solution for application and threat inspection. Use spoke NSGs for network-level filtering based on IP addresses, ports, and protocols. | Spoke NSGs provide granular workload-specific controls that complement hub security policies. This layered approach supports explicit permit rules for required traffic and enforces deny-by-default posture. It reduces the attack surface and limits lateral movement after compromise. |
| Turn on [diagnostic settings](/en-us/azure/virtual-wan/monitor-virtual-wan) on Virtual WAN resources, virtual hubs, VPN gateways, ExpressRoute gateways, point-to-site gateways, and Azure Firewall. Turn on log categories, including AllMetrics, GatewayDiagnosticLog, TunnelDiagnosticLog, RouteDiagnosticLog, and IKEDiagnosticLog. Route logs to a Log Analytics workspace for centralized collection. Build queries that target security-relevant events, like authentication failures, connection anomalies, and configuration changes. | Supports security event detection through analysis of suspicious activities and anomalous behaviors. Supports compliance and audit requirements through long-term event retention. Provides forensic evidence for security incident investigation. |
| Create [metric alerts](/en-us/azure/virtual-wan/monitor-virtual-wan) for security-relevant metrics, like VPN gateway connection status, ExpressRoute circuit status, BGP peer status, and bandwidth utilization anomalies. Set alert thresholds based on established baseline metrics for normal operations. Use action groups to route alerts to security operations or automated response systems. | Supports rapid detection of connectivity failures that indicate security problems or denial of service. Identifies bandwidth anomalies that indicate data exfiltration. Provides early detection of BGP routing problems that affect segmentation. |
| Connect [Microsoft Sentinel](/en-us/azure/sentinel/overview) to the Log Analytics workspace that receives Virtual WAN logs. Turn on the [Azure Firewall data connector](/en-us/azure/sentinel/data-connectors/azure-firewall) in Microsoft Sentinel. Create analytics rules for Virtual WAN threat scenarios, like anomalous VPN authentication patterns, unusual traffic volumes, and firewall policy violations. Create incident response playbooks that automate actions like blocking suspicious source IP addresses and compromised VPN users. | Provides advanced threat detection through machine learning and behavioral analytics. Correlates Virtual WAN security events with organizational security telemetry. Provides security operations teams with unified monitoring. |

## Cost Optimization

Cost Optimization focuses on **detecting spend patterns, prioritizing investments in critical areas, and optimizing in others** to meet the organization's budget while meeting business requirements.

The [Cost Optimization design principles](/en-us/azure/well-architected/cost-optimization/principles) provide a high-level design strategy for achieving those goals and making tradeoffs as necessary in the technical design related to Virtual WAN and its environment.

### Workload design checklist

Start your design strategy based on the [design review checklist for Cost Optimization](../cost-optimization/checklist) for investments. Fine-tune the design so that the workload is aligned with the budget that's allocated for the workload. Your design should use the right Azure capabilities, monitor investments, and find opportunities to optimize over time.

- **Understand pricing structures to create accurate cost models:** Virtual WAN pricing has fixed and variable components. Fixed costs include SKU selection and allocated scale and connection units. Variable costs include data transfer charges and active features.
Data transfer costs represent significant variable expenses. Hub-to-hub transfers across regions incur cross-region charges, while hub router processing contributes to hub data processing costs. Estimate both fixed and variable costs before deployment to avoid budget surprises.
- **Monitor costs and hub utilization for ongoing optimization:** Implement daily cost tracking for Virtual WAN spending. Focus on hub data processing charges, gateway connection usage, and cross-region data transfer costs.
Organize resources by business unit or application by using tags for cost allocation. Implement chargeback or showback reporting. Monitor spending against budgets to detect unexpected increases early.
- **Establish spending guardrails by using budgets and alerts:** Implement budgets and alerts to prevent unexpected spending. Set graduated alert thresholds for early warnings before budget exhaustion.
Track metrics that directly affect variable costs. Monitor hub router traffic volume for hub data processing charges and connection unit usage for capacity costs.
Apply governance policies to prevent unauthorized cost increases. Use Azure Policy to require approvals for high-cost changes and mandate reviews before you add capacity.
- **Rightsize infrastructure capacity based on actual workload requirements:** Size routing infrastructure units based on actual workload needs rather than maximum theoretical capacity. Each unit increases virtual machine (VM) capacity and costs.
Each hub incurs fixed monthly costs regardless of traffic volume. Add hubs only where connectivity requirements justify the cost. Size gateway scale units based on actual throughput requirements. Track usage patterns and adjust capacity when monitoring shows sustained changes in demand.
- **Choose cost-effective connection types and integrated service SKUs:** Site-to-site VPN provides cost-effective connectivity for lower bandwidth and noncritical connections. ExpressRoute delivers higher performance at substantially higher cost. Point-to-site VPN supports remote users that have different cost characteristics.
Use VPN for development and test environments where lower cost justifies variable performance. Use ExpressRoute for production workloads that require consistent bandwidth and reliability. Implement hybrid approaches that route routine traffic through a VPN and direct business-critical applications through ExpressRoute.
- **Optimize routing to minimize data transfer costs:** Traffic flow patterns directly affect variable costs. Hub-to-hub communication across regions generates cross-region charges. Hub router processing contributes to hub data processing costs.
Optimize the routing topology to reduce costs without sacrificing connectivity. Use direct virtual network peering for spoke-to-spoke communication to bypass hub processing charges. Evaluate the hub location based on dominant traffic patterns to minimize cross-region transfer charges. Balance cost optimization against security and routing policy requirements.
- **Develop a cost-effective scaling strategy for growth:** Plan hub placement to balance latency requirements with costs. Position hubs near user populations to reduce latency and avoid excessive hub count. Consolidate regions where acceptable latency thresholds permit.
Optimize connection unit allocation based on actual bandwidth requirements rather than theoretical capacity. Monitor utilization to identify optimization opportunities as demand fluctuates.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| Use the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) to model deployment costs before implementation. Set up expected hubs across regions, select connection types with appropriate scale units, and estimate monthly data transfer volumes. Estimate bandwidth requirements to determine gateway scale units. Calculate minimum hub capacity in routing infrastructure units based on anticipated VM workload and throughput needs. | Supports budget planning and approval with accurate cost estimates. Anticipates variable costs from data transfer and hub processing before deployment. |
| [Apply tags to Virtual WAN hubs](/en-us/azure/azure-resource-manager/management/tag-resources), VPN gateways, ExpressRoute gateways, and connections. Use consistent naming conventions, like business unit, application name, environment, or cost center. Use Azure Policy to enforce mandatory tags on resource creation. Create Microsoft Cost Management reports to aggregate and filter costs by tag values. Use tagged cost data for chargeback or showback to business units. | Provides accurate cost allocation to business units or applications. Supports chargeback models for internal cost recovery and departmental accountability. |
| Use [Azure Monitor](/en-us/azure/virtual-wan/monitor-virtual-wan) to collect hub router traffic volume metrics continuously. Create workbooks or dashboards that visualize trends over time. Establish baseline traffic patterns to identify normal versus anomalous behavior. Use traffic volume data to identify optimization opportunities. Detect high-volume spoke-to-spoke traffic that can use direct peering instead of hub routing, unexpected spikes that require investigation, or inefficient routing patterns that increase hub processing costs. | Supports data-driven optimization decisions based on actual traffic patterns. Supports cost forecasting through traffic trend tracking. |
| Create a [Cost Management budget](/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets) for the Virtual WAN resource group or subscription based on cost model projections. Set alert thresholds at 90%, 100%, and 110%. Assign stakeholder email addresses or action groups to receive alerts at each threshold. Create metric alerts on hub router traffic volume when it approaches levels that correlate with budget concerns. Analyze historical patterns to establish a baseline and set alert thresholds before traffic reaches budget-critical levels. | Proactive notification prevents unexpected cost overruns and supports timely intervention before costs exceed budget. Provides greater visibility into Virtual WAN spending patterns for better cost management. |
| Set virtual hub routing infrastructure units to the minimum level adequate for current workload. Start conservatively by using baseline capacity rather than anticipated peak. Each unit supports a specific VM count and [throughput capacity](/en-us/azure/virtual-wan/hub-settings#capacity). Set [VPN gateway scale units](/en-us/azure/virtual-wan/gateway-settings) to match anticipated site-to-site throughput, with each unit providing 500-megabits per second (Mbps) capacity. Set ExpressRoute gateway scale units to match connection needs, with each unit delivering 2-gigabits per second (Gbps) bandwidth. Schedule capacity adjustments during planned maintenance windows. Increase capacity when utilization monitoring shows that you're approaching limits, or reduce capacity when monitoring shows consistently low utilization. | Optimizes hub costs by aligning capacity with actual workload, which prevents overprovisioning waste from excessive unit allocation. Maintains adequate capacity for performance requirements without excessive spending. |
| Assess connectivity requirements for each site, branch, or connection endpoint to determine appropriate connection types based on workload criticality and performance needs. Use [site-to-site VPN connections](/en-us/azure/virtual-wan/virtual-wan-site-to-site-portal) for development environments, testing workloads, nonproduction scenarios, backup connectivity paths, or moderate bandwidth requirements that don't require guaranteed SLAs. Use [ExpressRoute connections](/en-us/azure/virtual-wan/virtual-wan-expressroute-portal) for mission-critical production workloads that require guaranteed bandwidth. Implement hybrid connectivity by using VPN connections and ExpressRoute together. Route general connectivity through a VPN and direct critical application traffic through ExpressRoute. | Reduces connectivity costs through appropriate use of lower-cost VPN options. Maintains performance and reliability for critical workloads. Supports cost-effective scaling by using VPN connections for noncritical growth. |
| Assess whether specific virtual network-to-virtual network traffic flows require hub-mediated routing by determining if centralized routing policy enforcement is necessary or if Azure Firewall or NVA inspection is required. Use [direct virtual network peering](/en-us/azure/virtual-network/virtual-network-peering-overview) between virtual networks that have high-volume communication and don't require hub processing. Create peering connections between source and destination virtual networks, update route tables to use peering instead of a hub router, and verify connectivity through the direct path. | Reduces hub data processing costs by eliminating the hub router from virtual network-to-virtual network traffic paths. Improves network latency for peered virtual networks and saves money. |

## Operational Excellence

Operational Excellence primarily focuses on procedures for **development practices, observability, and release management**.

The [Operational Excellence design principles](/en-us/azure/well-architected/operational-excellence/principles) provide a high-level design strategy for achieving those goals for the operational requirements of the workload.

### Workload design checklist

Start your design strategy based on the [design review checklist for Operational Excellence](../operational-excellence/checklist) for defining processes for observability, testing, and deployment related to Virtual WAN.

- **Implement infrastructure as code (IaC) for consistent deployments:** Use Azure Resource Manager templates (ARM templates), Bicep, or Terraform for repeatable Virtual WAN deployments across environments. ARM templates and Bicep provide native Azure integration. Terraform supports multicloud scenarios.
- **Design modular IaC templates:** Separate core hub infrastructure from connection policies and routing rules. Core infrastructure changes infrequently, and routing rules change more often. Parameterize environment-specific values like scale units and address spaces.
- **Orchestrate resource dependencies:** Sequence operations correctly because gateways require hubs, connections require gateways, and routing policies require connections. Include wait conditions in your automation to verify route propagation before you mark the deployment complete.
- **Establish build and deployment pipelines for automation:** Design deployment pipelines with stage separation for validation, approval, and deployment. Implement quality gates between stages to block problematic changes.
Include static validation for syntax checking, policy compliance, and security rule verification. Implement predeployment testing for configuration validation against organizational standards.
- **Implement monitoring for topology, services, and dependencies:** Establish complete visibility across topology, service health, and operational telemetry. Monitor global hub distribution, spoke connectivity, and gateway operational status.
Collect gateway performance metrics for throughput utilization and connection counts. Track connection reliability metrics for tunnel availability. Monitor routing health metrics for route propagation status.
Design role-based operational views. Create real-time health dashboards for operations teams and capacity trend views for architects. Set data retention periods that balance the need for historical investigation with storage costs.
- **Create alerting for connectivity and performance problems:** Design alerting around failure scenarios that affect operations. Target connectivity failures that disrupt user access, performance degradation that slows applications, and configuration anomalies that indicate errors.
Define specific measurable conditions like tunnel disconnections, gateway CPU saturation above safe thresholds, and unexpected routing changes. Balance alert thresholds between early detection and alert fatigue. Establish notification routing that matches alert severity with appropriate urgency.
- **Automate operational tasks and connectivity validation:** Automate repetitive Virtual WAN tasks like connection status validation and multihub configuration updates. Automate time-sensitive operations to reduce manual effort.
Implement scheduled automation for routine health checks. Use event-driven automation for configuration drift remediation. Create validation scripts and troubleshooting tools that operators can run on demand.
Use Virtual WAN native automation capabilities, including automatic route advertisement, route propagation across hub infrastructure, and gateway autoscaling that responds to load patterns.
- **Implement progressive deployment practices:** Deploy to development first and then to staging, and validate at each step. Run static configuration validation and policy compliance checks before deployment. Follow deployment with smoke tests to verify gateway reachability and connection establishment.
- **Establish rollback capability:** Maintain configuration versioning in an IaC repository. Document rollback procedures for reverting gateway settings and routing policies. Separate routine deployments from emergencies. Route routine changes through full validation with approvals. Allow emergencies to skip extended approvals while still validating syntax.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| Use [ARM templates](/en-us/azure/templates/microsoft.network/virtualwans) or [Bicep](/en-us/azure/azure-resource-manager/bicep/overview) for Virtual WAN infrastructure deployment. Define modular templates that separate resource types, like hubs, VPN and ExpressRoute gateways, connections, and routing policies. Parameterize environment-specific values, like hub address spaces, gateway scale units, connection settings, and routing preferences. Deploy templates by using the Azure CLI or Azure PowerShell with environment-specific parameter files. Store templates in version control with continuous integration and continuous delivery (CI/CD) pipeline integration. | Ensures consistent configuration through declarative syntax. Tracks changes and supports rollback through version control. Deploys identical architectures across environments by using parameterization. |
| Create a CI/CD pipeline by using [Azure Pipelines](/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines) or [GitHub Actions](/en-us/azure/developer/github/github-actions) for Virtual WAN deployment automation. Define a multistage pipeline that has separate stages for validation, development deployment, and production deployment. Set up the validation stage with ARM template validation, Azure Policy compliance checks, and security scanning. Add approval gates that require manual approval before production deployment. Define deployment stages with environment-specific parameters and service connections. | Reduces manual effort and eliminates human error through automation. Prevents problematic changes from reaching production by using approval gates. Supports compliance and incident investigation through deployment history. |
| Use [Azure Monitor Insights](/en-us/azure/virtual-wan/azure-monitor-insights) for Virtual WAN to access integrated topology visualization and [metrics workbooks](/en-us/azure/virtual-wan/monitor-virtual-wan). Collect metrics for gateway throughput, connection counts, BGP peer status, and routing table health. Set the metric collection interval and aggregation granularity based on monitoring requirements. For long-term analysis, export metrics to a Log Analytics workspace for retention beyond the default 93-day period. | Provides unified visibility across regions and hubs. Delivers immediate value without custom development through built-in dashboards. Supports rapid diagnosis and capacity planning through historical data. |
| Turn on [diagnostic settings](/en-us/azure/azure-monitor/essentials/diagnostic-settings) for Virtual WAN hub, VPN gateway, and ExpressRoute gateway resources. Collect logs for GatewayDiagnosticLog, TunnelDiagnosticLog, RouteDiagnosticLog, and IKEDiagnosticLog categories. Send logs to a Log Analytics workspace for centralized analysis. Create operational dashboards by using [Azure dashboards](/en-us/azure/azure-monitor/visualize/tutorial-logs-dashboards) or [workbooks](/en-us/azure/azure-monitor/visualize/workbooks-overview) to visualize gateway status, connection counts, error trends, and throughput metrics. Set dashboard refresh intervals and time ranges for operational monitoring needs. | Supports effective troubleshooting through detailed telemetry. Provides operational visibility by capturing gateway events and state transitions. Supports audit and compliance requirements through change documentation. |
| Create [metric alert rules](/en-us/azure/azure-monitor/alerts/alerts-create-metric-alert-rule) for Virtual WAN gateway and hub resources. Set alert conditions for VPN gateway metrics, like TunnelEgressPacketDropCount, TunnelIngressPacketDropCount, and TunnelBandwidth thresholds. Set ExpressRoute gateway alerts for BitsInPerSecond and BitsOutPerSecond when they approach circuit capacity. Create Virtual WAN hub alerts for PacketCount drops and RoutingState changes that indicate routing propagation problems. Create [action groups](/en-us/azure/azure-monitor/alerts/action-groups) that specify notification methods, like email, SMS, or webhook. Assign recipients based on alert severity. Set the alert evaluation frequency and lookback window to balance detection latency with alert accuracy. This approach prevents excessive false positives and maintains timely problem detection. | Minimizes business impact through rapid detection of connectivity or performance problems. Provides early warning before critical failures. Supports root cause analysis and proactive capacity planning through historical alert data. |
| Use the [Azure Network Watcher connection monitor](/en-us/azure/network-watcher/connection-monitor-overview) for automated connectivity testing across Virtual WAN infrastructure. Define test groups with source and destination endpoints that cover hub-to-hub, hub-to-spoke, and on-premises paths. Define test parameters, like Transmission Control Protocol (TCP) or Internet Control Message Protocol (ICMP), port numbers, probe frequency, and success thresholds. Set alert thresholds for test failures and latency that exceed acceptable limits. Integrate results with operational dashboards for continuous connectivity visibility. | Continuous validation detects connectivity problems before they affect users. Automated testing validates all paths and identifies failures immediately. End-to-end testing verifies complete connectivity, including routing and network paths. This approach reduces mean time to detection (MTTD) compared to reactive user reporting. |
| Create [Azure Automation](/en-us/azure/automation/overview) runbooks for repetitive Virtual WAN tasks. Examples include gateway scaling automation that monitors capacity metrics and updates configuration, VPN site management for bulk operations, and health validation that checks gateway status and routing tables. Invoke runbooks by using scheduled triggers for routine tasks or event-driven triggers based on Azure Monitor alerts. Use Azure Policy for drift detection and automatic remediation. Define policies that validate gateway SKU compliance, diagnostic settings, and network security rules. Set up [automatic remediation](/en-us/azure/governance/policy/concepts/effects) by using DeployIfNotExists or Modify effects. | Eliminates time-consuming repetitive tasks. Applies standards uniformly across hubs and gateways. Provides proactive maintenance and reactive responses to operational events. Maintains desired state through drift remediation and reduces misconfiguration risk. |
| Define [customer-controlled maintenance](/en-us/azure/virtual-wan/customer-controlled-gateway-maintenance) windows for VPN and ExpressRoute gateways. Define a maintenance schedule for a day of week, start time, and duration that aligns with low-traffic periods. Apply schedules to gateways individually or stagger them across hubs. Use phased deployment in your [CI/CD pipeline](/en-us/devops/deliver/what-is-continuous-delivery). Deploy to development and test environments first with connectivity validation. Then deploy to the first production hub. Monitor the hub for a period before you expand to the remaining hubs. Maintain rollback capability through IaC version control. Maintain previous configuration versions by using rollback tags in your Git repository. Deploy rollbacks by using previous ARM template versions and parameter files. Consider blue-green deployment patterns for instant traffic shifting. | Predictable maintenance timing reduces unplanned disruption risk. Scheduling maintenance during planned periods allows coordination with application teams. Phased rollout detects problems in development before they affect production. Automated rollback supports immediate recovery, and blue-green patterns support instant traffic shifting. |

## Performance Efficiency

Performance Efficiency is about **maintaining user experience even when there's an increase in load** by managing capacity. The strategy includes scaling resources, identifying and optimizing potential bottlenecks, and optimizing for peak performance.

The [Performance Efficiency design principles](/en-us/azure/well-architected/performance-efficiency/principles) provide a high-level design strategy for achieving those capacity goals against the expected usage.

### Workload design checklist

Start your design strategy based on the [design review checklist for Performance Efficiency](../performance-efficiency/checklist) for defining a baseline based on key performance indicators for Virtual WAN.

- **Conduct capacity planning for components:** Plan Virtual WAN capacity by assessing VPN and ExpressRoute gateways, hub routers, and routing infrastructure. Start by estimating VPN gateway throughput per tunnel because all active tunnels share the total gateway capacity.
Monitor current utilization across gateways and hub routers to establish performance baselines. Use these baselines to project future capacity needs accurately. Include peak traffic scenarios, expected business growth, and planned site connections in your capacity plans.
- **Implement performance monitoring:** Implement performance monitoring for every Virtual WAN component to maintain optimal operation. Establish a performance baseline during normal operations to identify typical behavior and detect deviations.
Monitoring data supports capacity planning initiatives and identifies optimization opportunities before performance degradation occurs. Tracking performance trends over time helps you predict future requirements and plan infrastructure changes proactively.
- **Design for scalable architecture:** Plan for horizontal scaling by adding hubs within regions when requirements exceed per-hub limits. Design routing infrastructure to support anticipated inter-hub and spoke-to-spoke traffic volumes while balancing performance requirements with cost considerations.
Validate scaling effectiveness through performance monitoring and capacity utilization analysis to ensure that the architecture meets business needs as requirements evolve.
- **Allocate spoke Virtual Network address ranges in a scalable and operationally simple manner:** Pre-allocate contiguous IP ranges that are unique and distinct for Virtual Networks connected to each Virtual WAN hub. Utilizing hub-level contiguous ranges simplifies network management and operational overhead when using route-maps to modify BGP attributes of spoke Virtual Network address in bulk or to perform route summarization or aggregation.
- **Establish performance testing practices:** Performance testing practices require deploying nonproduction Virtual WAN environments that match production configuration for validation. Test routing configurations, connectivity scenarios, and feature activation before production deployment to ensure optimal performance.
Use testing to validate performance for branch-to-Azure, branch-to-branch, and virtual network-to-virtual network traffic patterns. Evaluate gateway performance under peak traffic and concurrent connection loads. Compare test results against performance targets and baselines before you implement changes to prevent performance problems in production environments.
- **Optimize hub placement for minimal latency:** Optimize hub placement by positioning hubs in regions close to user populations and branch office locations to minimize network latency. Optimize hub placement for dominant traffic patterns like branch-to-Azure, branch-to-branch, or virtual network-to-virtual network connectivity. Consider cross-region traffic requirements and inter-hub connectivity performance.
- **Optimize configurations for performance:** Evaluate gateway sizing strategies by assessing VPN and ExpressRoute gateway capacity against bandwidth requirements and traffic projections. Account for peak traffic scenarios and expected business growth when you choose appropriate gateway SKUs.
Select IPsec encryption algorithms that balance security requirements with gateway CPU efficiency. Design routing path preferences to optimize business-critical traffic patterns. Consider the performance characteristics of different routing options, like hub-to-hub paths versus ExpressRoute paths for virtual network-to-virtual network scenarios.
- **Validate routing for performance troubleshooting:** Design operational procedures to verify route learning and propagation across hybrid network components. Document troubleshooting workflows for routing-related performance problems. Apply findings from routing incidents to improve monitoring and preventive measures.
- **Monitor and optimize capacity continuously:** Establish proactive practices that maintain performance as requirements evolve. Design a proactive capacity management approach that includes regular performance reviews. Plan capacity adjustments before utilization reaches limits to avoid negative performance impact. This approach aligns capacity optimization with business growth and changing connectivity patterns.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| Turn on native [Azure Monitor metrics](/en-us/azure/virtual-wan/monitor-virtual-wan-reference) for the hub router, ExpressRoute gateway, and VPN gateway components. Collect throughput metrics, connection health indicators, bandwidth utilization, packet loss rates, and latency measurements with appropriate retention periods. Set the metric retention to support historical trend analysis and capacity planning requirements. Create alert rules for critical performance thresholds including gateway throughput limits and hub capacity constraints. | Identifies performance bottlenecks before they affect users. Supports capacity planning through historical data. Simplifies monitoring through native Azure Monitor integration. |
| Set [routing infrastructure units](/en-us/azure/virtual-wan/hub-settings) at hub deployment based on calculated inter-hub and spoke-to-spoke throughput requirements. Deploy multiple hubs within the same region when traffic volumes exceed single hub limits or when you need different routing configurations. | Prevents bottlenecks in inter-hub and spoke-to-spoke connectivity. Supports expected traffic volumes without overprovisioning. Supports cost-effective performance with rightsized infrastructure. |
| Identify the geographic distribution of users, branch offices, and on-premises datacenters to position hubs optimally for highest-volume and most critical traffic patterns. Test network path latency to validate region selection before deployment. Evaluate multiregion deployment when populations span large geographic areas. | Minimizes network latency for users and applications. Improves application performance and user experience. Decreases network round-trip times for critical workloads. |
| Set the [hub routing preference](/en-us/azure/virtual-wan/about-virtual-hub-routing-preference) to **ExpressRoute**, **VPN Gateway**, or **AS Path** based on primary connectivity type and performance requirements for spoke-to-spoke traffic. Select **ExpressRoute** when ExpressRoute circuits provide lower latency paths between spoke virtual networks. Test the selected routing preference in a nonproduction environment before production deployment. | Reduces latency for critical connectivity scenarios. Provides efficient traffic path selection. Improves throughput efficiency for inter-hub and spoke traffic. |
| Set the GCMAES256 algorithm for both IPsec encryption and IPsec integrity parameters on site-to-site VPN connection [custom IPsec policies](/en-us/azure/vpn-gateway/vpn-gateway-about-compliance-crypto). Apply a custom IPsec policy with GCMAES256 settings to VPN connections during connection creation. | Reduces CPU overhead on VPN gateways and supports higher throughput on VPN site-to-site connections. Maintains security and maximizes gateway capacity utilization for improved performance. |
| Monitor [virtual hub effective routes](/en-us/azure/virtual-wan/effective-routes-virtual-hub) in hub routing tables. Verify that expected routes are present and learned correctly from connected resources. Monitor VM network interface card (NIC) effective routes to confirm that VMs receive correct routes from Virtual WAN hubs. Verify that route advertisements from on-premises BGP routers reach Virtual WAN hubs with expected metrics. Create Azure Monitor alerts for routing anomalies, like missing expected routes or route metric changes. | Identifies routing problems before they affect users and reduces mean time to resolution (MTTR) for connectivity and performance problems. Prevents performance degradation from routing misconfigurations through proactive monitoring. |
| Monitor [VPN Gateway](/en-us/azure/vpn-gateway/monitor-vpn-gateway) throughput metrics and [ExpressRoute gateway](/en-us/azure/expressroute/monitor-expressroute) throughput metrics. Track utilization against gateway SKU capacity limits. Monitor connection counts, packet rates per second, and active tunnel metrics to identify capacity constraints. Establish utilization threshold alerts at 70% capacity to trigger gateway resizing evaluation. Resize gateway SKUs when sustained utilization exceeds 80% capacity or during performance degradation. | Proactive capacity management maintains network performance as usage grows. Maintains consistent connection speeds and application response times as traffic patterns change. Early detection at 70% capacity provides time to plan gateway upgrades during scheduled maintenance windows. Prevents sudden decreases in performance that force emergency changes and disrupt users. Monitoring connection counts and packet rates helps you find capacity trends before they become problems. |
| When choosing private IP addresses to allocate to Virtual Networks connected to Virtual WAN, ensure that all IP addresses assigned to Virtual Networks connected to a single VIrtual WAN hub are allocated from unique and contiguous range(s) specific to that Virtual WAN hub. | Contiguous ranges can be aggregated or modified in bulk with [route-maps](/en-us/azure/virtual-wan/route-maps-about). This makes scaling network designs with Virtual WAN simpler and more manageable, especially when outbound route limits (1000 route limit for ExpressRoute, 1000 route limit for OpenVPN Point-to-site VPN, 255 route limit for Ikev2 Point-to-site VPN clients or 4000 route limit for Site-to-site VPN) require network summarization. In many scenarios, route aggregation or summarization is required to be done on the hub-level. For example, aggregate all spoke Virtual Networks to Virtual WAN hub 1 to a single /22 and aggregating all spoke Virtual Networks to Virtual WAN hub 2 to a different /22. |

## Azure Policy

Azure provides an extensive set of built-in policies related to Virtual WAN and its dependencies. Some of the preceding recommendations can be audited through Azure Policy. For example, you can check whether:

- Azure Firewall protects virtual hubs for centralized security inspection.
- VPN gateways avoid using the Basic SKU because it lacks reliability and performance features.
- Point-to-site VPN connections use Microsoft Entra ID authentication for enhanced security.

For comprehensive governance, review the [Azure Policy built-in definitions for Virtual WAN](/en-us/azure/governance/policy/samples/built-in-policies#network) and other policies that might affect network infrastructure security.

## Azure Advisor recommendations

Azure Advisor is a personalized cloud consultant that helps you follow best practices to optimize your Azure deployments.

For more information, see [Azure Advisor](/en-us/azure/advisor).

## Example architecture

Foundational architecture that demonstrates the key recommendations: [Hub-spoke network topology that uses Virtual WAN](/en-us/azure/architecture/networking/architecture/hub-spoke-virtual-wan-architecture).

## Related content

- [Virtual WAN FAQ](/en-us/azure/virtual-wan/virtual-wan-faq)
- [Training: Introduction to Virtual WAN](/en-us/training/modules/introduction-azure-virtual-wan/)
- [Virtual WAN partners, regions, and locations](/en-us/azure/virtual-wan/virtual-wan-locations-partners)

## Feedback

Was this page helpful?

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

## Additional resources

- Last updated on 2026-02-02

---

> 原页面：https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-virtual-wan（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
