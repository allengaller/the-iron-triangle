<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-interactions-in-a-distributed-system-to-prevent-failures.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Design interactions in a distributed system to prevent failures

Distributed systems rely on communications networks to interconnect components, such as
 servers or services. Your workload must operate reliably despite data loss or latency in these
 networks. Components of the distributed system must operate in a way that does not negatively
 impact other components or the workload. These best practices prevent failures and improve
 mean time between failures (MTBF).

###### Best practices

- [REL04-BP01 Identify the kind of distributed systems you depend on](./rel_prevent_interaction_failure_identify.html)
- [REL04-BP02 Implement loosely coupled dependencies](./rel_prevent_interaction_failure_loosely_coupled_system.html)
- [REL04-BP03 Do constant work](./rel_prevent_interaction_failure_constant_work.html)
- [REL04-BP04 Make mutating operations idempotent](./rel_prevent_interaction_failure_idempotent.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-interactions-in-a-distributed-system-to-prevent-failures.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
