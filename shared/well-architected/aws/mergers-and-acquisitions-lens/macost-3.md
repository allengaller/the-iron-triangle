<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-3.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MACOST 3: How do you plan for data transfer and storage charges in case of required data integration after mergers and acquisitions activity?

Plan and monitor data transfer charges so that you can make
 architectural decisions to minimize costs. A small yet
 effective architectural change can drastically reduce your
 operational costs over time.

## MACOST03-BP01 Perform data transfer modeling

Gather organization requirements, and perform data transfer modeling of the workload and each of its components. This identifies the lowest cost point for its current data transfer requirements.

## MACOST03-BP02 Select components to optimize data transfer cost

All components are selected, and architecture is designed to reduce data transfer costs. This includes using components such as wide-area-network (WAN) optimization and multi-Availability Zone (AZ) configurations.

## MACOST03-BP03 Implement services to reduce data transfer costs

Implement services to reduce data transfer. For example, using a content delivery network (CDN) such as Amazon CloudFront to deliver content to users, caching layers using Amazon ElastiCache, or using AWS Direct Connect instead of VPN for connectivity to AWS.

## MACOST03-BP04 Delete redundant data stores using policies

Manage the lifecycle of all your data, and automatically enforce deletion timelines to minimize the total storage requirements of your workload.

## MACOST03-BP05 Analyze data integration pattern of the combined organizations

Data is a combined organizational asset. Collect, store, organize, and process valuable data, and make it available in a secure way to the people and applications that need it.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-3.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
