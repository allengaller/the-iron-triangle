<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNREL04-BP01 Use physical location redundancy to host dedicated connections

Design dedicated connections hosted at multiple geographically
 separated data centers or colocation facilities to provide physical
 location redundancy. This design ensures that your connectivity to
 cloud remains available even if one location is affected by an
 outage or disaster.

**Desired outcome:** Maintain high
 availability and business continuity for hybrid connectivity, even
 in the event of a site-level failure.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Minimizes the risk of a single point of failure
- Enhance disaster recovery capabilities
- Supports compliance and uptime requirements
- Increases overall hybrid network resilience

## Implementation guidance

- Deploy Direct Connect connections in at least two
 geographically distinct locations.
- Route traffic dynamically between locations for failover.
- Test failover scenarios regularly to validate resilience.

**Resources:**

- [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
