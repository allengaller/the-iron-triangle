<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost02-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVCOST02-BP01 Use ARM processors for faster and more cost-effective bidder nodes

ARM processors can combine lower costs and higher performance, which makes them a great
 consideration for cost optimization.

## Implementation guidance

- Use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to identify
 the most cost-effective instance types for bidding workloads, and verify that ARM
 instances were considered.
- Use [AWS Graviton](https://aws.amazon.com/ec2/graviton/) instances,
 which are powered by ARM processors designed by AWS, for your cloud workloads
 running in [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/), AWS Lambda,
 containers, and various other services.
- Take advantage of the cost savings offered by Graviton instances, which generally
 cost less than comparable x86 instances.
- For custom software, recompile it for use on Graviton processors with the
 assistance of open-source tools like [sse2neon](https://github.com/DLTcollab/sse2neon) and [Porting Advisor for
 Graviton](https://github.com/aws/porting-advisor-for-graviton) for compiled applications.
- For interpreted or JIT languages, they generally run as-is or with minimal
 modifications on Graviton processors.
- Conduct performance testing and benchmarking to verify that Graviton instances
 meet bidding workload requirements.

## Key AWS services

- [Amazon Cloudwatch](https://aws.amazon.com/cloudwatch/)
- [Amazon
 Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

## Resources

- [Use Graviton instances and containers](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-graviton.html)
- [How DeviceAtlas optimized Real-Time Advertising Price/Performance on AWS
 Graviton3](https://aws.amazon.com/blogs/industries/how-deviceatlas-optimized-real-time-advertising-price-performance-on-aws-graviton3/)
- [Using
 Porting Advisor for Graviton](https://aws.amazon.com/blogs/compute/using-porting-advisor-for-graviton/)
- [AWS Unveils Next Generation AWS-Designed Chips](https://press.aboutamazon.com/2023/11/aws-unveils-next-generation-aws-designed-chips)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
