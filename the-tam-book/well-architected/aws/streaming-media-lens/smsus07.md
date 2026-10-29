<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus07.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Efficient hardware

The processor family and accelerator you select directly determine how much energy a given amount of work consumes.

## Capability intent

- Workloads run on the most efficient processor family that supports them.
- Specialized tasks use purpose-built hardware rather than general-purpose compute.
- Interruption-tolerant batch draws from spare capacity rather than dedicated instances.
- Hardware choices are revisited as more efficient generations become available.

## Common issues to watch for

- Running on older instance families when a more efficient option exists with no functional change.
- Self-managed transcoding on general-purpose compute instead of purpose-built media services.
- Over-allocating GPUs to tasks that don't need them.
- No tracking of compute hours by instance family.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus07.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
