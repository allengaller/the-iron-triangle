<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/metrics-for-data-ingestion-and-processing.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Metrics for data ingestion and processing

- **Data ingestion rate**:
 The amount of data ingested by monitoring systems in a
 given time period which indicates that the system can
 effectively process large volumes of telemetry data,
 leading to more accurate insights. Measure this metric by
 calculating the volume of data ingested by the monitoring
 systems per unit of time.
- **Data processing
 latency**: The time it takes for telemetry data
 to be processed and made available for analysis. Lower
 data processing latency aims to quickly assess and act on
 insights from telemetry data. Measure the time elapsed
 between data ingestion and the availability of processed
 data for analysis.
- **Data cost efficiency**:
 Measuring the cost of collecting, storing, and processing
 telemetry data compared to the number of actionable
 insights generated or decisions made based on these
 insights. This metric assures that resources are utilized
 effectively and unnecessary expenses are minimized.
 Calculate the total cost of data collection, storage, and
 processing, and contrast it to the actionable insights
 they provide.
- **Anomaly detection rate**:
 The percentage of anomalies detected by the monitoring
 systems. A higher anomaly detection rate indicates that
 the system is effective in identifying potential issues,
 enabling teams to proactively address them. Measure this
 metric by calculating the number of anomalies detected by
 the monitoring systems, divided by the total number of
 events, then multiply by 100 for the percentage.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/metrics-for-data-ingestion-and-processing.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
