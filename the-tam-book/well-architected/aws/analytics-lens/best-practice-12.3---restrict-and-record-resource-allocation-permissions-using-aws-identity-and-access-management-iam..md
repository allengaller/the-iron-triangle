<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-12.3---restrict-and-record-resource-allocation-permissions-using-aws-identity-and-access-management-iam..html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best practice 12.3 – Restrict and record resource allocation permissions using AWS Identity and Access Management (IAM)

To better control costs, create distinct IAM roles that authorize users to provision certain resources. This ensures that only permitted individuals can provision the resources they are allowed to, preventing unauthorized and unnecessary spending.

## Suggestion 12.3.1 – Create a cost governance framework that uses specialized IAM roles, rather than individual users, to provision costly infrastructure

Restrict the authorization to launch costly resources to
 specific IAM roles. For example, certain instances types
 can only be provisioned by certain teams to reduce
 unnecessary expenditure.

## Suggestion 12.3.2 – Track AWS CloudTrail logs to determine overall usage-per-user and role

Track the usage across users and roles to get a clear understanding of resource
 usage. As part of your cost-allocation governance, automatically process the AWS CloudTrail logs so
 that cost allocation is properly attributed to the relevant department.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-12.3---restrict-and-record-resource-allocation-permissions-using-aws-identity-and-access-management-iam..html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
