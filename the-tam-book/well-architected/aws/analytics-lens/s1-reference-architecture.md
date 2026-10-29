<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/s1-reference-architecture.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Reference architecture

The following diagram illustrates the solution architecture and its key components for data cataloging, security, compliance, and data access requirements using DataHub.

![Reference architecture for data discovery](/images/wellarchitected/latest/analytics-lens/images/scenario-1-ref.png)

*Reference architecture for data discovery*

1. DataHub is an open-source metadata management platform which enables end-to-end discovery, data observability, data governance , data lineage and many more. It runs on an Amazon EKS cluster, using Amazon OpenSearch Service, Amazon Managed Streaming for Apache Kafka (Amazon MSK), and RDS for MySQL as the storage layer for the underlying data model and indexes.
2. Pull technical metadata from AWS Glue and Amazon Redshift to DataHub.
3. Enrich the technical metadata with a business glossary.
4. Run an AWS Glue job to transform the data and observe the data lineage in DataHub.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/s1-reference-architecture.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
