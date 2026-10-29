<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Data protection

A DMP solution often collects multiple forms of data from
 customers, advertising solutions, DSPs, and SSPs to transform
 raw data and provide insights to different portions of a
 cloud-based advertising workload. Protecting DMPs usually
 requires robust security measures for the different parts of the
 pipeline that ingest and transform data. Consider using Amazon
 S3 as a centralized data store. Amazon S3 is an object storage
 service that can securely store data for a range of use cases.
 For data protection, strict S3 bucket policies should be
 implemented that enforce encryption of data at rest and define
 strict access controls.

An enhanced layer of protection would be to enforce the use of
 service-side encryption (SSE) with an AWS KMS-managed key
 (SSE-KMS) which can assist in protecting the data but also meet
 potential compliance requirements. SSE-KMS allows you to
 maintain the ownership of the keys with the ability to revoke
 access depending on the job requirements to the data. By
 implementing SSE-KMS you have a defense in depth strategy as the
 consumer of the data needs access to the data on S3 and
 permission to use the KMS key to decrypt it. A combination of
 these features verify data is protected at rest.

###### Best practices

- [ADVSEC04-BP01 Implement secure data collaboration with least privileged access and privacy controls](./advsec04-bp01.html)
- [Key AWS services](#key-aws-services-5)
- [Resources](#resources-10)

## Key AWS services

- [AWS S3](https://aws.amazon.com/pm/serv-s3/)
- [AWS KMS](https://aws.amazon.com/kms/)

## Resources

- [Using server-side encryption with AWS KMS keys (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)
- [Bucket policies for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
