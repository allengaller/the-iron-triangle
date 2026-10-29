<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Content delivery

CDN configuration and cache strategy determine whether viewers are served from nearby edge locations or generate repeated requests back to origin. Cache hit ratio is the primary performance and efficiency metric for delivery.

## Capability intent

- A CDN is in front of every origin with cache hit ratio tracked per content type.
- Cache-control headers are set per content type (live manifests, segments, and VOD assets).
- Origin shield collapses redundant requests from multiple edge locations.
- Invalidation is targeted rather than full-distribution.

## Common issues to watch for

- Tracking bandwidth but not cache hit ratio.
- Default cache-control headers that cause either over-caching of dynamic content or under-caching of static content.
- Caching live manifests as long as segments, causing stale playback.
- Full-distribution invalidation instead of path-targeted invalidation.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
