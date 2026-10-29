<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf06.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Latency optimization

Live streaming latency affects viewer engagement, especially for interactive content and live events. Reducing latency requires coordinated optimization across encoding, packaging, delivery, and player layers, and involves trade-offs with quality and reliability.

## Capability intent

- Latency targets are set per use case and balanced against quality and reliability requirements.
- Optimization spans all layers (encoder, packager, CDN, and player buffer) rather than targeting one in isolation.
- Ultra-low-latency delivery is reserved for interactive use cases where sub-second matters.
- Graceful fallback to standard latency is available for unsupported clients or degraded networks.

## Common issues to watch for

- Reducing segment length without matching changes in other layers.
- Chasing latency numbers without researching whether viewers notice the difference.
- WebRTC deployed for passive broadcast where low-latency HLS would suffice.
- No fallback path for devices that don't support the chosen low-latency protocol.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf06.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
