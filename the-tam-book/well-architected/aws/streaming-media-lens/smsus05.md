<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Storage and lifecycle

Media catalogs grow continuously. Masters, mezzanines, renditions, and archives accumulate, and storage becomes a steadily rising resource cost unless tiering and lifecycle rules tie retention to actual use.

## Capability intent

- Each class of media asset occupies the storage tier its access pattern justifies.
- Expired or regenerable assets are removed automatically rather than retained by default.
- Archives are compressed before moving to cold storage to reduce both stored bytes and retrieval energy.
- Storage growth is visible and reviewed, so waste is caught before it accumulates.

## Common issues to watch for

- The entire catalog on a single hot storage tier regardless of access frequency.
- No lifecycle policies, so drafts, test renditions, and superseded versions accumulate indefinitely.
- Masters kept in standard storage long after deliverable renditions have been produced.
- No storage analytics to surface unused buckets or incomplete uploads.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsus05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
