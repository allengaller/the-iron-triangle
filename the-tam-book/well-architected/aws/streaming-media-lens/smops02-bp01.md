<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smops02-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# SMOPS02-BP01 Establish performance metrics by defining key performance indicators (KPIs) and service-level objectives (SLOs)

Establishing a full set of operational performance metrics is critical in streaming video workloads. It helps organizations to measure, monitor, and validate the performance of streaming operations across different scenarios.

**Desired outcome:**

- A well-defined set of metrics that provide practical insights into streaming video performance and enable data-driven operational improvements.

**Benefits of establishing this best practice:**

- Objective measurement of streaming quality and performance
- Early detection of potential issues
- Ability to validate improvements over time
- Alignment between technical metrics and business outcomes

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance

Operational KPIs and SLOs specific to streaming video workloads provide the foundation for measuring and improving streaming performance. Different streaming scenarios require distinct metrics that reflect their unique characteristics and viewer expectations.

For video on demand (VOD) streaming, key metrics include content processing time, time to first frame, rebuffer ratio, and error rates by device type. Live streaming workloads require monitoring full-path latency, stream stability, encoder performance, and failover success rate. Ad-supported content introduces metrics such as ad insertion latency, ad fill rate, Video Ad Serving Template (VAST) response time, and ad quality parity with main content. Low-latency streaming focuses on glass-to-glass latency, consistent latency across devices, and encoder optimization metrics. Interactive streaming requires tracking real-time communication latency, synchronization between video and interactive elements, and chat message delivery time.

### Implementation steps

1. **Identify critical user experience metrics:** Determine the key user experience metrics for your specific streaming scenario that most directly reflect viewer satisfaction.
2. **Define correlated technical metrics:** Define technical metrics that correlate with user experience to enable root cause analysis when viewer-facing issues arise.
3. **Establish baseline performance:** Establish baseline performance for each metric using historical data or initial measurement periods.
4. **Set SLOs aligned with business requirements:** Set SLOs that match business requirements and reflect realistic performance targets.
5. **Implement monitoring:** Implement monitoring and alerting based on these metrics to detect deviations from expected performance.
6. **Create operational dashboards:** Create dashboards for operational visibility that surface the most important metrics for each team role.
7. **Review and refine metrics regularly:** Regularly review and refine metrics based on user feedback and evolving business needs.

## Resources

**Related documents**

- [Monitoring AWS Media Services](https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor.html)
- [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

**Related services**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS X-Ray](https://aws.amazon.com/xray/)
- [Amazon Managed Grafana](https://aws.amazon.com/grafana/)
- [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smops02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
