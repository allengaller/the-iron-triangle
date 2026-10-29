<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops01-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVOPS01-BP01 Assess trade-offs between ad serving architecture options and associated risks

When designing the ad serving infrastructure, evaluate the trade-offs between different
 architectural approaches and their associated risks. This includes considering factors such
 as performance, scalability, availability, security, and cost to determine the optimal
 solution.

## Implementation guidance

- Assess the performance and scalability requirements of your
 ad serving workload, including peak traffic patterns and
 seasonal fluctuations. Evaluate architectures that can
 dynamically scale, such as serverless or containerized
 approaches.
- Analyze the availability and reliability needs of your ad
 serving infrastructure, ensuring that your architecture
 includes redundancy and fault tolerance mechanisms to
 maintain high uptime.
- Evaluate the security risks associated with your ad serving
 workload, such as bot attacks and ad fraud, and implement
 appropriate controls like web application firewalls and rate
 limiting.

## Key AWS services

### Key AWS services

- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Fargate](https://aws.amazon.com/fargate/)
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [Amazon EKS](https://aws.amazon.com/eks/)
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
- [Amazon Route 53](https://aws.amazon.com/route53/)
- [AWS WAF](https://aws.amazon.com/waf/)
- [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)
- [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/)

### Resources

- [Building
 Applications with Serverless Architectures](https://aws.amazon.com/lambda/serverless-architectures-learn-more/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops01-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
