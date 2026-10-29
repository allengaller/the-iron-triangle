<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/storage-architecture.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Storage architecture

Healthcare requirements for compute are generally consistent
 with other industries. Guidance from the
 [Well-Architected
 Framework Storage Architecture Selection](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-storage.html) still applies.

AWS offers storage with extreme durability and performance.
 For example, [Amazon S3](https://aws.amazon.com/s3)
 provides 99.999999999% (11 nines) of data durability of objects
 over a given year.
 [Amazon EBS io2](https://aws.amazon.com/ebs/provisioned-iops/) block storage offers not only 99.999%
 durability, but up to 500 IOPS per GiB, enabling high
 performance and durability for healthcare workloads that
 require higher performance, such as transactional databases.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/storage-architecture.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
