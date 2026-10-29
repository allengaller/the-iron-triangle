<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/opex-configuration.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Configuration

For configuration management, use environment variables for infrequent changes,
 such as logging level and database connection strings. Use [AWS Systems Manager](https://aws.amazon.com/systems-manager/) Parameter Store (SSM) or AWS AppConfig for dynamic
 configuration, such as feature toggles. Store sensitive data using AWS Secrets Manager. In
 Lambda functions, lookup values by reference from these external systems (SSM, AWS AppConfig,
 Secrets Manager) in the function’s global scope outside the handler to reduce API calls. You
 can achieve the same goal of reducing API calls to configuration and secrets stores using
 Lambda extensions which provide more fine-grained controls and the ability to re-fetch
 values. Lambda extensions are powerful and flexible yet bring additional considerations and
 challenges including integrations with unit tests and consistent delivery across functions
 and runtimes. Lambda Powertools offer similar functionality to retrieve values from various
 providers including SSM, AWS AppConfig, Secrets Manager, DynamoDB or custom stores.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/opex-configuration.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
