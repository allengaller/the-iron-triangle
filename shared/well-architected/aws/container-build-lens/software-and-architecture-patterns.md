<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/software-and-architecture-patterns.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Software and architecture patterns

When designing containerized application, you should keep your
 build manifests up-to-date and aligned with your application
 needs. A containerized application image starts from a
 Dockerfile. The Dockerfile includes all commands required to
 include the configuration and dependencies for the
 containerized application. If there are some dependencies that
 are no longer required, removing them from the Dockerfile can:

- Reduce the time that it takes to build the container
 image. This affects host resource consumption by the build
 process.
- Reduce the container image size and therefore reduce the
 time it takes for this image to be pulled to an instance.
 This affects host resources usage for running and storing
 the container images.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/software-and-architecture-patterns.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
