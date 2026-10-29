<!-- source: https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Promote modular design

# Promote modular design Stay organized with collections Save and categorize content based on your preferences.

This principle in the performance optimization pillar of the
[Google Cloud Well-Architected Framework](/architecture/framework) 
provides recommendations to help you promote a modular design.
Modular components and clear interfaces can enable flexible scaling,
independent updates, and future component separation.

## Principle overview

Understand the dependencies between the application components and the system
components to design a scalable system.

Modular design enables flexibility and resilience, regardless of whether a
monolithic or microservices architecture was initially deployed. By decomposing
the system into well-defined, independent modules with clear interfaces, you can
scale individual components to meet specific demands.

Targeted scaling can help optimize resource utilization and reduce costs in the
following ways:

- Provisions only the necessary resources to each component, and
allocates fewer resources to less-demanding components.
- Adds more resources during high-traffic periods to maintain the user
experience.
- Removes under-utilized resources without compromising performance.

Modularity also enhances maintainability. Smaller, self-contained units are
easier to understand, debug, and update, which can lead to faster development
cycles and reduced risk.

While modularity offers significant advantages, you must evaluate the potential
performance trade-offs. The increased communication between modules can
introduce latency and overhead. Strive for a balance between modularity and
performance. A highly modular design might not be universally suitable. When
performance is critical, a more tightly coupled approach might be appropriate.
System design is an
[iterative process](/architecture/framework/performance-optimization),
in which you continuously review and refine your modular design.

## Recommendations

To promote modular designs, consider the recommendations in the following
sections.

### Design for loose coupling

Design a
[loosely coupled architecture](https://cloud.google.com/learn/what-is-microservices-architecture).
Independent components with minimal dependencies can help you build
[scalable and resilient applications](/architecture/scalable-and-resilient-apps).
As you plan the boundaries for your services, you must consider the availability
and scalability requirements. For example, if one component has requirements that
are different from your other components, you can design the component as a standalone
service. Implement a plan for graceful failures for less-important subprocesses
or services that don't impact the response time of the primary services.

### Design for concurrency and parallelism

Design your application to support multiple tasks concurrently, like processing
multiple user requests or running background jobs while users interact with your
system. Break large tasks into smaller chunks that can be processed at the same
time by multiple service instances. Task concurrency lets you use features like
autoscaling to increase the resource allocation in products like the following:

- [Compute Engine](/compute/docs/autoscaler)
- [Google Kubernetes Engine](/kubernetes-engine/docs/concepts/cluster-autoscaler)
- [BigQuery](/bigquery/docs/slots#slot-autoscaling)
- [Spanner](/spanner/docs/autoscaling-overview)

### Balance modularity for flexible resource allocation

Where possible, ensure that each component uses only the necessary resources
(like memory, storage, and processing power) for specific operations. Resource
over-allocation can result in unnecessary costs, while resource under-allocation can
compromise performance.

### Use well-defined interfaces

Ensure modular components communicate effectively through clear, standardized
interfaces (like APIs and message queues) to reduce overhead from translation
layers or from extraneous traffic.

### Use stateless models

A stateless model can help ensure that you can handle each request or interaction with
the service independently from previous requests. This model facilitates
scalability and recoverability, because you can grow, shrink, or restart the
service without losing the data necessary for in-progress requests or
processes.

### Choose complementary technologies

Choose technologies that complement the modular design. Evaluate programming
languages, frameworks, and databases for their modularity support.

For more information, see the following resources:

- [Re-architecting to cloud native](https://cloud.google.com/resources/rearchitecting-to-cloud-native)
- [Introduction to microservices](https://cloud.google.com/learn/what-is-microservices-architecture)

---

> 原页面：https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
