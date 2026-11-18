<!-- source: https://docs.cloud.google.com/architecture/framework/reliability/observability -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Detect potential failures by using observability

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](/architecture/framework) 
provides recommendations to help you proactively identify areas where errors and
failures might occur.

This principle is relevant to the *observation*
[focus area](/architecture/framework/reliability#focus-areas) 
of reliability.

## Principle overview

To maintain and improve the reliability of your workloads in
Google Cloud, you need to implement effective observability by using
metrics, logs, and traces.

- Metrics are numerical measurements of activities that you want to track
for your application at specific time intervals. For example, you might
want to track technical metrics like request rate and error rate, which can
be used as service-level indicators (SLIs). You might also need to track
application-specific business metrics like orders placed and payments received.
- Logs are time-stamped records of discrete events that occur within an
application or system. The event could be a failure, an error, or a change
in state. Logs might include metrics, and you can also use logs for SLIs.
- A trace represents the journey of a single user or transaction through a
number of separate applications or the components of an application. For
example, these components could be microservices. Traces help you to track
what components were used in the journeys, where bottlenecks exist, and how
long the journeys took.

Metrics, logs, and traces help you monitor your system continuously.
Comprehensive monitoring helps you find out where and why errors occurred. You
can also detect potential failures before errors occur.

## Recommendations

To detect potential failures efficiently, consider the recommendations in the
following subsections.

### Gain comprehensive insights

To track key metrics like response times and error rates, use
[Cloud Monitoring](/monitoring/docs/monitoring-overview) 
and
[Cloud Logging](/logging/docs/overview).
These tools also help you to ensure that the metrics consistently meet the needs
of your workload.

To make data-driven decisions, analyze default service metrics to understand
component dependencies and their impact on overall workload performance.

To customize your monitoring strategy, create and publish your own metrics by
using the Google Cloud SDK.

### Perform proactive troubleshooting

Implement robust error handling and enable logging across all of the components
of your workloads in Google Cloud. Activate logs like
[Cloud Storage access logs](/storage/docs/access-logs) 
and
[VPC Flow Logs](/vpc/docs/flow-logs).

When you configure logging, consider the associated
[costs](https://cloud.google.com/products/observability/pricing#logging-pricing-summary).
To control logging costs, you can configure
[exclusion filters](/logging/docs/routing/overview#exclusions) 
on the log sinks to exclude certain logs from being stored.

### Optimize resource utilization

Monitor CPU consumption, network I/O metrics, and disk I/O metrics to detect
under-provisioned and over-provisioned resources in services like
GKE, Compute Engine, and Managed Service for Apache Spark. For a
complete list of supported services, see
[Cloud Monitoring overview](/monitoring/docs/monitoring-overview).

### Prioritize alerts

For alerts, focus on critical metrics, set appropriate thresholds to minimize
alert fatigue, and ensure timely responses to significant issues. This targeted
approach lets you proactively maintain workload reliability. For more
information, see
[Alerting overview](/monitoring/alerts).

---

> 原页面：https://docs.cloud.google.com/architecture/framework/reliability/observability（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
