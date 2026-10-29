<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/foundations.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Foundations

An Amazon WorkSpaces environment can achieve increased resilience
 using the native deployment pattern within the managed services
 that dictates that a minimum of two Availability Zones (AZs) are
 used. Where increased resilience is required at the regional
 rather than zonal level, multi-region Amazon WorkSpaces
 environments can be deployed in separate regions.

For Amazon WorkSpaces Applications, increased resilience can be achieved by
 deploying fleets across a minimum of two AZs and using three AZs
 where possible. Where increased resilience is required at the
 regional rather than zonal level, multi-region Amazon AppStream
 2.0 environments can be deployed in separate regions. This is
 achieved by copying images between regions and establishing
 separate fleets in multiple regions.

###### Best practices

- [EUCREL01-BP01 Add redundancy and remove single points of failure in your environment](./eucrel01-bp01.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/foundations.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
