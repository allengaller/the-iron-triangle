<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Resource right-sizing

Agents that right-size their dependencies (memory, caching,
 compute, and networking) deliver automation value without placing
 unsustainable load on the systems they depend on. Increased agent
 traffic increases the load on these dependencies. Sustainable
 frameworks help dependent systems scale proportionally to the
 benefit achieved through agentic automation.

## Capability intent

- Memory and context infrastructure scales with actual
 contextual needs rather than worst-case estimates, with
 tiered storage and shared persistent context separating hot
 and cold access paths.
- Caching is applied at every integration point, and shared
 caches amortize work across the agent fleet rather than
 being rediscovered by each agent in isolation.
- Compute, networking, and storage scale dynamically with
 bursty agent workloads, contracting during quiet periods and
 expanding during peaks without manual intervention.
- Regional and connectivity choices are deliberate, so traffic
 stays close to the services agents depend on and private
 paths are used where security or latency justifies them.
- Environmental impact is measured alongside operational
 metrics, and deferrable workloads are scheduled and placed
 with carbon-awareness to reduce footprint without affecting
 user-facing performance.

## Common issues to watch for

- Teams build flat memory architectures without tiered
 storage, so frequently accessed context competes with
 archival data for the same tier and retrieval costs grow
 with every new session.
- Organizations treat each agent instance as an isolated
 system with its own cache, missing the fleet-wide
 amortization that turns one cache hit into savings for every
 agent that asks the same question.
- Infrastructure stays statically provisioned for worst-case
 demand, so utilization sits low during normal operations and
 dynamic contraction never happens.
- Regional placement ignores where the frequently accessed
 services live, so agent traffic crosses Regions
 unnecessarily and adds both latency and data transfer to
 every invocation.
- Sustainability claims are made without baselines or trend
 tracking, so optimization work can't be validated and
 deferrable workloads still run during peak hours alongside
 user-facing traffic.

###### Best practices

- [AGENTSUS02-BP01 Optimize context management and memory utilization](./agentsus02-bp01.html)
- [AGENTSUS02-BP02 Establish efficient agent caching strategies](./agentsus02-bp02.html)
- [AGENTSUS02-BP03 Appropriately scale data, networking, and compute dependencies](./agentsus02-bp03.html)
- [AGENTSUS02-BP04 Measure and optimize the environmental footprint of agent workloads](./agentsus02-bp04.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
