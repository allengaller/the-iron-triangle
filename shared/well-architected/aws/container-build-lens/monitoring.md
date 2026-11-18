<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/monitoring.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Monitoring

**Implement an automated
 performance testing strategy**

System performance can degrade over time. It’s important to
 have an automated testing and monitoring system in place to
 identify degradation of performance. Every time you build
 target images based on new parent images, you should measure
 the performance impact of the changes in the parent image.
 This also includes the overall build process, because we have
 to make sure that a testing and monitoring system covers the
 CI/CD chain. Performance metrics and image sizes have to be
 collected using services like Amazon CloudWatch and teams must
 be alarmed
 if [anomalies](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
 have been detected.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/monitoring.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
