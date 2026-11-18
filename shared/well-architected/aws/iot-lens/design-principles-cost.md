<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/design-principles-cost.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Design principles

In addition to the overall Well-Architected Framework cost
 optimization design principles, there are three design principle
 for cost optimization for IoT:

- **Manage manufacturing cost
 tradeoffs**: Business partnering criteria, hardware
 component selection, firmware complexity, and distribution
 requirements all play a role in manufacturing cost. Minimizing
 that cost helps determine whether a product can be brought to
 market successfully over multiple product generations.
 However, making inefficient decisions in the selection of your
 components and manufacturer can increase downstream costs. For
 example, partnering with a reputable manufacturer helps
 minimize downstream hardware failure and customer support
 cost. Selecting a dedicated crypto component can increase bill
 of material (BOM) cost, but reduce downstream manufacturing
 and provisioning complexity, since the part may already come
 with an onboard private key and certificate.
- **Avoid unnecessary data access,
 storage, and transmission**: Identify and classify
 data collected throughout your IoT landscape and learn their
 corresponding business use-case. Collect the data that is
 required, applying filtering mechanisms at the edge to
 minimize sending redundant data to the cloud.
- **Process data at the edge whenever
 possible**: Processing data at the edge can help to
 save costs. Process large volumes of data locally, upload only
 relevant insights and high-value data to the cloud.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/design-principles-cost.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
