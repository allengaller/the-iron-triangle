<!-- source: https://docs.cloud.google.com/architecture/framework/performance-optimization -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Well-Architected Framework: Performance optimization pillar

This pillar in the
[Google Cloud Well-Architected Framework](/architecture/framework) 
provides recommendations to optimize the performance of workloads in
Google Cloud.

This document is intended for architects, developers, and administrators who
plan, design, deploy, and manage workloads in Google Cloud.

The recommendations in this pillar can help your organization to operate
efficiently, improve customer satisfaction, increase revenue, and reduce cost.
For example, when the backend processing time of an application decreases, users
experience faster response times, which can lead to higher user retention and
more revenue.

The performance optimization process can involve a trade-off between
performance and cost. However, optimizing performance can sometimes help you
reduce costs. For example, when the load increases, autoscaling can help to
provide predictable performance by ensuring that the system resources aren't
overloaded. Autoscaling also helps you to reduce costs by removing unused
resources during periods of low load.

Performance optimization is a continuous process, not a one-time activity. The
following diagram shows the stages in the performance optimization process:

The performance optimization process is an ongoing cycle that includes the
following stages:

1. **Define requirements**: Define granular performance requirements for
each layer of the application stack before you design and develop your
applications. To plan
resource allocation, consider the key workload characteristics and performance
expectations.
2. **Design and deploy**: Use elastic and scalable design patterns that can
help you meet your performance requirements.
3. **Monitor and analyze**: Monitor performance continually by using logs,
tracing, metrics, and alerts.
4. **Optimize**: Consider potential redesigns as your applications evolve.
Rightsize cloud resources and use new features to meet changing performance
requirements.
As shown in the preceding diagram, continue the cycle of monitoring,
re-assessing requirements, and adjusting the cloud resources.

For performance optimization principles and recommendations that are specific to AI and ML workloads, see
[AI and ML perspective: Performance optimization](/architecture/framework/perspectives/ai-ml/performance-optimization)
in the Well-Architected Framework.

## Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and
recommendations in this pillar, use the
[google-cloud-waf-performance-optimization](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-performance-optimization)
skill, which is available in the Google Agent Skills repository in GitHub.

To install the skill, run the following command in your agent's client or
terminal:

```
npx
 
skills
 
add
 
google/skills
 
--skill
 
google-cloud-waf-performance-optimization
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

The recommendations in the performance optimization pillar of the Well-Architected Framework
are mapped to the following core principles:

- [Plan resource allocation](/architecture/framework/performance-optimization/plan-resource-allocation)
- [Take advantage of elasticity](/architecture/framework/performance-optimization/elasticity)
- [Promote modular design](/architecture/framework/performance-optimization/promote-modular-design)
- [Continuously monitor and improve performance](/architecture/framework/performance-optimization/continuously-monitor-and-improve-performance)

## Contributors

Authors:
 [Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect[Gary Harmson](https://www.linkedin.com/in/garyharmson) | Principal Architect[Luis Urena](https://www.linkedin.com/in/urena-luis) | Developer Relations Engineer[Zach Seils](https://www.linkedin.com/in/zachseils) | Networking Specialist

Other contributors:
 [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist[Jose Andrade](https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist[Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer[Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer[Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist[Ryan Cox](https://www.linkedin.com/in/ryanlcox) | Principal Architect[Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework[Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer[Wade Holmes](https://www.linkedin.com/in/wholmes) | Global Solutions Director

---

> 原页面：https://docs.cloud.google.com/architecture/framework/performance-optimization（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
