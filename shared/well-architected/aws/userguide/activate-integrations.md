<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/activate-integrations.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Activating support in AWS WA Tool for other AWS services

AWS Well-Architected Agent is in preview release and is subject to change.


Activating Organization access permits AWS Well-Architected Tool to gather information about your
 organization's structure to share resources more easily (see [Activate resource sharing within AWS Organizations](./sharing.html#getting-started-sharing-orgs) for more information). Activating Discovery
 support gathers information from [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html), [AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html), and related resources (such as CloudFormation stacks in AppRegistry resource
 collections) to help you more easily discover the information needed to answer
 Well-Architected review questions, and tailor the Trusted Advisor checks for a workload.

Activating support for AWS Organizations, or activating Discovery support automatically creates
 a service-linked role for your account.

**To turn on support for other services that AWS WA Tool can interact
 with, navigate to Settings.**

1. To gather information from AWS Organizations, turn on **Activate AWS Organizations support**.
2. Turn on **Activate Discovery support** to gather information from other AWS
 services and resources.
3. Select **View role permissions** to view the service-linked role permissions or trust relationship policies.
4. Select **Save settings**.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/activate-integrations.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
