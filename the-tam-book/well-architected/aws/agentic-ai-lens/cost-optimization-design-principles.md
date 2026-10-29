<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/cost-optimization-design-principles.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Design principles

In addition to the lens-level design principles, the cost optimization best practices in this lens are represented by at least one of the following principles:

- **Pay only for the reasoning the task requires:** Match model class, context length, and reasoning depth to task complexity instead of provisioning the largest model and longest context for the worst case.
- **Enforce consumption ceilings at every layer:** Token budgets, iteration limits, time bounds, and concurrency caps live as policy at the gateway, runtime, and orchestration tiers so unbounded execution is rejected at the boundary rather than paid for and discovered later.
- **Reuse before you recompute:** Caching of prompts, tool results, retrievals, and intermediate state turns repeat work into lookups. Inference is the most expensive operation in the system; build the architecture around that fact.
- **Attribute spend to the unit that drives it:** Tag every invocation with agent, tenant, session, and workflow so reporting moves from infrastructure-level to per-decision accounting and over-provisioned components become visible.
- **Close the loop between cost data and architecture:** Cost telemetry feeds back into model selection, prompt design, and orchestration choices on a regular cadence. Optimization is continuous, not a one-time review.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/cost-optimization-design-principles.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
