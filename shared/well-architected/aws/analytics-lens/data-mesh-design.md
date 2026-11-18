<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/data-mesh-design.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Design

The following are data mesh design goals:

- **Data as a product:** Each organizational domain owns their data end-to-end. They’re responsible for building, operating, serving, and resolving any issues arising from the use of their data. Data accuracy and accountability lies with the data owner within the domain.
- **Federated data governance:** Data governance helps ensure that data is secure, accurate, and the right personas have access to the right data. The technical implementation of data governance, such as collecting lineage, validating data quality, and enforcing appropriate access controls, can be managed by each of the data domains. However, central data discovery, reporting, and auditing is needed to make it easy for users to find data, and for auditors to verify compliance.
- **Common access:** Data must be easily consumable by subject matter experts, such as data analysts and data scientists, and by purpose-built analytics and machine learning (ML) services. This requires data domains to expose a set of interfaces that make data consumable while enforcing appropriate access controls and audit tracking.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/data-mesh-design.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
