<!-- source: https://docs.cloud.google.com/architecture/framework/security -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Well-Architected Framework: Security, privacy, and compliance pillar

The Security, Privacy and Compliance pillar in the
[Google Cloud Well-Architected Framework](/architecture/framework) 
provides recommendations to help you design, deploy, and operate cloud workloads
that meet your requirements for security, privacy, and compliance.

This document is designed to offer valuable insights and meet the needs of a
range of security professionals and engineers. The following table describes
the intended audiences for this document:

| Audience | What this document provides |
| --- | --- |
| Chief information security officers (CISOs), business unit leaders, and IT managers | A general framework to establish and maintain security excellence in the cloud and to ensure a comprehensive view of security areas to make informed decisions about security investments. |
| Security architects and engineers | Key security practices for the design and operational phases to help ensure that solutions are designed for security, efficiency, and scalability. |
| DevSecOps teams | Guidance to incorporate overarching security controls to plan automation that enables secure and reliable infrastructure. |
| Compliance officers and risk managers | Key security recommendations to follow a structured approach to risk management with safeguards that help to meet compliance obligations. |

To ensure that your Google Cloud workloads meet your security, privacy,
and compliance requirements, all of the stakeholders in your organization must
adopt a collaborative approach. In addition, you must recognize that cloud
security is a shared responsibility between you and Google. For more
information, see
[Shared responsibilities and shared fate on Google Cloud](/architecture/framework/security/shared-responsibility-shared-fate).

