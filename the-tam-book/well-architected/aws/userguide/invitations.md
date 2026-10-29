<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/invitations.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Share invitations

AWS Well-Architected Agent is in preview release and is subject to change.


A share invitation is a request to share a workload, custom lens, or review template owned by
 another AWS account. A workload or lens can be shared with all users in an AWS account,
 individual users, or both.

- If you accept a workload invitation, the workload is added to
 your **Workloads** and **Dashboard** pages.
- If you accept
 a custom lens invitation, the lens is added to your **Custom lenses** page.
- If you accept a profile invitation, the profile is added to your
 **Profiles** page.
- If you accept a review template invitation, the
 template is added to your **Review templates** page.

If you reject the
 invitation, it's removed from the list.

###### Note

Workloads, custom lenses, profiles, and review templates can only be shared within the
 same AWS Region.

The owner of the workload or custom lens controls who has shared access.

The **Share invitations** page, available from the left navigation,
 provides information about your pending workload and custom lens invitations.

The following information is displayed for each workload invitation:

The name of the workload, custom lens, or review template to be shared.

The type of invitation, either **Workload**, **Custom
 lens**, **Profiles**, or **Review template**.

The AWS account ID that owns the workload.

The permission that you are being granted to the workload.

- Read-Only
Provides read-only access to the workload, custom lens, profiles, or
 review template.
- Contributor
Provides update access to answers and their notes, and read-only
 access to the rest of the workload. This permission is only available
 for workloads.

Detailed description of the permission.

## Accepting a share invitation

###### To accept a share invitation

1. Select the share invitation to accept.
2. Choose **Accept**.

For workload invitations, the workload is added to the **Workloads**
 and **Dashboard** pages. For custom lens invitations, the custom lens
 is added to the **Custom lenses** page. For profile invitations, the
 profile is added to the **Profiles** page. For review
 template invitations, the template is added to the **Review templates**
 page.

You have seven days to accept an invitation. If you do not accept the invitation within
 seven days, it's automatically expired.

If a user and their AWS account both have accepted workload invitations, the
 workload invitation for the user determines the user's permission.

## Rejecting a share invitation

###### To reject a share invitation

1. Select the workload or custom lens invitation to reject.
2. Choose **Reject**.

The invitation is removed from the list.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/invitations.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
