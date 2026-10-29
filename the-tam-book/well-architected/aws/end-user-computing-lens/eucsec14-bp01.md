<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec14-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCSEC14-BP01 Encrypt disk volumes to protect data at rest

Protect security, integrity, and availability of data at rest to
 make sure it is reliably accessible when needed.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

Encrypt Amazon WorkSpaces Personal disk volumes. Each Amazon
 WorkSpace Personal instance is provisioned with a root volume
 (C: drive for Windows WorkSpaces Personal, root file system
 for Amazon Linux WorkSpaces Personal) and a user volume (D:
 drive for Windows WorkSpaces Personal, /home for Amazon Linux
 WorkSpaces Personal). The encrypted WorkSpaces feature
 encrypts one or both volumes. For WorkSpaces Personal
 instances used by users (rather than for creating custom
 images), it is a best practice for these to be encrypted. For
 more details, see
 [Encrypted
 WorkSpaces in WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/encrypt-workspaces.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec14-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
