<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops06-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSOPS06-BP01 Validate data quality during ingestion

Define data quality measurements and implement checks during
 ingestion.

**Desired outcome:** Data is clean
 and ready for analysis upon ingestion.

**Benefits of establishing this best
 practice:**

- More trusted results.
- Faster output to conclusions.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

Build data quality checks into data ingestion pipelines.

Plan to isolate erroneous data and have a way to review it as
 needed.

### Implementation steps

1. Identify expected patterns in received data.
2. Build data quality checks in AWS Glue Data Quality.
3. Incorporate checks in data pipelines.
4. Build processes to catch and isolate erroneous data. Alert
 personnel to investigate data errors

## Resources

**Related examples:**

- [Measure
 performance of AWS Glue Data Quality for ETL pipelines](https://aws.amazon.com/blogs/big-data/measure-performance-of-aws-glue-data-quality-for-etl-pipelines/)

**Related tools:**

- [AWS Glue](https://aws.amazon.com/glue/)
- [AWS Glue Data Quality](https://aws.amazon.com/glue/features/data-quality/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops06-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
