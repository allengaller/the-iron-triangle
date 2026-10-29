<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsus03-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCSUS03-BP01 Monitor workload and component resource utilization to identify any that are unneeded or over-provisioned when using Local Zones

Monitoring workload utilization is critical to identifying those
 which are overprovisioned and can be scaled down to reduce energy
 consumption.

**Desired outcome:** Workloads are
 deployed on Amazon EC2 instances that are aligned to requirements
 and provide optimal performance.

**Benefits of establishing this best
 practice:** Workloads and resources which are
 overprovisioned can be scaled down to reduce energy consumption
 and support sustainability objectives.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

Monitor and capture workload metrics such as CPU utilization,
 memory utilization, network connections, and network throughput
 using
 [Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) to identify workloads or components
 that are no longer used or are under-utilized. Routinely review
 the recommendations made by
 [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to identify instances that have been
 over-provisioned, and adjust as necessary to match instance type
 and size to the workload requirements. With AWS Local Zones, it
 is possible to maximize sustainability by using the large
 variety of Amazon EC2 instances to match resource consumption to
 workload requirements.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsus03-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
