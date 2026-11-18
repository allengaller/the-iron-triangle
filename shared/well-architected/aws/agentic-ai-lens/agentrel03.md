<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Agent memory and state management

Agents that classify, persist, and recover memory reliably deliver
 consistent behavior across sessions and maintain functionality
 even during component failures. Agent memory is beholden to the
 same reliability considerations of any data store. How do you
 support returning the right information, and how does the agent
 behave when state is unavailable?

## Capability intent

- Agent memory is explicitly classified by scope and
 persistence, so short-term session context never
 contaminates long-term knowledge and retrieval is
 predictable across task types.
- Memory stores are redundant and have automated failover
 paths, so individual component failures produce degraded but
 usable memory rather than complete outages.
- Long-running workflows persist checkpoints at stage
 boundaries and resume from the last known-good state after
 interruption, rather than restarting from zero.
- Agents detect degraded memory conditions, transition into
 well-defined reduced modes, and communicate their current
 capabilities transparently to users and orchestration
 systems.
- Memory and state health are instrumented as first-class
 telemetry, so retrieval quality, failover activations, and
 checkpoint lifecycle are observable and operationally
 tunable.

## Common issues to watch for

- Teams store all agent memory in a single undifferentiated
 tier, so retrieval returns stale intermediate reasoning
 alongside stable domain facts and degrades task quality
 silently.
- Long-running workflows lack checkpointing, so any transient
 failure forces a full restart and the workflow pays its full
 cost every time something goes wrong.
- Workflow steps are not idempotent, so checkpoint-based
 replay produces duplicate side effects rather than safely
 resuming work.
- Memory outages are treated as agent outages because there is
 no degradation hierarchy, and users see confusing errors
 instead of clearly communicated reduced capability.
- Failover paths exist only on paper, and gaps in redundancy
 and recovery are discovered during production incidents
 because fault-injection testing isn't part of the release
 process.

###### Best practices

- [AGENTREL03-BP01 Design an information classification model to identify short-term and long-term memories](./agentrel03-bp01.html)
- [AGENTREL03-BP02 Architect fault-tolerant memory stores with redundancy and failover](./agentrel03-bp02.html)
- [AGENTREL03-BP03 Implement comprehensive state management and checkpoint-based recovery](./agentrel03-bp03.html)
- [AGENTREL03-BP04 Implement graceful degradation for memory and state operations](./agentrel03-bp04.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
