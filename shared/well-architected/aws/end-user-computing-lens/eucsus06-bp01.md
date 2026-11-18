<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus06-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCSUS06-BP01 Stop image builders and app block builders when not in use

In WorkSpaces Applications, image builders and app block builders are two instances used only when
 creating your baseline image or application package. There is no requirement to keep them
 running.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

The [Cost Optimizer for Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/cost-optimizer-for-amazon-appstream-2-0-on-the-solutionist/) monitors your WorkSpaces Applications image builders, notifying
 you and halting them when they are active for longer than specified thresholds.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus06-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
