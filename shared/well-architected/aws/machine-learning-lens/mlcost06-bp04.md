<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost06-bp04.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# MLCOST06-BP04 Enable debugging and logging

Implementing comprehensive logging and debugging capabilities for
 your machine learning workflows assists you to understand resource
 consumption patterns and identify optimization opportunities. By
 collecting and analyzing runtime metrics, you can reduce costs and
 enhance the efficiency of your ML training operations.

**Desired outcome:** You gain
 visibility into training jobs through metrics and logs that reveal
 resource consumption patterns. This practice identifies optimization
 opportunities, reduces costs, and improves ML model training
 performance. You implement monitoring systems to track compute and
 storage utilization, and instrument code to record key metrics.

**Common anti-patterns:**

- Training ML models without performance visibility.
- Ignoring resource consumption data until costs become
 problematic.
- Deploying ML solutions without adequate logging infrastructure.
- Using manual methods to track performance metrics.
- Waiting for issues to arise before implementing monitoring.

**Benefits of establishing this best
 practice:**

- Early identification of model training inefficiencies.
- Reduced compute and storage costs through resource optimization.
- Faster troubleshooting of training job issues.
- Enhanced visibility into ML pipelines.
- Data-driven decisions for infrastructure provisioning.

**Level of risk exposed if this best practice
 is not established:** Medium

## Implementation guidance

Proper debugging and logging are crucial for cost management in
 machine learning workflows. As ML models grow in complexity, the
 computational resources required for training also increase. By
 implementing comprehensive monitoring, you can identify
 inefficiencies, optimize resource allocation, and reduce overall
 costs.

Effective logging and debugging require instrumentation at
 multiple levels, from the ML code itself to the underlying
 infrastructure. This visibility provides an understanding of how
 resources are being utilized during training jobs and identifies
 bottlenecks so that you can make data-driven decisions about when
 and how to scale resources. The metrics and logs collected can
 reveal patterns of inefficient resource utilization that might
 otherwise go unnoticed.

Additionally, monitoring storage consumption is important as data
 preparation and feature engineering can generate large
 intermediate datasets. By tracking both compute and storage
 metrics, you can identify opportunities for optimization across
 your entire ML pipeline.

### Implementation steps

1. **Set up Amazon SageMaker AI
 Debugger**.
 [Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html) captures training job states at
 regular intervals, providing visibility into the ML training
 process. It monitors, records, and analyzes data during
 training, enabling you to:
Track model parameters, gradients, and tensor valuesIdentify training issues like vanishing gradients or
 tensor explosionsReceive automated alerts for common training problemsVisualize and analyze captured data interactively
2. **Implement CloudWatch
 logging**. Integrate
 [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) with your SageMaker AI training jobs to
 centralize and analyze log data. Configure CloudWatch to:
Collect standard output and error logs from training
 jobsEncrypt log data using an
 [AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) for securitySet up custom log groups and streams for different ML
 workflowsCreate log retention policies to manage storage costs
3. **Instrument ML code for metrics
 collection**. Add instrumentation code to your ML
 training scripts to capture performance metrics and resource
 utilization data:
Track timing information for different training phasesMonitor memory usage during training operationsRecord batch processing statistics and convergence
 metricsLog hyperparameter values and their impact on training
 performance
4. **Configure resource
 monitoring**. Set up monitoring for compute and
 storage resources used by your ML workflows:
Use CloudWatch metrics to track instance utilizationMonitor data transfer volumes between storage and
 compute resourcesSet up alerts for abnormal resource consumption patternsCreate dashboards to visualize resource utilization
 trends
5. **Implement automated
 alerting**. Configure notification systems to alert
 you when resource consumption exceeds expected thresholds:
Set up CloudWatch alarms for high CPU, memory, or GPU
 utilizationCreate alerts for extended training job durationsConfigure notifications for storage capacity issuesEstablish alerting for debugging rule violations in
 SageMaker AI Debugger
6. **Analyze and optimize training
 jobs**. Use the collected metrics and logs to
 identify optimization opportunities:
Review resource utilization patterns to identify
 right-sizing opportunitiesAnalyze training job logs for inefficient code pathsExamine data loading and preprocessing bottlenecksOptimize hyperparameters based on performance metrics
7. **Use enhanced debugging
 capabilities**. Use improved SageMaker AI Studio
 debugging and monitoring capabilities with better
 integration to popular ML frameworks and enhanced
 visualization tools for more efficient troubleshooting.
8. **Use generative AI for log
 analysis**. Use generative AI capabilities to
 analyze and extract insights from ML training logs. Utilize
 Q Diagnostics integrated into the console or your preferred
 IDE for log analysis.
Implement natural language processing to summarize log
 patternsUse Amazon Bedrock to build intelligent log analysis
 assistantsDeploy ML models that can predict resource needs based
 on historical dataCreate automated reports of cost optimization
 opportunities from log data

## Resources

**Related documents:**

- [Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html)
- [What
 is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [Analyzing
 log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
- [Logging
 and Monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-incident-response.html)
- [Logging
 Amazon ML API Calls with AWS CloudTrail](https://docs.aws.amazon.com/machine-learning/latest/dg/logging-using-cloudtrail.html)
- [Amazon SageMaker AI Debugger API](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html)

**Related examples:**

- [Debugger
 example notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-debugger))
- [SageMaker AI
 Debugger GitHub Repository](https://github.com/awslabs/sagemaker-debugger)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost06-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
