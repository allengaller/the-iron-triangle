<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/manage-demand-and-supply-resources.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Manage demand and supply resources

Longer startup times for containerized applications can result in wasted compute resources.
 Shortening startup times can be done on the application-level (code optimization), or on the container level. For example, if the application needs external dependencies to be present in the container, it should be already installed during the build process, or it should be included in the parent image, and not downloaded at startup using an entrypoint script or `DOCKERFILE` commands.

Creating any build process requires developing, maintaining, and operating a build system. This can be done by a variety of methods, such as using OSS tooling for job automation, or using self-developed systems that are able to run build scripts for your application. However, running and maintaining this kind of system involves software development costs, operational costs, compute, and storage costs for running the system.
 Alternatively you can use build and pipeline services, such as Amazon EC2 Image Builder, AWS CodeBuild, and AWS CodePipeline. Using managed services removes the operational overhead and allows developers to consume pipeline runs and build jobs on a pay-as-you-go basis.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/manage-demand-and-supply-resources.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
