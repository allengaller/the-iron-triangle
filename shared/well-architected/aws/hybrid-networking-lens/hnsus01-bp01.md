<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsus01-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSUS01-BP01 Decommission unused assets and consolidate redundant resources

Regularly audit your workload to identify and remove unused or
 redundant assets (for example, orphaned storage volumes, inactive
 EC2 instances, and outdated datasets). Consolidate overlapping
 resources (for example, duplicate reports and redundant databases)
 to eliminate waste.

**Desired outcome:** Reduced resource
 consumption and minimized environmental footprint by eliminating
 unnecessary infrastructure.

**Level of risk exposed if this best practice
 is not established:** Low

**Benefits of establishing this best
 practice:**

- Frees up compute, storage, and network resources
- Lowers energy consumption and costs
- Simplifies architecture and improves maintainability

## Implementation guidance

- Identify underutilized resources. For example, you can achieve
 this using AWS Trusted Advisor Cost Optimization Checks
- Use policies to automate deletion of unused assets. For
 example, you can achieve this using Amazon S3 Lifecycle
 Policies and Amazon Data Lifecycle Manager

## Resources

- [AWS Trusted Advisor: Cost Optimization Checks](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)
- [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Delete
 Amazon Data Lifecycle Manager policies](https://docs.aws.amazon.com/ebs/latest/userguide/delete.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsus01-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
