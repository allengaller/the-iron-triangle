<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops07-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSOPS07-BP02 Isolate GxP data from non-GxP data

Take steps to isolate and segment GxP data from non-GxP data. In
 conjunction with the recommendations around data discovery and
 classification, separate GxP data so the organization can implement
 the necessary technical and administrative controls.

**Desired outcome:** Demonstrable
 division between GxP and non-GxP data.

**Common anti-patterns:**

- Granting access at a workload level grants access to the data,
 GxP and non-GxP.
- Retaining logs that are adjacent to GxP relevant metadata.
- Including GxP data in logs.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

Incorporate system separation, including table and row-level
 access controls.

### Implementation steps

1. Foster system separation though architecture design and
 deployment. Create distinct datastores (like Amazon S3 and
 Amazon RDS) for GxP data.
2. Implement table and row-level access controls through
 application logic.
3. Apply AWS Lake Formation rules for consistent control to
 data sets.
4. Produce evidence of verification of access controls.

## Resources

**Related tools:**

- [Amazon RDS](https://aws.amazon.com/rds/)
- [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
- [Amazon S3](https://aws.amazon.com/s3/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops07-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
