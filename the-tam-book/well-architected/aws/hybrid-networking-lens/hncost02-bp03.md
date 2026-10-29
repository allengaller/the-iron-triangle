<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost02-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNCOST02-BP03 Analyze network traffic patterns for optimization opportunities

Analyzing network traffic patterns in hybrid environments is crucial
 for optimizing performance across cloud components. By examining
 data flow, organizations can identify latency issues caused by
 network distance, data volume, and traffic spikes that impact
 application responsiveness. Traffic pattern monitoring enables
 businesses to make informed decisions about workload placement and
 data prioritization, ultimately creating a more efficient hybrid
 infrastructure that balances performance needs with cost
 considerations.

**Desired outcome:** Optimized
 network traffic flows and reduced data transfer costs through
 actionable insights.

**Level of risk exposed if this best practice
 is not established:** Medium

**Benefits of establishing this best
 practice:**

- Improved network efficiency
- Reduced data transfer costs
- Enhanced troubleshooting and capacity planning

## Implementation guidance

- Enable flow logs to collect network flow data. For example,
 you can achieve this using VPC Flow Logs and Transit Gateway
 Flow Logs
- Regularly review and analyze flow logs to identify
 optimization opportunities. For example, you can achieve this
 using Amazon Managed Grafana or Amazon OpenSearch Service

## Resources

- [VPC
 Flow Logs Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [AWS Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)
- [Stream
 VPC flow logs to Amazon OpenSearch Service via Amazon Data Firehose](https://aws.amazon.com/blogs/big-data/stream-vpc-flow-logs-to-amazon-opensearch-service-via-amazon-kinesis-data-firehose/)
- [Monitor
 AWS Transit Gateway Flow Logs centrally using Amazon Managed Grafana](https://aws.amazon.com/blogs/mt/monitor-aws-transit-gateway-flow-logs-centrally-using-amazon-managed-grafana/)
- [Visualize
 and gain insights into your VPC Flow logs with Amazon Managed Grafana](https://aws.amazon.com/blogs/mt/visualize-and-gain-insights-into-your-vpc-flow-logs-with-amazon-managed-grafana/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost02-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
