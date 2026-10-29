<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVOPS02-BP03 Implement centralized logging to aggregate logs from all components of your advertising stack

To provide comprehensive visibility and operational efficiency
 across your advertising stack, implement a centralized logging
 solution. You can gain a holistic view of your system's
 performance and behavior by aggregating logs from all components
 of your advertising stack, including third-party integrations and
 custom applications.

## Implementation guidance

Review
 [centralized
 logging with opensearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/) to aggregate logs from
 all core components of the advertising workload.

**Amazon OpenSearch Service**

Use Amazon OpenSearch Service to aggregate logs from all core
 components of the advertising workload, including ad serving
 components like AWS Fargate tasks, Amazon EC2 instances, or AWS Lambda functions. OpenSearch provides a robust, scalable, and
 highly-available log aggregation solution with powerful search
 and analytics capabilities. Use this approach to have a
 consolidated view of logs across your entire advertising
 ecosystem, facilitating faster issue detection and resolution.

**Amazon CloudWatch Logs**

Alternatively, you can use Amazon CloudWatch Logs to capture and
 aggregate logs specifically from your ad serving components.
 CloudWatch Logs is a fully-managed service that makes it easy to
 monitor, store, and access your log files from various AWS
 services and on-premises sources. If your primary focus is on
 monitoring and analyzing the logs related to your ad serving
 components, CloudWatch Logs can be a suitable option.

The choice between OpenSearch and CloudWatch Logs for ad serving
 logs depends on your specific requirements and the overall
 complexity of your advertising workload. If you need a
 comprehensive, cross-component log aggregation and analysis
 solution, OpenSearch may be the preferred choice. However, if
 your needs are more focused on the ad serving components,
 CloudWatch Logs can be a simpler and more cost-effective option.

## Resources

- [Centralized
 Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
