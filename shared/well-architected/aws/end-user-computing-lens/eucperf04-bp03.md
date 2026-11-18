<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf04-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCPERF04-BP03 Determine the running mode and size of hardware bundles needed to support each user type's applications

It's important to have a high degree of familiarity with the applications that need to
 be delivered using Amazon WorkSpaces Personal in terms of their compute resource requirements and
 their usage pattern. By understanding core compute requirements such as the amount of
 memory, CPU, network bandwidth, latency, and disk space that applications require, you can
 more effectively determine the optimum WorkSpaces Personal bundle type. The optimal running mode
 required to support the workload is determined by understanding the pattern of usage of the
 application.

## Implementation guidance

Determine the compute requirements for your applications.

- Assess your users' applications and tasks and deploy a sufficient level of
 performance as is needed.
- Monitor the resulting user feedback to verify that performance meets their needs
 without overprovisioning their hardware types.
- If performance or productivity suffers for various users, increase the size of
 their instances.
- For Personal WorkSpaces, establish the current or required pattern of usage of the
 applications or desktops being delivered. Select an Always-On running mode for user
 environments that are broadly used throughout each month (> 80 hours), select the
 Auto-Stop running mode where usage will be <80 hours per month. Alternatively,
 consider implementing the [Cost Optimizer
 for Amazon WorkSpaces Solution](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/) to automatically select the optimum running mode for
 each instance.
- [Enable self-service WorkSpace management capabilities for your users.](https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-user-self-service-workspace-management.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf04-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
