<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops06-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCOPS06-BP01 Deploy test, development, and pre-production environments to reduce risk to production services

Training and testing should be undertaken in isolated environments, with little or no
 connectivity to production services.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Separate the EUC environments used for training, testing, and development from
 production services to reduce the risk of non-production activities affecting normal
 business operations. Create discrete test environments and use them for activities that
 could disrupt production services, cause outages or performance degradation, or compromise
 security.

When testing and staging new releases or updates to production systems, these should
 be undertaken in a separate environment that matches the current production deployment as
 closely as possible. This reduces the likelihood of issues arising from disparities
 between test, staging and production.

AWS EUC services are Regional in nature and delivered on an AWS account by
 account basis. Multiple Regions and accounts can be deployed to separate training,
 testing, and production environments.

Multiple AWS accounts can also be deployed to separate production workloads for
 scalability reasons, helping to avoid having all resources in the same place or where
 service separation is necessary to align with compliance or security requirements.

AWS Control Tower can be used to streamline the management and governance of multiple
 AWS accounts.

Unlike on-premises infrastructure, Amazon WorkSpaces and WorkSpaces Applications environments can be
 [deployed using automated processes](https://pages.awscloud.com/rs/112-TZM-766/images/2020_0210-EUC_Slide-Deck.pdf) and only attract costs while in use.

AWS CloudFormation templates can be used to deploy new AWS services such as WorkSpaces and
 WorkSpaces Applications to reduce the likelihood of human error and reduce configuration drift.

AWS Systems Manager Runbooks can be used to automate some aspects of WorkSpaces deployment. For
 more detail, see [SSM
 Runbooks for Amazon WorkSpaces](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-wsp.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops06-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
