<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/architecture-selection.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Architecture selection

Selecting the most appropriate Regions or Availability Zones to deploy your EUC services
 will be a critical factor to consider to provide the best performance for your end users,
 partners, and customers.

A well-performing AWS EUC architecture will consider the location of the users
 accessing the services and the latency to key service endpoints in each Region. Consider
 the proximity of user data such as home drives, user profile stores, databases, and data
 feeds to the users to design an efficient data flow. For further information related to
 tradeoffs to consider in relation to latency as well as how to determine the latency
 between user locations and the location of AWS EUC services, see [EUC latency
 tradeoffs](https://guide.aws.dev/en/articles/ARiy3h1QGUSWePxGqdV_SYLA) and [How to check latency to the closest AWS Region](https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/how-to-check-latency-to-the-closest-aws-region.html).

A typical EUC deployment uses many backend services which are deployed, managed and
 supported by the business. AWS offers a range of managed services which offer resilience
 and scalability, and which augment the performance of your desktop and application
 delivery tiers.

###### Best practices

- [EUCPERF01-BP01 Check Regional support for the required EUC services](./eucperf01-bp01.html)
- [EUCPERF01-BP02 Consider the requirements of your Availability Zones when architecting your AWS EUC services](./eucperf01-bp02.html)
- [EUCPERF01-BP03 Consider disaster recovery (DR) requirements when architecting your AWS EUC solution](./eucperf01-bp03.html)
- [EUCPERF02-BP01 Identify geographic distribution of end users and design to minimize latency](./eucperf02-bp01.html)
- [EUCPERF02-BP02 Scale your EUC environment to accommodate the required number of end users](./eucperf02-bp02.html)
- [EUCPERF02-BP03 Evaluate external data sources that your environment integrates with, and assess its impact on performance](./eucperf02-bp03.html)
- [EUCPERF03-BP01 Consider modernization of backend services to use managed services from AWS for best performance](./eucperf03-bp01.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/architecture-selection.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
