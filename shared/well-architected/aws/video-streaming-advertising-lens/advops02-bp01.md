<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVOPS02-BP01 Implement monitoring across each layer of your advertising stack including infrastructure, applications, and user experience

Ensuring operational excellence in advertising workloads requires
 a holistic approach to monitoring. This best practice emphasizes
 the importance of implementing comprehensive monitoring solutions
 that span all layers of the advertising stack. The advertising
 stack includes the ad-serving infrastructure, data pipelines,
 application performance, and user experience. By monitoring these
 various components, you can gain a complete understanding of the
 overall health and performance of your advertising workload. This
 understanding helps you identify and address issues, optimize
 resource utilization, and deliver a seamless customer experience.
 With a multi-layered monitoring approach, you can proactively
 detect and resolve problems before they impact your business.

## Implementation guidance

Monitor and set KPIs and SLOs for infrastructure services using
 [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) for services like
 [Amazon EC2](https://aws.amazon.com/ec2/)
 and [Amazon EBS](https://aws.amazon.com/ebs/). Set up CloudWatch Alarms for resource utilization,
 performance, and availability.

## Resources

- [Observability using native Amazon CloudWatch and AWS X-Ray for serverless modern applications](https://aws.amazon.com/blogs/mt/observability-using-native-amazon-cloudwatch-and-aws-x-ray-for-serverless-modern-applications/)
- [AWS Observability Maturity Model](https://aws-observability.github.io/observability-best-practices/guides/observability-maturity-model/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
