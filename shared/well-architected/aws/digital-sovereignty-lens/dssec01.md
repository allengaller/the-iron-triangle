<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dssec01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Security foundations

Sovereign workloads carry regulatory obligations that span data
 residency, jurisdictional access, and continuous compliance. These
 obligations are easier to meet when security and sovereignty
 controls are part of the architecture from initial deployment rather
 than added later. A security foundation supplies automated
 guardrails, standardized baselines, and pre-configured compliance
 frameworks, so teams can deploy new workloads without rebuilding
 controls each time.

This capability covers multi-account landing zone architecture,
 digital sovereignty controls, data perimeters, and layered security
 patterns that enforce sovereignty requirements across the network,
 identity, data, and application layers.

## Capability intent

- Security, compliance, and sovereignty controls are embedded in
 the architecture from initial deployment, not retrofitted
 after workloads are running.
- Automated guardrails enforce data residency and jurisdictional
 access boundaries across all accounts and workloads without
 manual intervention.
- Landing zone configurations codify regulatory requirements
 into repeatable infrastructure as code, so new accounts
 inherit sovereignty controls by default.
- Data perimeters combine identity-based, network-based, and
 resource-based controls to prevent unauthorized cross-boundary
 access at multiple layers.
- Compliance monitoring runs continuously and produces
 audit-ready evidence without separate manual collection
 efforts.

## Common issues to watch for

- Security controls added after workloads are already running.
 The gap between deployment and compliance then persists until
 the next audit cycle.
- Landing zone accelerators deployed with default configurations
 that do not account for jurisdiction-specific sovereignty
 requirements, which gives a false sense of compliance.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dssec01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
