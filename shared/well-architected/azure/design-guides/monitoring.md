<!-- source: https://learn.microsoft.com/en-us/azure/well-architected/design-guides/monitoring -->
<!-- captured: 2026-10-25 -->
<!-- vendor: azure -->

# How to build a monitoring system for Azure workloads

Note




Monitoring is the mindful practice of collecting and analyzing telemetry to understand system health and behavior. Its purpose is to make the state of a system observable through measurement, connecting technical signals to operational outcomes. Proper monitoring allows teams to detect anomalies, investigate failures, and make informed decisions.

As a cloud solution architect, treat monitoring as a core architectural capability, and design it alongside the functional stack rather than later. Think of it as its own system, with a dedicated stack and data flows, that observes functional stack: infrastructure, application health, and build and release processes. As the workload grows, also evolve monitoring practices from simple metrics to cross-service correlation and structured analysis.

Typically, a monitoring flow follows a linear progression and can be divided into four logical phases, each building on the insights of the previous one.

This guide explores the process of building those phases and provides best practices. It doesn't cover specialized monitoring use cases like security. The guidance builds on the key strategies outlined in [OE:07 Architecture strategies for designing a monitoring system](../operational-excellence/observability), which you should review first.

## Terminology

| Term | Definition |
| --- | --- |
| **Activity ID** | A unique identifier assigned to each request and propagated across services, threads, queues, and dependencies to enable correlation of related telemetry data. |
| **Activity logs** | Platform logs that track subscription-level operations such as resource creation, updates, and deletions. |
| **Aggregation** | The process of combining and consolidating telemetry data from multiple sources to create meaningful insights and reduce storage footprint. |
| **APM (Application Performance Management)** | Tools that automatically capture telemetry from applications, including request rates, failure rates, dependency duration, and distributed traces. |
| **Cold analysis** | Analysis that works with large volumes of historical telemetry data and usually runs on a scheduled or ad-hoc basis. This is useful for identifying trends over a long period. |
| **Distributed tracing** | A technique for tracking requests across multiple services or machines in distributed systems, using unique activity IDs propagated across components. |
| **Hot analysis** | Analysis that processes telemetry immediately after it is generated. This path is used when rapid detection and response are critical. |
| **Instrumentation** | The process of embedding code or tools in your source to generate operational signals called telemetry. |
| **Logs** | Timestamped records of discrete events that capture what happened in a system at specific points in time. |
| **Metrics** | Numerical measurements of a system or resource at a specific point in time, often accompanied by one or more tags or dimensions. When captured continuously over time, they reveal trends, patterns, and anomalies. |
| **Monitoring** | The mindful practice of collecting and analyzing telemetry to understand system health and behavior. Makes the state of a system observable through measurement, connecting technical signals to operational outcomes. |
| **Resource logs** | Platform logs that capture resource-specific events, such as storage access logs or firewall events. |
| **Sampling** | A technique to reduce telemetry volume and costs by collecting only a representative subset of data while maintaining sufficient insight for analysis. |
| **Telemetry** | Operational signals generated from systems, referring to logs, traces, and metrics that provide insight into system behavior and performance. |
| **Traces** | Records that track request paths across components, showing how a request flows through distributed systems. |
| **Warm analysis** | Analysis that occurs after telemetry is collected and lightly aggregated. It usually involves correlating multiple telemetry sources to understand why something happened. |

## Phase 1 - Instrumentation

*Instrumentation* is the process of embedding code or tools in your source to generate operational signals called *telemetry*. This refers to logs, traces, and metrics. *Logs* are timestamped records of discrete events, while *traces* record request paths across components. *Metrics* are numerical measurements of a system or resource at a specific point in time, often accompanied by one or more tags or dimensions. Unlike logs or traces, a single metric on its own provides limited insight; metrics help you monitor health and when captured continuously over time to reveal trends, patterns, and anomalies.

Start by deciding *what to track from the system*. Think about the layers of the system and what information can help decision making during analysis:

