<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Encoding and delivery

Every avoidable bit in an encode is multiplied across millions of viewing sessions in network transfer and client decode energy.

## Capability intent

- Bit rate is allocated based on content complexity and measured viewing demand, not a fixed profile.
- Renditions that are not requested are not produced or stored.
- Codec and packaging choices are made per content tier, weighing compression gains against encode cost and device reach.
- Lightweight delivery logic runs at the edge rather than generating origin round-trips.
- Encoding efficiency is measured through resource proxies and reviewed regularly.

## Common issues to watch for

- A single fixed bit rate ladder applied to all content regardless of complexity.
- Pre-encoding every rendition for the full catalog, including titles that are rarely watched.
- Adopting a newer codec across the whole catalog without confirming device decode support.
- No measurement of bytes delivered per viewing session or encode compute per title.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
