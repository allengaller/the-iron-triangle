<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCPERF10-BP01 Align the instance type and instance size of a fleet with the workload

As needed, user environments can be updated on a pre-determined schedule or in response
 to periodic changes in performance to satisfy a change in the anticipated demand for
 resources.

**Level of risk exposed if this best practice is not
 established:** Low

## Implementation guidance

Determine the optimal instance family and size for your applications.

- The non-graphics instance families can utilize the same image across them. This
 provides image portability across these instance families and the instance sizes
 associated with them and allows varying requirements for compute resources to be
 catered for.
- Images created for a graphics instance family (for example, stream.graphics.g5)
 can only be associated with that family due to the specific GPU drivers for the
 associated GPU. Consequently, choose a graphics instance family carefully from the
 outset to avoid the need to create a new image for a different GPU family.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
