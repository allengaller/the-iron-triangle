<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnperf02-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNPERF02-BP04 Select the most appropriate region for your workloads

Selecting the optimal region for your workloads in a hybrid
 networking environment requires careful consideration of latency,
 data residency requirements, and connectivity options to your
 on-premises infrastructure. Choose regions geographically proximate
 to your physical data centers and end users to minimize network
 latency while ensuring compliance with data sovereignty regulations
 specific to your industry. The region selection will ultimately
 balance performance needs with compliance requirements and cost
 considerations for your hybrid architecture

**Desired outcome:**

- Achieve optimal workload performance by strategically placing
 cloud infrastructure closer to end-users and on-premises
 resources.
- Ensures minimal latency for latency-sensitive applications while
 maintaining secure and reliable connectivity between your data
 center and Cloud resources.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Single-digit millisecond latency for latency-sensitive
 applications like media rendering, real-time gaming, virtual
 desktop solutions or any other latency sensitive applications.
- Maintain data residency requirements while leveraging services
 closer to their physical location.

## Implementation guidance

- Identify workloads that require ultra-low latency or local
 data processing.
- Select the infrastructure such as AWS local zones which are
 closer to your end users to run latency-sensitive
 applications.
- Implement dedicated connection such as Direct Connect with a
 private virtual interface through Direct Connect gateway for
 optimal performance.
- Track the application and network performance through
 monitoring solutions like Amazon CloudWatch

## Resources

- [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)
- [Extend
 a VPC to a Local Zone, Wavelength Zone, or Outpost](https://docs.aws.amazon.com/vpc/latest/userguide/Extend_VPCs.html)
- [AWS Direct Connect and AWS Local Zones interoperability
 patterns](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-direct-connect-and-aws-local-zones-interoperability-patterns/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnperf02-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
