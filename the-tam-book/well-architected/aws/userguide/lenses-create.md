<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-create.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Creating a custom lens for a workload in AWS WA Tool

AWS Well-Architected Agent is in preview release and is subject to change.


###### To create a custom lens

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).
2. In the left navigation pane, choose **Custom
 lenses**.
3. Choose **Create custom lens**.
4. Choose **Download file** to download the JSON template
 file.
5. Open the JSON template file with your favorite text editor and add the
 data for your custom lens. This data includes your pillars, questions, best
 practices, and improvement plan links.
Refer to [Lens format specification in AWS WA Tool](./lenses-format-specification.html) for details. A custom lens
 cannot exceed 500 KB in size.
6. Choose **Choose file** to select your JSON file.
7. (Optional) In the **Tags** section, add any tags you want to
 associate with the custom lens.
8. Choose **Submit & Preview** to preview the custom lens, or
 **Submit** to submit the custom lens without
 previewing.
If you choose to **Submit & Preview** your custom
 lens, you can select **Next** to navigate through the
 lens preview, or select **Exit Preview** to go back to **Custom lenses**.

If validation fails, edit your JSON file and try creating the custom lens
 again.

After AWS WA Tool validates your JSON file, your custom lens is displayed in
 **Custom lenses**.

After a custom lens has been created, it's in **DRAFT** status.
 You must [publish the lens](./lenses-publish.html) before it can be
 applied to workloads or shared with other AWS accounts.

You can create up to 15 custom lenses in an AWS account.

###### Disclaimer

Do not include or gather personal identifiable information (PII) of end users
 or other identifiable individuals in or via your custom lenses. If your custom
 lens or those shared with you and used in your account do include or collect PII
 you are responsible for: ensuring that the included PII is processed in
 accordance with applicable law, providing adequate privacy notices, and
 obtaining necessary consents for processing such data.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-create.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
