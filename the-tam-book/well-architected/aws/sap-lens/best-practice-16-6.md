<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-16-6.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best Practice 16.6 – Develop mechanisms for simulating production load for analysis purposes

Having a clone of production data in a test system allows system administrators to
 simulate production SAP workloads and conduct vital performance tests, such as stress and
 volume testing. This type of testing can help identify potential performance bottlenecks
 and prevent performance issues from occurring in a live production environment.

**Suggestion 16.6.1 – Define performance sensitive activities**

Evaluate which transactions, reports, and operational activities could have an impact on
 your business if they do not meet peak load requirements or time-critical thresholds. For
 example, an overnight batch job which must complete in five hours, or a customer-facing
 transaction accessed concurrently by thousands of users during a quarterly business peak.
 Document and agree on the measurement approach, KPIs, and success criteria for these
 workload activities.

**Suggestion 16.6.2 – Create an automated test approach for key
 activities**

If required, develop a test strategy to confirm that your SAP workload performance
 benchmarks are met. Evaluate how test landscapes and tools can enable a repeatable suite of
 tests to measure the impact of operational activities, change releases and major patching on
 the performance of your workload.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-16-6.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
