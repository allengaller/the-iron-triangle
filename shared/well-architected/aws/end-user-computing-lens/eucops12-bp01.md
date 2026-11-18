<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops12-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCOPS12-BP01 Deploy alerting mechanisms that quickly identify anomalous metrics

AWS EUC services provide access to desktops and applications which can be highly
 variable in their resource requirements over time. Weekly, monthly, quarterly, and year-end
 activities can cause spikes in resource consumption that might result in unnecessary alerts
 and a degraded user experience.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

The design and pilot phases of an AWS EUC project should identify resource
 requirements for each application set over a typical business cycle. Identify the peak
 activity levels to verify that the compute instance types selected for both Amazon WorkSpaces and
 WorkSpaces Applications can deliver performance that maintains a good user experience and improves
 productivity.

Third party tools from vendors such as ControlUp, Nuvens, LiquidWare, Lakeside
 Software, and Aternity can be used to collect resource usage trends and build baselines
 for key applications. Some of these can be found on the AWS Marketplace.

AWS and the AWS Partner Network offer many services and automation capabilities you can use
 to automatically and elastically scale backend application services or to provide
 increased compute capabilities during periods of heavy utilization**.**

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops12-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
