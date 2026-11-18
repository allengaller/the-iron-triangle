<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsus02-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCSUS02-BP01 When using Local Zones, monitor and scale your workloads to match demand, and use only the minimum required resources

Resources and services in AWS Local Zones, like those in AWS Regions, can be scaled dynamically to match measured demand,
 minimizing energy consumption.

**Desired outcome:** The number and type of Amazon EC2 instances deployed will be optimized to support workload requirements while adhering to sustainability goals

**Benefits of establishing this best
 practice:** Resource utilization can be reduced to
 minimize energy consumption and support your sustainability
 objectives.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

Although Local Zones provide only a subset of the Amazon EC2
 instance families and types available in an AWS Region, you
 should still use AWS capabilities that support elasticity to
 monitor and scale workloads to meet the measured demand and
 improve sustainability.

Services such as
 [Auto
 Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html),
 [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html), and
 [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) can be used to optimize the number and
 sizes of EC2 instances to meet workload demands. For
 [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) workloads, consider using
 [Karpenter](https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/)
 to automatically scale Kubernetes clusters to match
 instantaneous demand using instances aligned exactly to compute
 demands. For more detail on scaling for sustainability, see
 [SUS02-BP01
 Scale workload infrastructure dynamically](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a2.html) and
 [SUS02-BP03
 Stop the creation and maintenance of unused assets](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a4.html)
*.*

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsus02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
