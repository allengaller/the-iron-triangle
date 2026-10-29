<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-delete.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Delete a workload in AWS Well-Architected Tool

AWS Well-Architected Agent is in preview release and is subject to change.


You can delete a workload when it's no longer needed. Deleting a workload removes all data
 associated with the workload including any milestones and workload share invitations.
 Only the owner of a workload can delete it.

###### Warning

Deleting a workload cannot be undone. All data associated with the workload is permanently
 removed.

###### To delete a workload

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).
2. In the left navigation pane, choose **Workloads**.
3. Select the workload you want to delete and choose **Delete**.
4. In the **Delete** window, choose **Delete** to confirm
 the deletion of the workload and its milestones.

To prevent an entity from deleting workloads, attach a policy that denies
 `wellarchitected:DeleteWorkload` actions.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-delete.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
