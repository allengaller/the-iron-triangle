<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# GAMEPERF06-BP01 Centralize log collection and storage

Implement a centralized log collection and storage solution to gather logs from game server
 instances and GameLift.

**Level of risk exposed if this best practice is not established:**
 High

## Implementation guidance

Use services like Amazon CloudWatch Logs to collect, monitor, and store log data from your game
 servers and GameLift instances. CloudWatch Logs provides a scalable and fully managed solution for log
 management, facilitating efficient storage and retrieval of log data without impacting game
 server performance. If you are running the [CloudWatch Logs agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html), consider the
 various install types and configuration options like batch size, buffer duration to minimize
 impact to the game server. Consider the game server instances ephemeral and reduce dependency
 on localized logging where possible. Establish a centralized policy for implementation of
 [Logging best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/logging-best-practices.html).

### Implementation steps

- Use Amazon CloudWatch Logs to collect, monitor, and store log data from game server instances
 and GameLift, facilitating centralized and scalable log management.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
