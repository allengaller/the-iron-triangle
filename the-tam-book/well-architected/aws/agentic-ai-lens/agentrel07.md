<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel07.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Agent monitoring, management and recovery

Agent systems that decompose workflows into recoverable stages,
 classify failures for targeted retry, and implement end-to-end
 distributed tracing recover smoothly from the failures that occur
 across their many components.

## Capability intent

- Agent workflows are decomposed into stages with persisted
 outputs and explicit validation between them, so failures
 are contained to the affected stage rather than cascading
 through the whole workflow.
- Failures are classified before any recovery action is taken,
 so retries apply to transient errors, fallbacks apply to
 persistent ones, and only genuinely unrecoverable failures
 reach human attention.
- Retries use exponential backoff with jitter and a retry
 budget, so widespread upstream failures don't produce
 unbounded retry storms.
- Self-healing responses address common failure patterns
 directly (prompt refinement, tool substitution, context
 reconstruction) before escalating to fallbacks.
- End-to-end distributed tracing covers every agent
 invocation, with agent-specific annotations and
 framework-level reasoning steps captured in the same trace
 view.
- Traces, metrics, and logs are correlated in unified
 dashboards, so operators diagnose incidents from evidence
 rather than by pivoting between tools.

## Common issues to watch for

- Long-running workflows run as monolithic processes, so a
 failure late in the workflow loses all progress and forces
 complete restart.
- Retry logic is applied uniformly to every failure, retrying
 non-retryable errors that will never succeed and delaying
 the human intervention that would resolve them.
- Retries run at fixed intervals without exponential backoff
 or jitter, producing thundering-herd effects that amplify
 incidents rather than recovering from them.
- Only retry-based recovery is implemented, so persistent
 failures after retries become user-visible errors instead of
 degrading through a fallback.
- Tracing stops at the application boundary or at queue
 boundaries, so debugging failures in multi-agent systems
 depends on manual log correlation across services.
- Traces are captured without agent-specific annotations, so
 trace queries can't be filtered down to the specific agent,
 task type, or model that failed.

###### Best practices

- [AGENTREL07-BP01 Design workflows in stages with incremental recovery](./agentrel07-bp01.html)
- [AGENTREL07-BP02 Enable automatic recovery from agent execution failures](./agentrel07-bp02.html)
- [AGENTREL07-BP03 Implement distributed tracing to track system dependencies and facilitate recovery](./agentrel07-bp03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel07.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
