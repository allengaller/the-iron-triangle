<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/selection.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Selection

Run performance tests on your serverless application using steady and burst rates. Using
 the result, try tuning capacity units and the provisioning model, and load test after changes
 to help you select the best configuration:

- **Amazon API Gateway :** Use Edge endpoints for geographically
 dispersed customers. Use Regional for regional customers and when using other AWS
 services within the same Region.
- **AWS Lambda :** Test different memory settings since CPU,
 network, and storage IOPS are allocated proportionally. Optimize static initialization and
 consider provisioned concurrency.
- **AWS Step Functions**: Test Standard and Express Workflows, consider
 the per second rates for both execution start rate and state transition rate.
- **Amazon DynamoDB:** Use on-demand for unpredictable application
 traffic, otherwise provisioned mode for consistent traffic.
- **Amazon Kinesis:** Use enhanced-fan-out for dedicated input/output
 channels per consumer in multiple consumer scenarios. Use an extended batch window for low
 volume transactions with Lambda.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/selection.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
