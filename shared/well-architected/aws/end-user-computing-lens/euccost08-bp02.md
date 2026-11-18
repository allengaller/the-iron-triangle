<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost08-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCCOST08-BP02 Monitor your Amazon WorkSpaces Applications fleet utilization, and optimize scaling policies and buffer capacity

Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/?nc1=h_ls) to observe and
 monitor your Amazon WorkSpaces Applications resources. Amazon WorkSpaces Applications publishes several [WorkSpaces Applications
 Metrics and Dimensions](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-with-cloudwatch.html) to Amazon CloudWatch that you can visualize and use to check if you
 are overprovisioning buffer capacity or if you are running into capacity shortages at times.
 Use these metrics to adjust your WorkSpaces Applications Fleet capacity and scaling policies to minimize idle
 capacity and reduce insufficient capacity errors where possible.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

Create your own customized CloudWatch dashboards to visualize key WorkSpaces Applications metrics for your
 WorkSpaces Applications fleets. These dashboards can contain several widgets that display a view of
 selected metrics of a specific WorkSpaces Applications fleet or across multiple WorkSpaces Applications fleets. Review these
 dashboards on a regular basis.

Additionally, use the EUC Toolkit to review Amazon CloudWatch and OS-level metrics. This
 Toolkit also helps you manage large WorkSpaces and WorkSpaces Applications deployments at scale. After review of
 the metrics, determine whether changes to the fleet capacity or scaling policies are
 required, and plan for how to implement those changes. For more information, see [Use the EUC
 Toolkit to manage Amazon WorkSpaces Applications and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost08-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
