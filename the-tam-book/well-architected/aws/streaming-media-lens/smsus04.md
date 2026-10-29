<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Live streaming efficiency

Live workflow resource cost is governed by event duration and concurrent audience rather than catalog size. Channels that run idle between events or default to ultra-low latency for every stream consume resources without corresponding value.

## Capability intent

- Live channels run only for the scheduled event window and stop when the event ends.
- The latency tier for each event matches the experience requirement rather than defaulting to the lowest available.
- Pipeline redundancy is applied where availability justifies it, not uniformly.
- Supporting components scale to observed concurrency rather than a peak assumption.

## Common issues to watch for

- Channels left running continuously between events.
- Ultra-low latency applied as a blanket default regardless of content type.
- Standing redundant pipelines for all channels regardless of the event's availability needs.
- No tracking of channel run-hours or redundant pipeline-hours per event.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
