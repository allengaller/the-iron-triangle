<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSEC04-BP01 Control access to network resources

Comprehensive network access control applied across both on-premises
 and cloud environments to create a unified security posture that
 addresses the unique challenges of hybrid infrastructures while
 maintaining compliance with regulatory requirements.

**Desired outcome:** Protect hybrid
 network resources by controlling traffic from on-premises and cloud
 environments.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Restrict network access to only approved sources
- Minimizes risk of unauthorized or malicious traffic
- Enables granular, instance-level security controls

## Implementation guidance

- Define least-privilege inbound and outbound rules matching
 only approved network prefixes.
- Regularly review and update rules for accuracy and compliance.

## Resources

- [Control
 traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
- [Control
 subnet traffic with network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
