<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops05-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCOPS05-BP02 Store and regularly analyze log files to detect anomalous activity and behaviors

Maintaining a central store of log data and performance metrics is frequently a
 mandatory requirement if specific compliance standards need to be maintained. Even in the
 absence of compliance requirements, maintaining a central store of data facilitates a better
 understanding of service scaling, performance, and security enables analysis, which improves
 root cause analysis and drives incremental service improvement.

Review the available data sources that provide key insight into the usage of your EUC
 environment.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Extracting performance data and log files from both WorkSpaces and WorkSpaces Applications and
 storing it centrally is essential if you need to adhere to specific industry compliance
 standards or if you want to perform retrospective analysis of data for troubleshooting
 purposes, root cause analysis, or predicting service scalability and requirements.

Amazon CloudWatch can be used to capture specific metrics and store the data longer term in
 Amazon S3. Amazon Kinesis agents can also be installed on WorkSpaces or WorkSpaces Applications instances to
 propagate system logs in real time to a centralized location. For more detail, see [Using Amazon Kinesis Agents to Store AppStream Event Logs](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-kinesis-agent-for-microsoft-windows-to-store-appstream-2-0-windows-event-logs/).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops05-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
