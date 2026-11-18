<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops03-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSOPS03-BP02 Limit available services to improve regulatory adherence

Use infrastructure tooling to allow only services that fit into
 required regulatory frameworks.

**Desired outcome:** Only approved
 services will be available for use.

**Level of risk exposed if this best practice
 is not established:** Medium

## Implementation guidance

Verify components and services used as available to comply with
 identified frameworks. Check vendor documentation to confirm that
 the products you use are approved at the vendor level.

### Implementation steps

1. Identify the available services by referring to
 [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).
2. Review audit guides for the available services.
3. Setup an AWS Organization to be able to centrally manage
 policies and controls.
4. Implement service control policies (SCP) limiting access to
 only the available services.

## Resources

**Related guides, videos, and
 documentation:**

- [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)
- [What
 is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
- [Service
 control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

**Related tools:**

- [AWS Organizations](https://aws.amazon.com/organizations/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops03-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
