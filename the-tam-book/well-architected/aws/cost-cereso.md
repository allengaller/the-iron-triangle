<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-cereso.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Cost-effective resources

Using the appropriate instances and resources for your workload is
 key to cost savings. For example, a reporting process might take
 five hours to run on a smaller server but one hour to run on a
 larger server that is twice as expensive. Both servers give you
 the same outcome, but the smaller server incurs more cost over
 time.

A well-architected workload uses the most cost-effective
 resources, which can have a significant and positive economic
 impact. You also have the opportunity to use managed services to
 reduce costs. For example, rather than maintaining servers to
 deliver email, you can use a service that charges on a per-message
 basis.

AWS offers a variety of flexible and cost-effective pricing
 options to acquire instances from Amazon EC2 and other services in
 a way that more effectively fits your needs. *On-Demand*
*Instances* permit you to pay for compute
 capacity by the hour, with no minimum commitments required.
 *Savings Plans and Reserved Instances* offer
 savings of up to 75% oﬀ On-Demand pricing. With Spot Instances,
 you can leverage unused Amazon EC2 capacity and offer savings of
 up to 90% oﬀ On-Demand pricing. *Spot
 Instances* are appropriate where the system can tolerate
 using a fleet of servers where individual servers can come and go
 dynamically, such as stateless web servers, batch processing, or
 when using HPC and big data.

Appropriate service selection can also reduce usage and costs;
 such as CloudFront to minimize data transfer, or decrease costs, such as utilizing Amazon Aurora on Amazon RDS to
 remove expensive database licensing costs.

The following questions focus on these considerations for cost
 optimization.

By factoring in cost during service selection, and using tools
 such as Cost Explorer and AWS Trusted Advisor to regularly review
 your AWS usage, you can actively monitor your utilization and
 adjust your deployments accordingly.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-cereso.html（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
