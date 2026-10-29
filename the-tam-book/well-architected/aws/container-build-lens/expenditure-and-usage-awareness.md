<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/expenditure-and-usage-awareness.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Expenditure and usage awareness

**Designing efficient
 container build process**

Building containers is a process that consumes compute and
 storage resources and can lead to unnecessary costs if not
 using it properly. The build process consumes resources for
 each build, and there are some considerations that have to be
 taken for it to be efficient from a cost perspective.

**Application
 dependencies**

The container image is usually being built alongside with the application build step. During this build step, all necessary dependencies, libraries, and modules that are being used by the application code are downloaded to the container image.
 Using unnecessary dependencies will make the build time longer, and will result in wasting compute resources of the build system.

**Common container image
 dependencies**

Some operating system packages are needed for multiple applications in the
 organization for a specific runtime (for example, Python and Java). Building a parent
 container image that preinstalls all common operating system packages and dependencies for
 the specific runtime will result in a more efficient build process. Without this common
 image, each individual container image would be installing the same packages, thus wasting
 compute and network resources. This practice will also shorten the time for container
 images built from a specific runtime, since all of its common operating system packages
 and dependencies are already included in the parent container image. As a result, this
 will reduce costs for building all other container images that use this parent image.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/expenditure-and-usage-awareness.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
