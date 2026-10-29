<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-5.1---prevent-unintended-access-to-the-infrastructure..html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best practice 5.1 – Prevent unintended access to the infrastructure

Grant least privilege access to infrastructure to help
 prevent inadvertent or unintended access to the
 infrastructure. For example, make sure that anonymous users
 are not allowed to access to the systems, and that the
 systems are deployed into isolated network spaces. Network
 boundaries isolate analytics resources and restrict network
 access. Network access control lists (NACLs) act as a
 firewall for controlling traffic in and out. To reduce the risk
 of inadvertent access, define the network boundaries of the
 analytics systems and only allow intended access.

## Suggestion 5.1.1 – Ensure that resources in the infrastructure have boundaries

Use infrastructure boundaries for services such as
 databases. Place services in their own VPC private subnets
 that are configured to allow connections only to needed
 analytics systems.

Use
 [AWS Identity and Access Management (IAM) Access
 Analyzer](https://aws.amazon.com/iam/features/analyze-access/) for all AWS accounts that are centrally
 managed through
 [AWS Organizations.](https://aws.amazon.com/organizations/) This allows security teams and
 administrators to uncover unintended access to resources
 from outside their AWS organization within minutes.

You can proactively address whether any resource policies
 across any of your accounts violate your security and
 governance practices by allowing unintended access.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-5.1---prevent-unintended-access-to-the-infrastructure..html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
