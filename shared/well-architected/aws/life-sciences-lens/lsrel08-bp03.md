<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel08-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSREL08-BP03 Align architecture priorities with scientific and regulatory context

Early in the design cycle, evaluate the scientific and regulatory
 priorities of each workload. In patient-facing clinical workloads,
 design for continuous availability with reconciliation workflows. In
 regulated manufacturing, prioritize data integrity in the
 architecture, even if this limits availability. Planning with these
 priorities in mind avoids trade-off surprises later.

**Desired outcome:** Availability
 trade-offs are consciously designed to meet workload-specific
 requirements.

**Common anti-patterns:**

- Treating each workload with a uniform HA design.
- Prioritizing availability at the cost of data integrity in
 regulated processes.
- Failing to document the rationale for architectural trade-offs.

**Benefits of establishing this best
 practice:** Aligns architectures with the unique regulatory
 and scientific priorities of each workload, and improves
 transparency in audits.

## Implementation guidance

Architectural planning should explicitly evaluate the workload's
 scientific and regulatory context before finalizing availability
 and failover mechanisms. For example, clinical trial systems may
 tolerate some reconciliation steps post-recovery if availability
 is critical, while batch manufacturing systems may require
 uncompromising data integrity even if it reduces availability.
 Document these trade-offs, rationale, and validation approach as
 part of the design package.

### Implementation steps

1. Capture availability and data integrity requirements in
 system requirements specifications and risk assessments.
2. Map RTO and RPO targets to these requirements.
3. On AWS, implement availability features with services like
 Amazon Aurora Multi-AZ or Amazon S3 Versioning, paired with
 validation steps for data integrity.
4. Store architecture trade-off documentation and validation
 outcomes in a controlled repository for audit readiness.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel08-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
