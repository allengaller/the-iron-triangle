<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVPERF05-BP04 Provide dedicated network connection between your on-premises environment and AWS to offer high bandwidth and low latency

Use dedicated network connections to provide stable and high-speed
 data communication between the on-premises data center and the AWS Cloud. This model is also applicable for connections between
 multiple Regions, providing efficient and secure data
 communication while effectively avoiding public network noise.

## Implementation guidance

For workloads that require high throughput or have strict
 compliance requirements, consider implementing
 [AWS Direct Connect](https://aws.amazon.com/directconnect/). AWS Direct Connect provides a dedicated
 network connection between your on-premises environment and AWS,
 offering high bandwidth, low latency, and enhanced security by
 bypassing the public internet.

## Key AWS services

- [AWS PrivateLink](https://aws.amazon.com/privatelink/)

## Resources

- [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)
- [Compliance
 validation for AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/DirectConnect-compliance.html)
- [Using
 the AWS Direct Connect Resiliency Toolkit to get started](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
