<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/expenditure-and-usage-awareness.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Expenditure and usage awareness

As covered in the [AWS
 Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html), the increased flexibility and agility that the cloud
 enables encourages innovation and fast-paced development and deployment. It eliminates the
 manual processes and time associated with provisioning on-premises infrastructure, including
 identifying hardware specifications, negotiating price quotations, managing purchase orders,
 scheduling shipments, and then deploying the resources.

As your serverless architecture grows, the number of Lambda functions, APIs, stages, and
 other assets will multiply. Most of these architectures need to be budgeted and forecasted in
 terms of costs and resource management, so tagging can help you here. You can allocate costs
 from your AWS bill to individual functions and APIs and obtain a granulated view of your
 costs and usage per project in AWS Cost Explorer.

A good implementation is to share the same key-value tag for assets that belong to the
 project programmatically, and create custom reports based on the tags that you have created.
 This feature will help you not only allocate your costs, but also identify which resources
 belong to which projects. To gain practical experience on this topic refer to the [Well Architected Labs](https://www.wellarchitectedlabs.com/). You can find many
 cost optimization walkthroughs that include tagging as well.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/expenditure-and-usage-awareness.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
