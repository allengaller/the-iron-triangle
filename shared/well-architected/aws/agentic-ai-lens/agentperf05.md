<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Workflow orchestration and multi-agent collaboration

The most impactful agent use cases (complex research, multi-domain
 customer service, and process automation) require multiple agents
 working together, and well-designed orchestration is what makes
 the whole greater than the sum of its parts. Complex agentic AI
 systems often involve multiple agents collaborating to solve tasks
 that exceed the capability of any single agent. Workflow
 orchestration coordinates these multi-agent interactions through
 patterns like supervisor-worker hierarchies, peer-to-peer
 collaboration, and pipeline-based task decomposition. The
 performance of multi-agent systems depends on how efficiently work
 is distributed, how agents are selected and invoked, how
 intermediate results are passed between agents, and how parallel
 execution is used to reduce latency.

## Capability intent

- Multi-agent workflows run with minimal orchestration
 overhead, so end-to-end latency approaches the critical path
 of dependent operations rather than the sum of every step.
- Orchestration patterns are matched to task shape, with
 dynamic graphs for reasoning-driven flows, Step Functions
 for deterministic skeletons, and hybrid layers for workflows
 that combine both.
- Independent subtasks run in parallel and large intermediate
 results are passed by reference, keeping the orchestration
 layer small and the critical path short.
- Collaboration models are matched to task characteristics
 (supervisor-worker, pipeline, peer-to-peer, swarm), and
 capabilities default to tools rather than sub-agents unless
 they need independent reasoning.
- Multi-stage pipelines use streaming and micro-batching to
 overlap stage processing, with right-sized compute per stage
 and end-to-end tracing that makes bottlenecks attributable.
- Delegation and handoff operations transfer only the context
 the receiving agent needs, through shared context stores and
 standardized interfaces, and handoff latency is a
 first-class metric.

## Common issues to watch for

- Teams default to sub-agents for capabilities that a tool
 call would handle in milliseconds, paying full
 reasoning-loop cost for deterministic, single-step work.
- Workflows run steps sequentially even when the dependency
 graph permits parallel execution, pushing end-to-end latency
 to the sum of step durations rather than the critical path.
- Dynamic graph orchestrations run without cycle detection,
 depth limits, or bounded fan-out, so the reasoning loop
 occasionally produces unbounded delegation chains or
 excessive concurrent branches.
- Orchestrators carry large payloads inline between steps
 rather than passing references, inflating state size and
 forcing the orchestrator's context window to hold raw data
 it doesn't need.
- Multi-stage pipelines use identical compute configurations
 for every stage, over-provisioning lightweight stages and
 starving compute-intensive ones, and skip streaming or
 micro-batching that could overlap stage processing.
- Delegation transfers the full conversation history on every
 handoff, receiving agents re-derive context the parent
 already had, and handoff latency isn't measured so the
 overhead grows silently.

###### Best practices

- [AGENTPERF05-BP01 Design efficient workflow orchestration patterns](./agentperf05-bp01.html)
- [AGENTPERF05-BP02 Implement optimized multi-agent collaboration models](./agentperf05-bp02.html)
- [AGENTPERF05-BP03 Optimize multi-stage AI pipeline execution](./agentperf05-bp03.html)
- [AGENTPERF05-BP04 Implement efficient agent delegation and handoff patterns](./agentperf05-bp04.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
