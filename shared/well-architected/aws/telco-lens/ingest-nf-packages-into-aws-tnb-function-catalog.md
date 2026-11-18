<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/ingest-nf-packages-into-aws-tnb-function-catalog.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Ingest NF packages into AWS TNB function catalog

CSPs ingest their 5G network function (NF) packages (for example, vCU, vUPF and vAMF)
 into the AWS TNB function catalog. These packages are in the form of a Cloud Service Archive
 (CSAR) file containing the NF descriptor, Helm charts, and custom scripts.

**Recommendation:** Work closely with NF vendors to verify
 the packages adhere to cloud design principles and meet the packaging requirements of
 AWS TNB. Establish a CI/CD pipeline to automate the ingestion of updated NF packages.

**Practical advice:** Thoroughly test the NF packages in a
 non-production environment before ingesting them into the production catalog. Maintain
 version control and cataloging of the NF packages to enable rollbacks and updates.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/ingest-nf-packages-into-aws-tnb-function-catalog.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
