<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dssec03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Sovereignty control verification

Claiming sovereignty compliance is different from proving it.
 Sovereignty controls must be verifiable through automated analysis
 rather than relying solely on manual audits or periodic reviews.
 Automated reasoning, network reachability analysis, and
 configuration validation provide mathematical or evidence-based
 assurance that policies enforce the jurisdictional boundaries they
 are designed to protect.

This capability covers the use of proactive and detective controls
 to validate that access policies, network paths, and resource
 configurations meet sovereignty baselines before and after
 deployment.

## Capability intent

- Access policies are validated through automated reasoning to
 confirm they enforce intended jurisdictional boundaries,
 rather than relying on manual policy review alone.
- Network paths are analyzed to verify they don't cross
 sovereign boundaries, and reachability findings are resolved
 before workloads go live.
- Resource configurations are evaluated against sovereignty
 baselines both before provisioning (proactive) and after
 deployment (detective), so the intended controls match what is
 actually deployed.
- Verification results produce audit-ready evidence that
 demonstrates control effectiveness to regulators without
 separate manual evidence collection.
- New resources are blocked from provisioning when they violate
 sovereignty baselines, moving enforcement earlier in the
 deployment lifecycle.

## Common issues to watch for

- Policies that appear correct on inspection but contain
 implicit allows or overly broad conditions that automated
 reasoning would catch.
- Network reachability analysis scoped only to individual VPCs,
 missing cross-account peering or transit gateway paths that
 cross jurisdictional boundaries.
- Proactive controls deployed without detective controls as a
 backstop, so resources that bypass the proactive layer (for
 example, through console actions) go undetected.
- Verification results that are not actionable because findings
 lack context on which sovereignty requirement is violated and
 what remediation is needed.
- Automated analysis that runs on a schedule rather than on
 change events, creating windows where noncompliant
 configurations exist undetected between analysis runs.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dssec03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
