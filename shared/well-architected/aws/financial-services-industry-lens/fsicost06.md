<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost06.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# FSICOST06: How do you track your workload usage cycles?

Financial services workload usage can be cyclical and can have usage spikes during
 specific days like month-end or quarter-end, or it can be intra-day during specific hours.
 AWS provides customers with a number of usage monitoring services that can scale your
 operations up and down as demand conditions require. Monitor cost at an application-level,
 and a workload-level on a regular basis, and optimize usage of resources and cost.

## FSICOST06-BP01 Monitor your workload usage cycle around times of higher and lower utilization (quarter-end, year-end, weekends, and holidays) to identify ways to reduce your costs

You may have workload usage cycles for week-end or month-end, and quarter-end have
 more usage of resources. In some cases, there could be higher usage due to events like the
 start of trading hours, holidays shopping, and so on. Monitoring usage and corresponding
 events are helpful to optimize cost and architecture. You can choose to shutdown unused
 instances, for example Amazon EC2 servers for development, or QA on Friday, and bring them back
 up on Monday.

Scale generative AI inference endpoints and vector search infrastructure dynamically
 with observed diurnal patterns. Pre-warm minimal capacity only for peak trading or
 batch-report windows, then decay to zero or low-cost tiers during off-hours. Automate
 these adjustments via scheduled scaling policies or event-driven Lambda functions to
 minimize idle inference costs.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost06.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
