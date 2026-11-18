<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-refresh-cadence.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Recommendation refresh and data freshness

AWS Well-Architected Agent is in preview release and is subject to change.


AWS WA Agent keeps recommendations current through scheduled refresh cycles:

- **Scheduled refresh:** Resource and application
 recommendations are refreshed automatically on a weekly cadence after the initial set of
 recommendations is generated. You do not need to trigger this manually.
- **Cooldown periods:** Scheduled recommendation generation
 runs on a weekly cycle for the same profile. You cannot trigger resource or application
 recommendations on demand.

###### Note

Architecture recommendations are not part of the scheduled refresh cycle. They are
 generated on demand through architecture reviews. For more information, see [Conducting architecture reviews](./agent-architecture-reviews.html).

**Staleness detection:** Recommendation timestamps are
 updated during each refresh cycle, even when the recommendation content does not change. A
 recommendation without a recent timestamp update may no longer be relevant to your current
 environment.

**Infrastructure changes:** Changes to your environment (new
 resources, modified configurations) are picked up during the next scheduled refresh cycle.
 Recommendations are re-evaluated against the current state of your infrastructure at each
 refresh.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-refresh-cadence.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
