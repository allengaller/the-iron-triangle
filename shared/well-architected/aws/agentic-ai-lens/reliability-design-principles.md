<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/reliability-design-principles.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Design principles

In addition to the lens-level design principles, the reliability best practices in this lens are represented by at least one of the following principles:

- **Decouple agents through durable messaging:** Persistence, retry, and dead-letter handling absorb transient failures inside the messaging layer instead of cascading them through synchronous call chains.
- **Constrain blast radius through atomic responsibilities:** Single-task agents with the minimum permissions and clear instructions limit how far any individual failure or misbehavior can propagate.
- **Recover from the last known good state, not the beginning:** Checkpointed workflows, idempotent steps, and graceful degradation let work resume after a fault rather than restart from scratch.
- **Make multi-agent coordination resilient by design:** Arbiter patterns, capability taxonomies, and fallback paths keep collaborative workflows running when individual agents become unavailable or unreliable.
- **Ground reasoning in verifiable evidence:** Retrieval from authoritative sources, explicit citation, and hallucination detection keep agent outputs traceable to real data instead of fabricated content.
- **Exercise failure paths regularly:** Inject faults, run degraded-dependency tests, and rehearse recovery procedures. The first time a failure mode occurs should not be in production.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/reliability-design-principles.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
