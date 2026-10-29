<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/design-principles.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Design principles

In the cloud, there are several principles that can help you create and run streaming
 media workloads. Keep these in mind as we discuss best practices:

- **Keep a glass-to-glass perspective:** From camera to
 viewer device, consider how changes impact the critical path of media delivery.
 Identify key health and diagnostic metrics for video, audio, captions, and metadata
 that affect Quality of Experience (QoE).
- **Scale delivery:** Media streaming can generate high
 traffic volumes with stringent requirements for Quality of Service (QoS). To handle
 demand effectively, use content in adaptive bitrates (ABR) with content delivery
 networks (CDNs) for appropriate caching and auto scaling. Verify that static content
 is cached with appropriate time-to-live (TTL) values and load test dynamic content
 well above expected audience capacity.
- **Understand content value:** Establish a shared
 understanding among stakeholders regarding content value and legal obligations,
 weighing these against costs, performance, and latency considerations. Content
 protection may require implementation of Digital Rights Management (DRM) and
 media-specific tokenization.
- **Design for failure:** Define complete reliability
 objectives across workflows based on risks to viewer experience. Architect systems
 to gracefully handle one or more component failure or degradation through primary,
 backup, and disaster recovery modes. Test failure scenarios extensively with
 operational playbooks and verify that operations teams have complete workflow
 visibility.
- **Enable monetization:** Use Server-Side Ad Insertion
 (SSAI) or Server-Guided Ad Insertion (SGAI) for personalized video advertising to
 maximize revenue while maintaining uninterrupted playback.
- **Know your audience:** Build deep audience
 understanding to inform business and technical decisions. Use analytics to identify
 network conditions, devices, and displays your audience uses. Optimize for their
 consumption habits and prioritize playback testing. Analyze interaction data to
 engage audiences through recommendations, personalization, and notifications. Use
 viewership data and usage forecasts to validate workflow component performance at
 peak scale.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/design-principles.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
