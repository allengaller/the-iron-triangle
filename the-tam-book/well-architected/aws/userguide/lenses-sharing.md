<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-sharing.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Sharing a custom lens in AWS WA Tool

AWS Well-Architected Agent is in preview release and is subject to change.


You can share a custom lens with other AWS accounts, users, AWS Organizations, and organization units (OUs).

###### To share a custom lens with other AWS accounts and users

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).
2. In the left navigation pane, choose **Custom
 lenses**.
3. Select the custom lens to be shared and choose **View
 details**.
4. On the [Viewing lens details for a workload in AWS WA Tool](./lenses-details.html)
 page, choose **Shares**. Then choose
 **Create** and **Create shares to users or accounts** to 
 create a lens share invitation.
5. Enter the 12-digit AWS account ID or the ARN of the user that you want
 to share the custom lens with.
6. Choose **Create** to send a lens share invitation to the
 specified AWS account or user.

You can share a custom lenses with up to 300 AWS accounts or users.

If the lens share invitation is not accepted within seven days, the invitation is
 automatically expired.

###### Important

Before sharing a custom lens with an organization or organization units (OUs),
 you must [enable AWS Organizations
 access](./sharing.html#getting-started-sharing-orgs).

###### To share a custom lens with your organization or OUs

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).
2. In the left navigation pane, choose **Custom
 lenses**.
3. Select the custom lens to be shared.
4. On the [Viewing lens details for a workload in AWS WA Tool](./lenses-details.html)
 page, choose **Shares**. Then choose
 **Create** and **Create shares to Organizations**.
5. On the **Create custom lens share** page, choose whether to grant permissions
 to the entire organization, or to one or more OUs.
6. Choose **Create** to share the custom lens.

To see who has shared access to a custom lens, choose **Shares**
 from the [Viewing lens details for a workload in AWS WA Tool](./lenses-details.html)
 page.

###### Disclaimer

By sharing your custom lenses with other AWS accounts, you acknowledge that
 AWS will make your custom lenses available to those other accounts. Those
 other accounts may continue to access and use your shared custom lenses even if
 you delete the custom lenses from your own AWS account or terminate your
 AWS account.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-sharing.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
