<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/migrate-rel.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Migrate

The migrate phase is where the actual migration of the workload
 takes place. In this phase, we perform migration as planned,
 monitor the migration process, and keep a plan in place to
 rollback in case issues encountered during the migration.

Test to validate that your workload meets functional and non-functional requirements before and after migration cutover. It is important to validate and update existing reliability components, which may be different in the new cloud environment.

## MIG-REL-BP-8.1 Before the cut-over, test HA and FT for the migrated workloads, and perform a DR dry-run after the migration

This BP applies to the following best practice areas: Failure
 management

### Implementation guidance

**Suggestion 8.1.1:** Follow the best practices (BPs) in the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html?) to complete the failure management testing for the migrated workloads.

This includes using playbooks to investigate failures, performing post-incident analysis, testing functional requirements for the migrated applications, testing scaling and performance, and testing resilience using chaos engineering.

For more detail, see [How
 do you test reliability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-12.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/migrate-rel.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
