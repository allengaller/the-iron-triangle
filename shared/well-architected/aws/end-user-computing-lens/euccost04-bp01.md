<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost04-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCCOST04-BP01 Tag your Amazon WorkSpaces and Amazon WorkSpaces Applications resources

[Tagging your Amazon WorkSpaces Applications resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html) or [tagging WorkSpaces
 resources](https://docs.aws.amazon.com/workspaces/latest/adminguide/tag-workspaces-resources.html) helps you allocate your cost to logical groups, such as departments or
 business entities.

**Level of risk exposed if this best
 practice is not established:** Low

## Implementation guidance

Plan your tagging strategy before you start deploying your EUC resources. You may
 think of tagging EUC resources with information such as cost center, department,
 usernames, projects, location, or deployment types (like development, test, and
 production). The more dimensions you add with your tags, the easier it will be to report
 and break down the cost once you are in production.

If you already use tagging in your organization, implement a standardized approach
 for tagging that aligns with the approach being used by the rest of the organization,
 which results in a standardized format for the key value pairs being used for tags in the
 organization. Using [Service control
 policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) with AWS Organizations enforces tags to restrict resource creation
 unless they are correctly tagged.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost04-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
