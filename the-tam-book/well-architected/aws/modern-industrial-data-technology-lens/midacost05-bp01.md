<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost05-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDACOST05-BP01 Implement a buffering or throttling approach

Implement balanced resource utilization that handles varying workload demands while
 maintaining cost efficiency for manufacturing systems. This includes prioritizing critical
 processes while queuing less time-sensitive tasks and implementing appropriate scaling
 triggers aligned with production cycles.

**Desired outcome:** Balanced resource utilization that handles
 varying workload demands while maintaining cost efficiency.

**Common anti-patterns:**

- Implementing throttling on time-critical manufacturing processes
- Using the same buffering strategy for all types of industrial data
- Overlooking real-time requirements of production monitoring systems
- Setting queue limits without considering production batch sizes
- Implementing aggressive throttling that impacts quality data collection
- Not accounting for upstream and downstream dependencies in manufacturing processes
- Using standard IT buffering patterns without adapting to manufacturing needs

**Benefits of establishing this best practice:**

- Controlled resource consumption
- Avoided system overload
- Optimized costs during peak periods
- Improved system stability

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Before you begin, you will need:

- Documented critical and non-critical manufacturing processes
- Peak resource utilization patterns for different production phases
- Response time requirements for various manufacturing systems

Key decisions needed:

- Resource allocation priorities for critical vs. non-critical processes
- Throttling thresholds for different types of manufacturing workloads
- Queue configurations for deferrable processes
- Scaling triggers aligned with production cycles and peaks

Implement buffering and throttling mechanisms to manage cloud resource utilization
 during manufacturing peaks. Design a system that prioritizes critical processes (for
 example, real-time monitoring, quality control) for immediate resource access, while queuing
 less time-sensitive tasks (for example, batch analytics, report generation). Use
 auto-scaling for baseline capacity but implement throttling to help prevent non-critical
 tasks from consuming resources needed for production-critical operations.

Consider the following:

- Using Spot Instances for interruptible, non-critical workloads
- Implementing reserved capacity for predictable, critical processes
- Using serverless technologies for sporadic, scalable tasks

Regularly review and adjust your buffering and throttling strategies based on changing
 production patterns and business needs.

### Implementation steps

- Identify and categorize manufacturing workloads:
Critical real-time processes (for example, process control, safety systems)Time-sensitive operations (for example, quality inspections, inventory
 updates)Deferrable tasks (for example, long-term analytics, reporting)
- Design resource allocation strategies:
Priority-based access for critical systemsQueueing mechanisms for non-critical operationsLoad balancing across production lines or facilities
- Implement OT-aware monitoring:
Set up real-time monitoring for critical production KPIsConfigure alerts based on manufacturing thresholdsIntegrate with SCADA or MES for comprehensive visibility
- Establish OT-IT integrated scaling mechanisms:
Automatic scaling triggered by production volumesResource reservation for planned production increasesGradual scale-down aligned with shift changes or maintenance windows
- Conduct regular performance and cost reviews:
Analyze resource utilization against production outputIdentify opportunities for optimization without impacting OTAdjust strategies based on changing manufacturing requirements
- Implement feedback loops with shop floor:
Gather input from operators on system performanceAlign IT resource adjustments with production schedulesContinuously refine based on real-world manufacturing impact

## Key AWS services

- Amazon SQS
- Amazon Kinesis
- AWS Auto Scaling
- Amazon API Gateway

## Resources

**Related documents:**

- [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [Amazon Kinesis Data Streams Developer Guide](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- [AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html)
- [Throttle requests to your REST APIs for better throughput in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost05-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
