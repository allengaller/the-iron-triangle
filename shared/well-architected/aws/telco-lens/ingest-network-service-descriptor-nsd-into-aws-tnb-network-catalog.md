<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/ingest-network-service-descriptor-nsd-into-aws-tnb-network-catalog.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Ingest network service descriptor (NSD) into AWS TNB network catalog

CSPs ingest the NSD, which describes the required compute and network resources, as
 well as the NFs to be deployed, into the AWS TNB network catalog.

**Recommendation:** Design the NSD to be modular and
 reusable, allowing for the creation of multiple network instances from a single template.
 Leverage AWS TNB's support for ETSI SOL003/SOL005 APIs to integrate with existing ETSI-based
 service orchestrators.

**Practical advice:** Thoroughly test the NSD in a
 non-production environment to verify the correct mapping of resources and NFs. Maintain
 version control of the NSD to enable updates and rollbacks.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/ingest-network-service-descriptor-nsd-into-aws-tnb-network-catalog.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
