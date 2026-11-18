<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-9-2.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best Practice 9.2 – Perform periodic tests for security bugs

As described in the Well-Architected Framework Security Pillar incident response
 sections on simulations, assembling a runbook and conducting game days are recommended for all
 workloads, including those for SAP on AWS. This type of periodic testing can identify
 new attack vectors and vulnerabilities as well as prepare your SAP security resources for
 a rapid and effective response in the event of a security incident.

Well-Architected Framework [Security]: [Incident Response – Simulation](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/simulate.html)

**Suggestion 9.2.1 – Include SAP applications as targets in addition
 to standard security and penetration testing**

Probative security testing is an important part of maintaining a secure environment.
 In addition to conducting standard penetration testing in AWS, make sure to include your
 SAP solution as an additional potential target for malicious activities. Keep in mind
 SAP-specific software solutions that often are publicly exposed in your architecture such
 as SAProuter, Web Dispatcher, Cloud Connector, and SAP Fiori.

- AWS Documentation: [Penetration
 Testing](https://aws.amazon.com/security/penetration-testing/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-9-2.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
