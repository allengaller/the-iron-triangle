<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Encoding and adaptive bit rate

Encoding settings and the ABR ladder determine the balance between quality, bandwidth, and device compatibility. These decisions affect both viewer experience and delivery cost at scale.

## Capability intent

- The ABR ladder is sized to the actual device and network distribution of the audience.
- Renditions are spaced appropriately (1.5-2x between rungs) to avoid switching oscillation.
- Encoding settings are chosen per content type and validated with objective quality metrics.
- The ladder is reviewed regularly as audience devices and codecs evolve.

## Common issues to watch for

- Copying a default ladder without validating it against the actual audience.
- Too many renditions causing switching oscillation.
- Uniform encoding presets across all content regardless of complexity.
- Measuring only bit rate without objective quality metrics (VMAF, PSNR).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
