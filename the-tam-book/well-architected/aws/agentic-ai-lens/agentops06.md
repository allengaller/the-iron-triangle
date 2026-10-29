<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops06.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Testing, evaluation, and validation frameworks

Systematic testing and evaluation processes confirm agent quality, reliability, and
 alignment with business objectives through both traditional software testing and
 AI-specific quality assessment. Without a framework that covers every stage of the agent
 lifecycle, quality regressions from prompt changes, tool updates, or model updates reach
 users before anyone notices.

## Capability intent

- Agents are validated at every layer, from isolated components to entire
 workflows running in production-shadow mode, before changes reach
 users.
- Quality, safety, efficiency, and business-alignment metrics are measured
 continually against version-controlled benchmarks, with regressions surfaced
 as soon as they appear.
- Change governance is proportional to risk. Low-risk changes flow through
 automated gates, and high-risk changes receive SME and business-owner
 review.
- Evaluation datasets, prompts, and scoring rubrics are versioned and kept
 current as agent capabilities and use cases evolve.
- Rollback paths for prompts, tools, models, and agent versions are defined,
 rehearsed, and wired to the same telemetry that detects quality threshold
 violations.

## Common issues to watch for

- Teams stop at deterministic unit tests and skip shadow testing on real
 traffic, so agents ship with unknown behavior on edge cases, adversarial
 inputs, and production data distributions.
- Quality is measured once at release and never again, so data drift, prompt
 decay, and upstream model updates silently erode output quality between
 releases.
- All changes flow through either a heavyweight board or a rubber-stamp
 review, which either bottlenecks minor tweaks or waves through autonomy
 increases without SME scrutiny.
- Test and evaluation datasets are created once and never refreshed, so
 scores stay green while real-world failure modes go undetected.
- Rollback procedures live in a runbook but are never rehearsed, so the
 first real attempt during an incident discovers broken artifact stores,
 missing permissions, or prompt and tool version mismatches.

###### Best practices

- [AGENTOPS06-BP01 Design multi-layered testing frameworks](./agentops06-bp01.html)
- [AGENTOPS06-BP02 Evaluate and track ongoing agent performance](./agentops06-bp02.html)
- [AGENTOPS06-BP03 Establish SME-driven validation and business approval workflows](./agentops06-bp03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops06.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
