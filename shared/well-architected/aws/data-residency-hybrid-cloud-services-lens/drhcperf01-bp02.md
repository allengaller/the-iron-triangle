<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcperf01-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCPERF01-BP02 Monitor hybrid edge-specific metrics, and update resource configurations

Monitor your current capacity and plan for scaling to meet demand.

**Desired outcome:** You are aware
 of what capacity you have, and you scale as needed.

**Benefits of establishing this best
 practice:** You can proactively make decisions to acquire
 the appropriate capacity for your workloads.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

Outposts surfaces Amazon CloudWatch metric data, including CPU,
 network, and storage. You should monitor these metrics as you
 would in-Region to verify that you are achieving your
 performance targets. Monitor your resource consumption, and
 right-size compute and storage configurations based on the
 metric data. This is an iterative process as workloads change
 over time. Each server has a specific slotting configuration
 based on initial order. This can be modified based on metric
 data as long as the configuration is supported by the underlying
 server. For supported configurations, see
 [Modify
 AWS Outposts instance capacity](https://docs.aws.amazon.com/outposts/latest/userguide/modify-instance-capacity.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcperf01-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
