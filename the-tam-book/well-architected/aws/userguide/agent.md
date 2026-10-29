<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# What is AWS Well-Architected Agent (preview)?

AWS Well-Architected Agent is in preview release and is subject to change.


AWS Well-Architected Agent (AWS WA Agent) is an AI-powered cloud optimization service that continuously
 analyzes your AWS environment and delivers personalized, prioritized recommendations across
 cost, security, performance, and resilience. The service generates recommendations at three
 levels (resource, application, and architecture) with ready-to-deploy automation scripts so you
 can act immediately.

###### Important

Application-level recommendations are a new recommendation format currently in beta. We
 are actively seeking customer feedback to improve their quality and relevance. As with any
 AI-generated content, please thoroughly review each recommendation before taking any action
 based on it.

To set up AWS WA Agent and generate your first recommendations, see
 [Getting started with AWS Well-Architected Agent](./agent-getting-started.html).

AWS WA Agent is intended for both business leadership and technical teams. By tying recommendations
 to your stated business goals, it helps leadership and engineering teams align on technical
 remediation priorities derived from business objectives.

## Key capabilities

- **Automated analysis:** Unlike point-in-time architecture reviews, AWS WA Agent analyzes your environment on an ongoing
 schedule. Scheduled recommendations are refreshed on a weekly cadence.
- **Ready-to-deploy remediation:** Recommendations include prescriptive guidance and ready-to-implement fixes like updated IaC code, not only findings.
- **Goal-aligned prioritization:** Recommendations are ranked against the business goals you define. For more information,
 see [Goals and optimization pillars](./agent-concepts.html#agent-concept-goals).
- **Cross-pillar impacts:** Every recommendation shows how acting on the recommendation provides positive impact on the other pillars, alongside an impact category.
- **Trade-off analysis:** Each recommendation describes trade-offs that occur from implementing the recommendation, including pillar, risk level, and mitigation strategy.
- **Scale:** A single agent profile can analyze up to 100 AWS accounts and scan resources in all
 commercial AWS Regions. For limits, see [AWS Well-Architected Agent Quotas and limits](./agent-quotas.html).
- **Builds on existing AWS optimization services:** AWS WA Agent ingests findings from services such as AWS Trusted Advisor and adds personalization,
 goal-aligned prioritization, and automation-ready remediation. This reduces manual triage of
 optimization findings. For more information, see
 [Related services](./agent-related-services.html).

## How it works

1. Create an agent profile that defines your accounts, Regions, optimization pillars, and business
 goals.
2. AWS WA Agent scans the resources in your configured accounts.
3. AWS WA Agent generates prioritized recommendations at the resource, application, and architecture
 levels.
4. You review recommendations and deploy remediations using the provided guidance.

You can also run architecture reviews of IaC templates on demand. For more information, see
 [Conducting architecture reviews](./agent-architecture-reviews.html).

AWS WA Agent analyzes your infrastructure across four optimization pillars: cost optimization,
 security, resilience, and performance. For more information, see
 [AWS Well-Architected Agent Concepts and terminology](./agent-concepts.html).

## Accessing AWS WA Agent

- **AWS Well-Architected console:** AWS WA Agent is available from the AWS Well-Architected console. For a step-by-step
 walkthrough of setting up your first agent profile using the console, see
 [Getting started with AWS Well-Architected Agent](./agent-getting-started.html).
- **APIs:** Programmatic access is available through the `wellarchitected` service
 namespace. For a CLI-based setup walkthrough, see [API quickstart](./agent-api-quickstart.html). For available operations, see
 [API actions](./wa-api-actions.html). For complete API documentation, see the [AWS
 Well-Architected API Reference](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/Welcome.html).
- **AWS MCP Server:** An AI agent configured with the AWS MCP Server can run the
 AWS WA Agent `wellarchitected` API operations through your IAM credentials, as an
 alternative to running AWS CLI commands directly. For more detail, see
 [(Optional) API quickstart using the AWS MCP Server](./agent-api-quickstart.html#agent-api-mcp). To set up and connect the
 server, see [AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html).

## Availability

**Support plan eligibility:** AWS WA Agent is available to customers
 with an AWS Support plan at the Business+ tier or higher: Business+, Enterprise On-Ramp,
 Enterprise Support, or Unified Operations. Customers on Developer or Business tier plans do not
 have access to AWS WA Agent. For tier-specific entitlements, see
 [AWS Well-Architected Agent Quotas and limits](./agent-quotas.html).

**Region availability:** AWS WA Agent profiles are hosted in
 US East (N. Virginia), US East (Ohio), or US West (Oregon). From these hosting Regions,
 AWS WA Agent scans resources in all commercial AWS Regions. See
 [AWS Well-Architected Agent Quotas and limits](./agent-quotas.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
