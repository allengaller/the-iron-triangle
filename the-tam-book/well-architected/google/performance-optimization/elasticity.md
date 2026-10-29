<!-- source: https://docs.cloud.google.com/architecture/framework/performance-optimization/elasticity -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Take advantage of elasticity

# Take advantage of elasticity Stay organized with collections Save and categorize content based on your preferences.

This principle in the performance optimization pillar of the
[Google Cloud Well-Architected Framework](/architecture/framework) 
provides recommendations to help you incorporate elasticity, which is the ability
to adjust resources dynamically based on changes in workload requirements.

Elasticity allows different components of
a system to scale independently. This targeted scaling can help improve performance and
cost efficiency by allocating resources precisely where they're needed, without
over provisioning or under provisioning your resources.

## Principle overview

The performance requirements of a system directly influence when and how the
system scales vertically or scales horizontally. You need to evaluate the system's
capacity and determine the load that the system is expected to handle at baseline.
Then, you need to determine how you want the system to respond to increases and decreases
in the load.

When the load increases, the system must scale out horizontally, scale up
vertically, or both. For horizontal scaling, add replica nodes to ensure that
the system has sufficient overall capacity to fulfill the increased demand. For
vertical scaling, replace the application's existing components with components
that contain more capacity, more memory, and more storage.

When the load decreases, the system must scale down (horizontally, vertically,
or both).

Define the *circumstances* in which the system scales up or scales down. Plan to
manually scale up systems for known periods of high traffic. Use tools like
autoscaling, which responds to increases or decreases in the load.

## Recommendations

To take advantage of elasticity, consider the recommendations in the following
sections.

### Plan for peak load periods

You need to plan an efficient scaling path for known events, such as expected
periods of increased customer demand.

Consider scaling up your system ahead of known periods of high traffic. For
example, if you're a retail organization, you expect demand to increase during
seasonal sales. We recommend that you manually scale up or scale out your systems before
those sales to ensure that your system can immediately handle the increased load
or immediately adjust existing limits. Otherwise, the system might take several minutes to
add resources in response to real-time changes. Your application's capacity
might not increase quickly enough and cause some users to experience delays.

For unknown or unexpected events, such as a sudden surge in demand or traffic,
you can use autoscaling features to trigger elastic scaling that's based on
metrics. These metrics can include CPU utilization, load balancer serving
capacity, latency, and even custom metrics that you define in
[Cloud Monitoring](/monitoring/docs/monitoring-overview).

For example, consider an application that runs on a
[Compute Engine](/compute/docs/overview) 
managed instance group (MIG). This application has a requirement that each instance performs
optimally until the average CPU utilization reaches 75%. In this example, you
might define an
[autoscaling policy](/compute/docs/autoscaler#autoscaling_policy) 
that creates more instances when the CPU utilization reaches the threshold.
These newly-created instances help absorb the load, which helps ensure that the average
CPU utilization remains at an optimal rate until the maximum number of instances
that you've configured for the MIG is reached. When the demand decreases, the
autoscaling policy removes the instances that are no longer needed.

Plan
[resource slot reservations in BigQuery](/bigquery/docs/reservations-intro#reservations) 
or adjust the limits for autoscaling configurations in Spanner by using the
[managed autoscaler](/spanner/docs/managed-autoscaler).

### Use predictive scaling

If your system components include Compute Engine, you must evaluate whether
[predictive autoscaling](/compute/docs/autoscaler#predictive_mode) 
is suitable for your workload. Predictive autoscaling forecasts the future load
based on your metrics' historical trends—for example, CPU utilization.
Forecasts are recomputed every few minutes, so the autoscaler rapidly adapts its
forecast to very recent changes in load. Without predictive autoscaling, an
autoscaler can only scale a group reactively, based on observed real-time changes
in load. Predictive autoscaling works with both real-time data and
historical data to respond to both the current and the forecasted load.

### Implement serverless architectures

Consider implementing a serverless architecture with serverless services that
are inherently elastic, such as the following:

- [Cloud Run](/run/docs/overview/what-is-cloud-run)
- [Cloud Run functions](/functions/docs)
- [BigQuery](/bigquery/docs/introduction)
- [Spanner](/spanner/docs)
- [Eventarc](/eventarc/docs)
- [Workflows](/workflows/docs)
- [Pub/Sub](/pubsub/docs)

Unlike autoscaling in other services that require fine-tuning rules (for
example, Compute Engine), serverless autoscaling is instant and can
scale down to zero resources.

### Use Autopilot mode for Kubernetes

For complex applications that require greater control over Kubernetes, consider
[Autopilot mode in Google Kubernetes Engine (GKE)](/kubernetes-engine/docs/concepts/autopilot-overview).
Autopilot mode provides automation and scalability by default.
GKE automatically scales nodes and resources based on
traffic. GKE manages nodes, creates new nodes for your applications, and
configures automatic upgrades and repairs.

---

> 原页面：https://docs.cloud.google.com/architecture/framework/performance-optimization/elasticity（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
