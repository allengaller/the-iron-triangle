<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/alignment-to-demand.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Alignment to demand

In hybrid networking architectures, aligning network capacity with actual demand is
 fundamental to sustainability. Over-provisioned network connections waste energy through
 unused bandwidth and idle hardware, while under-provisioned links can cause retransmission and
 increased power consumption. By implementing demand-based capacity management and intelligent
 routing, organizations can optimize their network resource utilization while maintaining
 required performance levels.

Redundant infrastructure and excessive data movement increase energy consumption, carbon
 emissions, and costs. Proactively identifying and removing unused assets, consolidating
 overlapping resources, and minimizing data transfers ensures efficient resource utilization
 and reduces environmental impact.

Not all components in a workload are equally critical. By analyzing the purpose,
 utilization, and environmental impact of each component, you can prioritize optimizations for
 high-value resources while deprioritizing or retiring non-critical ones.

###### Best practices

- [HNSUS01-BP01 Decommission unused assets and consolidate redundant resources](./hnsus01-bp01.html)
- [HNSUS02-BP01 Prioritize critical components](./hnsus02-bp01.html)
- [HNSUS02-BP02 Perform lifecycle assessments for sustainability trade-offs](./hnsus02-bp02.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/alignment-to-demand.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
