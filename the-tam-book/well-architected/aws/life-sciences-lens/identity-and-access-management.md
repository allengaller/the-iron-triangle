<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/identity-and-access-management.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Identity and access management

Separation of duties, as it relates to security, has two primary objectives.

The first objective is the avoidance of conflict of interest, abuse, and errors.

The second objective is the detection of control failures that include security breaches,
 information theft, and circumvention of security controls.

Separation of duties is also essential for demonstrating that data integrity has been
 maintained. The FDA, for example, clearly states in its [guidance](https://www.fda.gov/media/119267/download) that the system
 administrator role should only be assigned to personnel who are not responsible for the record
 content. This separation stops an individual whose role has a direct interest in the results
 of the decision from having the ability to modify or delete critical data. This protects the
 integrity of the data and avoids the risk of allegations of tampering.

###### Best practices

- [LSSEC01-BP01 Implement the principle of separation of duties](./lssec01-bp01.html)
- [LSSEC01-BP02 Maintain a history of IAM configurations and changes over time](./lssec01-bp02.html)
- [LSSEC01-BP03 Set up alerts for IAM configuration changes and perform audits](./lssec01-bp03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/identity-and-access-management.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
