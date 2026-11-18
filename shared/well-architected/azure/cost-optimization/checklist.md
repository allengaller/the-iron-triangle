<!-- source: https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/checklist -->
<!-- captured: 2026-10-25 -->
<!-- vendor: azure -->

# Design review checklist for Cost Optimization

Note




This checklist presents a set of recommendations about cost optimization for your workload to help you achieve a high return on investment (ROI) based on the business value that your workload delivers. Cost optimization balances actual costs versus perceived value, team efficiency, focus, and effort, while meeting the defined functional and nonfunctional requirements of your workload.

Every workload has direct and indirect costs, and every workload is designed to deliver value. If you don't incorporate the recommendations in this article and consider the tradeoffs, your design might not make the best use of your time and money. Carefully consider the points covered in the following checklist to instill confidence in your design's success.

Cost optimization is a continuous process in which you optimize workload costs and align your workload with the broader governance discipline of cost management. What's important today might not be important tomorrow. Technology choices or options and features that your platform offers today might be different. Learn from production and nonproduction environments, be aware of platform changes, and apply your findings to your workload and your workload's dependencies.

## Checklist

|  | Code | Recommendation |
| --- | --- | --- |
| ☐ | [CO:01](create-culture-financial-responsibility) | **Create a culture of financial responsibility.** Regularly train personnel so technical skills remain sharp. Foster creativity and spending accountability in the work environment. Invest in tooling and implementing automation. |
| ☐ | [CO:02](cost-model) | **Create and maintain a cost model.** A cost model should estimate the initial cost, run rates, and ongoing costs. Negotiate a budget that covers a cost model and has a buffer for unplanned spending. |
| ☐ | [CO:03](collect-review-cost-data) | **Collect and review cost data.** Data collection should capture daily costs. In cost reports, include incurred costs (metered), prepaid costs (amortized), trends, and forecasts. Stakeholders should regularly review spending against the budget and cost model. Automate alerts to trigger notifications at key thresholds and detect anomalies to indicate deviations from trend baselines. |
| ☐ | [CO:04](set-spending-guardrails) | **Set spending guardrails.** Guardrails should include release gates, governance policies, resource limits, and access controls. Prioritize platform automation over manual processes. |
| ☐ | [CO:05](get-best-rates) | **Get the best rates from providers.** You should find and use the best rates for cloud resources and licenses. Regularly review cost savings. Cost reviews should include regional pricing, pricing tiers, pricing models (consumption or commitment-based), license portability, corporate purchasing plans, and price sheets. |
| ☐ | [CO:06](align-usage-to-billing-increments) | **Align usage to billing increments.** You should understand billing increments (meters) and align resource usage to those increments. Modify the service to align with billing increments, or modify resource usage to align with billing increments. Consider using a proof-of-concept to validate billing knowledge and design choices for major cost drivers and to reveal ways to align billing and resource usage. |
| ☐ | [CO:07](optimize-component-costs) | **Optimize component costs.** Regularly remove or optimize legacy, unneeded, and underutilized workload components, including application features, platform features, and resources. |
| ☐ | [CO:08](optimize-environment-costs) | **Optimize environment costs.** Align spending to prioritize preproduction, production, operations, and disaster recovery environments. For each environment, consider the required availability, licensing, operating hours and conditions, and security. Nonproduction environments should emulate the production environment. Implement strategic tradeoffs into nonproduction environments. |
| ☐ | [CO:09](optimize-flow-costs) | **Optimize flow costs.** Align the cost of each flow with flow priority. When you prioritize flows, consider the features, functionality, and nonfunctional requirements of each flow. Optimizing flow spend often requires strategic compromises. |
| ☐ | [CO:10](optimize-data-costs) | **Optimize data costs.** Data spending with data priority. Data optimization should include improvements to data management (tiering and retention), volume, replication, backups, file formats, and storage solutions. |
| ☐ | [CO:11](optimize-code-costs) | **Optimize code costs.** Evaluate and modify code to meet functional and nonfunctional requirements with fewer or cheaper resources. |
| ☐ | [CO:12](optimize-scaling-costs) | **Optimize scaling costs.** Evaluate alternative scaling within your scale units. Consider alternative scaling configurations, and align with the cost model. Considerations should include utilization against the inherit limits of every instance, resource, and scale unit boundary. Use strategies for controlling demand and supply. |
| ☐ | [CO:13](optimize-personnel-time) | **Optimize personnel time.** Align the time personnel spends on tasks with the priority of the task. The goal is to reduce the time spent on tasks without degrading the outcome. Optimization efforts should include minimizing noise, reducing build times, high fidelity debugging, and production mocking. |
| ☐ | [CO:14](consolidation) | **Consolidate resources and responsibility.** Look within the workload for ways to consolidate resources and increase density. Outside the workload, use existing centralized resources and services that enable you to consolidate workload responsibilities. |

## Next steps

We recommend that you review the Cost Optimization tradeoffs to explore other concepts.

[Cost Optimization tradeoffs](tradeoffs)

## Feedback

Was this page helpful?

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

## Additional resources

- Last updated on 2023-11-15

---

> 原页面：https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/checklist（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
