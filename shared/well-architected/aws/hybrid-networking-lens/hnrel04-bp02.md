<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNREL04-BP02 Use redundant hardware and telecommunication providers

When designing remote connections to your cloud provider, use
 redundant on-premises hardware and diverse telecommunications
 providers. Ensure your last-mile connectivity has diverse physical
 paths and that providers offer SLAs that meet your uptime
 requirements.

**Desired outcome:** Reduce the risk
 of connectivity loss due to hardware failure or carrier issues,
 supporting continuous access to cloud resources.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Mitigates risks from hardware or provider outages
- Increases fault tolerance and connection reliability
- Supports compliance with high-availability SLAs
- Provides business continuity during provider-specific
 disruptions

## Implementation guidance

- Use at least two separate routers, switches, and cabling for
 each Direct Connect location.
- Contract with multiple telecommunications providers for
 circuit diversity.
- Periodically review provider SLAs and test failover.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
