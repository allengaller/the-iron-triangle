<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dssec08.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Specialized data protection

Some sovereign workloads require protections that go beyond standard
 encryption at rest and in transit. Data that must stay protected
 during active computation needs confidential computing. Keys that
 must stay within a specific jurisdiction need a key management
 architecture that separates management roles from usage roles and
 constrains where key material can be stored.

This capability covers protecting data during compute with
 hardware-based isolation, and managing encryption keys under
 jurisdictional controls over key material, access, and auditability.

## Capability intent

- Sensitive data is protected during active computation through
 hardware-based isolation, so the underlying host, hypervisor,
 or operator can't access it.
- Encryption keys remain within approved jurisdictions
 throughout their lifecycle, including generation, storage,
 usage, and destruction.
- Key management responsibilities are separated between roles
 that administer the key infrastructure and roles that use keys
 for cryptographic operations.
- Cryptographic operations are auditable, with logs recording
 which key was used, by whom, and for what purpose.
- Key management architecture supports the operational
 requirements of multi-Region workloads without requiring key
 material to leave approved jurisdictions.

## Common issues to watch for

- Service-managed encryption keys used for workloads that
 require jurisdictional key control. These encrypt the data but
 give no sovereign control over the key material.
- Key policies that restrict access by identity but not by
 geographic constraints, allowing key operations from outside
 approved jurisdictions.
- Confidential computing deployed without attestation
 verification. This gives isolation but not the proof
 regulators need.
- Key administration and key usage combined in the same role,
 which makes one credential a single point of compromise for
 both management and decryption.
- Multi-Region workloads that replicate key material across
 jurisdictions for operational convenience, which undermines
 the residency controls the key management architecture was
 meant to enforce.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dssec08.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
