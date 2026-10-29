<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC02-BP01 Enforce least privilege and security policies to control system access

Minimize access rights for users and systems by enforcing least privilege principles.
 This reduces the risk of lateral movement and privilege escalation in manufacturing
 environments.

**Desired outcome:** Users and systems can only access
 resources necessary for their roles, reducing exposure to unauthorized activities.

**Benefits of establishing this best practice:** Limits the
 scope of security incidents and enhances overall control over sensitive manufacturing
 resources.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Map access requirements for different production roles and critical system
 interactions. Implement IAM policies and SCPs aligned with manufacturing functions,
 enforcing clear boundaries between IT/OT systems. Monitor access patterns using AWS IAM Access Analyzer to continually align with operational needs.

### Implementation steps

- Conduct role analysis across IT/OT to define minimum required privileges.
- Apply IAM permission boundaries and SCPs at account and organizational unit
 levels.
- Use IAM Access Analyzer to detect overly permissive roles.
- Implement regular audits to verify adherence to least privilege policies.

## Resources

**Related documents:**

- [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Using IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
