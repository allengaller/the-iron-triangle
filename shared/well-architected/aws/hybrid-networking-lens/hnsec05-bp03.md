<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec05-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSEC05-BP03 Use application layer encryption

Applying TLS encryption at the application layer ensures data
 confidentiality even when transmitted over untrusted networks. For
 optimal security, use certificates for authentication where
 available and ensure encryption requirements follow the latest
 standards and best practices, allowing only secure protocols with
 strong cipher suites that are regularly monitored and updated.

**Desired outcome:** Ensure that data
 remains protected on lower-speed or hosted Direct Connect
 connections.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Protects sensitive data regardless of Direct Connect speed or
 type
- Enables flexibility with software or application-based
 encryption
- Maintains compliance with security policies and data protection
 requirements
- Ensures end-to-end encryptions for all workloads

## Implementation guidance

- For application-layer encryption, use TLS/SSL for all
 sensitive communications.
- Use certificate-based authentication where possible.
- Periodically test and review encryption configurations and key
 management.

## Resources

- [Encryption
 in transit over external networks: AWS guidance for NYDFS and
 beyond](https://aws.amazon.com/blogs/security/encryption-in-transit-over-external-networks-aws-guidance-for-nydfs-and-beyond/)
- [Hybrid
 Connectivity AWS Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/hybrid-connectivity.pdf).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec05-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
