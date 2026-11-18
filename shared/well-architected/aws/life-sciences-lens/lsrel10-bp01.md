<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel10-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSREL10-BP01 Implement comprehensive reliability testing

Develop structured protocols that test reliability aspects including
 load performance, failover, recovery, and long-term stability. For
 regulated systems, include reliability tests in the validation
 package with traceability to user and regulatory requirements. Use
 controlled chaos engineering experiments to validate resilience by
 safely injecting faults and failures into your applications while
 preserving data integrity and adherence.

**Desired outcome:**

- Reliability tests are systematic, repeatable, and documented.
- Systems demonstrate resilience to failure injection and load
 stress.
- Test evidence supports regulatory validation requirements.

**Common anti-patterns:**

- Treating reliability tests as optional instead of mandatory.
- Running only idealized tests without simulating failures.
- Lack of traceability between reliability test cases and
 regulatory or user requirements.

**Benefits of establishing this best
 practice:**

- Improves predictability of experiments and workloads under
 stress.
- Builds regulator and auditor confidence in system resilience.
- Reduces costly delays by uncovering reliability gaps early.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

Define reliability acceptance criteria in line with user and
 regulatory requirements.

Incorporate resilience tests into validation and qualification
 protocols.

Perform controlled chaos experiments to uncover weaknesses safely.

Automate reliability testing where possible for repeatability.

### Implementation steps

1. Run fault-injection experiments with AWS Fault Injection Service (FIS).
2. Use AWS CodePipeline to integrate reliability tests into
 CI/CD.
3. Capture test logs in Amazon CloudWatch Logs and archive
 evidence in Amazon S3 Object Lock for regulatory adherence.
4. Document test execution and results in AWS Audit Manager.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel10-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
