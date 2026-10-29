<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec01-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSEC01-BP02 Implement encryption in transit

Encryption in transit is essential for protecting data
 confidentiality as traffic moves between on-premises networks and
 cloud environments. All sensitive data traversing untrusted networks
 should be encrypted using strong protocols like TLS or IPsec.

**Desired outcome:** All sensitive
 data is protected during transmission, meeting regulatory mandates
 for confidentiality and data integrity.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Ensures confidentiality and integrity of sensitive data
- Meets requirements in regulations such as HIPAA, GDPR, and PCI
 DSS
- Reduces risk of breaches and compliance penalties
- Build customer and auditor trust

## Implementation guidance

- Establish encrypted connections between cloud and on-premises
 environments.
For example, you can use services such as AWS Site-to-Site VPN
 and AWS Direct Connect with MACsec.
- Enforce HTTPS/TLS for all application traffic between cloud
 and on-premises environments.
- Manage and rotate encryption keys according to compliance
 requirements.

## Resources

- [Encryption
 in AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html)
- [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
- [Choosing
 an AWS cryptography service](https://docs.aws.amazon.com/decision-guides/latest/cryptography-on-aws-how-to-choose/guide.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec01-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
