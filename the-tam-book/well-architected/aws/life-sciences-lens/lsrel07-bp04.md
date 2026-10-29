<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel07-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSREL07-BP04 Track data lineage with lifecycle metadata

Assign metadata tags (for example, raw,
 filtered, processed, and
 analyzed) at each lifecycle stage, so data state
 is visible. This enables reproducibility, auditing, and debugging
 when results need to be traced back to raw inputs. Use catalogs and
 governance tools to track lineage across storage and processing
 layers.

**Desired outcome:** Data state is
 transparent across ingestion, processing, and analysis, with lineage
 records supporting reproducibility and audits.

**Common anti-patterns:**

- Failing to label datasets by processing stage.
- Storing derived data without linkage to raw inputs.
- Using inconsistent or unstructured metadata practices.

**Benefits of establishing this best
 practice:**

- Enables reproducibility by tracing results back to raw data.
- Simplifies compliance-related audits by showing how data was
 transformed.
- Reduces troubleshooting time by quickly identifying the source
 of anomalies.

**Level of risk exposed if this best practice
 is not established:** Medium

## Implementation guidance

Every dataset should be tagged with lifecycle metadata reflecting
 its stage: raw, filtered,
 processed, or analyzed.
 Lineage metadata should include transformation steps, software
 versions, and parameter settings. These lineage records must be
 centralized in a catalog or metadata repository to provide
 transparency across the workload.

### Implementation steps

1. Store datasets in Amazon S3 with metadata tags to reflect
 their lifecycle stage.
2. Use AWS AWS Glue Data Catalog to maintain a centralized record
 of lineage and transformations.
3. Capture transformation metadata during pipeline execution
 using AWS Step Functions or AWS Lambda and store results in
 Amazon DynamoDB or Amazon OpenSearch Service.
4. Include metadata in evidence packages for GxP-regulated
 workloads.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel07-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
