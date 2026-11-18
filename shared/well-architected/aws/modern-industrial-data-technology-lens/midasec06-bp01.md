<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec06-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC06-BP01 Use secure data exchange protocols

Use secure and standardized protocols for sharing industrial data internally and
 externally, helping protect integrity and confidentiality.

**Desired outcome:** Data is transmitted securely across
 different systems and organizations without unauthorized interception or tampering.

**Benefits of establishing this best practice:** Helps prevent
 data breaches, supports secure collaboration, and aligns with industry data exchange
 standards.

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Use MQTT over TLS, HTTPS, or OPC-UA with encryption and certificate-based
 authentication.

### Implementation steps

- Configure IoT and gateway devices to communicate over secure protocols.
- Enforce TLS 1.2 or higher for all data-in-transit.
- Implement endpoint authentication using certificates or tokens.
- Monitor traffic for anomalies using AWS IoT Device Defender.

## Resources

- [AWS IoT Core protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html)
- [What is AWS IoT Device Defender?](https://docs.aws.amazon.com/iot-device-defender/latest/ug/what-is.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec06-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
