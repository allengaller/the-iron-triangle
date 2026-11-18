<!-- source: https://docs.cloud.google.com/architecture/framework/reliability -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Well-Architected Framework: Reliability pillar

The reliability pillar in the
[Google Cloud Well-Architected Framework](/architecture/framework) 
provides principles and recommendations to help you design, deploy, and manage
reliable workloads in Google Cloud.

This document is intended for cloud architects, developers, platform engineers,
administrators, and site reliability engineers.

*Reliability* is a system's ability to consistently perform its intended
functions within the defined conditions and maintain uninterrupted service. Best
practices for reliability include redundancy, fault-tolerant design, monitoring,
and automated recovery processes.

As a part of reliability, *resilience* is the system's ability to withstand and
recover from failures or unexpected disruptions, while maintaining performance.
Google Cloud features, like
[multi-regional deployments](/architecture/deployment-archetypes/multiregional),
automated backups, and disaster recovery solutions, can help you improve your
system's resilience.

Reliability is important to your cloud strategy for many reasons, including the
following:

- **Minimal downtime**: Downtime can lead to lost revenue, decreased
productivity, and damage to reputation. Resilient architectures can help
ensure that systems can continue to function during failures or recover
efficiently from failures.
- **Enhanced user experience**: Users expect seamless interactions with
technology. Resilient systems can help maintain consistent performance and
availability, and they provide reliable service even during high demand or
unexpected issues.
- **Data integrity**: Failures can cause data loss or data corruption.
Resilient systems implement mechanisms such as backups, redundancy, and
replication to protect data and ensure that it remains accurate and accessible.
- **Business continuity**: Your business relies on technology for critical
operations. Resilient architectures can help ensure continuity after a
catastrophic failure, which enables business functions to continue without
significant interruptions and supports a swift recovery.
- **Compliance**: Many industries have regulatory requirements for system
availability and data protection. Resilient architectures can help you to
meet these standards by ensuring systems remain operational and secure.
- **Lower long-term costs**: Resilient architectures require upfront
investment, but resiliency can help to reduce costs over time by preventing
expensive downtime, avoiding reactive fixes, and enabling more efficient
resource use.

## Organizational mindset

To make your systems reliable, you need a plan and an established strategy.
This strategy must include education and the authority to prioritize reliability
alongside other initiatives.

Set a clear expectation that the entire organization is responsible for
reliability, including development, product management, operations, platform
engineering, and
[site reliability engineering (SRE)](https://cloud.google.com/sre).
Even the business-focused groups, like marketing and sales, can influence
reliability.

Every team must understand the reliability targets and risks of their
applications. The teams must be accountable to these requirements. Conflicts
between reliability and regular product feature development must be prioritized
and escalated accordingly.

Plan and manage reliability holistically, across all your functions and teams.
Consider setting up a Cloud Centre of Excellence (CCoE) that includes a
reliability pillar. For more information, see
[Optimize your organization's cloud journey with a Cloud Center of Excellence](https://cloud.google.com/blog/topics/training-certifications/optimize-your-organizations-cloud-journey-with-a-cloud-center-of-excellence).

## Focus areas for reliability

The activities that you perform to design, deploy, and manage a reliable system
can be categorized in the following focus areas. Each of the reliability
principles and recommendations in this pillar is relevant to one of these focus
areas.

- **Scoping**: To understand your system, conduct a detailed analysis of
its architecture. You need to understand the components, how they work and
interact, how data and actions flow through the system, and what could go
wrong. Identify potential failures, bottlenecks, and risks, which helps you
to take actions to mitigate those issues.
- **Observation**: To help prevent system failures, implement
comprehensive and continuous observation and monitoring. Through this
observation, you can understand trends and identify potential problems
proactively.
- **Response**: To reduce the impact of failures, respond appropriately
and recover efficiently. Automated responses can also help reduce the
impact of failures. Even with planning and controls, failures can still occur.
- **Learning**: To help prevent failures from recurring, learn from each
experience, and take appropriate actions.

## Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and
recommendations in this pillar, use the
[google-cloud-waf-reliability](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-reliability)
skill, which is available in the Google Agent Skills repository in GitHub.

To install the skill, run the following command in your agent's client or
terminal:

```
npx
 
skills
 
add
 
google/skills
 
--skill
 
google-cloud-waf-reliability
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

The recommendations in the reliability pillar of the Well-Architected Framework are
mapped to the following core principles:

- [Define reliability based on user-experience goals](/architecture/framework/reliability/define-reliability-based-on-user-experience-goals)
- [Set realistic targets for reliability](/architecture/framework/reliability/set-targets)
- [Build highly available systems through resource redundancy](/architecture/framework/reliability/build-highly-available-systems)
- [Take advantage of horizontal scalability](/architecture/framework/reliability/horizontal-scalability)
- [Detect potential failures by using observability](/architecture/framework/reliability/observability)
- [Design for graceful degradation](/architecture/framework/reliability/graceful-degradation)
- [Perform testing for recovery from failures](/architecture/framework/reliability/perform-testing-for-recovery-from-failures)
- [Perform testing for recovery from data loss](/architecture/framework/reliability/perform-testing-for-recovery-from-data-loss)
- [Conduct thorough postmortems](/architecture/framework/reliability/conduct-postmortems)

## Contributors

Authors:
 [Laura Hyatt](https://www.linkedin.com/in/laura-hyatt) | Customer Engineer, FSI[Jose Andrade](https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist[Gino Pelliccia](https://www.linkedin.com/in/gino-pelliccia-13637025) | Principal Architect

Other contributors:
 [Andrés-Leonardo Martínez-Ortiz](https://www.linkedin.com/in/almo) | Technical Program Manager[Brian Kudzia](https://www.linkedin.com/in/brian-kudzia-3061558) | Enterprise Infrastructure Customer Engineer[Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect[Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist[Gary Harmson](https://www.linkedin.com/in/garyharmson) | Principal Architect[Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer[Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer[Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist[Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework[Ryan Cox](https://www.linkedin.com/in/ryanlcox) | Principal Architect[Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer[Wade Holmes](https://www.linkedin.com/in/wholmes) | Global Solutions Director[Zach Seils](https://www.linkedin.com/in/zachseils) | Networking Specialist

---

> 原页面：https://docs.cloud.google.com/architecture/framework/reliability（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
