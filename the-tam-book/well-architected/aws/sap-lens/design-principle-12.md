<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/design-principle-12.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# 12 – Plan for data recovery

**How do you plan for logical, data-related recovery for your SAP
 workload?** Work backwards from the business requirements to define an approach
 to recover or reconstruct your business data. Depending on how you have architected for
 resilience, different scenarios might fit in this category. At a minimum, your backup or
 disaster recovery (DR) posture should protect you from accidental deletion, logical data
 corruption, and malware. Be deliberate about the decision to restore, taking into account
 the time to return to service and the dependencies between systems.

| ID | Priority | Best Practice |
| --- | --- | --- |
| ☐ BP 12.1 | Required | Establish a method for consistent recovery of business data |
| ☐ BP 12.2 | Highly Recommended | Establish a method for recovering configuration data |
| ☐ BP 12.3 | Highly Recommended | Define a recovery approach for your complete SAP estate |
| ☐ BP 12.4 | Recommended | Conduct periodic tests to validate your recovery procedure |

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/design-principle-12.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
