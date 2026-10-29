<!-- source: https://docs.cloud.google.com/architecture/framework/reliability/set-targets -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Set realistic targets for reliability

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](/architecture/framework) 
helps you define reliability goals that are technically feasible for your
workloads in Google Cloud.

This principle is relevant to the *scoping*
[focus area](/architecture/framework/reliability#focus-areas) 
of reliability.

## Principle overview

Design your systems to be just reliable enough for user happiness. It might
seem counterintuitive, but a goal of 100% reliability is often not the most
effective strategy. Higher reliability might result in a significantly higher
cost, both in terms of financial investment and potential limitations on
innovation. If users are already happy with the current level of service, then
efforts to further increase happiness might yield a low return on investment.
Instead, you can better spend resources elsewhere.

You need to determine the level of reliability at which your users are happy,
and determine the point where the cost of incremental improvements begin to
outweigh the benefits. When you determine this level of *sufficient
reliability*, you can allocate resources strategically and focus on features and
improvements that deliver greater value to your users.

## Recommendations

To set realistic reliability targets, consider the recommendations in the
following subsections.

### Accept some failure and prioritize components

Aim for high availability such as 99.99% uptime, but don't set a target of 100%
uptime. Acknowledge that some failures are inevitable.

The gap between 100% uptime and a 99.99% target is the allowance for failure.
This gap is often called the *error budget*. The error budget can help you take
risks and innovate, which is fundamental to any business to stay competitive.

Prioritize the reliability of the most critical components in the system.
Accept that less critical components can have a higher tolerance for failure.

### Balance reliability and cost

To determine the optimal reliability level for your system, conduct thorough
cost-benefit analyses.

Consider factors like system requirements, the consequences of failures, and
your organization's risk tolerance for the specific application. Remember to
consider your
[disaster recovery metrics](/architecture/dr-scenarios-planning-guide#basics_of_dr_planning),
such as the recovery time objective (RTO) and recovery point objective (RPO).
Decide what level of reliability is acceptable within the budget and other
constraints.

Look for ways to improve efficiency and reduce costs without compromising
essential reliability features.

---

> 原页面：https://docs.cloud.google.com/architecture/framework/reliability/set-targets（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
