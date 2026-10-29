<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/practice-cloud-financial-management-cfm.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Practice Cloud Financial Management (CFM)

Cloud Financial Management (CFM) allows finance, product, technology, and business
 organizations to manage, optimize, and plan costs as they grow their usage and scale on AWS.
 The primary goal of CFM is to allow customers to achieve their business outcomes in the most
 cost-efficient manner and accelerate economic and business value creation while finding the
 right balance between agility and control. AWS CFM offers a set of capabilities to manage,
 optimize, and plan for cloud costs while maintaining business agility. CFM is paramount not
 only to effectively manage costs, but also to verify that investments are driving expected
 business outcomes. The four pillars of the Cloud Financial Management Framework in the
 AWS Cloud are *see*, *save*,
 *plan*, and *run*. Each of these pillar areas has a set
 of activities and capabilities.

Expand showback and chargeback taxonomies to include generative AI-specific tags or Cost
 Categories such as `model_name`, `model_family`, `token_in`,
 `token_out`, `vector_store_ops`, `embedding_jobs`,
 `kb_storage_gb`, `agent_name`, and
 `safety_filters_triggered`. This enhances visibility into which generative AI
 components are driving spend and supports more precise forecasting and accountability.

Establish **model policy tiers** (for example, gold, silver,
 and bronze) that map business criticality to permitted models, context window sizes, and
 latency SLOs. Enforce these tiers through guardrails in CI/CD pipelines and API gateways to
 ensure cost discipline and consistent application of enterprise standards.

Following the best practices in CFM is essential for managing costs in your financial
 services workloads.

These Cloud Financial Management best practices help you establish cost transparency to
 control your resources and plan your spend to optimize your return on investments.

###### Best practice questions

- [FSICOST01: Is your cloud team educated on relevant technical and commercial optimization mechanisms?](./fsicost01.html)
- [FSICOST02: Do you apply the Pareto-principle (80/20 rule) to manage, optimize, and plan your cloud usage and spend?](./fsicost02.html)
- [FSICOST03: Do you use automation to drive scale for Cloud Financial Management practices?](./fsicost03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/practice-cloud-financial-management-cfm.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
