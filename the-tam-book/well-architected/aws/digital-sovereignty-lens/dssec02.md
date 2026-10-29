<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dssec02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Access control within sovereign boundaries

A single control layer isn't sufficient to protect sovereign data.
 Network controls alone can't enforce identity rules, and identity
 controls alone can't account for network paths. To protect data
 within its sovereign boundary, you need layered preventive controls
 that verify identity, constrain network paths, and restrict
 resource-level access in proportion to data sensitivity and
 jurisdictional requirements.

This capability covers data perimeters that combine IAM conditions,
 resource-based policies, service control policies, VPC endpoint
 policies, and network controls to enforce jurisdictional boundaries
 and block unauthorized access before it occurs.

## Capability intent

- Data remains accessible only to authorized identities
 operating within designated sovereign boundaries, and every
 access path is auditable.
- Network-centric and identity-centric controls operate as
 layered preventive boundaries rather than relying on detection
 after access has already occurred.
- Operator access is constrained to approved jurisdictions and
 approved roles, with access patterns recorded for regulatory
 demonstration.
- Cross-service and cross-Region data flows are explicitly
 mapped and controlled rather than implicitly permitted.
- Access control policies are expressed declaratively and
 validated through automated analysis, so teams rely less on
 manual review.

## Common issues to watch for

- Relying on a single control layer (for example, only detective
 controls) to identify violations rather than applying
 preventive controls that stop violations before they occur.
- Cross-service data flows that traverse Region boundaries
 without explicit mapping, which opens unintentional
 sovereignty gaps.
- VPC endpoint policies that allow all principals by default,
 which negates the boundary enforcement the endpoint was meant
 to provide.
- Operator access paths that bypass data perimeter controls
 through break-glass mechanisms that lack proper logging and
 time-bound constraints.
- Access control reviews conducted only at deployment time, so
 policy drift and permission accumulation over the workload
 lifecycle go unnoticed.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dssec02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
