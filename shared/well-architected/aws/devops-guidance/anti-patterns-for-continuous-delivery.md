<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/anti-patterns-for-continuous-delivery.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Anti-patterns for continuous delivery

- **Large batch
 deployments**: Batching multiple changes into a
 single, large release can lead to increased risk and
 longer lead times. Deploying in smaller batches allows for
 faster feedback and quicker resolution of issues,
 ultimately leading to a more efficient and reliable
 delivery process.
- **Manual deployments**: Deployments done manually lack
 consistency, increase the chances of human error, and hinder the pace of delivering
 software changes. This practice contradicts the fundamental premise of continuous
 delivery and continuous deployment which emphasizes on automation to ensure reliability
 and speed.
- **Building more than once**: Not adhering to the
 *build once, deploy many* principle during deployments. When code
 is built multiple times, there's a chance that inconsistencies due to different
 environments having different configurations, component versions, or updates. This can
 lead to deployment errors, causing failures in production that weren't encountered in
 pre-production environments. To ensure consistency, build the artifact once, and always
 deploy artifacts directly from trusted artifact repositories.
- **Tightly coupled systems**: Developing and deploying in a
 tightly coupled architectural environment can lead to numerous continuous delivery
 challenges. In tightly coupled systems, a change in one component often necessitates
 changes in others, leading to cascading updates and increased complexity in managing
 deployments. This makes isolation of changes for testing purposes difficult, leading to
 longer lead times and an increased likelihood of bugs being introduced. This also makes
 the system less resilient, as failures can easily propagate through the system. Instead,
 architect loosely coupled systems that use modular components or microservices. This
 allows for systems to be updated and deployed independently of each other, reducing
 complexity and risk.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/anti-patterns-for-continuous-delivery.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
