<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost08-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNCOST08-BP01 Regular cost analysis

Review cost dashboards to identify underutilized resources,
 anomalous spikes, and opportunities to switch connectivity types.

**Desired outcome:** Data-driven cost
 reduction through continuous refinement.

**Level of risk exposed if this best practice
 is not established:** Low

**Benefits of establishing this best
 practice:**

- Visibility into cost drivers
- Identification of legacy resources for decommissioning
- Support for budget forecasting

## Implementation guidance

- Identified data transfer changes in cost data, such as by
 filtering Cost and Usage data by line_item_usage_type for
 DataTransfer-Out-Bytes.
- Use cost dashboards to review usage patterns. For example, you
 can achieve this by using Amazon Athena and Amazon Quick
 Suite.
- Share findings in regular, weekly or monthly and FinOps
 reviews.

**Resources:**

- [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/data-transfer-cost-analysis.html)
- [AWS Well-Architected Cost & Usage Report Library](https://catalog.workshops.aws/cur-query-library/en-US/queries/networking-and-content-delivery)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost08-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
