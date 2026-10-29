<!-- source: https://docs.cloud.google.com/architecture/framework/security/use-ai-securely-and-responsibly -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Use AI securely and responsibly

# Use AI securely and responsibly Stay organized with collections Save and categorize content based on your preferences.

This principle in the security pillar of the
[Google Cloud Well-Architected Framework](/architecture/framework) 
provides recommendations to help you secure your AI systems. These
recommendations are aligned with Google's
[Secure AI Framework (SAIF)](https://safety.google/cybersecurity-advancements/saif/),
which provides a practical approach to address the security and risk concerns of
AI systems. SAIF is a conceptual framework that aims to provide industry-wide
standards for building and deploying AI responsibly.

## Principle overview

To help ensure that your AI systems meet your security, privacy, and compliance
requirements, you must adopt a holistic strategy that starts with the initial
design and extends to deployment and operations. You can implement this holistic
strategy by applying the
[six core elements of SAIF](https://developers.google.com/machine-learning/resources/saif).

Google uses AI to enhance security measures, such as identifying threats,
automating security tasks, and improving detection capabilities, while keeping
humans in the loop for critical decisions.

Google emphasizes a collaborative approach to advancing AI security. This
approach involves partnering with customers, industries, and governments to
enhance the SAIF guidelines and offer practical, actionable resources.

The recommendations to implement this principle are grouped within the
following sections:

- [Recommendations to use AI securely](#recommendations_to_use_ai_securely)
- [Recommendations for AI governance](#recommendations_for_ai_governance)

## Recommendations to use AI securely

To use AI securely, you need both foundational security controls and
AI-specific security controls. This section provides an overview of
recommendations to ensure that your AI and ML deployments meet the security,
privacy, and compliance requirements of your organization.

For an overview of architectural principles and recommendations that are specific to AI
and ML workloads in Google Cloud, see the
[AI and ML perspective](/architecture/framework/perspectives/ai-ml)
in the Well-Architected Framework.

### Define clear goals and requirements for AI usage

This recommendation is relevant to the following
[focus areas](/architecture/framework/security#focus_areas_of_cloud_security):

- Cloud governance, risk, and compliance
- AI and ML security

This recommendation aligns with the SAIF element about contextualizing AI
system risks in the surrounding business processes. When you design and evolve
AI systems, it's important to understand your specific business goals, risks, and
compliance requirements.

### Keep data secure and prevent loss or mishandling

This recommendation is relevant to the following
[focus areas](/architecture/framework/security#focus_areas_of_cloud_security):

- Infrastructure security
- Identity and access management
- Data security
- Application security
- AI and ML security

This recommendation aligns with the following SAIF elements:

- Expand strong security foundations to the AI ecosystem. This element
includes data collection, storage, access control, and protection against
data poisoning.
- Contextualize AI system risks. Emphasize data security to support
business objectives and compliance.

### Keep AI pipelines secure and robust against tampering

This recommendation is relevant to the following
[focus areas](/architecture/framework/security#focus_areas_of_cloud_security):

- Infrastructure security
- Identity and access management
- Data security
- Application security
- AI and ML security

This recommendation aligns with the following SAIF elements:

- Expand strong security foundations to the AI ecosystem. As a key
element of establishing a secure AI system, secure your code and model
artifacts.
- Adapt controls for faster feedback loops. Because it's important for
mitigation and incident response, track your assets and pipeline runs.

### Deploy apps on secure systems using secure tools and artifacts

This recommendation is relevant to the following
[focus areas](/architecture/framework/security#focus_areas_of_cloud_security):

- Infrastructure security
- Identity and access management
- Data security
- Application security
- AI and ML security

Using secure systems and validated tools and artifacts in AI-based applications
aligns with the SAIF element about expanding strong security foundations to the
AI ecosystem and supply chain. This recommendation can be addressed through the
following steps:

- Implement a secure environment for ML training and deployment
- Use validated container images
- Apply
[Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev) 
guidelines

### Protect and monitor inputs

This recommendation is relevant to the following
[focus areas](/architecture/framework/security#focus_areas_of_cloud_security):

- Logging, auditing, and monitoring
- Security operations
- AI and ML security

This recommendation aligns with the SAIF element about extending detection and
response to bring AI into an organization's threat universe. To prevent issues,
it's critical to manage prompts for generative AI systems, monitor inputs, and
control user access.

## Recommendations for AI governance

All of the recommendations in this section are relevant to the following
[focus area](/architecture/framework/security#focus_areas_of_cloud_security):
Cloud governance, risk, and compliance.

Google Cloud offers a robust set of tools and services that you can use
to build responsible and ethical AI systems. We also offer a framework of
policies, procedures, and ethical considerations that can guide the development,
deployment, and use of AI systems.

As reflected in our recommendations, Google's approach for AI governance is
guided by the following principles:

- Fairness
- Transparency
- Accountability
- Privacy
- Security

### Use fairness indicators

[Gemini Enterprise Agent Platform](/gemini-enterprise-agent-platform/machine-learning) 
can detect bias during the data collection or post-training evaluation process.
Agent Platform provides
[model evaluation metrics](/gemini-enterprise-agent-platform/machine-learning/evaluation/intro-evaluation-fairness) 
like *data bias* and *model bias* to help you evaluate your model for bias.

These metrics are related to fairness across different categories like race,
gender, and class. However, interpreting statistical deviations isn't a
straightforward exercise, because differences across categories might not be a
result of bias or a signal of harm.

### Use Vertex Explainable AI

To understand how the AI models make decisions, use Vertex Explainable AI. This
feature helps you to identify potential biases that might be hidden in the
model's logic.

This explainability feature is integrated with
[BigQuery ML](/bigquery/docs/xai-overview) 
and
[Vertex Explainable AI](/vertex-ai/docs/explainable-ai/overview),
which provide feature-based explanations. You can either perform explainability
in BigQuery ML or
[register your model](/bigquery/docs/managing-models-vertex#register_models) 
in Agent Platform and perform explainability in
Agent Platform.

### Track data lineage

Track the origin and transformation of data that's used in your AI systems.
This tracking helps you understand the data's journey and identify potential
sources of bias or error.

[Data lineage](/knowledge-catalog/docs/about-data-lineage) 
is a Knowledge Catalog feature that lets you track how data moves through your
systems: where it comes from, where it's passed to, and what transformations are
applied to it.

### Establish accountability

Establish clear responsibility for the development, deployment, and outcomes of
your AI systems.

Use
[Cloud Logging](/logging/docs/overview) 
to log key events and decisions made by your AI systems. The logs provide an
audit trail to help you understand how the system is performing and identify
areas for improvement.

Use
[Error Reporting](/error-reporting/docs/grouping-errors) 
to systematically analyze errors made by the AI systems. This analysis can
reveal patterns that point to underlying biases or areas where the model needs
further refinement.

### Implement differential privacy

During model training,
[add noise](/bigquery/docs/differential-privacy#add_noise) 
to the data in order to make it difficult to identify individual data points but
still enable the model to learn effectively. With
[SQL in BigQuery](/bigquery/docs/introduction-sql),
you can transform the results of a query with differentially private
[aggregations](/bigquery/docs/differential-privacy).

---

> 原页面：https://docs.cloud.google.com/architecture/framework/security/use-ai-securely-and-responsibly（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
