<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smrel03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Content distribution

Content distribution is the final step before viewers. Failures here directly cause buffering, playback errors, or complete outages. Distribution reliability covers origin redundancy, CDN failover, and multi-tier caching.

## Capability intent

- Viewers receive uninterrupted streaming when individual origin servers, CDN points of presence, or entire regions experience outages.
- Origin failover is health-check-driven and automatic.
- Cache warming prepares edge locations ahead of high-demand live events.
- Multi-CDN or multi-origin strategies provide fallback when a single path fails.

## Common issues to watch for

- Single origin without failover or health-check-based routing.
- No origin shielding, so cache misses overwhelm origin during spikes.
- No cache warming for live events, causing a thundering herd at the origin on event start.
- Single CDN reliance with no fallback path for regional CDN failures.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smrel03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
