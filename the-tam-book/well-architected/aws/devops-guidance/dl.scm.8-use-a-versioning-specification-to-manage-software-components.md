<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.8-use-a-versioning-specification-to-manage-software-components.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# [DL.SCM.8] Use a versioning specification to manage software components

**Category:** RECOMMENDED

Apply a versioning specification across all software
 components within your development lifecycle. Use a versioning
 specification, such as Semantic Versioning (SemVer), to
 significantly simplify governance of software governance by
 providing a systematic approach to tracking different types of
 releases (major, minor, and patch). A well-organized,
 versioned code base offers a clear chronological history of
 modifications, enhancing manageability, maintainability, and
 navigability.

Implementing version pinning for dependencies is a practical use case enabled by
 using a versioning specification. By locking dependencies to a specific version or version
 range, build reproducibility is ensured. This approach helps ensure the reproducibility of
 software builds, but complicates dependency management as developers then need to make
 updates to stay up-to-date with security fixes, bug fixes, or other improvements.

Use automated governance dependency management tools to maintain the balance between
 stable builds and timely updates. Consider integrating automation mechanisms that can
 update versions based on commit messages. For example, if a commit message contains the
 keyword `major`, it could trigger an update to the major version number. This
 automated approach ensures that versions are updated while minimizing chance for human
 error. It's also possible to automate nightly or weekly upgrades of third-party
 dependencies to ensure they are regularly updated and kept secure.

**Related information:**

- [Semantic Versioning
 2.0.0](https://semver.org/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.8-use-a-versioning-specification-to-manage-software-components.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
