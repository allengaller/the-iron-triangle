<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Disaster Recovery (DR) objectives

In addition to availability objectives, your resiliency strategy should also include
 Disaster Recovery (DR) objectives based on strategies to recover your workload in case of a
 disaster event. Disaster Recovery focuses on one-time recovery objectives in response to
 natural disasters, large-scale technical failures, or human threats such as attack or error.
 This is different than availability which measures mean resiliency over a period of time in
 response to component failures, load spikes, or software bugs.

**Recovery Time Objective (RTO)** Defined by the organization.
 RTO is the maximum acceptable delay between the interruption of service and restoration of
 service. This determines what is considered an acceptable time window when service is
 unavailable.

**Recovery Point Objective (RPO)** Defined by the organization.
 RPO is the maximum acceptable amount of time since the last data recovery point. This
 determines what is considered an acceptable loss of data between the last recovery point and
 the interruption of service.

![Timeline showing RPO before disaster, data loss period, RTO after disaster, and downtime period.](/images/wellarchitected/latest/reliability-pillar/images/business-continuity.png)

*The relationship of RPO (Recovery Point Objective), RTO (Recovery Time
 Objective), and the disaster event.*

RTO is similar to MTTR (Mean Time to Recovery) in that both measure the time between
 the start of an outage and workload recovery. However MTTR is a mean value taken over
 several availability impacting events over a period of time, while RTO is a target, or
 maximum value allowed, for a *single* availability impacting event.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