The recommendations in this pillar are grouped into core security principles.
Each principle-based recommendation is mapped to one or more of the
[focus areas of cloud security](#focus_areas_of_cloud_security) 
that might be critical to your organization. Each
recommendation highlights guidance about the use and configuration of
Google Cloud products and capabilities to help improve your organization's
security posture.

## Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and
recommendations in this pillar, use the
[google-cloud-waf-security](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-security)
skill, which is available in the Google Agent Skills repository in GitHub.

To install the skill, run the following command in your agent's client or
terminal:

```
npx
 
skills
 
add
 
google/skills
 
--skill
 
google-cloud-waf-security
```

When prompted, specify the AI agents for which you want to install the skill and
set the installation scope (project or global).

If you've already installed the skill, you can update it to the latest version
by running the following command:

```
npx
 
skills
 
update
```

## Core principles

The recommendations in this pillar are grouped within the following core
principles of security. Every principle in this pillar is important. Depending
on the requirements of your organization and workload, you might choose to
prioritize certain principles.

- [Implement security by design](/architecture/framework/security/implement-security-by-design):
Integrate cloud security and network security considerations starting from
the initial design phase of your applications and infrastructure.
Google Cloud provides architecture blueprints and recommendations to
help you apply this principle.
- [Implement zero trust](/architecture/framework/security/implement-zero-trust):
Use a *never trust, always verify* approach, where access to resources is
granted based on continuous verification of trust. Google Cloud
supports this principle through products like Chrome Enterprise Premium and
Identity-Aware Proxy (IAP).
- [Implement shift-left security](/architecture/framework/security/implement-shift-left-security):
Implement security controls early in the software development lifecycle.
Avoid security defects before system changes are made. Detect and fix
security bugs early, fast, and reliably after the system changes are
committed. Google Cloud supports this principle through products like
Cloud Build, Binary Authorization, and Artifact Registry.
- [Implement preemptive cyber defense](/architecture/framework/security/implement-preemptive-cyber-defense):
Adopt a proactive approach to security by implementing robust fundamental
measures like threat intelligence. This approach helps you build a
foundation for more effective threat detection and response.
Google Cloud's
[approach to layered security controls](/docs/security/overview/whitepaper#technology_with_security_at_its_core) 
aligns with this principle.
- [Use AI securely and responsibly](/architecture/framework/security/use-ai-securely-and-responsibly):
Develop and deploy AI systems in a responsible and secure manner. The
recommendations for this principle are aligned with guidance in the
[AI and ML perspective](/architecture/framework/perspectives/ai-ml) 
of the Well-Architected Framework and in Google's
[Secure AI Framework (SAIF)](https://saif.google).
- [Use AI for security](/architecture/framework/security/use-ai-for-security):
Use AI capabilities to improve your existing security systems and processes
through
[Gemini in Security](https://cloud.google.com/security/ai) 
and overall platform-security capabilities. Use AI as a tool to increase
the automation of remedial work and ensure security hygiene to make other
systems more secure.
- [Meet regulatory, compliance, and privacy needs](/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs):
Adhere to industry-specific regulations, compliance standards, and privacy
requirements. Google Cloud helps you meet these obligations through
products like Assured Workloads, Organization Policy Service, and our
[compliance resource center](https://cloud.google.com/security/compliance/).

## Organizational security mindset

A security-focused organizational mindset is crucial for successful cloud
adoption and operation. This mindset should be deeply ingrained in your
organization's culture and reflected in its practices, which are guided by core
security principles as described earlier.

An organizational security mindset emphasizes that you think about security
during system design, assume zero trust, and integrate security features
throughout your development process. In this mindset, you also think proactively
about cyber-defense measures, use AI securely and for security, and consider
your regulatory, privacy, and compliance requirements. By embracing these
principles, your organization can cultivate a security-first culture that
proactively addresses threats, protects valuable assets, and helps to ensure
responsible technology usage.

## Focus areas of cloud security

This section describes the areas for you to focus on when you plan,
implement, and manage security for your applications, systems, and data. The
recommendations in each principle of this pillar are relevant to one or more of
these focus areas. Throughout the rest of this document, the recommendations
specify the corresponding security focus areas to provide further clarity and
context.

| **Focus area** | **Activities and components** | **Related Google Cloud products, capabilities, and solutions** |
| --- | --- | --- |
| Infrastructure security | Secure network infrastructure. Encrypt data in transit and at rest. Control traffic flow. Secure IaaS and PaaS services. Protect against unauthorized access. | [Firewall Policies](/firewall/docs/firewall-policies-overview) [VPC Service Controls](/vpc-service-controls/docs/overview) [Google Cloud Armor](/armor/docs/cloud-armor-overview) [Cloud Next Generation Firewall](/firewall/docs/about-firewalls) [Secure Web Proxy](/secure-web-proxy/docs/overview) |
| Identity and access management | Use authentication, authorization, and access controls. Manage cloud identities. Manage identity and access management policies. | [Cloud Identity](/identity/docs/overview) [Google's Identity and Access Management (IAM) service](/iam/docs/overview) [Workforce Identity Federation](/iam/docs/workforce-identity-federation) [Workload Identity Federation](/iam/docs/workload-identity-federation) |
| Data security | Store data in Google Cloud securely. Control access to the data. Discover and classify the data. Design necessary controls, such as encryption, access controls, and data loss prevention. Protect data at rest, in transit, and in use. | [Google's IAM service](/iam/docs/overview) [Sensitive Data Protection](/sensitive-data-protection/docs/sensitive-data-protection-overview) [VPC Service Controls](/vpc-service-controls/docs/overview) [Cloud KMS](/kms/docs/key-management-service) [Confidential Computing](/confidential-computing/docs/confidential-computing-overview) |
| AI and ML security | Apply security controls at different layers of the AI and ML infrastructure and pipeline. Ensure model safety. | [Google's SAIF](https://saif.google/) [Model Armor](/security-command-center/docs/model-armor-overview) |
| Security operations (SecOps) | Adopt a modern SecOps platform and set of practices, for effective incident management, threat detection, and response processes. Monitor systems and applications continuously for security events. | [Google Security Operations](/chronicle/docs/secops/secops-overview) |
| Application security | Secure applications against software vulnerabilities and attacks. | [Artifact Registry](/artifact-registry/docs/overview) [Artifact Analysis](/artifact-analysis/docs/artifact-analysis) [Binary Authorization](/binary-authorization/docs/overview) [Assured Open Source Software](/assured-open-source-software/docs/overview) [Google Cloud Armor](/armor/docs/cloud-armor-overview) [Web Security Scanner](/security-command-center/docs/concepts-web-security-scanner-overview) |
| Cloud governance, risk, and compliance | Establish policies, procedures, and controls to manage cloud resources effectively and securely. | [Organization Policy Service](/resource-manager/docs/organization-policy/overview) [Cloud Asset Inventory](/asset-inventory/docs/asset-inventory-overview) [Security Command Center Enterprise](/security-command-center/docs/security-command-center-overview) [Resource Manager](/resource-manager/docs) |
| Logging, auditing, and monitoring | Analyze logs to identify potential threats. Track and record system activities for compliance and security analysis. | [Cloud Logging](/logging/docs/overview) [Cloud Monitoring](/monitoring/docs/monitoring-overview) [Cloud Audit Logs](/logging/docs/audit) [VPC Flow Logs](/vpc/docs/flow-logs) |

## Contributors

Authors:
 [Wade Holmes](https://www.linkedin.com/in/wholmes) | Global Solutions Director[Hector Diaz](https://www.linkedin.com/in/hectorgdiaz) | Cloud Security ArchitectCarlos Leonardo Rosario | Google Cloud Security Specialist[John Bacon](https://www.linkedin.com/in/johnbac/) | Partner Solutions Architect[Sachin Kalra](http://www.linkedin.com/in/thesachinkalra) | Global Security Solution Manager

Other contributors:
 [Anton Chuvakin](https://www.linkedin.com/in/chuvakin/) | Security Advisor, Office of the CISO[Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect[Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist[Gary Harmson](https://www.linkedin.com/in/garyharmson) | Principal Architect[Gino Pelliccia](https://www.linkedin.com/in/gino-pelliccia-13637025) | Principal Architect[Jose Andrade](https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist[Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer[Laura Hyatt](https://www.linkedin.com/in/laura-hyatt) | Customer Engineer, FSI[Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer[Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist[Noah McDonald](https://www.linkedin.com/in/noah-mcdonald-77b04a173) | Cloud Security Consultant[Osvaldo Costa](https://www.linkedin.com/in/osvaldocostajr) | Networking Specialist Customer Engineer[Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework[Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer[Susan Wu](https://www.linkedin.com/in/susanwu88) | Outbound Product Manager

---

> 原页面：https://docs.cloud.google.com/architecture/framework/security（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
