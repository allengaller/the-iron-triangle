<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/performance-architecture.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Performance architecture

**Offload encryption to
 hardware**

Certain encryption approaches, such as VPN tunnels or IPsec
 meshes, can impact performance when implemented at scale.
 Where possible, offload encryption to hardware to maintain
 security while improving performance.

The [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) provides hardware components that allow
 for easy offloading of encryption services to the hardware.
 For example, some instance types use the hardware capabilities
 of the Nitro System hardware to encrypt in-transit traffic
 between instances with no impact to network performance. This
 allows healthcare organizations to enable encryption
 in-transit for sensitive healthcare data. Use instance types
 that support the Nitro System where possible.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/performance-architecture.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