- **Application logic**. Capture the flow of incoming requests like, their start times, durations, and status codes. Pay attention to the information emitted in exceptions and failures. These are often useful in uncovering patterns and root causes. Also, track meaningful business events. For example, in an eCommerce workload, orders placed, payments processed, or messages handled.
- **External dependencies**. Track communication with external dependencies like calls to databases, web services, and infrastructure components. Include their duration, status, retries, and errors.

There are also platform and runtime components that generate telemetry. Because you aren't accountable for their source, you can only enable collection of that data. This includes components like frameworks, operating system, Azure resources.

#### Best practices for instrumentation

When adding instrumentation, follow these simple principles: Maintain consistency, provide sufficient context, and structure information for ease of analysis in later phases.

- **Choose technology that's language-agnostic and can integrate with multiple monitoring platforms**. OpenTelemetry is a vendor-neutral option that's adopted by a lot of applications.
- **Record all relevant context consistently**. Include information about source component, environment, deployment, activity ID, user info, and dependency data. For example, timestamps should be recorded at the moment a log entry is created and formatted in a consistent, standardized way. All telemetry data should use Coordinated Universal Time (UTC) to ensure events can be accurately correlated across services, regions, and systems.
- **Use structured telemetry**, which is recorded in both human- and machine-readable formats (JSON, MessagePack, Protobuf).
- **Make log verbosity configurable** because verbose logging can incur significant costs. Also, it can lead to noise making querying and filtering challenging. One strategy could be to set log levels according to the environment. Increase verbosity in lower environments, and pull back on verbosity in production. Another strategy is to align verbosity with the criticality of the component.
- **Categorize by operational concern** to make filtering and analysis more efficient. For example, indicate purpose in telemetry data whether it's for audit, security, debugging, or performance.
- **Enable correlation**. Distributed tracing is particularly valuable in systems where requests traverse multiple services or machines. Assign a unique activity ID to each request and propagate it across services, threads, queues, dependencies. Correlation must rely on identifiers and context, not timestamps alone.

#### Example: Instrumentation

Consider an ecommerce application. When a customer places an order, a business transaction begins. The API processes the payment, the database records the order, and a confirmation email is sent. When the system works as expected, everything completes within the expected timeframe. But suppose something breaks.

Without instrumentation, you might only see: "Checkout failed." There's no context, no clear cause, while the user experience quietly deteriorates. Troubleshooting becomes guesswork. Is the database down? Did the email service time-out? Is the payment provider experiencing issues?

With proper instrumentation, the request is tracked end-to-end across every component. Logs reveal that the payment API returned a 500 error. A distributed trace shows latency spiking specifically within the payment service. Metrics confirm that the checkout failure rate has climbed from 1% to 8% in 10 minutes. That makes diagnosis systematic and data-driven rather than speculative.

## Phase 2 - Telemetry data collection and storage

While instrumentation is about what operational signals should be tracked, this phase is about *where to route the telemetry data* and manage it responsibly.

It's common to use data collection services or monitoring agents that pull data and write the information directly to common storage.

Or, the agents can act as a passive receiver that waits for the data to be sent from the application.

Telemetry usually comes from these sources:

- **Application-level telemetry**. After the application is instrumented by using SDKs or standards like OpenTelemetry, telemetry data can be pulled automatically using Application Performance Management (APM) tool, such as [Azure Application Insights](../service-guides/application-insights). It will automatically capture custom business metrics like **OrderPlaced** and **NewUserProfileCreated**, and diagnostics data like application exceptions, dependency duration, and distributed traces. Then, that data is ingested into Azure Monitor Logs for analysis. Application Insights gives you the ability to control data retention periods, configure sampling, and manage certain privacy settings.
- **Application host telemetry**. Application hosts emit several categories of telemetry. These signals help monitor the behavior of the application platform, like request rate, request queue length, response time, dependency call count, and HTTP status code distribution. Application Insights is well-integrated with most Azure application hosting services like Azure Functions, App Service, and Virtual Machines.
- **Platform logs**. There's telemetry generated from the other infrastructure that the application runs on. In Azure, that's mainly *activity logs* and *resource logs*. Activity logs track subscription-level operations (resource creation, updates, deletes). Resource logs that capture resource-specific events, like storage access logs, firewall events.
Enable Diagnostic settings for each resource and route logs to a storage solution.
Platform log collection requires explicit configuration. For example, Azure Monitor Agent. When installed on the VMs, it pulls local logs and delivers them to Azure Monitor, Microsoft Sentinel, and Microsoft Defender for Cloud.

