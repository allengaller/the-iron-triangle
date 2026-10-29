<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost03-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNCOST03-BP01 Implement tiered connectivity based on workload requirements

Hybrid networking connectivity must balance performance,
 reliability, and cost. Workloads with varying requirements for
 throughput, latency, and uptime should leverage different
 connectivity solutions. For example, non-critical workloads (for
 example, development or testing) can use cost-effective
 internet-based VPNs, while mission-critical production workloads may
 require dedicated connections like AWS Direct Connect. A tiered
 approach ensures you only pay for the level of connectivity your
 workloads actually need.

**Desired outcome:** Cost savings
 through workload-aligned connectivity, with no overpayment for
 unnecessary bandwidth or redundancy.

**Level of risk exposed if this best practice
 is not established:** Medium

**Benefits of establishing this best
 practice:**

- Reduces costs for non-critical workloads
- Ensures high performance for production workloads
- Simplifies scaling as requirements evolve

## Implementation guidance

- Use IPSec VPN connections for non-mission critical workloads
- Use dedicated connections for production workloads
- Scale from IPSec VPN connections in testing phase to dedicated
 connections after bandwidth requirements are defined
- Use direct connectivity to single cloud network connectivity
 to avoid additional cloud transit costs, For example, you can
 use Direct Connect private VIF to connect directly to VPC.
- Use cloud transit connectivity to connect to multiple cloud
 networks. For example, you can use Direct Connect transit VIF
 to connect to Transit Gateway for VPCs in the same region, or
 Cloud WAN core network for VPCs in multiple regions

## Resources

- [Site-to-Site VPN
 pricing](https://aws.amazon.com/vpn/pricing/)
- [AWS Direct Connect Pricing](https://aws.amazon.com/directconnect/pricing/)
- [AWS Transit Gateway Pricing](https://aws.amazon.com/transit-gateway/pricing/)
- [AWS Cloud WAN Pricing](https://aws.amazon.com/cloud-wan/pricing/)
- [Hybrid
 Connectivity](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/hybrid-connectivity.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost03-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
