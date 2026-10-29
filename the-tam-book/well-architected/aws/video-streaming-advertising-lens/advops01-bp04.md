<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops01-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVOPS01-BP04 Establish data governance and compliance operations

Advertising data management requires robust governance and
 compliance procedures, especially in a multi-Region
 environment. This best practice verifies adherence to
 regional data privacy laws while maintaining operational
 efficiency across global advertising operations.

## Implementation guidance

- For data residency compliance alignment:
Implement landing zone controls for different
 geographical RegionsConfigure data boundary controls using AWS Control
 TowerSet up guardrails for data movement between RegionsMonitor and enforce data locality requirements
- For data governance:
Establish data classification policies for
 advertising data typesImplement data retention and archival proceduresSet up access controls and encryption policiesConfigure audit logging and compliance reporting
- For regulatory compliance alignment:
Implement GDPR requirements for EU user dataSet up consent management systemsMonitor compliance with regional advertising laws

## Key AWS services

- AWS Control Tower
- AWS Organizations
- AWS Config
- AWS CloudTrail
- Amazon Macie
- AWS Local Zones
- AWS Identity and Access Management

## Resources

- [Best Practices for managing data residency in AWS Local Zones using landing zone controls](https://aws.amazon.com/blogs/compute/best-practices-for-managing-data-residency-in-aws-local-zones-using-landing-zone-controls/)
- [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/)
- [Scale
 across borders: build a multi-Region architecture while
 maintaining data residency](https://community.aws/content/2dhVhtsciD5gVBlCKUlHoszrDzU/scale-beyond-borders?lang=en#aws-reference-architecture-for-multiregion-with-data-residency)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops01-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
