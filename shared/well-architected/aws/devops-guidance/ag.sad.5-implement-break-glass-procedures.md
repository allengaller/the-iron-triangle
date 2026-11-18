<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.5-implement-break-glass-procedures.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# [AG.SAD.5] Implement break-glass procedures

**Category:** FOUNDATIONAL

Emergencies or unforeseen circumstances might necessitate temporary access beyond
 regular permissions for day-to-day work. Having break-glass procedures helps ensure that
 your organization can respond effectively to crises without compromising long-term
 security. During emergency scenarios, like the failure of the organization's identity
 provider, security incidents, or unavailability of key personnel, these measures provide
 temporary, elevated access beyond regular permissions.

Implement measures that improve the resilience of your DevOps environments through
 the ability to respond effectively to emergencies without compromising long-term security.
 Create break-glass roles and users you can assume control of during emergencies that are
 able to bypass established controls, update guardrails, troubleshoot issues with automation
 tooling, or remediate security and operational issues that may occur. These break-glass
 roles and users should have adequate security measures, such as configuring them with
 hardware-based multi-factor authentication (MFA), to ensure that even in emergencies, access
 is tightly controlled and auditable. Establish alerts and alarms triggered by the use of
 these break-glass roles and users, and tie their usage closely to incident response and
 recovery procedures.

**Related information:**

- [AWS Well-Architected Security Pillar: SEC03-BP03 Establish
 emergency access process](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_emergency_process.html)
- [Break
 glass access](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/break-glass-access.html)
- [Amazon's
 approach to high-availability deployment: Dealing with the
 real world](https://youtu.be/bCgD2bX1LI4?t=1300)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.5-implement-break-glass-procedures.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
