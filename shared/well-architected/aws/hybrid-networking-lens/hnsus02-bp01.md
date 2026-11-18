<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsus02-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSUS02-BP01 Prioritize critical components

Break down your workload into individual components (for example,
 microservices, databases, and APIs). Use metrics like CPU
 utilization, request rates, and business impact to classify them as
 critical or non-critical.

**Desired outcome:** Resource
 allocation aligned with business value, minimizing waste in
 low-impact areas.

**Level of risk exposed if this best practice
 is not established:** Medium

**Benefits of establishing this best
 practice:**

- Focuses optimization efforts on high-impact components
- Reduces energy consumption
- Maintains performance for mission-critical workloads

## Implementation guidance

- Map component dependencies and usage. For example, you can
 achieve this using AWS X-Ray.
- Apply tags to categorize components (for example,
 business-critical, dev-test).
- Right-size your resources during off-peak hours. For example,
 you can achieve this using AWS Auto Scaling.

## Resources

- [AWS X-Ray: Service Map Analysis](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html)
- [Best
 Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html)
- [AWS Auto Scaling - application scaling](https://aws.amazon.com/autoscaling/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsus02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
