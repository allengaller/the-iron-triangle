<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/scenario-a-user-and-audit-consent-for-data-storage-outside-country.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Scenario A: User and audit consent for data storage outside country

This scenario covers situations where regulations allow data
 storage outside the country with user consent as data subjects
 or the permission or notification of the regulators (or both).

![Scenario diagram covering user and audit consent for data storage outside the country](/images/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/images/scenario-A.jpg)

*Scenario A*

The use case diagram depicts the following:

- Organization A in Country B seeks consent from Individuals X
 (the data subjects).
- Validation checks the consent and verifies compliance.
- A precondition is validated based on Country B's
 regulations, which must be met before storing data in Region
 Y.
- If the precondition is satisfied, the data can be stored in
 Region Y, which may be outside of Country B. This suggests
 that the data storage could occur in a different
 geographical region while still complying with Country B's
 legal requirements.
- If the precondition fails, an Alternative Path is triggered,
 which may involve considering a different region or scenario
 that meets compliance requirements.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/scenario-a-user-and-audit-consent-for-data-storage-outside-country.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
