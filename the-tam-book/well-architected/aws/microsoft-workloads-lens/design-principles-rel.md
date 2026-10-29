<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/design-principles-rel.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Design principles

- **Use Microsoft high availability patterns:** Implement SQL
 Server Always On Availability Groups across multiple Availability Zones, deploy Active
 Directory domain controllers with proper site topology, and use Exchange Database
 Availability Groups to maintain Microsoft workload resilience while benefiting from AWS
 infrastructure reliability.
- **Integrate with AWS managed services for Microsoft
 technologies:** Use Amazon RDS Multi-AZ for SQL Server, AWS Managed Microsoft AD for directory
 services, and Amazon FSx for Windows File Server to reduce operational overhead while maintaining Microsoft
 workload compatibility and using AWS managed reliability features.
- **Design for cross-AZ resilience with Microsoft-aware
 configurations:** Configure SQL Server listener endpoints across Availability
 Zones, establish Active Directory sites aligned with Availability Zones, implement
 SharePoint farm topology with cross-AZ redundancy, and verify that .NET applications
 handle Availability Zone failures gracefully through stateless design and proper load
 balancing.

For general reliability design principles that apply to all workloads, see [Design principles for reliability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/design-principles-rel.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
