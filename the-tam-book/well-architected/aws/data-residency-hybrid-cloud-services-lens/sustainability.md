<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/sustainability.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Sustainability

The sustainability pillar includes the ability to deliver business
 value while minimizing resource usage, environmental impacts, and
 energy consumption. This section provides you with an overview of
 sustainability design principles, best
 practices, and questions. You can find implementation
 guidance in the
 [Sustainability
 Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).

## Definitions

This whitepaper covers sustainability in the cloud, describing best practices in the following areas:

- Region selection
- Alignment to demand
- Software and architecture patterns
- Data management
- Hardware and services

## Design principles

The Well-Architected Framework identifies a set of general design
 principles to facilitate sustainability while deploying hybrid
 services and workloads:

- **Consider workload
 placement:** It is always a best practice to use AWS Regions when building workloads, as Regions offer tools for
 managing service and instance elasticity. If a workload has
 latency or data residency requirements that cannot be
 addressed in a Region, consider using an AWS Local Zone where
 workload elasticity is still easily achieved with Amazon EC2.
 If a Local Zone cannot meet workload requirements, consider
 using AWS Outposts, where capacity must be more precisely
 matched with requirements.
- **Characterize workload
 requirements:** Before using AWS hybrid services,
 fully assess and understand your workload resource
 requirements. Always engage an AWS migration specialist, and
 use the AWS Migration Evaluator to capture workload resource
 utilization to make a data-driven decision on which hybrid
 services to use and how much capacity to deploy.
- **Match EC2 instance size to measured
 load:** Use tools such as Amazon CloudWatch and AWS Compute Optimizer to track EC2 instance resource utilization
 and right-size instances based on data-driven recommendations.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/sustainability.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
