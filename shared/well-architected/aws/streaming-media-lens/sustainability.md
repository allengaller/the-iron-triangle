<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/sustainability.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Sustainability

The sustainability pillar provides design principles, operational guidance, and best practices to reduce the environmental impact of your streaming media workloads on AWS. Streaming media is resource-intensive by nature. Encoding, storage, and delivery consume compute, network, and storage at scale. The practices in this pillar help you align that consumption with the work actually being done, so resources track demand rather than sitting idle or over-provisioned.

You can find prescriptive guidance on implementation in the [Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) whitepaper.

**Capabilities**

- [Region selection](smsus01.html)
- [Alignment to demand](smsus02.html)
- [Encoding and delivery](smsus03.html)
- [Live streaming efficiency](smsus04.html)
- [Storage and lifecycle](smsus05.html)
- [Movement and caching](smsus06.html)
- [Efficient hardware](smsus07.html)
- [Managed services](smsus08.html)
- [Development and deployment](smsus09.html)
- [Measurement and optimization](smsus10.html)

## Design principles

- **Optimize content processing efficiency:** Match processing intensity to content value and viewer needs rather than applying uniform profiles.
- **Maximize resource utilization:** Use dynamic scaling and workload scheduling to align computing resources with viewer demand patterns.
- **Implement sustainable storage practices:** Apply lifecycle management to optimize content storage based on access patterns and business value.
- **Design for regional efficiency:** Balance viewer experience requirements with regional carbon intensity when placing infrastructure.
- **Adopt energy-efficient technologies:** Use purpose-built media processing hardware and managed services over general-purpose compute where they fit.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/sustainability.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
