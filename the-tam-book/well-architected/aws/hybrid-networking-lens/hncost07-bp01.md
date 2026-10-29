<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost07-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNCOST07-BP01 Use dedicated connection for high-volume predictable traffic

Deploy dedicated connection for production workloads requiring
 consistent, high-bandwidth connectivity between on-premises and
 cloud environments. Dedicated connection offers lower per-GB costs
 compared to IPSec VPN and avoids internet variability.

**Desired outcome:** Predictable,
 reduced data transfer costs for mission-critical workloads.

**Level of risk exposed if this best practice
 is not established:** Medium

**Benefits of establishing this best
 practice:**

- cost savings versus VPN for high-volume traffic
- Improved performance and reliability

## Implementation guidance

- Start with low bandwidth dedicated connections and scale up
 with high bandwidth connections or multiple connections with
 LAG

## Resources

- [AWS Direct Connect Pricing](https://aws.amazon.com/directconnect/pricing/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost07-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
