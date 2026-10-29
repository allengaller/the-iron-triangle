<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsec03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Forensics

When content is distributed without consent, forensic controls help trace leaked material back to its source. This covers watermarking and session-level traceability.

## Capability intent

- Leaked content can be traced to the specific session or user that captured it.
- Forensic watermarking is applied invisibly across all distribution channels.
- A mapping between watermark identifiers and playback sessions is maintained.

## Common issues to watch for

- No watermarking capability at all.
- Single shared watermark ID rather than per-session identifiers.
- Only visible watermarks without invisible forensic ones.
- No active piracy monitoring to detect when leaked content surfaces.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsec03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
