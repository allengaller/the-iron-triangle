<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/resiliency-and-the-components-of-reliability.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Resiliency, and the components of reliability

Reliability of a workload in the cloud depends on several factors, the primary of which
 is *Resiliency*:

- **Resiliency** is the ability of a workload to recover from
 infrastructure or service disruptions, dynamically acquire computing resources to meet
 demand, and mitigate disruptions, such as misconfigurations or transient network issues.

The other factors impacting workload reliability are:

- Operational Excellence, which includes automation of changes, use of playbooks to
 respond to failures, and Operational Readiness Reviews (ORRs) to confirm that
 applications are ready for production operations.
- Security, which includes preventing harm to data or infrastructure from malicious
 actors, which would impact availability. For example, encrypt backups to ensure that
 data is secure.
- Performance Efficiency, which includes designing for maximum request rates and
 minimizing latencies for your workload.
- Cost Optimization, which includes trade-offs such as whether to spend more on EC2
 instances to achieve static stability, or to rely on automatic scaling when more
 capacity is needed.

Resiliency is the primary focus of this whitepaper.

The other four aspects are also important and they are covered by their respective
 pillars of the [AWS
 Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/). Many of the best practices here also address those
 aspects of reliability, but the focus is on resiliency.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/resiliency-and-the-components-of-reliability.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
