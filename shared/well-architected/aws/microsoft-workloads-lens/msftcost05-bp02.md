<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost05-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MSFTCOST05-BP02 Control Amazon EBS volumes or snapshots lifecycle

EBS snapshots are incremental backups stored in S3, saving only
 changed blocks since the last snapshot. They can backup unattached
 volumes before deletion. Two storage tiers available: Standard
 (higher storage cost and free retrieval) and Archive (lower storage
 cost and paid retrieval). Managing snapshot lifecycles and removing
 unused volumes helps optimize costs.

**Desired outcome:** Implement an
 effective EBS volume and snapshot management strategy that
 automatically identifies and removes unused volumes while
 maintaining cost-efficient snapshot lifecycles across appropriate
 storage tiers, resulting in optimized storage costs for Microsoft
 workloads on AWS.

**Common anti-patterns:**

- Neglecting to delete unattached EBS volumes: Keeping unused
 volumes active, leading to unnecessary ongoing storage costs for
 resources that are no longer needed.
- Inconsistent or manual snapshot management: Relying on manual
 processes or ad-hoc scripts for creating and managing snapshots,
 leading to inconsistent backup coverage, potential data loss,
 and inefficient use of storage resources.

**Benefits of establishing this best
 practice:**

- By systematically managing EBS volumes and snapshots, you can
 significantly reduce storage costs by removing unused resources
 and efficiently tiering snapshots based on access needs.
- Regular lifecycle management ensures that your backup strategy
 is consistent and up-to-date, reducing the risk of data loss and
 maintaining appropriate retention periods for compliance and
 disaster recovery purposes.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

To effectively control EBS volume and snapshot lifecycles, start
 by implementing automated tools such as AWS Data Lifecycle
 Manager. Configure policies to regularly identify and delete
 unattached volumes, create consistent snapshot schedules, and
 manage snapshot retention across appropriate storage tiers. Use
 tags to categorize resources and enable granular control.
 Regularly review and adjust your policies to ensure they align
 with changing business needs and cost optimization goals.
 Implement monitoring and alerting to track resource usage and
 potential cost savings opportunities.

### Implementation steps

1. Set up AWS Data Lifecycle Manager policies to automate
 snapshot creation and deletion based on defined schedules
 and retention rules.
2. Implement a tagging strategy to categorize EBS volumes and
 snapshots, enabling easier management and cost allocation.
3. Create an automated process to identify and alert on
 unattached EBS volumes, with an option to delete them after
 a specified period.
4. Establish a tiering policy to move infrequently accessed
 snapshots from Standard to Archive tier after a set duration
 to optimize storage costs.

## Resources

**Related documents:**

- [Modify
 Amazon EBS snapshots](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-ebs-snapshots.html)
- [Delete
 unattached Amazon EBS volumes](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-delete-ebs-volumes.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost05-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
