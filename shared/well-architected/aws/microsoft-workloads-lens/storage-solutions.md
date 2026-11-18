<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/storage-solutions.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Storage solutions

Selecting appropriate storage solutions is critical for Microsoft
 workload performance, as storage often becomes a bottleneck for
 Windows applications and SQL Server databases. AWS offers various
 storage options from different EBS volume types to fully managed
 services like Amazon FSx for Windows File Server and FSx for ONTAP. Understanding the performance characteristics, use cases, and
 cost implications of each storage option enables organizations to
 optimize their Microsoft workloads for both performance and
 efficiency.

AWS offers different storage options that can address different
 needs for your Microsoft workloads. Appropriate storage options can
 be used by your Windows machines to bring the performance efficiency
 needed by your workload.

###### Best practices

- [MSFTPERF03-BP01 Consider Amazon EBS gp3 volumes for general workloads](./msftperf03-bp01.html)
- [MSFTPERF03-BP02 Consider Amazon EBS io2 Block Express volumes for high-intense I/O workloads](./msftperf03-bp02.html)
- [MSFTPERF03-BP03 Consider Amazon FSx for Windows File Server](./msftperf03-bp03.html)
- [MSFTPERF03-BP04 Consider Amazon FSx for NetApp ONTAP](./msftperf03-bp04.html)
- [MSFTPERF03-BP05 Leverage instance store temporary block storage for EC2 instances](./msftperf03-bp05.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/storage-solutions.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
