<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops02-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# GAMEOPS02-BP02 Organize infrastructure resources using resource tagging

To effectively manage and track your
 [infrastructure
 resources](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-laying-the-foundation/tagging.html) in AWS, use proper
 [resource
 tagging](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) and
 [grouping](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html)
 to identify each resource's owner, project, application, cost
 center, and other data. Tagged resources can be grouped together
 using [resource
 groups](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html), which assists with operational support.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

Define [tagging
 policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html). Typical strategies include resource tags for
 identifying the resource owner, such as team name or individual
 name, the name of the game, application, or project, the studio
 name, environment (like development or production), and the role
 of the resource (such as database server, web server, dedicated
 game server, app server, or cache server). You can add other tags
 to assist with business and IT
 needs. [AWS Config](https://aws.amazon.com/config/) can also enforce a
 [tagging
 policy](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) at resource creation and update time. Tags and
 resource groups are available from the AWS Management Console, the
 AWS CLI, and API operations.

### Implementation steps

- Tag resources to identify their owner, project, app, cost
 center, and other relevant data.
- Implement tagging policies including tags for owner,
 project, studio, environment, and resource role.
- Use AWS Config to enforce tagging policies, and manage tags
 through AWS Management Console, CLI, and API.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops02-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
