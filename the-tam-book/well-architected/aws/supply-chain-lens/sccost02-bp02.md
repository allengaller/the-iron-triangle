<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost02-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# SCCOST02-BP02 Query and retrieve data by partitions to save cost and improve performance

Optimize data access by using partitioned queries to enhance
 cost-efficiency and performance in supply chain systems.

**Desired outcome:** Data access
 requirements are taken into consideration while defining data
 storage strategy.

**Benefits of establishing this best
 practice:** Reduced cost, optimized performance, and
 better customer satisfaction

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

Organize supply chain data by time, geography, or other relevant
 criteria to enhance storage efficiency and reduce retrieval
 costs.

Implement data partitioning strategies to divide large volumes
 into manageable chunks based on specific characteristics like
 time or product ID, focusing query operations on relevant
 segments and reducing scanned data volume and associated costs.

### Implementation steps

1. Analyze supply chain data access patterns to identify
 optimal partitioning strategies based on time, geography,
 or product categories.
2. Implement data partitioning in storage systems to organize
 data into logical segments that align with query patterns.
3. Configure query engines to use partition pruning to scan
 only relevant data segments during retrieval operations.
4. Use AWS Glue for automated data partitioning and Amazon S3's integrated compression options to further reduce
 costs.
5. Implement partition management processes to maintain
 optimal partition sizes and help prevent partition
 proliferation.
6. Monitor query performance and costs to continuously
 optimize partitioning strategies and data organization.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost02-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
