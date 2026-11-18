<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops03-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNOPS03-BP02 Consider flow logs for enhanced network visibility when needed

Flow logs capture detailed information about network traffic
 traversing your cloud infrastructure network components. While not
 essential for all deployments, implementing flow logs is recommended
 for environments requiring in-depth network analysis and security
 auditing. The logs provide valuable insights into network behavior,
 enabling teams to troubleshoot connectivity issues, monitor traffic
 patterns, detect security anomalies, ensure compliance with network
 policies, and optimize network performance. By leveraging this
 feature, organizations can enhance their network visibility, improve
 security posture, and gain actionable insights for network
 optimization.

**Desired outcome:**

- Comprehensive visibility into network traffic patterns, source
 and destination IP addresses, ports, protocols, and packet
 counts.
- Greater insights during network troubleshooting, and security
 analysis

**Level of risk exposed if this best practice
 is not established:** Medium

**Benefits of establishing this best
 practice:**

- Reduce mean time to resolution (MTTR) for network issues through
 rapid troubleshooting and root cause analysis.
- Detailed traffic visibility enables teams to analyze traffic
 patterns to enhance capacity planning, optimize network
 spending, and prevent over-provisioning of resources.
- Comprehensive audit trails of network activity help
 organizations to meet compliance requirements and security
 standards.

## Implementation guidance

- Evaluate the volume of network traffic and associated logging
 costs of flow logs.
- Identify the network resources that require monitoring and
 determine the appropriate destination for your logs based on
 your analysis needs and retention requirements.
For example, VPC and Transit Gateway flow logs can be sent to
 Amazon CloudWatch Logs, S3, or Amazon Data Firehose.
- Consider implementing log filters to focus on specific types
 of traffic or to alert suspicious activities.

## Resources

- [Logging
 IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [AWS Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops03-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
