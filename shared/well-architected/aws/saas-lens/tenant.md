<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Tenant

A tenant is the most fundamental construct of a SaaS environment. As a SaaS provider
 building an application, you are making this application available to your customers. Any
 customer that you sign up to use your SaaS environment is one of the tenants of your system.
 The sum total of all the customers using your SaaS environment are the tenants. Imagine, for
 example, that your organization has created an accounting service that you want to make
 available to other companies that will use your service to manage their businesses. Each one
 of these companies would be viewed as a tenant of your system.

Upon signing up, a tenant will typically provide user information
 for the tenant administrator. This tenant administrator can then
 log into the system and configure it based on the needs of their
 business. This includes having the ability to add users to a given
 tenant environment.

The software that is provided in this model is referred to as a
 multi-tenant SaaS system because each of the tenants of the
 service are consuming a single, shared system that supports the
 needs of these tenants through a unified experience. An update to
 the system, for example, would typically be applied to all tenants
 of that system.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
