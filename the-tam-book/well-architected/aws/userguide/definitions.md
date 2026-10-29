<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/definitions.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# AWS Well-Architected glossary

AWS Well-Architected Agent is in preview release and is subject to change.


The following defines common terms used in AWS Well-Architected Tool, AWS Well-Architected Agent, and the AWS
 Well-Architected Framework.

## AWS Well-Architected Agent terms

The primary entity that defines the scope, goals, and cross-account
 configuration for recommendation generation. A profile specifies which
 AWS accounts to analyze, which AWS Regions to scan, which
 optimization pillars to focus on, and what business goals to prioritize.
 Each profile is scoped to a single AWS account and
 AWS Region.

The output of the AWS Well-Architected Agent analysis system. Each recommendation
 contains a title, description, impact assessment, trade-offs, guided
 actions, and remediation steps. A recommendation has a lifecycle with
 three states: active, completed, and suppressed.

The scope level of a recommendation. AWS Well-Architected Agent generates three
 types: Resource (targets a specific AWS resource), Application (spans
 multiple related resources within a discovered application), and
 Architecture (generated from IaC template analysis).

An optimization dimension that AWS Well-Architected Agent analyzes. The available
 pillars are: Cost optimization, Security, Resilience, and
 Performance.

A natural language business objective associated with a pillar. Goals
 drive recommendation prioritization and ranking. Each goal consists of a
 goal statement and a target pillar. For best results, goals should be
 specific, measurable, and time-bound.

An AWS Identity and Access Management role in the profile account that AWS Well-Architected Agent assumes to
 orchestrate resource discovery across your configured accounts. The
 execution role must trust the
 `wellarchitected.amazonaws.com` service principal and
 have permission to assume access roles in target accounts.

An IAM role deployed in each target AWS account that you want
 AWS Well-Architected Agent to analyze. The access role grants AWS Well-Architected Agent read-only
 permissions to discover and analyze resources in that account.

The process of producing recommendations. Generation can be proactive
 (running automatically on a recurring schedule) or on-demand (triggered
 by you, such as for architecture reviews).

A saved filter configuration that controls which recommendations
 appear when listing. Views filter by pillar, service, goal, account, and
 region. Views are sharable across users in the same AWS account and do
 not affect which recommendations are generated.

Additional customer-provided data that informs recommendation
 generation. Context can include IaC templates, custom best practices
 (uploaded as CSV), and other supplemental information.

Actionable steps to implement a recommendation. Remediation can be
 SSM Runbook automation (for recommendations derived from AWS Trusted Advisor
 checks) or guided actions (AI-generated step-by-step instructions for
 console, AWS CLI, SDK, or IaC implementation).

## AWS Well-Architected Tool terms

A collection of business-context questions and answers that you attach to workloads.
 Profiles prioritize the review questions and improvement plan risks that are most relevant
 to your business. AWS WA Tool profiles are unrelated to AWS WA Agent profiles.

A set of components that deliver business value. The workload is
 usually the level of detail that business and technology leaders
 communicate about. Examples include marketing websites, ecommerce
 websites, the backend for a mobile app, and analytic platforms.
 Workloads vary in architectural complexity from a static website to
 microservices architectures with multiple data stores.

A marker for key changes in your architecture as it evolves
 throughout the product lifecycle: design, testing, go live, and
 production.

A way for you to consistently measure your architectures against
 best practices and identify areas for improvement. In addition to the
 lenses provided by AWS, you can create and use your own lenses, or
 use lenses that have been shared with you.

An architectural or operational choice that AWS has found might
 result in significant negative impact to a business. HRIs might affect
 organizational operations, assets, and individuals.

An architectural or operational choice that AWS has found might
 negatively impact business, but to a lesser extent than HRIs.

For additional information, see [High Risk Issues (HRIs) and Medium Risk Issues (MRIs)](./workloads.html#wat-hri-mri).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/definitions.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
