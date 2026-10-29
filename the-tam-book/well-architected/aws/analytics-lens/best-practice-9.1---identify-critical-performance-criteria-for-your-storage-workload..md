<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-9.1---identify-critical-performance-criteria-for-your-storage-workload..html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best practice 9.1 – Identify critical performance criteria for your storage workload

In data analytics, throughput is often a constraining
 factor to enable your workloads to run effectively.
 Throughput is measured by the amount of information that has
 successfully moved through the network, compute, or storage
 layers. Improving throughput in each of these layers
 generally results in better query performance.

## Suggestion 9.1.1 – Use performance monitoring tools to determine if the analytics system performance is limited by compute, storage, or networking

Use a metric collection and reporting system, such as
 Amazon CloudWatch, to analyze the performance
 characteristics of the analytics system. Evaluate the
 measured performance metrics relative to system reference
 documentation to characterize the system constraints for
 the workload as a percentage of maximum performance.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-9.1---identify-critical-performance-criteria-for-your-storage-workload..html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
