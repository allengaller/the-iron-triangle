<!-- source: https://docs.cloud.google.com/architecture/framework/reliability/define-reliability-based-on-user-experience-goals -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Define reliability based on user-experience goals

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](/architecture/framework) 
helps you to assess your users' experience, and then map the findings to
reliability goals and metrics.

This principle is relevant to the *scoping*
[focus area](/architecture/framework/reliability#focus-areas) 
of reliability.

## Principle overview

Observability tools provide large amounts of data, but not all of the data
directly relates to the impacts on the users. For example, you might observe
high CPU usage, slow server operations, or even crashed tasks. However, if these
issues don't affect the user experience, then they don't constitute an outage.

To measure the user experience, you need to distinguish between internal system
behavior and user-facing problems. Focus on metrics like the success ratio of
user requests. Don't rely solely on server-centric metrics, like CPU usage,
which can lead to misleading conclusions about your service's reliability. True
reliability means that users can consistently and effectively use your
application or service.

## Recommendations

To help you measure user experience effectively, consider the recommendations
in the following sections.

### Measure user experience

To truly understand your service's reliability, prioritize metrics that reflect
your users' actual experience. For example, measure the users' query success
ratio, application latency, and error rates.

Ideally, collect this data directly from the user's device or browser. If this
direct data collection isn't feasible, shift your measurement point
progressively further away from the user in the system. For example, you can use
the load balancer or frontend service as the measurement point. This approach
helps you identify and address issues before those issues can significantly
impact your users.

### Analyze user journeys

To understand how users interact with your system, you can use tracing tools
like
[Cloud Trace](/trace/docs/overview).
By following a user's journey through your application, you can find bottlenecks
and latency issues that might degrade the user's experience. Cloud Trace
captures detailed performance data for each *hop* in your service architecture.
This data helps you identify and address performance issues more efficiently,
which can lead to a more reliable and satisfying user experience.

---

> 原页面：https://docs.cloud.google.com/architecture/framework/reliability/define-reliability-based-on-user-experience-goals（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
