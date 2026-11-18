<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus11.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# FSISUS11: Do you store processed data or raw data?

## FSISUS11-BP01 Use processed data to reduce your storage footprint

Often raw data from your data sources may include a large number of observations from
 streaming data sources that continually produce data or include large amounts of redundant
 data from a variety of sources. You can reduce your storage requirements by first
 processing the raw data, then storing only the results. Unless you have a raw data
 retention compliance policy or requirement, you can purge the raw data automatically
 shortly after processing to reduce your data storage requirements.

Store processed generative AI training data rather than raw data when compliance
 allows. Implement efficient vector storage strategies for generative AI applications.
 Optimize vector lengths for embedded tokens in generative AI systems.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus11.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