#### Telemetry data storage decision

Data storage should be chosen based on how you plan to use it. For instance, there might be a need for quick analysis of some telemetry data so that the results can be sent directly to the visualization and alerting subsystem (hot analysis). And so, storage for the hot tier should be able to do real-time processing. Alternatively, data that's subjected to warm or cold analysis is held in storage while it awaits processing.

Create a matrix that clearly highlights the use case, requirements, and technology choices. Here's an example:

| Use Case | Recommended storage |
| --- | --- |
| Interactive querying and troubleshooting | [Azure Log Analytics](../service-guides/azure-log-analytics) |
| Real-time analytics | [Azure Databricks](../service-guides/azure-databricks) |
| Long-term archival | [Azure Blob Storage](../service-guides/azure-blob-storage) |
| SIEM or security integration | [Event Hubs](../service-guides/azure-event-hubs) |
| Aggregation and analysis for exploring trends and advanced analytics | [Azure Data Explorer](/en-us/azure/data-explorer) |

In some cases, you might send the same telemetry to multiple destinations for different purposes.

#### Telemetry performance and reliability considerations

A single application can generate massive volumes of telemetry from multiple web and worker roles, database shards, and supporting Azure services. Sending all of this data to a single central store can quickly overwhelm available I/O bandwidth and create a bottleneck. The monitoring system must scale with the system to make sure critical data isn't lost. A practical way to achieve this is by introducing queuing.

In this architecture, a monitoring agent publishes telemetry data to a queue. A separate, asynchronous process, such as a storage writing service, consumes messages from the queue and writes them to shared storage.

Using a message queue is recommended because it provides *at-least-once* delivery semantics, helping ensure that telemetry data is not lost after it is submitted. The storage writing service can run as an independent worker role, allowing ingestion and storage to scale independently and preventing the monitoring pipeline from becoming a system bottleneck.

#### Telemetry data lifecycle management

Not all telemetry needs to live forever. Be clear on how long you want to retain based on the use of the data. For example, raw debugging data may only require short-term retention, whereas performance metrics, historical trends, or auditing records may need long-term storage.

> **Tradeoff**: Telemetry data can grow significantly even within a short period of time. Set clear retention policies so that you keep the data that truly matters while letting go of what doesn't. Like spot trends, anticipate capacity issues within the right time window. At the same time, you avoid paying for storage you don't really need.

In addition to retention policies that archive older data to lower-cost storage, there are other techniques to optimize costs. Where appropriate, down-sample it to reduce storage usage while preserving sufficient resolution for analysis. Aggregate related events to reduce storage footprint and process data faster.

#### Telemetry data security

While telemetry isn't workload functional data, it's still critical from an operational perspective. From a security point: protect data against accidental deletion; control access with role-based access control (RBAC). Consider the use of:

- Enable soft delete to allow recovery within a defined period. Most Azure storage services offer soft delete. Refer to product documentation for details on the service you've chosen for your workload.
- Apply [resource locks](/en-us/azure/azure-resource-manager/management/lock-resources) to prevent unintended changes or deletions to important resources.
- Sensitive data must be encrypted and scrubbed of personally identifiable information. If your workload needs to store telemetry for regulatory purposes, follow the governance policies according to those compliance requirements.

## Phase 3 - Correlation, aggregation, analysis

Once telemetry is collected and stored, the next step is to turn raw data (logs, metrics, and traces) into insight. The outcome of this phase is to understand *what does the data mean and how to ensure the right people can act on them?*

Analyzing telemetry begins by structuring data around defined KPIs and performance metrics. Start by asking these questions:

- Are users experiencing failures?
- Is performance degrading?
- Are dependencies slowing down?
- Is capacity reaching limits?
- Are business KPIs trending negatively?

