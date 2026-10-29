<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel13-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSREL13-BP01 Implement comprehensive monitoring for regulated systems

Establish monitoring that spans infrastructure, applications, data
 integrity, and audit controls. For GxP systems, verify that your
 monitoring covers validation-critical parameters identified in risk
 assessments, so that regulated workloads can demonstrate continuous
 oversight.

**Desired outcome:**

- Holistic visibility into workload health and reliability.
- Early detection of anomalies across infrastructure and
 applications.
- Assurance that monitoring captures validation-critical
 parameters in GxP systems.

**Common anti-patterns:**

- Monitoring only infrastructure without application or data-level
 coverage.
- Relying on reactive alerts instead of proactive anomaly
 detection.
- Lack of defined monitoring scope for regulated workloads.

**Benefits of establishing this best
 practice:**

- Enables quick response before failures impact experiments or
 studies.
- Provides audit-ready evidence of system oversight for
 regulators.
- Improves researcher trust in system stability and availability.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

Design monitoring across layers, including infrastructure
 (compute, storage, network), application (latency, errors,
 throughput), and data integrity. Incorporate health checks aligned
 with business priorities. Define thresholds for alerting and
 automate incident response workflows. Retain monitoring records in
 adherence to retention and audit requirements.

### Implementation steps

1. Instrument workloads with Amazon CloudWatch metrics, alarms,
 and dashboards.
2. Capture logs centrally in Amazon CloudWatch Logs.
3. Use AWS X-Ray for distributed tracing of microservices.
4. Monitor configuration drift with AWS Config and events with
 AWS Security Hub CSPM.
5. Store monitoring evidence in Amazon S3 for regulatory
 audits.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel13-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
