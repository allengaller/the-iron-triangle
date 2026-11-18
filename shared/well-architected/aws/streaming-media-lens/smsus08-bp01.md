<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus08-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# SMSUS08-BP01 use AWS managed services for efficient resource utilization

Use managed services in place of self-operated equivalents wherever a workload fits one. Managed services share infrastructure across many customers and scale with demand, so they reach a far higher average utilization than a self-managed component that each team provisions for its own peak and leaves idle the rest of the time.

**Desired outcome:**

- Capabilities that AWS offers as managed services are consumed as managed services rather than rebuilt on self-operated infrastructure.
- Workloads scale with demand and don't hold idle capacity for peaks that occur rarely.
- Engineering effort goes to streaming-specific differentiation rather than operating commodity infrastructure at low utilization.

**Common anti-patterns:**

- Building and operating bespoke transcoding, analytics, or recommendation infrastructure when a managed service provides the same capability at higher shared utilization.
- Provisioning standing clusters sized for peak load to run intermittent analytics or processing, leaving them powered and idle between jobs.
- Self-hosting machine learning for content moderation or recommendations on persistent instances rather than using managed inference that scales with request volume.
- Running self-managed monitoring infrastructure that must itself be provisioned and maintained instead of using a managed observability service.

**Benefits of establishing this best practice:**

- Higher infrastructure utilization, because managed services share capacity across customers rather than each team provisioning its own peak.
- Reduced idle capacity, because managed services scale with demand instead of holding standing resources.
- Lower operational resource overhead, because the supporting infrastructure for monitoring, scaling, and patching is shared rather than duplicated per workload.
- More engineering capacity directed at streaming differentiation rather than operating commodity components.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance

A self-managed component is provisioned by a single team for its own peak demand and runs below that peak, often far below, the rest of the time, so the gap between provisioned and used capacity is powered and idle. A managed service aggregates demand across many customers and scales capacity to match, so the same workload runs at a much higher average utilization and the idle headroom each team would otherwise hold is removed. For intermittent media workloads such as batch transcoding or periodic analytics, this difference is large, because the self-managed alternative is idle most of the time.

The decision isn't unconditional, and treating "managed is unconditionally better" as a rule is how this practice is misapplied. Managed services trade a degree of control and portability for efficiency and reduced operations, and some workloads have requirements such as specific codec configurations, data residency, or latency characteristics that a managed service doesn't meet. The right approach is to default to the managed service where the workload fits and reserve self-managed infrastructure for the cases that genuinely require it, rather than rebuilding commodity capabilities by habit.

Apply the same reasoning across the stack. The following all have managed options that run at higher utilization than self-hosted equivalents.

- File-based transcoding
- Streaming analytics
- Recommendation
- Content moderation
- Observability

Energy use isn't measurable per request, so use resource proxies such as the share of workloads on managed compared to self-managed infrastructure, and the idle capacity removed by the shift. Read account-level carbon impact per Region from the AWS Customer Carbon Footprint Tool, which publishes monthly.

### Implementation steps

1. **Inventory self-managed components against managed equivalents:** List the self-operated infrastructure in the streaming workload and identify which capabilities have a managed AWS equivalent, flagging those running at low average utilization as the highest-value candidates.
2. **Move file-based transcoding to a managed service:** Replace self-managed encoding with AWS Elemental MediaConvert so transcoding runs on shared, demand-scaled infrastructure rather than standing capacity.
3. **Use managed analytics for intermittent processing:** Run streaming analytics through managed services such as Amazon Managed Service for Apache Flink or Amazon Kinesis rather than standing clusters provisioned for peak.
4. **Use managed inference for recommendation and moderation:** Adopt Amazon Personalize for recommendations and Amazon Rekognition for content analysis and moderation instead of self-hosting models on persistent instances.
5. **Use managed observability:** Consolidate monitoring on Amazon CloudWatch rather than operating self-managed monitoring infrastructure that must itself be provisioned and scaled.
6. **Measure the utilization shift:** Track the proportion of workloads on managed services and the idle capacity removed, and review against the monthly account-level figures from the AWS Customer Carbon Footprint Tool.

## Resources

**Related best practices**

- [SMSUS02-BP01 Implement adaptive infrastructure scaling based on viewer patterns](smsus02-bp01.html)
- [SMSUS07-BP01 Leverage energy-efficient computing resources](smsus07-bp01.html)

**Related documents**

- [Optimizing Streaming Media Workflows to Reduce Your Carbon Footprint, Part I](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-i/)
- [Sustainability Pillar, Hardware and services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/hardware-and-services.html)

**Related services**

- [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/)
- [Amazon Personalize](https://aws.amazon.com/personalize/)
- [Amazon Rekognition](https://aws.amazon.com/rekognition/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus08-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
