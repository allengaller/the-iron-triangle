<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel10-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSREL10-BP03 Test data integrity under failure conditions

Design and execute specific tests to validate that data integrity is
 preserved during system failures, network outages, or recovery
 processes. For workloads involving trial data, manufacturing
 records, or patient datasets, enforce transactional boundaries, roll
 back partial updates safely, and block corrupted data from entering
 downstream systems.

**Desired outcome:**

- Data integrity maintained during failures and recovery.
- Tests confirm correct handling of partial transactions and error
 scenarios.
- Evidence demonstrates adherence to data integrity requirements.

**Common anti-patterns:**

- Relying on functional tests without failure/integrity
 validation.
- No rollback or compensation testing for partial failures.
- Assuming backups restore consistent datasets without testing.

**Benefits of establishing this best
 practice:**

- Protects against corrupted datasets invalidating scientific
 outcomes.
- Builds trust in data reproducibility and traceability for
 regulators.
- Avoids costly reruns of experiments or trials due to data loss.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

Incorporate integrity validation into test plans for recovery and
 failover.

Test for both transient disruptions and long-term outages.

Use domain-specific integrity checks for genomic, clinical, or
 manufacturing datasets.

### Implementation steps

1. Enable Amazon RDS point-in-time recovery and validate
 consistency after restore.
2. Run AWS Glue Data Quality jobs to verify schema and record
 consistency.
3. Store validation reports in Amazon S3 with Object Lock for
 immutability.
4. Integrate validation results into reports with AWS Audit
 Manager.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel10-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
