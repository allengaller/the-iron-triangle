<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDACOST02-BP04 Implement manufacturing-specific data retention policies

Implement cost-effective industrial data management that balances retention requirements
 for production data, quality records, and compliance needs with optimized storage costs. This
 includes implementing tiered storage strategies and automated archival processes.

**Desired outcome:** Cost-effective industrial data management
 that balances retention requirements for production data, quality records, and compliance
 needs with optimized storage costs.

**Common anti-patterns:**

- Applying generic IT data retention policies to manufacturing data
- Failing to differentiate between operational data and long-term quality records
- Overlooking industry-specific regulations (for example, FDA, ISO) in retention
 policies
- Storing manufacturing data indefinitely without a defined purpose
- Not considering data dependencies in retention schedules (for example, keeping raw
 data but deleting related metadata)
- Implementing retention policies without input from production and quality teams

**Benefits of establishing this best practice:**

- Alignment with regulatory requirements
- Optimized storage costs
- Clear data lifecycle management
- Reduced risk of compliance violations

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Implement comprehensive data retention policies that store manufacturing data only as
 long as necessary for operational, regulatory, and business purposes while optimizing
 storage costs.

### Implementation steps

1. Document regulatory requirements.
2. Define data classification schemes.
3. Create retention schedules.
4. Implement automated archival processes.
5. Set up compliance monitoring.
6. Regular policy review and updates.

## Key AWS services

- Amazon S3 Lifecycle policies
- Amazon Glacier
- AWS Backup
- AWS Storage Gateway
- Amazon Macie
- AWS CloudTrail

## Resources

**Related documents:**

- [Amazon Simple Storage Service: Managing the lifecycle of
 objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)
- [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
