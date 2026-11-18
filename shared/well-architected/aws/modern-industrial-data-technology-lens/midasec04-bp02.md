<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec04-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC04-BP02 Use firewalls, perimeter networks, and dedicated network zones

Implement perimeter defenses such as firewalls, perimeter networks and dedicated network
 zones to manage and secure traffic flows between cloud, IT, and OT systems.

**Desired outcome:** Traffic is filtered and restricted at each
 trust boundary to enforce zero trust and layered defense.

**Benefits of establishing this best practice:** Helps improve
 network security posture, prevent direct exposure of OT systems, and support layered
 defense-in-depth architecture.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Deploy AWS Network Firewall, private subnets, and multi-tier perimeter network
 architectures to filter and control inbound and outbound traffic.

### Implementation steps

- Deploy AWS Network Firewall or third-party appliances in VPCs.
- Create perimeter networks between public internet and sensitive workloads using
 public and private subnet models.
- Enforce rule groups that restrict IPs, ports, and protocols.
- Continuously monitor and update firewall rules and network configurations.

## Resources

- [What is AWS Network Firewall?](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
- [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://aws.amazon.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec04-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
