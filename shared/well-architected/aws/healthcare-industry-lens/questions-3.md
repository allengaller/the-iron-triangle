<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/questions-3.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Questions

Datasets should be cleansed, tracked, and versioned to maintain their quality. Use a
 central Data Catalog to register and discover these datasets. Automate master data
 management processes to reduce burden and improve adoption. Label sensitive datasets with
 authorization enforced. Track licenses for applicable datasets. Standard healthcare
 ontologies are preferred over proprietary to promote reuse and data sharing.

Various public and private organizations maintain healthcare ontologies. The frequency
 of publication and methods of distribution vary widely. New concepts are added to these
 ontologies over time and others are deprecated. Automated processes for keeping the content
 updated reduce manual error-prone efforts and improve data quality. The publication of new
 content may be used to trigger this update process; otherwise, set up an automated schedule
 aligned with the content owner.

Health data lakes should store a copy of data in open standard formats (such as HL7,
 DICOM, standard genomic files like Binary Alignment Map (BAM), Compressed Reference-oriented
 Alignment Map (CRAM) and (g)VCF, XML, CSV, JSON, Parquet, or JPEG). Derivative copies of
 data may use non-standard formats to support downstream analytics. Storing health data
 in open formats expands the software that can be used to process the data, and may decrease
 the data transformations needed for interoperability.

Healthcare data access should follow least privilege. Access to the data should be
 granted to only those individuals who need it. Maintaining this access is greatly simplified
 using role-based and attribute-based mechanisms built on a common identity provider.
 Likewise, revoke access when no longer needed. Control access to individual datasets, but
 also verify that the user’s ability to combine datasets does not expose unintended risks.

Audit logs for access to all protected information must be maintained in a central
 immutable data store. Lock down permissions to audit logs. The logs must be maintained in
 accordance with your regulatory compliance. The logs can be migrated to lower-cost storage
 tiers automatically over time to reduce costs.

Many healthcare analytics use cases don’t require personally identifiable information.
 By deidentifying or redacting data, storing and accessing data becomes less risky. Use
 irreversible de-identification mechanisms to scrub sensitive information if it’s not needed
 by downstream consumers of the data.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/questions-3.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
