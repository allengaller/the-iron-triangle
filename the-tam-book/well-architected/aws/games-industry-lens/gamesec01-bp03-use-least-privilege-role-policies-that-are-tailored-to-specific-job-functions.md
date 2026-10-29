<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01-bp03-use-least-privilege-role-policies-that-are-tailored-to-specific-job-functions.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# GAMESEC01-BP03 Use least privilege role policies that are tailored to specific job functions

Configuring IAM policies is an essential part of establishing a strong security
 foundation. When you set permissions with IAM policies, grant only the permissions required
 to perform a task. You do this by defining the actions that can be taken on specific resources
 under specific conditions, also known as least-privilege permissions. For example, QA teams
 need access to change things in the testing environments but should not have the ability to
 modify the production environment.

**Level of risk exposed if this best practice is not established:**
 Medium

## Implementation guidance

You might start with broad permissions, like [managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html),
 while you explore the permissions that are required for your workload or use case. As your use
 case matures, you can work to reduce the permissions that you grant to work toward least
 privilege.

### Implementation steps

- Follow the practice of least privilege permissions for create IAM roles for users
 and applications.
- Use AWS-managed policies to quickly provide broad access while identifying the
 specific permissions teams or applications need to perform their tasks.
- Studios can also use [IAM
 access analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_reduce-permissions-edit-policy.html) to generate custom IAM policies based on
 CloudTrail events that identify actions and services used by an IAM entry.
- Regularly review IAM policies and edit overly permissive policies.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01-bp03-use-least-privilege-role-policies-that-are-tailored-to-specific-job-functions.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
