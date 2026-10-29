<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDACOST02-BP02 Implement manufacturing-aware resource decommissioning process

Systematically remove unused resources while preserving critical manufacturing data,
 maintaining production system integrity, and complying with industrial requirements. This
 involves careful consideration of dependencies between manufacturing systems, data retention
 requirements, and proper archival procedures before resource removal.

**Desired outcome:** Systematic removal of unused resources
 while preserving critical manufacturing data, maintaining production system integrity, and
 complying with industrial requirements.

**Common anti-patterns:**

- Decommissioning resources without checking their connection to active production
 lines
- Failing to preserve quality control and compliance data before resource removal
- Not considering seasonal manufacturing patterns when identifying unused resources
- Decommissioning without checking impact on OT or IT integrated systems
- Removing resources without validating manufacturing regulatory requirements
- Failing to archive production performance data and custom configuration settings
 before decommissioning
- Not considering maintenance and repair history requirements

**Benefits of establishing this Best Practice:**

- Reduced costs from unnecessary resource retention
- Minimized risk of accidental data loss
- Clear process for resource retirement
- Compliance with data governance requirements

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Establish formal processes for identifying and safely decommissioning resources in your
 manufacturing setup that are no longer needed, while meeting data preservation requirements
 and managing dependencies.

### Implementation steps

1. Create decommissioning criteria based on:
Resource utilization thresholdsBusiness value assessmentData retention requirements
2. Establish approval workflows.
3. Document dependencies and impact analysis.
4. Create backup and archival procedures.
5. Implement verification steps post-decommissioning.
6. Consider manufacturing-specific decommissioning criteria:
Production line changeoversEnd of product lifecycleEquipment replacement cyclesHistorical data retention for quality compliance and machine learning

## Key AWS services

- AWS Backup
- Amazon S3 Lifecycle policies
- AWS Organizations
- Amazon CloudWatch
- AWS Glue Data Catalog

## Resources

**Related documents:**

- [Amazon Simple Storage Service: Examples of S3 Lifecycle configurations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html)
- [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [Detecting unusual spend with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
