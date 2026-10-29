<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost06-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNCOST06-BP01 Implement QoS policies for traffic prioritization

Configure QoS rules on on-premises routers to prioritize
 latency-sensitive traffic such as voice and video over bulk
 transfers such as data syncs.

**Desired outcome:** Guaranteed
 performance for critical workloads while optimizing bandwidth costs.

**Level of risk exposed if this best practice
 is not established:** Medium

**Benefits of establishing this best
 practice:**

- Prevents costly performance degradation for high-priority
 traffic
- Enables oversubscription of links without impacting critical
 workloads
- Aligns network costs with business value

## Implementation guidance

- Tag traffic with DSCP markers for on-premises traffic
 classification
- Apply shapers or queues on on-premises routers

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost06-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
