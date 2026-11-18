<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSEC04-BP03 Implement network traffic security inspection

Network traffic security inspection provides a layered security
 approach to ensure traffic between your cloud and on-premises
 resources is properly monitored and protected against threats.

**Desired outcome:** Deploy
 inspection and security enforcement on ingress and egress network
 paths as needed.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Enables deep packet inspection
- Provides scalable firewall for hybrid network traffic
- Enables advanced rule sets for protocol, domain, and threat
 filtering
- Simplifies compliance with perimeter defense requirements

## Implementation guidance

- Route traffic through the firewall appliances
- Define and maintain firewall rule groups for hybrid traffic.
- Monitor firewall activity and adapt rules as threats evolve.

## Resources

- [Gateway
 Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html)
- [Centralized Traffic Inspection with Gateway Load Balancer on AWS](https://aws.amazon.com/blogs/apn/centralized-traffic-inspection-with-gateway-load-balancer-on-aws/)
- [AWS Network Firewall Documentation](https://docs.aws.amazon.com/network-firewall/latest/developerguide/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
