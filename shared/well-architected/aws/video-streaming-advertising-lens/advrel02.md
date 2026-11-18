<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Latency sensitive advertising

Consider strategies for managing latency-sensitive advertising
 workloads through throttling and rate-limiting implementations.
 Avoid traditional retry mechanisms for fast-failing services,
 implement effective caching strategies, and proportionally scale
 across all system components to maintain consistent performance.

###### Best practices

- [ADVREL02-BP01 To allow fast and graceful failure of latency-sensitive services, avoid exponential backing off and retry](./advrel02-bp01.html)
- [ADVREL02-BP02 Implement a caching strategy](./advrel02-bp02.html)
- [ADVREL02-BP03 Prevent scale mismatch of both internal services and external partners](./advrel02-bp03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
