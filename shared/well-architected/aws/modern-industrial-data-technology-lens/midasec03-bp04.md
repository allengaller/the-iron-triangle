<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC03-BP04 Implement industrial encryption policies

Apply encryption policies across all layers of the manufacturing data system, including
 at rest, in transit, and optionally during processing, to help protect sensitive operational
 and proprietary information.

**Desired outcome:** Data remains encrypted end-to-end,
 providing confidentiality and integrity and helping with regulatory alignment.

**Benefits of establishing this best practice:** Reduces impact
 of data breaches, supports regulatory compliance, and builds trust with partners and
 customers.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Use AWS KMS for key management and enforce encryption using S3 bucket policies, VPC
 security, and service-level configurations.

### Implementation steps

- Enable default encryption on all data stores (for example, Amazon S3, Amazon RDS,
 Amazon Redshift, and Amazon DynamoDB).
- Use TLS 1.2+ for all data in transit.
- Create customer-managed keys (CMKs) using AWS KMS for sensitive workloads.
- Regularly rotate keys and audit access with AWS CloudTrail.

## Resources

- [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
- [Setting default server-side encryption behavior for Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
