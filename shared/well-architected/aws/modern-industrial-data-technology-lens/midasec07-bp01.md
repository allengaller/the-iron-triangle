<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec07-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC07-BP01 Deploy continuous monitoring tools

Implement continuous monitoring of your industrial systems to detect and respond to
 threats in real time. Monitoring should span cloud, edge, and on-premises systems across both
 IT and OT environments.

**Desired outcome:** Security teams can detect anomalies and
 threats early, reducing the impact of potential breaches.

**Benefits of establishing this best practice:** Enables
 real-time visibility, faster incident response, and proactive threat mitigation.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Use AWS monitoring tools such as Amazon CloudWatch, AWS IoT Device Defender, and AWS Config to gather and analyze telemetry.

### Implementation steps

- Enable Amazon CloudWatch metrics and logs for all AWS workloads.
- Deploy AWS IoT Device Defender to monitor device behavior and audit
 configurations.
- Use AWS Config to track configuration changes across resources.
- Integrate alerts with AWS SNS or AWS Security Hub CSPM for real-time response.

## Resources

- [What is AWS IoT Device Defender?](https://docs.aws.amazon.com/iot-device-defender/latest/ug/what-is.html)
- [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/what-is-aws-config.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec07-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
