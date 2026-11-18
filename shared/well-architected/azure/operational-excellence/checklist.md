<!-- source: https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/checklist -->
<!-- captured: 2026-10-25 -->
<!-- vendor: azure -->

# Design review checklist for Operational Excellence

Note




This checklist presents a set of recommendations to help you build a culture of operational excellence. Start with a DevOps approach to integrate specializations from multiple disciplines. This approach creates a rigorous design and development practice. This approach leads to repeatable, reliable, and safe deployments of infrastructure and code.

Prioritize human intervention in areas that benefit from it, and incorporate automation in other areas. Observability serves operational excellence by monitoring health events and also for validating the current workload design and implementation to inform future product development.

If you don't consider tradeoffs and recommendations for operational excellence, your workload might be at risk. Carefully consider the points covered in the following checklist to instill confidence in your design's success.

## Checklist

|  | Code | Recommendation |
| --- | --- | --- |
| ☐ | [OE:01](devops-culture) | **Define your standard practices to develop and operate your workload.** Align team members' specializations to clear practices for designing, deploying, and operating the workload. Establish accountability and create a culture that promotes continuous improvement and a blameless culture that supports learning. |
| ☐ | [OE:02](formalize-operations-tasks) | Use standardization as a way to make routine, ad-hoc, and emergency operations consistent and predictable. |
| ☐ | [OE:03](formalize-development-practices) | Formalize processes across the full software development lifecycle, from ideation to delivery, and make them transparent to the team and stakeholders. |
| ☐ | [OE:04](tools-processes) | **Enhance software development and quality assurance** by implementing industry-standard practices. Ensure clear role definitions and consistent processes by standardizing tools, source control, design patterns, documentation, and style guides. |
| ☐ | [OE:05](infrastructure-as-code-design) | **Use a standardized infrastructure as code (IaC) approach to prepare resources and configurations.** Use IaC to ensure consistent styles, modularization, and quality assurance. Prefer declarative over imperative approaches when practical. |
| ☐ | [OE:06](workload-supply-chain) | **Build a workload supply chain that drives changes** through predictable, automated pipelines. Ensure these pipelines test and promote changes across all environments and quality gates. Incorporate comprehensive testing. |
| ☐ | [OE:07](observability) [OE:07](instrument-application) | **Design a monitoring stack** that captures operational telemetry, metrics, and logs from the workload's infrastructure and code to validate design decisions and guide future improvements. |
| ☐ | [OE:08](incident-response) | **Establish a clear, structured incident management process** with defined roles, documented procedures, and architecture designed for rapid detection, diagnosis, and recovery. |
| ☐ | [OE:09](testing) | **Enhance the quality of your workload** by adopting testing practices that align with business objectives and uphold quality standards. |
| ☐ | [OE:10](enable-automation) | **Design automation to be reliable, secure, and maintainable** across the workload lifecycle. Automate repetitive, procedural tasks that deliver clear return on investment. |
| ☐ | [OE:11](safe-deployments) | **Clearly define your workload's safe deployment practices.** Focus on small, incremental releases with quality gates. Use modern deployment patterns and progressive exposure to manage risk. Plan for both routine and emergency deployments. |

## Next steps

We recommend that you review the Operational Excellence tradeoffs to explore other concepts.

[Operational Excellence tradeoffs](tradeoffs)

## Feedback

Was this page helpful?

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

## Additional resources

- Last updated on 2026-06-11

---

> 原页面：https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/checklist（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
