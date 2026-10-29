<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/data-protection.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Data protection

**Do not hardcode sensitive data into your container image**

With respect to handling data in the build and design of the
 container, it is important that no sensitive information is
 stored in the container itself. For example, user credentials
 should never be hardcoded into your container image. Instead,
 consider using a secret management protocol that is compatible
 with the container orchestration system being used to manage
 the container workloads.

**Ensure that persistent data
 is stored outside of the container**

Also, if your containerized application writes or consumes
 persistent data, ensure that data is stored outside of the
 container. Since containers are intended to be ephemeral, use
 volumes to store persistent data that will remain intact long
 after a container’s lifecycle has completed.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/data-protection.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
