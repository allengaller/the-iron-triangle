<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-interactions-in-a-distributed-system-to-mitigate-or-withstand-failures.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Design interactions in a distributed system to mitigate or withstand failures

Distributed systems rely on communications networks to interconnect components (such as
 servers or services). Your workload must operate reliably despite data loss or latency over
 these networks. Components of the distributed system must operate in a way that does not
 negatively impact other components or the workload. These best practices allow workloads to
 withstand stresses or failures, more quickly recover from them, and mitigate the impact of
 such impairments. The result is improved mean time to recovery (MTTR).

These best practices prevent failures and improve mean time
 between failures (MTBF).

###### Best practices

- [REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into soft dependencies](./rel_mitigate_interaction_failure_graceful_degradation.html)
- [REL05-BP02 Throttle requests](./rel_mitigate_interaction_failure_throttle_requests.html)
- [REL05-BP03 Control and limit retry calls](./rel_mitigate_interaction_failure_limit_retries.html)
- [REL05-BP04 Fail fast and limit queues](./rel_mitigate_interaction_failure_fail_fast.html)
- [REL05-BP05 Set client timeouts](./rel_mitigate_interaction_failure_client_timeouts.html)
- [REL05-BP06 Make systems stateless where possible](./rel_mitigate_interaction_failure_stateless.html)
- [REL05-BP07 Implement emergency levers](./rel_mitigate_interaction_failure_emergency_levers.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-interactions-in-a-distributed-system-to-mitigate-or-withstand-failures.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
