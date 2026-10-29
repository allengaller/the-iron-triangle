<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/practice-cloud-financial-management.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Practice Cloud Financial Management

HPC workloads can use a large number of resources in a short space of time. Use of cloud
 compute changes the way users decide what to run, where decisions on what jobs will be run are
 budget based. Using the following best practices, on-going expenditure can be tracked.

## HPCCOST01-BP01 Use the right tools to collect and analyze the data you need.

There are many ways to keep track of costs using the standard
 AWS tools, which will vary depending on the chosen architecture.
 Please refer to the
 [Cost Optimization Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).

### Implementation guidance

- For HPC applications, it is very common to use tagging.
 Resources used for jobs can be tagged with project names,
 user ids or any other attributes you choose. Once
 resources are tagged with tags activated for cost
 allocation, you can generate reports based on the
 attributes chosen earlier.
- If a queuing system, such as
 [Slurm](https://slurm.schedmd.com/documentation.html)
 or
 [IBM
 Spectrum LSF Suites](https://www.ibm.com/products/hpc-workload-management) is in use, they typically have
 ways to log the usage of resources, such as Slurm
 Accounting or LSF Analytics. Details vary depending on the
 system in use.

## Key AWS services

- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [Slurm
 accounting with AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/slurm-accounting-v3.html)
- [Metrics
 in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/practice-cloud-financial-management.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
