<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops08-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCOPS08-BP01 Adopt a mandatory and formalized process for managing any changes to EUC services and dependent infrastructure

Create a new process or integrate with existing processes that track all changes that
 can affect the stability and security of your EUC deployment.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Track all changes which might directly or indirectly affect the performance and
 availability of Amazon WorkSpaces or Amazon WorkSpaces Applications services. Implement a change control
 process that documents each service update with a robust risk assessment and back-out plan
 and involves technology stakeholders from all relevant areas. This process can reduce the
 risk of service outages or degradation.

Both WorkSpaces and Amazon WorkSpaces Applications have key dependencies on many external services.
 If changes to any of these services is required, a representative from the AWS EUC team
 should be part of the change control team to review and quantify the risk of the change.

The service dependencies for Amazon WorkSpaces and Amazon WorkSpaces Applications include, but are not
 restricted to:

- AWS networking
- Active Directory and connectors
- RADIUS
- Microsoft PKI (if certificate-based authentication is in use)
- Third Party PKI services that may be used to allocate public certificates for
 related services
- AWS KMS if used for encryption of WorkSpaces images
- SAML 2.0 IdP availability (if SAML 2.0 authentication is in use)
- Private certificate authority (if certificate-based authentication is in use)
- User data repositories (like file shares or profile stores)
- Application web tiers
- Application database tiers
- Application licensing servers
- Web proxies
- Firewalls and other related security infrastructure
- Anti-malware infrastructure
- Thin client management infrastructure

Amazon WorkSpaces and Amazon WorkSpaces Applications also use other AWS services, such as Amazon EBS and
 Amazon S3 for storage, so you should understand any changes being made to these systems.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops08-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
