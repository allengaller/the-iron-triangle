<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel06-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNREL06-BP02 Ensure service continuity with redundant hardware and diverse telecommunications providers

Implementing redundant hardware components across geographic
 locations, organizations can mitigate single points of failure that
 threaten critical workloads. This resilience strategy should extend
 beyond computing resources to include diverse telecommunications
 providers, creating independent network paths that remain
 operational even when regional carriers experience outages. The
 combination of hardware redundancy and carrier diversity creates a
 robust foundation that enables businesses to maintain operations
 through localized disruptions, ensuring that customers experience
 minimal service interruptions and that service level agreements
 remain intact despite infrastructure challenges.

**Desired outcome:** Reduce risk of
 connectivity loss due to hardware or carrier failures, maintaining
 consistent hybrid network availability.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Increases fault tolerance and uptime
- Minimizes downtime from single hardware or carrier outages
- Supports disaster recovery planning
- Helps meet or exceed AWS and provider SLA commitments

## Implementation guidance

- Use separate network devices and cables for each connection.
- Engage more than one telecom provider with diverse paths for
 "last mile" connections.
- Periodically review and test infrastructure and SLAs.

## Resources

- [AWS Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel06-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
