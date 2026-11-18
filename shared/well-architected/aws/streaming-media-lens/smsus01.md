<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Region selection

Region selection determines the baseline environmental cost of a streaming service. The energy mix of the Region and the distance content travels to viewers are fixed before any other optimization takes effect.

## Capability intent

- Compute-intensive workloads run in regions chosen with carbon intensity as an explicit selection criterion.
- Content reaches viewers from nearby caches so transfer distance and energy are minimized.
- Multi-region footprint follows demonstrated redundancy and latency needs rather than default posture.
- Placement decisions are reviewed against measured per-region carbon data on a regular cadence.
- Latency-sensitive delivery and latency-tolerant batch work are placed independently based on their different proximity requirements.

## Common issues to watch for

- Selecting regions on cost and latency alone with no visibility into carbon intensity.
- Deploying to many regions for resilience that the workload doesn't require, multiplying infrastructure footprint.
- Serving a global audience from a single distant region because the architecture was never revisited after initial deployment.
- Placing compute-intensive transcoding in a high-carbon region for convenience when lower-carbon alternatives exist.
- No periodic review of placement against the AWS Customer Carbon Footprint Tool data.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
