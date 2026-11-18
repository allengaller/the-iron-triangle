<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dssec04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Detection and investigation

Sovereign workloads face threats beyond standard cybersecurity
 concerns. Unauthorized cross-border data transfers, operator access
 violations, and jurisdictional compliance drift are
 sovereignty-specific threats that require purpose-built detection
 capabilities. Standard threat detection must be augmented with
 jurisdiction-specific intelligence, full telemetry with data
 residency controls, and detailed logging of operator actions.

This capability covers threat detection, sovereignty-specific
 monitoring, and operator action logging that together enable timely
 investigation of security events in sovereign workloads.

## Capability intent

- Threat detection covers both traditional cybersecurity threats
 and sovereignty-specific threats such as unauthorized
 cross-border data transfers and operator access violations.
- Threat intelligence is enriched with jurisdiction-specific
 indicators that reflect the regulatory and geopolitical
 context of each operating region.
- Telemetry data is retained within approved jurisdictions and
 accessible to authorized investigators without violating data
 residency requirements.
- Operator actions are logged with sufficient detail (identity,
 location, time, and scope) to support forensic investigation
 and regulatory demonstration.
- Detection findings are correlated across data sources to
 reduce alert fatigue and flag high-confidence sovereignty
 violations for immediate response.

## Common issues to watch for

- Threat detection services enabled with default rulesets that
 don't cover sovereignty-specific threats, creating blind spots
 for cross-border data exfiltration and operator access
 violations.
- Centralized logging architectures that aggregate telemetry
 across jurisdictions without access controls, violating data
 residency requirements for the logs themselves.
- Operator action logs that record what was done but not from
 where or by whom at a sufficient level of detail, making
 forensic investigation and regulatory reporting incomplete.
- Alert volume that overwhelms investigation teams because
 detection rules lack tuning for sovereignty context, producing
 false positives from legitimate cross-Region operational
 activity.
- Investigation workflows that require cross-jurisdictional data
 access to complete, creating a circular dependency when the
 data residency controls prevent the investigation from
 proceeding.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dssec04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
