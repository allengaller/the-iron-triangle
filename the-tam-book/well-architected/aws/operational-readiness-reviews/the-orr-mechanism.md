<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/the-orr-mechanism.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# The ORR mechanism

To build a mechanism, work backwards from the challenge you want to solve. The ORR was
 designed by AWS to help prevent the reoccurrence of known, common causes of impact in services
 without slowing builders down. The design and operations of those services are the inputs. The
 outputs are what you want to achieve by resolving the business challenge. In our case at AWS,
 the desired business result was higher levels of availability and resilience in our systems by
 decreasing the frequency of incidents (*fewer*), decreasing the
 duration of incidents (*shorter*), and decreasing the scope of
 impact of an incident (*smaller*). You can start with the same
 business challenge and results when you create your own ORR mechanism.

The following sections examine each component of the mechanism. Each section describes the
 AWS approach and provides recommendations for that part of the mechanism. After you have
 defined your business challenge, use these sections as a guide for building the tool, driving
 adoption, inspecting the process, and iterating.

###### Topics

- [The ORR tool](./the-orr-tool.html)
- [Gaining adoption](./gaining-adoption.html)
- [Inspect the process](./inspect-the-process.html)
- [Iteration](./iteration.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/the-orr-mechanism.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
