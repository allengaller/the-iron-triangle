<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus09.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Development and deployment

The engineering process behind a streaming service carries its own resource footprint, dominated by idle non-production environments.

## Capability intent

- Non-production environments exist only when in use.
- Build environments are right-sized and dependencies are cached.
- Deployment overlap windows are as short as safety allows.
- Sustainability metrics are visible within the delivery pipeline.

## Common issues to watch for

- Development and staging environments running continuously including nights and weekends.
- Oversized build environments rebuilding dependencies from scratch every run.
- Blue/green deployments with long overlap windows doubling resources far beyond what cutover requires.
- No visibility into non-production running hours or build compute hours.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus09.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
