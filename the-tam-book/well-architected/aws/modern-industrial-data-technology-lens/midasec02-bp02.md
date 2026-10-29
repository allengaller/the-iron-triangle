<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC02-BP02 Enable multi-factor authentication (MFA) and token authorization (TA)

Strengthen identity verification by enforcing MFA for human users and implementing
 token-based authorization for machines and services.

**Desired outcome:** Stronger authentication for both human
 users and industrial systems accessing AWS resources.

**Benefits of establishing this best practice:** Reduces risks
 associated with credential theft and replay attacks across IT/OT boundaries.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Enable MFA across all accounts, and integrate token services for secure, time-bound
 access.

### Implementation steps

- Require MFA for all AWS accounts and IAM users using virtual or hardware devices.
- Implement SSO with MFA enforcement using AWS IAM Identity Center.
- Use temporary credentials and tokens through AWS Security Token Service for
 federated and service access.
- Enable and monitor MFA usage compliance with AWS Config rules.

## Resources

- [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
- [What is AWS Identity and Access Management Access Analyzer?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Welcome to the AWS Security Token Service API Reference](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
