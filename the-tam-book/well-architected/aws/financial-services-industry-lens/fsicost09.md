<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost09.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# FSICOST09: Are you using the cost advantages of tiered storage?

FSI companies usually have long retention policies for their regulatory and audit
 requirements. They usually span multiple years and might even be able to take up to a day or
 two to be able to retrieve old data. Understand and use the cost advantages of tiered
 storage.

## FSICOST09-BP01 Define data retention policies to select the right storage type for your data lifecycle

FSI companies usually have long retention policies for their regulatory and audit
 requirements. They usually span multiple years and might even be able to take up to a day
 or two to be able to retrieve old data. Defining data retention policies and corresponding
 architecture to transfer data from main storage to archival storage is important. This can
 be achieved by transferring data from RDS database to S3 or creating a snapshot and
 storing it for better cost efficiencies.

Apply lifecycle policies for Retrieval-Augmented Generation (RAG) artifacts and
 generative AI datasets: maintain hot vector indexes (for current-quarter documents or
 active knowledge bases) in high-performance vector databases, transition warm data
 (historical embeddings or older training data) to object storage such as Amazon S3 Standard–IA,
 and archive cold or infrequently accessed corpora (for example, legacy PDFs, or processed
 embeddings) in Amazon Glacier or Deep Archive. Automate transitions using S3 Lifecycle policies to
 minimize long-term storage costs while preserving retrieval fidelity when needed.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost09.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
