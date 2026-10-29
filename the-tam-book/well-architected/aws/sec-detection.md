<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-detection.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Detection

You can use detective controls to identify a potential security
 threat or incident. They are an essential part of governance
 frameworks and can be used to support a quality process, a legal
 or compliance obligation, and for threat identification and
 response efforts. There are different types of detective controls.
 For example, conducting an inventory of assets and their
 detailed attributes promotes more effective decision making (and
 lifecycle controls) to help establish operational baselines. You
 can also use internal auditing, an examination of controls related
 to information systems, to verify that practices meet policies
 and requirements and that you have set the correct automated
 alerting notifications based on defined conditions. These controls
 are important reactive factors that can help your organization
 identify and understand the scope of anomalous activity.

In AWS, you can implement detective controls by processing logs,
 events, and monitoring that allows for auditing, automated
 analysis, and alarming. CloudTrail logs,
 AWS API calls, and CloudWatch provide monitoring of metrics with
 alarming, and AWS Config provides configuration history. Amazon
 GuardDuty is a managed threat detection service that continuously
 monitors for malicious or unauthorized behavior to help you
 protect your AWS accounts and workloads. Service-level logs are
 also available, for example, you can use Amazon Simple Storage Service (Amazon S3) to log access requests.

The following question focuses on these considerations for
 security.

Log management is important to a Well-Architected workload for
 reasons ranging from security or forensics to regulatory or legal
 requirements. It is critical that you analyze logs and respond
 to them so that you can identify potential security incidents.
 AWS provides functionality that makes log management easier to
 implement by giving you the ability to define a data-retention
 lifecycle or define where data will be preserved, archived, or
 eventually deleted. This makes predictable and reliable data
 handling simpler and more cost effective.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-detection.html（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
