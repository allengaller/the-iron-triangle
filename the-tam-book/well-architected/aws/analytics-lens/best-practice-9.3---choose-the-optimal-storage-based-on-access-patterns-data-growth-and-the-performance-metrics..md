<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-9.3---choose-the-optimal-storage-based-on-access-patterns-data-growth-and-the-performance-metrics..html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best practice 9.3 – Choose the optimal storage based on access patterns, data growth, and the performance requirements

Storage options for data analytics can have performance
 tradeoffs based on access patterns and data size. For
 example, in Amazon S3, can be much more efficient to retrieve a smaller number of larger objects, as opposed to a larger number of smaller objects.

Evaluate your workload needs and usage patterns
 to determine if the method or location of storing your data
 can improve the overall efficiency of your solution.

## Suggestion 9.3.1 – Identify available solution options for the performance improvement

When data I/O is limiting performance and business
 requirements are not being met, improve I/O through the
 options available within that service. For example, with
 EBS volumes of GP3 type, increase Provisioned IOPS or
 throughput, or for Amazon Redshift, increase the number of
 nodes.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-9.3---choose-the-optimal-storage-based-on-access-patterns-data-growth-and-the-performance-metrics..html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
