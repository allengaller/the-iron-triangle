<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/reference-architecture-4.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Reference architecture

![Diagram showing QuickSight dashboard end-to-end design](/images/wellarchitected/latest/analytics-lens/images/quicksight-dashboard-design.png)

*Figure 6: QuickSight dashboard end-to-end design*

**Data sources:** Supports connection with traditional Data
 Warehouse or databases and also have the capacity to connect to non-traditional sources such
 as SaaS applications. Supported datasources in QuickSight include Amazon S3, Amazon Redshift, Amazon Aurora,
 Oracle, MySQL, Microsoft SQL Server, Snowﬂake, Teradata, Jira, and ServiceNow. Check [here](https://docs.aws.amazon.com/quicksight/latest/user/supported-data-sources.html)
 for the complete list of data sources supported in QuickSight. These data sources could be
 secured behind a private subnet and QuickSight can connect in a secure mechanism using
 strategies such as VPC endpoints, and secure firewalls.

**Visualization Tool:** Quick.

**Consumers:** Visual dashboard consumers accessing a QuickSight
 console or embedded QuickSight analytics dashboard.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/reference-architecture-4.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
