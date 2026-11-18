<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoops06-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# TELCOOPS06-BP01 Verify resource availability for scale-out scenarios in telecommunication workloads

If the cloud providers cannot guarantee instant EC2 instance availability, especially for
 large instance types commonly used in telco deployments, implement proactive capacity planning.
 Capacity planning can be broken into two classes: *new service*
 and *run-rate*.

New service planning requires cloud resources where there is no trend data to indicate a
 future demand profile, and the service team has no visibility to the future demand profile.

Run-rate planning indicates a stable environment where organic growth can be modeled and
 forecast based on service consumption.

Introduction of new services in an existing deployment requires both approaches as the
 composite demand is both run-rate and new service. The methods include utilizing capacity
 reservations, maintaining buffer capacity, and implementing predictive scaling strategies based
 on historical usage patterns. Organizations should also consider using a mix of instance types
 and sizes that can support their workloads while increasing the likelihood of resource
 availability during scale-out events.

**Desired outcome:**

- Guaranteed resource availability.
- Efficient capacity planning.
- Predictable scaling operations.
- Optimized resource utilization.
- Minimized deployment delays.
- Cost-effective scaling.

**Common anti-patterns:**

- Reactive capacity planning.
- No resource forecasting.
- Missing buffer capacity.
- Poor utilization tracking.
- Inadequate reservation strategy.
- No scaling limits.
- Unplanned resource constraints.

**Level of risk exposed if this best practice is not established:**
 High

## Implementation guidance

Implement a comprehensive capacity management strategy that addresses both new service
 launches and ongoing operational needs. Create predictive scaling models that combine
 historical usage patterns with forecasted demand to verify adequate resource availability
 without over-provisioning. Develop buffer capacity policies that maintain appropriate headroom
 for unexpected demand spikes while considering cost implications and resource constraints.
 Establish regular capacity review processes that evaluate resource utilization trends,
 identify potential bottlenecks, and adjust capacity plans to maintain optimal performance and
 cost efficiency.

### Implementation steps

- Use Service Quotas for limit management and AWS Compute Optimizer for resource optimization
 recommendations.
- Implement AWS Auto Scaling for dynamic resource adjustment and EC2 Fleet for capacity
 diversity.
- Deploy AWS Systems Manager Automation for scaling procedures and Amazon EventBridge for automated
 scaling triggers.
- Configure AWS Cost Explorer for resource cost tracking and AWS Budgets for cost management.
- Use AWS Systems Manager OpsCenter for capacity management and Amazon CloudWatch for utilization
 monitoring.

## Resources

**Key AWS services:**

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [Amazon EC2 Fleet](https://aws.amazon.com/pm/ec2/)
- [AWS
 Capacity Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-manager.html)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Application Auto Scaling](https://aws.amazon.com/autoscaling/)
- [AWS
 Service Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoops06-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
