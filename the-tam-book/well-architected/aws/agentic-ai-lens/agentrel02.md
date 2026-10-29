<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Predictable task execution

Agents that constrain LLM stochasticity through atomic task
 design, least-privilege permissions, and clear instruction
 protocols deliver predictable outcomes even when the underlying
 models are non-deterministic. Agent reliability extends beyond
 supporting infrastructure to the reliability of executing the
 intended task with the appropriate data at the correct time.

## Capability intent

- Each agent owns a single atomic capability with explicit
 input validation and a structured output schema, so LLM
 stochasticity is bounded by narrow, testable contracts.
- Every agent operates within a least-privilege permission
 envelope enforced at identity, policy, and access-control
 layers, so an unexpected model decision affects only the
 systems explicitly authorized for that agent.
- Agents emit agent-specific telemetry (prompts, tool calls,
 memory access, output quality) that is compared against
 behavioral baselines, so drift and anomalies are detected
 before they cascade into failures.
- Instructions reach agents through canonical prompt
 templates, versioned configuration, and explicit handoff
 schemas, so interpretation of objectives is consistent
 across single-agent and multi-agent workflows.
- Agent actions are routed to the appropriate tier of human
 oversight based on risk and reversibility, so
 high-consequence decisions receive review without adding
 latency to routine work.

## Common issues to watch for

- Agents accumulate broad, overlapping responsibilities over
 time, so a single misinterpretation can affect multiple
 capabilities and failure modes become harder to reproduce as
 scope expands.
- IAM execution roles and policy boundaries are written with
 wildcards or at the convenience of a first deployment, so
 the scope of impact of any unpredicted LLM action is wider
 than the agent's legitimate function.
- Monitoring captures infrastructure signals but not
 agent-specific decision points, so behavioral drift (longer
 outputs, more tool calls, or shifts in output distribution)
 is invisible until it produces a user-visible failure.
- Prompts and handoff formats are authored ad-hoc by each
 team, so agents interpret objectives inconsistently and
 multi-agent workflows break when either side of a handoff
 evolves independently.
- All agent actions receive the same level of human review,
 either uniform approval that bottlenecks automation or
 uniform autonomy that lets high-consequence decisions ship
 without oversight.

###### Best practices

- [AGENTREL02-BP01 Design agents for specific and atomic tasks](./agentrel02-bp01.html)
- [AGENTREL02-BP02 Limit agent permissions to minimum required access](./agentrel02-bp02.html)
- [AGENTREL02-BP03 Implement behavioral anomaly detection and monitoring](./agentrel02-bp03.html)
- [AGENTREL02-BP04 Develop clear instruction protocols for agents](./agentrel02-bp04.html)
- [AGENTREL02-BP05 Establish tiered human oversight and approval workflows](./agentrel02-bp05.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
