<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel05-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVREL05-BP02 Create disaster recovery (DR) runbooks, and regularly test documented backup and restoration processes

Processes for backup, restoration, and failover of data should be
 documented and regularly tested to validate efficacy and
 understanding.

## Implementation guidance

Advertising workloads are designed for low latency when
 accessing information. An unsuccessful or slow data restoration
 could result in negative impact to the workload. To mitigate the
 impact from data unavailability during a disaster, implement
 data backup mechanisms which can quickly make necessary data
 available. By documenting processes, incident response teams can
 address impactful events, while validation ensures that the
 processes will work when needed, and that team members are
 comfortable, and confident, in performing disaster response
 activities quickly.

## Key AWS services

- [AWS Elastic Disaster Recovery (DRS)](https://aws.amazon.com/disaster-recovery/) is a
 service that can help design a DR solution, map applications
 and networks, and build and test a DR runbook
- [AWS Config](https://aws.amazon.com/config/) can be used to continuously monitor
 and record resource configurations
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/) can detect drift in stacks
 that have been deployed

## Resources

- [Disaster
 recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)
- [Orchestrate
 disaster recovery automation using Amazon Application Recovery Controller (ARC) and AWS Step Functions](https://aws.amazon.com/blogs/networking-and-content-delivery/orchestrate-disaster-recovery-automation-using-amazon-route-53-arc-and-aws-step-functions/)
- [Testing
 disaster recovery](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/testing-disaster-recovery.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel05-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
