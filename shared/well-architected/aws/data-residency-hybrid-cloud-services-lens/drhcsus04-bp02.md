<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsus04-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCSUS04-BP02 Use elasticity and automation to optimize storage volumes usage in AWS Local Zones

EBS volumes attached to EC2 instances in AWS Local Zones should be
 provisioned as small as possible to meet workload requirements and
 then grown as needed when more capacity is required.

**Desired outcome:** EBS volumes
 will be sized to meet workload requirements and minimize energy
 consumption, while growing dynamically via automation when needed.

**Benefits of establishing this best
 practice:** Your workloads will be provisioned to use the
 minimum required EBS storage, decreasing energy consumption, while
 retaining the ability to grow storage via automation when needed.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

Create and use Amazon EBS volumes in Local Zones with size,
 throughput, and latency characteristics appropriate for your
 data residency workloads. Provision the smallest suitable EBS
 volumes, and use
 [elasticity
 and automation](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a5.html) to expand volumes as data grows. This
 improves sustainability by preventing over-provisioning of
 workload storage. Use
 [Amazon CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.html) to collect and monitor guest disk
 utilization, and set thresholds to initiate EBS volume expansion
 when thresholds are reached.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsus04-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
