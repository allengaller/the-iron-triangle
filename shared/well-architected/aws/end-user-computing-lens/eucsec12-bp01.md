<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec12-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCSEC12-BP01 Allow user access to only the software binaries needed to perform their job

Users should only have access to the software binaries required
 for them to perform their role. Access to additional software
 that could introduce risks should be blocked.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

Implement security controls to restrict access to software
 binaries. Permissions applied to software binaries present on
 Amazon WorkSpaces or WorkSpaces Applications instances should restrict
 the ability for users to run the programs and applications
 that they require to fulfill their role. Evaluate other
 software binaries present in the image to verify that the
 default permissions applied in the file system do not permit
 users to run them.

System hardening should also be considered to further secure
 the operating system image. For reference, consider the Center
 for Internet Security (CIS) AWS End User Compute Services
 Benchmark. You can apply your chosen security settings by
 incorporating them into the image pre-deployment,
 post-deployment using scripts, or for Windows instances by
 using Group Policy Objects (GPOs). In addition, for Windows
 instances, consider FSLogix or AppLocker to restrict access to
 specific software binaries.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec12-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
