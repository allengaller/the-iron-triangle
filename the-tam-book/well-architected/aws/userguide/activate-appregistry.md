<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/activate-appregistry.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Activating AppRegistry for a workload

AWS Well-Architected Agent is in preview release and is subject to change.


Using AppRegistry is optional, and AWS Business and Enterprise Support customers can
 activate it on a per-workload basis.

Whenever Discovery support is turned on and AppRegistry is associated with a new or
 existing workload, AWS Well-Architected Tool creates a service-managed attribute group. The attribute
 group **Metadata** in AppRegistry contains the workload ARN, the
 workload name, and the risks associated with the workload.

- When Discovery support is turned on, any time there is a change to the workload, the
 attribute group is updated.
- When Discovery support is turned off or the application is removed from the workload, the
 workload information is removed from AWS Service Catalog.

If you want an AppRegistry application to drive the data fetched from Trusted Advisor, set
 your workload **Resource definition** as
 **AppRegistry** or **All**. Create roles for all
 accounts that own resources in your application following the guidelines in [Activating Trusted Advisor for a workload in IAM](./activate-ta-in-iam.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/activate-appregistry.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
