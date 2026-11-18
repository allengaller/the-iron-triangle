<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcrel02-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCREL02-BP01 Provision redundant power and network to on-premises components

To ensure high availability for AWS Outposts deployments,
 implement redundant power sources and network connectivity while
 considering multi-Outpost distribution across different
 Availability Zones.

**Desired outcome:** Achieve high
 availability of on-premises systems, helping to provide consistent
 data access and processing capabilities in compliance with data
 residency requirements.

**Benefits of establishing this best
 practice:** Redundant power and network infrastructure
 improves the reliability and availability of on-premises
 components, minimizing potential downtime.

**Level of risk exposed if this best
 practice is not established**: High

[Outpost
 Racks](https://docs.aws.amazon.com/outposts/latest/userguide/disaster-recovery-resiliency.html) are designed with redundant power and networking
 equipment. Customer racks will house
 individual [Outposts
 servers](https://docs.aws.amazon.com/outposts/latest/server-userguide/what-is-outposts.html). To meet high availability objectives, we recommend
 providing dual power sources and redundant network connectivity to
 Outposts and customer racks.

## Implementation guidance

- Provide dual power sources to Outposts and Customer racks.
- Provision redundant network connectivity (for example,
 redundant network devices) to Outposts.
- For higher availability, deploy applications on multiple
 Outposts, each attached to a different Availability Zone, to
 build additional application resilience and avoid dependence
 on a single Availability Zone.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcrel02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
