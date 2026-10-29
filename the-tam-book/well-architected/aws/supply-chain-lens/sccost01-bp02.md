<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost01-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# SCCOST01-BP02 Adopt a flexible and scalable cloud infrastructure

A typical supply chain landscape will include ERPs, warehouse
 management systems (WMS), and transportation management systems
 (TMS) running on a large infrastructure that needs to be reliable,
 scalable and optimized for cost and performance.

**Desired outcome:** Pay as you go
 cloud infrastructure configured with auto scaling to expand or
 shrink as per demand of the workload. Cloud service quotas
 configured for peak usage.

**Benefits of establishing this best
 practice:** Reduced cost and better resiliency.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

Use AWS' pay-as-you-go model to align costs with actual usage
 and demand fluctuations, while implementing auto scaling
 capabilities to automatically adjust resources based on workload
 demands. Configure service quotas to accommodate peak usage for
 respective services and use containerization and serverless
 technologies for improved resource utilization and cost
 optimization.

### Implementation steps

1. Assess current infrastructure costs and identify
 opportunities for pay-as-you-go optimization.
2. Implement auto-scaling policies for compute, storage, and
 database resources based on demand patterns.
3. Configure appropriate service quotas to handle peak usage
 while avoiding unnecessary over-provisioning.
4. Deploy containerization technologies to improve resource
 utilization and reduce infrastructure costs.
5. Implement serverless architectures for event-driven
 workloads to minimize idle resource costs.
6. Establish cost monitoring and alerting mechanisms to track
 spending and identify optimization opportunities.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost01-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
