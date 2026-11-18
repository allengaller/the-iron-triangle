<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost06.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Agent discovery and deployment cost optimization

Teams that optimize agent lifecycle infrastructure through
 lightweight discovery, efficient versioning, and warm
 initialization help keep operational overhead from growing faster
 than the agent fleet itself. Agent infrastructure costs can
 escalate through inefficient discovery mechanisms, version
 proliferation, and cold start penalties.

## Capability intent

- Agent discovery runs on consumption-based infrastructure, so
 registry costs track actual query and write activity rather
 than a fixed overhead for the fleet.
- Metadata caching serves most capability lookups without
 re-reading the registry, keeping read costs proportional to
 the rate of registry change rather than the rate of
 invocation.
- Agent versioning stores shared dependencies once and retires
 unused versions automatically, so storage costs stay
 contained as the agent fleet evolves.
- Deployments use weighted traffic routing on shared
 infrastructure, so blue/green and canary rollouts don't pay
 twice for parallel environments.
- Frequently invoked agents reuse warm sessions with cached
 initialization artifacts, and infrequent agents scale to
 zero to avoid idle capacity charges.
- Cold start rates, cache hit rates, and per-version storage
 are instrumented and reviewed, giving owners the signal to
 address cost drivers before they scale with the fleet.

## Common issues to watch for

- Organizations deploy heavyweight service mesh infrastructure
 for simple capability lookups, paying fixed monthly costs
 for features the agent fleet doesn't use.
- Teams put the registry on the critical path for every
 invocation, repeatedly re-reading capability metadata
 instead of caching it, so read costs grow linearly with
 invocation volume.
- Agent version retention runs without lifecycle policies, so
 every configuration change accumulates images in the
 container registry and storage costs grow indefinitely.
- Blue/green and canary deployments run full parallel fleets
 instead of routing a small traffic percentage, doubling
 compute cost during every rollout.
- Frequently invoked agents pay cold start costs on every
 invocation because session lifetimes, persistent filesystem
 caching, and session affinity are not configured.
- Discovery, versioning, and initialization costs are not
 instrumented, so expensive patterns such as scan-heavy
 queries, unused versions, and repeated cold starts grow
 silently as the fleet expands.

###### Best practices

- [AGENTCOST06-BP01 Implement lightweight discovery and registry for cost-effective collaboration](./agentcost06-bp01.html)
- [AGENTCOST06-BP02 Cost optimize versioning and deployment through efficient artifact management](./agentcost06-bp02.html)
- [AGENTCOST06-BP03 Design cost-efficient initialization through warm pools and caching](./agentcost06-bp03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost06.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
