<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/design-principles-rel.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Design principles

In addition to the design principles in the AWS Well-Architected
 Framework whitepaper, the following are design principles that can
 increase reliability in the cloud for games workloads:

- **Establish the baseline for the peak
 player concurrency and system scalability targets required to
 meet business projections:** Prior to launching a
 game and during live game operations, develop estimates for
 the number of concurrent players expected at peak to establish
 target goals for system scalability to meet these projections.
 This assists creating a baseline for your game's reliability.
 Define scaling policies to accommodate changes in demand
 automatically without impact availability by verifying that
 your scaling systems gracefully manage active player sessions.
- **Measure your reliability and the
 impact on player experience:** Define key performance
 indicators (KPIs) that represent the health of your game.
 Monitor the impact of changes in infrastructure and game
 features on your reliability.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/design-principles-rel.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
