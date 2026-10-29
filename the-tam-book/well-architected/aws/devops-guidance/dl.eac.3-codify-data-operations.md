<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.3-codify-data-operations.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# [DL.EAC.3] Codify data operations

**Category:** FOUNDATIONAL

Codifying data operations in a DevOps environment extends the infrastructure as code
 (IaC) principle to data management, which involves treating database schemas, data
 transformations, and data pipelines as code. Codifying data operations enables other DevOps
 capabilities including the use of data management pipelines for data lifecycle management,
 enforcing quality assurance and governance standards, providing auditability of changes, and
 the ability to rollback changes when necessary.

Store database schemas, along with any related procedures,
 views, and triggers, in version control systems alongside your
 application code. This enables the ability to track, review,
 and test schema changes before deploying them to your
 production environment. To start managing existing data source
 schemas as code, database migration and event analysis tools
 like
 [AWS DMS Schema Conversion Tool](https://aws.amazon.com/dms/schema-conversion-tool/) and
 [Amazon EventBridge](https://aws.amazon.com/eventbridge/) can help to infer schemas from existing
 data sources.

**Related information:**

- [Converting
 database schemas using DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html)
- [Creating
 an Amazon EventBridge schema](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema-create.html)
- [Using
 Amazon RDS Blue/Green Deployments for database
 updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.3-codify-data-operations.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
