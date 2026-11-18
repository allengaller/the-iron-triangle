<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# GAMEPERF06-BP03 Enable efficient log formatting and batching

Configure your game server processes to generate logs in a structured and in a format that
 can be parsed, such as JSON.

**Level of risk exposed if this best practice is not established:**
 High

## Implementation guidance

Implement log batching techniques to minimize the frequency of log data transfers from
 your game servers to the centralized log storage. Batching logs reduces network overhead and
 improves game server performance. Use verbose or debug level logs as an exception and not a
 default, as they can incur a performance and cost penalty that should be avoided when
 possible.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
