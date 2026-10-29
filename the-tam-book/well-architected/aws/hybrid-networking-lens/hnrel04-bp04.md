<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNREL04-BP04 Provision sufficient network capacity

Provision enough network capacity so that the failure of a single
 network connection does not overwhelm or degrade the remaining
 redundant connections.

**Desired outcome:** Maintain
 performance and service levels during network outages or planned
 maintenance by ensuring available bandwidth meets business needs.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Avoids performance bottlenecks during failover
- Ensure sufficient capacity for critical workloads at all times
- Supports scalability and growth in hybrid environments
- Enhances customer and user experience

## Implementation guidance

- Analyze peak and average bandwidth requirements for hybrid
 workloads.
- Size redundant connections so any one connection can handle
 the full load if others fail.
- Monitor bandwidth usage and adjust capacity proactively.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
