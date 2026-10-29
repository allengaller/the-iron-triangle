<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smcost03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Encoding and quality optimization

Encoding decisions directly determine delivery cost. Lower bit rate at equivalent quality means fewer bytes to store and transfer. Content-aware encoding matches spend to complexity rather than applying uniform high bitrates.

## Capability intent

- Quality is measured objectively (VMAF, PSNR) alongside cost so that encoding changes can be evaluated.
- Encoder settings vary by content type and viewing context rather than applied uniformly.
- Variable bit rate modes spend bits where complexity demands them and save where it doesn't.

## Common issues to watch for

- Fixed high bit rate without measuring whether the quality justifies the cost.
- Identical encoding settings for all content regardless of complexity (static compared to fast motion).
- CBR used everywhere instead of variable bit rate modes that reduce average bandwidth.
- Encoding changes made without measuring the impact on both quality and cost.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smcost03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
