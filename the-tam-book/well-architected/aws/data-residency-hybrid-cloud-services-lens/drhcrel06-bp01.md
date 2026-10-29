<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcrel06-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCREL06-BP01 Use AWS Health to receive EC2 instance retirement notifications and scheduled events on Outposts that may require instance failover ahead of time

Configure AWS Health event monitoring and maintain current
 operations contact information while ensuring adequate capacity to
 minimize impact during maintenance activities.

**Desired outcome:** Use AWS Health
 for getting AWS events signals and taking recommended actions,
 providing high availability while meeting data residency
 requirements.

**Benefits of establishing this best
 practice:** Using AWS Health for proactive notifications
 allows for timely planning and initiation of instance failovers,
 minimizing potential downtime while meeting data residency
 requirements during maintenance events.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

Monitor AWS Health events through
 [AWS EventBridge,](https://aws.amazon.com/eventbridge/)
[AWS Health API](https://docs.aws.amazon.com/health/latest/ug/health-api.html), or email. We recommend updating the correct
 contact information, especially the operations contact as
 described
 [in
 our accounts documentation so that the correct individuals
 receive these events.](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html) Provide sufficient capacity and
 highly available design to avoid any impact during maintenance
 activities.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcrel06-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
