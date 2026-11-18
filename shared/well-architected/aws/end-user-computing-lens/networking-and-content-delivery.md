<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/networking-and-content-delivery.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Networking and content delivery

The optimal networking solution for a workload varies based on latency, throughput
 requirements, jitter, and bandwidth. Physical constraints, such as the location of users and
 data sources, will affect the performance of the solution.

In an EUC architecture, there are two key networking configurations to consider:

- Connections from end users to their most proximal AWS EUC service connection point
- Connections from the EUC instances to any backend infrastructure and other services

###### Best practices

- [EUCPERF06-BP01 Minimize latency between end users and EUC services](./eucperf06-bp01.html)
- [EUCPERF06-BP02 Minimize latency between EUC instances and dependent services](./eucperf06-bp02.html)
- [EUCPERF06-BP03 Make sure that EUC network configurations don't interfere with service management connections](./eucperf06-bp03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/networking-and-content-delivery.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
