<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsops02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Compliance baselining and automation

Compliance requirements accumulate from multiple sources:
 cybersecurity directives, privacy legislation, industry regulations,
 and internal policies. Even within a single jurisdiction these
 requirements can overlap or diverge, and the overlap grows as
 jurisdictions are added. Without a structured compliance catalog,
 teams can't determine which controls apply to their workloads or
 verify that those controls are implemented correctly.

This capability covers building a compliance catalog that maps
 requirements to technical controls, and codifying those controls as
 policy as code with automated validation embedded in deployment
 pipelines.

## Capability intent

- Compliance requirements from all applicable sources are
 cataloged and mapped to specific technical controls,
 validation criteria, and evidence requirements.
- Controls are codified as policy as code and enforced through
 automated mechanisms rather than relying on manual
 implementation and review.
- Deployment pipelines validate compliance before resources
 reach production, blocking noncompliant configurations at the
 source.
- The compliance catalog serves as a single reference for which
 requirements apply to which workloads in which jurisdictions,
 eliminating ambiguity for implementation teams.
- Baseline updates propagate automatically to affected workloads
 and accounts when requirements change, without requiring
 manual redeployment.

## Common issues to watch for

- Compliance catalogs that map requirements to controls at an
 abstract level without specifying validation criteria, which
 makes it impossible to automate verification or confirm
 control effectiveness.
- Policy as code that enforces a single baseline across all
 jurisdictions and misses requirements that differ between
 regulatory frameworks operating in the same environment.
- Deployment pipelines with compliance gates that can be
 bypassed through alternative deployment paths (the console or
 direct API calls), which creates resources that avoid
 automated validation.
- Exceptions granted without expiration dates or justification
 records, which accumulate over time and erode the baseline
 without visibility into the cumulative drift.
- Compliance baselines that are updated centrally but require
 manual redeployment to affected accounts, leading to
 compliance drift.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsops02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
