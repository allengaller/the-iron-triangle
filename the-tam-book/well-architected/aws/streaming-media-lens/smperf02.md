<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Source contribution

Source quality and transport reliability constrain what the entire downstream pipeline can deliver. Contribution protocol choice and source acquisition quality have a direct effect on what viewers ultimately see.

## Capability intent

- Sources are acquired at the highest quality reasonably obtainable for the use case.
- Contribution uses reliable UDP-based transport protocols with redundant paths.
- Transport metrics (round-trip time, packet loss, jitter) are monitored in real time with auto-failover.

## Common issues to watch for

- Accepting whatever a provider delivers without specifying quality requirements.
- Using TCP-based contribution (RTMP) for mission-critical live without fallback.
- Monitoring only bit rate while ignoring loss, jitter, and round-trip time.
- Single network path without bonded or redundant connectivity.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
