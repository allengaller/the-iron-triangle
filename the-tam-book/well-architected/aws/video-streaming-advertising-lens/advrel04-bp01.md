<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel04-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVREL04-BP01 Through your CI/CD pipeline, employ end-to-end regression, performance, and canary testing

Integrate comprehensive testing methodologies into CI/CD pipelines
 for advertising workloads. Monitor key metrics like 5xx errors and
 latency, especially in RTB systems, and respond quickly to issues
 through immediate engagement and fast rollbacks.

## Implementation guidance

For RTB at scale, the primary reliability metrics for
 availability are 5xx internal errors and elevated latency. If
 these metrics are breached, do not wait for impacts to ad
 effectiveness. Instead, fail fast and revert changes until the
 root cause of the issue can be identified and addressed.

## Key AWS services

- [AWS CodePipeline](https://aws.amazon.com/codepipeline/) is a fully-managed continuous
 delivery service
- [AWS Fault Injection Service](https://aws.amazon.com/fis/) is a
 fully-managed service that simulates real-world failures
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

## Resources

- [Deployment
 strategies](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/deployment-strategies.html)
- [Canary
 deployments](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/canary-deployments.html)
- [Use
 CloudWatch Synthetics to Monitor Sites, API Endpoints, Web Workflows, and More](https://aws.amazon.com/blogs/aws/new-use-cloudwatch-synthetics-to-monitor-sites-api-endpoints-web-workflows-and-more/)
- [Performing
 canary deployments and metrics-driven rollback with Amazon managed Service for Prometheus and Flagger](https://aws.amazon.com/blogs/opensource/performing-canary-deployments-and-metrics-driven-rollback-with-amazon-managed-service-for-prometheus-and-flagger/index.html)
- [Testing
 and creating CI/CD pipelines for AWS Step Functions](https://aws.amazon.com/blogs/devops/testing-and-creating-ci-cd-pipelines-for-aws-step-functions-using-aws-codepipeline-and-aws-codebuild/index.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel04-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
