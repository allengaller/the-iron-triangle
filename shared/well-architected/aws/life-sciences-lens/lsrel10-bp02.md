<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel10-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSREL10-BP02 Validate end-to-end reliability of regulated workloads

Conduct end-to-end reliability validation exercises that test not
 just recovery but the overall system's ability to maintain adherence
 and functionality during adverse events. These tests should validate
 high availability, monitoring alerts, automated failover, and
 controls in production-like scenarios.

**Desired outcome:**

- Holistic system reliability validated under real-world
 conditions.
- Compliance-aligned functions (audit trails, access controls,
 data integrity) remain intact during adverse events.
- Test outcomes provide documented evidence for regulatory audits.

**Common anti-patterns:**

- Focusing only on technical recovery while ignoring controls.
- Testing components in isolation but never validating the
 end-to-end system.
- No evidence of reliability testing available for auditors.

**Benefits of establishing this best
 practice:**

- Demonstrates system resilience across full workflows, not just
 components.
- Strengthens audit readiness with comprehensive reliability
 evidence.
- Reduces operational risk by validating reliability before real
 incidents occur.

**Level of risk exposed if this best practice
 is not established:** Medium

## Implementation guidance

Plan integrated reliability tests across application and data
 layers.

Simulate production-like workloads during validation.

Validate not only failover and monitoring but also regulatory
 controls.

Store test artifacts centrally with immutable retention.

### Implementation steps

1. Use AWS Elastic Load Balancing with Auto Scaling to validate
 failover.
2. Run simulated production workloads using AWS Batch or Amazon ECS.
3. Trigger alerts through Amazon CloudWatch Alarms and verify
 monitoring in AWS Config.
4. Archive reliability validation evidence in Amazon Glacier
 for long-term retention.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel10-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
