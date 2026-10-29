<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/practice-cloud-financial-management.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Practice cloud financial management

Building a containerized application can result in multiple
 images for the same service. Depending on your organization
 policy, you might want to keep a subset of your container
 images to be used in a case of a rollback scenario. An example
 of such a policy might be that you don’t roll back more than
 three versions, or more than three months in time. That means,
 that not all container images of a specific application should
 be kept. Deleting old images can save costs as container
 registries charge by size of images stored in the registry.
 You can achieve this deletion policy by creating automation
 processes, or use service features, for example: Amazon ECR
 supports a lifecycle policy that can be used to expire
 (delete) images based on rules such as image age, count,
 specific tags and more
 (see [Examples
 of lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/lifecycle_policy_examples.html)).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/practice-cloud-financial-management.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
