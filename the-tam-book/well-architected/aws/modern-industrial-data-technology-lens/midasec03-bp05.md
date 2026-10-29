<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC03-BP05 Implement data retention policies for each data class

Define and enforce data retention rules based on classification and regulatory
 requirements to reduce storage costs and minimize compliance risks.

**Desired outcome:** Only required data is retained, improving
 cost efficiency and reducing exposure of legacy data.

**Benefits of establishing this best practice:** Helps prevent
 unnecessary storage costs, reduce audit complexity, and support lifecycle compliance.

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Use Amazon S3 lifecycle policies, AWS Glue table TTLs, and tagging strategies to
 automate enforcement of retention policies.

### Implementation steps

- Define data retention durations based on classification and compliance needs.
- Apply tags and metadata to datasets to identify lifecycle requirements.
- Use S3 lifecycle rules or Glue jobs to delete or archive data.
- Regularly review and update retention policies based on changing regulations.

## Resources

- [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/index.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
