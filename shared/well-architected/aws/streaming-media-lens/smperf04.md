<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Viewer experience measurement

Infrastructure monitoring provides only part of the picture. Real user monitoring and client-side metrics are necessary to understand what viewers actually experience and to correlate client-side issues with infrastructure events.

## Capability intent

- Client telemetry is collected and correlated with CDN and infrastructure logs.
- Metrics are broken down by geography, device, ISP, and title.
- Alerts correlate client-side quality events with infrastructure signals.

## Common issues to watch for

- Relying solely on server-side logs with no client telemetry.
- Client telemetry in a system that can't correlate with CDN or origin data.
- No breakdown by geography or device, so localized issues are invisible.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
