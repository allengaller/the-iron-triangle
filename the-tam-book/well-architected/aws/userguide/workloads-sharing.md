<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-sharing.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Share a workload in AWS Well-Architected Tool

AWS Well-Architected Agent is in preview release and is subject to change.


You can share a workload that you own with other AWS accounts, users, an organization, and organization units (OUs) in the
 same AWS Region.

###### Note

You can only share workloads within the same AWS Region.

When sharing a workload with another AWS account, if the recipient does not have
 the `wellarchitected:UpdateShareInvitation` permission, they cannot
 accept the share invitation. See [Providing users, groups, or roles access to AWS WA Tool](./iam-auth-access.html) for permission
 policy examples.

###### To share a workload with other AWS accounts and users

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).
2. In the left navigation pane, choose **Workloads**.
3. Select a workload that you own in one of the following ways:
Choose the name of the workload.
Select the workload and choose **View
 details**.
4. Choose **Shares**. Then choose
 **Create** and **Create shares to users or accounts** to
 create a workload invitation.
5. Enter the 12-digit AWS account ID or the ARN of the user that you want to
 share the workload with.
6. Choose the permission that you want to grant.
**Read-Only**
Provides read-only access to the workload.
**Contributor**
Provides update access to answers and their notes, and read-only
 access to the rest of the workload.
7. Choose **Create** to send a workload invitation to the
 specified AWS account or user.

If the workload invitation is not accepted within seven days, the invitation is
 automatically expired.

If a user and the user's AWS account both have workload invitations, the workload
 invitation with the highest level permission is applied to the user.

###### Important

Before sharing a workload with an organization or organization units (OUs),
 you must [enable AWS Organizations
 access](./sharing.html#getting-started-sharing-orgs).

###### To share a workload with your organization or OUs

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).
2. In the left navigation pane, choose **Workloads**.
3. Select a workload that you own in one of the following ways:
Choose the name of the workload.
Select the workload and choose **View
 details**.
4. Choose **Shares**. Then choose
 **Create** and **Create shares to Organizations**.
5. On the **Create workload share** page, choose whether to grant permissions
 to the entire organization, or to one or more OUs.
6. Choose the permission that you want to grant.
**Read-Only**
Provides read-only access to the workload.
**Contributor**
Provides update access to answers and their notes, and read-only
 access to the rest of the workload.
7. Choose **Create** to share the workload.

To see who has shared access to a workload, choose **Shares** from
 the [View workload details in AWS Well-Architected Tool](./workload-details.html) page.

To prevent an entity from sharing workloads, attach a policy that denies
 `wellarchitected:CreateWorkloadShare` actions.

You can also share custom lenses that you own with other AWS accounts, users,
 your organization, and OUs 
 in the same AWS Region. For details, refer to [Sharing a custom lens in AWS WA Tool](./lenses-sharing.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-sharing.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
