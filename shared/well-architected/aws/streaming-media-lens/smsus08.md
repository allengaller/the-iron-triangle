<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus08.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Managed services

A self-managed component provisioned for one team's peak sits idle most of the time. Managed services aggregate demand across customers and scale to match, reaching higher average utilization.

## Capability intent

- Capabilities that have a managed equivalent are consumed as managed services.
- Workloads scale with demand rather than holding idle capacity for rare peaks.
- Engineering effort goes to streaming-specific differentiation rather than operating commodity infrastructure.

## Common issues to watch for

- Building bespoke infrastructure when a managed service provides the same capability at higher utilization.
- Standing clusters sized for peak to run intermittent work, idle between jobs.
- Self-hosting ML inference on persistent instances when managed inference scales with request volume.
- Assuming that managed is unconditionally better without evaluating workload fit.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus08.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
