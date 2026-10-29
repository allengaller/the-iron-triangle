<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops03-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVOPS03-BP02 Automate runbooks to gain operational efficiency

Document runbooks for failover procedures, capacity scaling, and incident response
 workflows using AWS Systems Manager documents for automation.

## Implementation guidance

Consider the following example use case runbooks:

**Scaling runbook**

- Design step-by-step workflows for manually scaling up and down Amazon EC2 instances
 and increasing or decreasing managed service capacities
- Create automation scripts to initiate auto scaling actions
 based on predefined events
- Perform validation checks for successful scaling operations

**Third-party service
 disruptions**

- Implement multi-provider redundancy and failover mechanisms
 using AWS Lambda functions and Amazon API Gateway
- Use [AWS X-Ray](https://aws.amazon.com/xray/) for end-to-end tracing and troubleshooting of
 distributed applications and third-party integrations
- Document playbooks for provider switching, data
 synchronization, and incident escalation using
 [AWS Step Functions](https://aws.amazon.com/step-functions/) and
 [AWS Lambda](https://aws.amazon.com/lambda/)

**Infrastructure capacity
 issues**

- Implement auto scaling and load balancing using Amazon EC2 Auto Scaling and
 [Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/)
- Use
 [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) for predictive scaling based on
 historical data and scheduled scaling for planned events
- Document runbooks for capacity planning, scaling procedures,
 and cost optimization using
 [AWS Systems Manager](https://aws.amazon.com/systems-manager/) Documents

**Cost optimization runbook**

- Procedures for reviewing resource utilization and
 identifying opportunities for optimization using AWS Cost Explorer
- Guidelines for selecting the most cost-effective Amazon EC2 instance types and
 purchasing models (like On-Demand, Reserved, or Spot) based on workload patterns
- Automation to right size Amazon EC2 instances, remove unused resources, and use AWS
 Savings Plans
- Processes for periodic cost reviews and budget management

**Data management runbook**

- Create runbooks for:
Data pipeline failuresReplication issuesStorage capacity managementCompliance violations
- Include Regional considerations.
- Document recovery procedures.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops03-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
