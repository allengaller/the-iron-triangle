<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec01-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVSEC01-BP01 Implement user authentication and access control to protect bidding process and content

Authenticate the approved SSPs (supply-side platforms) and
 advertisers. Based on this authentication, DSPs can provide them
 with least-privileged authorization and access to the relevant
 resources and data.

## Implementation guidance

AWS offers multiple services to provide SSPs and DSPs secured
 and scalable user management across all parts of the workload.
 Consider using
 [Amazon Cognito](https://aws.amazon.com/cognito/) to provide scalable authentication,
 authorization, and user management to your applications.
 Implementing federated identity integration with trusted
 identity providers can allow for ideal single sign on (SSO) for
 both publishers and advertisers. SSPs and DSPs can either use
 SAML 2.0 or OpenID Connect (OIDC) to create a trusted identity
 provider. From there, roles and permissions can be configured by
 a trusted administrator for users from the identity provider.

Additionally, you can use
 [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam) for fine-grained access control
 for users and different AWS services that may interact with
 advertising workloads. Enforce strict IAM policies that define
 permissions to help control access within AWS workloads. IAM
 policies define permissions for an action regardless of the
 method used to perform the operation.

Consider implementing role-based access control to determine
 which access to resources may align with a role based on
 business requirements. Use specific roles for different
 advertising services, including DSPs and SSPs, to verify that
 services operate with limited least privileged access.

## Resources

- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec01-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
