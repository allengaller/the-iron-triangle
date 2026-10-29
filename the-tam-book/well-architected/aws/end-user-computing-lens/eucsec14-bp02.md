<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec14-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCSEC14-BP02 Encrypt data in transit in your EUC environment

Use encryption to protect data confidentiality while in transit
 inside your EUC environment.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

Use AWS EUC streaming protocols to encrypt streaming data in
 transit. Amazon WorkSpaces and Amazon WorkSpaces Applications provide
 data encryption of pixel streaming traffic between instances
 and end user devices by default. Evaluate the default levels
 of encryption to verify that they provide sufficient
 protection in terms of key length and cipher suites and
 satisfy the requirements of the organization. For further
 details regarding the encryption used for Amazon AppStream,
 see
 [Data
 Protection in Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/data-protection.html) , and for Amazon WorkSpaces, see
 
 
 [Data
 Protection in Amazon WorkSpaces.](https://docs.aws.amazon.com/workspaces/latest/adminguide/data-protection.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec14-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
