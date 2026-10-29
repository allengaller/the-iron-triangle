<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf07-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCPERF07-BP01 Conduct realistic end-to-end testing aligned with organizational objectives

When planning to conduct testing, consider how your users interact with the EUC service
 and on an everyday basis. Create tests that align with the primary use of the service
 initially and expand to edge cases over time or in response to incidents to verify that they
 do not arise in future iterations of the service.

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Conduct tests that align with the expected use of the service. Work backwards from
 organizational objectives to conduct realistic tests. For example, consider any use case
 where remote users process invoices in an accounting application. Key metrics may include
 the number of invoices that each user processes per hour and their accuracy. A realistic
 test would include experienced application users processing actual invoices, using
 representative client devices under typical network conditions.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf07-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
