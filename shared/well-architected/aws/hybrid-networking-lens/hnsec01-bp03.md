<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec01-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSEC01-BP03 Implement continuous logging

Continuous logging provides real-time visibility across on-premises
 and cloud infrastructures. Implementing comprehensive logging
 mechanisms enables teams to quickly detect anomalies, troubleshoot
 connectivity issues, and maintain a consistent audit trail for
 security compliance.

**Desired outcome:** Achieve
 continuous visibility, reduce mean time to resolution during
 incidents, and automated enforcement of compliance configurations.

**Benefits of establishing this best
 practice:**

- Enables prompt incident detection and response
- Provides clear audit trails for compliance
- Ensures ongoing alignment with regulatory standards
- Reduces manual compliance effort

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

- Capture cloud environment API activities using services such
 as AWS CloudTrail.
- Enable flow logs for network visibility using services such as
 VPC Flow Logs and Transit Gateway Flow Logs.

## Resources

- [AWS services for logging and monitoring](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/aws-services-logging-monitoring.html)
- [AWS Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)
- [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [Logging
 IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec01-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
