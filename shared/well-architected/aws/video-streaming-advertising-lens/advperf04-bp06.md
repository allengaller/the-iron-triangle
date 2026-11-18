<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp06.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVPERF04-BP06 Consider AWS Clean Rooms collaboration

AWS Clean Rooms have limits on query result size (for example,
 AWS Clean Rooms has a 5GB limit), so consider using
 aggregations and filters to reduce result sets.

## Implementation guidance

Large datasets can impact query performance.
 Partition data effectively.

A higher number of collaborators in a collaboration channel
 impacts processing time. Consider this as one of the
 factors for designing the collaboration framework with
 collaborators in play.

AWS Clean Rooms offers analysis templates work to support parameterized queries assisting in performance improvement through query reuse. Optimize queries before creating templates.
 Consider the choice of cryptographic operations for secure computation, as it adds to processing time.

## Key AWS services

- AWS Clean Rooms

## Resources

- [Guidelines for the C3R encryption client](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-guidelines.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp06.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
