<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel02-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSREL02-BP01 Build resilient and highly available research solutions

Design research systems using fault-isolated, redundant deployment
 patterns that allow continuous access during maintenance or
 localized outages. Use highly available configurations where
 near-zero downtime is required (for example, ELNs) and
 active-passive designs with automated failover for systems with less
 stringent latency or availability needs (for example, LIMS).

**Desired outcome:**

- Research systems remain available during maintenance or outages.
- Ongoing experiments and data collection continue without
 interruption.
- Researchers have a consistent experience across sites and
 geographies.

**Common anti-patterns:**

- Relying on single-instance deployments for critical systems.
- Maintenance performed without phased rollouts or rollback plans.
- Highly available architectures implemented without routine
 failover testing.

**Benefits of establishing this best
 practice:**

- Protects ongoing experiments from interruption, reducing risk of
 wasted samples or time.
- Preserves continuity in multi-day or multi-week lab workflows.
- Provides global research teams access to shared tools without
 productivity loss.
- Enhances regulatory readiness by reducing gaps in system
 availability records.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

When designing research workloads for resiliency, use deployment
 topologies that minimize the scope of impact of maintenance and
 outage events. Multi-site or multi–AZ deployments allow for
 uninterrupted operation when a system component is taken offline.
 Automated health checks and intelligent traffic routing directs
 users to healthy endpoints, maintaining continuity during upgrades
 or failover scenarios. Maintenance windows should be orchestrated
 to minimize user disruption, and resilience should be validated
 regularly through simulated failovers or planned game days.

### Implementation steps

1. Deploy AWS IoT Greengrass for local buffering of instrument
 data.
2. Deploy LIMS, EHR and ELN solutions across multiple
 Availability Zones using Amazon EC2 Auto Scaling for
 workload redundancy.
3. Place applications behind an Elastic Load Balancer (ALB or
 NLB) to support highly available deployment configurations,
 or configure Amazon Route 53 DNS failover with health checks
 for active-passive failover strategies.
4. Use AWS Systems Manager to coordinate upgrades with minimal
 disruption. Monitor resilience, health status, and failover
 events in Amazon CloudWatch, and validate readiness with
 regular failover exercises.

## Resources

**Related best practices:**

- Change management and controlled rollout strategies
- Incident response playbooks for scientific research systems
- Risk-based classification of R&D applications

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
