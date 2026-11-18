<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/infrastructure-protection.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Infrastructure protection

For scenarios where your serverless application needs to interact with other
 components deployed in a virtual private cloud (VPC) or applications residing
 on-premises, it’s important to ensure that networking boundaries are considered.

Lambda functions can be configured to access resources within a VPC. Control traffic
 at all layers as described in the AWS Well-Architected Framework. For workloads that
 require outbound traffic filtering due to compliance reasons, proxies can be used in the
 same manner that they are applied in non-serverless architectures.

Enforcing networking boundaries solely at the application code level and giving
 instructions as to what resources one could access is not recommended due to separation
 of concerns.

For service-to-service communication, favor dynamic authentication, such as temporary
 credentials with AWS IAM over static keys. API Gateway and AWS AppSync both support IAM
 Authorization that makes it ideal to protect communication to and from AWS
 services.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/infrastructure-protection.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
