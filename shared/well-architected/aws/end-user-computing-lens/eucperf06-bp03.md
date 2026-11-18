<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCPERF06-BP03 Make sure that EUC network configurations don't interfere with service management connections

WorkSpaces Applications instances use a dedicated management network interface (eth0) for
 streaming and service management connections.

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Do not configure applications or the operating system to interfere with the
 connections listed in [Amazon WorkSpaces Applications Connections to Your VPC](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream2-port-requirements-appstream2.html#management_ports). If private network connectivity
 from WorkSpaces Applications instances to resources outside your VPC is required, use a VPC-level
 solution such as AWS Site-to-Site VPN or AWS Transit Gateway. Do not use a client VPN on the WorkSpaces Applications
 instance, as this is complex and error-prone to configure properly.

WorkSpaces instances use a dedicated management network interface (eth0) for streaming and
 service management connections.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
