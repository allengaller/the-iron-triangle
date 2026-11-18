<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus03-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCSUS03-BP02 Adapt the AutoStop timeout and idle disconnect timeout for Amazon DCV

The AutoStop timeout in WorkSpaces is only available with AutoStop. This is not applicable
 to AlwaysOn WorkSpaces. In WorkSpaces, you can configure how long a user can be inactive while
 connected to a WorkSpace before they are disconnected. Amazon DCV (Desktop Cloud Virtualization)
 is the remote display protocol used by Amazon WorkSpaces to stream pixels, keystrokes and mouse
 movements.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

By default, AutoStop time (in
 hours**)** is set to one hour,
 which means that the WorkSpace stops automatically an hour
 after the WorkSpace is disconnected. Keep the AutoStop time
 at the default value, as this is the lowest value offered.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus03-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
