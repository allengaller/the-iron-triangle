<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel06-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNREL06-BP01 Use multiple data centers for physical location redundancy

Connect from multiple geographically separate data centers or
 colocation sites to cloud for true physical location redundancy. Use
 dynamically routed, Active/Active connections across these sites to
 enable automatic load balancing and failover.

**Desired outcome:** Ensure network
 connectivity to cloud remains available even if one location
 experiences an outage or disaster.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Eliminates single points of failure at the physical site level
- Enables business continuity and disaster recovery
- Supports high availability and compliance requirements
- Improves resilience to disasters or unplanned events

## Implementation guidance

- Deploy dedicated connections from at least two geographically
 distinct facilities.
- Use dynamic routing BGP for automatic failover.
- Test failover regularly to validate resiliency.

## Resources

- [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel06-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
