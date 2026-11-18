<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Resource reusability

Organizations that invest in reusable agent infrastructure
 accelerate every subsequent project while reducing cumulative
 resource consumption. As agents are used more, the opportunity to
 optimize, share, and recycle agent resources increases. Shared
 resources pose a less significant burden on the overall
 architecture, creating a more sustainable workflow.

## Capability intent

- Each agent encapsulates a single, well-defined capability
 with explicit resource boundaries, and those boundaries
 cascade through delegation to child agents so no subtree
 consumes resources without a defined cap.
- Recurring workflow patterns (retrieval, validation,
 transformation, and decision-making) exist as parameterized,
 discoverable components that teams compose rather than
 rebuild for every new use case.
- Common infrastructure such as connection pools, caches,
 authentication, and foundation model access is consolidated
 into shared services, so capacity grows with aggregate
 demand rather than with the number of agent instances.
- Cognitive pathways are right-sized to task complexity, with
 model selection, retrieval depth, and memory scope each
 matched to actual needs rather than defaulting to the
 largest or broadest option.
- Long-running and frontier workloads run against explicit
 specifications covering success criteria, resource budgets,
 and termination conditions, with checkpoints that make
 compute investment reviewable against business value.

## Common issues to watch for

- Teams provision agents for worst-case scenarios and let
 parent agents delegate work to child agents without
 cascading resource budgets, so runaway consumption in one
 subtree is discovered only after the monthly bill.
- Recurring workflow logic is rebuilt for each new use case,
 accumulating duplicated code and testing debt while missing
 the renewable-architecture benefit of optimizing a shared
 pattern once and propagating the improvement everywhere.
- Each agent establishes its own connections, caches, and
 authentication flows rather than consuming shared services,
 so infrastructure costs scale linearly with agent count
 instead of with aggregate demand.
- Every request is routed to the largest foundation model,
 retrieval is unbounded against knowledge bases, and memory
 grows without pruning, so cognitive overhead is
 disproportionate to the value delivered by each interaction.
- Long-running and frontier agents run without specifications,
 resource budgets, or checkpoints, so they explore tangential
 paths and consume extended compute without an accountability
 mechanism that ties outcomes to business value.

###### Best practices

- [AGENTSUS01-BP01 Design specialized agents with explicit resource boundaries](./agentsus01-bp01.html)
- [AGENTSUS01-BP02 Implement reusable workflow patterns](./agentsus01-bp02.html)
- [AGENTSUS01-BP03 Optimize resource utilization through shared services](./agentsus01-bp03.html)
- [AGENTSUS01-BP04 Scale cognitive processing pathways appropriately](./agentsus01-bp04.html)
- [AGENTSUS01-BP05 Adopt specification-driven tasks for frontier agents and long-running workflows](./agentsus01-bp05.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
