<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel03-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCREL03-BP01 Add redundancy to networking connections

Use a redundant networking architecture for Amazon WorkSpaces and WorkSpaces Applications,
 incorporating multiple Active Directory (AD) Controllers, AD connectors, DNS servers,
 gateways, VPNs, or AWS Direct Connect links. This approach supports continuous
 connectivity by providing alternative pathways for network traffic, reducing the risk of
 service disruptions due to network incidents and enhancing overall system resilience.
 Redundant networking helps mitigate the impact of network failures and supports
 uninterrupted access to WorkSpaces environments.

**Level of risk exposed if this best practice is not
 established:**High

## Implementation guidance

Enhance the resilience of Amazon WorkSpaces and WorkSpaces Applications by configuring
 redundant networking components such as VPN connections or AWS Direct Connect links.
 This setup provides alternative paths for network traffic, mitigating the impact of
 network incidents and supporting continuous access to WorkSpaces environments. Verify
 that you have multiple AD controllers and connectors across multiple Availability Zones.

Additionally, regularly monitor and test the redundant networking setup to check
 its effectiveness in maintaining continuous connectivity. Conduct failover tests and
 simulations to validate the redundancy configuration and identify any potential areas
 for improvement. By implementing redundant networking architecture, you can strengthen
 the resilience of your EUC environment and reduce the risk of downtime caused by network
 disruptions.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel03-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
