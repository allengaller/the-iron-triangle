<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/infrastructure-protection.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Infrastructure protection

**[CMSEC_BP13.1] Define a baseline of normal behavior for your vehicle as
 a reference and reject and alert on any request patterns that deviate.**

Implement a solution to create a baseline of metrics for vehicles within your fleet. For
 example, AWS IoT Device Defender can be used for devices which connect to AWS IoT Core. This baseline can help
 in detecting anomalies such as impossible motion speeds, or a vehicle existing in multiple
 locations simultaneously. Through the use of [Security Profiles](https://docs.aws.amazon.com/iot/latest/developerguide/detect-behaviors.html) within IoT
 Core and the enablement of metrics by Device Defender a threshold can be established to
 define this anomalous behavior. These thresholds can be either rule-based or use Machine
 Learning to evaluate how these devices should behave. An alert is generated when the defined
 threshold is crossed which can be used to perform automated mitigation actions you define
 such as updating a policy or certificate and can also send notifications via Amazon Simple Notification Service
 (SNS).

**[CMSEC_BP14.1] Conduct threat modeling using a formal methodology such
 as the MITRE Threat Assessment and Threat Analysis Risk Assessment (TARA) on in-vehicle
 systems.**

**[CMSEC_BP14.2] Conduct tests on ECUs to determine if there are any
 unnecessary configurations such as open ports, default permissions, unnecessary services
 running, or other vulnerabilities.**

**[CMSEC_BP14.3] Develop requirements and processes to address and
 remediate vulnerabilities discovered through testing.**

**CMSEC_BP15.1] Validate all software updates are cryptographically
 signed upon release and verified before installation.**

For devices which use AWS IoT, software updates can be signed using AWS Signer a fully managed code-signing service. AWS Signer uses certificates imported to AWS Certificate Manager to sign software, AWS Identity Access Management (IAM) to assign roles to restrict who can sign and in what Region. All actions within AWS Signer are also captured in AWS CloudTrail for auditing purposes.

**[CMSEC_BP15.2] Test software packages for vulnerabilities and errors
 prior to deployment.**

**[CMSEC_BP15.3] Perform controlled and secure deployment of software
 to vehicle fleets with rollback capabilities in case of failures.**

**[CMSEC_BP16.1] Maintain an accurate and continuously updated
 inventory of vehicles and any versions of software packages or underlying hardware.**

This should include any applicable Software Bill of Material (SBOM) documents as
 outlined by something such as [The Minimum Elements For a Software Bill of Materials (SBOM)](https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf) pursuant to [Executive Order 14028](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) including any [Vulnerability
 Exploitability eXchange (VEX)](https://ntia.gov/files/ntia/publications/vex_one-page_summary.pdf) documents as outlined by the United States
 Department of Energy in coordination with the National Telecommunications and Information
 Administration. A VEX document is an attestation and contains information about a product
 and whether it is affected by a known vulnerability.

**[CMSEC_BP17.1] Use methods for ensuring integrity such as through
 secure boot and software signing methodologies.**

**[CMSEC_BP18.1] Develop SDLC policies which govern these requirements
 and provide prescriptive guidance for implementing required controls.**

**[CMSEC_BP19.1] Continuously monitor informational feeds on threat
 intelligence from vendors, suppliers, third-party intelligence providers, repositories,
 and communities.**

Threat intelligence feeds provide additional insights into signatures of potentially
 malicious activity such as malware, botnets, and phishing. This information helps to
 supplement the tools already in use by security teams to understand the current threat
 landscape at a broader scope. AWS Partners such as Recorded Future and Tenable provide
 threat intelligence feeds and are readily available through the AWS Marketplace. IP based threat
 lists from these providers can also be used to supplement detections within [AWS GuardDuty](https://aws.amazon.com/guardduty/) our purpose-built threat
 detection service. Customers can also leverage an AWS partner like Argus Cyber Security to
 help implement in-vehicle security systems like an Intrusion Detection System for Controller
 Area Networks (CAN), vehicle vulnerability management, and firewall capabilities to protect
 components. Industry specific feeds such as Auto-ISAC can provide additional insights based
 on contributions from organizations within automotive.

**[CMSEC_BP19.2] Conduct vulnerability impact analysis and testing in
 isolated and secure environments.**

When conducting tests of vulnerabilities on systems or investigating potentially compromised
 systems an isolated and secure environment should be used. This verifies that other
 resources are not inadvertently impacted or compromised by these activities. When conducting
 this testing in AWS environments a separate Account should be created to provide
 segmentation from other Accounts and resources. Strong defense-in-depth configurations
 should also be used such as for forensic investigations. Some of these strategies are
 outlined in the [Forensic investigation environment strategies in the AWS Cloud](https://aws.amazon.com/blogs/security/forensic-investigation-environment-strategies-in-the-aws-cloud/) blog post.

**[CMSEC_BP19.3] Define a process for classifying and prioritizing
 vulnerabilities for remediation.**

Processes for classification, prioritization, and remediation of vulnerabilities should be
 formally documented and readily accessible to stakeholders. Playbooks and runbooks specific
 to your organizations technology stack and operational processes should be used as a means
 of automating segments of the investigation and help minimize manual errors during a
 potentially stressful situation. Automation can be accomplished through solutions such as
 Jupyter Notebooks or running automation documents within AWS Systems Manager for example.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/infrastructure-protection.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
