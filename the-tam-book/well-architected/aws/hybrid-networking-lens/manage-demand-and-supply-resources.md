<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/manage-demand-and-supply-resources.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Manage demand and supply resources

Effectively managing demand and supply resources in hybrid networking environments
 requires a strategic approach that balances on-premises infrastructure with cloud resources.
 Organizations should implement scaling mechanisms that dynamically adjust network resources
 based on real-time traffic patterns and application demands.

Effective hybrid networking requires alignment between resource supply and fluctuating
 demand. Since scaling hybrid connectivity components like dedicated connections often involves
 significant lead times, forward planning becomes crucial. Organizations should implement a
 proactive approach that combines early provisioning for anticipated future needs with regular
 performance testing to identify bottlenecks. This balanced strategy ensures seamless
 connectivity across on-premises and cloud environments while maintaining cost-effectiveness,
 preventing both expensive over-provisioning and performance-limiting under-allocation.

Prioritizing traffic ensures mission-critical applications such as VoIP and real-time
 data to receive guaranteed bandwidth, while non-critical traffic such as backups uses
 remaining capacity. This prevents congestion and aligns costs with business priorities.

###### Best practices

- [HNCOST05-BP01 Forecast demand and baseline requirements before scaling dedicated connections](./hncost05-bp01.html)
- [HNCOST06-BP01 Implement QoS policies for traffic prioritization](./hncost06-bp01.html)
- [HNCOST06-BP02 Separate traffic classes for dedicated connections](./hncost06-bp02.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/manage-demand-and-supply-resources.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
