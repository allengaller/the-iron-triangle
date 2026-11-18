<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/wa-security.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Security in AWS Well-Architected

AWS Well-Architected Agent is in preview release and is subject to change.


Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data
 centers and network architectures that are built to meet the requirements of the most
 security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility
 model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security
 *in* the cloud:

- **Security of the cloud**: AWS is responsible for protecting
 the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with
 services that you can use securely. Third-party auditors regularly test and verify the
 effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that
 apply to AWS Well-Architected, see [AWS Services in Scope by Compliance
 Program](https://aws.amazon.com/compliance/services-in-scope/).
- **Security in the cloud**: Your responsibility is determined
 by the AWS service that you use. You are also responsible for other factors including the
 sensitivity of your data, your company's requirements, and applicable laws and
 regulations.

This documentation helps you understand how to apply the shared responsibility model when
 using AWS Well-Architected services. The following topics show you how to configure these
 services to meet your security and compliance objectives. You also learn how to use other
 AWS services that help you monitor and secure your resources.

The security information in this chapter applies to both the AWS Well-Architected Tool and
 AWS Well-Architected Agent. Where the access model differs between services, service-specific guidance is
 provided.

###### Topics

- [Data handling and privacy](#agent-security-data-handling)
- [Shared responsibility for AI-generated content](#agent-security-ai-responsibility)
- [Data protection in AWS Well-Architected](./data-protection.html)
- [Compliance validation for AWS Well-Architected](./wat-compliance.html)
- [Incident response in AWS Well-Architected](./incident-response.html)
- [Resilience in AWS Well-Architected](./disaster-recovery-resiliency.html)
- [Infrastructure security in AWS Well-Architected](./infrastructure-security.html)
- [Configuration and vulnerability analysis in AWS Well-Architected](./vulnerability-analysis.html)
- [Identity and access management for AWS Well-Architected](./security-iam.html)
- [Cross-service confused deputy prevention](./cross-service-confused-deputy-prevention.html)
- [Logging AWS Well-Architected API calls with AWS CloudTrail](./logging-using-cloudtrail.html)

## Data handling and privacy

AWS WA Agent analyzes resource telemetry, usage patterns, and configuration data from your AWS
 environment. It does not access the contents of your data stores such as Amazon S3 objects or database
 records.

All permissions granted to AWS WA Agent through the managed policy use read-only actions
 (`Get*`, `List*`, `Describe*`). AWS WA Agent cannot create, modify,
 or delete resources in your accounts.

## Shared responsibility for AI-generated content

AWS WA Agent does not execute AI-generated remediation steps on your behalf. AI-generated guided
 actions are provided for your review and validation. You are responsible for reviewing, testing,
 and executing these steps in your environment.

Remediation derived from AWS Trusted Advisor checks uses pre-built SSM Runbooks that are
 deterministic and tested. AWS WA Agent can trigger these on your behalf with your consent.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/wa-security.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
