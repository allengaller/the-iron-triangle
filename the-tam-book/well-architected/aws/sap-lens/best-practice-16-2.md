<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-16-2.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best Practice 16.2 – Establish baseline performance requirements

Every SAP application has unique performance requirements. Using historical monitoring
 data helps SAP administration teams understand the baseline performance of these
 applications, enabling them to identify and understand the extent of any performance
 changes. Relevant alerts can be put in place to detect anomalies, such as unintended CPU
 spikes, storage throughput deltas, memory consumption increases, and more complex
 performance decrements. This monitoring data can be used to further fine-tune
 performance.

**Suggestion 16.2.1 – Collect and evaluate data that reflects
 SAP-specific KPIs**

This suggestion aligns closely with additional suggestions in the Well-Architected
 Framework Performance Efficiency Pillar discussion regarding [resource monitoring](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/monitor-your-resources-to-ensure-that-they-are-performing-as-expected.html).

In addition to this general guidance, SAP-specific KPIs include dialog response time,
 buffer swaps, used memory. These KPIs might differ based on the type of SAP software and
 version you are running on. Further detail on KPI and monitoring recommendations is
 available in this document in the Operational Excellence pillar:

- SAP Lens [Operational Excellence]: [Best
 Practice 1.2 - Implement infrastructure monitoring for SAP](./best-practice-1-2.html)
- SAP Lens [Operational Excellence]: [Best
 Practice 1.3 - Implement application and database monitoring for SAP](./best-practice-1-3.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-16-2.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
