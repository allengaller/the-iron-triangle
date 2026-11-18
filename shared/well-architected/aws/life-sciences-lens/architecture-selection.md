<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/architecture-selection.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Architecture selection

When selecting architectures for genomic sequencing and molecular modeling, prioritize
 scalable compute patterns that efficiently handle variable workloads. Evaluate
 high-performance computing options with high memory-to-CPU ratios and GPU acceleration to
 optimize performance while maintaining data integrity for your scientific workflows.

Implement tiered storage strategies using hot to cold storage tiers for cost-efficient
 management of large scientific datasets while keeping sensitive patient records in encrypted
 database instances. Deploy auto scaling data processing pipelines that efficiently handle both
 high-velocity instrument data and carefully controlled clinical information flows.

Analyze workload characteristics to identify optimization targets. Deploy
 high-performance computing resources for research pipelines requiring massive parallel
 processing, while prioritizing availability and consistent performance for clinical
 applications. Use dedicated and isolated environments with tailored service configurations to
 meet distinct research and clinical requirements.

For long-term clinical trials, design architectures that maintain consistent performance
 over extended timeframes. Implement data lifecycle policies that optimize storage costs while
 preserving query performance. Deploy versioned infrastructure-as-code to create reproducible
 environments that can be efficiently recreated years later for regulatory adherence.

###### Best practices

- [LSPERF01-BP01 Design and benchmark computing architecture for genomic workloads to optimize cost-performance ratio](./lsperf01-bp01.html)
- [LSPERF01-BP02 Specialized hardware selection and optimization for genomic and molecular workloads](./lsperf01-bp02.html)
- [LSPERF01-BP03 Performance optimizations should validate data integrity](./lsperf01-bp03.html)
- [LSPERF02-BP01 Data-aware storage tiering](./lsperf02-bp01.html)
- [LSPERF02-BP02 Secure data separation by classification](./lsperf02-bp02.html)
- [LSPERF02-BP03 Elastic data processing pipelines](./lsperf02-bp03.html)
- [LSPERF03-BP01 Workload-specific performance analysis](./lsperf03-bp01.html)
- [LSPERF03-BP02 Environment isolation by workload type](./lsperf03-bp02.html)
- [LSPERF03-BP03 Tailored service configuration by use case](./lsperf03-bp03.html)
- [LSPERF04-BP01 Performance consistency through clinical trial lifetime](./lsperf04-bp01.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/architecture-selection.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
