<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/sustainability.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Sustainability

The sustainability pillar includes the ability to continually
 improve sustainability impacts by reducing energy consumption and
 increasing efficiency across all components of a workload by
 maximizing the benefits from the provisioned resources and
 minimizing the total resources required.

The term sustainability encompasses a wide range of factors such as
 economic viability, social equity, biodiversity, resilience, and
 environmental impact. We focus specifically on how to design your
 IoT solutions to improve sustainability by lowering their
 [carbon
 footprint](https://css.umich.edu/publications/factsheets/sustainability-indicators/carbon-footprint-factsheet) while simultaneously reducing operational costs.

Reducing carbon footprint is a key aspect of mitigating climate
 change, which is a pressing global environmental challenge. One way
 to achieve this is to use resources in a responsible and efficient
 manner, minimize waste and maximize the use of renewable
 resources. As described later in this paper, the actions taken to
 improve sustainability usually have a positive effect on operational
 costs, not just through resource efficiency, but also by optimizing
 operational processes.

While IoT solutions span the range from sensors and devices at the
 edge to applications in the cloud, this paper focuses largely on
 sustainability at the edge. Sustainability of and through the cloud
 is covered in the
 [Sustainability
 Pillar of the AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).

It is important to recognize that the carbon footprint of an IoT
 device is distributed across its entire lifecycle, consisting of the
 design and build phase, the operational (in-use) phase, and the
 disposal phase.

- The design and build phase deals with design, component
 sourcing, manufacturing, and other supply chain activities. This
 phase usually accounts for most of the carbon footprint
 associated with a device, often referred to as the
 *embodied carbon*.
- The operational phase of the device lifecycle has a significant
 carbon footprint impact as well. 
 [Reaching
 Net-Zero Carbon by 2040: Decarbonizing and Neutralizing the Use
 Phase of Connected Devices](https://sustainability.aboutamazon.com/devices-use-phase-decarbonization.pdf) shows that this phase accounts
 for 10-15% of the entire lifecycle carbon footprint for
 re-chargeable battery powered devices and 60-80% for plugged-in
 devices.
- The disposal phase of IoT devices refers to the stage when a
 device is no longer needed or usable in operation.

Implementing the best practices outlined here involves trade-offs
 between cost, reliability, performance, carbon footprint, and any
 current or future regulatory requirements. Your organization should
 examine these best practices, both holistically and individually,
 and agree on how to best meet your sustainability goals for each use
 case.

###### Focus areas

- [Design principles](./design-principles-sus.html)
- [Definitions](./definitions-sus.html)
- [Region selection](./region-selection.html)
- [Alignment to demand](./alignment-to-demand.html)
- [Software and architecture optimization](./software-and-architecture-optimization.html)
- [Software and architecture – Cloud](./software-and-architecture-cloud.html)
- [Data management](./data-management-sus.html)
- [Hardware and services - Hardware optimization](./hardware-and-services-optimization.html)
- [Hardware and services - Power management](./hardware-and-services-power-management.html)
- [Process and culture - User guidance](./process-and-culture-user-guidance.html)
- [Key AWS services](./key-aws-services-sus.html)
- [Resources](./resources-sus.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/sustainability.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
