<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/deactivate-ta-for-workload.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Deactivating Trusted Advisor for a workload

AWS Well-Architected Agent is in preview release and is subject to change.


**To deactivate Trusted Advisor for a workload**

You can deactivate Trusted Advisor for any workload from the AWS Well-Architected Tool by editing your workload
 and deselecting **Activate Trusted Advisor**. For more information on
 editing workloads, see [Edit a workload in AWS Well-Architected Tool](./workloads-edit.html).

Deactivating Trusted Advisor from the AWS WA Tool does not delete the roles created in IAM.
 Deleting roles from IAM requires a separate cleanup measure. Workload owners or
 owners of associated accounts should delete the IAM roles created when Trusted Advisor is
 deactivated in AWS WA Tool, or to stop AWS WA Tool from collecting Trusted Advisor data for the
 workload.

**To delete the WellArchitectedRoleForTrustedAdvisor in IAM**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).
2. In the navigation pane of the **IAM** console, choose
 **Roles**.
3. Search for
 `WellArchitectedRoleForTrustedAdvisor- WORKLOAD_OWNER_ACCOUNT_ID`
 and select the role name.
4. Choose **Delete**. In the pop-up window, type the
 name of the role to confirm deletion, and select **Delete** again.

For more information about deleting a role from IAM, see [Deleting an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#roles-managingrole-deleting-console) in the *IAM User
 Guide*.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/deactivate-ta-for-workload.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
