<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-failmgmt.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Failure management

In any system of reasonable complexity, it is expected that
 failures will occur. Reliability requires that your workload be
 aware of failures as they occur and take action to avoid impact on
 availability. Workloads must be able to both withstand failures
 and automatically repair issues.

With AWS, you can take advantage of automation to react to monitoring data. For example,
 when a particular metric crosses a threshold, you can initiate an automated action to
 remedy the problem. Also, rather than trying to diagnose and fix a failed resource that is
 part of your production environment, you can replace it with a new one and carry out the
 analysis on the failed resource out of band. Since the cloud allows you to stand up
 temporary versions of a whole system at low cost, you can use automated testing to verify
 full recovery processes.

The following questions focus on these considerations for
 reliability.

Regularly back up your data and test your backup files to verify
 that you can recover from both logical and physical errors. A
 key to managing failure is the frequent and automated testing of
 workloads to cause failure, and then observe how they recover.
 Do this on a regular schedule and verify that such testing is also
 initiated after significant workload changes. Actively track KPIs, 
 and also the recovery time objective (RTO) and recovery point
 objective (RPO), to assess a workload's resiliency (especially
 under failure-testing scenarios). Tracking KPIs will help you
 identify and mitigate single points of failure. The objective is
 to thoroughly test your workload-recovery processes so that you
 are confident that you can recover all your data and continue to
 serve your customers, even in the face of sustained problems. Your
 recovery processes should be as well exercised as your normal
 production processes.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-failmgmt.html（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
