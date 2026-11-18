<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/cost-effective-resources.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Cost-effective resources

Cost-effective hybrid networking solutions strategically balance on-premises
 infrastructure with cloud services, optimizing resource allocation while minimizing
 unnecessary expenditure.

Selecting the most cost-effective hybrid networking solution requires understanding the
 connectivity needs of each workload. Not all workloads require the same level of bandwidth,
 reliability, or consistency. For non-critical or development workloads, internet-based VPN
 connections offer flexibility and lower costs, while production workloads with higher
 performance and reliability requirements may justify the investment in dedicated connections
 like dedicated connections. By starting with scalable, internet-based options during testing
 or migration, you can accurately assess your true bandwidth and performance needs before
 committing to more permanent and potentially costly solutions.

Data transfer costs can escalate quickly in hybrid environments. Optimization requires a
 combination of technical strategies (for example, compression) and architectural decisions
 (for example, region selection) to minimize unnecessary traffic and leverage cost-effective
 cloud services.

###### Best practices

- [HNCOST03-BP01 Implement tiered connectivity based on workload requirements](./hncost03-bp01.html)
- [HNCOST04-BP01 Implement data transfer optimization techniques](./hncost04-bp01.html)
- [HNCOST04-BP02 Select cost-effective regions and availability zones](./hncost04-bp02.html)
- [HNCOST04-BP03 Implement compression and caching for repetitive data transfers](./hncost04-bp03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/cost-effective-resources.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
