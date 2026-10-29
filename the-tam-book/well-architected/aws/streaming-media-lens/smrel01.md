<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smrel01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Content ingestion and contribution

Ingestion is the entry point of the streaming workflow. Failures here cascade through the entire delivery chain. Ingestion reliability covers redundant contribution paths for live sources and validated, resumable transfers for file-based content.

## Capability intent

- Live streams continue without interruption when individual contribution sources, encoders, or network paths fail.
- Large media files transfer reliably with automatic recovery from network interruptions.
- Content is validated before entering the processing pipeline.
- Geographic redundancy helps protect against site-level failures at ingest.

## Common issues to watch for

- Single encoder or single network path for live contribution with no redundancy.
- No resume capability for large file transfers, requiring full re-upload on failure.
- Content entering the processing pipeline without integrity or quality validation.
- Plain RTP without retransmission for contribution over unreliable networks.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smrel01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
