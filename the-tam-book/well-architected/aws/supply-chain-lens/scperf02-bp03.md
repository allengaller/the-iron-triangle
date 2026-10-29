<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf02-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# SCPERF02-BP03 Use edge compute capabilities for supply chain applications

AWS offers a robust suite of edge computing solutions that extend
 cloud capabilities closer to end users, devices, and on-premises
 locations. At the core of AWS's edge computing strategy are two
 main services: AWS Outposts and AWS Local Zones.

**Desired**
**outcome:** These edge compute
 capabilities enable a single-digit millisecond latency for
 applications like supply chain which needs real-time edge data to
 perform machine learning inferences and action autonomously
 without pushing the decision making at the cloud.

**Benefits of establishing this best
 practice:** Agility, performance, and low latency.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

AWS offers a robust suite of edge computing solutions that
 extend cloud capabilities closer to end users, devices, and
 on-premises locations. At the core of AWS's edge computing
 strategy are two main services: AWS Outposts and AWS Local
 Zones. AWS Outposts brings native AWS services, infrastructure,
 and operating models to virtually any datacenter or on-premises
 facility. It's ideal for workloads requiring low latency access
 to on-premises systems, local data processing, or data residency
 requirements. AWS Local Zones are infrastructure deployments
 that place compute, storage, database, and other AWS services
 closer to large population and industry centers. Local Zones act
 as an extension of an AWS Region, connected through
 high-bandwidth, secure connections.

### Implementation steps

1. Assess supply chain operations to identify use cases that
 require low-latency processing or local data residency.
2. Deploy AWS Outposts for on-premises workloads that need
 AWS services with local data processing capabilities.
3. Implement AWS Local Zones for applications requiring
 ultra-low latency access to end users or manufacturing
 facilities.
4. Configure AWS IoT Greengrass for edge devices to enable
 local data processing and autonomous decision-making
 capabilities.
5. Establish secure connectivity between edge locations and
 central cloud infrastructure to maintain data
 synchronization.
6. Monitor edge computing performance and optimize resource
 allocation to facilitate efficient operation across
 distributed locations.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf02-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
