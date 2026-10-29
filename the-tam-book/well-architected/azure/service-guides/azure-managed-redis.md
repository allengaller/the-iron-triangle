<!-- source: https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-managed-redis -->
<!-- captured: 2026-10-25 -->
<!-- vendor: azure -->

# Architecture best practices for Azure Managed Redis

Note




Azure Managed Redis (AMR) is a managed, in-memory data store built on the Redis Enterprise engine. It provides low-latency caching and data structures for high-throughput workloads, with high availability (HA), online scaling for highly available instances, and active geo-replication on supported SKUs. Multiple Redis shards use the available vCPUs in parallel to improve performance and scalability.

AMR also supports AI application patterns such as semantic caching and agent memory. Applications can use Redis data structures to store conversation state and use [vector search](/en-us/azure/redis/redis-modules#redisearch) to retrieve relevant context. Application code or libraries manage response reuse, memory retention, and retrieval. Choose a tier, SKU, and module configuration that supports your workload's capacity, performance, and feature requirements.

This article assumes that as an architect, you've reviewed your caching and in-memory data store options and chose Azure Managed Redis as the solution for your workload.

The guidance in this article provides architectural recommendations that are mapped to the principles of the [Well-Architected Framework pillars](/en-us/azure/well-architected/pillars).

**Technology scope**

This review focuses on the interrelated decisions for the following Azure resources:

- Azure Managed Redis

## Reliability

The purpose of the Reliability pillar is to provide continued functionality by **building enough resilience and the ability to recover fast from failures**.

[Reliability design principles](/en-us/azure/well-architected/reliability/principles) provide a high-level design strategy applied for individual components, system flows, and the system as a whole.

### Workload design checklist

Start your design strategy based on the [design review checklist for Reliability](../reliability/checklist). Determine its relevance to your business requirements while keeping in mind the nature of your application and the criticality of its components. Extend the strategy to include more approaches as needed.

- **Account for service constraints:** Review service limits, quotas, large SKU availability, and immutable settings before selecting a tier, SKU, and clustering policy. Choose the clustering policy based on client compatibility, throughput, and module requirements.
OSS clustering is the default and recommended option for higher performance. OSS clustering doesn't support RediSearch, use Enterprise clustering when RediSearch is required. Select [Redis modules](/en-us/azure/redis/redis-modules) at creation. OSS and Enterprise clustering policies can't be changed in place, although eligible non-clustered instances can change to a clustered policy. See [clustering policy restrictions](/en-us/azure/redis/how-to-scale#can-the-clustering-policy-be-changed-after-selecting-oss-or-enterprise-cluster). Use a blue-green deployment when an immutable setting must be changed.
- **Anticipate potential failures through failure mode analysis:** Identify cache failures and define a mitigation for each one.
Failure
Mitigation
Single node or shard failure
Verify that clients reconnect after automatic failover.
Availability-zone outage
Use a zone-redundant deployment.
Regional outage
Redirect clients to a healthy geo-replicated instance.
Client-side connection exhaustion or timeouts
Use connection pooling, keep client VMs appropriately sized, and implement circuit breakers.
Memory pressure causing evictions
Set an eviction policy aligned to the workload and scale before capacity is exhausted.
- **Align reliability targets with the service SLA:** Review the current [Azure Managed Redis SLA requirements](/en-us/azure/reliability/reliability-managed-redis#service-level-agreement) and the [SLAs for online services](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services). Eligibility depends on topology and applicable terms, and the connectivity SLA doesn't guarantee data durability.
Define workload service level objectives (SLOs) from business needs, then validate that the complete architecture can meet them. Include dependencies such as the client tier, Microsoft Entra ID, Private Link, DNS, and the system of record.
Define recovery time objectives (RTOs) and recovery point objectives (RPOs) for each recovery path. Intra-region failover occurs automatically, whereas cross-region recovery requires failure detection and client redirection, and it must account for replication lag. Persistence rehydration and manual recovery processes, such as export and import operations, can introduce additional delays and should be factored into recovery planning.
Document whether each environment uses a single-zone, zone-redundant, or geo-replicated deployment model so that stakeholders clearly understand the associated availability and recovery expectations.
- **Use built-in redundancy features:** With high availability enabled, Azure Managed Redis provides primary and replica shards, self-healing, traffic routing, and automatic failover. Deploy in a region with availability-zone support to obtain zone redundancy. Replication is asynchronous, so recent writes can be lost during a failure. See [reliability in Azure Managed Redis](/en-us/azure/reliability/reliability-managed-redis).
Use [active geo-replication](/en-us/azure/redis/how-to-active-geo-replication) to improve resilience across regions. It requires HA and matching instance configurations. B0, B1, and Flash Optimized SKUs are excluded; supported modules are limited to RedisJSON and RediSearch. Configure each application deployment to connect to its local cache endpoint to reduce latency. Because geo-replication uses conflict-free replicated data types (CRDTs) and provides eventually consistent replication in active-active topologies, design applications to tolerate replication lag and concurrent write scenarios.
Match redundancy to reliability requirements. Account for the cost of HA and each geo-replicated instance. Zone redundancy follows the HA configuration in supported regions; it isn't a separately selected set of additional cache nodes. For geo-replication, also consider eventual consistency and the current bandwidth billing policy.
- **Plan for reliable scaling under variable load:** Initiate scaling through the portal, an API, or workload automation. HA instances remain available during scaling, but clients can experience transient connection failures. Non-HA instances become unavailable and lose their data during scaling. See [scaling behavior](/en-us/azure/redis/how-to-scale).
Plan ahead to minimize disruptions. Scale before resource limits are reached, preferably during low-traffic periods. Check the supported target SKUs for the current instance before requesting a change. A smaller target also requires sufficient usable memory and a compatible shard configuration. Maintain headroom based on measured peak load, scaling time, and failure scenarios. Ensure clients can retry transient failures and refresh cluster topology information after scaling.
Consider a deployment-stamp pattern that assigns a separate cache to each stamp or tenant group. As demand grows, add deployment stamps instead of continually scaling a shared cache to keep scaling predictable and reduce the failure blast radius.
Coordinate scaling activities with dependent services. Verify client reconnection, latency, and the cache-hit ratio after scaling. If data must be reloaded, limit cache-fill concurrency so the backing store can handle the additional reads.
Scaling instances in an active geo-replication group is in preview and shouldn't be used in production workloads. Geo-replicated instances can't scale down to a smaller memory size or shard count.
- **Configure reliability monitoring and alerting:** Measure availability, successful requests, errors, and latency percentiles in the application. Use synthetic canary probes to measure end-to-end availability against the workload's SLOs. Combine these signals with Azure Service Health and the documented [Azure Managed Redis metrics](/en-us/azure/redis/monitor-cache-reference), including Geo Replication Healthy for geo-replicated deployments.
Configure multi-window alerts for conditions that threaten the SLO or consume the error budget, such as sustained connection failures, increased application latency, and unhealthy geo-replication. Geo Replication Healthy reports health, not a measured replication delay. Use application-level checks when data freshness is a service level indicator (SLI). Correlate these signals with Microsoft Entra ID, Private Link, DNS, the client tier, and the system of record to identify the affected dependency and recovery path.
- **Build self-preservation into the application:** Design the application to tolerate cache unavailability. For data that can be rebuilt from a system of record, use cache-aside with a tested fallback path. Limit fallback requests to the backing store's capacity. [Prevent cache stampedes](https://redis.io/docs/latest/develop/use-cases/cache-aside/) when popular keys expire. When business requirements allow, serve stale or default data so a cache disruption degrades performance instead of causing an outage. For session state, messages, or agent state that can't be recreated, define an explicit recovery or failure behavior.
Configure connection and command timeouts separately, and use circuit breakers during sustained disruption. Retry transient errors with bounded exponential backoff and jitter, and refresh the cluster topology after failover. Design operations to be idempotent so retries don't cause duplicate effects. See [connection resilience](/en-us/azure/redis/best-practices-connection). Limit the failure scope by using zone redundancy, circuit breakers, bulkheads and deployment stamps.
- **Plan disaster recovery and backup:** Within a region, replica shards and optional persistence provide different recovery paths. Redis Database (RDB) provides periodic snapshots, whereas append-only file (AOF) records writes more frequently. [Persistence](/en-us/azure/redis/how-to-persistence) requires HA and can't be used with active geo-replication. Persistence supports recovery to the same instance but isn't a retained backup and can preserve corrupted or unintended data changes.
Use [export](/en-us/azure/redis/how-to-import-export-data) to create snapshots in Azure Blob Storage and import to restore them. Automate exports because Azure Managed Redis doesn't provide a built-in backup schedule. Store snapshots in versioned, geo-redundant storage, apply lifecycle policies that meet retention requirements, and regularly verify that exports can be restored. Import replaces existing data and makes the target unavailable; use a separate instance for recovery tests. Storage accounts that use firewalls or Azure Private Link [aren't supported for import or export](/en-us/azure/redis/how-to-import-export-data#import-export-faq#are-storage-accounts-that-enable-firewalls-or-private-links-supported). Validate Blob Storage permissions and network access for the export process.
For regional recovery, use CRDT-based active geo-replication to support active-active replication across regions, enabling lower RPOs and faster recovery for regional failures.
For an application that uses an active-passive regional design, direct application traffic to one region while keeping another instance in the active geo-replication group. The Redis replication topology remains active-active. During a regional outage, redirect the application to a healthy endpoint. Alternatively, restore exports in another region when the recovery objectives permit.
Regularly test failover, failback, geo-replication resynchronization, and export-and-import recovery procedures in non-production environments. Measure RTO, RPO, and client behavior during recovery events. Document the procedures in runbooks and repeat testing after significant architectural or configuration changes.
Don't use Azure Managed Redis as the authoritative system of record. Keep authoritative data and data that can't be reconstructed in a persistent data store when data loss is unacceptable.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| Enable [high availability](/en-us/azure/reliability/reliability-managed-redis#resilience-to-availability-zone-failures) and deploy in a region that supports availability zones. | Maintains cache availability during zone failures through replica shards and automatic failover. |
| Configure [active geo-replication](/en-us/azure/redis/how-to-active-geo-replication) on compatible instances when regional recovery is required. Configure local endpoints and test client redirection. | Maintains access to cached data during a regional outage by redirecting traffic to a healthy regional instance. |
| Select RDB or AOF [persistence](/en-us/azure/redis/how-to-persistence) when local data recovery is required. Persistence requires HA and can't be combined with active geo-replication. Choose the persistence mode against the workload's recovery and performance requirements. | Recovers data to the same instance after a failure. The selected mode balances recovery-point requirements against performance overhead. |
| Schedule [exports](/en-us/azure/redis/how-to-import-export-data) to Blob Storage and test imports into a separate recovery instance. | Provides retained recovery copies for restoring data after corruption or unintended changes. A separate instance enables recovery testing without risking production data. |
| Configure [connection and command timeouts](/en-us/azure/redis/best-practices-connection) separately. Use bounded retries with backoff and jitter. | Improves recovery from transient faults while preventing retry storms and keeping operations within the request time budget. |
| Configure application availability probes, [Service Health alerts](/en-us/azure/service-health/alerts-activity-log-service-notifications-portal), and alerts when [Geo Replication Healthy](/en-us/azure/redis/monitor-cache-reference) is 0. | Shortens the time to detect and respond to application, service, and geo-replication failures. |

## Security

The purpose of the Security pillar is to provide **confidentiality, integrity, and availability** guarantees to the workload.

The [Security design principles](/en-us/azure/well-architected/security/principles) provide a high-level design strategy for achieving those goals by applying approaches to the technical design of Azure Managed Redis.

### Workload design checklist

Start your design strategy based on the [design review checklist for Security](../security/checklist) and identify vulnerabilities and controls to improve the security posture. Extend the strategy to include more approaches as needed.

- **Restrict network access:** Use a [private endpoint and private DNS](/en-us/azure/redis/private-link), and explicitly disable public network access so cache traffic uses Azure Private Link. Connect by the service hostname and verify that it resolves to a private IP address from each client environment. Apply network security groups and routes to the appropriate subnets. Enable private-endpoint network policies where these controls must apply to the endpoint. Don't assume that creating a private endpoint also disables public access.
- **Configure identity and access management:** Use Azure RBAC for control-plane operations such as provisioning, scaling, network configuration, key management, and role assignment. Use [Microsoft Entra ID authentication](/en-us/azure/redis/entra-for-authentication) over TLS for data-plane access. Add only required users or service principals; Microsoft Entra groups aren't supported. Clients must refresh tokens and reauthenticate before expiry.
Apply Conditional Access and Privileged Identity Management to supported administrative identities. [Conditional Access for workload identities](/en-us/entra/identity/conditional-access/workload-identity) doesn't cover managed identities. Restrict privileged operations, including scaling, key regeneration, network changes, customer-managed key configuration, and role assignments to a small platform or security group. Require approvals and Privileged Identity Management elevation, audit changes through the Azure Activity Log, and tightly control break-glass access keys.
Each user or service principal that you add receives broad access to all Redis commands and keys. For finer-grained data-plane authorization, evaluate [custom Redis ACL permissions](/en-us/azure/redis/configure-access-permissions). This feature is in preview and has other constraints. If these constraints prevent the required command or key isolation, use separate instances.
- **Protect data and securely manage secrets:** Classify cached data, such as session data, tokens, personal data, and vector embeddings. Azure Managed Redis doesn't provide confidential computing memory encryption for data in use. Minimize sensitive cached data, use short expiration times, and consider another service if confidential computing is required.
Keep non-TLS access disabled and enforce certificate validation. The platform manages the cache endpoint certificate. AMR encrypts supported disks with Microsoft-managed keys by default. When required, configure [customer-managed keys](/en-us/azure/redis/how-to-encryption) (CMK) for supported disk encryption. CMK doesn't cover the Flash Optimized ephemeral NVMe disk, and the destination storage account controls encryption of exported blobs.
Retrieve tokens at runtime through managed identities. Never embed credentials in code, configuration, or container images. Store access keys and connection strings in Azure Key Vault. To rotate keys without downtime, regenerate the secondary key, move clients from the primary to the secondary, and then regenerate the primary.
- **Monitor security events:** Collect [ConnectionEvents logs](/en-us/azure/redis/monitor-diagnostic-settings), Azure Activity Logs, and relevant Microsoft Entra sign-in logs in the workload's central security monitoring platform. ConnectionEvents includes connection and authentication events; it doesn't provide an audit of every Redis command.
Alert on authentication failures, unusual connection sources or connection spikes, access-policy changes, key regeneration, privileged control-plane operations, and changes to network or customer-managed key configurations. Correlate these events with application logs, network flow logs, and Microsoft Entra sign-in events to investigate activity across identity, network, control-plane, and data-plane boundaries.
Use Microsoft Defender for Cloud for applicable security-posture assessments and Microsoft Sentinel for correlation, threat hunting, and response workflows. Verify which assessments apply to the deployed resource types. Route alerts through Azure Monitor action groups and security operations workflows that define severity, ownership, escalation, and response procedures. Extend the shared observability platform with security-specific queries and alerts instead of creating a separate monitoring system.
- **Validate security controls:** Microsoft manages the operating system and Redis Enterprise engine, so focus vulnerability testing on the application, client libraries, infrastructure configuration, identity, and network boundary. Add integration tests that verify public access is disabled, private DNS resolves correctly, Microsoft Entra authentication and token refresh work, non-TLS access is disabled, diagnostics are enabled, and customer-managed keys are configured where required.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| Use [Microsoft Entra ID authentication](/en-us/azure/redis/entra-for-authentication) with a managed identity. | Supports long-lived connections without storing a static cache credential and reduces credential leak risk. |
| Disable [access key authentication](/en-us/azure/redis/secure-azure-managed-redis#identity-and-access-management) after all clients use Microsoft Entra ID. Plan for connection resets when changing this setting. | Removing key authentication reduces exposure from leaked credentials. Planned reconnection limits the effect of the configuration change. |
| Create a [private endpoint](/en-us/azure/redis/private-link), configure private DNS, and set `publicNetworkAccess` to `Disabled`. | Reduces exposure to threats by limiting cache access to private network paths. |
| Keep non-TLS access disabled and use clients that validate the server certificate. Use TLS 1.2 or 1.3. See [AMR security guidance](/en-us/azure/redis/secure-azure-managed-redis#data-protection). | TLS protects data in transit and certificate validation helps confirm the server's identity. |
| Scope Azure RBAC to required management operations. For data-plane access, add only required principals and configure [custom Redis ACL permissions](/en-us/azure/redis/configure-access-permissions) when preview use and module limitations are acceptable. | Separates management permissions from Redis command and key authorization. Separate instances provide the best isolation boundary. |
| Configure [customer-managed keys](/en-us/azure/redis/how-to-encryption) at creation when required. Use a user-assigned managed identity and Key Vault with soft delete and purge protection. Flash NVMe data and exported blobs have separate encryption coverage. | The organization controls the lifecycle of keys that protects supported disks. |
| Enable [ConnectionEvents](/en-us/azure/redis/monitor-diagnostic-settings) diagnostics and collect Azure Activity Logs and relevant Microsoft Entra sign-in logs. | Improves threat detection and incident investigation by correlating connection and authentication events with changes to the resource and identity configuration. |

## Cost Optimization

Cost Optimization focuses on **detecting spend patterns, prioritizing investments in critical areas, and optimizing in others** to meet the organization's budget while meeting business requirements.

The [Cost Optimization design principles](/en-us/azure/well-architected/cost-optimization/principles) provide a high-level design strategy for achieving those goals and making tradeoffs as necessary in the technical design related to Azure Managed Redis and its environment.

### Workload design checklist

Start your design strategy based on the [design review checklist for Cost Optimization](../cost-optimization/checklist) for investments. Fine-tune the design to align the workload with the allocated budget. Your design should use the right Azure capabilities, monitor investments, and find opportunities to optimize over time.

- **Create and maintain a cost model:** Azure Managed Redis uses capacity-based pricing, so the selected tier, SKU, and availability configuration are primary cost drivers. Use pay-as-you-go pricing for short-lived or variable workloads, and evaluate [reservations](/en-us/azure/redis/reserved-pricing) for predictable, eligible compute usage. Check availability for the selected tier and region.
Include secondary costs such as Log Analytics ingestion and retention, Private Link, export storage, idle non-production instances, overprovisioned capacity, and additional geo-replicated instances. Check the [current geo-replication bandwidth policy](/en-us/azure/redis/how-to-active-geo-replication) that indicates replication transfer charges are absorbed by the service. Model other network charges separately and recheck this policy when costs are reviewed.
Use the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) and the workload's usage data to compare peak-demand and steady-state scenarios. Re-evaluate reservation coverage and utilization as demand becomes more predictable.
Avoid unnecessary costs by decommissioning unused resources. When migrating from a legacy service, decommission the legacy instance after the migration is successfully completed and validated.
- **Control cost with governance:** Organize resources by using consistent tags so every cache maps to an owner, environment, and cost center. Make application teams accountable for right-sizing their caches, while platform teams own reserved capacity planning and optimization. Use Microsoft Cost Management dashboards, forecasts, scheduled exports, and reserved capacity utilization reports to support chargeback and cost transparency.
Enable anomaly detection and implement scoped budget alerts for unexpected instances, SKU changes, and billed network-usage spikes. Use Azure Policy to enforce tags and restrict allowed SKUs and regions. Require approval for large or preview SKUs, geo-replication, and other changes that increase cost.
- **Optimize environment costs:** For development and test environments, reduce cost by using [non-high availability mode](/en-us/azure/redis/best-practices-development#choose-an-appropriate-availability-mode). Use this configuration only when an SLA isn't required. Consider creating ephemeral development and test caches on demand, and automate their teardown after use or during off-hours.
Use HA for production and add geo-replicated instances when regional recovery requirements justify them. Reduce diagnostic log retention periods where appropriate, but keep security controls such as TLS, private networking, and Microsoft Entra authentication consistent across environments.
- **Reduce cost through automation:** Use source-controlled pipelines or runbooks to automate environment provisioning and teardown, exports, and cleanup of associated private endpoints, DNS records, and diagnostic settings. Azure Automation and Azure Functions can be used to orchestrate scheduled operational tasks.
Identify right-sizing opportunities by monitoring Server Load, and Used Memory Percentage in Azure Monitor. Generate recommendations for human review before production changes. Validate that the target SKU is supported for the current instance; otherwise, plan a migration to a new instance.
Use insights from Azure Advisor and Microsoft Cost Management to support capacity planning and right-sizing decisions. Compare automation runtime and maintenance effort with the recurring savings before investing in custom workflows.
- **Consolidate where appropriate:** A single Azure Managed Redis instance can support compatible workloads through application-defined key prefixes. AMR supports one database per instance. Prefixes organize data but don't provide an authorization boundary. Use separate instances when command or key isolation can't be enforced with the supported data-access configuration. Consolidation can cut cost by increasing utilization and reducing the number of billed instances and private endpoints.
Compatible functions, such as caching, vector storage, and session storage, can also be consolidated within a shared instance when requirements allow. Size shared instances based on the combined memory, connection, bandwidth, throughput, and compute requirements of all participating workloads. Use separate instances when workloads require strong isolation, independent lifecycle management, predictable latency, or compliance boundaries.
Establish clear ownership and coordinate changes to the shared resource. Collect application-level usage metrics to allocate usage and costs accurately. Balance the savings from consolidation against noisy-neighbor effects, a larger failure scope, more complex operations, and the difficulty of allocating shared costs.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| Select a [tier and SKU](/en-us/azure/redis/overview#choosing-the-right-tier) based on your memory, compute, bandwidth, and feature needs. | Matching capacity to the workload limits unused resources while maintaining the required performance and capabilities. |
| Evaluate [one-year or three-year reservations](/en-us/azure/redis/reserved-pricing) for stable, eligible compute usage. Check tier and region availability. | Reservations can reduce the cost of predictable usage. Monitoring coverage and utilization helps avoid unused commitments. |
| Create disposable development and test instances without HA only when data loss and downtime are acceptable. See [availability-mode guidance](/en-us/azure/redis/best-practices-development#choose-an-appropriate-availability-mode). | Reduces environment costs for non-production workloads but doesn't provide production resilience. |
| Set workload-appropriate key expiration and [eviction policies](/en-us/azure/redis/best-practices-memory-management). Eviction must remain compatible with the workload and selected modules. Remove unused data and indexes. | A smaller working dataset can delay the need for a larger expensive SKU. |
| Configure owner and environment tags, budgets, and cost alerts. See [Cost Management](/en-us/azure/cost-management-billing/costs/overview-cost-management). Automate cleanup of disposable instances and their dependent resources. | Teams can identify unused capacity and unexpected spend. Removing resources after use prevents avoidable recurring charges. |

## Operational Excellence

Operational Excellence primarily focuses on procedures for **development practices, observability, and release management**.

The [Operational Excellence design principles](/en-us/azure/well-architected/operational-excellence/principles) provide a high-level design strategy for achieving those goals for the operational requirements of the workload.

### Workload design checklist

Start your design strategy based on the [design review checklist for Operational Excellence](../operational-excellence/checklist) for defining processes for observability, testing, and deployment related to Azure Managed Redis.

- **Automate routine operations:** Automate provisioning, scaling responses, configuration drift remediation, monitoring configuration, scheduled exports, role assignments, and credential rotation.
Use native Azure Managed Redis capabilities such as automatic failover, self-healing, online scaling, patching, data persistence, export, and active geo-replication rather than duplicating them with custom automation. Integrate them into pipelines, and enforce approved configurations with Azure Policy and drift detection.
- **Deploy changes safely:** Deploy infrastructure as code (IaC) changes progressively through deployment rings with health gates and validation. Use Bicep, ARM templates, or Terraform to deploy the `Microsoft.Cache/redisEnterprise` resource, its `databases/default` child resource, Private Link, and supporting infrastructure. Pin supported API or provider versions and verify that they expose the required settings. Review Azure Resource Manager what-if or terraform plan output before deployment.
Use reusable, parameterized modules and environment-specific parameter files to deploy caches and supporting resources consistently while varying capacity and optional features without weakening security controls.
Schedule changes with deployment pipelines, enforce validation, security, and health gates, publish resource outputs for downstream stages, and verify deployment health before increasing traffic.
Promote the deployment only when server load, memory use, connection errors, and client timeouts remain within defined thresholds. Define a tested recovery path for each change. An earlier IaC version can restore reversible settings, but it can't undo data loss or guarantee that a SKU, clustering, or HA change can be reversed.
- **Standardize observability:** Configure diagnostics through IaC. Use Azure Monitor and Log Analytics with the built-in [Dashboards with Grafana](/en-us/azure/redis/grafana-dashboards) experience for shared reliability, performance, and security views. This portal experience is separate from the Azure Managed Grafana service.
Automate alerts for server load, memory utilization, client connections, and bandwidth, along with dashboards, action groups, and scaling notifications. Configure ConnectionEvents on the `databases/default` resource of every instance, including each geo-replica. Send logs to Log Analytics, Event Hubs, or Storage, and set retention for the selected destination. See [diagnostic settings](/en-us/azure/redis/monitor-diagnostic-settings).
Use [Redis Insight](https://redis.io/docs/latest/develop/tools/insight/) and supported Redis commands such as `SLOWLOG`, `INFO`, and `LATENCY` for detailed data-plane investigations. Redis Insight supports Microsoft Entra authentication for Azure Managed Redis. Configure the required Azure permissions and network access before connecting.
Correlate cache telemetry with dependency health signals to determine whether incidents originate from Azure Managed Redis or another component in the application stack.
- **Prepare for incidents:** Plan for partial failures, including shard or node failover, Microsoft Entra token-acquisition failures, and DNS or Private Link disruptions.
Detect failures by correlating service metrics, ConnectionEvents, client-side errors and timeouts, application health probes, and Azure Service Health alerts.
Design an operational readiness process around the documented [force-unlink guidance](/en-us/azure/redis/how-to-active-geo-replication#force-unlink-if-theres-a-region-outage). While an unavailable instance remains linked, healthy instances accumulate metadata for writes that can't be synchronized. Monitor available memory and define a threshold for force-unlinking the unavailable instance before the metadata exhausts capacity. After a regional failure, verify replication health and application behavior before returning traffic.
- **Continuously validate operations:** Run connectivity, authentication, command, integration, and configuration-compliance tests in CI. Exercise recovery runbooks regularly in non-production. Use `redis-benchmark` or `memtier_benchmark` for command-level load tests, Azure Load Testing for end-to-end scenarios, and Azure Policy for continuous configuration compliance.
Run low-volume synthetic canaries in production using an isolated keyspace or test instance. Promote changes only when all tests and security policies pass, the infrastructure plan contains no unintended changes, and health metrics remain within thresholds throughout the soak period.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| Deploy `Microsoft.Cache/redisEnterprise` and its `databases/default` resource through versioned infrastructure as code. See [configuration guidance](/en-us/azure/redis/configure). | Produces consistent, reviewable deployments and reduces configuration drift across environments. |
| Configure [ConnectionEvents diagnostics](/en-us/azure/redis/monitor-diagnostic-settings) on `databases/default` for each instance, including every geo-replica. | A consistent log destination and retention policy supports investigations across environments and regions. |
| Use the built-in [Dashboards with Grafana](/en-us/azure/redis/grafana-dashboards) experience and configure shared alerts and action groups. | Teams get a common operational view without deploying a separate Azure Managed Grafana instance. |
| Add DNS, TLS, authentication, and representative Redis command checks to deployment health gates. Include [token refresh](/en-us/azure/redis/entra-for-authentication) in longer tests. | Detects configuration and connectivity issues early in the deployment process. |
| Configure and test runbooks for regional redirection, export recovery, and [force-unlink recovery](/en-us/azure/redis/how-to-active-geo-replication#force-unlink-if-theres-a-region-outage). | Provides tested steps for failure detection, recovery, and return to normal service, including cases that need instance recreation. |
| Review each proposed [scaling operation](/en-us/azure/redis/how-to-scale) and define a tested recovery path for changes that can't be reversed in place. | Reduces the risk of disruption by accounting for service constraints and data changes which can't be reversed through infrastructure redeployment. |

## Performance Efficiency

Performance Efficiency is about **maintaining user experience even when there's an increase in load** by managing capacity. The strategy includes scaling resources, identifying and optimizing potential bottlenecks, and optimizing for peak performance.

The [Performance Efficiency design principles](/en-us/azure/well-architected/performance-efficiency/principles) provide a high-level design strategy for achieving those capacity goals against the expected usage.

### Workload design checklist

Start your design strategy based on the [design review checklist for Performance Efficiency](../performance-efficiency/checklist). Define a baseline that's based on key performance indicators for Azure Managed Redis.

- **Plan for capacity:** Establish a baseline by running a representative load against a candidate SKU. Set operating limits below the point where latency or errors rise sharply, and leave capacity for growth, maintenance, and failure scenarios.
Evaluate memory, connection, and network limits for each candidate SKU. Include key and index overhead, fragmentation, persistence overhead where enabled, and growth. Distinguish application headroom from the service's reserved memory. [Used Memory Percentage](/en-us/azure/redis/best-practices-memory-management) accounts for the SKU limit and HA replication; don't double the SKU size just to account for the replica. For active geo-replication, also allow for CRDT metadata, disconnected-region backlog, and redirected application traffic. Validate these needs with representative tests instead of treating a fixed multiplier as a capacity guarantee.
To assess performance dependencies, include the client application, connection pool, virtual network, Private Link, DNS, Microsoft Entra ID, and storage used for persistence or export operations when those features are enabled. Check for common application bottlenecks such as connection storms, excessive round trips, and undersized client virtual machines.
- **Choose the right tier, SKU and scaling strategy:** Select a tier based on the memory-to-vCPU ratio and required features. The in-memory tiers have similar capabilities, but [Flash Optimized has feature restrictions](/en-us/azure/redis/overview#feature-comparison), including no active geo-replication or RediSearch. Review the current preview status of large SKUs before selecting them for production.
Multiple Redis shards can execute work across vCPUs. More vCPUs can improve aggregate throughput when the workload can use them; they don't remove a hot-key or long-running-command bottleneck. Consider Compute Optimized for compute-bound workloads and Memory Optimized for workloads that need more memory relative to compute. Evaluate Flash Optimized for a large dataset with a smaller frequently accessed working set, and test it with realistic occupancy and access patterns.
With the OSS clustering policy, use a cluster-aware client and distribute keys across hash slots. The service manages shard and node counts as part of the SKU; selecting a cluster-aware client doesn't enable automatic horizontal scaling. Co-locate keys with hash tags only when multi-key operations require it.
- **Monitor performance and capacity:** Continuously monitor CPU, Server Load, Used Memory Percentage, Connected Clients, and Operations Per Second. For workloads with a caching use case, also monitor Cache Read and Cache Write bandwidth, the hit ratio calculated from Cache Hits and Cache Misses, evicted and expired keys, and application latency percentiles. The platform Cache Latency metric is an average, not p95 or p99.
Continuously evaluate capacity trends and alert before measured operating limits are reached. Investigate sustained Server Load, high memory use, connections approaching the SKU limit, bandwidth saturation, rising application latency, and unexpected evictions or misses. Use thresholds established during load and recovery tests.
Instrument client applications to capture command latency, timeouts, retries, and connection-pool health. Correlate them with AMR metrics and client compute, Private Link, DNS, and token-acquisition latency to distinguish client, network, and cache bottlenecks.
- **Conduct performance testing:** Run a [load test](/en-us/azure/redis/best-practices-performance) and gradually ramp up to identify when CPU, Server Load, and latency rise sharply.
Model production conditions, including representative dataset and value sizes, key distribution, read and write mix, command set, pipeline depth, and connection counts at expected and peak concurrency. Match the production tier, SKU, clustering policy, TLS configuration, and Microsoft Entra authentication so tests include real network and encryption overhead.
Run load generators in the application region and through the production network path. Use enough client compute and bandwidth to avoid limiting the benchmark.
- **Tune configuration and optimize performance:** Select features according to the workload. Use more vCPUs for compute-bound workloads and consider OSS clustering for high throughput. [RediSearch requires Enterprise clustering and NoEviction](/en-us/azure/redis/redis-modules#redisearch). Enable optional features only when their benefits justify their resource use, and check compatibility. Keyspace notifications and persistence add overhead and should be enabled deliberately.
For reconstructable cached data, use cache-aside unless another consistency or update pattern is required. Read-through and write-behind behavior must be implemented by the application or a suitable integration. Set TTLs to control data retention and memory use. With `NoEviction`, plan explicit cleanup and capacity alerts because memory pressure can cause writes to fail.
Place the cache in the same region as the application and provide private connectivity from the application network. Azure Managed Redis isn't injected into that virtual network, and the service manages zone placement. For multiregion applications, consider active geo-replication on supported SKUs to provide local endpoints.
Reuse connections, tune connection pools, and use bounded pipelines to reduce round trips. Avoid large responses and long-running commands on request paths. Follow the clustering policy's multi-key restrictions. Microsoft handles patching and OS maintenance. Workload teams should manage capacity, TTL and eviction behavior, connection pools, client libraries, and timely scaling.

### Configuration recommendations

| Recommendation | Benefit |
| --- | --- |
| Use [OSS clustering](/en-us/azure/redis/architecture#cluster-policies) with a cluster-aware client when the command set permits it. Allow port 10000 and the discovered shard ports. | Direct shard connections can increase throughput. Correct client and network configuration prevents routing failures. |
| For [RediSearch](/en-us/azure/redis/redis-modules#redisearch), enable the module at creation and select Enterprise clustering with `NoEviction`. | Provides the required configuration for search and vector workloads. Capacity alerts and explicit data retention are important when automatic eviction is disabled. |
| Select additional compute for CPU-bound workloads and additional memory for dataset growth. Benchmark the candidate SKU with the actual request mix. See [performance testing](/en-us/azure/redis/best-practices-performance). | Independent compute and memory choices address the measured bottleneck and verify that the selected SKU meets workload performance targets. |
| Reuse [client connections](/en-us/azure/redis/best-practices-connection) and use bounded [pipelines](/en-us/azure/redis/best-practices-development#use-pipelining). | Connection reuse reduces setup overhead. Pipelining reduces round trips, while bounded batches control buffering and response delay. |
| Place the application and cache in the same region. Use the service hostname and configure private DNS resolution. See [development guidance](/en-us/azure/redis/best-practices-development). | Regional proximity reduces network latency and hostname-based connections remain valid when service IP addresses change. |
| Configure alerts by using thresholds based on load tests and recovery capacity requirements. See [metric definitions](/en-us/azure/redis/monitor-cache-reference). | Service metrics and client measurements expose different bottlenecks early enough to scale or remediate before users are significantly affected. |
| Use hash tags only for keys that must share a slot. Avoid broad scans, large responses, and long-running commands on request paths. See [AMR development guidance](/en-us/azure/redis/best-practices-development). | Balanced key distribution and bounded operations reduce hot shards and latency. |

## Tradeoffs

You might need to make design trade-offs when you use the approaches in the pillar checklists. The following sections highlight the advantages and drawbacks of key decisions.

**Flash Optimized tier for large datasets**

The Flash Optimized tier can reduce cost by moving less frequently used values to NVMe while keeping keys in RAM. Flash access can increase latency, and the tier restricts modules and geo-replication. Benchmark the expected dataset and access pattern. See [Flash Optimized architecture](/en-us/azure/redis/architecture#flash-optimized-tier).

**Memory Optimized tier**

The Memory Optimized tier is suitable for workloads that require high memory capacity relative to compute. It can reduce cost when the workload doesn't need the throughput of a tier with more vCPUs. Confirm latency and throughput under production load before selecting it.

**OSS clustering policy (vs. Enterprise/non-clustered)**

The OSS clustering policy is immutable after creation and allows for direct client connections to individual shards. It provides high throughput and low latency. However, it requires a cluster-aware client and can't be used with certain features like RediSearch.

**Enable data persistence on the cache**

Persistence can recover data to the same instance after a failure, subject to the latest persisted state. It requires HA and can't be combined with active geo-replication. RDB and AOF add resource overhead. Retained exports are still required when the workload needs recovery from deletion or corruption.

**Zone redundancy**

In a supported region, HA automatically distributes nodes across availability zones. The service determines node placement; three zones aren't guaranteed. HA costs more than non-HA and improves resilience, but applications still need capacity and retry behavior for a zone failure.

**Active geo-replication across regions**

With active-active CRDT replication, each region can accept writes and synchronize changes. This provides local access and regional recovery options, but requires additional instances, application failover logic, and tolerance of eventual consistency. Check the current replication bandwidth billing policy when estimating cost.

**Enforce TLS for all client connections**

Keep TLS enabled for client connections. Encryption and handshakes consume CPU, so reuse connections and include TLS in performance tests. If encryption overhead affects the workload, address connection behavior and capacity while preserving transport security.

**Customer-managed keys (CMK) for encryption at rest**

Customer-managed keys give you control over encryption keys for supported disks. It increases operational overhead with added key vault dependency and key-lifecycle management responsibilities. Configure CMK at creation where possible; switching an existing instance between Microsoft-managed and customer-managed keys can disrupt service. Flash NVMe data and exported blobs require separate consideration.

**Microsoft Entra ID auth with managed identity (vs. access keys)**

Microsoft Entra ID authentication with managed identity removes the need for long-lived application credentials. It requires token renewal and Redis reauthentication. Azure RBAC controls resource administration; Redis data access uses separate assignments. Managed identities aren't covered by Conditional Access, and the service's blocked commands apply independently of the authentication method.

**Private Link only (disable public endpoint)**

When you enable Private Link only and disable the public endpoint, all traffic to the cache is routed through the private endpoint, enhancing security by removing the public attack surface. However, it adds operational complexity as you need to manage private endpoints, private DNS, and virtual network connectivity for every consuming environment.

## Azure Advisor recommendations

Use [Azure Advisor](/en-us/azure/advisor/advisor-overview) to review personalized recommendations for Azure Managed Redis. Advisor analyzes resource configuration and usage telemetry and organizes applicable recommendations. Evaluate each recommendation against your workload requirements and architectural tradeoffs before implementation.

For more information, see [Advisor recommendations for Azure Managed Redis](/en-us/azure/redis/configure#advisor-recommendations).

## Example architecture

[Write-through caching with Azure Managed Redis and Azure SQL Database](/en-us/azure/architecture/databases/architecture/write-through-caching-azure-sql-managed-redis) demonstrates application-managed cache updates, private connectivity, managed identities, and recovery of failed cache updates.

## Related content

- [Azure Managed Redis architecture](/en-us/azure/redis/architecture)
- [Reliability in Azure Managed Redis](/en-us/azure/reliability/reliability-managed-redis)
- [Secure your Azure Managed Redis deployment](/en-us/azure/redis/secure-azure-managed-redis)
- [Azure Managed Redis configuration](/en-us/azure/redis/configure)
- [Performance testing with Azure Managed Redis](/en-us/azure/redis/best-practices-performance)
- [Azure Managed Redis monitoring data reference](/en-us/azure/redis/monitor-cache-reference)

## Feedback

Was this page helpful?

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

## Additional resources

- Last updated on 2026-10-01

---

> 原页面：https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-managed-redis（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
