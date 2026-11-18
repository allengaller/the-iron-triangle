<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/optimize-over-time.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Optimize over time

You can optimize cost over time by reviewing new services and implementing them in your
 workload. As AWS releases new services and features, it is a best practice to review your
 existing architectural decisions to ensure that they remain cost effective. As your
 requirements change, be aggressive in decommissioning resources, components, and workloads
 that you no longer require. Consider the following best practices to help you optimize over
 time. While optimizing your workloads over time and improving your [CFM](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/practice-cloud-financial-management.html) culture in your organization, evaluate
 the cost

of effort for operations in the cloud, review your time-consuming cloud operations, and
 automate them to reduce human efforts and cost by adopting related AWS services, third-party
 products, or custom tools (like [AWS CLI](https://aws.amazon.com/cli/) or [AWS SDKs](https://aws.amazon.com/developer/tools/)).

**Optimize over time**

Establish a quarterly generative AI cost optimization cadence that includes:

- Re-running evaluation benchmarks to validate model price-performance ratios
- Re-ranking models by business criticality and cost per task
- Tuning RAG caches and vector retrieval thresholds
- Pruning inactive embeddings or knowledge bases to reduce silent storage growth
- Archiving old fine-tuning artifacts to lower storage and inference costs

This helps your generative AI workloads evolve with business demand, maintain cost
 efficiency, and prevent silent spend creep over time.

###### Best practice questions

- [FSICOST15: Have you reviewed your ongoing cost structure tradeoffs for your current AWS services lately?](./fsicost15.html)
- [FSICOST16: Are you continuously assessing the ongoing costs and usage of your cloud implementations?](./fsicost16.html)
- [FSICOST17: Are you continually reviewing your workload to provide the most cost-effective resources?](./fsicost17.html)
- [FSICOST18: Do you have specific workload modernization or refactoring goals in your cloud strategy?](./fsicost18.html)
- [FSICOST19: Do you use the cloud to drive innovation and operational excellence of your business model to impact both the top and bottom line?](./fsicost19.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/optimize-over-time.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
