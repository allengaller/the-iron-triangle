<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnperf02-bp05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNPERF02-BP05 Plan for bandwidth scaling

High-speed dedicated connections can offer bandwidth up to hundreds
 of gigabits per second. LAG enables bundling multiple physical
 connections to increase total available bandwidth. Additionally,
 implementing load balancing across multiple connections using ECMP
 routing provides enhanced bandwidth scaling and improved
 reliability. For virtual private network implementations, similar
 scaling can be achieved by establishing multiple VPN connections and
 utilizing ECMP to distribute traffic effectively across these paths.
 Understanding these scaling options and their appropriate use cases
 is crucial for designing network architectures that can grow with
 business demands while maintaining performance and reliability.

**Desired outcome:**

- Achieve optimal network performance and capacity that meets
 growing business demands.
- Scalable network infrastructure capable of increasing traffic
 volumes

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Enables strategic bandwidth scaling decisions based on actual
 business needs while optimizing costs.
- Provides flexibility to adjust network capacity through various
 technical approaches as requirements evolve.
- Load balancing across multiple connections using BGP ECMP,
 ensuring optimal traffic distribution.

## Implementation guidance

- Assess current and projected bandwidth requirements,
 considering both peak usage patterns and growth trajectories.
- Evaluate infrastructure limitations and compatibility at both
 connection endpoints, including port speeds, hardware
 capabilities, and routing protocol support.
- Design for operational efficiency with centralized management,
 monitoring, and clear maintenance procedures.
- Consider cost implications and geographical requirements when
 choosing between scaling approaches, such as dedicated
 connections vs IPSec VPNs.

## Resources

- [AWS Direct Connect link aggregation groups (LAGs)](https://docs.aws.amazon.com/directconnect/latest/UserGuide/lags.html)
- [AWS Direct Connect routing policies and BGP communities](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html)
- [Active/Active
 and Active/Passive Configurations in AWS Direct Connect](https://docs.aws.amazon.com/architecture-diagrams/latest/active-active-and-active-passive-configurations-in-aws-direct-connect/active-active-and-active-passive-configurations-in-aws-direct-connect.html)
- [Scaling
 your VPN throughput using Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-vpn-throughput-using-aws-transit-gateway/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnperf02-bp05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
