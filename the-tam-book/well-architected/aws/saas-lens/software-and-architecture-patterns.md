<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/software-and-architecture-patterns.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Software and architecture patterns

- **Best Practice–01:** Have a good understanding of the key
 value and principles behind the silo, pool, and bridge models, including awareness how silo 
 and pool strategies can be applied more granularly across the layers and services of your solution.
- **Best Practice–02:** Understand the operational tradeoffs
 of each model. Build a unified onboarding, operations, and analytics experience spanning
 any of these models.
- **Best Practice–03:** Have a complete end-to-end automated
 tenant onboarding process that maps the tenancy models to the resources that are
 provisioned at each architecture layer or component. Also have detailed insights into
 the footprint and consumption costs and tradeoffs associated with each of these models

SaaS applications can be built using a variety of different architectural models.
 Regulatory, competitive, strategic, cost efficiency, and market considerations all influence
 the shape of your SaaS architecture. At the same time, there are strategies and patterns
 that can be applied when defining the footprint of the components within a SaaS application.
 These patterns—silo, bridge, and pool—can be applied in combinations to enable the most
 efficient consumption of infrastructure resources.

**AWS services recommendation:**

- AWS WA SaaS Lens guidance on [Architectural
 model](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-pool-and-bridge-models.html)
- [SaaS Tenant Isolation Strategies whitepaper](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html)
- Amazon EKS SaaS reference solution [https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/amazon-eks-saas.html](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/amazon-eks-saas.html)
- Serverless SaaS reference solution [https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/serverless-saas.html](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/serverless-saas.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/software-and-architecture-patterns.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
