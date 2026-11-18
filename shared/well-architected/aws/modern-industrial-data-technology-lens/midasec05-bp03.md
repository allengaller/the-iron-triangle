<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec05-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC05-BP03 Implement data authorization models

Design and implement scalable data authorization frameworks using attribute-based or
 role-based access control (ABAC or RBAC) models.

**Desired outcome:** Users are granted access to data based on
 roles, attributes, or context, supporting scalable and secure access decisions.

**Benefits of establishing this best practice:** Improves
 flexibility in data sharing, reduces over-permissions, and enhances compliance controls.

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Define authorization attributes based on manufacturing context (like job function,
 facility, equipment type, or product line). Implement access controls using AWS Lake Formation for data-level permissions, AWS IAM conditions for resource access, and custom
 logic for specialized manufacturing scenarios.

Regularly review access patterns to verify alignment with production needs while
 maintaining security boundaries between IT and OT systems.

### Implementation steps

- Define business roles and relevant attributes (for example, plant location or
 department).
- Implement policies in Lake Formation or Amazon S3 bucket policies using
 conditions.
- Monitor access patterns and refine authorization models over time.
- Log and audit access for compliance reporting.

## Resources

- [What Is AWS Lake Formation?](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html)
- [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec05-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
