<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Secure agent tool usage

Agents interact with external systems through tools such as APIs,
 databases, file systems, and other services. Without proper
 controls, an agent with tool access can be directed to perform
 unintended actions. Authorization, input validation, and tool
 governance reduce the risk of tool misuse and unauthorized
 operations.

## Capability intent

- Every tool invocation is authorized against a declarative
 policy before execution, with the agent identity and the
 originating user context propagated through the
 authorization chain.
- Agents invoke only tools within their approved scope, and
 tool parameters and responses pass through schema and policy
 checks that keep operations inside defined boundaries.
- High-risk mutating operations stop at a human-in-the-loop
 checkpoint, and rate limits cap the impact scope when an
 agent enters a runaway loop.
- Tools and the MCP servers that host them are available to
 agents only after going through a documented security review
 and being registered with a pinned version, data
 classification, and review expiry.
- Tool usage is observable end to end, with authorization
 decisions, validation failures, and invocation rates feeding
 detection and compliance workflows.

## Common issues to watch for

- Tool access granted at the agent level but enforced only by
 the agent's reasoning, so nothing outside the model helps
 prevent an injected or poisoned prompt from invoking tools
 that sit outside the agent's intended scope.
- Schema validation applied to user-facing parameters but not
 to parameters the model generates, on the assumption that
 the model can't produce malformed output. In practice,
 model-generated parameters are an attack surface that
 carries injection payloads and invalid types.
- Registries maintained as static documents rather than as
 enforced controls at the gateway or the MCP client, so
 agents continue to discover and invoke tools that no one has
 reviewed.
- Remote Model Context Protocol (MCP) servers adopted with the
 same risk assumptions as local tools, which understates the
 exposure introduced by network connectivity, third-party
 authentication, and external data handling.
- Rate limiting treated as a cost control rather than as a
 security control, so a runaway loop or a prompt injection
 that triggers mass tool calls runs long enough to affect
 downstream systems before human responders intervene.

###### Best practices

- [AGENTSEC02-BP01 Implement tool authorization](./agentsec02-bp01.html)
- [AGENTSEC02-BP02 Validate tool inputs and outputs](./agentsec02-bp02.html)
- [AGENTSEC02-BP03 Maintain approved tool registry with security assessments](./agentsec02-bp03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
