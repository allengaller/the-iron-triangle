<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/scenarios.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Scenarios

Digital sovereignty encompasses the principles and practices that
 customers use to maintain control over their data, infrastructure,
 and operations within specific jurisdictions. The following
 scenarios represent common situations where digital sovereignty
 requirements apply. Review these scenarios to identify which are
 relevant to your organization or solution.

1. **Design and develop public digital
 infrastructure:** Digital infrastructure serving the
 daily needs of citizens (such as digital payment platforms,
 securities and commodities trading platforms, and healthcare
 systems) must be secure, resilient, and highly available.
 Citizens depend on these systems continuously. Disruption or
 compromise has direct consequences for public safety, economic
 stability, and trust in government services. Design for fault
 isolation, rapid recovery, and defense in depth commensurate
 with that criticality. Apply sovereignty controls that keep
 citizen data within jurisdictional boundaries and restrict
 operator access to authorized personnel.
2. **Set up and operate workloads in new
 jurisdictions:** Expanding into a new jurisdiction
 means entering a distinct regulatory environment. Data residency
 mandates, breach notification timelines, operator access
 restrictions, and continuity obligations differ from one
 jurisdiction to the next. Identify which obligations apply
 before deploying and adapt your architecture accordingly: choose
 Regions, configure controls, and establish jurisdiction scoped
 compliance capabilities.
3. **Protect citizens' data by complying with
 data export controls and privacy legislation:**
 Sovereign nations assert jurisdiction over citizens' data.
 Organizations collecting personal data must classify it by
 sovereignty sensitivity, enforce residency and transfer
 restrictions, and maintain a valid legal basis for any
 cross-border movement. Transferring data without proper legal
 basis exposes the organization to regulatory actions and erodes
 the trust that citizens place in the services they use.
 Demonstrate compliance through verifiable evidence: automated
 controls, continuous monitoring, and audit-ready documentation.
4. **Restrict who can provide operational
 support, to what extent, and from where:** Regulatory
 requirements may restrict who can access data. Determine who
 needs to provide operational support, from where, under what
 authority, and for how long. Enforce least privilege and
 location restrictions, and review access regularly. Uncontrolled
 operator access undermines data sovereignty regardless of how
 well other controls are implemented.
5. **Plan for unexpected
 disruptions:** Sovereignty controls that restrict data
 to a single jurisdiction or limit operator access can conflict
 with disaster recovery patterns that depend on geographic
 distribution or cross-border access. Assess the potential impact
 of reduced access to critical software, physical infrastructure,
 and technical skills, whether caused by trade restrictions,
 licensing changes, geopolitical instability, or natural
 disasters. Select DR site locations, evaluate interoperability
 and portability options, use open standards and open data
 formats where appropriate, and test recovery paths.
6. **Align with policy-led technology
 initiatives:** Some jurisdictions mandate or
 incentivise use of domestically developed technology stacks to
 reduce foreign dependency and stimulate local economic growth.
 Not following such mandates may limit regulatory access or
 public-sector contract eligibility. Track national and regional
 mandates, understand the timelines and implementation
 expectations, and engage with regulators and policy makers to
 anticipate how these decisions will be put into practice.
7. **Implement new technology without
 compromising sovereign controls:** Emerging technology
 (such as generative AI, edge computing, or multi-party
 computation) often introduces new data flows, third-party
 dependencies, or cross-border processing that may conflict with
 existing sovereignty controls. Evaluate new capabilities against
 your sovereignty requirements before adoption. Verify that
 locality, access control, and continuity controls remain intact.
 Organizations that assess before adopting avoid retroactive
 remediation and can enter new regulated jurisdictions with
 confidence.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/scenarios.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
