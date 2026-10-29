<!-- source: https://learn.microsoft.com/en-us/azure/well-architected/design-guides/capacity-resilience -->
<!-- captured: 2026-10-25 -->
<!-- vendor: azure -->

# How to design for capacity resilience

Note




Cloud computing is often described as *elastic* because of its ability to scale workloads and consume infrastructure without worrying about underlying hardware.

All cloud hyperscalers operate within the physical infrastructure available to support their services, including datacenter space, servers, networking, power, and cooling. As demand nears available supply, constraints can affect resource allocation and deployment, making proactive capacity planning a non-negotiable exercise.

This article covers architectural approaches and Azure capabilities that can proactively help you plan for capacity and minimize those issues during deployment. This article doesn't provide troubleshooting guidance or short term-mitigations. For that information, see [Troubleshoot allocation failures when you create or resize VMs in Azure](/en-us/troubleshoot/azure/virtual-machines/windows/allocation-failure).

## Terminology

| Term | Definition |
| --- | --- |
| **Allocation failure** | An error that occurs when a deployment request has sufficient quota but the physical capacity isn't available in the target region or availability zone. Common errors include `AllocationFailed` and `ZonalAllocationFailed`. |
| **Availability zone** | A group of datacenters within a region. Each availability zone is independent of the other availability zones and has its own power, cooling, and networking infrastructure. |
| **Azure Compute Fleet** | A capacity orchestration service that abstracts VM SKU selection by automatically selecting optimal combinations of VM types, availability zones, and pricing models to maximize deployment success. |
| **Azure Quota Groups** | An organizational feature that allows self-management and sharing of quota across multiple subscriptions, enabling dynamic reallocation based on workload demand rather than treating quota as siloed team boundaries. |
| **Capacity** | The amount of underlying physical infrastructure (datacenters, servers, networking, power, cooling) available in a specific region, availability zone, or cluster for a requested resource. |
| **Capacity Reservation Groups** | A logical container that groups capacity reservations, enabling centralized management and sharing of reserved capacity across subscriptions and business units. |
| **On-demand Capacity Reservation (ODCR)** | A feature that reserves VM compute capacity in a specific region or availability zone, guaranteeing capacity for critical workloads. Combines with Reserved Instances or Savings Plans for cost optimization. |
| **Quota** | A policy on how many resources your subscription can request in a given region and SKU family. |
| **Zone resiliency** | A deployment strategy where resources are spread across multiple availability zones within a region to protect against zone outages or capacity limitations. |

## Understand quota and capacity

Two distinct concepts control resource allocation in Azure: quota and capacity. Both must align for successful deployment.

*Quota* is the policy. It limits how many resources your subscription can consume in a given region and SKU family. For example, if your subscription has a quota of 100 vCPUs in East US, you can provision up to 100 vCPUs in that region.

*Capacity* is supply. It's the amount of underlying infrastructure available in a specific region or availability zone for the exact resource configuration being requested.

Unlike quota, capacity can only increase if the platform acquires more infrastructure.

Capacity-related deployment issues can occur at multiple scopes as shown in this image. Azure capacity is distributed across a large global pool, but each scope such as region, zone, service, VM family and SKU, or cluster placement rule narrows the set of valid targets for a deployment.

- Availability zone level: A single availability zone might run out of capacity for a specific SKU while other zones in the same region remain unaffected.
- Region level: An entire region might be constrained for a particular service or VM SKU, leaving no available capacity regardless of the zone selected.
- SKU level: Capacity can be limited to specific hardware or service offerings. For example, high-demand GPU instances or newly introduced VM families might be constrained, while other SKUs remain readily available.

Understand which scopes need flexibility so that you improve the chances of a successful deployment.

You can increase the resource limits assigned to your Azure subscription through quota requests. The system typically processes standard requests automatically and completes them quickly. For constrained resources, the system reviews requests manually. Large requests or requests in constrained regions can take longer to approve. Microsoft works with you through your support case to identify the best path forward.

## What are allocation failures?

Allocation failures occur when you have sufficient quota but physical capacity isn't available.

Those failures might be triggered by a particular combination of resource, configuration, and location, which can't be provisioned at a given moment. They usually appear during moments of change. For example, when you scale out during demand growth, resize or upgrade VM families, or during in-place updates.

