<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel04-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVREL04-BP02 Deploy new code or resources in staggered phases, separated by sufficient time, to verify that the changes are successful

Implement gradual, phased deployments to minimize risks and
 service impacts when updating systems.

## Implementation guidance

When deploying new code or resources, it is possible for
 unintended results to occur. Various deployment strategies can
 be used to reduce frequency and service impact.

By making changes through a blue/green deployment methodology,
 you can significantly reduce the impact of any potential issues
 and avoid downtime.

When a blue/green deployment isn't possible, a rolling
 deployment methodology should be used to reduce the number of
 resources being modified simultaneously. With a rolling
 deployment, changes are made in small batches, with a
 pre-determined amount of buffer time between batches. If an
 issue occurs with the deployment, the unchanged resources can
 continue handling traffic, avoiding downtime.

## Key AWS services

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/)

## Resources

- [Blue/Green
 Deployments on AWS](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/welcome.html)
- [Rolling
 deployments](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/rolling-deployments.html)
- [Deployment
 methods](Users/jblatch/Downloads/%E2%80%A2%20https:/docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/deployment-methods.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel04-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
