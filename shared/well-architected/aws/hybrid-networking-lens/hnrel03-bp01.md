<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel03-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNREL03-BP01 Monitor the bandwidth and scale the bandwidth as needed

Regularly monitor the bandwidth usage of your dedicated connection.
 If usage consistently approaches the connection limit, order
 additional dedicated connections and aggregate them into a LAG to
 increase bandwidth and resilience with minimal downtime.

**Desired outcome:** Avoid service
 degradation or outages due to bandwidth limitations by proactively
 scaling your hybrid connectivity.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Prevent performance bottlenecks and dropped traffic
- Enables cost-effective scaling of hybrid network connectivity
- Supports growth in hybrid workload demand
- Ensures seamless failover and aggregation

## Implementation guidance

- Monitor metrics for all dedicated connection and IPSec VPN
 links.
- Create alarms for sustained high utilization.
- Plan and implement LAG to aggregate bandwidth and connections.

## Resources

- [How
 can I migrate virtual Interfaces to Direct Connect connections
 or LAG bundles?](https://repost.aws/knowledge-center/migrate-virtual-interface-dx-lag)
- [Direct
 Connect link aggregation groups (LAGs)](https://docs.aws.amazon.com/directconnect/latest/UserGuide/lags.html)
- [Monitoring
 Direct Connect with CloudWatch](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel03-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
