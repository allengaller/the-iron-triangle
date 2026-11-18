<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/deploy-changes-to-production.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Deploy changes to production

Implement tested, validated, and approved improvements to
 production. Implement using limited deployments, confirm the
 functionality of your workload, test the actual reduction in
 provisioned resources and resources consumed per unit of work
 within the limited deployment, and check for unintended
 consequences of the change. Proceed with full deployments after
 successful testing.

Revert changes if tests fail or you encounter unacceptable
 unintended consequences of your change.

Applying this step to the [Example scenario](./improvement-process.html#example-scenario), you take the following actions.

You implement the changes in production using a limited deployment
 through a blue-green deployment methodology. Functionality tests
 against the newly deployed instances are successful. You see a 26%
 average reduction in provisioned storage for original and
 manipulated image files. You don’t see any evidence of an increase
 in compute load compressing new files.

You notice an unanticipated decrease in the elapsed time to
 compress image files, and you attribute this to the highly
 optimized code for the new compression algorithm.

You proceed with full deployment of the new version.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/deploy-changes-to-production.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
