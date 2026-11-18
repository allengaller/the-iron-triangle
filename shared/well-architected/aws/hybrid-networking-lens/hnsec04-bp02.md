<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSEC04-BP02 Implement routing controls for network segments

Implementing routing controls for network segments involves
 strategically managing traffic flow between different parts of your
 network infrastructure. This includes setting up route tables to
 direct traffic based on security policies. These controls should
 enforce the principle of least privilege, ensuring network
 components can only communicate with authorized segments.

**Desired outcome:** Enable
 centralized, flexible, and secure traffic routing between cloud and
 on-premises networks.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Provides centralized control of network paths
- Allows for segmentation and isolation using null routes
- Prevents unauthorized or misrouted hybrid traffic

## Implementation guidance

- Design route tables to segment environments and block
 unnecessary paths.
- Use null routes to block specific destinations when needed.
- Periodically review and simulate route changes before
 deployment.

## Resources

- [Transit
 gateway route tables in AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html)
- [Core
 network policy versions in AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-create-policy-version.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
