<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec05-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCSEC05-BP01 Evaluate applications and data access requirements and implement entitlements accordingly

Assess the types of users, their associated risk profile, and
 the access that each group of users requires to understand the
 access permissions each group of users require. Map the
 requirements to security groups, such as Active
 Directory security groups and the required permissions granted
 to these groups. Continually maintain the users associated with
 the group to verify ongoing appropriate access to applications
 and data.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

- **Automate user
 entitlements**: Use a provisioning and
 entitlement system that automates the addition and removal
 of users from groups that provide role-based permissions
 access. Automation creates consistency in the approach for
 handling permissions.
- **Use templates for user
 creation:** Use templates when creating user
 accounts to avoid manual configuration of user groups and
 settings that may lead to overly permissive access.
- **Review user entitlements
 regularly**: Review user entitlements regularly
 to verify that they are aligned with each user's current
 role and access requirements to fulfill the role. Consider
 a regular cadence, such as a quarterly or monthly review.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec05-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
