<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec08-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# GAMESEC08-BP01 Apply security at every stage of the CI/CD pipeline

Guardrails such as access controls, separation of duties, and
 audit trails provide protection against unauthorized access or
 malicious activities.

**Level of risk exposed if this best practice
 is not established:** Medium

## Implementation guidance

Your people, processes, and technology
 should secure the pipeline as well. The people closest to the code
 must establish secure coding practices and make sure they follow
 them. Iterate on your processes continuously to verify that there
 is consistency in the level of security throughout the pipeline.
 Lastly, implement technology to verify that best practices and
 processes are not bypassed.

**Customer example**

AnyCompany Games implements role-based access controls in which
 only senior developers can approve changes to their anti-cheat
 system code, while requiring mandatory code reviews from security
 team members for components that handle player payment data.

Their CI/CD pipeline automatically runs threat model validation
 checks, making sure that new features like a player trading
 marketplace are tested against previously identified attack
 vectors such as item duplication exploits or fraudulent
 transaction attempts.

### Implementation steps

- Provide users permissions bases on the principle of least
 privilege.
- Use AWS CloudTrail to audit API calls made across the
 services used in the pipeline.
- Employ pre-commit hooks to verify that code is following
 general practices and company policies.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec08-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
