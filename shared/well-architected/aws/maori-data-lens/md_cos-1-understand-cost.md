<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_cos-1-understand-cost.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MD_CO 1 Understand costs associated with infrastructure options

- **MD_CO01-BP01: How are you presenting the costs/benefit tradeoffs
 for infrastructure options?** Clearly present the cost to benefit trade-offs
 when looking at all infrastructure options. When designing technology solutions,
 organisations need to balance delivering functional and non-functional requirements with
 the cost associated with doing so. It is important that the cost to benefit ratio is
 assessed and understood. The assessment should take into account the strategic drivers for
 the organisation. Within the public sector, for example, value-for-money in terms of
 social, environmental, and public benefits is important. For some Māori customers,
 security, resilience, and sustainability may be key considerations.
An example may be an organisation wanting to store data close to the source for
 latency reasons. An AWS Outpost can help meet those requirements. An AWS Outpost
 is a managed service that extends AWS infrastructure, services, APIs, and tools to
 customer premises. However, there are several considerations when using an AWS
 Outpost. An Outpost has a limited set of AWS services available compared to the 200+
 services available in an AWS Region. This consideration may impact how you design
 your architecture. An AWS Outpost is a physical device that needs to be built,
 shipped, and installed within a datacentre that meets certain physical requirements.
 This can be done with a third-party data centre, but there is a cost associated with
 renting space.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_cos-1-understand-cost.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
