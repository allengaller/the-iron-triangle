<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/best-practices-rel.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best practices

HPC workloads can run for hours to days in duration, and often
 scale out to thousands and even millions of vCPUs. Traditionally,
 multiple users often access the same large system and require
 access to domain-specific applications. The best practices below
 provide guidance on how to best implement these reliability
 requirements on the cloud.

**Workload architecture**

- [HPCREL01-BP01 Consider instance type flexibility for your workload](./workload-architecture.html#hpcrel01-bp01)
- [HPCREL01-BP02 Deploy loosely coupled workloads across multiple Availability Zones](./workload-architecture.html#hpcrel01-bp02)

**Change management**

- [HPCREL02-BP01 Install software packages in a shared location to simplify multi-user, multi-resource software requirements management](./change-management.html#hpcrel02-bp01)
- [HPCREL02-BP02 Use package managers to simplify software dependency management when possible](./change-management.html#hpcrel02-bp02)

**Failure management**

- [HPCREL03-BP01 Implement checkpointing](./failure-management.html#hpcrel03-bp01)
- [HPCREL03-BP02 Use durable storage to store and back up datasets](./failure-management.html#hpcrel03-bp02)

###### Focus areas

- [Foundations](./foundations.html)
- [Workload architecture](./workload-architecture.html)
- [Change management](./change-management.html)
- [Failure management](./failure-management.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/best-practices-rel.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
