<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost01-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDACOST01-BP02 Configure automated cost monitoring and alerts for manufacturing workloads

Set up a comprehensive alerting system that notifies teams within 24 hours when costs
 exceed thresholds, generates cost reports by production line, identifies waste, and maintains
 cost visibility across manufacturing operations. This includes setting up progressive alerting
 using different severity levels and implementing automated remediation for common cost-related
 issues.

**Desired outcome:** Set up a comprehensive alerting system
 that:

- Notifies teams within 24 hours when costs exceed defined thresholds
- Generates daily/weekly cost reports by production line
- Identifies resource waste and cost anomalies automatically
- Maintains cost visibility across manufacturing operations

**Common anti-patterns:**

- Setting up generic alerts without considering manufacturing-specific cost patterns
- Creating too many alerts that lead to notification fatigue
- Failing to establish baseline costs before implementing monitoring
- Not differentiating between production and non-production environment alerts
- Sending alerts to a general distribution list instead of specific responsible teams
- Using the same thresholds for different types of manufacturing workloads
- Implementing alerts without defined response procedures
- Focusing only on total cost without considering cost per unit of production
- Not accounting for shift patterns in alert configurations

**Benefits of establishing this Best Practice:**

- Early detection of cost anomalies
- Reduced manual monitoring effort
- Improved cost visibility across teams
- Faster response to cost-related issues

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Before setting up automation, verify that you have:

- Identified key stakeholders who need cost alerts (operations, finance, IT teams)
- Determined cost thresholds for different manufacturing processes
- Mapped your AWS resources to specific production lines or cells
- Established baseline costs for normal operations

Then, implement monitoring systems that:

- Track daily or weekly cost variations against production schedules
- Alert relevant teams when costs deviate your set thresholds (for example, 20%) or more from
 baseline
- Generate automated reports showing cost per unit of production
- Monitor resource utilization during different manufacturing shifts

### Implementation steps

1. Define cost thresholds or budgets for different manufacturing workload
 components.
2. Configure automated alerts for:
Budget overrunsUnusual usage patternsIdle resourcesStorage growth rates
3. Create automated reports for:
Daily, weekly, or monthly cost trendsResource utilization and production outputCost per manufacturing line, cell, or product
4. Establish escalation procedures for cost-related incidents.

## Key AWS services

- AWS Cost Explorer
- AWS Budgets
- AWS CloudTrail
- AWS CloudWatch
- Amazon Simple Notification Service
- AWS Pricing Calculator
- AWS Lambda

## Resources

**Related documents:**

- [Detecting unusual spend with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)

- [Cost
 Optimization with AWS](https://aws.amazon.com/aws-cost-management/cost-optimization/)
- [Logging AWS Cost Management API calls with AWS CloudTrail](https://docs.aws.amazon.com/cost-management/latest/userguide/logging-with-cloudtrail.html)
- [Create a billing alarm to monitor your estimated AWS charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost01-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
