<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Change management

Changes to your advertising workload or its environment must be anticipated and accommodated to achieve reliable operation of the workload. Changes include those imposed on your workload such as spikes in demand, as well as those from within such as feature deployments and security patches.

Maintain reliability during application and infrastructure
 changes. Implement comprehensive testing (like regression,
 performance, and canary) in CI/CD pipelines to monitor impact on
 critical metrics. Additionally, use phased deployment strategies
 (like blue/green and rolling) to minimize service disruption and
 quickly recover from issues.

###### Best practices

- [ADVREL04-BP01 Through your CI/CD pipeline, employ end-to-end regression, performance, and canary testing](./advrel04-bp01.html)
- [ADVREL04-BP02 Deploy new code or resources in staggered phases, separated by sufficient time, to verify that the changes are successful](./advrel04-bp02.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
