<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/hardware-patterns.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Hardware patterns

To be able to [use instance types with the least environmental impact](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/use-instance-types-with-the-least-impact.html) (from the Sustainability
 Pillar whitepaper), you have to ensure your containerized application is able to run on a
 variety of instance types and architectures. This can be done by creating images that
 support multi-architecture as described in the [Cost Optimization Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html). For example, you can use a build service
 that supports multi-architecture build servers and combine them to a multi-architecture
 image using the CI pipeline (see Graviton workshop as an [example](https://graviton2-workshop.workshop.aws/en/amazoncontainers.html)
 of using AWS CodeBuild, and AWS CodePipeline alongside Graviton and Amazon EKS). You can also use tools
 that generate multi-architecture images from a single Dockerfile, such as [Docker Buildx.](https://docs.docker.com/desktop/multi-arch/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/hardware-patterns.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
