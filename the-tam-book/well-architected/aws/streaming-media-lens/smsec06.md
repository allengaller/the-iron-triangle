<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsec06.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Data protection

High-value content requires protection through Digital Rights Management (DRM) and encryption. The protection scheme must balance security requirements with device coverage and operational complexity.

## Capability intent

- Content protection requirements are defined collaboratively with business and legal stakeholders.
- The protection scheme meets licensing obligations across all target devices.
- Architecture supports multiple DRM systems where device coverage requires it.
- Protection decisions are revisited as content agreements and supported devices change.

## Common issues to watch for

- DRM implemented without consulting legal on contractual requirements.
- Single DRM chosen based on familiarity rather than device coverage analysis.
- Keys stored alongside content rather than in a separate key management service.
- Protection requirements never revisited as licensing agreements change.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smsec06.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
