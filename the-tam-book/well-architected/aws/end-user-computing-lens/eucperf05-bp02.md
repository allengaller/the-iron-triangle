<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf05-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCPERF05-BP02 Understand integrated storage capabilities (AppStream)

For persistent, per-user storage, WorkSpaces Applications offers built-in connectors to Amazon S3 home
 folders, Google Drive for Google Workspace, and OneDrive for Business. For more information
 on these connectors, see [Enable and Administer
 Persistent Storage for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/persistent-storage.html).

**Level of risk exposed if this best practice is not
 established:** Low

## Implementation guidance

Use Amazon S3 home folders when you need a simple, fully-managed solution for persisting
 user files between sessions and users don't need to access their files from outside their
 WorkSpaces Applications sessions. Use Google Drive for Google Workspaces or OneDrive for Business
 when you use Windows fleets and your users have a license for one of the services.

If the integrated storage features of Amazon WorkSpaces Applications do not offer the
 capabilities you require, consider Amazon FSx for Windows File Server, Amazon FSx for NetApp ONTAP, or Amazon EC2 hosted file
 sharing. You can use these fully or partly-managed solutions to store user data or user
 profiles, such as FSLogix, close to your AWS EUC control plane.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf05-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
