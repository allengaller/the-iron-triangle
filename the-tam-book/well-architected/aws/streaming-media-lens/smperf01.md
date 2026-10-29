<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Media origination

Origin technology selection directly affects delivery performance. The choice between pass-through origins and just-in-time packaging origins depends on workload characteristics. These include live compared to VOD, viewer count, latency targets, and format diversity.

## Capability intent

- Origin type is selected against workload characteristics rather than applied uniformly.
- The origin architecture can evolve without re-architecting the CDN or client stack.
- Pass-through and dynamic packaging are applied where each fits best.

## Common issues to watch for

- A single origin type used for both live and VOD regardless of their different requirements.
- Pass-through origins where just-in-time packaging would remove format proliferation.
- Tight coupling between origin and CDN that blocks independent evolution.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smperf01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
