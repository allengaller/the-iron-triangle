<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost01-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVCOST01-BP02 Evaluate resiliency needs against the cost of downtime for ad delivery and bidding

While resiliency can increase the cost of workloads, downtime can also be very
 expensive. It's important to understand the costs of having a resilient infrastructure
 against the costs of not having a resilient infrastructure.

## Implementation guidance

- Quantify the cost of downtime for each campaign based on its expected revenue.
Analyze historical data and projections to estimate the potential revenue
 loss due to downtime.Consider the impact on customer satisfaction and brand reputation.
- Estimate the cost of applying resiliency measures.
Evaluate the cost of additional resources required for multi-Regional
 deployments, backup, and recovery solutionsUse AWS tools like [AWS Pricing Calculator](https://calculator.aws/#/)
 for estimating costs of future resiliency efforts and [Quick](https://aws.amazon.com/quicksight/), [Amazon Athena](https://aws.amazon.com/athena/), AWS Cost and Usage Report, and [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) for cost analysis
 and reporting.
- Compare the cost of downtime with the cost of resiliency measures.
If the potential lost revenue and reputation costs of downtime exceed the
 cost of resiliency, favor implementing resiliency measures.Consider multi-regional deployments, backup and recovery solutions, and other
 resiliency best practices.

By following these steps, you can make informed decisions about implementing
 resiliency measures based on a cost-benefit analysis, using AWS tools and services to
 optimize your approach and ensure business continuity.

## Key AWS services

- [AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/)
- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)

## Resources

- [Stage
 1: Set objectives](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/stage-1.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost01-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
