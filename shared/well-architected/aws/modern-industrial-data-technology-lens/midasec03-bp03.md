<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC03-BP03 Identify source data and set data classifications

Discover and classify data at the source (for example, sensors, PLCs, MES, and ERP
 systems) to apply appropriate controls from ingestion onward.

**Desired outcome:** Data is classified and governed from the
 moment it enters the system, helping prevent downstream risk exposure.

**Benefits of establishing this best practice:** Improves
 control over high-risk data, simplifies pipeline security, and enhances lineage tracking and
 compliance auditing.

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Build data ingestion pipelines with tagging and classification integrated into the
 ingestion and cataloging layers.

### Implementation steps

- Identify all upstream data sources contributing to the system.
- Use edge and gateway services to apply initial metadata or tags.
- Ingest data into AWS using services like Amazon Kinesis, AWS IoT Core, or AWS IoT SiteWise with classification.
- Catalog and tag datasets in AWS Glue or AWS Lake Formation.

## Resources

- [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
- [AWS Glue](https://aws.amazon.com/glue/)
- [What is AWS IoT SiteWise?](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
