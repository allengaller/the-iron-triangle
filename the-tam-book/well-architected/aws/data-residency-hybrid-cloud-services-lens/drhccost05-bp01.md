<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhccost05-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCCOST05-BP01 Monitor data transfer to and from your hybrid edge workload

Regularly track and analyze data transfer costs.

**Desired outcome:** You monitor
 the costs associated with data transfer.

**Benefits of establishing this best
 practice:** You can recognize the cost associated with
 your network flows.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

While using hybrid edge services like AWS Outposts and Local
 Zones, monitor data transfer patterns and costs, and design your
 network configurations with cost optimization in mind. Data
 transfer from Outposts to AWS Regions is free, but transfers
 from Regions to Outposts are more expensive over the internet
 compared to AWS Direct Connect. Local Zones have internet
 gateways for local egress, but routing traffic to AWS Regions
 incurs additional charges similar to
 [inter-AZ
 transfers](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer_within_the_same_AWS_Region). You can use local VPC peering for Outposts and
 Local Zones, which incurs lower costs than using AWS Transit Gateway and minimizes network overhead. Additionally, you should
 design hybrid architectures following networking best practices
 to meet low latency requirements while optimizing costs.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhccost05-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
