<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/definition-1.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Definition

There are five best practice areas for security in the cloud:

- Identity and access management
- Detective controls
- Infrastructure protection
- Data protection
- Incident response

Multi-tenancy adds a layer of additional considerations to your
 SaaS architecture. With SaaS, you have users that are now
 accessing a shared environment in the context of a given tenant.
 This context must be captured and conveyed across all the layers
 of your application’s architecture and plays a fundamental role
 in securing the overall footprint of your environment.

From a security perspective, you need to look at how tenancy is
 introduced into your environment and how it is used to secure
 tenant resources. Overall, you need to ensure that each tenant
 has a carefully constrained experience that prevents them from
 accessing any other tenant’s resources.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/definition-1.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
