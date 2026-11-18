<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf07.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Multi-tenancy and resource optimization

A well-designed multitenant agent service lets organizations serve
 many teams and customers from shared infrastructure while
 delivering consistent, predictable performance to each.
 Multitenant agent deployments must isolate one tenant's workload
 so it can't degrade the performance experienced by other tenants,
 and at the same time optimize overall resource utilization to
 control costs. This requires designing deployment models that
 provide appropriate isolation boundaries, implementing throttling
 and quota mechanisms that enforce fair resource allocation, and
 right-sizing serverless compute configurations for the bursty
 nature of agent workloads.

## Capability intent

- Tenant deployments are organized into tiers with explicit
 performance, isolation, and cost profiles, rather than a
 single shape applied uniformly to every tenant.
- Pooled tiers share managed infrastructure that provides
 session-level isolation, and premium or enterprise tiers add
 dedicated resources where stronger isolation is required.
- Throttling is enforced at every shared resource layer (API,
 inference, memory, tools), so tenants can't bypass edge
 limits through long-running downstream operations.
- Adaptive throttling lets tenants use slack capacity during
 low-load periods and snaps back to baseline during
 contention, while honoring tier priority.
- Tenant context propagates through the full stack, and
 per-tenant dashboards track latency, error rates, throttle
 state, and resource consumption against the tier's SLA.
- Isolation is validated through regular noisy-neighbor
 testing, so the deployment model's performance claims are
 measured rather than assumed.

## Common issues to watch for

- Teams deploy fully isolated infrastructure for every tenant
 regardless of need, wasting capacity on tenants whose
 requirements would be met by pooled resources.
- Teams use a single pooled deployment without per-layer
 isolation, letting high-volume tenants consume
 disproportionate capacity and degrade performance for
 everyone else.
- Throttling is enforced only at the API edge, so tenants
 bypass edge limits through long-running inference, memory,
 or tool operations that saturate downstream shared
 resources.
- Throttling uses static limits that neither use available
 slack during low-load periods nor protect isolation during
 high-load periods, and premium tenants are throttled
 identically to standard tenants.
- Tenant onboarding requires infrastructure provisioning on
 every new customer, so onboarding time and operational
 overhead grow linearly with tenant count.
- Isolation is assumed rather than tested, so subtle changes
 (a new tool, a heavier prompt, a shift in traffic mix) erode
 the isolation boundary silently and surface only during a
 real incident.

###### Best practices

- [AGENTPERF07-BP01 Design efficient multitenant agent deployment models](./agentperf07-bp01.html)
- [AGENTPERF07-BP02 Implement tenant-aware performance isolation and throttling](./agentperf07-bp02.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf07.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
