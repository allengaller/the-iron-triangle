<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smops03-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# SMOPS03-BP03 Establish war room and incident readiness procedures for high-profile events

During large-scale streaming events, establish dedicated war room and incident readiness procedures that coordinate response and drive rapid resolution of any issues. This approach enables structured decision-making and clear communication during critical streaming periods.

**Desired outcome:**

- Rapid, coordinated resolution of issues during high-profile events through structured war room procedures, clear escalation paths, and pre-approved response actions.

**Benefits of establishing this best practice:**

- Coordinated incident response across cross-functional teams
- Improved communication during critical events
- Reduced impact of operational issues on viewers
- Faster decision-making through pre-approved remediation actions

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

Effective war room operations for high-profile streaming events require preparation across staffing, communication, and rapid response procedures.

War room staffing involves assembling cross-functional teams covering all workflow components, including representatives from content delivery network (CDN) and third-party providers, with clear roles and responsibilities and global coverage for international events. Having the right expertise available during the event window reduces response time and improves decision quality.

Communication procedures establish dedicated communication channels, define escalation paths and decision authorities, implement regular status updates, and create viewer-facing communication templates. Clear communication avoids confusion and keeps all stakeholders informed during high-pressure situations.

Rapid response procedures include preparing specialized runbooks for event-specific scenarios, implementing fast-track approval processes for emergency changes, creating pre-approved remediation actions, and establishing clear incident prioritization guidelines. Pre-approved actions enable teams to respond immediately without waiting for approval chains during time-critical incidents.

### Implementation steps

1. **Define war room team composition:** Define war room team composition and schedules that provide coverage for the entire event window including pre-event and post-event periods.
2. **Establish communication protocols:** Establish communication protocols and channels for internal coordination, external provider communication, and viewer-facing updates.
3. **Prepare event-specific runbooks and:** Prepare event-specific runbooks and procedures that address the most likely failure scenarios for the event type.
4. **Conduct war room simulation exercises:** Conduct war room simulation exercises to validate procedures and build team familiarity with the response process.
5. **Set up war room infrastructure:** Set up physical or virtual war room infrastructure with the necessary tools, dashboards, and communication systems.
6. **Create post-event analysis templates:** Create post-event analysis templates to capture lessons and improvement opportunities systematically.
7. **Document lessons learned process:** Document the lessons learned process so that insights from each event improve future preparations.

## Resources

**Related documents**

- [AWS Incident Detection and Response](https://aws.amazon.com/premiumsupport/business-support-idr)
- [AWS Systems Manager Incident Manager](https://aws.amazon.com/systems-manager/features/incident-manager/)

**Related services**

- [AWS Systems Manager Incident Manager](https://aws.amazon.com/systems-manager/features/incident-manager/)
- [Amazon Connect](https://aws.amazon.com/connect/)
- [AWS Q Developer in Chat Applications](https://aws.amazon.com/q/developer/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/smops03-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
