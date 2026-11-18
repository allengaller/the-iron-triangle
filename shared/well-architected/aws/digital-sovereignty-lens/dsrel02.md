<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsrel02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Third-party sovereignty risk management

Third-party vendors can introduce sovereignty risks that remain
 invisible until an audit or incident exposes them. Data processed in
 non-approved jurisdictions, operators accessing systems from foreign
 locations, and sub-processors that don't adhere to data residency
 requirements are common examples. Standard vendor risk assessments
 focus on security posture and financial stability but miss
 sovereignty-specific concerns.

This capability covers continuous third-party risk management that
 assesses vendor data residency, operator location, cross-border data
 flows, and contractual safeguards throughout the vendor lifecycle.

## Capability intent

- Third-party vendors are assessed against sovereignty-specific
 criteria (data residency, operator location, sub-processor
 chains, and contractual exit provisions) before onboarding and
 continuously thereafter.
- Vendor data flows are mapped to identify where data is stored,
 processed, and transferred, including flows through
 sub-processors.
- Contractual safeguards address sovereignty requirements
 explicitly, including data return provisions, audit rights,
 and notification of material changes to processing locations.
- Vendor risk posture is monitored continuously rather than
 assessed only at contract renewal, with triggers for
 reassessment when vendor circumstances change.
- Exit plans exist for critical vendors, with tested procedures
 for data extraction, migration, and continuity that maintain
 sovereignty compliance during transition.

## Common issues to watch for

- Vendor risk assessments that focus on security certifications
 without evaluating where data is actually processed or where
 operators are located.
- Sub-processor chains that are not mapped beyond the direct
 vendor, so sovereignty risks stay hidden in second-tier and
 third-tier relationships.
- Data return provisions that exist in contracts but have never
 been tested, so the organization has no validated path to
 reclaim data under sovereignty constraints.
- Vendor reassessment triggered only at contract renewal on
 annual or multi-year cycles, which misses material changes in
 processing locations or corporate ownership between
 assessments.
- Concentration of critical capabilities in a single vendor
 without pre-qualified alternatives, which becomes a
 sovereignty-relevant continuity risk if that vendor faces
 trade restrictions or regulatory action.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsrel02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
