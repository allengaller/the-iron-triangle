<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhccost04-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCCOST04-BP01 Implement mechanisms to manage the lifecycle of Amazon S3 data, EBS volumes, and snapshots

Apply data lifecycle management practices to hybrid edge
 environments.

**Desired outcome:** You can
 implement familiar mechanisms like you would in-Region to manage
 the lifecycle of your hybrid edge data.

**Benefits of establishing this best
 practice:** Through the use of familiar mechanisms, you
 can retain relevant data.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

Outposts contain fixed capacity specific to their configuration.
 You can manage the lifecycle of your data with familiar services
 such as
 [S3
 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsLifecycleManaging.html) for Amazon S3 on Outposts and
 [Data
 Lifecycle Manager](https://aws.amazon.com/about-aws/whats-new/2021/02/introducing-amazon-ebs-local-snapshots-on-outposts/) for Amazon EBS.
 Consider [archiving
 Amazon S3 content to AWS Regions using DataSync](https://aws.amazon.com/blogs/storage/automate-data-synchronization-between-aws-outposts-racks-and-amazon-s3-with-aws-datasync/) if
 possible.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhccost04-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
