<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcrel05-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCREL05-BP01 Provision spare compute capacity following an N+M model

Provision spare compute capacity following an N+M availability
 model, where N is the required capacity and M is the spare
 capacity to accommodate server failures. Use features like Amazon EC2 Auto Scaling groups, shared storage services, and AWS Elastic
 Disaster Recovery for reliable recovery.

**Desired outcome:** Achieve high
 availability with sufficient spare capacity and seamless failover
 capabilities in hybrid environments while consistently meeting
 data residency requirements, even during hardware failures or
 maintenance events.

**Benefits of establishing this best
 practice:** The N+M model improves availability and
 resilience by providing buffer capacity to handle unexpected
 server failures or maintenance events, minimizing downtime and
 maintaining consistent performance while meeting data residency
 requirements.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

Use placement groups with a spread strategy to improve
 reliability across hardware components. Prepare for network,
 instances, compute, racks or data centers, and Availability Zone
 or Region failure modes, and adopt highly-available design.
 Implement redundant network paths, and map application
 dependencies to understand the impact of disconnect events.
 Provide sufficient network redundancy to meet your application's
 availability requirements.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcrel05-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
