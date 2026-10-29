<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsec01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Identity and access management

Authentication and authorization systems control who can access content and how. This covers viewer-facing identity (subscription tiers, geo-restrictions) and infrastructure-level access (origin restrictions, CDN authentication).

## Capability intent

- Only authenticated and authorized users access protected content based on subscription, licensing, and geography.
- Content origins are accessible only through authorized distribution paths.
- Access tokens are short-lived and scoped to the session.
- Identity is federated from a central provider rather than managed per-application.

## Common issues to watch for

- Relying on obscured URLs instead of identity verification.
- Excessively long signed URL expiration that outlives the session.
- No Origin Access Control between CDN and origin, leaving origins directly accessible.
- Single shared API keys across all sessions rather than per-session tokens.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsec01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
