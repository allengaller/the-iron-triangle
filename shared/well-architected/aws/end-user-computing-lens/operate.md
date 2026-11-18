<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/operate.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Operate

Observability helps you focus on meaningful data and understand your workload's
 interactions and output. By concentrating on essential insights and removing unnecessary data,
 you maintain a straightforward approach to understanding workload performance. It is essential
 not only to collect data but also to interpret it correctly. Define clear baselines, set
 appropriate alert thresholds, and actively monitor for any deviations. A shift in a key
 metric, especially when correlated with other data, can pinpoint specific problem areas.

Agreeing on the metrics which are key to identifying service health help to verify
 adherence to service level agreements which have been agreed upon by the business, third
 parties or customers.

Following the identification of service degradation, quickly identifying the root cause
 and best method of remediation will be critical. Different user personas and application sets
 will likely have different priorities that must be dealt with based on their impact on the
 business.

To identify trends that can be used to improve service delivery and maintain a consistent
 user experience, establish an agreed cadence for reviewing data that identifies how your AWS
 EUC services are performing over time.

While AWS EUC-focused logs can expose issues specific to these services, access to data
 from other contingent services (like networking, authentication, storage, or backend services)
 provides a broader view of the cause and effect of cross-service outages.

###### Best practices

- [EUCOPS11-BP01 Create EUC health metrics that allow you to meet your operational goals](./eucops11-bp01.html)
- [EUCOPS12-BP01 Deploy alerting mechanisms that quickly identify anomalous metrics](./eucops12-bp01.html)
- [EUCOPS12-BP02 Define and maintain an alerting chain of command that quickly communicates issues in real time](./eucops12-bp02.html)
- [EUCOPS13-BP01 Perform regular service reviews to identify significant trends in performance, scalability, and availability](./eucops13-bp01.html)
- [EUCOPS14-BP01 Ingest log file data from multiple data sources to correlate key problem identifiers and trends](./eucops14-bp01.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/operate.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
