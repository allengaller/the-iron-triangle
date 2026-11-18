<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec05-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSEC05-BP02 Use MACsec encryption for dedicated connections

Dedicated connections allow hybrid network connectivity over a
 private network link. MACsec encrypts traffic at Layer 2 to securely
 pass high bandwidth workloads between cloud and on-premises
 infrastructure. It provides native, point-to-point encryption to
 protect data communications. To use MACsec, both the dedicated
 connection and your on-premises equipment must support it.

**Desired outcome:** Encrypt
 high-speed data traffic between cloud and your data center to
 protect sensitive workloads from interception or tampering.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Delivers encryption for high bandwidth connections
- Secures data in transit without sacrificing performance
- Enables compliance with industry and regulatory standards

## Implementation guidance

- Use dedicated connection links that support MACsec.
- Enable MACsec on both the dedicated connection port and your
 on-premises network device.
- Regularly validate and monitor MACsec status and connection
 health.

## Resources

- [MAC
 Security in Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec05-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
