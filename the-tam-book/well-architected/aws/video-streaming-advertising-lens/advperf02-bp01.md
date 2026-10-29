<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf02-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVPERF02-BP01 Evaluate compute benchmarks and compute options certified by the ISVs if applicable

Evaluate ISV compatibility for running on AWS, and use the right resources based on
 published benchmarking results.

## Implementation guidance

Aerospike's ISV product has been observed to be deployed for
 high-volume customer adtech workloads due to its speed at scale,
 real-time analytics capabilities, and strong data protection.

Databricks is a popular ISV platform used for advertising
 workloads due to its capabilities in big data processing,
 real-time capabilities and machine learning support. These
 facets make it well-suited for the large-scale and fast-changing
 needs of advertising analytics and intelligence.

Consider benchmark evaluation for
 [Amazon EC2](https://aws.amazon.com/ec2/)
 Intel and Graviton instances for Aerospike and Databricks.

## Resources

**Related documentation:**

- [Running
 Ad Tech Workloads on AWS with Aerospike at Petabyte Scale](https://aws.amazon.com/blogs/industries/running-ad-tech-workloads-on-aws-with-aerospike-at-petabyte-scale/)

**Related partner solutions:**

- [Database comparisons and performance benchmarks (Aerospike)](https://aerospike.com/resources/benchmarks/)
- [Running
 operational workloads with Aerospike at petabyte scale in the cloud on 20 nodes](https://aerospike.com/resources/white-papers/running-operational-workloads/)
- Introducing the Well-Architected Data Lakehouse from
 Databricks[6 Guiding Principles to Build an Effective Data Lakehouse](https://www.databricks.com/blog/2022/07/14/6-guiding-principles-to-build-an-effective-data-lakehouse.html)
- [Best
 Practices for Cost Management on Databricks](https://www.databricks.com/blog/best-practices-cost-management-databricks)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
