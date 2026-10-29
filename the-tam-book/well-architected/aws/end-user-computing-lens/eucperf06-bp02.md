<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCPERF06-BP02 Minimize latency between EUC instances and dependent services

In most cases, EUC users require connections to resources outside their EUC instances.
 Common dependencies include web or application servers, database servers, and storage
 services.

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

When possible, deploy these dependencies in the same AWS Region and ideally the same
 Availability Zone. If the system of record must reside elsewhere, consider deploying
 caches or replicas. For example, if your Active Directory domain controllers are on your
 on-premises network, deploy replicas on Amazon EC2.

When connecting to Amazon S3, use gateway VPC endpoints. For more information on
 configuring gateway endpoints, see [Gateway endpoints for
 Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
