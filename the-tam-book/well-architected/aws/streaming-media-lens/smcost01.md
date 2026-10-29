<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smcost01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Storage and delivery costs

Storage and data transfer often represent the largest cost components. A strategy for lifecycle management and edge caching reduces these costs while maintaining access performance.

## Capability intent

- Assets are stored in the most cost-effective tier based on measured access patterns.
- Edge caching reduces origin requests and data transfer volume.
- Just-in-time packaging removes the need for pre-packaged format variants for content that doesn't justify them.
- Lifecycle policies vary by content type rather than applying a single retention rule uniformly.

## Common issues to watch for

- A single storage class for all assets regardless of access frequency.
- Serving all requests from origin without edge caching.
- Pre-packaging every format variant for content that is rarely watched.
- Uniform retention policies that keep low-value assets as long as high-value ones.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smcost01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
