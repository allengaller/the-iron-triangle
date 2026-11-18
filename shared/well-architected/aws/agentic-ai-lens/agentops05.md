<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Observability and monitoring for agentic systems

Observability in agentic systems requires capturing not just infrastructure metrics,
 but also agent reasoning steps, decision paths, and workflow execution patterns.
 Traditional monitoring approaches must be extended to provide visibility into agent
 behavior, tool invocations, and multi-agent interactions.

## Capability intent

- Agent executions produce distributed traces that capture reasoning steps,
 tool invocations, memory operations, and inter-agent handoffs, with trace
 context propagated across every service boundary.
- Behavioral baselines are continually maintained for each agent, and drift,
 anomalies, and performance degradation are detected automatically before
 they impact users.
- Agent decisions, actions, and reasoning are captured in structured,
 queryable logs and immutable, PII-safe audit trails that support debugging,
 compliance reporting, and forensic analysis.
- Workflow effectiveness is measured through a defined KPI framework
 covering operational, quality, efficiency, and business dimensions, and KPIs
 are reported to technical and business stakeholders on a regular
 cadence.
- Operators have workflow-specific dashboards that surface health,
 bottlenecks, and remediation runbooks within seconds, shortening mean time
 to detect and mean time to resolve for agent incidents.

## Common issues to watch for

- Organizations instrument infrastructure metrics but not agent-specific
 spans such as reasoning iterations, tool invocations, and memory
 operations.
- Teams implement tracing without propagating context across agent
 boundaries, producing disconnected trace fragments that can't be reassembled
 into the workflow operators need to diagnose incidents.
- Behavioral baselines are set once at deployment and never refreshed, so
 legitimate behavioral evolution generates false positive alerts while
 gradual drift that redefines the baseline goes undetected.
- Logs are stored in mutable storage without integrity controls or
 personally identifiable information (PII) redaction, weakening the
 evidentiary value of audit trails and creating data protection exposures at
 the same time.
- KPIs and dashboards are defined at launch and never revisited as workflows
 evolve, so organizations continue to measure metrics that no longer reflect
 what matters while new failure modes go unmonitored.

###### Best practices

- [AGENTOPS05-BP01 Establish end-to-end tracing and telemetry for agent operations](./agentops05-bp01.html)
- [AGENTOPS05-BP02 Monitor agent behavior patterns and detect anomalies](./agentops05-bp02.html)
- [AGENTOPS05-BP03 Implement structured logging and comprehensive audit trails](./agentops05-bp03.html)
- [AGENTOPS05-BP04 Define and track KPIs for agent workflows](./agentops05-bp04.html)
- [AGENTOPS05-BP05 Create workflow-specific dashboards for operational health](./agentops05-bp05.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
