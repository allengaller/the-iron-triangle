<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Agent governance

Organizations that deliberately design how agents interact with
 users and business processes sustain both automation value and
 institutional expertise as adoption scales. As agents proliferate,
 there is a risk that internal expertise will be diluted or lost to
 fully automated processes. The patterns governing agent
 interactions must be deliberately designed and maintained,
 establishing reusable approaches based on real-world
 organizational needs.

## Capability intent

- Organizational competencies are deliberately categorized
 across human-owned, agent-augmented, and fully automated
 tiers, with clear boundaries enforced by routing and
 guardrail policies.
- Agent development targets processes the organization has
 already mastered, so automation accelerates proven workflows
 rather than substituting for process discovery.
- Agents ship with declarative specifications, dependency
 graphs, and policy documentation that remain current as
 agents evolve, so institutional knowledge is preserved in an
 accessible form.
- A central catalog of deployed agents captures owner,
 purpose, dependencies, and usage, and teams consult it
 before building new agents.
- The agent portfolio is actively rationalized, with inactive
 agents flagged for review, decommissioned through a
 structured lifecycle, and reclaimed infrastructure returned
 to the shared pool.

## Common issues to watch for

- Teams automate unfamiliar or poorly understood processes
 where decision criteria and success metrics are not
 documented, so agent development wastes resources on
 untested methodologies.
- Organizations skip competency tiering, so agents end up
 handling high-stakes or ambiguous decisions that should be
 routed to human experts and subject matter expertise quietly
 atrophies.
- Teams treat agent development as code-only artifacts without
 capturing the expert decision-making patterns and business
 logic rationale, leaving institutional knowledge locked
 inside implementations that only the original developers
 understand.
- Agents are deployed without ownership assignment or usage
 tracking, so there is no basis for evaluating whether an
 agent is still delivering value or has fallen out of use.
- Teams build new agents for capabilities that already exist
 elsewhere in the organization because no one searches the
 catalog first, creating redundant implementations and
 undermining reuse.

###### Best practices

- [AGENTSUS03-BP01 Maintain organizational skills and competencies](./agentsus03-bp01.html)
- [AGENTSUS03-BP02 Build agents to mirror your organizational skills and competencies](./agentsus03-bp02.html)
- [AGENTSUS03-BP03 Maintain comprehensive specifications for agents and agentic systems](./agentsus03-bp03.html)
- [AGENTSUS03-BP04 Decommission unused agents and prevent agent sprawl](./agentsus03-bp04.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
