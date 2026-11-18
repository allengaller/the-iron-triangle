<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops10-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSOPS10-BP02 Store data in a format that works both for archiving and for active use by retaining related metadata

Select a data format which is queried while the project is ongoing
 but archives natively. Iceberg's data format is ideal for life
 sciences projects because it stores metadata alongside the data. It
 offers advanced data versioning, time travel capabilities, and
 schema evolution, essential features for maintaining data lineage
 and regulatory adherence while handling large-scale scientific
 datasets that frequently change over time.

**Desired outcome:** Have a portable
 dataset that contains the data and metadata in a single package

**Level of risk exposed if this best practice
 is not established:** Low

## Implementation guidance

Verify that the output of data processing results in portable data
 formats to allow for simple archiving.

### Implementation steps

1. Build standard data pipelines using AWS Glue
2. For deep analysis on structured data use Amazon Redshift.
3. Build a data lake of the data in Amazon S3 in Iceberg
 format.

## Resources

**Related documentsn:**

- [What
 is Apache Iceberg?](https://aws.amazon.com/what-is/apache-iceberg/)

**Related examples:**

- [Build
 a high-performance quant research platform with Apache
 Iceberg](https://aws.amazon.com/blogs/big-data/build-a-high-performance-quant-research-platform-with-apache-iceberg/)

**Related tools:**

- [Modernize
 Data Archiving](https://aws.amazon.com/archive/)
- [Amazon S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops10-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
