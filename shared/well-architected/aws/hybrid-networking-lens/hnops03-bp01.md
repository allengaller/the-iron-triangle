<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops03-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNOPS03-BP01 Monitor hybrid networking components

Monitoring solutions serve as an essential tool to provide
 visibility across your hybrid network infrastructure. It enables
 collection, visualization, and analysis of metrics from network
 connectivity components like virtual private networks, dedicated
 connections, and network transit hubs, allowing teams to set alarms
 for performance thresholds and detect anomalies before they impact
 connectivity.

**Desired outcome:**

- Quickly identified and address performance issues, security
 anomalies, and connectivity problems
- Improved network reliability, optimized resource utilization,
 and enhanced operational efficiency.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Get real-time visibility into network performance, enabling
 quick detection and resolution of issues.
- Customizable alerts and automated responses to predefined
 conditions.
- Support capacity planning and resource optimization by providing
 historical data and trends.

## Implementation guidance:

- Identify critical hybrid networking components that require
 monitoring. Determine key metrics and thresholds relevant to
 each component.
- Configure dashboards, alarms, and automated actions using
 services such as Amazon CloudWatch
- Integrate automated notification and remediation to alarms
 using services such as Amazon SNS and AWS Lambda

## Resources

- [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [Metrics
 and events in Amazon VPC Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-monitoring.html)
- [AWS Direct Connect Monitoring](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html)
- [Monitor
 hybrid connectivity with Amazon CloudWatch Network Synthetic
 Monitor](https://aws.amazon.com/blogs/networking-and-content-delivery/monitor-hybrid-connectivity-with-amazon-cloudwatch-network-monitor/)
- [AWS Cloud WAN events and metrics](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-events-metrics.html)
- [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops03-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
