<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf07.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Advertising integration

Ad insertion affects streaming performance, viewer experience, and monetization. SSAI and CSAI have different performance characteristics. Proper ad integration maintains playback continuity while maximizing fill rate.

## Capability intent

- Ads are stitched into a single stream with matched resolution, bit rate, codec, and frame rate.
- Ad insertion failures don't break content playback (timeout and fallback).
- Ad prefetching fills inventory ahead of predictable breaks without violating targeting or expiry rules.

## Common issues to watch for

- Ads encoded at different bit rate, resolution, or codec than the main content causing visible transitions.
- No timeout on ad decisioning, causing playback stalls when the ad server is slow.
- Audio level mismatches between content and ads.
- Prefetching without expiry controls, serving stale or irrelevant ads.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf07.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
