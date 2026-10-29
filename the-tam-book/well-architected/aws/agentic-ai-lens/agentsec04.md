<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Agent goal alignment and manipulation prevention

Agents can be directed to pursue unintended objectives or exhibit
 behaviors outside their defined scope. Without goal alignment
 mechanisms, agents might take actions that conflict with
 organizational policies or user intent. Implementing guardrails,
 layered validation controls, and human-in-the-loop approvals helps
 verify that agents operate within intended boundaries.

## Capability intent

- Operational and policy boundaries for each agent are defined
 up front and enforced through layered controls rather than
 prompt instructions alone.
- Deterministic enforcement (IAM scoping, input schema
 validation, and policy engines) and probabilistic content
 controls (input and output filtering, behavioral evaluation)
 operate at distinct stages of the call chain, so a failure
 at one layer rarely results in a boundary violation.
- Risk classification is deterministic, with high-risk
 operations routed to human review before execution and
 routine low-risk operations proceeding autonomously.
- Reviewers receive sufficient decision context, timeout
 policies, and escalation paths to make informed approvals
 without stalling the workflow or defaulting to
 rubber-stamping.
- Guardrail interventions, approval decisions, and evaluation
 results are logged, alerted on, and reviewed on a defined
 cadence to keep policies current with emerging patterns.

## Common issues to watch for

- Alignment is treated as a prompt-engineering exercise rather
 than a layered enforcement problem, so a single adversarial
 input that influences the model can collapse multiple
 boundaries at once.
- Content filtering is applied only to model outputs, leaving
 the inference path open to prompt injection and consuming
 capacity on adversarial inputs that could have been rejected
 up front.
- A single guardrail profile is applied to every agent, which
 either over-constrains low-risk informational agents or
 leaves high-risk operational agents under-constrained.
- Approval workflows either route every action through human
 review (producing reviewer fatigue and rubber-stamping) or
 skip review for operations that warrant it, giving the worst
 of both extremes.
- Risk classification is delegated to an LLM exposed to the
 same untrusted content as the request it is evaluating,
 which can be influenced into marking that request as
 low-risk.

###### Best practices

- [AGENTSEC04-BP01 Implement guardrails and alignment controls](./agentsec04-bp01.html)
- [AGENTSEC04-BP02 Human-in-the-loop for critical decisions](./agentsec04-bp02.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
