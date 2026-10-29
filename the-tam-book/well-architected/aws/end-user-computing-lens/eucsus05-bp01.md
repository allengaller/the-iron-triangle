<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus05-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCSUS05-BP01 Optimize machine image creation, copying, and sharing to each environment (like development, testing, and production)

Using automation with machine images facilitates scalability and
 elasticity, minimizing over-provisioning and associated energy
 consumption. Centralized management and compliance reporting
 further support sustainability initiatives. Overall, automation
 pipelines contribute to lower environmental impact and improved
 resource optimization.

**Level of risk exposed if this best
 practice is not established:** Low

## Implementation guidance

Use a dedicated and separate account to create your Amazon AppStream images to manage your
 changes and your image history. Push the image (copy or share) with other development or
 production AWS accounts. For more detail, see [UpdateImagePermissions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateImagePermissions.html) and [UpdateWorkspaceImagePermission](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceImagePermission.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus05-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
