<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Secure agent memory and state

One reason agentic AI is effective is the ability to perform
 long-running tasks. To achieve a goal, agents need to store
 context, tasks, and results. Agent memory systems can be targeted
 to introduce false information or influence agent decisions, so
 securing memory and state helps maintain agent integrity.

## Capability intent

- Agent memory is partitioned along the isolation axes that
 matter for the workload, with each principal restricted to
 the namespaces its task requires.
- Tamper detection runs on every memory read, and an
 append-only versioned history supports forensic replay when
 a poisoning attempt is suspected.
- Every write path into memory, including user inputs, tool
 outputs, inter-agent messages, and consolidation, passes
 through a layered validation pipeline before data reaches
 the store.
- Hallucinations are detected and contained before they
 cascade across sessions or propagate to downstream agents in
 a multi-agent workflow.
- Memory operations are monitored continually, and anomalous
 access or injection signals are routed to the incident
 response pipeline for review.

## Common issues to watch for

- Shared namespaces treated as the default rather than an
 explicit design decision, so one affected session can read
 or overwrite context that belongs to a different user or
 tenant.
- Validation applied only at the public API boundary, whereas
 tool outputs, inter-agent messages, and consolidation writes
 bypass the pipeline. This creates a blind spot for content
 that originates inside the agent system.
- Model outputs written directly into long-term memory without
 grounding checks, so hallucinated facts persist across
 sessions and compound because each agent builds its
 reasoning chain on fabricated context from earlier runs.
- Monitoring that captures memory events but routes no signals
 into alerts or incident response, so poisoning and
 propagation are discovered only during post-incident review.
- Memory access policies that are set once at deployment and
 never revisited, so permissions drift as the agent system
 evolves and the least-privilege posture decays over time.

###### Best practices

- [AGENTSEC01-BP01 Implement memory isolation and integrity controls](./agentsec01-bp01.html)
- [AGENTSEC01-BP02 Validate and sanitize memory inputs](./agentsec01-bp02.html)
- [AGENTSEC01-BP03 Monitor for hallucination propagation](./agentsec01-bp03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
