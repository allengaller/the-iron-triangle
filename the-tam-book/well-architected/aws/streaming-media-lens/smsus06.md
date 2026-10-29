<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus06.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Movement and caching

Every transfer carries energy and often triggers duplicate processing downstream. Streaming amplifies both distance and repetition because popular assets are requested millions of times.

## Capability intent

- Content is served from caches close to viewers so repeated requests don't return to origin.
- Processing stays within a single Region where the architecture allows.
- Intermediate file movement between stages is minimized.
- Hot metadata is served from memory rather than queried on every request.

## Common issues to watch for

- Serving directly from origin on every request instead of caching at the edge.
- Spreading a transcode pipeline across regions so large files copy between regions at each stage.
- Re-fetching whole assets when only a portion has changed.
- No measurement of cache hit ratio or cross-region transfer volume.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus06.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
