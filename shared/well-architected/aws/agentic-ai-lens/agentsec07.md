<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Human oversight protection and agent containment

Human oversight is a key control in agentic systems, but it is
 only effective if reviewers can make informed decisions without
 being overwhelmed or misled. At the same time, you must detect and
 contain agents that deviate from their intended behavior before
 they can affect other parts of the system. This capability covers
 both sides: protecting the quality of human review, and
 implementing detection and containment mechanisms for agents that
 operate outside their defined boundaries.

## Capability intent

- Review queues are prioritized and load-balanced, and
 reviewer workload is monitored for signs of rubber-stamping,
 so human reviewers make informed decisions rather than
 approving under pressure.
- Each decision presented for review carries calibrated
 context, including confidence scores, policy-check results,
 anomaly flags, and similar past decisions, so reviewers
 match their scrutiny to the actual risk of the action.
- High-risk agent actions receive independent review from
 multiple qualified reviewers, with blind review, consensus
 logic, and escalation for disagreement.
- Behavioral baselines exist for each agent, and deviations
 trigger rapid containment through credential revocation and
 circuit-breaker activation, with forensic state captured
 before isolation.
- Security assessments combine continuous automated scanning
 with scheduled red team and purple team exercises targeted
 at agent-specific manipulation scenarios, and findings flow
 back into guardrails, detection rules, and incident response
 runbooks. Red team exercises are adversarial simulations
 where a dedicated team attempts to compromise the agent
 system using the techniques a real attacker would use.
 Purple team exercises run the same scenarios collaboratively
 with the defenders so detection rules and runbooks are
 updated based on what was observed during the simulation.

## Common issues to watch for

- Review capacity is planned by volume alone, without metrics
 that detect rubber-stamping when queues back up, so human
 oversight degrades silently under load as reviewers approve
 faster than they can evaluate.
- Reviewers see agent recommendations without confidence
 scores, anomaly flags, or similar past decisions, and apply
 the same level of scrutiny to high-risk and low-risk actions
 because they have no basis for calibrating their attention.
- High-risk operations depend on a single approver, or
 multiple reviewers are allowed to see each other's decisions
 before submitting their own, turning the review process into
 either a single point of failure or an exercise in anchoring
 bias.
- Rogue-agent detection relies on infrastructure metrics
 rather than per-agent behavioral baselines, and quarantine
 requires a human to act, so an agent operating outside its
 intended scope keeps running for hours as responders
 mobilize.
- Security assessments are one-time, generic, or disconnected
 from the agents they are meant to protect, so findings never
 translate into updated guardrails, detection rules, or
 incident runbooks.

###### Best practices

- [AGENTSEC07-BP01 Implement cognitive load management](./agentsec07-bp01.html)
- [AGENTSEC07-BP02 Clear confidence indicators and manipulation warnings](./agentsec07-bp02.html)
- [AGENTSEC07-BP03 Multiple reviewers for critical operations](./agentsec07-bp03.html)
- [AGENTSEC07-BP04 Behavioral anomaly detection and agent containment](./agentsec07-bp04.html)
- [AGENTSEC07-BP05 Regular security assessments and red teaming](./agentsec07-bp05.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
