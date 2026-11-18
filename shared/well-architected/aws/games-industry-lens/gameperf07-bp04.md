<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf07-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# GAMEPERF07-BP04 Regularly monitor networking performance

For competitive games, it is important to have a consistent player
 experience.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

A game that is reliably 50ms for a larger player base
 is fairer and more fun than a match where one player has 10ms ping
 and another who has 70ms ping. ISP routing changes may impact part
 of the player population, and your matchmaking system will need to
 adapt.
 [Amazon CloudWatch Network Monitoring](https://aws.amazon.com/cloudwatch/features/network-monitoring/) assists in determining
 whether the issue is with your game or the player internet
 provider.

### Implementation steps

- Use Amazon Cloudwatch Network Monitoring to track network
 performance and identify routing issues.
- Use VPC Flow Logs to identify abnormal traffic patterns or
 dropped packets, which can indicate network congestion, ISP
 issues, or misconfigurations impacting player latency.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf07-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
