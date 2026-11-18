<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC02-BP04 Develop a mechanism for regular review of IAM roles and policies

Establish processes to regularly review IAM roles and permissions to help prevent
 privilege creep and maintain access integrity over time.

**Desired outcome:** Stale or over-permissive access is
 detected and remediated proactively.

**Benefits of establishing this best practice:** Improves
 compliance posture, reduces operational risk, and enforces clean access policies aligned to
 least privilege.

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Use tools like IAM Access Analyzer, AWS Config, and custom automation to audit and
 report access configuration regularly.

### Implementation steps

- Establish a schedule for IAM access reviews.
- Use AWS IAM Access Analyzer to identify unused or overly broad permissions.
- Log and track review outcomes for auditing purposes.
- Automate revocation or modification of unneeded permissions using AWS Lambda or
 AWS Systems Manager.

## Resources

- [Using IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer.html)
- [iam-user-policy-check](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-policy-check.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
