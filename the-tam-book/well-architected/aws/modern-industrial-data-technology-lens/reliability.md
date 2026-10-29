<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/reliability.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Reliability

Reliable and resilient data infrastructure is critical for manufacturing organizations to
 drive sustained innovation, operational excellence, and product quality. MIDA is designed with
 reliability as a core principle, verifying that data is consistently available, processed
 correctly, and recoverable even in the face of disruptions.

Manufacturing environments face unique reliability challenges due to their hybrid nature
 and critical operational requirements. The integration of OT with IT systems, real-time
 processing needs, and the necessity to maintain production continuity demand a sophisticated
 approach to reliability. MIDA addresses these challenges through a comprehensive architecture
 that spans from the shop floor to the cloud.

The architecture employs a hybrid edge-cloud model where edge components provide
 resilient local processing for mission-critical applications while cloud infrastructure offers
 scalable, fault-tolerant services for broader data management and analytics. This approach
 means that manufacturing operations can continue even during network disruptions, maintaining
 data consistency and enabling recovery across the entire system.

Through services like AWS IoT Greengrass, AWS IoT SiteWise, Amazon Kinesis, and
 purpose-built databases, MIDA provides the foundation for highly available manufacturing
 systems. The architecture incorporates automated failover, data replication, and comprehensive
 monitoring capabilities to provide reliability at every layer, from sensor data collection to
 enterprise-wide analytics.

###### Topics

- [Design principles](./design-principles-rel.html)
- [Foundations](./foundations.html)
- [Workload architecture](./workload-architecture.html)
- [Change management](./change-management.html)
- [Failure management](./failure-management.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/reliability.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
