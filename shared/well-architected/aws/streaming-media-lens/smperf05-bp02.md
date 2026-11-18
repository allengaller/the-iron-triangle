<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf05-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# SMPERF05-BP02 Select appropriate encoding settings for your content type and quality targets

Choose encoding parameters matched to your content characteristics

(sports, animation, and talking heads) and validate output quality with objective metrics.

**Desired outcome:**

- You have encoder settings chosen against content characteristics (sports, animation, and talking heads) rather than applied uniformly across the library.
- Your codec and preset selections are validated against the target device fleet, so efficiency gains from newer codecs reach actual viewers.
- You measure output quality with objective metrics (Video Multimethod Assessment Fusion (VMAF), peak signal-to-noise ratio (PSNR)) or subjective assessment at each rendition, not just average bit rate.

**Common anti-patterns:**

- Using encoder presets without validating them against representative content (sports, animation, and film) that exposes different trade-offs.
- Optimizing purely for average bit rate without measuring perceived quality through VMAF, PSNR, or subjective assessment.
- Re-encoding previously encoded, lossy content without going back to the highest-quality source, compounding quality loss.

**Benefits of establishing this best practice:**

- Higher VMAF scores at the same bit rate by tuning to content complexity
- Lower bandwidth cost because content-aware settings avoid wasted bits on low-complexity scenes
- Reduced encoding compute cost from selecting appropriate presets per content type
- Consistent perceptual quality across renditions rather than consistent bit rate
- Smaller stored file sizes for the VOD library without visible quality loss

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance

Encoding quality is determined by rate-distortion performance, not bit rate alone. Two files at the same bit rate can deliver different perceived quality. Codec, preset, content complexity, and bit-allocation strategy all matter. Because of this, you need to measure output quality rather than relying on bit rate as a proxy. VMAF and PSNR give objective scores per frame and per rendition. Subjective review catches the cases where the metrics disagree with human perception. The optimization game is also not the same for live and video on demand (VOD). VOD tolerates multi-pass analysis and content-aware encoding, which let the encoder rebalance bits across the whole title. Live runs single-pass with hard real-time deadlines. The knobs are group of pictures (GOP) length, lookahead, and scene-change handling, and each setting also affects the latency budget covered in low-latency delivery.

### Implementation steps

1. **Analyze your content types and characteristics:** Understand the nature of your video content to inform encoding decisions.
2. **Select appropriate codecs based on use case and device support:** Use H.265/High Efficiency Video Coding (HEVC) for contribution feeds to optimize bandwidth, H.264/Advanced Video Coding (AVC) for broad device compatibility, and AOMedia Video 1 (AV1) for higher compression efficiency (20-30% additional savings over HEVC).
3. **Configure encoder settings based on content type:** Sports and action content requires higher bitrates and faster encoding presets, talking heads benefit from lower bitrates and quality-focused presets, and animation is optimized for flat colors and sharp edges.
4. **Use content-aware encoding features in AWS Elemental MediaConvert:** Use automated quality optimization capabilities.
5. **Implement quality testing and validation processes:** Verify encoding output meets quality standards.
6. **Monitor encoding efficiency and adjust settings based on results:** Continuously optimize encoder configurations.
7. **Consider using machine learning-based encoding optimization:** Explore ML-driven approaches for further efficiency gains.
8. **Plan codec migration strategy:** Consider device support timelines when planning codec transitions.

## Resources

**Related best practices**

- [SMPERF05-BP01 Optimize the number of adaptive bitrate renditions for your workload](smperf05-bp01.html)
- [SMPERF06-BP01 Optimize processing, origination, delivery, and client for low latency](smperf06-bp01.html)

**Related documents**

- [HLS Authoring Specification for Apple
- [AWS Elemental MediaConvert User

**Related services**

- [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/)
- [AWS Elemental MediaLive](https://aws.amazon.com/medialive/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf05-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
