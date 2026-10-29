<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsperf01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Sovereign solution selection

Not every sovereign workload needs the same level of control, and
 applying maximum restrictions everywhere drives unnecessary cost and
 complexity. AWS provides a continuum of deployment options with
 different combinations of service availability, operational
 responsibility, and sovereignty controls. Selecting the right option
 for each workload requires a data-driven approach that matches
 regulatory obligations, data residency needs, and operational
 constraints to the deployment model that satisfies them without
 over-engineering.

This capability covers the evaluation and selection of sovereign
 deployment options across the continuum of AWS Regions, European
 Sovereign Cloud, Dedicated Local Zones, and Outposts, using
 data-driven criteria rather than blanket policies.

## Capability intent

- Workloads are matched to sovereign deployment options based on
 specific regulatory obligations and data residency
 requirements, not blanket policies that apply the same
 restrictions to all workloads.
- Decision criteria are explicit, documented, and repeatable so
 that different teams evaluating similar workloads reach
 consistent conclusions.
- The trade-offs between sovereignty controls, service
 availability, operational complexity, and cost are understood
 and accepted for each workload before deployment.
- Decision criteria are reviewed when regulatory requirements,
 service availability, or deployment options change, so
 placement decisions remain valid over time.
- The evaluation process considers the full lifecycle of the
 workload, including growth scenarios where requirements may
 shift to more or less restrictive options.

## Common issues to watch for

- Blanket policies that place all workloads in the most
 restrictive deployment option. Workloads that do not need
 maximum controls then carry unnecessary cost and lose access
 to services unavailable in that option.
- Decision criteria that weigh data residency alone and ignore
 operational complexity, service availability constraints, and
 cost, so the chosen option is compliant but hard to operate.
- Workload placement decisions made once at initial deployment
 and never revisited, even when regulatory requirements or
 available deployment options change.
- Evaluation processes that are neither documented nor
 repeatable, so teams reach different conclusions and workloads
 with similar requirements land in different options.
- Trade-off decisions made without input from both compliance
 and operations stakeholders, which satisfy one concern and
 create problems for the other.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsperf01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