To reach conclusive results, this phase involves complex queries and reporting checking against target metrics.

To prepare data for analysis, a common step is to **aggregate data from multiple sources**. For example, for distributed tracing, aggregation involves combining events with the same activity or transaction ID. Data preparation is another task during aggregation. Here, duplicates are removed, and irrelevant data is filtered out.

#### Correlation

Correlation is the process of **linking telemetry data from multiple system layers** to understand what is happening across the entire application environment. While individual logs, metrics, or traces provide snapshots of activity, correlation connects these pieces together to reveal cause-and-effect relationships.

Correlation is also important for diagnosing failures. An exception in a lower-level component (such as a database or infrastructure service) can propagate upward and cause application-level errors.

To support effective correlation, telemetry data must include sufficient context, such as: activity IDs or correlation IDs, Timestamps in universal format, and service or component identifiers. Make sure that information is included during instrumentation.

#### Supporting hot, warm, and cold analysis

Not all telemetry data is analyzed with the same urgency. Evaluate which flows need hot, warm, and cold analysis paths, which determine how quickly data must be processed and how it is stored.

- **Hot analysis (real-time)**
Hot analysis processes telemetry immediately after it is generated. This path is used when rapid detection and response are critical. Because these scenarios are time-sensitive, data must be available instantly. The storage technology must support fast indexing and querying. Sometimes analysis runs close to where the data is produced to reduce latency.
Typical use cases include alerting systems, especially for security monitoring where detect and response must be done as soon as possible.
- **Warm analysis (near-real-time investigation)**
Warm analysis occurs after telemetry is collected and lightly aggregated. It usually involves correlating multiple telemetry sources to understand why something happened.
This analysis requires aggregation of multiple events, correlation, and statistical analysis across a group of events.
It's common to use warm analysis for performance analysis and operational troubleshooting.
- **Cold analysis (historical long-term data)**
Cold analysis works with large volumes of historical telemetry data and usually runs on a scheduled or ad-hoc basis. This is useful for identifying trends over a long period.

#### Best practices for alerts

Analysis can also generate alerts to notify you when action is needed. Here are some best practices:

- Define thresholds based on historical data.
- Include sufficient context and filter out false alarms.
- Integrate with automated workflows like your support ticketing. systems, auto-remediation, scaling actions.
- Assign ownership to the responsible team.
- Set prioritization indicators like severity, which separate critical issues from informational notifications.
- Use a health model that aggregates multiple correlated signals into health states, then alert on state transitions, not isolated metric thresholds.

#### Example: Correlation, aggregation, analysis

Let's continue with the eCommerce example. By using hot analysis, it was detecting that the checkout failure rate increased from 1% to 8% within 10 minutes, the team began investigating by correlating telemetry across multiple sources.

They first queried the application logs and filtered them to the relevant time window, confirming an increase in request timeout exceptions. By grouping the results by dependency, they identified that the spike in failures occurred in requests that relied on the database. Then, queried the database request telemetry and confirmed that query latency had doubled, using correlation IDs to verify that the failing requests were directly affected by the increased latency.

Based on the collected metrics, they examined platform metrics during the same period and observed that the database server CPU utilization hit and remained at 90% for the time period, confirming that infrastructure-level database resource exhaustion was driving the request timeouts.

Warm analysis revealed that the cause was the dependency on the database, which was under heavy load, because:

- Application logs showed errors with timeout exceptions
- Database latency doubled during that time
- Platform logs showed that CPU on database server is at 90%

By retaining analysis data over time, teams performed cold historical analysis to uncover trends. For example, consistent increase in database load or gradually rising response times can indicate a change in architecture or optimization. For example, scaling the database or optimizing queries may be necessary.

## Phase 4 - Visualization

With analysis in place, the next step is to take action. *How do we make the insights visible?*

Visualization converts complex telemetry into actionable insights using dashboards, charts, and reports.

#### Best practices for visualization

- **Align with your health model and visualize components using a color scheme that reflects your service level objectives (SLOs) based on health signals**. For example, Healthy (green), Degraded (amber), and Unhealthy (red). Your health dashboards should have the capability of drill-down from system-level health to individual entities.

