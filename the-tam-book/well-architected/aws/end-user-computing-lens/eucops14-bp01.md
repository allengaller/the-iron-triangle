<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops14-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCOPS14-BP01 Ingest log file data from multiple data sources to correlate key problem identifiers and trends

Identify and implement mechanisms to maintain a centralized source of EUC service data
 that can be used for root cause analysis of cross service issues.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Store logs and metrics from AWS EUC services and their dependent services in a
 centralized location to allow analysis tools to build a picture of cross system failures
 that are affecting AWS EUC reliability. For example, expiry of a critical SSL
 certificate on a load balancer or remote access tier may be the root cause of login
 degradation or other failures at the AWS EUC service tier.

Use Amazon CloudWatch to gather metrics and logs, which are stored for subsequent analysis, to
 identify problems or trends that have occurred over time.

Amazon Kinesis agents can be installed onto Amazon WorkSpaces or WorkSpaces Applications images to export log
 file data in real time to a centralized location for retrospective analysis.

For larger environments, consider creating a data lake of key data from system logs,
 performance monitoring, and security tools across all service lines. Develop analysis
 capabilities using Amazon AI/ML tools to generate a more holistic insight into end to end
 systems health and scalability.

###### Note

Review CloudWatch and Kinesis data retention policies and service charges to verify that
 data availability and costs are within EUC project guidelines.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops14-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
