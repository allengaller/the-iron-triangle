<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsec04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Content ingest protection

Ingest endpoints accept content from providers and encoding devices. They need to be restricted to trusted sources and protected in transit to reduce the risk of injection, interception, or degradation.

## Capability intent

- Only authorized sources can send content into workflows.
- All ingest traffic is encrypted with current TLS versions.
- High-value content travels over private connectivity rather than the public internet.
- Physical media transfers use hardware encryption with chain-of-custody controls.

## Common issues to watch for

- Ingest endpoints accepting connections from any IP address.
- Unencrypted RTMP or HTTP contribution without TLS.
- Source content sent over public internet without dedicated connectivity.
- Stale ACL entries for former providers never removed.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsec04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
