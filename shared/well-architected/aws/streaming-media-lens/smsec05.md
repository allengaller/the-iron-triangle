<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsec05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Infrastructure protection

Content origins need protection from DDoS attacks at both network and application layers, unauthorized direct access bypassing the CDN, and application-level exploits.

## Capability intent

- Origins are shielded behind CDN and DDoS protection.
- Direct access to origins is blocked for all external traffic.
- Application-layer attacks are filtered by AWS WAF rules tuned to streaming patterns.
- Traffic anomalies trigger alerts and automated response.

## Common issues to watch for

- Origins exposed without DDoS protection or CDN in front.
- Security groups allowing all sources rather than restricting to CDN IPs.
- AWS WAF deployed in count-only mode indefinitely without moving to block.
- No streaming-specific AWS WAF rules (rate limiting on manifest requests, bot detection).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsec05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
