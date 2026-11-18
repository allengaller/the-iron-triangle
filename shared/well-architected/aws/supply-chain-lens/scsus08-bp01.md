<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus08-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# SCSUS08-BP01 Collect usage data to feed advanced analysis and ML models to better predict future resources needs

Consider improving your ability to predict AWS Cloud resources
 required for your supply chain and sustainability-related
 workloads to prefer on-demand over always-on. Base this data on
 forecasts, seasonality, and peaks and valleys analysis to
 efficiently turn resources on and off accordingly or scaling
 resources up and down and horizontally.

**Desired outcome**: Achieve
 dynamic scalability and resource efficiency by using historical
 usage data to predict and optimize resource needs.

**Benefits of establishing this best
 practice:** Improves operational agility, reduces
 downtime, and minimizes unnecessary resource usage.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

Consider collecting data about resource usage over the past
 years to design and prefer on-demand over always-on, with the
 main goal of optimizing resources scaling, uptime and downtime,
 availability, and replication based on your business needs.

Gain visibility of required resources through ML-based
 predictions, using built-in features of AWS System Manager,
 Instance Scheduler on AWS, and signals from Amazon CloudWatch,
 while using managed databases like Amazon RDS, and
 [containers
 orchestration](https://aws.amazon.com/containers/) running on AWS towards serverless
 architectures.

### Implementation steps

1. Collect and analyze historical resource usage data to
 identify patterns and optimization opportunities for
 on-demand resource allocation.
2. Implement machine learning-based prediction models to
 forecast future resource needs based on business patterns
 and seasonality.
3. Deploy AWS Systems Manager and Instance Scheduler to
 automate resource scheduling based on predicted demand
 patterns.
4. Configure Amazon CloudWatch monitoring to provide
 real-time signals for dynamic resource scaling decisions.
5. Migrate appropriate workloads to managed databases and
 serverless architectures to optimize resource utilization.
6. Establish continuous monitoring and optimization processes
 to refine on-demand resource strategies over time.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus08-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
