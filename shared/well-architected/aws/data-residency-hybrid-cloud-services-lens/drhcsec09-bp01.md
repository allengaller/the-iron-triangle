<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsec09-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCSEC09-BP01 Train and test incident responders on policies specific to data residency

Train and test incident responders on regulations on storage
 location based on data
 classification.

**Desired outcome:** Incident
 responders have passed tests of their ability to respond to data
 being stored in noncompliant locations.

**Common anti-patterns:**

- Playbooks not being tested by people responsible for using
 them

**Benefits of establishing this best
 practice:** You can prepare for a data residency incident
 by having incident management and investigation policy and
 processes that align to your data residency requirements.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

- Update your incident response playbooks with the impact of
 policies specific to data residency, such as authorized and
 unauthorized locations for data.
- Update expected incidents and known security findings or
 alerts with the findings for each data residency-related
 detective control.
- For each preventative control, create at least one test hat
 proves that the attempted action is denied.
- For each detective control, create at least one test,
 perform the test, then assess if the detection occurred and
 was visible where expected for responders.
- If you use Outposts or Local Zones and have policies that
 prohibit data from being stored within Region locations,
 create a test for each service you use in the workload, and
 configure iterations of the test for all Regions that aren't
 covered by the organization-wide Region deny SCP.
- Evaluate
 [AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html) to determine if it's an
 appropriate option for your organization.

## Resources

**Related best practices:**

- [SEC10-BP03
 Prepare forensic capabilities](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_prepare_forensic.html)
- [SEC11-BP01
 Train for application security](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_train_for_application_security.html)
- [SEC10-BP04
 Develop and test security incident response
 playbooks](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_playbooks.html)

**Related documentation:**

- [Application
 security](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/application-security.html)

**Related videos:**

- [re:Invent
 2024 SEC360: Respond and recovery faster with AWS Security
 Incident Response](https://www.youtube.com/watch?v=5Bx7f_e4dDM)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsec09-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
