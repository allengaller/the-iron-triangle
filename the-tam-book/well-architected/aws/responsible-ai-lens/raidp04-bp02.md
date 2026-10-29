<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp04-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# RAIDP04-BP02 Periodically evaluate and update datasets in the registry

Schedule regular review cycles that assess whether existing datasets
 still meet your evolving requirements and quality standards.
 Increment version numbers and update associated documentation
 whenever datasets change, maintaining records of what changed and
 why. Assess whether dataset updates require corresponding system
 retraining or evaluation re-runs to maintain validity of previous
 results. Remove or archive outdated dataset versions while
 preserving the ability to reproduce historical results when needed
 for auditing or comparison purposes.

**Level of risk exposed if this best practice
 is not established:** Medium

## Implementation considerations

1. Schedule review processes that automatically flag datasets for
 evaluation based on age, usage patterns, or changes in your
 system requirements.
2. Create change management workflows that require documenting
 the reason for a dataset modification along with version
 increments.
3. Compare new dataset versions against established quality
 metrics to catch degradation over time.
4. Design impact assessment procedures that assist you to decide
 when dataset changes require retraining your models or
 re-running evaluations.
5. Set up archival processes that move old dataset versions to
 long-term storage while keeping enough metadata to recreate
 historical results if needed.

## Resources

**Related documents:**

- [Data
 Analytics Lens : Best practice 7.2 – Monitor for data quality
 anomalies](https://docs.aws.amazon.com/it_it/wellarchitected/latest/analytics-lens/best-practice-7.2---monitor-for-data-quality-anomalies..html)
- [Generative
 AI lens: GENOPS02-BP02 Monitor foundation model metrics](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops02-bp02.html)
- [Data
 quality in Amazon SageMaker AI Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/data-quality.html)
- [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html)
- [Detecting
 data drift using Amazon SageMaker AI](https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/)
- [ISO/IEC
 42001:2023](https://www.iso.org/standard/42001) A.7.5 Data provenance

**Related tools:**

- [Amazon SageMaker AI Catalog](https://aws.amazon.com/sagemaker/catalog/)
- [AWS Glue Data Quality](https://aws.amazon.com/glue/features/data-quality/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp04-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
