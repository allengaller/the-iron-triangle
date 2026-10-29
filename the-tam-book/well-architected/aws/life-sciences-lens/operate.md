<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/operate.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Operate

Life sciences projects often require different groups to work together but maintain clear
 boundaries between resources. Building an auditable environment makes the separation
 manageable. Data isolation is a valuable tool for GxP systems to maintain data integrity,
 improve data security, and adhere to regulatory requirements.

Maintaining audit readiness in life sciences projects is crucial because it blocks costly
 regulatory violations and potential product recalls that could harm both patients and the
 company's reputation. Strong audit preparation assists you in adhering to regulations, enables
 faster responses to agency inquiries, and demonstrates the organization's commitment to
 product quality and safety standards.

Part of being audit ready is being able to identify the source and destination of project
 datasets. As data changes over time, being able to track those changes is critical to attain
 valid and auditable results at the conclusion of a project.

Collect data in a manner that can later be converted or exported for archival. Verify
 your infrastructure is reproducible in case of re-engagement requirements.

When collaborating with other institutions, be clear about data ownership and management.
 Keep a clear log of data lineage and history of access. Implement a clean room technology that
 limits data sharing to only assigned individuals. The technology should have a complete
 auditing history to see how the data has moved, changed and who has accessed it.

A controlled semantic layer gives everyone working on life sciences projects the same
 vocabulary and way to organize data, making sure everything matches up correctly. This shared
 language assists teams work together better and makes it easier to combine and analyze
 different types of research data.

###### Best practices

- [LSOPS07-BP01 Maintain a controlled multi-account environment](./lsops07-bp01.html)
- [LSOPS07-BP02 Isolate GxP data from non-GxP data](./lsops07-bp02.html)
- [LSOPS08-BP01 Continuously generate and maintain evidence](./lsops08-bp01.html)
- [LSOPS09-BP01 Track data ownership and lineage over the life of the project](./lsops09-bp01.html)
- [LSOPS10-BP01 Reproducibility](./lsops10-bp01.html)
- [LSOPS10-BP02 Store data in a format that works both for archiving and for active use by retaining related metadata](./lsops10-bp02.html)
- [LSOPS11-BP01 Identify clear dataset owners and access history](./lsops11-bp01.html)
- [LSOPS12-BP01 Create a controlled semantic layer](./lsops12-bp01.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/operate.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
