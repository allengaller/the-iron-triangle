<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost05-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDACOST05-BP02 Implement dynamic resource provisioning

Enable automated resource scaling that matches manufacturing workload demands while
 optimizing costs. This includes implementing warm pools for faster scaling, considering
 application warm-up times, and aligning scaling policies with production schedules and peak
 processing times.

**Desired outcome:** Automated resource scaling that matches
 manufacturing workload demands while optimizing costs.

**Common anti-patterns:**

- Implementing automatic scaling without considering production schedule requirements
- Setting scaling thresholds without consulting manufacturing operations teams
- Using the same scaling policies for both production and non-production workloads
- Neglecting warm-up times for manufacturing applications when scaling
- Implementing aggressive scale-in policies that could impact production monitoring
- Not accounting for data retention requirements when scaling storage resources
- Ignoring the impact of scaling on integrated manufacturing systems
- Setting up dynamic provisioning without consideration for compliance requirements

**Benefits of establishing this best practice:**

- Optimized resource utilization
- Reduced manual intervention
- Cost-efficient scaling
- Improved responsiveness

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Before you begin, you will need:

- Detailed production schedules and patterns
- Peak resource usage data by workload type
- System warm-up and response time requirements

Key decisions needed:

- Scaling thresholds for different manufacturing workloads
- Resource retention periods based on production needs
- Performance impact limits for critical systems
- Cost optimization targets by workload type

Design your manufacturing workloads to automatically adjust resource provisioning
 based on current demand and production schedules. Implement a data-driven approach that
 correlates IT resource needs with manufacturing operations, providing appropriate safeguards
 for critical production systems and consideration for startup times and warm pools.

### Implementation steps

1. Define scaling metrics:
Production demand indicatorsResource utilization thresholdsCost constraints
2. Configure auto scaling policies:
Scale-out conditionsScale-in conditionsCool-down periods
3. Implement monitoring.
4. Set up cost tracking.
5. Perform regular policy review and optimization.

## Key AWS services

- AWS Auto Scaling
- Amazon EC2 Auto Scaling
- AWS Lambda
- Amazon CloudWatch

## Resources

**Related documents:**

- [AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html)
- [Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
- [AWS Lambda: Configuring reserved concurrency for a function](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html)
- [AWS Lambda: Configuring provisioned concurrency for a function PDF RSS](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)
- [Amazon CloudWatch: Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
- [Predictive scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost05-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