- **Prioritize the display of actionable data**. Avoid cluttering dashboards with non-critical details. Focus on information or trends that support decisions, such as environment, service, and region.
- **Support interactive exploration**. Allow filtering by time range, service, or deployment. Enable ad-hoc queries to investigate anomalies.
- Tailor dashboards for intended audience. For example,
Audience
View
Developers
Real-time logs, traces, error trends
Operators
KPIs, resource utilization, alerts
Business stakeholders
High-level metrics, revenue-impact KPIs
- Tailor dashboards for intended use. For example,
Use
View
Operational reports
Resource usage, trends, exceptions, efficiency
Security reports
Audit user actions, track anomalies for compliance
Business reports
KPI trends, revenue per user, transactions over time

#### Example: Visualization

Let's return to the eCommerce application. A developer oriented dashboard visualizes:

- Latency trends over the past 24 hours
- Failure rates by endpoint
- Database CPU usage
- Orders processed per minute

From this dashboard, a developer can narrow in investigations about failure spikes when database CPU exceeds 85%. Meanwhile when latency exceeds 2 seconds for the checkout user flow, developer sees request ID, database load, and recent errors. At this point, with sufficient testing an automated workflow is triggered that scales database tier.

## Monitoring antipatterns and how to avoid them

The following antipatterns commonly undermine what monitoring can do for workloads.

| Antipattern | Guidance |
| --- | --- |
| **Logging too little, or too much** - Missing contextual information required for troubleshooting. - Excessive verbosity creating noise, high ingestion costs, and slow queries. | Strive for high signal, low noise: - Define logging standards at design time. - Log structured data with consistent fields. - Include contextual fields such as: Correlation ID, User/tenant ID (when allowed), Operation name, Environment. - Use log levels properly (Debug, Info, Warning, Error). - Implement sampling for high-volume components. - Periodically review log usefulness and cost. |
| **Missing correlation across services** Correlation IDs are not propagated across services. Logs, metrics, and traces are analyzed in isolation. | Enable end-to-end traceability: - Generate at the entry point if not included in the request, propagate the provided one if included. - Adopt distributed tracing standards. - Ensure logs, metrics, and traces share common identifiers. - Correlate telemetry types during analysis. |
| **Ignoring business context** Monitoring is treated as purely technical and disconnected from business objectives. Only technical metrics (CPU, memory, latency) are emitted and analyzed. | Align monitoring to business value: - Define business KPIs alongside technical SLIs. - Instrument business events. - Build dashboards that show business KPIs with supporting technical indicators. - Align alerts severity with customer impact. |
| **Unconfigured or mismanaged telemetry** Logging is enabled without proper diagnostic configuration. All telemetry is stored in one place without purpose or categorization. | Design telemetry architecture intentionally: - Define telemetry categories (Operational, Security, Audit, Business). - Route data to appropriate stores based on usage. - Configure retention and indexing policies. - Regularly audit diagnostic settings. |
| **Poor data governance** Logs are considered harmless technical artifacts rather than regulated data. Raw telemetry is kept indefinitely. Sensitive data appears in logs. Retention and compliance are ignored. | Treat monitoring data as production data: - Define retention policies per data type. - Mask or avoid logging sensitive data (PII, secrets). - Enforce encryption in transit and at rest. - Automate lifecycle management aligned with compliance requirements. |
| **Ignoring monitoring costs** No planning for telemetry growth, ingestion volume, or storage expansion. | Plan for observability cost in your cost model: - Estimate telemetry volume during design. - Model ingestion and retention costs. - Apply sampling, aggregation, and tiered storage. - Regularly review cost versus value. |
| **Inconsistent and fragmented telemetry** Different teams emit logs in different schemas and naming conventions. Multiple disconnected tools are used. | Standardize observability practices: - Establish naming conventions and common schemas. - Define tagging taxonomy. - Provide shared logging libraries or SDKs. - Implement centralized governance and periodic reviews. |
| **Poorly designed dashboards** Dashboards are cluttered, overly complex, or not aligned with KPIs or system health model. | Design dashboards for decisions: - Define audience (Executive, Ops, Engineering). - Align to health model (Availability, Latency, Errors, Saturation). - Focus on clarity and actionable insights. - Remove decorative or redundant metrics. |
| **Alert fatigue** Too many alerts, no severity differentiation, no ownership, and alerts lack context. | Make alerts actionable: - Classify alerts (Critical, Warning, Informational). - Define ownership per alert. - Include contextual metadata in alerts. - Use dynamic thresholds where appropriate. - Regularly prune unnecessary alerts. |
| **No trend analysis or forecasting** Monitoring focuses only on real-time failures with no long-term insight. | Enable proactive monitoring: - Implement weekly/monthly trend dashboards. - Analyze error rates, latency, and capacity growth. - Forecast scaling needs and cost growth. - Include observability insights in architecture reviews. |

