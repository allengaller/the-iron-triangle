<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsops05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Compliance remediation

Detecting a compliance finding accomplishes nothing until someone
 remediates it. When a finding appears, regional teams need to
 investigate root causes and apply fixes independently, without
 waiting for a central team to triage and respond. Good remediation
 gives those teams jurisdiction-scoped access to findings, a
 standardized root cause analysis process, pre-approved runbooks, and
 automated fixes that keep audit trails.

This capability covers the investigation, root cause analysis, and
 remediation of compliance findings. It emphasizes letting regional
 teams act independently and automating remediation where possible.

## Capability intent

- Regional teams can investigate and remediate compliance
 findings within their jurisdiction independently, without
 waiting for a central team in another jurisdiction.
- Root cause analysis follows a standardized process that
 identifies systemic issues rather than treating each finding
 as an isolated event.
- Pre-approved remediation runbooks provide consistent,
 auditable procedures that regional teams can execute within
 their authority.
- Automated remediation handles known finding types with
 consistent fixes, traceable to the regulatory requirement each
 fix addresses.
- Remediation effectiveness is measured (time-to-remediate and
 recurrence rate) and feeds back into control design and
 prevention mechanisms.

## Common issues to watch for

- Regional teams can see findings but lack the authority or
 tooling to remediate them. That creates a dependency on
 central teams, which delays resolution and lets compliance
 debt pile up.
- Remediation is applied to individual findings without root
 cause analysis, so the same type of noncompliance keeps
 recurring across accounts and deployments.
- Automated remediation runs without sufficient guard rails and
 makes unintended changes, such as restricting access in a way
 that breaks legitimate workloads, which erodes trust in
 automation.
- Audit trails record what was changed but not why, which makes
 it hard to demonstrate regulatory alignment during audits.
- Escalation paths are unclear or untested, so regional teams
 have no recourse when findings fall outside their runbook
 coverage.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsops05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
