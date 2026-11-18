<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/architecture-selection.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Architecture selection

There are multiple technology and design choices to consider when setting up hybrid
 networking connectivity on AWS. Each option has its own performance characteristics and
 considerations. Understand your performance requirements to make the right choice.

Carefully evaluate the application requirements, including bandwidth demands, latency
 sensitivity, and jitter tolerance. This evaluation should also encompass the geographical
 distribution of resources and users, scalability needs for future growth, security and
 compliance requirements, and the cost-effectiveness of different solutions like IPSec VPN or
 dedicated connectivity. By considering these elements, organizations can make informed
 decisions that align with specific needs and ensure a robust, efficient hybrid network
 infrastructure.

When selecting technology for high-performance hybrid networking architectures,
 organizations carefully evaluate their connectivity options based on specific workload
 requirements. Dedicated network connections offer consistent latency and higher bandwidth
 capabilities compared to virtual private networks operating over the internet. For
 mission-critical workloads requiring predictable performance, redundant dedicated connections
 are often the optimal choice, despite higher costs. Organizations should consider factors such
 as geographic distribution, bandwidth requirements, latency sensitivity, and budget
 constraints when selecting connectivity solutions. The chosen technology should balance
 performance needs with operational costs while ensuring reliability and scalability across
 multiple Regions.

###### Best practices

- [HNPERF01-BP01 Determine and define your performance requirements using bandwidth, latency and jitter values.](./hnperf01-bp01..html)
- [HNPERF01-BP02 Identify what applications and types of data will be transmitted over the network](./hnperf01-bp02.html)
- [HNPERF02-BP01 Use tradeoffs to improve network performance](./hnperf02-bp01.html)
- [HNPERF02-BP02 Choose the right physical PoP location for dedicated connectivity](./hnperf02-bp02.html)
- [HNPERF02-BP03 Choose the right termination endpoint in the cloud](./hnperf02-bp03.html)
- [HNPERF02-BP04 Select the most appropriate region for your workloads](./hnperf02-bp04.html)
- [HNPERF02-BP05 Plan for bandwidth scaling](./hnperf02-bp05.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/architecture-selection.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
