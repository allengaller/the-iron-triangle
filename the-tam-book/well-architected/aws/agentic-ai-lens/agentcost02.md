<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Model invocation and token cost optimization

Teams that right-size model selection to task complexity and
 optimize token consumption per invocation can improve their cost
 reductions without sacrificing agent decision quality. Foundation
 model costs can dominate agentic AI budgets, with agents
 potentially invoking expensive models for simple tasks or
 consuming excessive tokens through verbose reasoning.

## Capability intent

- Model selection matches task complexity, with routine
 classification and formatting handled by cost-efficient
 models and premium models reserved for reasoning that
 genuinely needs them.
- Prompts, tool descriptions, and output constraints are kept
 at the minimum size required to maintain decision quality
 across planning, execution, and reflection phases.
- Repeated reasoning and stable context are served from caches
 rather than regenerated, so equivalent requests don't pay
 the full inference cost twice.
- High-volume recurring tasks run on specialized or customized
 models whose one-time training cost amortizes against
 sustained per-invocation savings.
- Cost-per-correct-response, token consumption, cache hit
 rate, and cascade escalation rate are tracked per model tier
 and fed back into routing, caching, and customization
 decisions.

## Common issues to watch for

- Every agent invocation defaults to the most capable
 general-purpose model, resulting in higher inference costs
 for routine classification and formatting that could use
 cost-effective alternatives.
- System prompts and tool catalogs accumulate without review,
 so the fixed input-token tax paid on every invocation rises
 silently across months even when traffic is flat.
- Caching is treated as a one-time enablement rather than an
 ongoing discipline, so stale invalidation policies, weak
 similarity thresholds, or drifting cacheable prefixes erode
 hit rates and savings without anyone noticing.
- Model customization is pursued on low-volume or vanity
 workloads rather than on high-volume recurring tasks where
 training cost can amortize, leaving the investment
 permanently underwater.
- Cost signals are tracked only at aggregate level, so teams
 can't see which tier, reasoning phase, or cache layer is
 driving spend and can't prioritize optimization work against
 evidence.

###### Best practices

- [AGENTCOST02-BP01 Architect tiered model selection for cost-performance optimization](./agentcost02-bp01.html)
- [AGENTCOST02-BP02 Cost optimize token consumption through efficient prompt engineering](./agentcost02-bp02.html)
- [AGENTCOST02-BP03 Use intelligent caching to reduce redundant model invocations](./agentcost02-bp03.html)
- [AGENTCOST02-BP04 Implement model customization for long-term cost reduction](./agentcost02-bp04.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
