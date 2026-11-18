<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC01-BP05 Implement incident response playbooks

Develop and test incident response playbooks for common OT/IT scenarios such as device
 compromise, unauthorized access, and data exfiltration. Verify your cross-functional
 coordination and readiness to minimize downtime and safety risks.

**Desired outcome:** Manufacturing organizations respond to
 incidents swiftly with predefined procedures, minimizing production disruption.

**Benefits of establishing this best practice:** Improves MTTD
 and MTTR, reduces risk of safety events, and improves regulatory and audit outcomes.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Use AWS Systems Manager, AWS Lambda, and Amazon EventBridge to automate containment and
 response. Simulate scenarios to validate readiness.

### Implementation steps

- Identify critical incident types and build corresponding playbooks.
- Use AWS Systems Manager Automation to orchestrate predefined remediation.
- Run chaos experiments using AWS Fault Injection Service to test response
 efficacy.
- Train IT and OT teams on roles and escalation procedures.

## Resources

**Related documents:**

- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [AWS Fault Injection Service](https://aws.amazon.com/fis/)
- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
