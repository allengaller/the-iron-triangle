<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf04-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MSFTPERF04-BP02 Define baseline performance requirements

Microsoft workloads vary in their performance needs, making
 historical data analysis crucial for establishing baseline
 performance metrics. This approach allows organizations to detect
 and quantify performance fluctuations effectively. By implementing
 targeted alerts, IT teams can quickly identify anomalies, such as
 unexpected CPU usage spikes, changes in storage throughput,
 increased memory consumption, or more intricate performance issues.
 The collected monitoring data serves a dual purpose: it not only
 helps in detecting problems, but also provides valuable insights for
 ongoing performance optimization.

**Desired outcome:** Establish clear,
 measurable performance baselines for Microsoft workloads that enable
 effective anomaly detection, performance optimization, and capacity
 planning while providing objective criteria for evaluating system
 health and performance improvements over time.

**Common anti-patterns:**

- Operating Microsoft workloads without defined performance
 baselines, making it difficult to identify when performance
 degrades or to measure the effectiveness of optimization
 efforts.
- Setting performance baselines based on assumptions rather than
 actual historical data analysis, leading to inappropriate
 thresholds that generate false alerts or miss genuine
 performance issues.
- Creating static baselines that does not account for normal
 performance variations or business cycles, resulting in alert
 fatigue or missed performance degradation during expected usage
 patterns.

**Benefits of establishing this best
 practice:**

- Effective anomaly detection through well-defined baselines that
 enable accurate identification of performance deviations and
 potential issues before they impact business operations.
- Improved performance optimization through objective measurement
 criteria that enable evaluation of optimization efforts and
 identification of areas requiring attention.
- Enhanced capacity planning and resource allocation through
 baseline-driven analysis that supports data-driven decisions
 about scaling and infrastructure investments.

**Level of risk exposed if this best practice
 is not established:** Medium

## Implementation guidance

Implementing performance baselines requires systematic analysis of
 historical performance data and establishment of meaningful
 thresholds that account for normal variations while detecting
 genuine performance issues.

### Implementation steps

1. Collect sufficient historical performance data across all
 Microsoft workload components to establish statistically
 meaningful baselines.
2. Analyze performance patterns including daily, weekly, and
 seasonal variations to understand normal performance
 fluctuations.
3. Define performance baseline metrics for key indicators
 including CPU utilization, memory consumption, storage I/O,
 network throughput, and application response times.
4. Establish performance thresholds and alert criteria based on
 statistical analysis of historical data and business
 requirements.
5. Configure monitoring and alerting systems to detect
 deviations from established baselines and notify appropriate
 teams of performance anomalies.
6. Implement regular baseline review and adjustment processes
 to account for changing workload patterns and business
 requirements.
7. Document baseline definitions, measurement criteria, and
 alert thresholds for consistent application across
 environments and teams.
8. Integrate baseline monitoring into operational procedures
 and incident response processes to enable rapid performance
 issue identification and resolution.

## Resources

**Related documents:**

- [Using
 CloudWatch outlier detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
- [Best
 practices for monitoring Microsoft SQL Server on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/monitoring.html)
- [Windows
 Server - Power and performance tuning](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/hardware/power/power-performance-tuning)
- [Select
 the right instance type for Windows workloads](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/right-size-selection.html)
- [FSx for Windows File Server performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)
- [Windows
 container memory requirements](https://docs.aws.amazon.com/eks/latest/best-practices/windows-oom.html#_windows_container_memory_requirements)

**Related tools:**

- [Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch/)
- [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf04-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
