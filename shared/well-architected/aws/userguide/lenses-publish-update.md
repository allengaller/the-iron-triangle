<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-publish-update.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Publishing an update to a custom lens in AWS WA Tool

AWS Well-Architected Agent is in preview release and is subject to change.


###### To publish an update to an existing custom lens

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).
2. In the left navigation pane, choose **Custom
 lenses**.
3. Select the desired custom lens and choose
 **Edit**.
4. If you do not have an updated JSON file ready, choose **Download
 file** to download a copy of the current custom lens. Edit
 the downloaded JSON file with your favorite text editor and make your
 desired changes.
5. Choose **Choose file** to select your updated JSON file
 and choose **Submit & Preview** to preview the custom
 lens, or **Submit** to submit the custom lens without
 previewing.
A custom lens cannot exceed 500 KB in size.
After AWS WA Tool validates your JSON file, your custom lens is displayed in
 **Custom lenses** in **DRAFT**
 status.
6. Select the custom lens again and choose **Publish
 lens**.
7. Choose **Review
 changes before publishing** to verify that the changes made to
 your custom lens are correct. This includes validating:
The name of the custom lensThe pillar namesThe new, updated, and deleted questions
Choose **Next**.
8. Specify the type of
 version change.
**Major version**
Indicates that substantial changes have been made to the lens.
 Use for changes that impact the meaning of the custom
 lens.
Any workloads with the lens applied will be notified that a
 new version of the custom lens is available.
Major version changes are *not*
 automatically applied to workloads using the lens.
**Minor version**
Indicates that minor changes have been made to the lens. Use
 for small changes, such as text changes or updates to the URL
 links.
Minor version changes are automatically applied to workloads
 using the custom lens.
Choose **Next**.
9. In the **Version name** box, enter a unique identifier
 for the version change. This value can be up to 32 characters and must only
 contain alphanumeric characters and periods (".").
10. Choose **Publish custom lens**.
After a custom lens has been published, it's in
 **PUBLISHED** status.

The updated custom lens can now be applied to workloads or shared with other
 AWS accounts or users.

If the update is a *major version change*, any workloads with
 the previous version of the lens applied will be notified that a new version is
 available and given the option to upgrade.

Minor version updates are automatically applied without any notification.

You can create up to 100 versions of a custom lens.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-publish-update.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
