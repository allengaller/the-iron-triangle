<!-- source: https://docs.cloud.google.com/architecture/framework/operational-excellence -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Well-Architected Framework: Operational excellence pillar

The operational excellence pillar in the
[Google Cloud Well-Architected Framework](/architecture/framework) 
provides recommendations to operate workloads efficiently on Google Cloud.
Operational excellence in the cloud involves designing, implementing, and
managing cloud solutions that provide value, performance, security, and
reliability. The recommendations in this pillar help you to continuously improve
and adapt workloads to meet the dynamic and ever-evolving needs in the cloud.

The operational excellence pillar is relevant to the following audiences:

- **Managers and leaders**: A framework to establish and maintain
operational excellence in the cloud and to ensure that cloud investments
deliver value and support business objectives.
- **Cloud operations teams**: Guidance to manage incidents and problems,
plan capacity, optimize performance, and manage change.
- **Site reliability engineers (SREs)**: Best practices that help you to
achieve high levels of service reliability, including monitoring, incident
response, and automation.
- **Cloud architects and engineers**: Operational requirements and best
practices for the design and implementation phases, to help ensure that
solutions are designed for operational efficiency and scalability.
- **DevOps teams**: Guidance about automation, CI/CD pipelines, and change
management, to help enable faster and more reliable software delivery.

To achieve operational excellence, you should embrace automation,
orchestration, and data-driven insights. Automation helps to eliminate toil. It
also streamlines and builds guardrails around repetitive tasks. Orchestration
helps to coordinate complex processes. Data-driven insights enable
evidence-based decision-making. By using these practices, you can optimize cloud
operations, reduce costs, improve service availability, and enhance security.

Operational excellence in the cloud goes beyond technical proficiency in cloud
operations. It includes a cultural shift that encourages continuous learning and
experimentation. Teams must be empowered to innovate, iterate, and adopt a
growth mindset. A culture of operational excellence fosters a collaborative
environment where individuals are encouraged to share ideas, challenge
assumptions, and drive improvement.

For operational excellence principles and recommendations that are specific to AI and ML workloads, see
[AI and ML perspective: Operational excellence](/architecture/framework/perspectives/ai-ml/operational-excellence)
in the Well-Architected Framework.

## Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and
recommendations in this pillar, use the
[google-cloud-waf-operational-excellence](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-operational-excellence)
skill, which is available in the Google Agent Skills repository in GitHub.

To install the skill, run the following command in your agent's client or
terminal:

```
npx
 
skills
 
add
 
google/skills
 
--skill
 
google-cloud-waf-operational-excellence
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

The recommendations in the operational excellence pillar of the Well-Architected Framework
are mapped to the following core principles:

- [Ensure operational readiness and performance using CloudOps](/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops):
Ensure that cloud solutions meet operational and performance requirements
by defining service level objectives (SLOs) and by performing comprehensive
monitoring, performance testing, and capacity planning.
- [Manage incidents and problems](/architecture/framework/operational-excellence/manage-incidents-and-problems):
Minimize the impact of cloud incidents and prevent recurrence through
comprehensive observability, clear incident response procedures, thorough
retrospectives, and preventive measures.
- [Manage and optimize cloud resources](/architecture/framework/operational-excellence/manage-and-optimize-cloud-resources):
Optimize and manage cloud resources through strategies like right-sizing,
autoscaling, and by using effective cost monitoring tools.
- [Automate and manage change](/architecture/framework/operational-excellence/automate-and-manage-change):
Automate processes, streamline change management, and alleviate the burden
of manual labor.
- [Continuously improve and innovate](/architecture/framework/operational-excellence/continuously-improve-and-innovate):
Focus on ongoing enhancements and the introduction of new solutions to stay
competitive.

## Contributors

Authors:
 [Alex Stepney](https://www.linkedin.com/in/alexstepney/) | Lead Principal Architect[Ryan Cox](https://www.linkedin.com/in/ryanlcox) | Principal Architect[Hadrian Knotz](https://www.linkedin.com/in/hadrianknotz) | Enterprise Architect

Other contributors:
 [Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect[Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist[Gary Harmson](https://www.linkedin.com/in/garyharmson) | Principal Architect[Jose Andrade](https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist[Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer[Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist[Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework[Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer[Zach Seils](https://www.linkedin.com/in/zachseils) | Networking Specialist[Wade Holmes](https://www.linkedin.com/in/wholmes) | Global Solutions Director

---

> 原页面：https://docs.cloud.google.com/architecture/framework/operational-excellence（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
