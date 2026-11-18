<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-mandem.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Manage demand and supply resources

When you move to the cloud, you pay only for what you need. You
 can supply resources to match the workload demand at the time
 they’re needed, this decreases the need for costly and wasteful
 over provisioning. You can also modify the demand, using a
 throttle, buﬀer, or queue to smooth the demand and serve it with
 less resources resulting in a lower cost, or process it at a
 later time with a batch service.

In AWS, you can automatically provision resources to match the
 workload demand. Auto Scaling using demand or time-based
 approaches permit you to add and remove
 resources as needed. If you can anticipate changes in demand, you
 can save more money and validate that your resources match your workload
 needs. You can use Amazon API Gateway to implement throttling, or
 Amazon SQS to implementing a queue in your workload. These will
 both permit you to modify the demand on your workload components.

The following question focuses on these considerations for cost
 optimization.

When designing to modify demand and supply resources, actively
 think about the patterns of usage, the time it takes to provision
 new resources, and the predictability of the demand pattern.
 When managing demand, verify you have a correctly sized queue or
 buﬀer, and that you are responding to workload demand in the
 required amount of time.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-mandem.html（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
