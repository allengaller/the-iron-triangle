<!-- source: https://docs.cloud.google.com/architecture/framework/cost-optimization -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Well-Architected Framework: Cost optimization pillar

The cost optimization pillar in the
[Google Cloud Well-Architected Framework](/architecture/framework) 
describes principles and recommendations to optimize the cost of your workloads
in Google Cloud.

The intended audience includes the following:

- CTOs, CIOs, CFOs, and other executives who are responsible for strategic
cost management.
- Architects, developers, administrators, and operators who make decisions
that affect cost at all the stages of an organization's cloud journey.

The cost models for on-premises and cloud workloads differ significantly.
On-premises IT costs include capital expenditure (CapEx) and operational
expenditure (OpEx). On-premises hardware and software assets are acquired and
the acquisition costs are
[depreciated](https://en.wikipedia.org/wiki/Depreciation) 
over the operating life of the assets. In the cloud, the costs for most cloud
resources are treated as OpEx, where costs are incurred when the cloud resources
are consumed. This fundamental difference underscores the importance of the
following core principles of cost optimization.

For cost optimization principles and recommendations that are specific to AI and ML workloads, see
[AI and ML perspective: Cost optimization](/architecture/framework/perspectives/ai-ml/cost-optimization)
in the Well-Architected Framework.

## Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and
recommendations in this pillar, use the
[google-cloud-waf-cost-optimization](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-cost-optimization)
skill, which is available in the Google Agent Skills repository in GitHub.

To install the skill, run the following command in your agent's client or
terminal:

```
npx
 
skills
 
add
 
google/skills
 
--skill
 
google-cloud-waf-cost-optimization
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

The recommendations in the cost optimization pillar of the Well-Architected Framework
are mapped to the following core principles:

- [Align cloud spending with business
value](/architecture/framework/cost-optimization/align-cloud-spending-business-value):
Ensure that your cloud resources deliver measurable business value by
aligning IT spending with business objectives.
- [Foster a culture of cost
awareness](/architecture/framework/cost-optimization/foster-culture-cost-awareness):
Ensure that people across your organization consider the cost impact of
their decisions and activities, and ensure that they have access to the cost
information required to make informed decisions.
- [Optimize resource
usage](/architecture/framework/cost-optimization/optimize-resource-usage):
Provision only the resources that you need, and pay only for the resources
that you consume.
- [Optimize
continuously](/architecture/framework/cost-optimization/optimize-continuously):
Continuously monitor your cloud resource usage and costs, and proactively
make adjustments as needed to optimize your spending. This approach involves
identifying and addressing potential cost inefficiencies before they become
significant problems.

These principles are closely aligned with the core tenets of
[cloud FinOps](https://cloud.google.com/learn/what-is-finops).
FinOps is relevant to any organization, regardless of its size or maturity in
the cloud. By adopting these principles and following the related
recommendations, you can control and optimize costs throughout your journey in
the cloud.

## Contributors

Author: [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist

Other contributors:
 [Anuradha Bajpai](https://www.linkedin.com/in/anuradhabajpai) | Solutions Architect[Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect[Eric Lam](https://www.linkedin.com/in/ericlam) | Head of Google Cloud FinOps[Fernando Rubbo](https://www.linkedin.com/in/fernandorubbo) | Cloud Solutions Architect[Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist[Gary Harmson](https://www.linkedin.com/in/garyharmson) | Principal Architect[Jose Andrade](https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist[Kent Hua](https://www.linkedin.com/in/kenthua) | Solutions Manager[Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer[Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer[Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework[Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer[Steve McGhee](https://www.linkedin.com/in/stevemcghee) | Reliability Advocate[Sergei Lilichenko](https://www.linkedin.com/in/sergei-lilichenko) | Solutions Architect[Wade Holmes](https://www.linkedin.com/in/wholmes) | Global Solutions Director[Zach Seils](https://www.linkedin.com/in/zachseils) | Networking Specialist

---

> 原页面：https://docs.cloud.google.com/architecture/framework/cost-optimization（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