## Azure facilitation

**Core Monitoring Platform:**

- [Azure Monitor](/en-us/azure/azure-monitor/overview) is the central platform for collecting, analyzing, and acting on telemetry data from cloud and on-premises environments. It provides unified metrics, logs, and application monitoring.
[Azure Monitor health models](/en-us/azure/azure-monitor/health-models/overview) help you define, measure, and visualize workload health by correlating metrics, logs, and traces into actionable health states across Azure resources and components.
[Azure Monitor Metrics](/en-us/azure/azure-monitor/platform/metrics-supported) collects time-series data from monitored resources and supports real-time analysis and alerting.
[Azure Monitor Logs](/en-us/azure/azure-monitor/logs/data-platform-logs) provides Log Analytics with KQL for analyzing log data and creating custom insights.
[Azure Monitor Alerts](/en-us/azure/azure-monitor/platform/alerts-overview) enables intelligent alerting with action groups, notification routing, and automated responses.
Use simple log alerts when row-level evaluation helps you detect specific failure records faster. Tune those rules carefully to control noise and preserve clear operator action.

**Application Performance Monitoring:**

- [Application Insights](/en-us/azure/azure-monitor/app/app-insights-overview) provides APM capabilities with end-to-end tracing, dependency mapping, and user behavior analytics.

**Visualization and Analysis:**

- [Azure Workbooks](/en-us/azure/azure-monitor/platform/workbooks-overview) enables custom dashboard creation with interactive analytics and rich visualizations for drill-down scenarios.
- [Azure Dashboards](/en-us/azure/azure-portal/azure-portal-dashboards) provides centralized views of Azure resources and monitoring data with role-based access controls.
- [Log Analytics](/en-us/azure/azure-monitor/log-query/log-query-overview) is the analytics engine for querying and correlating multi-tier logs with advanced trending capabilities.
- [Azure VM Insights](/en-us/azure/azure-monitor/insights/vminsights-overview) provides specialized monitoring for virtual machine workloads with performance maps and dependency tracking.
- [Azure Container Insights](/en-us/azure/azure-monitor/insights/container-insights-overview) offers container-specific monitoring with cluster health, node performance, and pod-level insights.
For Azure Container Apps, managed OpenTelemetry export can standardize telemetry delivery to multiple backends when teams need a portable pipeline. Govern routing, retention, and ingestion cost before you enable more destinations.
ContainerAppHTTPLogs adds request-level traffic visibility that can improve traffic analysis and troubleshooting. Decide up front how much detail to retain because request logs can grow quickly and might expose sensitive request data.
- [Network Watcher](/en-us/azure/network-watcher/network-watcher-monitoring-overview) provides network-specific monitoring, diagnostics, and analytics for Azure networking resources.

## Related links

- [Recommendations for designing and creating an observability framework](../operational-excellence/observability)
- [Create an effective incident management plan to manage disruptions](incident-management)
- [Performance efficiency design principles](../performance-efficiency/principles)
- [Recommendations for designing a reliable monitoring and alerting strategy](../reliability/monitoring)

## Feedback

Was this page helpful?

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

## Additional resources

- Last updated on 2026-03-31

---

> 原页面：https://learn.microsoft.com/en-us/azure/well-architected/design-guides/monitoring（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
