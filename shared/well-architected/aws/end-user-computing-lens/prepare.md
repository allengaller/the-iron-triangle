<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/prepare.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Prepare

To prepare for operational excellence, you must understand your workloads and their
 expected behaviors. You can then design them to provide insight to their status and build the
 procedures to support them.

Deciding on the tools you use to provide insight and observability into your AWS EUC
 deployment is key to maintaining acceptable levels of performance and availability. Using
 well-known, incumbent tools while cloud alternatives are reviewed and deployed should be a
 part of your design and deployment process.

While training is essential to verify competency across all aspects of AWS EUC service
 delivery, you should also provide a discrete training environment that won't impact production
 services.

Create and agree upon specific processes to write and continually update service
 documentation as your AWS EUC services evolve over time.

Closely control both direct changes to the AWS EUC service itself and indirect changes
 that affect dependent infrastructure. Formally review any activities that mightaffect the
 performance, availability, or cost structure usinga cross-disciplinary panel of experts and
 test all changes before they are deployed into production.

Each workload, desktop, or application service delivered on your AWS EUC system will
 have a specific architecture, a cadence for updates and patching, metrics for performance
 monitoring, and availability and resilience requirements. Train and provide appropriate
 permissions to a dedicated team with deep insight into delivering each workload to verify that
 each is delivered successfully, promoting user satisfaction and engagement.

While operational training is essential to provide the skills to build and maintain each
 service, user training is equally important to promote employee engagement and to reduce
 support calls. Project success or failure can pivot upon successful adoption of the services
 provided, and successful business outcomes can only be realized if the service users can
 efficiently use its capabilities.

###### Best practices

- [EUCOPS05-BP01 Identify monitoring tools to provide the expected levels of insight into operational performance](./eucops05-bp01.html)
- [EUCOPS05-BP02 Store and regularly analyze log files to detect anomalous activity and behaviors](./eucops05-bp02.html)
- [EUCOPS06-BP01 Deploy test, development, and pre-production environments to reduce risk to production services](./eucops06-bp01.html)
- [EUCOPS07-BP01 Formalize the mandatory creation and maintenance of all EUC service-related documentation](./eucops07-bp01.html)
- [EUCOPS08-BP01 Adopt a mandatory and formalized process for managing any changes to EUC services and dependent infrastructure](./eucops08-bp01.html)
- [EUCOPS09-BP01 Maintain an up to date matrix of all EUC service owners and quick access links to the support plans for each service](./eucops09-bp01.html)
- [EUCOPS09-BP02 Allocate training time so your teams can build and maintain their skills to deploy and manage your AWS EUC environment](./eucops09-bp02.html)
- [EUCOPS10-BP01 Encourage user participation during service development and rollout to maximize engagement and project success](./eucops10-bp01.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/prepare.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