During those events, you might see deployment failures with errors like `AllocationFailed` or `ZonalAllocationFailed`. You might also see SKU unavailability messages for a particular zone. For more information about allocation failures, see [Troubleshoot allocation failures when you create or resize VMs in Azure](/en-us/troubleshoot/azure/virtual-machines/windows/allocation-failure).

When Microsoft detects capacity constraints that could affect your workloads, you are alerted through [Azure Service Health](https://azure.microsoft.com/get-started/azure-portal/service-health) with details about the issue, potential alternatives, and expected timelines for resolution. Alerts are only triggered for actual allocation failures. Service Health alerts are just one signal; they don't guarantee that a specific allocation request will succeed.

When you see these errors, start by asking: Is the failure limited to one zone, all zones in a region, one SKU family, a managed-service dependency, or the subscription itself? A thorough analysis should lead you to the next move: a quota request, a region or zone access request, a different deployment shape, or an architectural change. The following sections focus on the architectural strategies that can prevent these failures.

## Adopt a shared responsibility model

Cloud hyperscalers continually expand infrastructure and provide capabilities that improve resource allocation and deployment success. However, capacity management is best treated as a shared responsibility between the cloud provider and its customers.

Microsoft is responsible for expanding and maintaining regional infrastructure to support customer demands. It also uses capacity-management controls to reduce noisy-neighbor effects. For example, Azure can detect demand spikes and apply resource controls that help prevent a single resource's sudden increase in usage from affecting shared capacity.

As part of your responsibility, design your workload to judiciously use what's available. You're responsible for forecasting your capacity, designing flexible architectures, and reserving or requesting capacity before you need it. For capacity planning strategies, see [Make capacity planning an ongoing operational practice](#make-capacity-planning-an-ongoing-operational-practice).

Availability is also point-in-time and request-specific. Releasing resources or changing deployment constraints can change the outcome of a subsequent allocation request, even when the request uses the same region, zone, and service or VM family.

## Make capacity planning an ongoing operational practice

Start capacity planning with questions like *"How do we recover?"* to *"What capacity will we need next month, next quarter, or during our next growth event, and what will it cost if we forecast it early rather than wait until we need it?"*

Capacity planning must be a continuous operational discipline. Estimate the CPU, memory, storage, and network bandwidth needed to support current and anticipated demand. Apart from independent raw metrics from resources, also express capacity requirements for scale units and deployment stamps that include all resources in the unit.

Plan with sufficient lead time for the slowest dependencies. Factor in time for obtaining region access, enabling availability zones, and setting up capacity reservations.

This factor is also a cost decision. Use those demand forecasts to guide reservations and savings plans, so you can lock in capacity and pricing before a constrained peak forces premium pay-as-you-go rates. Be aware that cost can vary by region.

For key strategies, see [PE:02: Architecture strategies for capacity planning](../performance-efficiency/capacity-planning).

### Plan and forecast demand

- Build demand forecasts by using production telemetry, historical growth trends, and planned onboarding activities. Include temporary demand from upgrades, replacements, and failover. For example, AKS and VMSS surge operations create extra instances and consume quota and capacity while the operation is in progress.
- Track capacity requirements by service or SKU family, region, availability zone, and dependent services.

### Place workloads and secure capacity

- Start capacity planning early and refine forecasts throughout the planning phase. Finalize capacity before activation and allow time for quota requests, region access approvals, and capacity reservations. Apply reservations and savings plans as soon as practical after resources are created, track commitment coverage to avoid overpurchasing, and coordinate with operations teams to avoid surprises when workloads are offboarded.
- Preserve subscriptions that already have access to restricted regions or specialized SKUs instead of deleting and recreating them. Consider using [Azure Quota Groups](/en-us/azure/quotas/quota-groups) that allow you to self-manage and share quota among a group of subscriptions. For example, use quota groups to reclaim unused quota from a subscription and keep the cores in a private quota pool for use by another subscription.
**Risk**: Requesting new access to constrained regions adds more competition for the same finite capacity. Preserve existing access and share it instead of requesting new access.

### Optimize, govern, and automate

- Ensure your subscriptions have quota and access policies configured in advance of production deployment.
- Configure quota alerts at meaningful utilization thresholds, such as 70%, 85%, and 95%, to identify potential issues before they affect deployments.
- Treat allocation failures as operational signals that indicate emerging capacity pressure, rather than isolated deployment anomalies. Observe trends in allocation failures to act early when a workload or region is approaching its capacity limits.

Start capacity planning at the individual workload level, then expand it across business units and workload portfolios as your cloud adoption grows.

## Prioritize multi-region design over single-region deployments

Treat Azure as a global platform with multiple regional capacity pools. Each region has a carrying capacity based on available space, power, cooling, and other factors, which defines how much it can absorb. Deployment approaches such as single-region, paired-region passive (where available), or two-region active-active are still valid, but they might not be sufficient when it comes to building capacity resilience. A multi-region design gives your workload more flexibility by giving it access to extra capacity pools and deployment locations.

The right number of regions depends on your workload requirements and operating model:

- **Single-region** can be appropriate for workloads with modest growth requirements, low availability needs, strict data residency requirements that only a single Azure region can meet, or a strong preference for operational simplicity. Confirm that the region and services you select can support anticipated growth and recovery requirements. It provides no regional fallback, so choose it deliberately when the workload requirements and operating model support that constraint.
- **Two regions** provide an extra capacity pool and can support active-passive or active-active designs. This design can be appropriate for noncritical or lightly distributed workloads that need regional failover but can tolerate the risk that both regions experience capacity pressure at the same time.
- **Three or more regions** provides stronger protection. This approach can be appropriate for larger or business-critical workloads. When one region is constrained, two others remain available for capacity and failover. If one region experiences capacity pressure, the other two remain available to support capacity needs and failover. For most medium-scale organizations, consider this as the baseline strategy. Evaluate the benefits against business requirements like data residency, operational complexity, cost, and others.
You can expand even more. Four or more regions are recommended for large enterprises. It maximizes capacity, geographic proximity to users, and resilience against regional outages or constraints.

Start with a multi-region approach. You don't need to deploy every application to every region. For example, App A can run active-active in regions 1 and 2 for high volume and low latency, App B in regions 2 and 3 for geographic diversity, and App C in regions 3 and 4 for a different user base. This distribution spreads load across regional capacity pools, which have different utilization profiles.

Select regions based on these factors:

- Reliability and recovery targets.
- Capacity and SKU availability for current and anticipated workload requirements.
- Tolerated latency between users, application components, data stores, and dependent services.
- Data residency, sovereignty, and compliance requirements.
- Availability of the Azure services, features, and zones that the workload requires.
- Performance characteristics, including cross-region replication and network egress.
- The cost and operational complexity of deploying, monitoring, securing, and recovering the workload across regions.

This table shows the common deployment patterns for a three-tier application. These numbers are illustrative and depend on workload architecture, dependencies, and recovery automation.

| Deployment pattern | Availability model | Example target availability |
| --- | --- | --- |
| Single zone | Protects against host or rack failure, but not zone loss or regional disruption | ~99.9% |
| Multi-zone | Protects against zone failure with redundant placement across zones | ~99.95% to 99.99% |
| Multi-region | Protects against zone and regional outage and capacity limitations, assuming failover automation and data replication | ~99.99% + |

> **Tradeoff**: A multi-region architecture improves resilience but it also introduces tradeoffs. Replicating data across regions can increase latency and data egress costs, while data residency and sovereignty requirements may restrict where data can be stored or replicated. Operating across multiple regions also increases architectural and operational complexity, requiring additional mechanisms for replication, failover, monitoring, and consistency management.
Adding a new region doesn't automatically require a full networking stack in that region. In many multi-region designs, you can use global connectivity, peering, and centralized shared services instead of duplicating a full hub-and-spoke deployment in every region.

Don't rely solely on a primary region and its Azure-paired region, if it has one. If the paired region experiences the same failure as the primary region, it might not have sufficient capacity to absorb failover demand. This condition can make it harder to meet availability and disaster recovery objectives. Paired regions work well for blob storage with GRS (Geo-Redundant Storage) because Microsoft handles replication, but they aren't suitable as the sole capacity strategy for compute workloads that you manage directly, such as VMs, AKS, and App Service.

For more information about regional availability strategies, see [Using Availability Zones and Regions](regions-availability-zones) and [Develop a disaster recovery plan for multi-region deployments](disaster-recovery).

## Design for zone flexibility

Consider a two-zone deployment strategy, where supported. Depending on the service, a two-zone deployment can meet availability targets without using every availability zone in a region. Confirm the applicable SLA for each service. Services such as Azure VMs and some eligible PaaS services (see [Azure services that support availability zones](/en-us/azure/reliability/availability-zones-service-support)) can run in a two-zone configuration while maintaining their documented SLA and availability guarantees. When a single availability zone experiences capacity degradation, a two-zone deployment can help maintain availability targets while improving deployment flexibility.

## Pre-provision capacity intentionally

A common reactive pattern is to provision infrastructure first and request quota only when needed. This approach assumes Azure can allocate capacity within minutes or hours, which might not hold when capacity is constrained. Forecast demand from expected growth, planned deployments, seasonal events, and other drivers, then:

- Reserve capacity for compute resources that are critical for your workload.
- Validate region and availability zone access, subscription quota, SKU availability, service dependencies, and recent deployment test results in your target locations. Identify fallback zones, regions, and alternative SKUs in advance. Because capacity is allocated only at deployment time, capacity reservations are suitable for workloads that require guaranteed VM capacity.
Do eligibility checks and identify unsupported GPU/HPC families, Spot VMs, availability sets, dedicated hosts, and other constraints.
- Classify workloads and flows by criticality. Workload components that are business-critical should be supported with pre-provisioned capacity. Other flows can use flexible architecture, reducing unnecessary capacity costs. For more information, see [Identify critical flows](optimize-workload-using-flows).
- Use a phased provisioning approach for large capacity requests. Instead of requesting all capacity at once, provision incrementally in stages (for example, 25% stages for a 2,000 vCPU request).

For workloads with predictable or business-critical capacity requirements, consider [Azure Capacity Reservations](/en-us/azure/virtual-machines/capacity-reservation-overview). This capability reserves VM compute capacity in a specific Azure region or availability zone. To create the reservation, you must have subscription quota and capacity available. If there's already an outage or capacity shortage, don't assume you can create a reservation at that moment to solve the problem. Plan in advance.

You can associate an existing zonal VM with a capacity reservation without redeploying or reallocating the VM. For example, if you deployed 100 zonal VMs in East US, Zone 1, and the workload later becomes business critical, you can attach them to capacity reservations to protect against capacity shortages during future changes.

For regional (nonzonal) VMs, you can still associate them with capacity reservations, but the VM must be deallocated and reallocated to the capacity reservation group. For more information, see [Associate an existing virtual machine](/en-us/azure/virtual-machines/capacity-reservation-associate-vm).

> **Tradeoff**: Capacity reservations involve a cost tradeoff. You pay for reserved capacity even when it isn't being used because Azure is holding those resources for your workload.
Reserve capacity where the cost of not having it is greater than the cost of keeping it idle. Evaluate factors such as the cost per tenant, cost per application stamp, and the business impact of specific scenarios. For example, consider the impact of delaying a large migration, missing a customer onboarding deadline, or being unable to scale a SaaS service.
For business-critical workloads, paying for reserved headroom is often less expensive than the operational and financial impact of capacity shortages.
Reserved Instances and Savings Plans optimize cost. Capacity Reservations secure capacity availability. These mechanisms can be combined, allowing organizations to reserve capacity while still benefiting from existing commitment discounts.

## Treat quota as a dynamic pool

Organizations often treat Azure subscriptions as permanent organizational boundaries. Instead, treat them as containers for acquiring and managing quota.

Use [Azure Quota Groups](/en-us/azure/quotas/quota-groups) to self-manage and share quota across subscriptions. They're particularly valuable for Enterprise Agreement (EA) customers, allowing approved quota to move across business units instead of remaining siloed in subscriptions with constrained limits.

Important

Quota Groups reallocate quota between member subscriptions; they don't guarantee physical capacity.

## Share reserved capacity

When teams or workloads manage reserved capacity independently, it can be underutilized while other business units have unmet deployment requirements. Disaster recovery (DR) capacity can also remain idle for long periods.

Manage reservations centrally and share them across business units, subscriptions, and workloads where needed. Consider using passive DR infrastructure to support analytics workloads, generating grounding data for AI, and performing other compute-intensive work that doesn't need to be done in real time. This approach also aligns with the Cost Optimization principle of [use what you pay for](../cost-optimization/principles#design-for-rate-optimization).

For more information, see [Share a Capacity Reservation Group](/en-us/azure/virtual-machines/capacity-reservation-group-share).

## Prefer fungible VM deployments

Design workloads to support multiple compatible VM SKUs instead of pinning to a single series. Consider using [Azure Compute Fleet](/en-us/azure/azure-compute-fleet/overview), a capacity orchestration service that abstracts SKU selection. You specify your compute capacity needs; Compute Fleet automatically selects the optimal combination of VM types, availability zones, and pricing. Keep in mind that quotas still apply per subscription, region, and VM family.

This infrastructure abstraction provides key benefits:

- Azure makes placement decisions, so you can focus on your functional and nonfunctional requirements.
- Higher deployment success rates by using available capacity pools.
- Potential cost optimization through mix and match of compatible VM families.
- Reduced operational overhead from SKU management. Instead of managing quotas for hundreds of individual VM series, adopt vCPU-based quota categories that support capacity-first deployment.

Example use cases for fungible deployments:

- **Web and application server scaling**: Use [Virtual Machine Scale Sets (VMSS)](../service-guides/virtual-machines) with flexible orchestration to deploy mixed VM types within a single scale set. Azure automatically distributes instances across SKUs and zones based on availability.
- **Containerized workloads**: Use [Azure Kubernetes Service (AKS)](../service-guides/azure-kubernetes-service) auto-provisioning to automatically provision nodes across multiple VM types and zones based on workload requirements, eliminating manual SKU pinning.

## Common antipatterns and alternatives

This section highlights common antipatterns to watch for and alternatives that can help you build more resilient, flexible deployments.

| **Antipattern** | **Risk** | **Recommended alternative** |
| --- | --- | --- |
| **Zone-pinned deployment** | Creates a dependency on a single availability zone, eliminating alternatives during outages or capacity shortages. | Remove unnecessary zone pinning, use zone-resilient deployments where possible, and keep alternate zone options ready for constrained events. |
| **Single-region deployment as the primary model** | Relies on a single regional capacity pool. Regional outages or capacity issues prevent deployments, scaling, and disaster recovery. | Adopt multi-region architecture as the default resilience boundary, targeting three regions as a baseline and four or more for large enterprises. |
| **Using only one SKU or instance type** | High-demand or specialized SKUs can become constrained, preventing deployment or scale-out even when alternatives exist. | Design fungible deployments across compatible SKUs and use services like Compute Fleet, flexible VMSS, or AKS auto-provisioning to avoid SKU lock-in. |
| **Reactive scaling without capacity planning** | Autoscaling might trigger successfully but fail to provision additional resources, resulting in degraded application performance or availability during peak demand. | Run ongoing capacity planning with forecasts, quota checks, and early requests; set quota alerts and finalize major capacity needs at least eight weeks before activation. |
| **Not anticipating allocation failures** | Scale-out or replacement operations can fail unexpectedly, causing performance degradation or availability impact when workloads rely on new instances. | Design for the possibility that new instances can't be allocated when needed because of capacity pressures. Use throttling, queues, retries, and degraded operation to continue serving requests when scale-out is delayed or fails. Verify that new instances are healthy and ready before directing traffic or depending on their capacity. |
| **Hoarding reserved capacity within teams** | Teams hold unused capacity while others are limited in their deployments. This fragmentation prevents optimal allocation. | Manage reservations centrally and share capacity reservation groups across subscriptions to improve utilization and response flexibility. |
| **Treating quota as immutable team boundaries** | Separate quotas per team or subscription create silos; dynamic pooling allows capacity to flow where needed most. | Treat quota as a dynamic pool by using Azure Quota Groups and reassigning quota based on changing workload demand. |
| **Delaying capacity reservations until critical** | Provisioning reservations only when workloads become business-critical misses opportunities for proactive planning and increases deployment risk during growth events. | Pre-provision capacity for critical workloads, use phased provisioning for large requests, and reserve headroom before growth events. |

## Related links

[PE:02: Architecture strategies for capacity planning](../performance-efficiency/capacity-planning)

## Feedback

Was this page helpful?

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

## Additional resources

- Last updated on 2026-09-09

---

> 原页面：https://learn.microsoft.com/en-us/azure/well-architected/design-guides/capacity-resilience（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
