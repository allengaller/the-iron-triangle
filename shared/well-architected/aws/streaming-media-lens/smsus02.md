<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Alignment to demand

Streaming demand varies by orders of magnitude across the day and across events. Infrastructure sized for a theoretical peak sits idle most of its life.

## Capability intent

- Media processing capacity follows real-time audience size rather than holding a static peak.
- Delivery bit rate adapts to each session's network and device capability.
- Deferrable processing runs during off-peak or lower-carbon-intensity periods.
- Scaling responds to both predictable patterns and unexpected demand spikes.
- Utilization is tracked and idle capacity is treated as waste to be reduced.

## Common issues to watch for

- Fixed provisioning based on a worst-case assumption that is never revisited.
- Delivering a single high bit rate to all viewers regardless of what their session can use.
- Running batch work during peak demand, competing with live traffic for resources.
- Reactive-only scaling without predictive pre-warming for known events.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
