<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsec08-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCSEC08-BP01 Implement backups to enable recovery from data corruption and data deletion, as well as point-in-time views of data

Configure backups to be taken automatically based on a periodic
 schedule informed by the Recovery Point Objective (RPO), or by
 changes in the dataset. Critical datasets with low data loss
 requirements need to be backed up automatically on a frequent
 basis, whereas less critical data where some loss is acceptable
 can be backed up less frequently.

**Desired outcome:** Successful
 periodic test results of ability to recover data.

**Common anti-patterns:**

- Failing to fully test if your data backup and recovery
 procedures are functional

**Benefits of establishing this best
 practice:** Helps you detect and fix backup and recovery
 misconfigurations if they occur.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

- Configure Amazon EBS snapshots. If your compliance
 requirements allow backups to be stored in-Region, that can
 be a lower cost option. Otherwise, configure Amazon EBS
 local snapshots on Outposts, or implement a third-party
 backup solution.
For implementations details, see
 [Amazon Elastic Block Store Local Snapshots on AWS Outposts](https://aws.amazon.com/blogs/aws/new-amazon-elastic-block-store-local-snapshots-on-aws-outposts/) and
 [Amazon EBS local snapshots on Outposts](https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html).
- Enable
 [S3
 Versioning on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsManagingVersioning.html) to preserve, retrieve, and
 restore every version of every object stored in your S3
 buckets on Outposts.
- Enable
 [S3
 Replication on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsReplication.html) to replicate the Amazon S3
 objects to another Outpost or even another bucket on the
 same Outpost. If copies of data may be stored in-Region,
 then configure
 [AWS Datasync](https://aws.amazon.com/blogs/storage/automate-data-synchronization-between-aws-outposts-racks-and-amazon-s3-with-aws-datasync/) to replicate the data to the S3 bucket in
 the Region.
- Perform capacity planning, and periodically review your
 plans to reduce risk of running out of capacity within S3
 Outposts.
- Third-party backup solutions are available from
 [AWS Partners who have tested their solutions on Outposts](https://partners.amazonaws.com/search/partners/?facets=Product%20%3A%20AWS%20Outposts&keyword=Backup&page=1).
- Periodically test your ability to fully recover data,
 including from specific points in time.

## Resources

**Related best practices:**

- [REL09-BP03
 Perform data backup automatically](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_automated_backups_data.html)
- [Incident
 Response](https://docs.aws.amazon.com/wellarchitected/latest/framework/a-incident-response.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsec08-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
