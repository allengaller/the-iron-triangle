<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel08.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Graceful degradation and configuration management

Agents that detect degradation accurately through thorough
 telemetry and maintain consistent configuration across all
 instances make informed decisions about when to activate graceful
 degradation. Consistent configuration management helps agents have
 reliable, up-to-date information about capabilities and
 limitations across the agent environment.

## Capability intent

- Agent configuration lives in a central, versioned,
 schema-validated source, so every instance runs the same
 current settings and drift is detected automatically.
- Configuration changes roll out gradually with automatic
 rollback, and sensitive values are held in encrypted
 parameter storage with fine-grained access control.
- Stage-level telemetry covers every phase of agent processing
 (context retrieval, inference, tool execution, response
 generation), so degradation decisions are informed rather
 than reactive.
- Anomaly detection and composite alarms combine signals
 across stages into a single useful health state, triggering
 graceful degradation automatically.
- Resource isolation separates high-priority user-facing
 agents from background workloads, and contention is detected
 through composite scores before it causes failures.
- Memory utilization is tracked per tier (in-context,
 short-term session, long-term persistent) with automated
 responses for summarization, pruning, and consolidation
 before exhaustion produces silent failures.

## Common issues to watch for

- Configuration is hardcoded or partially centralized, so
 parameter changes require redeployment and configuration
 drift between instances is detected only through downstream
 failures.
- Configuration changes are applied without validation or
 staged rollout, which lets misconfigured values reach
 production and degrade agent behavior instantly.
- Telemetry is captured only at the request boundary, so a
 rise in overall latency or error rate provides no signal
 about which processing stage is responsible.
- All agents share a single resource pool and upstream quota,
 so a high-volume background agent degrades the latency of
 user-facing agents and throttling cascades across workloads.
- Memory monitoring stops at infrastructure metrics, so
 in-context exhaustion and gradual memory leaks produce
 silent output degradation with no leading indicator.
- Static alarm thresholds either fire too often during routine
 traffic shifts or miss gradual degradation, so graceful
 degradation activates reactively rather than proactively.

###### Best practices

- [AGENTREL08-BP01 Establish consistent configuration management practices](./agentrel08-bp01.html)
- [AGENTREL08-BP02 Implement agent tracing for telemetry throughout agent processing](./agentrel08-bp02.html)
- [AGENTREL08-BP03 Architect agent systems with resource isolation and contention mitigation](./agentrel08-bp03.html)
- [AGENTREL08-BP04 Track agent memory utilization metrics](./agentrel08-bp04.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel08.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
