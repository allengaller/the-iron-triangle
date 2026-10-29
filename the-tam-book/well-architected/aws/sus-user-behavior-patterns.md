<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/framework/sus-user-behavior-patterns.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Alignment to demand

The way users and applications consume your workloads and other resources can help you identify improvements to meet sustainability goals. Scale infrastructure to continually match demand and verify that you use only the minimum resources required to support your users. Align service levels to customer needs. Position resources to limit the network required for users and applications to consume them. Remove unused assets. Provide your team members with devices that support their needs and minimize their sustainability impact.

The following question focuses on this consideration for sustainability:

The way users and applications consume your workloads and other resources can help you identify improvements to meet sustainability goals. Scale infrastructure to continually match demand and verify that you use only the minimum resources required to support your users. Align service levels to customer needs. Position resources to limit the network required for users and applications to consume them. Remove unused assets. Provide your team members with devices that support their needs and minimize their sustainability impact.

Scale infrastructure with user load: Identify periods of low or no utilization and scale
 resources to reduce excess capacity and improve efficiency.

Align SLAs with sustainability goals: Define and update service level agreements (SLAs)
 such as availability or data retention periods to minimize the number of resources required
 to support your workload while continuing to meet business requirements.

Decrease creation and maintenance of unused assets: Analyze application assets (such as
 pre-compiled reports, datasets, and static images) and asset access patterns to identify
 redundancy, underutilization, and potential decommission targets. Consolidate generated
 assets with redundant content (for example, monthly reports with overlapping or common datasets and outputs) to reduce the resources consumed when duplicating outputs. Decommission
 unused assets (for example, images of products that are no longer sold) to release consumed
 resources and reduce the number of resources used to support the workload.

Optimize geographic placement of workloads for user locations: Analyze network access
 patterns to identify where your customers are connecting from geographically. Select Regions
 and services that reduce the distance that network traffic must travel to decrease the total
 network resources required to support your workload.

Optimize team member resources for activities performed: Optimize resources provided to
 team members to minimize the sustainability impact while supporting their needs. For
 example, perform complex operations, such as rendering and compilation, on highly used
 shared cloud desktops instead of on under-utilized high-powered single user systems.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/framework/sus-user-behavior-patterns.html（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
