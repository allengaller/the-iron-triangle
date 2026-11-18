<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus10-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVSUS10-BP01 Optimize content moderation systems for sustainable operation

As content grows for organizations, optimizing content moderation systems can benefit sustainability-related key performance indicators (KPIs). Implement or build architectures that include efficient machine learning models, automated scaling, and optimized storage patterns.

## Implementation guidance

- Use efficient machine learning models for content
 classification. Use AWS Inferentia chips when possible,
 for improved performance per watt.
- Implement batch processing for non-real-time moderation
 tasks.
- Configure regional content analysis to minimize data
 movement.
- Use caching strategies for frequently accessed moderation
 rules.
- Use energy-efficient computing resources, such as AWS
 Graviton, for moderation workloads.
- Implement automated scaling based on moderation demand
 using auto scaling rules and Amazon CloudWatch metrics.
- Optimize storage patterns for moderation results and audit
 trails. For workloads using Amazon S3, use Storage Lens for
 insights and recommendations to optimize storage use.

## Key AWS services

- Amazon Rekognition
- AWS Inferentia
- Amazon SageMaker AI
- AWS Auto Scaling
- AWS CloudWatch
- Amazon ElastiCache
- Amazon S3 Storage Lens

## Resources

- [Optimize AI/ML workloads for sustainability: Part 1, identify business goals, validate ML use, and process data](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus10-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
