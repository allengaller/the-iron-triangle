<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smops02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Observability

Streaming workflows are distributed systems spanning ingest, processing, origin, CDN, and client. Detecting, diagnosing, and resolving issues requires visibility into metrics, events, and dependencies across all of these layers.

## Capability intent

- KPIs and SLOs are defined for each layer of the streaming workflow.
- Metrics are collected at sufficient granularity to isolate issues to specific components.
- Logs from all components are aggregated and correlated for cross-workflow troubleshooting.
- Application code is instrumented with contextual telemetry for rapid diagnosis.

## Common issues to watch for

- Metrics defined but not tied to alerting thresholds or SLOs.
- Logs siloed per component with no way to correlate events across the pipeline.
- Client-side telemetry missing, so viewer-facing quality issues go undetected.
- Observability instrumentation added after launch rather than built in.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smops02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
