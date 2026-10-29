<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Communication and protocol efficiency

Efficient communication between agents, tools, and services scales
 multi-agent systems from prototypes to production without latency
 growing alongside complexity. Agentic AI systems rely on
 communication between agents, tools, services, and users through
 various protocols and messaging patterns. The efficiency of these
 communication channels directly impacts agent performance. Every
 message exchange adds latency, every protocol handshake consumes
 time, and every serialization or deserialization operation uses
 compute resources. Optimizing communication requires selecting
 appropriate protocols for each interaction pattern, implementing
 efficient asynchronous messaging, and designing event-driven
 architectures that minimize polling and unnecessary processing.

## Capability intent

- Agent-to-agent and agent-to-service communication uses
 asynchronous messaging by default, with synchronous calls
 reserved for interactions that genuinely require an
 immediate response.
- Protocols are selected per interaction pattern, with MCP for
 tool integration, A2A for agent-to-agent coordination, and
 streaming transports such as WebSocket for real-time user
 interactions.
- Event-driven integration is push-based and precisely
 filtered, so agents are invoked only for events that match
 their processing requirements and consume no compute when
 idle.
- Message and event payloads carry references to durable
 stores rather than embedded data, keeping transfer times low
 and letting consumers skip work on events that have become
 irrelevant.
- Connection pooling, protocol-level compression, and token
 caching keep per-interaction overhead flat as the number of
 agent-to-agent hops and tool invocations grows.

## Common issues to watch for

- Teams default to synchronous HTTP/REST for every agent
 communication, creating tight coupling where a slow
 downstream component blocks the entire upstream chain and
 propagates scaling issues across the workflow.
- Agents receive broad event streams without content-based
 filtering and spend compute receiving, parsing, and
 discarding events they never act on, which inflates cost and
 obscures the latency of events that do matter.
- Message and event payloads inline full data (documents,
 base64-encoded files, entire records) rather than passing
 references, so queue throughput and network transfer are
 consumed by payloads that consumers could fetch on demand.
- Backpressure and dead letter queues are missing, which lets
 fast producers overwhelm slow consumers and hides persistent
 message failures until a downstream timeout or data-loss
 incident forces investigation.
- Authentication overhead, connection setup, and serialization
 costs are tracked as service-level metrics rather than
 per-hop overheads, so a workflow with many agent-to-agent
 hops accumulates silent latency that no single service's
 telemetry surfaces.

###### Best practices

- [AGENTPERF04-BP01 Optimize asynchronous message handling patterns](./agentperf04-bp01.html)
- [AGENTPERF04-BP02 Implement efficient protocol-based agent communications](./agentperf04-bp02.html)
- [AGENTPERF04-BP03 Design high-performing event-driven integration patterns](./agentperf04-bp03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
