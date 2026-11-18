<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec09-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC09-BP02 Perform regular vulnerability scans and penetration tests

Identify and mitigate vulnerabilities in applications and environments by conducting
 recurring scans and authorized penetration testing.

**Desired outcome:** Exposed vulnerabilities are proactively
 identified and mitigated before exploitation.

**Benefits of establishing this best practice:** Enhances
 visibility into system weaknesses and builds resilience against external and internal threats.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Use Amazon Inspector and integrate third-party scanning tools for deep and layered
 assessments.

### Implementation steps

- Schedule recurring scans using Amazon Inspector across EC2 and container
 workloads.
- Perform black-box and white-box pen tests with third-party experts.
- Integrate findings with AWS Security Hub CSPM for centralized visibility.
- Remediate critical vulnerabilities through prioritized CI/CD updates.

## Resources

- [Getting started with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/getting-started.html)
- [Penetration Testing](https://aws.amazon.com/security/penetration-testing/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec09-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
