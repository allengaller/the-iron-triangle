<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/define-workload-from-template.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Defining a workload from a template in AWS WA Tool

AWS Well-Architected Agent is in preview release and is subject to change.


You can define a workload from a review template that you created or a review template
 that has been shared with you. You cannot define a new workload from a review template
 that has been deleted, and if the review template contains an outdated version of a
 lens, you must upgrade the review template before you can define a new workload from it.
 For information on how to upgrade a review template, see [Upgrading a lens in AWS WA Tool](./lenses-upgrading.html).

###### Note

To define a workload from a review template, you must have IAM permissions to create a
 workload enabled:`wellarchitected:CreateWorkload`, as well as the
 following review template permissions:
 `wellarchitected:GetReviewTemplate`,
 `wellarchitected:GetReviewTemplateAnswer`,
 `wellarchitected:ListReviewTemplateAnswers`, and
 `wellarchitected:GetReviewTemplateLensReview`. For more information
 about IAM permissions, see the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

###### To define a workload from a review template

1. Select **Review templates** in the left navigation pane.
2. Select the name of the review template you want to define a workload from.
3. Choose **Define workload from template**.
NoteYou can also choose **Define from review template** from the **Define workload** dropdown on the **Workloads** page.
4. On the **Select review template** step, select the review template card, and choose **Next**.
5. On the **Specify properties** step, fill out required fields for the workload
 properties, and choose **Next**. For more detail, see [Defining a workload in AWS WA Tool](./define-workload.html).
6. (Optional) On the **Apply Profile** step, associate a
 profile with the workload by selecting an existing profile, searching
 for the profile name, or choosing **Create profile** to [create a profile](./tool-creating-a-profile.html). Choose
 **Next**.
[Well-Architected profiles](./tool-profiles.html) and review templates
 can be used in tandem. The questions that are pre-filled in your review template
 remain answered in the workload, and the questions are prioritized based on your
 profile.
7. (Optional) On the **Apply lenses** step, you may choose to apply additional lenses from **Custom lenses** or **Lens catalog** that were not already applied to the review template.
8. Choose **Define workload**.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/define-workload-from-template.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
