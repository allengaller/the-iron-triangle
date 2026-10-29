<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus03-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVSUS03-BP01 Use caching techniques to prevent frequent data access

Implement caching techniques to store frequently accessed data in
 cache, preventing repeated data retrieval and thereby reducing
 computing time and energy consumption for advertising workloads.

## Implementation guidance

- Implement caching strategies for advertising content and
 data to minimize frequent data access and reduce computing
 time and energy consumption.
- Use AWS caching services like
 [Amazon ElastiCache](https://aws.amazon.com/elasticache/) (for in-memory caching) and
 [Amazon CloudFront](https://aws.amazon.com/cloudfront/) (for content delivery network caching) to
 store frequently accessed data closer to the consumers,
 reducing latency and compute requirements.
- Consider using
 [AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/) and CloudFront Functions to run
 lightweight logic at edge locations, minimizing the need for
 data transfer to centralized servers and reducing overall
 energy consumption.

## Key AWS services

- [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) (for optimizing data transfer over
 the AWS Cloud)
- [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) (for energy-efficient compute
 instances)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus03-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
