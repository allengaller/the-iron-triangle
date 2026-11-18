<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/infrastructure-security.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Infrastructure security in AWS Well-Architected

AWS Well-Architected Agent is in preview release and is subject to change.


As a managed service, AWS Well-Architected is protected by AWS global network security. For
 information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS
 environment using the best practices for infrastructure security, see [Infrastructure
 Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected
 Framework*.

You use AWS published API calls to access AWS Well-Architected through the network. Clients must
 support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
 Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
 such as Java 7 and later support these modes.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/infrastructure-security.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
