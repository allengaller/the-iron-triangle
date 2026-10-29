<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops04-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNOPS04-BP01 Monitor network service provider maintenance events

Implementing a proactive monitoring and response system for
 scheduled network maintenance activities is crucial for minimizing
 service disruptions. By establishing a methodical framework to track
 maintenance notifications and planned network events, teams can
 prepare effectively, strategically schedule necessary changes during
 designated maintenance windows, and ensure continuous network
 connectivity throughout the process. This systematic approach
 enhances operational resilience while reducing the impact of
 essential maintenance on critical services

**Desired outcome:**

- Get timely notifications about links connecting the on-premises
 data center to the cloud.
- Enables proper planning for scheduled activities, minimizes
 service disruptions, and ensures optimal management of hybrid
 network connectivity.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Proactive maintenance planning and reduces the risk of
 unexpected service disruptions.
- Better coordination during maintenance windows with business
 operations, minimizing impact on critical workloads.
- Enhanced visibility into service health and upcoming changes

## Implementation guidance

- Integrate service provider notifications into monitoring and
 observability platforms. For example, you can achieve this
 using Amazon EventBridge to send AWS Direct Connect
 maintenance messages.

## Resources

- [AWS Direct Connect maintenance](https://docs.aws.amazon.com/directconnect/latest/UserGuide/dx-maintenance.html)
- [Monitoring
 events in AWS Health with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)
- [How
 can I get notifications for AWS Direct Connect scheduled
 maintenance or events](https://aws.amazon.com/premiumsupport/knowledge-center/get-direct-connect-notifications/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops04-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
