<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec01-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVSEC01-BP04 Implement authorization by setting access policies, and implement least privilege access to protect programmatic workloads

Address the risk of authenticated advertisers and SSPs access to
 data they should not reach.

## Implementation guidance

Implement strong
 [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam) policies when you deploy a global
 advertising technology workload. Use the principle of least
 privilege, and enforce the separation of duties for good
 security posture. Administrative access should only be given to
 a small number of secured administrators.

Use [IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) to validate IAM policies and verify that
 they match IAM best practices and your organization's security
 standards.
 
 IAM Access Analyzer can help your organization review and
 removed unused or external access across your AWS resources with
 continuous monitoring. IAM Access Analyzer can also assist
 administrators by validating your IAM policies against IAM
 policy grammar and AWS best practices.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec01-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
