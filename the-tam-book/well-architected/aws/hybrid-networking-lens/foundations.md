<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/foundations.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Foundations

When designing hybrid network connectivity solutions, organizations must prioritize
 redundant physical infrastructure across multiple data centers and implement diverse
 connectivity options through redundant hardware and telecommunications providers. Dynamic
 routing with active/active configurations enables automatic load balancing and failover, while
 sufficient network capacity ensures that redundant connections do not become overwhelmed when
 failures occur. These foundational elements must be complemented by appropriate bandwidth
 sizing based on workload requirements and regular testing of failover scenarios to validate
 configurations and recovery procedures.

Maintaining high availability and minimizing downtime in hybrid architectures requires
 not only redundant power and network connectivity, but also effective life cycle management of
 on-premises network equipment. Implementing redundancy at every layer and proactively managing
 the health, replacement, and support of physical networking assets are key to achieving a
 resilient hybrid environment.

###### Best practices

- [HNREL01-BP01 Implement redundant power infrastructure](./hnrel01-bp01.html)
- [HNREL01-BP02 Maintain effective life cycle management for on-premises network equipment](./hnrel01-bp02.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/foundations.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
