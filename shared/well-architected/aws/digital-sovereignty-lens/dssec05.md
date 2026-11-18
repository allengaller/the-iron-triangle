<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dssec05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Infrastructure access

Controlling how and from where operators access infrastructure is a
 core sovereignty concern. Operator access introduces risk when
 access paths span jurisdictions, when privileges persist beyond
 immediate need, or when regional teams lack the authority and
 tooling to operate independently. Sovereign workloads require access
 models that verify identity, validate access location through
 layered controls, enforce just-in-time privileges, and reduce
 interactive access through automation.

This capability covers operator access controls, jurisdictional
 access constraints, and the empowerment of regional teams to operate
 within their own jurisdictions without dependency on centralized
 access paths.

## Capability intent

- Operator access to infrastructure is constrained to approved
 locations and validated through layered identity and network
 controls.
- Privileges are granted just-in-time and scoped to the minimum
 necessary for each operation, with time-bound expiration.
- Interactive access to production systems is minimized through
 automation, reducing both risk surface and dependency on
 individual operators.
- Regional teams possess the authority, tooling, and training to
 operate their jurisdictions independently without requiring
 access from centralized or foreign locations.
- All operator access is logged with sufficient context
 (identity, source location, time, and scope) to support
 forensic review and regulatory reporting.

## Common issues to watch for

- Standing administrator credentials that persist across
 sessions, creating a permanent attack surface and violating
 least-privilege principles.
- Jurisdictional access constraints enforced only at the network
 level without corresponding identity conditions, allowing
 authenticated operators from non-approved locations to access
 systems through VPN or direct connections.
- Regional teams that lack sufficient authority or tooling to
 operate independently, creating bottlenecks where all changes
 must route through a central team in another jurisdiction.
- Automation pipelines that run with broad permissions and are
 not subject to the same jurisdictional constraints applied to
 human operators.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dssec05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
