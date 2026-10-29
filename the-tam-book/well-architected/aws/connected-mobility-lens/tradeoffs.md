<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/tradeoffs.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Tradeoffs

**[CMPERF_BP14.1] Develop criteria where trade-offs can be made
 based on the type of functionality.**

For example, infotainment functionality brings higher customer satisfaction where
 certain tradeoffs are acceptable (for example, retry actions are configurable to avoid
 draining battery). But when it comes to vehicle safety critical OTA updates are not
 inhibited by tradeoffs. Additional criteria can be applied:

- Ensure data collection concerning predictive maintenance are not being hindered
- Develop a revision process on actionable insights received from monitoring

**[CMPERF_BP14.2] Architecture design and
 trade-offs**

The following options have benefits which bring scalability, higher performance, faster
 response but the tradeoff is cost. With volume of vehicles that connect to a connected
 vehicle platform increases the cost to maintain them is critical in the long run. In
 addition, the amount of data that gets offloaded from vehicle continues to grow.

- Self-managed option
- AWS Managed Service option
- Serverless option

It is critical to identify and categorize the functions, vehicle signals and states,
 software updates that are needed to support the connected vehicle platform by processing and
 storing them.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/tradeoffs.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
